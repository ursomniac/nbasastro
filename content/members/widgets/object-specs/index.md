---
title: "object-specs"
date: 2026-05-03
layout: "members"
weight: 4
---

# `object-specs` — Object Data Panel

Use `object-specs` when your article is about a **single astronomical object**
and you want to display a summary data panel alongside the article text.
The panel reads its data from the `object_info:` block in your front matter.

---

## Usage

`object-specs` takes no parameters and contains no inner content:

{{< highlight markdown >}}
{{</* object-specs */>}}
{{< /highlight >}}

Place it near the top of your article body, right after `## Introduction`.
The panel floats alongside the following content.

---

## Setting Up the Front Matter

Use the **Object Specs** section in the Article Builder to define your data,
or add an `object_info:` block manually to your front matter.

Each row is a label and a value. Label names are flexible — use whatever
is relevant for the object type. Values must always be in quotes.

{{< highlight yaml >}}
object_info:
  type: "Emission Nebula"
  magnitude: "4.0"
  distance: "1,344 ly"
  constellation: "Orion"
  coordinates: "05h 35m / -05° 23'"
  best_seen: "Winter"
{{< /highlight >}}

> **Important:** Use spaces, not tabs, to indent the label/value pairs.
> Tabs will break the front matter.

---

## Common Fields by Object Type

**Deep Sky Objects:**
`type`, `magnitude`, `distance`, `constellation`, `coordinates`, `size`

**Planets:**
`type`, `diameter`, `distance`, `moons`, `orbital_period`, `best_seen`

**Stars:**
`type`, `magnitude`, `distance`, `spectral_class`, `constellation`

**Comets / Asteroids:**
`type`, `discovered`, `perihelion`, `magnitude_at_closest`

---

## Notes

- `object-specs` is for articles about a **single object**. For articles
  covering multiple objects, use the DSO/SSO front matter taxonomy fields
  instead — see [Front Matter Reference](/members/reference/front-matter/)
- If no `object_info:` block is present in the front matter, the shortcode
  renders nothing
