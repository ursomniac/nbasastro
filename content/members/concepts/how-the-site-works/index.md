---
title: "How the Site Works"
date: 2026-05-03
layout: "members"
weight: 1
---

# How the Site Works

Before writing your first article, a few concepts will make everything else
click into place.

---

## The Big Picture

The NBAS site is a **static site** built with a tool called Hugo.
Every page is pre-built as plain HTML before anyone visits it —
no database, no login system, no moving parts at runtime. The result
is a site that is fast, reliable, and collaborative.

The tradeoff is that adding content requires a small amount of structure.
That's what these docs are here to explain.

---

## The Building Block: The Article

Everything on the site is built from **Articles**. An Article is a page —
it can contain text, images, video, tables, and more.

What makes an Article powerful is its **metadata** (also called *front matter*):
a block of structured information at the top of the file that tells Hugo how
to categorize, link, and display the page across the entire site.

You don't write this metadata by hand. The
[Article Builder](/members/article-builder/) generates it for you.

---

## Site Sections

Most sections are collections of Articles filtered and arranged in different
ways. The key ones:

**All Articles** — Every published article, newest first.

**Tags** — Every article can have one or more tags. Hugo automatically creates
a page for each tag. You don't register a new tag — just use it and the page appears.

**DSO Catalog** — Articles linked to Deep Sky Objects are grouped here,
subdivided into Messier, Caldwell, NGC, and Other. Write about M 42 and it
appears on the M 42 page alongside every other article that references it.

**Solar System** — Same idea for Solar System Objects: Sun, Moon, Planets,
Comets, Asteroids, and Meteors.

**Knowledge Hub** — Topical grouping for educational content: Astronomy,
Education, Observing, Technology.

---

## Series

An Article can be part of a **Series** — a named collection of related
articles with no required schedule. The NBAS Newsletter is a Series.
So are Event pages, Announcements, and Constellation Highlights.

To start a new Series, name it in your article's metadata. Every article
that uses the same Series name gets grouped together automatically.

---

## Tags

Tags connect articles on a common subject regardless of when they were
written or what section they're in.

**Example:** You image a supernova in M 101. You tag the article `Supernova`
and also reference M 101 in the DSO metadata. Your article now appears in:

- All Articles
- The M 101 DSO page
- The Supernova tag page
- The Home page (as recent content)

All of that cross-referencing happens automatically from metadata you set once.

---

## What You Actually Have to Do

1. Generate a starting `index.md` with the [Article Builder](/members/article-builder/)
2. Write your content — see [Markdown Basics](/members/reference/markdown-basics/)
3. Add your media to the article directory
4. Submit via your chosen [pathway](/members/pathways/)

The site handles everything else.
