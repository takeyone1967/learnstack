# LearnStack

Honest, research-driven reviews of AI-powered learning tools — language apps,
online course platforms, and study tools. Live at [yameyaku.com](https://yameyaku.com).

## How this repo works

- `content/*.md` — articles in Markdown (front matter: title / description / date / slug)
- `assets/style.css` — site stylesheet
- `build.py` — static site generator (requires `pip install markdown`)
- `docs/` — built site output, served by GitHub Pages

To rebuild after editing content:

```bash
python3 build.py
```

Then commit and push. GitHub Pages serves `docs/` on the `main` branch.

## Editorial policy

- Every article carries an affiliate disclosure at the top.
- No fabricated first-person experience — claims are research-based and fact-checked before publication.
- Every review lists genuine weaknesses alongside strengths.
