---
title: "Pathway 4 — CMS Editor"
date: 2026-05-03
layout: "members"
weight: 4
---

# Pathway 4 — CMS Editor

A browser-based editing pathway is on the roadmap. It would allow members
to write and submit articles entirely through a web interface — no local
installation, no ZIP files, no git commands.

**This pathway is not yet configured.** Pathways 1, 2, and 3 are all
fully documented and available now.

---

## The Options Under Consideration

### CloudCannon

[CloudCannon](https://cloudcannon.com) is a Git-based CMS with first-class
Hugo support. It connects directly to the NBAS GitHub repository and gives
editors a visual interface for writing articles, managing front matter fields,
and uploading media. Critically, it supports Hugo shortcodes — meaning
`nbas-image`, `nbas-gallery`, and the other widgets would be available in
the editor.

The main obstacle is cost — CloudCannon starts at $55/month with no free tier.

### Pages CMS

[Pages CMS](https://pagescms.org) is a free, open-source alternative that
connects to GitHub repositories with minimal setup. It handles Markdown
front matter and body content through a web interface.

The limitation for the NBAS site is that Pages CMS has no shortcode support.
Members using it would still need to hand-edit shortcode syntax for images,
galleries, and video — which reduces its advantage for non-technical users.

---

## Want to Be the Guinea Pig?

If you feel strongly about getting a CMS pathway working and are willing
to experiment, get in touch with the site administrator. The person who
figures it out writes the docs.

---

## In the Meantime

Use one of the three available pathways:

- [Pathway 1 — Full Git](/members/pathways/pathway-1/)
- [Pathway 2 — Local Preview](/members/pathways/pathway-2/)
- [Pathway 3 — No Setup](/members/pathways/pathway-3/)
