#!/usr/bin/env python3
"""Rebuild data/index.json from data/questions/*.json and validate every question.
Usage:  python3 build_index.py          (run from the quiz-kapow folder)
Files starting with _ (like _template.json) are ignored."""
import json, glob, os, sys
root = os.path.dirname(os.path.abspath(__file__))
chapters, errors = [], []
for path in sorted(glob.glob(os.path.join(root, 'data', 'questions', '*.json'))):
    name = os.path.basename(path)
    if name.startswith('_'): continue
    try: d = json.load(open(path, encoding='utf-8'))
    except Exception as e: errors.append(f'{name}: invalid JSON ({e})'); continue
    for k in ('id', 'class', 'subject', 'title', 'questions'):
        if not d.get(k): errors.append(f'{name}: missing "{k}"')
    if d.get('id') and d['id'] != name[:-5]: errors.append(f'{name}: "id" must equal the file name ({name[:-5]})')
    for i, q in enumerate(d.get('questions', []), 1):
        o = q.get('options')
        if not q.get('q'): errors.append(f'{name} Q{i}: empty question')
        if not isinstance(o, list) or len(o) != 4 or any(not str(x).strip() for x in o): errors.append(f'{name} Q{i}: needs exactly 4 non-empty options')
        elif len(set(map(str, o))) != 4: errors.append(f'{name} Q{i}: options must be different')
        if q.get('answer') not in (0, 1, 2, 3): errors.append(f'{name} Q{i}: "answer" must be 0, 1, 2 or 3 (index of correct option)')
    chapters.append({'id': d.get('id'), 'class': str(d.get('class')), 'subject': d.get('subject'), 'book': d.get('book') or d.get('subject'),
        'order': d.get('order', 999), 'chapter': d.get('chapter', ''), 'title': d.get('title'), 'icon': d.get('icon', '📖'),
        'count': len(d.get('questions', [])), 'file': 'data/questions/' + name})
if errors:
    print('Fix these first:'); [print(' -', e) for e in errors]; sys.exit(1)
chapters.sort(key=lambda c: (int(c['class']) if c['class'].isdigit() else 99, c['subject'], c['book'], c['order'], c['id']))
json.dump({'chapters': chapters}, open(os.path.join(root, 'data', 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK: {len(chapters)} chapters, {sum(c["count"] for c in chapters)} questions -> data/index.json')
