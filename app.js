/* Quiz Kapow! — app logic (no dependencies, no build step).
   Question bank: data/index.json + data/questions/<chapter-id>.json  */
(function () {
  'use strict';

  var NCERT_URL = 'https://ncert-onestop.vercel.app';
  var TEAM_COLORS = ['#ffe600', '#00d2ff', '#ff9aa8', '#7be495', '#ffb35c', '#c9a3ff'];
  var KEYS = { settings: 'kapow:settings:v1', bests: 'kapow:bests:v1', sound: 'kapow:sound:v1' };
  var SUBJECT_ICONS = { English: '📖', Science: '🔬', Chemistry: '⚗️', Physics: '⚛️', Biology: '🧬', Mathematics: '📐', Maths: '📐', History: '🏛️', Geography: '🌍' };

  /* ---------------- helpers ---------------- */
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return [].slice.call((r || document).querySelectorAll(s)); }
  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function store(key, val) {
    try {
      if (val === undefined) { var raw = window.localStorage.getItem(key); return raw ? JSON.parse(raw) : null; }
      window.localStorage.setItem(key, JSON.stringify(val));
    } catch (e) { return null; }
    return null;
  }
  function pad2(n) { return n < 10 ? '0' + n : String(n); }
  function fmt(ms) { var s = Math.max(0, Math.ceil(ms / 1000)); return pad2(Math.floor(s / 60)) + ':' + pad2(s % 60); }
  function reduceMotion() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }

  var el = {};
  ['viewHome', 'viewQuiz', 'viewResult', 'classGrid', 'subjectGrid', 'chapterGrid', 'bookChips', 'stepper', 'pathBar', 'settings',
   'countChips', 'timeChips', 'teamGroup', 'teamCountChips', 'teamNames', 'pointsGroup', 'pointsChips', 'startBtn', 'startNote',
   'qzMode', 'qzChapter', 'qzCounter', 'qzFill', 'qCard', 'qBurst', 'qText', 'options', 'feedback', 'award', 'qActions',
   'timerCard', 'ringFg', 'timeText', 'timeLabel', 'sidePanel', 'stamp', 'quitDialog', 'toast', 'confetti', 'soundBtn',
   'heroStats', 'tickerTrack', 'qzFs', 'qzQuit', 'brandLink']
    .forEach(function (id) { el[id] = document.getElementById(id); });

  /* ---------------- state ---------------- */
  var chapters = [];
  var cache = {};
  var settings = Object.assign({ count: 10, seconds: 30, teams: 3, points: 10, names: [] }, store(KEYS.settings) || {});
  var soundOn = store(KEYS.sound) !== false;
  var sel = { cls: null, subject: null, book: 'all', chapter: null, mode: null };
  var step = 1;
  var game = null;

  /* ---------------- audio ---------------- */
  var actx = null;
  function beep(freq, dur, type, vol, delay) {
    if (!soundOn) return;
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      if (actx.state === 'suspended') actx.resume();
      var o = actx.createOscillator(), g = actx.createGain(), t0 = actx.currentTime + (delay || 0);
      o.type = type || 'sine'; o.frequency.setValueAtTime(freq, t0);
      g.gain.setValueAtTime(vol || 0.12, t0); g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      o.connect(g); g.connect(actx.destination); o.start(t0); o.stop(t0 + dur + 0.02);
    } catch (e) { /* audio unavailable */ }
  }
  var sfx = {
    click: function () { beep(620, 0.05, 'square', 0.05); },
    tick: function () { beep(900, 0.05, 'square', 0.07); },
    good: function () { [523, 659, 784, 1046].forEach(function (f, i) { beep(f, 0.16, 'triangle', 0.16, i * 0.09); }); },
    bad: function () { beep(180, 0.4, 'sawtooth', 0.14); beep(130, 0.4, 'sawtooth', 0.12, 0.12); },
    time: function () { beep(240, 0.6, 'square', 0.13); },
    win: function () { [523, 659, 784, 659, 784, 1046, 1318].forEach(function (f, i) { beep(f, 0.2, 'triangle', 0.16, i * 0.12); }); }
  };
  function syncSoundBtn() {
    el.soundBtn.textContent = soundOn ? '🔊' : '🔇';
    el.soundBtn.setAttribute('aria-pressed', String(soundOn));
    el.soundBtn.setAttribute('aria-label', soundOn ? 'Sound on' : 'Sound off');
  }
  function toggleSound() { soundOn = !soundOn; store(KEYS.sound, soundOn); syncSoundBtn(); sfx.click(); }

  /* ---------------- toast / stamp ---------------- */
  var toastTimer = 0, stampTimer = 0;
  function toast(msg) {
    el.toast.textContent = msg; el.toast.hidden = false; restart(el.toast, 'is-on');
    window.clearTimeout(toastTimer); toastTimer = window.setTimeout(function () { el.toast.hidden = true; }, 3200);
  }
  function stamp(text, good, ms) {
    el.stamp.textContent = text; el.stamp.hidden = false;
    el.stamp.className = 'stamp' + (good ? ' good' : ''); void el.stamp.offsetWidth; el.stamp.classList.add('is-on');
    window.clearTimeout(stampTimer); stampTimer = window.setTimeout(function () { el.stamp.hidden = true; }, ms || 1400);
  }

  /* ---------------- confetti ---------------- */
  var confettiRaf = 0;
  function confetti(ms) {
    if (reduceMotion()) return;
    var c = el.confetti, ctx = c.getContext('2d');
    c.width = window.innerWidth; c.height = window.innerHeight;
    var colors = ['#ffe600', '#00d2ff', '#ff2a55', '#22c55e', '#ff9aa8', '#000'];
    var parts = [];
    for (var i = 0; i < 160; i++) {
      parts.push({ x: Math.random() * c.width, y: -20 - Math.random() * c.height * 0.6, w: 6 + Math.random() * 8, h: 10 + Math.random() * 10,
        vx: -2 + Math.random() * 4, vy: 2 + Math.random() * 4, r: Math.random() * 6, vr: -0.2 + Math.random() * 0.4, c: colors[i % colors.length] });
    }
    var end = Date.now() + (ms || 3500);
    window.cancelAnimationFrame(confettiRaf);
    (function frame() {
      ctx.clearRect(0, 0, c.width, c.height);
      var alive = false;
      parts.forEach(function (p) {
        p.x += p.vx; p.y += p.vy; p.r += p.vr; p.vy += 0.03;
        if (p.y < c.height + 30) alive = true;
        ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r); ctx.fillStyle = p.c; ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.strokeStyle = '#000'; ctx.lineWidth = 1; ctx.strokeRect(-p.w / 2, -p.h / 2, p.w, p.h); ctx.restore();
      });
      if (alive && Date.now() < end + 2500) confettiRaf = window.requestAnimationFrame(frame);
      else ctx.clearRect(0, 0, c.width, c.height);
    })();
  }

  /* ---------------- data ---------------- */
  function loadIndex() {
    return fetch('data/index.json', { cache: 'no-cache' }).then(function (r) {
      if (!r.ok) throw new Error('index');
      return r.json();
    }).then(function (d) { chapters = (d.chapters || []).filter(function (c) { return c.count > 0; }); });
  }
  function loadChapter(c) {
    if (cache[c.id]) return Promise.resolve(cache[c.id]);
    return fetch(c.file).then(function (r) { if (!r.ok) throw new Error(c.id); return r.json(); })
      .then(function (d) { cache[c.id] = d; return d; });
  }
  function uniq(arr) { return arr.filter(function (v, i) { return arr.indexOf(v) === i; }); }
  function classList() { return uniq(chapters.map(function (c) { return String(c.class); })).sort(function (a, b) { return a - b; }); }
  function inClass(cls) { return chapters.filter(function (c) { return String(c.class) === cls; }); }
  function inSubject() { return inClass(sel.cls).filter(function (c) { return c.subject === sel.subject; }); }
  function sumQ(list) { return list.reduce(function (s, c) { return s + c.count; }, 0); }
  function bestFor(key) { var b = store(KEYS.bests) || {}; return b[key] || null; }

  /* ---------------- ticker + hero stats ---------------- */
  function buildTicker() {
    var items = ['<span>Solo practice · Classroom challenge · 4 options · Beat the timer</span>', '<span class="ticker-pop">KAPOW!</span>',
      '<span>Pick class → subject → chapter → mode → start!</span>', '<span class="ticker-pop cyan">BRAIN BLAST!</span>',
      '<span>Study notes &amp; summaries on NCERT One Stop</span>'].join('');
    el.tickerTrack.innerHTML = items + items;
  }
  function buildStats() {
    var subjects = uniq(chapters.map(function (c) { return c.subject; })).length;
    el.heroStats.innerHTML = '<li>' + classList().length + ' classes</li><li>' + subjects + ' subjects</li><li>' + chapters.length + ' chapters</li><li>' + sumQ(chapters) + ' questions</li>';
  }

  /* ---------------- views ---------------- */
  function showView(name) {
    el.viewHome.hidden = name !== 'home';
    el.viewQuiz.hidden = name !== 'quiz';
    el.viewResult.hidden = name !== 'result';
    document.body.dataset.view = name;
    window.scrollTo(0, 0);
  }

  /* ---------------- wizard ---------------- */
  function maxStep() { return !sel.cls ? 1 : !sel.subject ? 2 : !sel.chapter ? 3 : 4; }
  function renderWizard() {
    var max = maxStep();
    if (step > max) step = max;
    $$('.step').forEach(function (s) { s.hidden = Number(s.dataset.step) !== step; });
    $$('#stepper button').forEach(function (b) {
      var n = Number(b.dataset.goto);
      b.disabled = n > max;
      b.classList.toggle('is-active', n === step);
      b.classList.toggle('is-done', n < step);
    });
    var bits = [];
    if (sel.cls) bits.push('<span>Class ' + esc(sel.cls) + '</span>');
    if (sel.subject) bits.push('<span>' + esc(sel.subject) + '</span>');
    if (sel.chapter) bits.push('<span>' + esc(sel.chapter.title) + '</span>');
    if (sel.mode) bits.push('<span>' + (sel.mode === 'solo' ? 'Solo practice' : 'Classroom challenge') + '</span>');
    el.pathBar.hidden = !bits.length;
    el.pathBar.innerHTML = bits.length ? 'Your quiz: ' + bits.join('<i>→</i>') : '';
  }
  function goStep(n, scroll) {
    step = n;
    if (n <= 1) { sel.subject = null; sel.chapter = null; sel.mode = null; sel.book = 'all'; }
    if (n <= 2) { sel.chapter = null; sel.mode = null; sel.book = 'all'; }
    if (n <= 3) { sel.mode = null; }
    renderStep(n);
    renderWizard();
    if (scroll) { var w = document.getElementById('start'); if (w) w.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' }); }
  }
  function renderStep(n) {
    if (n === 1) renderClasses();
    else if (n === 2) renderSubjects();
    else if (n === 3) renderChapters();
    else renderMode();
  }

  function renderClasses() {
    el.classGrid.innerHTML = classList().map(function (c, i) {
      var list = inClass(c);
      return '<button type="button" class="pick class-card c' + (i % 4) + (sel.cls === c ? ' is-selected' : '') + '" data-class="' + esc(c) + '" style="--i:' + i + '">' +
        '<small>CLASS</small><strong>' + esc(c) + '</strong><span class="pill">' + list.length + ' chapters · ' + sumQ(list) + ' Qs</span></button>';
    }).join('');
  }
  function renderSubjects() {
    var subs = uniq(inClass(sel.cls).map(function (c) { return c.subject; }));
    el.subjectGrid.innerHTML = subs.map(function (s, i) {
      var list = inClass(sel.cls).filter(function (c) { return c.subject === s; });
      return '<button type="button" class="pick subject-card" data-subject="' + esc(s) + '" style="--i:' + i + '">' +
        '<span class="s-icon" aria-hidden="true">' + (SUBJECT_ICONS[s] || '📚') + '</span><strong>' + esc(s) + '</strong>' +
        '<span class="pill">' + list.length + ' chapters · ' + sumQ(list) + ' Qs</span></button>';
    }).join('');
  }
  function renderChapters() {
    var all = inSubject();
    var books = uniq(all.map(function (c) { return c.book; }));
    el.bookChips.hidden = books.length < 2;
    if (books.length > 1) {
      el.bookChips.innerHTML = ['all'].concat(books).map(function (b) {
        return '<button type="button" class="chip-btn" role="radio" aria-checked="' + (sel.book === b) + '" data-book="' + esc(b) + '">' + (b === 'all' ? 'All books' : esc(b)) + '</button>';
      }).join('');
    }
    var list = sel.book === 'all' ? all : all.filter(function (c) { return c.book === sel.book; });
    var mixedKey = 'mix:' + sel.cls + ':' + sel.subject + ':' + sel.book;
    var mb = bestFor(mixedKey);
    var html = '<button type="button" class="pick chapter-card mixed" data-chapter="__mixed" style="--i:0">' +
      '<div class="c-top"><span class="c-icon" aria-hidden="true">🎲</span><span class="c-label">MIXED</span></div>' +
      '<strong>Mixed blast — all ' + (sel.book === 'all' ? esc(sel.subject) : esc(sel.book)) + ' chapters</strong>' +
      '<div class="c-meta"><span class="pill">' + sumQ(list) + ' questions</span>' + (mb ? '<span class="pill best">Best ' + mb.pct + '%</span>' : '') + '</div></button>';
    html += list.map(function (c, i) {
      var b = bestFor(c.id);
      return '<button type="button" class="pick chapter-card" data-chapter="' + esc(c.id) + '" style="--i:' + (i + 1) + '">' +
        '<div class="c-top"><span class="c-icon" aria-hidden="true">' + esc(c.icon || '📖') + '</span><span class="c-label">' + esc(c.chapter || '') + '</span></div>' +
        '<strong>' + esc(c.title) + '</strong>' +
        '<div class="c-meta"><span class="pill">' + c.count + ' questions</span>' + (b ? '<span class="pill best">Best ' + b.pct + '%</span>' : '') + '</div></button>';
    }).join('');
    el.chapterGrid.innerHTML = html;
  }

  function availableQs() {
    return sel.chapter ? sel.chapter.count : 0;
  }
  function chip(label, val, on, extra) {
    return '<button type="button" class="chip-btn" role="radio" aria-checked="' + on + '" data-val="' + esc(val) + '"' + (extra || '') + '>' + label + '</button>';
  }
  function renderMode() {
    $$('.mode-card').forEach(function (b) { b.setAttribute('aria-pressed', String(sel.mode === b.dataset.mode)); });
    el.settings.hidden = !sel.mode;
    if (!sel.mode) return;
    var avail = availableQs();
    var counts = [5, 10, 15, 20].filter(function (n) { return n < avail; });
    var eff = (settings.count === 'all' || settings.count >= avail) ? 'all' : settings.count;
    el.countChips.innerHTML = counts.map(function (n) { return chip(n, n, eff === n); }).join('') +
      chip('All (' + avail + ')', 'all', eff === 'all');
    var times = [15, 20, 30, 45, 60, 0];
    el.timeChips.innerHTML = times.map(function (t) { return chip(t ? t + ' sec' : 'No timer', t, settings.seconds === t); }).join('');
    var isClass = sel.mode === 'class';
    el.teamGroup.hidden = !isClass; el.pointsGroup.hidden = !isClass;
    if (isClass) {
      el.teamCountChips.innerHTML = [2, 3, 4, 5, 6].map(function (n) { return chip(n + ' teams', n, settings.teams === n); }).join('');
      el.pointsChips.innerHTML = [5, 10, 20, 50].map(function (n) { return chip('+' + n, n, settings.points === n); }).join('');
      renderTeamNames();
    }
    el.startNote.textContent = isClass ? 'Teacher controls the timer, reveal and points. Press F for full screen.' : 'Tip: use keys 1–4 or A–D to answer fast.';
  }
  function renderTeamNames() {
    var html = '';
    for (var i = 0; i < settings.teams; i++) {
      var nm = settings.names[i] || 'Team ' + (i + 1);
      html += '<label style="--tc:' + TEAM_COLORS[i] + '"><span class="team-dot"></span><input type="text" maxlength="16" data-team="' + i + '" value="' + esc(nm) + '" aria-label="Team ' + (i + 1) + ' name"></label>';
    }
    el.teamNames.innerHTML = html;
  }
  function saveSettings() { store(KEYS.settings, settings); }

  /* wizard events */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-class],[data-subject],[data-chapter],[data-book],[data-mode],[data-goto],#countChips [data-val],#timeChips [data-val],#teamCountChips [data-val],#pointsChips [data-val]');
    if (!t) return;
    if (t.dataset.class) { sel.cls = t.dataset.class; sel.subject = null; sel.chapter = null; sel.mode = null; sfx.click(); step = 2; renderStep(2); renderWizard(); scrollWizard(); }
    else if (t.dataset.subject) { sel.subject = t.dataset.subject; sel.chapter = null; sel.mode = null; sel.book = 'all'; sfx.click(); step = 3; renderStep(3); renderWizard(); scrollWizard(); }
    else if (t.dataset.book) { sel.book = t.dataset.book; renderChapters(); }
    else if (t.dataset.chapter) {
      var list = sel.book === 'all' ? inSubject() : inSubject().filter(function (c) { return c.book === sel.book; });
      if (t.dataset.chapter === '__mixed') sel.chapter = { ids: list.map(function (c) { return c.id; }), title: 'Mixed — ' + (sel.book === 'all' ? sel.subject : sel.book), count: sumQ(list), key: 'mix:' + sel.cls + ':' + sel.subject + ':' + sel.book, mixed: true };
      else { var c = chapters.filter(function (x) { return x.id === t.dataset.chapter; })[0]; sel.chapter = { ids: [c.id], title: c.title, count: c.count, key: c.id }; }
      sel.mode = null; sfx.click(); step = 4; renderStep(4); renderWizard(); scrollWizard();
    }
    else if (t.dataset.mode) { sel.mode = t.dataset.mode; sfx.click(); renderMode(); renderWizard(); }
    else if (t.dataset.goto) { goStep(Number(t.dataset.goto), true); }
    else if (t.closest('#countChips')) { settings.count = t.dataset.val === 'all' ? 'all' : Number(t.dataset.val); saveSettings(); renderMode(); }
    else if (t.closest('#timeChips')) { settings.seconds = Number(t.dataset.val); saveSettings(); renderMode(); }
    else if (t.closest('#teamCountChips')) { settings.teams = Number(t.dataset.val); saveSettings(); renderMode(); }
    else if (t.closest('#pointsChips')) { settings.points = Number(t.dataset.val); saveSettings(); renderMode(); }
  });
  function scrollWizard() { var w = document.getElementById('start'); if (w) w.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' }); }
  el.teamNames.addEventListener('input', function (e) {
    var i = Number(e.target.dataset.team);
    if (isNaN(i)) return;
    settings.names[i] = e.target.value.trim() || 'Team ' + (i + 1);
    saveSettings();
  });
  document.getElementById('heroStart').addEventListener('click', function (e) { e.preventDefault(); scrollWizard(); });

  /* ---------------- game setup ---------------- */
  function buildQuestion(q, title) {
    var opts = shuffle(q.options.map(function (t, i) { return { t: t, c: i === q.answer }; }));
    return { q: q.q, opts: opts, ans: opts.findIndex(function (o) { return o.c; }), why: q.explanation || '', chapter: title };
  }
  function startGame() {
    var ids = sel.chapter.ids;
    el.startBtn.disabled = true; el.startBtn.textContent = 'Loading…';
    var list = ids.map(function (id) { return chapters.filter(function (c) { return c.id === id; })[0]; });
    Promise.all(list.map(loadChapter)).then(function (sets) {
      var pool = [];
      sets.forEach(function (d) { d.questions.forEach(function (q) { pool.push(buildQuestion(q, d.title)); }); });
      pool = shuffle(pool);
      var n = settings.count === 'all' ? pool.length : Math.min(settings.count, pool.length);
      launch(pool.slice(0, n));
    }).catch(function () { toast('Could not load questions. Check your connection and try again.'); })
      .then(function () { el.startBtn.disabled = false; el.startBtn.textContent = '▶ Start quiz!'; });
  }
  function reshuffleQs(qs) { return shuffle(qs.map(function (q) { var o = shuffle(q.opts); return { q: q.q, opts: o, ans: o.findIndex(function (x) { return x.c; }), why: q.why, chapter: q.chapter }; })); }

  function launch(qs) {
    var isClass = sel.mode === 'class';
    var teams = [];
    if (isClass) for (var i = 0; i < settings.teams; i++) teams.push({ name: settings.names[i] || 'Team ' + (i + 1), color: TEAM_COLORS[i], score: 0 });
    game = { mode: sel.mode, key: sel.chapter.key, title: sel.chapter.title, qs: qs, i: 0, seconds: settings.seconds, points: settings.points,
      state: 'asking', results: [], score: 0, streak: 0, bestStreak: 0, fifty: 2, hidden: [], teams: teams, awarded: [], qStart: 0 };
    el.viewQuiz.classList.toggle('is-class', isClass);
    el.qzMode.textContent = isClass ? 'Classroom challenge' : 'Solo practice';
    el.qzChapter.textContent = game.title;
    showView('quiz');
    sfx.click();
    showQuestion();
  }

  /* ---------------- timer ---------------- */
  var CIRC = 2 * Math.PI * 82;
  var T = { total: 0, remaining: 0, endAt: 0, running: false, paused: false, id: 0, lastSec: -1, onEnd: null };
  function timerStop() { window.clearInterval(T.id); T.running = false; }
  function timerStart(sec, onEnd) {
    timerStop();
    T.total = sec * 1000; T.remaining = T.total; T.paused = false; T.onEnd = onEnd; T.lastSec = -1;
    if (T.total > 0) { T.endAt = Date.now() + T.remaining; T.running = true; T.id = window.setInterval(timerTick, 100); }
    timerPaint();
  }
  function timerTick() {
    if (!T.running) return;
    T.remaining = Math.max(0, T.endAt - Date.now());
    var s = Math.ceil(T.remaining / 1000);
    if (T.remaining > 0 && T.remaining <= 5000 && s !== T.lastSec) { T.lastSec = s; sfx.tick(); }
    timerPaint();
    if (T.remaining <= 0) { timerStop(); if (T.onEnd) T.onEnd(); }
  }
  function timerTogglePause() {
    if (!T.total || T.remaining <= 0) return;
    if (T.running) { T.remaining = Math.max(0, T.endAt - Date.now()); timerStop(); T.paused = true; }
    else { T.endAt = Date.now() + T.remaining; T.running = true; T.paused = false; T.id = window.setInterval(timerTick, 100); }
    timerPaint();
  }
  function timerPaint() {
    var off = !T.total;
    el.timerCard.classList.toggle('is-off', off);
    el.timerCard.classList.toggle('is-low', !off && T.remaining > 0 && T.remaining <= 5000);
    el.timerCard.classList.toggle('is-done', !off && T.remaining <= 0);
    el.timerCard.classList.toggle('is-paused', T.paused);
    el.ringFg.style.strokeDasharray = CIRC.toFixed(1);
    el.ringFg.style.strokeDashoffset = off ? '0' : (CIRC * (1 - T.remaining / T.total)).toFixed(1);
    el.timeText.textContent = off ? '∞' : fmt(T.remaining);
    el.timeLabel.textContent = off ? 'no limit' : (T.paused ? 'paused' : (T.remaining <= 0 ? "time's up" : 'left'));
  }

  /* ---------------- question flow ---------------- */
  var ACCENTS = ['#ffe600', '#00d2ff', '#ff9aa8'];
  function showQuestion() {
    var g = game, q = g.qs[g.i];
    g.state = 'asking'; g.hidden = []; g.qStart = Date.now();
    el.qCard.className = 'q-card c' + (g.i % 3);
    void el.qCard.offsetWidth; el.qCard.classList.add('in');
    el.viewQuiz.style.setProperty('--accent', ACCENTS[g.i % 3]);
    el.qBurst.innerHTML = '<b>Q' + (g.i + 1) + '</b>';
    el.qText.textContent = q.q;
    var solo = g.mode === 'solo';
    el.options.innerHTML = q.opts.map(function (o, k) {
      var inner = '<span class="opt-key">' + 'ABCD'.charAt(k) + '</span><span class="opt-text">' + esc(o.t) + '</span><span class="opt-mark" aria-hidden="true"></span>';
      return solo ? '<button type="button" class="opt o' + k + '" data-opt="' + k + '" style="--n:' + k + '" aria-label="Option ' + 'ABCD'.charAt(k) + ': ' + esc(o.t) + '">' + inner + '</button>'
        : '<div class="opt o' + k + '" style="--n:' + k + '">' + inner + '</div>';
    }).join('');
    el.feedback.hidden = true; el.award.hidden = true;
    el.qzCounter.innerHTML = 'Question <b>' + (g.i + 1) + '</b> / ' + g.qs.length;
    el.qzFill.style.width = (g.i / g.qs.length * 100).toFixed(1) + '%';
    renderActions(); renderSide();
    timerStart(g.seconds, function () { onTimeUp(); });
  }

  function renderActions() {
    var g = game, last = g.i >= g.qs.length - 1, html = '';
    var nextBtn = '<button type="button" class="big-btn ' + (last ? 'go' : '') + ' grow" data-act="next">' + (last ? '🏆 See results' : 'Next →') + '</button>';
    var fiftyBtn = '<button type="button" class="big-btn small alt" data-act="fifty"' + (g.fifty < 1 ? ' disabled' : '') + '>✂ 50:50 (' + g.fifty + ')</button>';
    if (g.state === 'asking') {
      if (g.mode === 'solo') html = fiftyBtn;
      else html = '<button type="button" class="big-btn small alt" data-act="pause">' + (T.paused ? '▶ Resume' : '⏸ Pause') + '</button>' + fiftyBtn +
        '<button type="button" class="big-btn grow" data-act="reveal">👁 Reveal answer</button>';
    } else { html = nextBtn; }
    el.qActions.innerHTML = html;
  }

  function renderSide() {
    var g = game, html = '';
    if (g.mode === 'solo') {
      var answered = g.results.length;
      html = '<h3>Your stats</h3>' +
        '<div class="stat-row">Score <b>' + g.score + '</b></div>' +
        '<div class="stat-row' + (g.streak >= 3 ? ' hot' : '') + '">Streak 🔥 <b>' + g.streak + '</b></div>' +
        '<div class="stat-row">Answered <b>' + answered + '/' + g.qs.length + '</b></div>';
    } else {
      var top = Math.max.apply(null, g.teams.map(function (t) { return t.score; }));
      html = '<h3>Scoreboard</h3>' + g.teams.map(function (t, i) {
        return '<div class="team-row' + (top > 0 && t.score === top ? ' lead' : '') + '" data-t="' + i + '" style="--tc:' + t.color + '"><span class="t-name">' + esc(t.name) + '</span><span class="t-score">' + t.score + '</span></div>';
      }).join('');
    }
    el.sidePanel.innerHTML = html;
  }

  function markOptions(chosen) {
    var g = game, q = g.qs[g.i];
    $$('.opt', el.options).forEach(function (node, k) {
      node.classList.remove('is-gone');
      if (g.hidden.indexOf(k) > -1) node.classList.add('is-gone');
      if (k === q.ans) { node.classList.add('is-correct'); node.querySelector('.opt-mark').textContent = '✔'; }
      else if (k === chosen) { node.classList.add('is-wrong'); node.querySelector('.opt-mark').textContent = '✘'; }
      else node.classList.add('is-dim');
      if (node.tagName === 'BUTTON') node.disabled = true;
    });
  }
  function showFeedback(kind, title) {
    var q = game.qs[game.i];
    var correct = 'ABCD'.charAt(q.ans) + ') ' + q.opts[q.ans].t;
    el.feedback.className = 'feedback ' + kind;
    el.feedback.innerHTML = '<strong>' + esc(title) + '</strong><p><b>Correct answer: ' + esc(correct) + '</b>' + (q.why ? '<br>' + esc(q.why) : '') + '</p>';
    el.feedback.hidden = false;
  }

  /* solo */
  function answerSolo(k) {
    var g = game;
    if (g.mode !== 'solo' || g.state !== 'asking' || g.hidden.indexOf(k) > -1) return;
    timerStop();
    var q = g.qs[g.i], ok = k === q.ans, spent = (Date.now() - g.qStart) / 1000;
    g.state = 'revealed';
    g.results.push({ chosen: k, ok: ok, time: spent });
    if (ok) { g.score++; g.streak++; g.bestStreak = Math.max(g.bestStreak, g.streak); sfx.good(); } else { g.streak = 0; sfx.bad(); }
    markOptions(k);
    showFeedback(ok ? 'good' : 'bad', ok ? 'CORRECT!' : 'OOPS!');
    if (ok && g.streak >= 3) stamp('COMBO x' + g.streak + '!', true, 1100);
    renderActions(); renderSide();
    el.qzFill.style.width = ((g.i + 1) / g.qs.length * 100).toFixed(1) + '%';
  }
  function onTimeUp() {
    var g = game;
    if (!g || g.state !== 'asking') return;
    sfx.time();
    stamp("TIME'S UP!", false, 1300);
    if (g.mode === 'solo') {
      g.state = 'revealed'; g.results.push({ chosen: -1, ok: false, time: g.seconds }); g.streak = 0;
      markOptions(-1); showFeedback('bad', "TIME'S UP!"); renderActions(); renderSide();
      el.qzFill.style.width = ((g.i + 1) / g.qs.length * 100).toFixed(1) + '%';
    } else revealClass(true);
  }

  /* classroom */
  function revealClass(fromTimer) {
    var g = game;
    if (g.mode !== 'class' || g.state !== 'asking') return;
    timerStop(); T.paused = false; timerPaint();
    g.state = 'revealed'; g.awarded[g.i] = g.awarded[g.i] || [];
    markOptions(-1);
    showFeedback('good', 'ANSWER!');
    if (!fromTimer) sfx.good();
    el.award.hidden = false;
    renderAwards();
    renderActions();
    el.qzFill.style.width = ((g.i + 1) / g.qs.length * 100).toFixed(1) + '%';
  }
  function renderAwards() {
    var g = game, got = g.awarded[g.i] || [];
    el.award.innerHTML = '<h3>Which teams got it right? Tap to award +' + g.points + '</h3><div class="award-btns">' +
      g.teams.map(function (t, i) {
        return '<button type="button" class="award-btn' + (got.indexOf(i) > -1 ? ' is-on' : '') + '" data-award="' + i + '" data-pts="' + g.points + '" style="--tc:' + t.color + '"><kbd>' + (i + 1) + '</kbd> ' + esc(t.name) + '</button>';
      }).join('') + '</div>';
  }
  function toggleAward(i) {
    var g = game;
    if (g.mode !== 'class' || g.state !== 'revealed' || !g.teams[i]) return;
    var got = g.awarded[g.i], pos = got.indexOf(i);
    if (pos > -1) { got.splice(pos, 1); g.teams[i].score -= g.points; sfx.click(); }
    else { got.push(i); g.teams[i].score += g.points; sfx.good(); }
    renderAwards(); renderSide();
    var row = $('.team-row[data-t="' + i + '"]', el.sidePanel);
    if (row) restart(row, 'bump');
  }

  function useFifty() {
    var g = game;
    if (g.state !== 'asking' || g.fifty < 1) return;
    var q = g.qs[g.i];
    var wrong = [];
    q.opts.forEach(function (o, k) { if (k !== q.ans && g.hidden.indexOf(k) < 0) wrong.push(k); });
    if (wrong.length < 2) return;
    shuffle(wrong).slice(0, 2).forEach(function (k) {
      g.hidden.push(k);
      var node = el.options.children[k];
      node.classList.add('is-gone');
      if (node.tagName === 'BUTTON') node.disabled = true;
    });
    g.fifty--; sfx.click(); renderActions();
  }
  function nextQuestion() {
    var g = game;
    if (g.state !== 'revealed') return;
    if (g.i >= g.qs.length - 1) return finish();
    g.i++; sfx.click(); showQuestion();
  }

  /* quiz events */
  el.options.addEventListener('click', function (e) { var b = e.target.closest('[data-opt]'); if (b) answerSolo(Number(b.dataset.opt)); });
  el.qActions.addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]'); if (!b || !game) return;
    var a = b.dataset.act;
    if (a === 'next') nextQuestion();
    else if (a === 'fifty') useFifty();
    else if (a === 'reveal') revealClass(false);
    else if (a === 'pause') { timerTogglePause(); renderActions(); }
    if (b.blur) b.blur();
  });
  el.award.addEventListener('click', function (e) { var b = e.target.closest('[data-award]'); if (b) { toggleAward(Number(b.dataset.award)); b.blur(); } });

  /* ---------------- results ---------------- */
  function rating(pct) {
    if (pct >= 90) return ['LEGEND!', 'You absolutely crushed it!'];
    if (pct >= 70) return ['SUPER!', 'Great work — almost perfect!'];
    if (pct >= 50) return ['NICE TRY!', 'Good effort — a little more revision and you will fly.'];
    return ['KEEP GOING!', 'Every hero starts somewhere — revise and try again!'];
  }
  function finish() {
    timerStop(); T.total = 0;
    if (document.fullscreenElement && document.exitFullscreen) { try { document.exitFullscreen(); } catch (e) { /* ignore */ } }
    if (game.mode === 'solo') soloResult(); else classResult();
    showView('result');
  }
  function soloResult() {
    var g = game, total = g.qs.length, correct = g.score, pct = Math.round(correct * 100 / total);
    var r = rating(pct), stars = pct >= 80 ? 3 : pct >= 50 ? 2 : pct > 0 ? 1 : 0;
    var avg = g.results.length ? (g.results.reduce(function (s, x) { return s + x.time; }, 0) / g.results.length) : 0;
    var prev = bestFor(g.key), isBest = !prev || pct > prev.pct;
    var bests = store(KEYS.bests) || {};
    bests[g.key] = { pct: Math.max(pct, prev ? prev.pct : 0), plays: (prev ? prev.plays : 0) + 1 };
    store(KEYS.bests, bests);
    var wrong = [];
    g.results.forEach(function (x, i) { if (!x.ok) wrong.push(i); });
    var review = wrong.length ? '<section class="review"><h2>Review your mistakes</h2>' + wrong.map(function (i, n) {
      var q = g.qs[i], x = g.results[i];
      return '<article class="rev-item" style="--i:' + n + '"><div class="rev-q"><i>Q' + (i + 1) + '</i><span>' + esc(q.q) + '</span></div><div class="rev-body">' +
        '<p><span class="tag-bad">' + (x.chosen < 0 ? "Time's up" : 'Your answer') + '</span>' + (x.chosen < 0 ? 'No answer given' : esc('ABCD'.charAt(x.chosen) + ') ' + q.opts[x.chosen].t)) + '</p>' +
        '<p><span class="tag-good">Correct</span>' + esc('ABCD'.charAt(q.ans) + ') ' + q.opts[q.ans].t) + '</p>' +
        (q.why ? '<p>💡 ' + esc(q.why) + '</p>' : '') + '</div></article>';
    }).join('') + '</section>' : '<section class="review"><div class="perfect">🎉 Perfect round — no mistakes to review!</div></section>';
    el.viewResult.innerHTML =
      '<div class="res-card"><div class="burst"><b>' + correct + '<small>/' + total + '</small></b></div>' +
      '<h2 class="res-title">' + r[0] + '</h2><p class="res-sub">' + pct + '% correct · ' + r[1] + '</p>' +
      '<div class="stars" aria-label="' + stars + ' of 3 stars">' + [1, 2, 3].map(function (n) { return '<span class="' + (n <= stars ? '' : 'off') + '">⭐</span>'; }).join('') + '</div>' +
      '<div class="res-stats"><div class="res-stat good"><b>' + correct + '</b>Correct</div><div class="res-stat bad"><b>' + (total - correct) + '</b>Wrong / missed</div>' +
      '<div class="res-stat"><b>' + g.bestStreak + '🔥</b>Best streak</div><div class="res-stat"><b>' + avg.toFixed(1) + 's</b>Avg per question</div></div>' +
      '<p class="res-best">' + (isBest && pct > 0 ? '🏅 New best for this chapter!' : 'Best so far: ' + (prev ? Math.max(prev.pct, pct) : pct) + '%') + '</p>' +
      '<div class="res-actions"><button type="button" class="big-btn" data-res="again">↻ Play again</button>' +
      (wrong.length ? '<button type="button" class="big-btn alt" data-res="retry">🎯 Retry mistakes (' + wrong.length + ')</button>' : '') +
      '<button type="button" class="big-btn alt" data-res="home">🏠 New chapter</button>' +
      '<a class="big-btn alt" href="' + NCERT_URL + '" target="_blank" rel="noopener noreferrer">📚 Revise on NCERT One Stop ↗</a></div></div>' + review;
    if (pct >= 70) { sfx.win(); confetti(3500); } else if (pct >= 50) sfx.good(); else sfx.bad();
    game.wrongIdx = wrong;
  }
  function classResult() {
    var g = game, teams = g.teams.map(function (t, i) { return { name: t.name, color: t.color, score: t.score, i: i }; });
    teams.sort(function (a, b) { return b.score - a.score; });
    var rank = 0, prevScore = null;
    teams.forEach(function (t, idx) { if (t.score !== prevScore) { rank = idx + 1; prevScore = t.score; } t.rank = rank; });
    var winners = teams.filter(function (t) { return t.rank === 1; });
    var headline = winners[0].score === 0 ? 'NO POINTS YET!' : winners.length > 1 ? "IT'S A TIE!" : esc(winners[0].name).toUpperCase() + ' WINS!';
    var sub = winners.length > 1 && winners[0].score > 0 ? winners.map(function (w) { return esc(w.name); }).join(' & ') + ' share the crown' : 'Brilliant teamwork, everyone!';
    var top = teams.slice(0, 3);
    var order = top.length === 3 ? [top[1], top[0], top[2]] : top.length === 2 ? [top[1], top[0]] : top;
    var pod = order.map(function (t) {
      return '<div class="pod r' + Math.min(t.rank, 4) + '" style="--tc:' + t.color + '">' + (t.rank === 1 && t.score > 0 ? '<span class="crown">👑</span>' : '') +
        '<div class="p-name">' + esc(t.name) + '</div><div class="p-block"><span>' + t.score + '<small>' + (t.rank === 1 ? '1st' : t.rank === 2 ? '2nd' : t.rank === 3 ? '3rd' : t.rank + 'th') + '</small></span></div></div>';
    }).join('');
    var others = teams.slice(3).map(function (t) {
      return '<div class="team-row" style="--tc:' + t.color + '"><span class="t-name">' + t.rank + '. ' + esc(t.name) + '</span><span class="t-score">' + t.score + '</span></div>';
    }).join('');
    el.viewResult.innerHTML =
      '<div class="res-card"><div class="burst"><b>🏆</b></div><h2 class="res-title">' + headline + '</h2><p class="res-sub">' + sub + '</p>' +
      '<div class="podium">' + pod + '</div>' + (others ? '<div class="others">' + others + '</div>' : '') +
      '<div class="res-stats"><div class="res-stat"><b>' + g.qs.length + '</b>Questions played</div><div class="res-stat"><b>' + g.teams.length + '</b>Teams</div></div>' +
      '<div class="res-actions"><button type="button" class="big-btn" data-res="again">↻ Rematch</button><button type="button" class="big-btn alt" data-res="home">🏠 New chapter</button>' +
      '<a class="big-btn alt" href="' + NCERT_URL + '" target="_blank" rel="noopener noreferrer">📚 Revise on NCERT One Stop ↗</a></div></div>';
    if (winners[0].score > 0) { sfx.win(); confetti(4500); }
  }
  el.viewResult.addEventListener('click', function (e) {
    var b = e.target.closest('[data-res]'); if (!b || !game) return;
    var a = b.dataset.res;
    if (a === 'home') { goHome(); }
    else if (a === 'again') { var qs = reshuffleQs(game.qs); sel.mode = game.mode; relaunch(qs); }
    else if (a === 'retry') { var w = game.wrongIdx.map(function (i) { return game.qs[i]; }); relaunch(reshuffleQs(w)); }
  });
  function relaunch(qs) {
    var keep = { key: game.key, title: game.title };
    var isClass = game.mode === 'class';
    launch(qs);
    game.key = keep.key; game.title = keep.title;
    if (isClass) game.teams.forEach(function (t) { t.score = 0; });
    renderSide();
  }

  /* ---------------- navigation, quit, fullscreen ---------------- */
  function goHome() {
    timerStop(); game = null; showView('home');
    renderStep(step); renderWizard();
    if (sel.chapter) { step = 4; renderStep(4); renderWizard(); }
  }
  function toggleFs() {
    try {
      if (document.fullscreenElement) document.exitFullscreen();
      else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen();
    } catch (e) { /* ignore */ }
  }
  function quiting() { return document.body.dataset.view === 'quiz' && game; }
  el.qzQuit.addEventListener('click', function () { el.quitDialog.showModal(); });
  el.qzFs.addEventListener('click', toggleFs);
  el.quitDialog.addEventListener('close', function () {
    if (el.quitDialog.returnValue === 'quit') {
      if (document.fullscreenElement && document.exitFullscreen) { try { document.exitFullscreen(); } catch (e) { /* ignore */ } }
      goHome();
    }
    el.quitDialog.returnValue = '';
  });
  el.brandLink.addEventListener('click', function (e) {
    e.preventDefault();
    if (quiting()) el.quitDialog.showModal(); else goHome();
  });
  el.soundBtn.addEventListener('click', toggleSound);

  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var tag = e.target && e.target.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
    if (el.quitDialog.open) return;
    var k = e.key, lk = k.toLowerCase();
    if (lk === 'm') { toggleSound(); return; }
    if (!quiting()) return;
    var g = game, handled = true;
    if (k === 'Escape') el.quitDialog.showModal();
    else if (lk === 'f') toggleFs();
    else if (g.mode === 'solo') {
      var map = { '1': 0, '2': 1, '3': 2, '4': 3, a: 0, b: 1, c: 2, d: 3 };
      if (g.state === 'asking') {
        if (map[lk] !== undefined) answerSolo(map[lk]);
        else if (lk === 'h') useFifty();
        else handled = false;
      } else if (k === 'Enter' || k === ' ' || k === 'ArrowRight') nextQuestion();
      else handled = false;
    } else {
      if (g.state === 'asking') {
        if (k === ' ' || k === 'Enter') revealClass(false);
        else if (lk === 'p') { timerTogglePause(); renderActions(); }
        else if (lk === 'h') useFifty();
        else handled = false;
      } else {
        var n = parseInt(k, 10);
        if (n >= 1 && n <= g.teams.length) toggleAward(n - 1);
        else if (k === 'Enter' || k === ' ' || k === 'ArrowRight') nextQuestion();
        else handled = false;
      }
    }
    if (handled) e.preventDefault();
  });
  document.addEventListener('keyup', function (e) { if (e.key === ' ' && quiting() && e.target.tagName === 'BUTTON') e.preventDefault(); });

  el.startBtn.addEventListener('click', startGame);
  window.addEventListener('beforeunload', function (e) { if (quiting() && game.state !== 'done') { e.preventDefault(); e.returnValue = ''; } });

  /* ---------------- boot ---------------- */
  function boot() {
    syncSoundBtn(); buildTicker(); timerPaint();
    loadIndex().then(function () {
      buildStats(); renderStep(1); renderWizard();
    }).catch(function () {
      el.classGrid.innerHTML = '<div class="perfect">Could not load the question bank. If you opened this file directly, run it from a web server (for example <code>python3 -m http.server</code>) or deploy it to Vercel.</div>';
    });
    if ('serviceWorker' in navigator && window.location.protocol.indexOf('http') === 0) {
      window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () { /* ignore */ }); });
    }
  }
  boot();
})();
