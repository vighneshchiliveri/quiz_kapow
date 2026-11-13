# Quiz Kapow! — NCERT Practice Arena

Solo practice and classroom challenge quizzes. Static site (no build step).

## Add questions
1. Copy `data/questions/_template.json`, rename it (e.g. `class10-science-ch02.json`) and fill it in. The `id` must match the file name.
2. Run `python3 build_index.py` (checks your questions and rebuilds `data/index.json`).
3. Commit and push. Vercel redeploys automatically.

## Deploy on Vercel
Framework Preset: Other · Build Command: empty · Output Directory: empty.

## Mathematics question bank (Classes 6–12)
`tools/` holds the compact source text for all Mathematics chapters (`math_data_*.py`) and `gen_math.py`, which writes the JSON files in `data/questions/`.
Edit or add questions there (one line each: `question ~ correct ~ wrong 1 ~ wrong 2 ~ wrong 3 ~ explanation`), then run:
`python3 tools/gen_math.py && python3 build_index.py`
Or edit the generated JSON files directly (then only `build_index.py` is needed).
Chapter lists: Classes 6–8 Ganita Prakash, Class 9 Ganita Manjari Part 1, Classes 10–12 NCERT Mathematics.
