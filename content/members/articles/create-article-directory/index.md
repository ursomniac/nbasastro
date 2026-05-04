---
title: "Creating Your Article Directory"
date: 2026-05-03
layout: "members"
weight: 1
---

# Creating Your Article Directory

Every article on the NBAS site lives in its own directory. The directory
holds your `index.md` file and all media associated with the article.

---

## Directory Location

Articles go under `content/articles/` organized by year and month:

{{< highlight markdown >}}
content/articles/YYYY/MM/your-article-name/
{{< /highlight >}}

For example, an article written in May 2026:

{{< highlight markdown >}}
content/articles/2026/05/my-observation-of-m42/
{{< /highlight >}}

---

## Naming Your Directory

The directory name becomes part of the article's URL on the site.
Follow these rules:

- Lowercase letters, numbers, and hyphens only
- No spaces, no special characters, no uppercase
- Keep it short and descriptive
- Use the article subject, not the date (the date is already in the path)

**Good:** `m42-orion-nebula`, `january-meeting-recap`, `perseids-2026`

**Bad:** `My Article`, `article1`, `IMG_final`, `m42_orion_nebula`

---

## Creating the Directory

**On Mac (Terminal):**

{{< highlight bash >}}
mkdir -p ~/Documents/Projects/NBAS/content/articles/2026/05/my-article-name
{{< /highlight >}}

**On Windows (File Explorer):**

Navigate to `content/articles/2026/05/` and create a new folder with your
chosen name.

**On Windows (PowerShell):**

{{< highlight bash >}}
New-Item -Path "$HOME\Documents\Projects\NBAS\content\articles\2026\05\my-article-name" -ItemType Directory
{{< /highlight >}}

---

## After Creating the Directory

1. Move your downloaded `index.md` (from the Article Builder) into the directory
2. Add your image files to the same directory
3. Your directory should look like this:

{{< highlight markdown >}}
content/articles/2026/05/my-article-name/
  index.md
  main-image.jpg
  detail-shot.jpg
{{< /highlight >}}

---

## Reference

- [Article Builder](/members/article-builder/) — generate your `index.md`
- [Media Guidelines](/members/media/guidelines/) — image naming and size limits
