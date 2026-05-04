---
title: "clear"
date: 2026-05-03
layout: "members"
weight: 6
---

# `clear` — Layout Break

`clear` is a utility shortcode that resets the text flow after a floated
image. It has no parameters and no visible output.

---

## Usage

{{< highlight markdown >}}
{{</* clear */>}}
{{< /highlight >}}

---

## When to Use It

Use `clear` after a section of text that wraps around an aligned image,
when you want the next section to start at full width below the image.

**Without `clear`:** the next section header or paragraph may appear
beside the image rather than below it.

**With `clear`:** the next section starts cleanly below the image.

{{< highlight markdown >}}
{{</* nbas-image src="nebula.jpg" align="right" width="350" */>}}

This paragraph wraps around the image to the left.

{{</* clear */>}}

## Next Section

This section now starts cleanly below the image.
{{< /highlight >}}

---

## Notes

- `clear` is only needed after `nbas-image` with `align="left"` or
  `align="right"` — centered and full-width images do not create a float
- If your layout looks wrong — text appearing beside an image when it
  shouldn't — adding `{{</* clear */>}}` before the problem section
  usually fixes it
- You can use `clear` as many times as needed in an article
