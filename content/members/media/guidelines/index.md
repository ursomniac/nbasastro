---
title: "Media Guidelines"
date: 2026-05-03
layout: "members"
weight: 1
---

# Media Guidelines

Images are stored inside your article directory alongside `index.md`.
Following these guidelines keeps the site fast and consistent.

---

## File Location

All media files go in the **same directory as your `index.md`**. Do not
put images in `static/` or anywhere else.

{{< highlight markdown >}}
content/articles/2026/05/my-article/
  index.md
  m42.jpg
  m42-detail.jpg
  setup.png
{{< /highlight >}}

---

## Size Limits

<div class="article-body">

| Type | Max width | Max file size |
|---|---|---|
| Photos / astro images | 2000px | 2MB |
| Screenshots / diagrams | 1400px | 1MB |
| Thumbnails | 800px | 500KB |

</div>

If your image exceeds these limits, resize it before adding it to your
article directory. See:

- [Resizing images on Mac](/members/media/resize-mac/)
- [Resizing images on Windows](/members/media/resize-windows/)

---

## Supported Formats

- `.jpg` / `.jpeg` — best for photographs and astro images
- `.png` — best for screenshots, diagrams, and images with transparency
- `.gif` — use sparingly, only for short animations
- `.webp` — acceptable, good compression

Avoid `.tiff`, `.bmp`, `.heic`, and `.raw` — these will not render correctly.

---

## File Naming

- Use lowercase letters, numbers, and hyphens only
- No spaces, no special characters, no uppercase
- Keep names short and descriptive

**Good:** `m42-orion-nebula.jpg`, `setup-diagram.png`, `jan-meeting.jpg`

**Bad:** `IMG_4823.JPG`, `My Photo (final).jpeg`, `M42 Orion Nebula FINAL v2.jpg`

---

## Video

Video files are **not** stored on the NBAS site. Upload your video to
YouTube first, then use the `nbas-video` shortcode to embed it.
See [nbas-video](/members/widgets/nbas-video/) for details.
