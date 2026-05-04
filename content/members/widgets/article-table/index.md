---
title: "article-table"
date: 2026-05-03
layout: "members"
weight: 5
---

# `article-table` — Formatted Table

Use `article-table` to insert a table into your article, styled consistently
with the rest of the site. The table content is written in standard Markdown
table syntax inside the shortcode block.

---

## Usage

{{< highlight markdown >}}
{{</* article-table */>}}
| Column 1 | Column 2 | Column 3 |
|---|---|---|
| Row 1A | Row 1B | Row 1C |
| Row 2A | Row 2B | Row 2C |
{{</* /article-table */>}}
{{< /highlight >}}

---

## Markdown Table Format

A Markdown table has three parts:

1. A **header row** — column names separated by `|`
2. A **separator row** — `|---|` for each column
3. One or more **data rows**

Column widths are set automatically — you do not need to align the `|` characters.

---

## Example: Observation Log

{{< highlight markdown >}}
{{</* article-table */>}}
| Date | Object | Instrument | Seeing | Notes |
|---|---|---|---|---|
| 2026-01-14 | M 42 | 12" Dob | Good | Best view this season |
| 2026-01-14 | M 43 | 12" Dob | Good | Faint but resolved |
| 2026-01-22 | NGC 1977 | 12" Dob | Fair | Running Man visible |
{{</* /article-table */>}}
{{< /highlight >}}

---

## Notes

- Raw Markdown tables outside of this shortcode will not have NBAS site
  styling applied — always use `article-table` for consistency
- Keep tables reasonably narrow — very wide tables may not display well
  on mobile screens
- The Article Builder does not scaffold this shortcode — copy the syntax
  above and edit it in your text editor
