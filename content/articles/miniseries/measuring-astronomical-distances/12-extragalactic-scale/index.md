---
title: "Beyond the Local Group: The Universe in Megaparsecs"
date: 2027-02-15
description: "Past the Local Group, distances jump to megaparsecs. A tour of our larger neighborhood -- the M 81 and Sculptor groups, the Virgo and Coma clusters, the walls and voids between them -- and how far each of our distance rulers can actually reach."
byline: "Our extragalactic neighborhood, measured with the rungs we just built"
authors: ["bob-donahue"]
series: ["wider-view"]
tags: ["Local Void", "Galaxy Clusters"]
thumbnail: "thumbnail.webp"
banner: "banner2.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 12

dso_messier: ["49", "61", "64", "81", "82", "83", "84", "86", "87", "88", "91", "94", "99", "100"]
dso_caldwell: ["5", "65"]
dso_ngc: ["253", "4435", "4438", "4874", "4889", "7793"]
dso_other: ["IC 342", "Maffei 1", "Maffei 2"]

---
<!--
D12 v20 (2026-11-16, Claude): thumbnail.webp (600 px, banner crop); v19 + footnotes in the series style (33, incl. Stellarium, ZCAT, UNGC credits).
D12 v19 (2026-11-16, Claude): editorial pass on Bob's v18.
  - Banner caption: Stellarium colour-legend placeholder removed ("Small ellipses mark galaxies").
  - LINK:extending-the-ladder → /articles/2027/02/extending-the-ladder-beyond-the-cepheids/
    (from article 11's title + date, Hugo's usual slug; check it resolves on the local build).
  - Virgo: map caption "pictured below" → "above" (carousel is above it); old commented-out
    M 87/M 49 pair removed.
  - Supergalactic paragraph: "sky map above" → "below" (fig-sky-directions now follows it).
  - Spring-sky section: {{< clear >}} after the IC 342 float.
  - Wrapup: side view stays (Bob's v18); the placement NOTE removed.
  - Small wording: intro "seen whole / observe as a whole" repeat; dinosaurs sentence; byline
    "extragalactic"; rulers table points to galaxy 3 in the Coma image.
  - dso metadata: + M 91 (in the carousel). Maffei 1 and 2 kept (Bob: doable with a smart scope).
Facts: claude/extragalactic-scale-facts.md (rounds 1–4) + claude/extragalactic-scale-facts-r5.md.
-->

## Introduction

{{< nbas-image src="banner2.webp" fullwidth="true"
caption="The spring sky around the North Galactic Pole (+). Small ellipses mark galaxies bright enough for the chart to show. Gold circles: the Virgo Cluster, about 10° across, and the Coma Cluster, whose galaxies are too faint to appear at this scale. Cyan: galaxies named in this article.[^stellarium]"
alt="A star chart of the spring sky from Virgo and Hydra to Ursa Major and Leo, with constellation lines and dozens of small ellipses marking galaxies. A large gold circle surrounds a dense knot of ellipses between Virgo and Leo, labeled Virgo Cluster, with Markarian's Chain circled inside it. A small gold circle just above the North Galactic Pole marks the Coma Cluster. Cyan labels name M 64, M 94, M 51, M 81 and M 82, M 104, M 83, the Leo Triplet and the M 96 group." >}}

The [last article](/articles/2027/02/extending-the-ladder-beyond-the-cepheids/) built the upper rungs of the distance ladder: the
tip of the red giant branch, Tully-Fisher, and Type Ia supernovae. Each was calibrated on the rung
below it, and each reaches farther. A tool is only interesting for what it lets you do. This time
we use them.

What they show is a universe that is not spread out evenly. Leave the Local Group and you find
small groups like ours strung along thin sheets and filaments, a few enormous clusters where the
filaments meet, and between them voids: regions tens of megaparsecs across with very little in
them.

None of it can be seen whole. You can image a piece -- a few galaxies in Virgo, a field of faint
smudges in Coma -- but the structure itself is something we infer, not something we can look at. So
we'll take it in stages: the ruler, then the neighborhood from nearest to farthest, then how crowded
and how empty it gets, and finally how far each of our rulers really reaches.

---

## The Megaparsec (and the Million Light-Years)

Inside the Local Group, the natural ruler was the kiloparsec: the Milky Way and Andromeda sit about
760 kpc apart, roughly 2.5 million light-years. Beyond it, distances jump by factors of ten and a
hundred, and the natural unit becomes the **megaparsec**, a million parsecs.

> 1 Mpc = 3.26 million light-years (Mly)

{{< article-table align="right" >}}

| Place | Distance | |
|---|---|---|
| Andromeda | 0.76 Mpc | 2.5 Mly |
| M 81 group | 3.6 Mpc | 12 Mly |
| Virgo Cluster | 16.5 Mpc | 54 Mly |
| Coma Cluster | ~100 Mpc | ~330 Mly |
| Hercules Cluster | ~156 Mpc | ~510 Mly |

{{< /article-table >}}

We'll use both units, for the reason we gave when we [chose two units on
purpose](/articles/2026/12/parsecs-vs.-light-years/): the parsec is the astronomer's ruler, and the
light-year tells the story. Here's the story version. The Virgo Cluster is about 16.5 Mpc away --
54 million light-years -- so the light reaching your telescope tonight has been travelling for 54
million years. When it set out, the dinosaurs had already been gone for twelve million years (the
extinction is dated to 66.04 million years ago)[^kpg], and the world it left behind was recognizably
mammal-ruled. And that's the *nearest* big cluster.

The table at right is the outline of the tour. Each step is several times farther than the last,
each is measured with a different rung from the last article, and each rung is a little rougher
than the one before.

{{< clear >}}

{{< nbas-image src="fig-scale-strip.webp" fullwidth="true"
caption="From Andromeda to the Hercules Cluster on a logarithmic scale, each stop labeled with the method that measured its distance. The farther the stop, the rougher the ruler."
alt="A horizontal strip on a logarithmic distance scale from 0.5 to 300 megaparsecs. Gold dots mark Andromeda at 0.76 Mpc and the M 81 group at 3.6 Mpc (Cepheids and red giants), the Virgo Cluster at 16.5 Mpc (surface brightness fluctuations), the Coma Cluster at about 100 Mpc (Type Ia supernovae) and the Hercules Cluster at about 156 Mpc (Tully-Fisher, 39 spirals)." >}}

---

## The Nearest Groups

Step outside the Local Group in almost any direction and the first thing you meet is nothing.
Between us and the M 81 group lies the nearest cosmic mini-void, a region about 3 Mpc across with
no bright galaxies in it.[^minivoid] Our group sits in a clearing.

### M 81 and its group

{{< nbas-image src="m_82-equ-20m.webp" width="360" align="right"
caption="M 82, eQuinox 2, 20 min"
alt="The edge-on starburst galaxy M 82, a bright elongated streak crossed by dark dust." >}}
{{< nbas-image src="m_81-equ-35m.webp" width="360" align="right"
caption="M 81, eQuinox 2, 35 min"
alt="The spiral galaxy M 81, an oval with a bright core and fainter spiral arms." >}}
{{< clear >}}

On the far side of that clearing is the **M 81 group**, at about 3.6 Mpc (12 Mly). M 81 is one of
the best-measured galaxies outside the Local Group: Cepheids found by the Hubble Space Telescope and
the tip of the red giant branch -- two independent rungs -- agree on its distance to about five
percent.[^m81] Its companion M 82, the starburst galaxy with the ragged red plumes, is at the same
distance, and the two are interacting. Around them are dozens of dwarfs with red-giant distances of
their own.

### Sculptor: a group that turned into a filament

{{< nbas-image src="ngc_7793-s50-21m.webp" width="360" align="right"
caption="NGC 7793, Seestar S50, 21 min"
alt="The spiral galaxy NGC 7793, a soft oval glow with a patchy, loosely wound disk." >}}
{{< nbas-image src="c_65-equ-25m.webp" width="360" align="right"
caption="NGC 253, eQuinox 2, 25 min"
alt="NGC 253, a long, nearly edge-on spiral galaxy, mottled with dust along its length." >}}
{{< clear >}}

Now turn to the opposite side of the sky, near the South Galactic Pole. Five bright spirals in
Sculptor and Cetus -- NGC 55, NGC 247, NGC 253, NGC 300 and NGC 7793 -- were long treated as one
"Sculptor Group," assumed to be the nearest group to ours. Good distances broke that picture apart.
The five are strung along a filament pointing almost straight at us, from the edge of the Local
Group out to about 7 Mpc (23 Mly).[^sculptor]

Nor is the filament one group. NGC 55 and NGC 300, the nearest, are about 2 Mpc (6.5 Mly) away and
form a loose association with their dwarf companions. NGC 253, the brightest, sits nearly twice as
far, at 3.6–3.9 Mpc (12–13 Mly), at the core of a separate group with a dozen dwarf satellites.
What looks like one clump on the sky is several lined up in depth -- the same membership problem we
met in the [Local Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/),
where only distance could decide who belongs.

### The Local Sheet and the Council of Giants

M 81 and NGC 253 lie in almost opposite directions, yet they sit at almost the same distance from
us. As we noted in [our closer look at NGC 253](/articles/2026/11/ngc-253-the-silver-coin-caroline-found/),
that's no coincidence. Both belong to the **Local Sheet**, a thin, flat layer of galaxies with the
Local Group inside it. Marshall McCall, who mapped it in 2014, puts it this way: all the bright galaxies
within 20 million light-years of us lie in a sheet about 34 million light-years across and only 1.5 million
light-years thick. (Counting the dwarfs, the layer is fatter, about 1.5 Mpc.) Out to about 7 Mpc
the sheet's galaxies also move together; beyond that, their motions change sharply. For its width,
the sheet of big galaxies is thinner than a dinner plate.[^mccall]
<!-- COMPUTED: 34/1.5 ≈ 23:1; a 25 cm plate ~2 cm thick is ~12:1. -->

{{< nbas-gallery title="Some Council of Giants Galaxies" size="300px" style="carousel" >}}
m_64-equ-20m.webp | M 64   | eQuinox 2, 20 min |
m_83-equ-31m.webp | M 83   | eQuinox 2, 31 min |
m_94-equ-31m.webp | M 94   | eQuinox 2, 31 min |
{{< /nbas-gallery >}}

Within the sheet, the twelve biggest galaxies near us form a rough ring around the Local Group,
about 3.75 Mpc in radius (24 million light-years across): the "Council of Giants," in McCall's
phrase. Ten are spirals. The two ellipticals sit on opposite sides of the ring: Maffei 1, hidden
behind the Milky Way in Cassiopeia, and Centaurus A. The table doubles as an observing list --
everything with a decent altitude in the last column lies in the same thin layer we do: M 81, M 82,
M 94 and M 64 in spring, IC 342 and NGC 253 in autumn.[^council]

| Galaxy | Type | Constellation | Distance | Highest altitude from 42½° N |
|---|---|---|---|---|
| Maffei 1 | elliptical | Cassiopeia | 3.3 Mpc (10.7 Mly) | 73° (but behind ~5 magnitudes of dust) |
| Maffei 2 | spiral | Cassiopeia | 3.4 Mpc (11.2 Mly) | ~73° (also heavily dimmed by dust) |
| IC 342 | spiral | Camelopardalis | 3.4 Mpc (11.0 Mly) | 64° |
| M 81 | spiral | Ursa Major | 3.7 Mpc (12.2 Mly) | 63° |
| M 82 | spiral (starburst) | Ursa Major | 3.5 Mpc (11.4 Mly) | 63° |
| M 94 | spiral | Canes Venatici | 4.5 Mpc (14.7 Mly) | 89° |
| M 64 | spiral | Coma Berenices | 5.0 Mpc (16.3 Mly) | 69° |
| NGC 253 | spiral | Sculptor | 3.5 Mpc (11.3 Mly) | 22° |
| M 83 | spiral | Hydra | 4.9 Mpc (16.1 Mly) | 18° |
| Centaurus A | elliptical | Centaurus | 3.6 Mpc (11.6 Mly) | 4° |
| NGC 4945 | spiral | Centaurus | 3.3 Mpc (10.9 Mly) | never rises |
| Circinus | spiral | Circinus | 4.3 Mpc (13.9 Mly) | never rises |
<!-- Distances: McCall 2014, MNRAS 440, 405, Table 1 distance moduli, converted (computed).
Altitudes: 90° − |42.5° − Dec|. M 81 3.7 here vs 3.6 (Durrell) above: different sources. -->

---

## Virgo: The Nearest Big Cluster

{{< nbas-gallery size="300px" style="carousel" title="Sample of Virgo Cluster Galaxies" >}}
m_49-equ-20m.webp | Messier 49 | eQuinox 2, 20 min
m_61-equ-28m.webp | Messier 61 | eQuinox 2, 28 min
m_87-92U-PIXRCAGRAXGHS-square.webp | Messier 87 | eQuinox 2, 16 min
m_88-equ-20m.webp | Messier 88 | eQuinox 2, 20 min
m_91-equ-20m-fair.webp | Messier 91 | eQuinox 2, 20 min
m_99-equ-20m-fair.webp | Messier 99 | eQuinox 2, 20 min
m_100-equ-20m.webp | Messier 100 | eQuinox 2, 20 min
{{< /nbas-gallery >}}


Groups like ours hold a few big galaxies and a crowd of dwarfs. A **cluster** is a different kind of
place. The Virgo Cluster has more than a thousand members -- the standard catalog lists about 1,300
-- including giant ellipticals like M 87 and M 49, many times brighter than anything in a group. It
is about 16.5 Mpc (54 Mly) away: the mean of 79 galaxies measured one by one with surface
brightness fluctuations, a rung calibrated through Cepheids and the tip of the red giant branch.[^mei]

Because those galaxies were measured individually, they can be placed front to back, which no
photograph can do. Virgo turns out to be about 2.4 Mpc deep, and its two main clumps sit at slightly
different distances: M 87's at 16.7 Mpc, M 49's at 16.4.

### Why Virgo covers so much sky

On the sky, Virgo's galaxies spread across a roughly circular area about 10 degrees wide -- twenty
full Moons. Fifteen of Charles Messier's 110 objects are Virgo Cluster galaxies; he was collecting
them in 1781 without knowing what they were.[^binggeli]

{{< nbas-image src="virgo-sky-annotated.webp" fullwidth="true"
caption="The Virgo Cluster on the sky. Ellipses mark galaxies. The gold circle, 10° across and centered on M 87, outlines the cluster's main body, though members spill beyond it, like M 61 to the south; the small circle marks Markarian's Chain. Cyan: the seven galaxies pictured above. The white disk is a full Moon drawn to the same scale. Chart: Stellarium."
alt="A star chart of the region between Denebola and Vindemiatrix, scattered with small red, orange and blue ellipses marking galaxies, densest inside a large gold circle. Cyan circles and labels mark M 87 near the center, M 49 near the bottom edge, M 88, M 91, M 99 and M 100 along the top, and M 61 below the circle. A small gold circle just right of center marks Markarian's Chain. In the lower right, a small white disk labeled full Moon, to scale, is far smaller than the gold circle." >}}

To turn that angle into a real size, multiply by the distance:

> 16.5 Mpc × (10° in radians, 0.175) ≈ 2.9 Mpc

So Virgo is about 2.9 Mpc wide and 2.4 Mpc deep: roughly as deep as it is wide. Two independent
measurements, one from angles on the sky and one from galaxy-by-galaxy distances, describe the same
three-dimensional object.

### How big is "big"?

Here's a puzzle. The Local Group is about 2 Mpc across and has around 100 known members. Virgo is
about 2.9 Mpc across and has around 1,300. Per unit volume, Virgo comes out only about three times as
crowded as our group. For a "big cluster," that sounds meager.

The catch is in the counting. Most of the Local Group's members are faint dwarfs we know about only
because they're close. The Virgo catalog stops at galaxies about 25 million times as bright as the
Sun, and many of our own dwarfs are fainter than that. The faintest are astonishingly faint: Segue 1,
a satellite of the Milky Way, shines with the light of only about 300 Suns -- less than a single
bright red giant star. It's still a galaxy, not a star cluster, because what holds it together is
dark matter, which outweighs its stars thousands of times over. At Virgo's distance, galaxies like
that would never make the list.[^segue1] The two counts aren't measuring the same thing.
<!-- Bob's NOTE answered. Segue 1: M_V = −1.5 (+0.6/−0.8) (Geha et al. 2009, ApJ 692, 1464) → ~300 L☉
(Wikipedia, consistent); "total luminosity less than that of a single bright red giant", M/L_V ~3400
(Simon et al. 2011, ApJ 733, 46). VERIFIED. -->

Count only the big galaxies -- Milky Way-class spirals and giant ellipticals -- and the picture
changes. The Local Group has two, the Milky Way and Andromeda. Within 6 degrees of M 87 (about 1.7
Mpc), Virgo has more than fifty.

Mass tells the same story. The Local Group weighs a few trillion Suns. Virgo, measured by how fast
galaxies around it are falling in, holds about 1.2 × 10^15 -- around four hundred times as much, in
a region only about one and a half times as wide. Virgo isn't meager; it's untidy: irregular, made
of at least three clumps, and still pulling in groups from its surroundings. By mass, it's in the
same league as Coma.[^virgomass] (What that crowding does to the galaxies themselves comes up in
[Crowded and empty](#crowded-and-empty).)
<!-- COMPUTED: B < 12.0 at Virgo (M_B < −19.1): 54 within 6° of M87, 19 within 2°. Mass ratio ~380×.
VCC B_T ≈ 18 → 2.6e7 L☉(B). Segue 1: Simon et al. 2011. M33 misses the cut. See facts rounds 3–4. -->

### Markarian's Chain: a piece of Virgo in one field

{{< nbas-image src="mchain-s30-6m-full-rotated.webp" fullwidth="true"
caption="Markarian's Chain, Seestar S30, 34 min"
alt="A wide field of stars crossed by a gently curving line of galaxies: two large, round elliptical glows at one end, a close pair of galaxies nicknamed the Eyes, and smaller galaxies continuing the arc." >}}
<!-- RESOLVED (Bob): 34 min is right; PixInsight rejected ~80% of frames (leaving 6 min), so the
Seestar's own stacked FITS was the base. Filename scheme: 92U = eQuinox 2, process v9.2; 92S = S50;
92T = S30. -->

You can't take in all of Virgo at once, but you can take in a piece of its core. **Markarian's
Chain** is a gentle arc of galaxies about 1.3 degrees long, anchored by the big lenticulars M 84 and
M 86 and running past the interacting pair NGC 4435 and NGC 4438, "the Eyes." At Virgo's distance,
1.3 degrees is about 0.37 Mpc -- 1.2 million light-years, half the distance from here to Andromeda,
in one camera frame. Not every galaxy in the chain belongs to it: several appear to move together,
while others only line up by chance. Benjamin Markarian noticed the shared motion in 1961, which is
why the chain carries his name.[^markarian]

With big binoculars (100 mm) under a dark sky, the brightest members show as faint smudges. M 84 and
M 86 show up even in a 60 mm telescope, and from them you can sweep along the arc to the Eyes and
beyond.[^chainobs]
<!-- Binoculars: BBC Sky at Night; 60 mm: Astronomy, May 2020 (SECONDARY, observing guides). -->

---

## Coma: A Cluster for Comparison

{{< nbas-image src="coma-s30-26m-annotated-n10.webp" fullwidth="true"
caption="The Coma Cluster, Seestar S30, 26 min. NGC and IC galaxies labeled; the ten brightest are numbered in blue (4 and 5 are a close pair, NGC 4841A and B)."
alt="A star field with dozens of small galaxies labeled with NGC and IC numbers, crowded around two larger elliptical galaxies near the center, NGC 4889 and NGC 4874. Ten galaxies carry numbers from 1 to 10 in order of brightness." >}}
<!-- DONE (Claude): NGC 4874 label + ten brightest numbered from a WCS fitted to 12 labelled galaxies
(residuals ≤ ~10 px). Ranking: OpenNGC V (B − 0.9 where V missing): 1 NGC 4889, 2 4874, 3 4921, 4/5 4841A/B,
6 4911, 7 4926, 8 4895, 9 4908, 10 4869 (V 13.36). Ranks 8–14 within ~0.3 mag. -->

For a really rich cluster, go to the **Coma Cluster** (Abell 1656), about 100 Mpc (330 Mly) away --
six times farther than Virgo. Coma is one of the richest and most massive clusters in the nearby
universe, around 10^15 times the mass of the Sun, with two giant ellipticals, NGC 4889 and NGC 4874,
at its center. Where Virgo is irregular and still assembling, Coma is richer, more concentrated, and
far poorer in spirals.

Distance changes how it looks. A cluster as wide as Virgo would span only about 1.7 degrees at
Coma's distance -- three or four full Moons instead of twenty -- so all of Coma fits in one wide
field, where Virgo needs a mosaic.

Coma is also where the rungs from the last article start to strain. Thirteen Type Ia supernovae have
gone off in Coma; calibrated with the Cepheid ladder, they put it at about 98.5 Mpc. Other methods
range from the mid-80s to around 100 Mpc. "About 100 Mpc" is honest.[^coma] A precise number turns out to
matter a great deal, for reasons that belong with redshift.

### Counting galaxies the way Abell did

In 1958, George Abell went through the plates of the new Palomar Sky Survey and picked out 2,712
rich clusters of galaxies by eye. He gave each a rough distance, with no redshift, from a crude
standard candle: how bright the cluster's **tenth-brightest galaxy** looked. Assuming the tenth-brightest
member of every rich cluster is about equally luminous, the fainter it looks, the farther away the
cluster. Try it on the Coma image above: count down to galaxy 10, NGC 4869, which shines at about
magnitude 13.4.
<!-- Ranks 8–14 within ~0.3 mag: the magnitude is robust, the name isn't (round 1b). -->

Abell's other number was a count of everything else. To call a cluster "rich," he took the magnitude
of its third-brightest galaxy and counted every member up to two magnitudes fainter; only clusters
with at least fifty made his catalog.[^abell] The bright few tell you how far away a cluster is; the crowd
behind them tells you how big it is.

{{< nbas-image src="hercules-s50-32m-annotated.webp" fullwidth="true"
caption="The Hercules Cluster, Seestar S50, 32 min. Green: NGC and IC galaxies. Blue: PGC galaxies."
alt="A star field densely labeled with galaxy names: a few dozen NGC and IC galaxies in green, clustered toward the center, and well over a hundred fainter PGC galaxies in blue spread across the whole frame." >}}

The **Hercules Cluster**, half again as far as Coma at about 156 Mpc (510 Mly), shows the crowd at a
glance. The galaxies labeled in green were bright enough to make the NGC and IC catalogs in the
nineteenth century: 28 of them. The ones in blue are PGC galaxies, catalogued only in the age of sky
surveys: about 180. Many belong to the cluster itself -- a deep spectroscopic survey has
confirmed 360 members -- while others lie in front of it or far behind.[^hercules]
<!-- COUNT (Claude, read off the 1920 px image): 179 PGC labels, 28 NGC/IC labels; automated checks
bracket it (121 merged text blobs; 188 OCR tokens incl. misreads). Agulli et al. 2017: 360 members (M_r < −16, 1.3 R200). "Many", not "most". -->

---

## Why the Spring Sky Is Full of Galaxies

If you observe from the northern hemisphere, you know this part. Spring is **galaxy season**. Autumn
has galaxies too -- Andromeda, M 33, NGC 253 -- but they're mostly our own neighbors. In spring the
sky is full of galaxies tens of megaparsecs away.

Two reasons add up. The first is the one [our closer look at NGC
253](/articles/2026/11/ngc-253-the-silver-coin-caroline-found/) used for the South Polar Group: look
toward a galactic pole and you look out through the thinnest part of our own galaxy's dust and
stars. The North Galactic Pole is in Coma Berenices, high in the spring evening sky. The second is
that Virgo, and Coma behind it, happen to lie in the same part of the sky: Coma just 2 degrees from
the pole, Virgo about 15. The nearest big cluster sits in the clearest window we have.[^ngp]
<!-- COMPUTED (astropy): NGP 12h51m26s +27°07′42″; Coma 2.0°, Virgo (M 87) 15.5° from it. -->

{{< nbas-image src="c_5-equ-33m.webp" width="300" align="right"
caption="IC 342 (Caldwell 5), eQuinox 2, 33 min."
alt="The face-on spiral galaxy IC 342, a faint, broad pinwheel seen through a dense field of foreground Milky Way stars." >}}
The opposite is also true. Look toward the plane of the Milky Way and dust blocks most of the view.
Astronomers call that band the **Zone of Avoidance**. It hides a fifth to a quarter of the sky from
ordinary optical galaxy catalogs,[^zoa] so our map of the nearby universe has a hole wrapped all the way
around the sky. Maffei 1, one of the Council's two ellipticals, is a giant only 3 to 4 Mpc away --
the nearest giant elliptical we know of -- yet nobody knew it was there until Paolo Maffei found it
on an infrared plate in 1967. It sits half a degree from the Milky Way's plane, behind nearly five
magnitudes of dust. Without that dust it would be one of the brightest galaxies in the sky, about
two-thirds the size of the full Moon.[^maffei]

Another Council member, IC 342, sits only about 10 degrees from the plane. Dust dims it by well over
a magnitude, which is why [our closer look at it](/articles/2027/01/the-hidden-galaxy/) calls it the
Hidden Galaxy -- and why, in a photograph, you see it through a curtain of foreground Milky Way
stars.

{{< clear >}}

---

## Walls, Filaments and Voids

Step back far enough and the groups and clusters stop looking like separate things. They become
beads on a web.[^zcat]

{{< nbas-image src="fig-nearby-map.webp" fullwidth="true"
caption="Our neighborhood out to about 150 Mpc, seen face-on in the supergalactic plane: about 12,000 galaxies lying within 20 Mpc of the plane, with the Local Group at the center. This is a slab seen from above, so anything far above or below it, including the Local Void and the Hercules Cluster, is off the map. Distances come from redshift, which includes each galaxy's own motion, so rich clusters such as Coma look stretched along the line toward us. The shaded wedges mark the Zone of Avoidance (approximate). Data: CfA Redshift Catalog (Huchra et al.), via NASA's HEASARC."
alt="A face-on map of galaxies around the Local Group, shown as a grainy web of points out to about 150 megaparsecs, with dashed rings at 50, 100 and 150 Mpc. Lettered markers are explained in a key at the right. A dense knot just above the center is the Virgo Cluster (A). Filaments run out from it: up to the Coma Cluster (B) and the Leo Cluster (C) about 100 Mpc away, where Coma forms a long spike pointing back toward us; left to the Centaurus Cluster (D); and down-right through the Perseus Cluster (F) and the Pisces group (G), the Perseus–Pisces supercluster (H). Two shaded wedges along the horizontal axis mark the Zone of Avoidance; the hidden Norma Cluster (E) sits inside the left one. Between the filaments are large, nearly empty regions." >}}

### Walls and filaments

Coma doesn't sit alone. It lies in the **Great Wall**, a sheet of galaxies mapped by Geller
and Huchra in 1989. In their survey it was at least 240 Mpc long and 85 Mpc wide (about 800 by
280 million light-years) -- and those were the edges of the survey, not of the wall --[^greatwall] yet thin by
comparison. Several filaments meet at Coma. Clusters grow where filaments cross, the way towns grow
where roads meet.

Why should matter arrange itself this way? Gravity works on whatever unevenness the early universe
started with, and an uneven region doesn't collapse evenly. It collapses fastest along its shortest
direction, flattening first into a sheet. Sheets meet in filaments, and filaments meet in knots,
which become clusters. Yakov Zel'dovich worked out the first step in 1970: the first places to reach
high density are flattened sheets, later nicknamed "Zel'dovich pancakes."[^zeldovich]

{{< nbas-image src="fig-local-sheet-edge-on.webp" fullwidth="true"
caption="The nearby universe seen edge-on, through a slice 4 Mpc thick: galaxies whose distances were measured directly, not inferred from their speeds. Our Local Sheet is the thin band through the Local Group; about 4½ Mpc below it, the Leo I group (M 96) sits in the next layer down, the Leo Spur. The shaded bands are guides to the eye. Both axes are drawn to the same scale. Data: Updated Nearby Galaxy Catalog (Karachentsev, Makarov & Kaisina 2013)."
alt="A scatter plot of nearby galaxies seen edge-on, supergalactic Y across and supergalactic Z up, in megaparsecs. A thin shaded horizontal band labeled Local Sheet runs through the Local Group at the center, holding most of the galaxies, including about a dozen large ones shown as gold dots. About four and a half megaparsecs below it and to the right, a second shaded band labeled Leo Spur holds a tight clump of gold dots, the Leo I group (M 96). Above the Local Sheet, toward an arrow labeled toward Hercules and the Local Void, there are only a few scattered dwarfs. An arrow at right points toward Virgo, 16.5 megaparsecs away." >}}

You can see the pancakes from here. Our Local Sheet is one. A few megaparsecs "below" it -- on the
side away from the North Supergalactic Pole -- lies the next, the **Leo Spur**, home to the Leo
Triplet and the M 96 group, in a layer roughly parallel to ours. Farther below is the **Fornax
Wall**, a flattened strand running from Cetus through Fornax and Eridanus to Dorado, with the compact
Fornax Cluster at 20 Mpc. Above our sheet is a layer with clouds of galaxies in Pegasus. Layers this
close spread across big patches of sky simply because they're near. The Perseus–Pisces supercluster
is the opposite case: about 70 Mpc away, it still spans 45 to 60 degrees of sky because it's
enormous -- a chain of clusters at least 70 Mpc long.[^layers]

### Voids

The other half of the web is empty. The **Local Void** begins right at the edge of the Local Group;
our Local Sheet is one of its walls. Its center is at least 23 Mpc away, toward Hercules, and it is
at least 45 Mpc across -- some 150 million light-years with almost no galaxies in it. Much of it is
hard to study because it lies partly behind the plane of the Milky Way.[^localvoid]

How empty is "empty," and what would a galaxy in there have for neighbors? Those are the questions
we asked of Virgo, and the answers belong side by side.

### Crowded and empty

Put everything on one yardstick -- how much matter a region holds compared with an average patch of
the universe, and how far a big galaxy is from its nearest big neighbor, in Milky Way diameters --
and our neighborhood lines up like this:[^density]

| Place | Matter density vs. cosmic average | Nearest big neighbor |
|---|---|---|
| Virgo Cluster | ~600 | ~7 Milky Way diameters (core) |
| Our Local Group | ~20 | ~27 Milky Way diameters (Andromeda) |
| Inside a void | ~0.2 (center: under 0.1) | none known within 3 Mpc -- over 100 diameters |
<!-- COMPUTED: densities Ωm 0.3, h 0.7 (LG ×18.5, Virgo ×660 within 2.2 Mpc), order of magnitude.
Voids ≈ 20% (van de Weygaert 2016; Geller & Huchra 1989), centres < 10% (arXiv 0803.0918).
Virgo core spacing: B<12 within 2° of M87 → 190 kpc = 6.8 diameters (28 kpc). MW–M31 761 kpc = 27.
KK 246: Kreckel et al. 2011; 3 Mpc = 107 diameters. -->

{{< nbas-image src="fig-crowding-ladder.webp" fullwidth="true" caption="How far apart big galaxies are, measured in Milky Way diameters and drawn to one scale. In the core of the Virgo Cluster, a big galaxy's nearest big neighbor is on average about 7 diameters away; in our Local Group, Andromeda is about 27 diameters from the Milky Way. Every galaxy is drawn the size of the Milky Way; the Virgo spacing is an average worked out from how many big galaxies crowd into the core." alt="Two rows of gold disks on a common scale. Top row, Virgo Cluster core: two disks 7 Milky Way diameters (190 kiloparsecs) apart. Bottom row, Local Group: two disks 27 diameters (761 kiloparsecs) apart, nearly four times farther." >}}

In the [Local Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/) we
found that galaxies are crowded compared with stars: neighboring stars are about 30 million
Sun-widths apart, while the Milky Way and Andromeda are under 30 of their own diameters apart. That
number depends on where you are.

In the core of a cluster like Virgo, big galaxies are packed something like fifty times more densely
than in our group, and a big galaxy's nearest big neighbor is only about 7 Milky Way diameters away
-- four times closer than Andromeda is to us.

In a void, the question almost stops making sense. Only one galaxy is confirmed to lie well inside
the Local Void: a faint dwarf called KK 246, a few megaparsecs in from the edge, with no known galaxy
of any size within 3 Mpc.[^kk246] The big galaxies aren't in the void at all; they're in the walls around it,
and our Local Sheet is one of those walls. Voids don't stay as they are, either. Matter drains out
of them toward the walls, so over billions of years voids grow emptier, walls grow denser, and the
gap between crowded and empty keeps widening.

### The neighborhood changes the residents

In 1980, Alan Dressler sorted about 6,000 galaxies in 55 rich clusters by type and by how crowded
their surroundings were. The pattern was simple: the more crowded the neighborhood, the larger the
share of elliptical and lenticular galaxies; the emptier, the more spirals. Later work traced it all
the way from the densest cluster cores to the emptiest open spaces. As Dressler summed it up in 1984,
the sparsest places are 80–90% spirals, and the densest are 80–90% ellipticals and lenticulars.[^dressler] Even
inside Virgo, the spirals tend to stay out of the core.

Why? Not mainly because galaxies in a cluster merge: in a rich cluster they pass each other far too
fast -- several hundred to a thousand kilometers per second. Instead, the cluster wears them down. A
spiral falling through the cluster's hot gas has its own gas swept out, like smoke from a speeding
car, and without gas it stops making new stars. Repeated high-speed flybys heat and thicken its
disk. Mergers do build ellipticals, but mostly earlier, in slower-moving groups, before those groups
fall into a cluster. The exception is the giant at the very center, which can still swallow whatever
sinks to the middle: M 87 absorbed an entire medium-sized galaxy within the last billion years.[^mechanisms]
Moving to the big city changes you, and that goes for galaxies too.
<!-- Sources: Dressler 1980; Dressler 1984 ARA&A 22, 185; Gunn & Gott 1972; Moore et al. 1996;
Combes astro-ph/0308293; Longobardi et al. 2015. See facts rounds 3–4. -->

---

## Superclusters and Laniakea

Virgo sits at the heart of what Gérard de Vaucouleurs called the **Local Supercluster**: the
flattened spread of groups, ours included, that surrounds the cluster. He first called it the "Local
Supergalaxy" in 1953 -- a galaxy made of galaxies -- and renamed it five years later.[^devauc]

He took the idea far enough to give it its own coordinate system. Just as galactic coordinates are
built on the plane of the Milky Way, **supergalactic coordinates** are built on the plane of the
Local Supercluster: the dashed hoop on the sky map below, nearly at right angles (about 84 degrees)
to the Milky Way's plane. M 81, IC 342, NGC 253, Centaurus A and the Virgo Cluster each lie within a
few degrees of it. The big galaxies near us really do lie in a plane, tipped across our sky like a
hoop. Its zero point, where the two planes cross, is in Cassiopeia, less than two degrees from
Maffei 1.[^sgcalc]
<!-- NOTE (Bob, for a future coordinates article): show the planes of all four systems -- Earth's
equator, the ecliptic, the galactic disk, the supergalactic plane -- tilted against each other. -->

{{< nbas-image src="fig-sky-directions.webp" fullwidth="true"
caption="The whole sky in galactic coordinates, with the Milky Way's plane across the middle (the shaded band is schematic). The map is centred on the direction of the North Supergalactic Pole, so the supergalactic plane -- the flattened spread of nearby galaxies, tipped almost at right angles to our own galaxy's disk -- appears as the dashed hoop around the middle."
alt="An oval all-sky map. A shaded horizontal band through the middle marks the Zone of Avoidance. Near the top, the North Galactic Pole is marked, with the Coma Cluster almost at it and the Virgo Cluster nearby. A dashed blue oval, the supergalactic plane, loops around the middle of the map through M 81, IC 342, Maffei 1, NGC 253, Centaurus A and the Virgo Cluster. The North Supergalactic Pole is marked in Hercules at the center of the oval, just below an open circle marking the direction of the Local Void's center; the Hercules Cluster sits above them. The Perseus, Norma and Fornax clusters are also marked." >}}

The North Supergalactic Pole is in Hercules. Look that way and you are looking straight out of the
plane our neighborhood lies in -- and almost straight at the center of the Local Void. The Hercules
Cluster lies in the same broad direction, about 40 degrees from the pole. So the nearest tens of
megaparsecs along that sightline are nearly empty, and the cluster waits on the far shore, about 156
Mpc out. An image of the Hercules Cluster is a picture taken across one of the emptiest places near
us. (The side-on map at the end of this article shows that sightline.)
<!-- GEOMETRY (computed): Hercules sightline 36° from the listed Local Void centre; passes within
~13.5 Mpc of a centre ≥23 Mpc away → inside the void if the centre is closer than ~38 Mpc. -->

And the Local Supercluster is only one part of something larger. In 2014, Brent Tully and his
colleagues mapped a structure about 160 Mpc (520 Mly) across, holding around 100,000 galaxies and
10^17 times the mass of the Sun, and named it **Laniakea**, Hawaiian for "immense heaven."[^laniakea] Our galaxy
is near its outskirts. One thing about Laniakea is different from everything else in this article:
its boundary isn't drawn around where galaxies are. It's drawn around where they're going.

---

## How Far Does Each Ruler Reach?

Every distance in this article came from a rung we built in the last two articles. Each rung's reach
is set by what it needs to see -- and at the edge of each one is a galaxy you've already met.[^rulers]

| Ruler | What it reads | Practical reach | At the edge of its reach |
|---|---|---|---|
| Cepheids | individual pulsating supergiant stars | a few tens of Mpc; the farthest, with Hubble, about 80 Mpc | M 100 in Virgo (17 Mpc), Hubble's 1994 milestone; Hubble has also hunted Cepheids in NGC 4921, galaxy 3 in our Coma image |
| Tip of the red giant branch | the brightest old red giants | about 20 Mpc with Hubble; 50 Mpc or more expected with JWST | the Fornax Cluster (20 Mpc), now reached by JWST |
| Surface brightness fluctuations | the "graininess" of an elliptical galaxy's starlight | about 100 Mpc with Hubble's infrared camera | NGC 4874, Coma's central giant: 100 ± 10 Mpc |
| Tully-Fisher | how fast a spiral spins vs. how bright it is | about 10,000 spirals out to about 210 Mpc | the Hercules Cluster: 154 ± 5 Mpc, from 39 of its spirals |
| Fundamental plane | an elliptical's size, brightness and star speeds | about 42,000 ellipticals out to about 400 Mpc | beyond every cluster in this article |
| Type Ia supernovae | exploding white dwarfs | far beyond this article -- but only where one happens to go off | Coma: 13 so far |
<!-- Sources: claude/extragalactic-scale-facts-r5.md. -->

The table has two halves. The top three rulers read stars, or the graininess stars make, so they give
a good distance to a single galaxy -- but only if you can see that much detail, which runs out
somewhere between Virgo and Coma. The next two read a whole galaxy at once: its spin, its size, its
brightness. They reach much farther but are rough for any one galaxy; the fundamental plane, for
instance, is good to about 20 percent. Their strength is numbers. Average 39 spirals in the Hercules
Cluster and the roughness mostly cancels: Tully-Fisher puts Hercules at 154 Mpc, right beside the
156 Mpc its redshift gives.[^herctf]

---

## Wrapup

{{< nbas-image src="fig-side-view.webp" fullwidth="true"
caption="Our neighborhood out to about 150 Mpc, seen side-on: a slice 30 Mpc thick that stands upright through the Local Group (the cross at the center) and holds both the Virgo Cluster and the Hercules Cluster. The supergalactic plane runs across the middle. Our line of sight to Hercules climbs out of the plane through thinly populated space; straight up, toward the center of the Local Void, the view is blocked by the Milky Way's own dust (shaded). Distances come from redshift, which stretches clusters such as Hercules along the line toward us, and fainter galaxies drop out of the catalog with distance, so the far parts of the map look emptier than they are. Data: CfA Redshift Catalog (Huchra et al.), via NASA's HEASARC."
alt="A side-on map of galaxies out to about 150 megaparsecs, with dashed rings at 50, 100 and 150 Mpc around a cross at the center marking the Local Group. A dense horizontal smear of galaxies along the supergalactic plane runs right from the cross to the Virgo Cluster, and a filament runs down and to the left from it. A shaded wedge, the Zone of Avoidance, points straight up and straight down from the center; an arrow beside the upper wedge reads straight up: toward the Local Void's center. A dashed blue line, our line of sight to Hercules, climbs at about fifty degrees through a sparse region to a gold diamond marking the Hercules Cluster at 156 Mpc, where galaxies form a streak pointing back toward us." >}}

Here's our neighborhood in megaparsecs. The Local Group sits in a clearing inside
a thin sheet, ringed by a council of big galaxies. Sixteen megaparsecs away is Virgo, the nearest big
cluster. Straight up, mostly hidden behind our own galaxy, is the Local Void. A hundred megaparsecs
out are Coma and the Great Wall, and beyond the void, Hercules.

Look at what measured each stop. M 81: Cepheids and red giants. Virgo: surface brightness
fluctuations, calibrated on both. Coma: a handful of Type Ia supernovae, and an argument about the
last few percent. Hercules: dozens of spirals averaged together. Each step outward trades precision
for reach.

But look at the maps themselves. Every galaxy on them was placed by redshift alone, because redshift
is the one measurement you can make for any galaxy you can get a spectrum of. Turning a redshift
into a distance means knowing exactly how fast the universe is expanding -- and the only way to know
that is to calibrate it against the ladder we just finished climbing. That's where the next article
begins.


[^stellarium]: Star fields rendered with Stellarium (stellarium.org); Stellarium contributors, Stellarium v26.2 (2026), doi:10.5281/zenodo.23020615; G. Zotti et al., "The Simulated Sky: Stellarium for Cultural Astronomy Research," *Journal of Skyscape Archaeology* 6(2), 221–258 (2021), doi:10.1558/jsa.17822.

[^kpg]: P. R. Renne et al. 2013, *Science* 339, 684.

[^minivoid]: I. D. Karachentsev et al. 2002, *A&A* 383, 125.

[^m81]: 3.63 ± 0.14 Mpc from four red-giant-tip and Cepheid measurements: P. R. Durrell et al. 2010, arXiv:1006.2036; Cepheids alone 3.60 ± 0.23 Mpc: McCommas et al. 2009.

[^sculptor]: NGC 55 and NGC 300 at 2.12 and 2.00 Mpc: arXiv:astro-ph/0407389. NGC 253 at 3.94 Mpc (Karachentsev et al. 2003, arXiv:astro-ph/0302045) and 3.70 Mpc (Karachentsev et al. 2021, arXiv:2102.11354, which also traces the filament to about 7 Mpc). NGC 55 and NGC 300 as a separate association: R. B. Tully 2015, arXiv:1411.1511.

[^mccall]: M. L. McCall 2014, *MNRAS* 440, 405; the "34 million light-years across and only 1.5 million light-years thick" wording is McCall's, quoted in *ScienceDaily*, 2014 March 11. The common motion out to about 7 Mpc: R. B. Tully et al. 2008, *ApJ* 676, 184. The plate comparison is our arithmetic (about 23 to 1, against about 12 to 1 for a dinner plate).

[^council]: Distances converted from the distance moduli in McCall (2014), Table 1. Highest altitude is our calculation for latitude 42½° N (90° minus the difference between latitude and declination).

[^mei]: S. Mei et al. 2007, *ApJ* 655, 144: 16.5 ± 0.1 (random) ± 1.1 (systematic) Mpc, back-to-front depth 2.4 ± 0.4 Mpc, M 87 and M 49 subclusters at 16.7 and 16.4 Mpc.

[^binggeli]: B. Binggeli, review of the Virgo Cluster (NASA/IPAC Extragalactic Database, Level 5). The catalog: B. Binggeli, A. Sandage & G. A. Tammann 1985, *AJ* 90, 1681 (2,096 galaxies, 1,277 of them members, complete to about B = 18).

[^segue1]: The catalog limit in Suns is our conversion of B = 18 at 16.5 Mpc. Segue 1: M_V = −1.5 (M. Geha et al. 2009, *ApJ* 692, 1464); "total luminosity less than that of a single bright red giant" and the dark-matter dominance: J. D. Simon et al. 2011, *ApJ* 733, 46.

[^virgomass]: Virgo's mass within 2.2 Mpc from infall: P. Fouqué et al. 2001; R. B. Tully & R. Mohayaee 2004. Local Group mass: van der Marel et al. 2012. Counts of big galaxies (brighter than B = 12 at Virgo) are our own, from the OpenNGC catalog. Virgo's three clumps: arXiv:astro-ph/0301585.

[^markarian]: B. E. Markarian 1961, *AJ* 66, 555.

[^chainobs]: Binoculars: *BBC Sky at Night Magazine*, "Markarian's Chain." Small telescope: *Astronomy*, May 2020, "Explore Markarian's Chain."

[^coma]: Thirteen Type Ia supernovae and 98.5 Mpc: D. Scolnic et al. 2025, *ApJL* 979. The ten-brightest ranking in our image uses V magnitudes from the OpenNGC catalog; galaxies 8 to 14 lie within about 0.3 magnitude of each other, so the magnitude of number 10 is firmer than its name.

[^abell]: G. O. Abell 1958, *ApJS* 3, 211; the richness and distance-group rules as summarized in N. Bahcall's and C. Sarazin's reviews (NASA/IPAC Extragalactic Database, Level 5).

[^hercules]: 360 spectroscopic members brighter than M_r = −16: I. Agulli et al. 2017, *MNRAS* 467, 4410. The label counts (28 NGC/IC, 179 PGC) are ours, from the annotated image.

[^ngp]: Positions and angles in this section are our calculations with astropy: North Galactic Pole at 12h51m26s, +27°07′42″ (J2000); the Coma Cluster 2.0° and M 87 15.5° from it.

[^zoa]: About 25%: R. C. Kraan-Korteweg & O. Lahav 2000, *A&ARv* 10, 211; about 20% of the optical extragalactic sky: P. A. Woudt & R. C. Kraan-Korteweg 2001.

[^maffei]: Discovery: P. Maffei 1968, *PASP* 80, 618. Distance, extinction and unobscured size: R. L. Fingerhut et al. 2003 (2.9 Mpc); T. J. Davidge & S. van den Bergh 2001 (4.4 Mpc).

[^zcat]: The galaxy maps in this article use the CfA Redshift Catalog (ZCAT), J. P. Huchra et al., version of June 1995 (CDS VII/193), obtained through NASA's High Energy Astrophysics Science Archive Research Center (HEASARC); see also J. Huchra, M. Geller, C. Clemens, S. Tokarz & A. Michel 1992, *Bull. Inf. CDS* 41, 31. Distances are redshift divided by 70 km/s per Mpc.

[^greatwall]: M. J. Geller & J. P. Huchra 1989, *Science* 246, 897: "a minimum extent of 60 h⁻¹ Mpc × 170 h⁻¹ Mpc." Converted with h = 0.7 (our arithmetic).

[^zeldovich]: Ya. B. Zel'dovich 1970, *A&A* 5, 84.

[^layers]: The edge-on figure uses the Updated Nearby Galaxy Catalog: I. D. Karachentsev, D. I. Makarov & E. I. Kaisina 2013, *AJ* 145, 101, via HEASARC (table NEARGALCAT). Leo Spur: Karachentsev et al. 2015, arXiv:1503.06027. Fornax Wall: Fairall et al. 1994, via arXiv:2407.03225. Pegasus layer: R. B. Tully 1986, *ApJ* 303, 25. Fornax Cluster at 20.0 Mpc: J. P. Blakeslee et al. 2009. Perseus–Pisces: arXiv:2105.14051 and arXiv:2511.05925.

[^localvoid]: Center at least 23 Mpc away: Tully et al. 2008. Size: a smaller void about 35 Mpc long inside a larger one about 60 Mpc long, R. B. Tully 2007, arXiv:astro-ph/0611357.

[^density]: Voids average about a fifth of the cosmic mean density (R. van de Weygaert 2016, arXiv:1611.01222; also Geller & Huchra 1989), with centers below a tenth (arXiv:0803.0918). The Local Group and Virgo densities, and the Virgo-core spacing, are our order-of-magnitude calculations (matter density parameter 0.3, h = 0.7; Milky Way diameter 28 kpc).

[^kk246]: K. Kreckel et al. 2011, *AJ* 141, 204.

[^dressler]: A. Dressler 1980, *ApJ* 236, 351; A. Dressler 1984, *ARA&A* 22, 185.

[^mechanisms]: Gas stripping: J. E. Gunn & J. R. Gott 1972; high-speed flybys ("harassment"): B. Moore et al. 1996; mergers mostly in groups before clusters form: F. Combes, arXiv:astro-ph/0308293. M 87: A. Longobardi et al. 2015, *A&A* 579, L3.

[^devauc]: G. de Vaucouleurs 1953 and 1958; supergalactic coordinates as defined by de Vaucouleurs et al. 1976.

[^sgcalc]: Angles in this section are our calculations with astropy's supergalactic frame: the planes meet at 83.7°; the Local Void's listed center is 4.7° from the North Supergalactic Pole, and the Hercules Cluster 40.6°.

[^laniakea]: R. B. Tully et al. 2014, *Nature* 513, 71.

[^rulers]: Cepheids: SH0ES hosts from 6.7 Mpc (M 101) to 80 Mpc (NGC 105), arXiv:2403.02801; M 100 at 17.1 ± 1.8 Mpc, W. L. Freedman et al. 1994, *Nature* 371, 757. Red-giant tip: about 20 Mpc with Hubble and at least 50 Mpc with JWST, G. S. Anand et al. 2024, *ApJ* 966, 89; Fornax with JWST, arXiv:2405.03743. Surface brightness fluctuations to at least 100 Mpc: J. P. Blakeslee et al. 2021, *ApJ* 911, 65; NGC 4874 at 100 ± 10 Mpc, M. C. Liu & J. R. Graham 2001, *ApJ* 557, L31. Tully-Fisher: 9,792 spirals within 15,000 km/s, E. Kourkchi et al. 2020, *ApJ* 902, 145. Fundamental plane: 42,221 distances in Cosmicflows-4 (Tully et al. 2023), about 20% per galaxy (Scodeggio et al. 1997, arXiv:astro-ph/9610082). Reach in Mpc is our conversion at 70 km/s per Mpc.

[^herctf]: Abell 2151, 39 spirals, 154.4 ± 5.0 Mpc: Cosmicflows-4 Tully-Fisher calibration, arXiv:2004.14499. Redshift distance 156 Mpc (h = 0.705), NASA/IPAC Extragalactic Database.
