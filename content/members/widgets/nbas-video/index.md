---
title: "nbas-video"
date: 2026-05-03
layout: "members"
weight: 3
---

# `nbas-video` — Embedded Video

Use `nbas-video` to embed a YouTube video in your article.
Video files are **not** stored on the NBAS site — all video is hosted on
YouTube and embedded by reference.

---

## Parameters

<div class="article-body">

| Parameter | Required | Description |
|---|---|---|
| `id` | Yes | The YouTube video ID (see below) |
| `title` | Yes | A title for the video, used for accessibility |

</div>

---

## Finding the YouTube Video ID

The video ID is the string of characters after `v=` in a YouTube URL.

{{< highlight markdown >}}
https://www.youtube.com/watch?v=dQw4w9WgXcQ
                                ^^^^^^^^^^^^ this is the ID
{{< /highlight >}}

For shortened URLs, the ID is the part after the `/`:

{{< highlight markdown >}}
https://youtu.be/dQw4w9WgXcQ
                 ^^^^^^^^^^^^ this is the ID
{{< /highlight >}}

---

## Usage

{{< highlight markdown >}}
{{</* nbas-video id="abc123XYZ" title="Jupiter Opposition — May 2026" */>}}
{{< /highlight >}}

---

## Notes

- The video must be **published on YouTube** before it can be embedded
- You do not need to upload any video files to your article directory
- Place the shortcode where you want the video to appear in the reading flow
- The embed respects the site's night-vision color scheme

---

## Article Builder

Check **Video** in the Content Snippets section. The builder generates a
placeholder with `id="ID"` and `title="Title"` — replace both with your
actual YouTube video ID and a descriptive title.
