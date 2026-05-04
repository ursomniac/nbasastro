---
title: "Front Matter Reference"
date: 2026-05-03
layout: "members"
weight: 2
---

# Front Matter Reference

Every article begins with a block of metadata called **front matter** — the
lines between the two `---` markers at the top of `index.md`. Hugo reads this
to build the page and link it to the rest of the site.

The [Article Builder](/members/article-builder/) generates this for you.
Use this page if you need to add or correct a field after the fact.

---

## Editing Front Matter Safely

Open `index.md` in a plain text editor (not Word or Pages).
Front matter is sensitive to formatting — follow these rules:

- Strings go in `"double quotes"`
- Lists go in `["square", "brackets"]`
- Dates have **no quotes**: `date: 2026-05-03`
- Use **spaces, not tabs** for indentation
- A typo here can prevent the page from building — check carefully

---

## Required Fields

These four fields must be present in every article.

**title**
{{< highlight yaml >}}
title: "My Article Title"
{{< /highlight >}}
The title shown in all listing pages and the page header.

**date**
{{< highlight yaml >}}
date: 2026-05-03
{{< /highlight >}}
Publication date. No quotes. Set a future date to schedule the article —
it will not appear on the site until that date.

**authors**
{{< highlight yaml >}}
authors: ["Jane Smith"]
{{< /highlight >}}
Your name as you want it to appear. Multiple authors are comma-separated
inside the brackets.

If you have an author profile page on the site, use your slug instead:
{{< highlight yaml >}}
authors: ["jane-smith"]
{{< /highlight >}}
The slug links your article to your profile and bio, and groups all your
articles together. Use it consistently — `"Jane Smith"` and `"jane-smith"`
will not be recognized as the same author.

**byline**
{{< highlight yaml >}}
byline: "A short teaser sentence shown under the title in listing cards."
{{< /highlight >}}

---

## Optional Fields

These fields are omitted entirely when not needed.

**series**
{{< highlight yaml >}}
series: ["constellation-highlights"]
{{< /highlight >}}
The series slug this article belongs to. The series must already exist.
Contact the site admin to register a new series.

**tags**
{{< highlight yaml >}}
tags: ["deep-sky", "nebula", "imaging"]
{{< /highlight >}}
Comma-separated list of tags. New tags create their own pages automatically.

**knowledgetopics**
{{< highlight yaml >}}
knowledgetopics: ["astronomy", "observing"]
{{< /highlight >}}
Valid values: `astronomy`, `education`, `observing`, `tech`.

**thumbnail**
{{< highlight yaml >}}
thumbnail: "myimage.jpg"
{{< /highlight >}}
Image filename (in the article directory) to use as the listing card thumbnail.
If omitted, a default icon is used.

---

## Astronomy Taxonomy Fields

These fields place your article on the DSO and Solar System catalog pages.
All values go in lists, even if there is only one.

**Deep Sky Objects:**
{{< highlight yaml >}}
dso_messier: ["42", "43"]
dso_caldwell: ["14"]
dso_ngc: ["1977", "1980"]
dso_other: ["PK 9-7.1"]
{{< /highlight >}}
Use catalog numbers only — not full names. For Messier, use `"42"` not `"M 42"`.

**Solar System Objects:**
{{< highlight yaml >}}
sso_planets: ["Jupiter", "Mars"]
sso_meteors: ["Perseids"]
sso_comets: ["C/2023 A3"]
sso_asteroids: ["Vesta"]
{{< /highlight >}}

**Stars:**
{{< highlight yaml >}}
stars_variable: ["Mira"]
stars_nearby: ["Proxima Centauri"]
stars_bright: ["Sirius", "Spica"]
stars_multiple: ["Albireo"]
stars_exotic: ["Sgr A*"]
{{< /highlight >}}

---

## Object Info (Single Object Articles)

Use this when writing about a single object and you want a data panel
rendered by the `object-specs` shortcode.

{{< highlight yaml >}}
object_info:
  type: "Planetary Nebula"
  magnitude: "8.8"
  distance: "2,300 ly"
  constellation: "Lyra"
  coordinates: "18h 53m / +33° 02'"
{{< /highlight >}}

Label names are flexible — use whatever is relevant for the object.
Values are always strings in quotes. Use spaces, not tabs, for indentation.

---

## A Complete Example

{{< highlight yaml >}}
---
title: "The Ring Nebula — M 57"
date: 2026-05-03
byline: "A perfect smoke ring in Lyra."
authors: ["jane-smith"]
tags: ["planetary-nebula", "lyra", "imaging"]
knowledgetopics: ["observing"]
dso_messier: ["57"]
object_info:
  type: "Planetary Nebula"
  magnitude: "8.8"
  distance: "2,300 ly"
  constellation: "Lyra"
  coordinates: "18h 53m / +33° 02'"
---
{{< /highlight >}}
