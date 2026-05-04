---
title: "nbas-image"
date: 2026-05-03
layout: "members"
weight: 1
---

# `nbas-image` — Single Image

Use `nbas-image` to place a single image in the flow of your article content.
The image file must be in your article's directory alongside `index.md`.

---

## Parameters

<div class="article-body">

| Parameter | Required | Description |
|---|---|---|
| `src` | Yes | Filename of the image |
| `align` | No | Float the image: `"left"` or `"right"` |
| `width` | No | Display width in pixels, e.g. `"400"` |
| `fullwidth` | No | Set to `"true"` to span the full content width |
| `caption` | No | Caption text shown below the image |
| `credit` | No | Credit line shown below the caption |

</div>

---

## Usage

**Centered image (default):**
{{< highlight markdown >}}
{{</* nbas-image src="m42.jpg" */>}}
{{< /highlight >}}

**Right-aligned with text wrap:**
{{< highlight markdown >}}
{{</* nbas-image src="m42.jpg" align="right" width="400" */>}}
{{< /highlight >}}

Place this shortcode _before_ the paragraph text you want to wrap around it.
Use `{{</* clear */>}}` after the paragraph to stop the text wrap.

**Full-width image:**
{{< highlight markdown >}}
{{</* nbas-image src="panorama.jpg" fullwidth="true" */>}}
{{< /highlight >}}

**With caption and credit:**
{{< highlight markdown >}}
{{</* nbas-image src="m42.jpg" align="right" width="400" caption="The Orion Nebula" credit="Jane Smith" */>}}
{{< /highlight >}}

---

## Notes

- Image files must be in the **same directory** as your `index.md`
- Supported formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- Resize large images before adding them — see [Media Guidelines](/members/media/guidelines/)
- After using `align="left"` or `align="right"`, use `{{</* clear */>}}` to
  prevent the next section wrapping awkwardly around the image

---

## Article Builder

The builder offers three image snippet options:

<div class="article-body">

| Builder option | Generates |
|---|---|
| Image (Aligned) | `nbas-image` with `align="right" width="400"` |
| Image (Centered) | `nbas-image` with no alignment |
| Image (Full Width) | `nbas-image` with `fullwidth="true"` |

</div>

Replace `file.png` with your actual filename in all cases.
