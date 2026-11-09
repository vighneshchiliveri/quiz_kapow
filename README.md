# Quiz Kapow! — NCERT Practice Arena

Solo practice and classroom challenge quizzes. Static site (no build step).

## Add questions
1. Copy `data/questions/_template.json`, rename it (e.g. `class10-science-ch02.json`) and fill it in. The `id` must match the file name.
2. Run `python3 build_index.py` (checks your questions and rebuilds `data/index.json`).
3. Commit and push. Vercel redeploys automatically.

## Deploy on Vercel
Framework Preset: Other · Build Command: empty · Output Directory: empty.
