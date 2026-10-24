# Senior Java Interview Prep

A personal knowledge base for senior Java developer interviews, written in Markdown and published as a website with MkDocs Material.

The goal is to keep everything in one place so that the next interview starts from these notes instead of from scratch.

## Run locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000. Edit any file in `docs/` and the page reloads.

## Edit with Obsidian (optional)

Open the `docs/` folder as an Obsidian vault. The files are plain Markdown, so both tools work on the same notes.

## Publish to GitHub Pages

1. Push this repository to GitHub (public repos get free Pages).
2. In the repository go to Settings > Pages and set Source to GitHub Actions.
3. Every push to `main` builds and publishes the site through `.github/workflows/pages.yml`.

## Habits that keep it useful

- After every interview, add a note in `docs/interview-log/` from the template within 24 hours.
- Drop interesting links into `docs/inbox.md` and sort them once a week.
- Add each new question you were asked to `docs/question-bank.md` with your answer.
