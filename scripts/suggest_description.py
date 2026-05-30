#!/usr/bin/env python3
"""
suggest_description.py
Suggests a Google-optimized meta description for a single Hugo article.

Usage:
  python3 suggest_description.py content/articles/2026/06/hr-diagram/index.md
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"
MAX_DESC_CHARS = 160

SYSTEM_PROMPT = """You are an SEO specialist writing meta descriptions for an amateur astronomy club website.
Your descriptions must:
- Be under 160 characters including spaces
- Be specific to the actual content of the article
- Be written for a general audience interested in astronomy
- Not start with the site name or club name
- Not use the word "discover" or "explore"
- Be a complete sentence or clear phrase
- Focus on what the reader will learn or find

Respond with ONLY the description text. No quotes. No explanation. No preamble."""


def read_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        print("Error: no front matter found")
        sys.exit(1)

    end = content.find("---", 3)
    if end == -1:
        print("Error: front matter not closed")
        sys.exit(1)

    frontmatter = content[3:end]
    body = content[end+3:].strip()

    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
    title = title_match.group(1).strip('"\'') if title_match else ""

    desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
    current_desc = desc_match.group(1).strip('"\'') if desc_match else ""

    return title, current_desc, body


def clean_body(body):
    body = re.sub(r'\{\{[^}]+\}\}', '', body)
    body = re.sub(r'^#{1,6}\s+', '', body, flags=re.MULTILINE)
    body = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', body)
    body = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', body)
    body = re.sub(r'<[^>]+>', '', body)
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def generate_description(title, body):
    excerpt = clean_body(body)[:1500]

    prompt = f"""Article title: {title}

Article content:
{excerpt}

Write a Google meta description for this article."""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 100
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            desc = result.get("response", "").strip().strip('"\'')
            return desc
    except urllib.error.URLError as e:
        print(f"Error calling Ollama: {e}")
        sys.exit(1)


def check_length(desc):
    chars = len(desc)
    if chars > MAX_DESC_CHARS:
        return chars, f"WARNING: {chars} chars — over the {MAX_DESC_CHARS} char limit"
    else:
        return chars, f"OK: {chars} chars"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 suggest_description.py path/to/index.md")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"Error: {filepath} not found")
        sys.exit(1)

    title, current_desc, body = read_frontmatter(filepath)

    print(f"\nFile:  {filepath}")
    print(f"Title: {title}")
    print()

    if current_desc:
        chars, status = check_length(current_desc)
        print(f"Current ({chars} chars): {current_desc}")
        print(f"  {status}")
    else:
        print("Current: (none)")

    print()
    print("Generating proposed description...")
    proposed = generate_description(title, body)
    chars, status = check_length(proposed)
    print()
    print(f"Proposed ({chars} chars): {proposed}")
    print(f"  {status}")
    print()
    print("To apply, add or update this line in the front matter:")
    print(f'  description: "{proposed}"')
    print()


if __name__ == "__main__":
    main()
