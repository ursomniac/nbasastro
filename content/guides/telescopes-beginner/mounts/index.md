---
title: "Telescopes: Mounts"
navtext: "Mounts"
byline: "The part nobody talks about until it ruins their night"
description: "Understanding telescope mounts — the part that holds your telescope steady and determines how you move it across the sky."
date: 2026-06-05
weight: 20
layout: guide_child
guide_child: true
series:
  - getting-started
build:
  list: local
draft: false
---

The mount is the part of your telescope that nobody talks about
until it ruins their night. A bad mount — one that wobbles, drifts,
or fights you when you try to point it — makes observing miserable
regardless of how good the optics are. A good mount disappears into
the background and lets you focus on the sky.

There are two fundamental mount types, with motorized variants of each.

{{< nbas-image src="mount-comparison.jpeg" align="center" caption="Left to right: alt-azimuth (refractor), alt-azimuth (Dobsonian), and equatorial mounts." >}}

## Alt-Azimuth Mounts

An alt-azimuth mount moves in two directions: up-down (altitude)
and left-right (azimuth). It's the most intuitive design — point
it the way you'd point a camera on a tripod. No special knowledge
required to get started.

Alt-az mounts are lighter, simpler, and less expensive than equatorial
mounts of equivalent quality. They're the natural choice for
beginners, casual observers, and anyone who prioritizes portability.

The limitation is tracking. As Earth rotates, objects drift across
the sky — and an alt-az mount has to move in both axes simultaneously
to follow them. Without a motor this means constant nudging; with
a motor it works fine for visual observing but causes **field
rotation** for imaging (more on that below).

**Dobsonians are alt-az mounts** — just a particularly elegant and
stable implementation of the design. A Dob's rocker box is an alt-az
mount optimized for large, heavy tubes at low cost. For visual
observing, it's arguably the best mount design ever made. For those
who want tracking on a Dob without buying a new telescope, an
**equatorial platform** (a motorized wedge that tilts the entire
rocker box) is a niche but effective solution.

**Pros:** Simple to use, lighter, less expensive, more portable.
**Cons:** No tracking without a motor, field rotation makes long-exposure imaging impractical.

## Equatorial Mounts

An equatorial mount is tilted so that one axis — the **right ascension
(RA) axis** — is parallel to Earth's rotational axis. This means a
single slow rotation of that one axis can follow any object across
the sky perfectly, compensating for Earth's rotation.

This makes equatorial mounts essential for astrophotography and
very convenient for extended visual observing sessions, where you'd
otherwise constantly nudge the telescope to keep objects in view.

The tradeoff is complexity and weight. Equatorial mounts require
**polar alignment** — pointing the RA axis at the celestial pole
(near Polaris in the northern hemisphere) before observing. It
sounds intimidating but is entirely learnable; a rough polar alignment
takes five minutes and is good enough for visual observing, while
a precise alignment for imaging takes longer and involves a few
well-documented techniques.

Equatorial mounts are also heavier and bulkier than alt-az mounts
of equivalent stability, and significantly more expensive.

{{< nbas-image src="polar-alignment.jpg" align="right" width="350" caption="Polar alignment points the mount's axis at the celestial pole, allowing single-axis tracking." >}}

**Pros:** Single-axis tracking, ideal for astrophotography, no field rotation.
**Cons:** Heavier, more complex, requires polar alignment, more expensive.

## Field Rotation

{{< nbas-image src="field-rotation.jpg" width="350" align="right" >}}
When an alt-az mount tracks an object using motors on both axes,
the image slowly rotates in the field of view. For visual observing
this is invisible and irrelevant. For astrophotography — where you
stack many exposures taken over several minutes — field rotation
causes stars at the edges of the frame to trail in arcs, ruining
the image.

Equatorial mounts don't have this problem because their tracking
axis is aligned with Earth's rotation, so the image stays fixed.

This is the primary reason serious astrophotographers use equatorial
mounts, and why alt-az mounts — however convenient for visual use
— have limits for imaging. Smart scopes handle field rotation in
software to varying degrees; see the [Smart Scopes](/guides/telescopes/beginner/smart/) 
page for more on that.

## GoTo Mounts

GoTo mounts add a computerized pointing system to either alt-az or
equatorial designs. After a brief alignment procedure (usually
pointing at two or three known stars), the mount can automatically
slew to any object in its database — thousands of galaxies, nebulae,
star clusters, planets, and more — at the push of a button.

For beginners, GoTo can be genuinely liberating. Finding faint
objects by star-hopping takes practice and patience; GoTo removes
that barrier entirely and lets you spend your time observing rather
than hunting.

The counterargument is that learning to navigate the night sky
manually builds a deeper understanding of how it works, and that
knowledge makes you a better observer. Both positions have merit.
GoTo doesn't prevent you from learning the sky — it just doesn't
force you to.

GoTo is available at all price levels, from modest alt-az beginners'
scopes to high-end equatorial imaging platforms. As with most things
in astronomy, you get what you pay for: budget GoTo systems can be
slow and imprecise, while quality systems are fast, accurate, and
genuinely impressive.  

## Which Mount Is Right for You?

A few straightforward guidelines:

- **Visual observing, portability a priority, keeping it simple:** Alt-az, or a Dobsonian if you want maximum aperture.
- **Visual observing, want to find objects easily without learning star-hopping:** GoTo alt-az.
- **Serious about astrophotography from the start:** Equatorial with a motor drive. Budget accordingly — a good equatorial mount costs as much as or more than the telescope it carries.  "Smart" scopes mostly have an alt/az mount:  some like the Seestar series can be mounted equatorially (you have to purchase that separately, but it's an upgrade path that many people do).
- **Not sure yet:** Start with a good alt-az or Dobsonian. You can always add tracking and upgrade later once you know what you want.

The mount is not the place to cut corners. A stable, smooth mount on a modest telescope is far more satisfying than a shaky mount under a great one.

