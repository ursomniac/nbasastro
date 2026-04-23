---
title: "Articles"
date: 2026-04-22
layout: "members"
---

# All About Articles

**THE BAD NEWS** - you have to learn Markdown

**THE GOOD NEWS** - it's not hard

## The layout of index.md

Each article index.md file has two parts:

* the Metadata
* the Content

Let's do the content first.  It's easier.

## Content

### Markdown

Strictly speaking you don't need _any_ Markdown, you could just put a lot of paragraphs
of text in the file (under the Metadata) and the page would render.  It just wouldn't look
very good.   While _mastering_ Markdown involves a lot of complicated syntax, fortunately,
unless you're trying to do something _very_ particular, there are only a few things you
need to know:

#### 1. **Headers**: in Markdown you just start a line with one or more "#" characters followed by the title.  The more "#" there are the lower-level header is it (if you know HTML,
this is the SAME things as H1, H2, H3, etc.).   

So you'd use "# My Main Title" at the top.  If you want to break things down into 
sections with a title: "## Lots of People!",  "## What we Saw" -- you get the idea and
if you want sections within sections, "### some minor section", and so on.

Easy.  Done.

#### 2. Text Highlighting:

* surround text with underscores for _italics_
* surround text with two asterisks for **bold**

#### 3. Lists: 

Here the syntax is a little weird.  There are two kinds, numbered and bulleted.

For numbered lists, just put a number and a dot and the text (1. first thing, etc.)
The "weird" part is that it doesn't care WHAT the number is, but generally you want
to do 1,. 2., 3., etc.  

For bulleted lists, it's an asterisk '*'.

So: 
1. here's a numbered list
2. with another thing
3. and something else

* here's a bulleted list
* and another thing
* and something else.
   * and I just threw curveball!
   * How did I do THAT?

To get a list in a list, just add a few spaces (not tabs!) at the beginning of
the line under a list item with another number/bullet.   Markdown does all the 
indenting and formatting for you.

#### 4. HTML

Markdown itself lets you put in raw HTML, but **Hugo ignores it**!

It **does** allow character entities, though.  So, you can do "&beta" and "&frac12"
and all those things.  UTF-8 is also allowed so you can put in 🔭 or 🌝 or any other 
emoji no problem.

#### 5. Tables, Links, etc.

Yes - you can do it all - but at this point I'd say "look up a good 
Markdown documentation page in Google" is the best way to do that.

#### 6. Media

This isn't Markdown per se - we've made snippets for all of that, and there are
separate docs for each of them.

### Metadata

OK - this is a little hairy because it looks "weird" and - if you mess something up,
chances are you'll crash the website (well, your local website).  But that's Hugo.

Let's look at a SIMPLE case:

```
---
title: "Launching the NBAS Website"
date: 2026-04-12
authors: ["NBAS Staff"]
byline: "A new way to stay connected with the stars in the Northern Berkshires."
series: ["nbas-announcement"]
tags: ["Digital"]
thumbnail: "icon.jpg"
---
```

The Metadata is the stuff between the two '---' lines (yes, they're part of the file).
The syntax for all of these is (unforunately) VERY important.  Some are strings, 
some are lists of string, others (not in this example) are _indented_ 
(with spaces, NOT TABS - that's one of the "oops" that will crash the site)

* `title: "PUT MY TITLE HERE"` - sets the title shown on all the listing pages.
* `date: YYYY-MM-DD` - _NOTE_ no quote marks.
    * Yes, you can set a date in the future!
    * IF you do this, then the article "won't go live" on the site until then.
* `byline: "some more text in quotes"` - this will put the little blurb under the title
* `authors: ["me", "co-author", "co-author2"]`
    * Most of the time you're the only author
    * This is another "weird" thing you can do this one of two ways:
        * ["John Smith"] shows up under Author, and there MIGHT be a link to a page with all the other pages written by "John Smith" (but no guarantee they'll all be there).
        * ["john-smith"] shows up under Author, with a link to all of "john-smith"'s articles AND the Bio for John Smith (which is another page under `content/authors/john-smith`.
* `series: ["slug-for-the-series"]` - here the Series has to be registered.  
* `tags: ["tag1", "tag2", "tag3"] - assigns your article to those Tags. 
* `icon: "myimage.jpg"` - OPTIONAL: if you put in one of your images here, then in listings the icon will be a small version of that image.  Otherwise it picks a default icon.

But lots of other things can be in the metadata (depending on the type of article).

#### A Crazy Case:

Without going into the gory details, for a Constellation Highlight page has a LOT
of metadata - pretty much the kitchen sink.

```
---
layout: "single-constellation"
title: "Sagittarius"
date: 2024-08-07
authors: ["nbas-staff"]
series: ["constellation-highlights"]
constellations: ["Sagittarius"]
byline: "Looking to the center of our Galaxy"
description: "Things to learn about the Sagittarius constellation"
thumbnail: "icon.jpg"

# Constellation Profile Panel
profile_data:
  "Abbreviation": SGR
  "Genitive": Sagitarii
  "Best Viewed": Summer
  "Hemisphere": Southern
  "Brightest Star": Kaus Australis
  "Area": 867 sq degrees

# Taxonomy refs:
stars: ["Sgr A"]
catalogs: ["messier", "ngc", "caldwell", "other"]
object_sections:
  messier: ["17", "20", "21", "22"]
  ngc: ["6822"]
  caldwell: ["57"]
  other: ["PK 9-7.1"]
solarsystem: ["planets", "meteor_showers"]
  planets: ["Uranus", "Neptune"]
  meteor_showers: ["Taurids"]

# The 6 Objects of Interest Table
highlights:
  - name: "Messier 17"
    type: "Emission Nebula"
    using: "Binoculars/Small Telescope"
  - name: "Messier 20"
    type: "Emission/Reflection Nebula"
    using: "Binoculars/Small Telescope"
  - name: "Messier 22"
    type: "Globular Cluster"
    using: "Naked Eye/Binoculars"
  - name: "Caldwell 57 (NGC 6822)"
    type: "Dwarf Galaxy"
    using: "Medium/Imaging Telescopes"
  - name: "Messier 21"
    type: "Open Cluster"
    using: "Binoculars"
  - name: "Sgr A"
    type: "Galactic Center"
    using: "Naked Eye/Binoculars"
---
```

But here are ALSO the examples of "what to do with DSOs and SSOs".

* **DSO**s: use `catalogs: ["messier", etc.] for the catalogs you want to reference
    * then for each one: e.g., `messier: ["17", "20", "24"], etc.
* **SSO**s: use `solarsystem: ["planets", "moon", "comets", etc.] for the types you want to reference,
    * then for each one: e.g., `planets: ["Saturn"]`

_That_ handles putting your Articles under "DSO Catalog" and "Solar System" pages.

**We will have templates for all of the most common cases, so you should just have to 
cut/paste it into place and "fill in the blanks"!**
