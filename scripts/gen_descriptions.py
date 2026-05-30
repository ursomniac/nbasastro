#!/usr/bin/env python3
"""
gen_descriptions.py
Generates Google-optimized descriptions for NBAS Hugo articles.
Output: descriptions.csv with columns:
  file, title, current_description, proposed_description, char_count

Usage:
  python3 gen_descriptions.py /path/to/content
"""

import os
import sys
import csv
import json
import re
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"
MAX_DESC_CHARS = 160

SKIP_DIRS = {"members", "_index.md"}
SKIP_FILES = {"_index.md"}

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
    """Extract title, description, and body from a Hugo markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Must start with ---
    if not content.startswith("---"):
        return None, None, None

    # Find end of frontmatter
    end = content.find("---", 3)
    if end == -1:
        return None, None, None

    frontmatter = content[3:end]
    body = content[end+3:].strip()

    # Extract title
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
    title = title_match.group(1).strip('"\'') if title_match else ""

    # Extract current description
    desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
    current_desc = desc_match.group(1).strip('"\'') if desc_match else ""

    return title, current_desc, body


def clean_body(body):
    """Strip Hugo shortcodes and markdown for cleaner AI input."""
    # Remove shortcodes
    body = re.sub(r'\{\{[^}]+\}\}', '', body)
    # Remove markdown headers
    body = re.sub(r'^#{1,6}\s+', '', body, flags=re.MULTILINE)
    # Remove markdown links
    body = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', body)
    # Remove bold/italic
    body = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', body)
    # Remove HTML tags
    body = re.sub(r'<[^>]+>', '', body)
    # Collapse whitespace
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def generate_description(title, body):
    """Call Ollama to generate a description."""
    # Use first 1500 chars of body to keep prompt manageable
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
            desc = result.get("response", "").strip()
            # Remove any quotes the model added
            desc = desc.strip('"\'')
            # Truncate if over limit
            if len(desc) > MAX_DESC_CHARS:
                desc = desc[:MAX_DESC_CHARS-3] + "..."
            return desc
    except urllib.error.URLError as e:
        return f"ERROR: {e}"


def find_articles(content_dir):
    """Find all article index.md files, skipping members and index pages."""
    articles = []
    for root, dirs, files in os.walk(content_dir):
        # Skip members section
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for fname in files:
            if fname in SKIP_FILES:
                continue
            if fname.endswith(".md"):
                articles.append(os.path.join(root, fname))

    return sorted(articles)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gen_descriptions.py /path/to/content")
        sys.exit(1)

    content_dir = sys.argv[1]
    if not os.path.isdir(content_dir):
        print(f"Error: {content_dir} is not a directory")
        sys.exit(1)

    articles = find_articles(content_dir)
    print(f"Found {len(articles)} articles")

    output_file = "descriptions.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file", "title", "current_description", "proposed_description", "char_count"])

        for i, filepath in enumerate(articles, 1):
            # Get relative path for readability
            relpath = os.path.relpath(filepath, content_dir)

            title, current_desc, body = read_frontmatter(filepath)
            if title is None:
                print(f"  [{i}/{len(articles)}] SKIP (no frontmatter): {relpath}")
                continue

            if not body:
                print(f"  [{i}/{len(articles)}] SKIP (no body): {relpath}")
                continue

            print(f"  [{i}/{len(articles)}] {relpath} ...", end=" ", flush=True)
            proposed = generate_description(title, body)
            chars = len(proposed)
            print(f"{chars} chars")

            writer.writerow([relpath, title, current_desc, proposed, chars])
            csvfile.flush()

    print(f"\nDone. Results written to {output_file}")


if __name__ == "__main__":
    main()
