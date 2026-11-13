#!/usr/bin/env python3
"""Generates data/questions/class*-mathematics-*.json from the compact text in math_data_*.py.
Each question line:  question ~ correct answer ~ wrong 1 ~ wrong 2 ~ wrong 3 ~ explanation
The correct option is shuffled to a random (but repeatable) position, so answer positions vary.
Run from the project root:  python3 tools/gen_math.py && python3 build_index.py"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math_data_6_8 import DATA as D1
from math_data_9_10 import DATA as D2
from math_data_11_12 import DATA as D3

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, 'data', 'questions')
os.makedirs(out, exist_ok=True)
total = 0
for cls, book, part, order, title, icon, text in D1 + D2 + D3:
    cid = 'class%s-mathematics-%sch%02d' % (cls, (part + '-') if part else '', order)
    rng = random.Random(cid)
    qs = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        f = [x.strip() for x in line.split('~')]
        assert len(f) == 6, (cid, line)
        q, correct, w1, w2, w3, ex = f
        opts = [correct, w1, w2, w3]
        assert len(set(opts)) == 4, (cid, line)
        rng.shuffle(opts)
        qs.append({'q': q, 'options': opts, 'answer': opts.index(correct), 'explanation': ex})
    doc = {'id': cid, 'class': str(cls), 'subject': 'Mathematics', 'book': book, 'order': order,
           'chapter': 'Chapter %d' % order, 'title': title, 'icon': icon, 'questions': qs}
    with open(os.path.join(out, cid + '.json'), 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    total += len(qs)
print('Wrote %d chapters, %d questions' % (len(D1 + D2 + D3), total))
