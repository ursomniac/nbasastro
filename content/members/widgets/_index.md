---
title: "Widgets & Shortcodes"
date: 2026-05-03
layout: "members"
weight: 4
---

# Widgets & Shortcodes

Shortcodes are small snippets you place in your article content to insert
media and formatted elements. Hugo processes them at build time — you never
write HTML yourself.

All NBAS shortcodes use this syntax:

{{< highlight markdown >}}
{{</* shortcode-name param="value" */>}}
{{< /highlight >}}

Some shortcodes wrap content between opening and closing tags:

{{< highlight markdown >}}
{{</* shortcode-name param="value" */>}}
...content...
{{</* /shortcode-name */>}}
{{< /highlight >}}

The Article Builder scaffolds the most common ones automatically.

---

## Available Shortcodes

<div class="article-body">

| Shortcode | Purpose |
|---|---|
| [nbas-image](/members/widgets/nbas-image/) | Single image in the content flow |
| [nbas-gallery](/members/widgets/nbas-gallery/) | Grid or carousel of multiple images |
| [nbas-video](/members/widgets/nbas-video/) | Embedded YouTube video |
| [object-specs](/members/widgets/object-specs/) | Side panel of object data |
| [article-table](/members/widgets/article-table/) | Formatted table in the content flow |
| [clear](/members/widgets/clear/) | Layout break to reset float and flow |

</div>
