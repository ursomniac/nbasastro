---
title: "Submitting Articles"
date: 2026-04-22
layout: "members"
---

# How to Submit Your Content

To maintain the structural integrity and "Night-Vision" compatibility of the NBAS website, please follow one of the two methods below.

## Method 1: The ZIP Method (Recommended for most)
1. **Draft locally:** If you have the repo running, create your article in `content/articles/your-title.md`.
2. **Preview:** Run `hugo server` to ensure your images and layout look correct.
3. **Package:** Create a ZIP file containing:
   - Your `.md` file.
   - Any images used (ensure they are in `static/images/`).
4. **Send:** Email the ZIP to the Site Administrator.

## Method 2: The GitHub Workflow (Technical Members)
1. **Fork/Branch:** Create a feature branch (e.g., `feature/m31-observation`).
2. **Commit:** Only add files to `content/articles/` or `static/images/`.
3. **Pull Request:** Open a PR against the `main` branch. 
   *Note: All PRs undergo an automated build check. If the build fails, check your shortcode syntax.*

---

## Technical Constraints
- **Styling:** Do NOT use `<style>` tags or inline `style=""` attributes.
- **Top Matter:** Use the `topmatter` shortcode for introductions:
  `{{< topmatter >}} Your text here {{< /topmatter >}}`
- **Images:** Use the `nbas-media` shortcode for consistent borders and captions.

