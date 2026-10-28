#!/usr/bin/env python3
"""Print a shared ChatGPT conversation as plain text.

Usage: fetch_chatgpt_share.py <share-url> [output-file]

Share pages are rendered by JavaScript, so a normal fetch returns nothing useful.
The conversation text is embedded in the raw HTML; this script downloads the page
with a browser user-agent and collects the long message strings. If the page format
changes and nothing is found, ask the user to paste the chat instead.
"""
import json
import re
import sys
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def download(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract(html: str) -> str:
    parts, seen = [], set()
    for raw in re.findall(r'streamController\.enqueue\("((?:[^"\\]|\\.)*)"\)', html, re.S):
        try:
            data = json.loads(json.loads(f'"{raw}"'))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, list):
            continue
        for item in data:
            if isinstance(item, str) and len(item) > 200 and "\n" in item and item not in seen:
                seen.add(item)
                parts.append(item.strip())
    return "\n\n---\n\n".join(parts)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    text = extract(download(sys.argv[1]))
    if not text:
        print("No conversation found. Ask the user to paste the chat.", file=sys.stderr)
        return 1
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
