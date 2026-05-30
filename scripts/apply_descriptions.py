#!/usr/bin/env python3
"""
apply_descriptions.py
Reads the approved descriptions CSV and patches Hugo front matter files.
- If description: exists, replaces it
- If description: does not exist, inserts it after date:
- Skips files marked SKIP or with empty proposed_description

Usage:
  python3 apply_descriptions.py descriptions_approved.csv /path/to/content

IMPORTANT: Run this from your Hugo project root.
Make sure you have committed your work before running this script.
"""

import os
import sys
import csv
import re
import shutil
from datetime import datetime

# Files to skip entirely
SKIP_FILES = {
    "menu/index.md",
    "newsflash/test-flash.md",
}

# Files where we keep the existing description and ignore proposed
KEEP_EXISTING = {
    "guides/telescopes-beginner/basics/index.md",
    "guides/telescopes-beginner/buying/index.md",
    "guides/telescopes-beginner/eyepieces/index.md",
    "guides/telescopes-beginner/features/index.md",
    "guides/telescopes-beginner/gear/index.md",
    "guides/telescopes-beginner/mounts/index.md",
    "guides/telescopes-beginner/smart/index.md",
    "guides/telescopes-beginner/types/index.md",
    "quizzes/guess-the-moon/index.md",
    "quizzes/match-dso-types/index.md",
    "articles/2026/04/t-coronae-borealis/index.md",
}


def patch_file(filepath, description):
    """
    Patch the description in a Hugo front matter file.
    Returns (success, message)
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return False, "No front matter found"

    # Find end of front matter
    end = content.find("---", 3)
    if end == -1:
        return False, "Front matter not closed"

    frontmatter = content[3:end]
    rest = content[end:]

    # Clean description for front matter - escape any quotes
    clean_desc = description.strip().strip('"\'')

    # Check if description: already exists
    if re.search(r'^description:', frontmatter, re.MULTILINE):
        # Replace existing description
        new_frontmatter = re.sub(
            r'^description:.*$',
            f'description: "{clean_desc}"',
            frontmatter,
            flags=re.MULTILINE
        )
    else:
        # Insert after date: line
        new_frontmatter = re.sub(
            r'^(date:.+)$',
            r'\1\ndescription: "' + clean_desc + '"',
            frontmatter,
            flags=re.MULTILINE
        )
        # If no date: line found, insert after title:
        if new_frontmatter == frontmatter:
            new_frontmatter = re.sub(
                r'^(title:.+)$',
                r'\1\ndescription: "' + clean_desc + '"',
                frontmatter,
                flags=re.MULTILINE
            )

    new_content = "---" + new_frontmatter + rest

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "OK"


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 apply_descriptions.py descriptions_approved.csv /path/to/content")
        sys.exit(1)

    csv_file = sys.argv[1]
    content_dir = sys.argv[2]

    if not os.path.isfile(csv_file):
        print(f"Error: {csv_file} not found")
        sys.exit(1)

    if not os.path.isdir(content_dir):
        print(f"Error: {content_dir} is not a directory")
        sys.exit(1)

    # Create backup directory
    backup_dir = f"descriptions_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    print(f"Backing up files to {backup_dir}/")

    results = []
    skipped = 0
    kept = 0
    updated = 0
    errors = 0

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Processing {len(rows)} rows from CSV...\n")

    for row in rows:
        relpath = row["file"].strip()
        proposed = row["proposed_description"].strip()

        # Skip internal files
        if relpath in SKIP_FILES:
            print(f"  SKIP (internal): {relpath}")
            skipped += 1
            continue

        # Skip empty proposed
        if not proposed:
            print(f"  SKIP (no proposed): {relpath}")
            skipped += 1
            continue

        # Keep existing for guide/quiz files
        if relpath in KEEP_EXISTING:
            print(f"  KEEP (existing better): {relpath}")
            kept += 1
            continue

        # Full path to file
        filepath = os.path.join(content_dir, relpath)
        if not os.path.isfile(filepath):
            print(f"  ERROR (file not found): {relpath}")
            errors += 1
            continue

        # Back up the file
        backup_path = os.path.join(backup_dir, relpath.replace("/", "_"))
        shutil.copy2(filepath, backup_path)

        # Patch the file
        success, msg = patch_file(filepath, proposed)
        if success:
            print(f"  UPDATED: {relpath}")
            updated += 1
        else:
            print(f"  ERROR ({msg}): {relpath}")
            errors += 1

    print(f"""
Done.
  Updated:  {updated}
  Kept existing: {kept}
  Skipped:  {skipped}
  Errors:   {errors}
  Backup:   {backup_dir}/

Next steps:
  1. Run: hugo --environment production 2>&1 | grep -i error
  2. Spot-check a few pages in your browser
  3. If anything looks wrong, restore from {backup_dir}/
  4. git add -A && git commit -m "Add AI-generated descriptions to all articles"
""")


if __name__ == "__main__":
    main()
