---
title: "Markdown Basics"
date: 2026-05-03
layout: "members"
weight: 1
---

# Markdown Basics

Markdown is a lightweight way to format text using plain characters.
You only need to know six things to write a well-formatted article.

> **Just want to write prose?** Plain paragraphs of text under your front
> matter will render fine. Markdown is only needed when you want formatting.

---

## 1. Paragraphs

A blank line between blocks of text creates a new paragraph.

*Example:*
{{< highlight markdown >}}
This is the first paragraph.

This is the second paragraph.
{{< /highlight >}}

---

## 2. Headers

Start a line with `#` characters. More `#` means a lower-level header.
Use `##` for major sections and `###` for subsections within them.
Do not use `#` (H1) in your article body — the article title already uses it.

*Example:*
{{< highlight markdown >}}
## A Major Section
### A Subsection
#### A Minor Heading
{{< /highlight >}}

---

## 3. Bold and Italic

Surround text with `**double asterisks**` for bold, or `_underscores_` for italic.

*Example:*
{{< highlight markdown >}}
This is **bold text** and this is _italic text_ and this is **_bold and italic_**.
{{< /highlight >}}

---

## 4. Lists

For a bulleted list, start each line with `*` followed by a space.
For a numbered list, start each line with `1.`, `2.`, etc.
For a sub-item, indent with spaces (not tabs) before the `*` or number.

*Bulleted list example:*
{{< highlight markdown >}}
* First item
* Second item
  * Indented sub-item
  * Another sub-item
* Third item
{{< /highlight >}}

*Numbered list example:*
{{< highlight markdown >}}
1. First step
2. Second step
3. Third step
{{< /highlight >}}

> **Important:** Use spaces, not tabs, for indentation. Tabs will break rendering.

---

## 5. Special Characters and Emoji

Hugo does not allow raw HTML in article content, but supports HTML character
entities and UTF-8 characters including emoji.

*Example:*
{{< highlight markdown >}}
The object is 2&deg; above the horizon.
Angular size: &frac12; arcminute.
Observed with: 🔭
{{< /highlight >}}

---

## 6. Links

Surround the link text with `[brackets]` and follow immediately with the URL
in `(parentheses)`.

*Example:*
{{< highlight markdown >}}
Find out more at [the NBAS website](https://nbasastro.org).
{{< /highlight >}}

For internal links to other articles on the site, use the relative path:

{{< highlight markdown >}}
See our [M42 observation](/articles/2025/03/m42-orion-nebula/).
{{< /highlight >}}

---

## What Markdown Can't Do

Images, galleries, video, and tables are handled by NBAS shortcodes —
not raw Markdown. This keeps formatting consistent across the site.

See [Widgets & Shortcodes](/members/widgets/) for full documentation.
