---
title: "nbas-gallery"
date: 2026-05-03
layout: "members"
weight: 2
---

# `nbas-gallery` — Image Gallery

Use `nbas-gallery` to display a collection of images as either a scrollable
**carousel** or a static **grid**. Each image is defined by a line inside
the shortcode block.

---

## Parameters

<div class="article-body">

| Parameter | Required | Description |
|---|---|---|
| `type` | Yes | Display mode: `"grid"` or `"carousel"` |

</div>

---

## Image Entry Format

Each line inside the shortcode block defines one image.
The three fields are separated by `|` (pipe characters):

{{< highlight markdown >}}
filename | caption | credit
{{< /highlight >}}

- **filename** — required. Must match the file in your article directory exactly.
- **caption** — optional but recommended.
- **credit** — optional. Photographer or source credit.

Leave a field blank by leaving nothing between the pipes:

{{< highlight markdown >}}
image.jpg | | Photo credit here
{{< /highlight >}}

---

## Usage

**Grid:**
{{< highlight markdown >}}
{{</* nbas-gallery type="grid" */>}}
ngc891.jpg | Edge-on galaxy NGC 891 | Jane Smith
ngc891-crop.jpg | Core detail | Jane Smith
{{</* /nbas-gallery */>}}
{{< /highlight >}}

**Carousel:**
{{< highlight markdown >}}
{{</* nbas-gallery type="carousel" */>}}
jan-meeting.jpg | January meeting setup |
speaker.jpg | Dr. Evans presenting | NBAS
q-and-a.jpg | Q&A session |
{{</* /nbas-gallery */>}}
{{< /highlight >}}

---

## Grid vs. Carousel

**Grid** — All images displayed at once in a tiled layout. Best for a set
of related images the reader will scan. Works well for 3–12 images.

**Carousel** — One image at a time with prev/next controls. Best for a
sequence where order matters, or for a large set of images.

---

## Notes

- All image files must be in the **same directory** as your `index.md`
- The order of lines determines the display order
- Resize large images before adding them — see [Media Guidelines](/members/media/guidelines/)

---

## Article Builder

The builder offers two gallery snippet options — Grid and Carousel — each
generating a block with one placeholder row. Add one line per image inside
the block and replace `image1.png` with your actual filenames.
