---
title: "Resizing Images — Mac"
date: 2026-05-03
layout: "members"
weight: 2
---

# Resizing Images — Mac

Two methods: Terminal (faster for multiple files) or Preview (no typing required).

---

## Method 1: Terminal — `sips`

`sips` is built into macOS — no installation needed.

Open Terminal and navigate to your article directory:

{{< highlight bash >}}
cd ~/Documents/Projects/NBAS/content/articles/2026/05/my-article
{{< /highlight >}}

Resize a single image to a maximum width of 2000px:

{{< highlight bash >}}
sips -Z 2000 m42.jpg
{{< /highlight >}}

Resize all JPGs in the current directory at once:

{{< highlight bash >}}
sips -Z 2000 *.jpg
{{< /highlight >}}

Resize all PNGs:

{{< highlight bash >}}
sips -Z 2000 *.png
{{< /highlight >}}

> `-Z 2000` sets the longest dimension to 2000px, preserving aspect ratio.
> The file is resized in place — the original is overwritten.
> If you want to keep the original, duplicate the file first.

---

## Method 2: Preview

1. Open the image in **Preview**
2. Go to **Tools → Adjust Size**
3. Make sure **Scale proportionally** is checked
4. Set **Width** to `2000` pixels (or less)
5. Click **OK**
6. Go to **File → Save** (not Save As — overwrite the original)

For multiple images, select them all in Finder, right-click and choose
**Open With → Preview**. All images open in one Preview window. Use
**Edit → Select All**, then **Tools → Adjust Size** to resize them together.

---

## Checking File Size

To check the file size of all images in your article directory:

{{< highlight bash >}}
ls -lh *.jpg *.png
{{< /highlight >}}

The size is shown in the fifth column. Aim for under 2MB per image.

---

## Reference

See [Media Guidelines](/members/media/guidelines/) for size limits and
supported formats.
