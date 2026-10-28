---
name: ingest-chat
description: Turn a chat (ChatGPT share link, pasted text or file) about an interview topic into compact notes merged into the docs/ site. Use when the user shares a conversation and asks to analyse it, extract the important parts, or add it to the interview prep material.
---

# Ingest a chat into the interview site

The site is a MkDocs Material knowledge base in `docs/`. The goal is a short, readable, structured page per topic, never a transcript.

## 1. Get the text

- Pasted text or a file: use it directly.
- ChatGPT share link (`https://chatgpt.com/share/...`): normal web fetch returns almost nothing because the page is rendered by JavaScript. Run:
  `python3 .cursor/skills/ingest-chat/scripts/fetch_chatgpt_share.py <url> /tmp/chat.txt`
  and read `/tmp/chat.txt`. If it prints "No conversation found", ask the user to paste the chat.
- Never write the raw chat into the repo.

## 2. Triage

Keep what matters for a senior interview: concepts, trade-offs, failure modes, concrete flags and numbers, diagnosis procedures, common traps, practice questions.

Drop: filler and pleasantries, analogies that do not teach, "interview answer" paraphrases that repeat the content, favicon/image/source artefacts (`[image](...)`, `docs.oracle.com+1`, `&#x20;`, `utm_source`), and meta lines such as "let's make this interactive".

## 3. Check facts

Do not copy blindly. Flag claims that are wrong, vague or version-dependent (Java version, JVM vendor, default settings). Tag version-specific facts in the notes (for example "Java 17+"). Mention doubtful claims in the final report.

## 4. Map to pages

Match each topic to an existing page listed in `mkdocs.yml` (`java-core/`, `spring/`, `architecture/`, `testing.md`, `algorithms.md`, `behavioral.md`). Create a new page only when nothing fits, and then add it to `nav` in `mkdocs.yml` and to the roadmap if relevant. Keep the page title the same as the `nav` entry.

## 5. Merge, do not duplicate

Read the target page first. Extend its sections in the house style:

- `## Key concepts` with short bold-term bullets
- tables for comparisons, fenced code only when it teaches something
- `## Common questions` as short question bullets
- `!!! warning "Gotchas"` admonition for traps

Reorganise existing content only where it overlaps. Preserve everything that is still correct. Write short English bullets, one idea each.

## 6. Feed the question bank

Add each practice question to the matching table in `docs/question-bank.md` with a one-line answer and a level (`strong`, `medium`, `weak`). Use `weak` for questions the user has not drilled yet. Chats often leave answers empty, so write them from the chat content. Put leftover links or study-order notes in `docs/inbox.md`.

## 7. Guardrails

- No private data (salary, offers, personal details); the site may be public.
- Run `pip install -r requirements.txt && mkdocs build --strict` and fix warnings.
- One commit per ingested chat, conventional message, for example `docs: add JVM chat notes`.

## 8. Report

Finish with a short summary: pages changed, what was added, what was skipped and why, doubtful claims, and topics from the chat that still need their own page.
