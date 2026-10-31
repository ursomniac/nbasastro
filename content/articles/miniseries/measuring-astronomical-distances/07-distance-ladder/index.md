---
title: "Building the Distance Ladder"
date: 2026-12-30
description: "Parallax runs out fast. How astronomers built the first rungs of the distance ladder (moving clusters, main-sequence fitting, spectroscopic parallax, Cepheids and RR Lyrae), how each rung broke, and how it was repaired."
byline: "Parallax only reaches so far. To go farther, you need stars that tell you how bright they really are."
authors: ["bob-donahue"]
series: ["astronomical-frameworks", "historical-perspectives"]
thumbnail: "thumbnail.webp"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 7

dso_caldwell: ["41"]
dso_messier: ["13", "35", "45"]
dso_ngc: ["2158"]
dso_other: ["Hyades", "Pleiades"]
stars_variable: ["Delta Cep", "RR Lyr"]
stars_bright: ["Polaris"]
---

## Introduction

{{< nbas-image src="banner.webp" fullwidth="true"
caption="Henrietta Leavitt's 25 Cepheids, 1912: the longer the period, the brighter the star. Data: Harvard College Observatory Circular 173, Table I."
alt="Graph of 25 glowing gold dots on a dark blue background, magnitude against pulsation period on a logarithmic scale from 1 to 100 days. The dots rise from lower left to upper right along a faint straight line, and the brightest ones glow the most." >}}

Consider a long, straight road at night, lined with streetlights. If every lamp is the same
type, the same make, and the same wattage, you can judge how far away each one is just by how
bright it looks. A lamp that looks a quarter as bright is twice as far away. You don't need a
tape measure; you just need to know that the lamps are all the same.

That's the whole idea behind this chapter, and it's the general idea behind most of the distances
we measure in astronomy. In [Parsecs vs. Light Years](/articles/2026/12/parsecs-vs-light-years/) we
saw the bookkeeping: if you know how bright a star *really* is (its absolute magnitude) and
how bright it *looks*, a short formula gives you its distance. The hard part was never the
formula. The hard part is the word "really." Every method in this chapter is an answer to one question:
**How bright is it, really?**

We need the answer to that question because parallax, the one direct method we have, runs out fast. By
1900 astronomers had parallaxes for somewhere between 60 and 100 stars, depending on whose
standards you use for "reliable." The measurements were good to a few hundredths of an
arcsecond at best, so beyond about 25 parsecs (80 light-years) a star's parallax was barely
bigger than its error. The visible universe, of course, goes on much farther than that.

In order to map more far-away things, astronomers needed a distance **ladder**, built of **rungs**: kinds of
objects whose true brightness is known, so their distances can be worked out. Each rung needs
something you can see a long way off, with a connection back to something already measured independently.
In our streetlight example, you need a type of lamp you can recognize from a distance, and at
least a few examples of that lamp close enough to walk up to and measure. This chapter builds
the lower rungs of the ladder, the ones that rest directly on parallax. Every one of them broke
at least once. We'll show the breaks and the repairs, so that when you climb past this
chapter, you're standing on the rungs as they actually are today.

---

## Herschel's Mistake

The first person to try this on the scale of the whole sky was William Herschel. In the 1780s
he counted stars in hundreds of small patches of sky ("star gauges") and turned the counts
into a map of our star system. When it came to putting distances on the stars, he reached for
brightness. His unit of distance was the distance of Sirius, standing in for a typical bright
star, and the reasoning behind it was simple: a fainter star is a farther star. However, that 
assumption only works if the stars are all roughly alike.

{{< nbas-image src="Herschel-Galaxy.webp" width="450" align="right"
caption="Herschel's \"Section of our sidereal system,\" worked out from his star counts, with the Sun near the center (\"On the Construction of the Heavens,\" 1785). Drawing credited to Caroline Herschel; public domain, via Wikimedia Commons."
alt="A long, irregular, flattened outline of our star system, like a lumpy lens, split into two arms at one end, with the Sun marked near the middle." >}}

In streetlight terms, Herschel assumed every light on the road was the same kind of lamp. 
Except they're not. Some are porch lights, some are stadium floodlights, but from a distance they all look
like points. We now know that stars span a range of more than a billion in true brightness.
(The [H-R diagram in our winter star colors article](/articles/2026/12/winter-star-colors/)
shows how wide that range is.)  Apparent brightness as a guide to distance fails star by star.

How that map went wrong is a story for the next chapter. What matters here is the lesson. The
distance ladder is the search for the stars that *really are* standard: the ones that are all
the same lamp, and that we can recognize from far away.

---

## Motion Returns: Secular Parallax

Before we get to those special stars, there's a way to stretch parallax itself.

Ordinary parallax uses Earth's orbit as a baseline: 2 AU from one side to the other, the same
every year. In [our parallax chapter](/articles/2026/12/parallax/) the individual motion of the
stars themselves was *noise*, one of the layers we had to peel away to get at the parallax.
Now we turn that around.

The Sun is moving relative to the stars around it, at about 20 km/s. That carries us roughly
4 AU every year, always in the same direction. After a century the baseline isn't 2 AU, it's
over 400 AU. Nearby stars appear to drift backward, away from the direction we're heading, and
the nearer the star, the bigger the drift. That's **secular parallax**: "secular" in the old
sense of meaning slow and long-running. Herschel himself was the first to see the Sun's motion, in
1783, from the catalog motions of just a handful of stars. He placed the direction we're
heading in Hercules, within about 10° of the accepted modern value.

{{< nbas-image src="fig-secular-parallax.webp" fullwidth="true"
caption="Secular parallax in real data. The whole sky, with each arrow showing the average motion of the stars 10 to 40 parsecs away in that patch of sky, drawn as the distance they'd drift in 150,000 years. Individual stars move every which way, but on average they stream away from the solar apex, the direction we're heading, toward the antapex behind us. The arrows are shortest near those two points and longest in between, just as a reflection of our own motion should be. Data: Hipparcos, via the HYG database v4.1 (CC BY-SA 4.0)."
alt="Oval all-sky map with about a hundred gold arrows. Two points are marked: the solar apex, upper right, and the solar antapex, lower left. Arrows near the apex are short; across the sky the arrows tend to point away from the apex and toward the antapex, with plenty of scatter." >}}

The catch is that all of the other stars are moving too, each in its own direction. For any single star,
you can't separate its own motion from the reflection of ours. But for a large group of
stars, their own motions average out, while the reflection of the Sun's motion doesn't. So
secular parallax gives you the *average* distance of a group of stars, never the distance of
one. Jacobus Kapteyn built much of his work around 1900 on exactly this: the Sun's own motion,
about four times the radius of Earth's orbit every year, as a baseline that never stops growing.

That sounds like a weakness. It turns out to be the tool we need, because the stars we most
want to calibrate (the rare, special, standard ones) were never close enough for ordinary
parallax. But we can collect a group of them and ask how far away they are *on average*.
That's what Hertzsprung will do with the Cepheids, a few sections from now.

---

## The Hyades: A Ruler Made From a Speedometer

{{< nbas-image src="hyades-stellarium.webp" width="400" align="right"
caption="The Hyades cluster, rendered with Stellarium."
alt="Star chart of the Hyades in Taurus: a V-shaped scatter of stars, with bright orange Aldebaran at one tip." >}}

A cluster of stars, born together and moving together, is a special case. If every star in
the cluster moves through space in the same direction at roughly the same speed because they all "belong together,"
perspective does something useful.

Think of railroad tracks. They're parallel, but they appear to meet at a point on the
horizon. Stars moving on parallel paths do the same thing on the sky: their motions, traced
forward, appear to converge on a single point, the **convergent point**. Where that point
sits tells you the *direction* of the cluster's motion through space.

Now add a spectrograph. The Doppler shift of a star's spectral lines gives its speed toward or
away from us, the **radial velocity**, in kilometers per second, with no knowledge of its
distance at all. Combining the two observations:

- The convergent point gives the angle between the cluster's motion and our line of sight.
- The Doppler shift gives the part of the speed along our line of sight, in km/s.
- Together they give the speed *across* our line of sight, the **transverse velocity**, also in km/s.
- The proper motion gives that same sideways motion as an *angle* per year.

{{< nbas-image src="fig-space-motion.webp" width="600"
caption="A star's motion through space splits into two parts: radial velocity, along our line of sight, measured from the Doppler shift; and transverse velocity, across it. Seen from the Sun, the transverse velocity shows up as proper motion, an angle per year. For a moving cluster, the convergent point gives the angle θ, so the radial velocity gives the transverse velocity, and the transverse velocity and proper motion together give the distance. Not to scale."
alt="Diagram: the Sun at left, a star at right on a dashed line of sight. From the star, a white space-motion arrow splits into a blue radial-velocity arrow along the line of sight and a gold transverse-velocity arrow at right angles to it, with the angle theta between motion and line of sight. A narrow angle mu at the Sun shows the proper motion. Text: distance equals transverse velocity divided by mu." >}}

A known speed and the angle it covers per year can only be reconciled at one distance. That's
the **moving-cluster method**, and its natural subject is the Hyades, the V-shaped cluster
around Aldebaran in Taurus (see the chart[^stellarium]). The Hyades is close enough to sprawl across several degrees of
sky, which is exactly what makes the convergence visible.

Lewis Boss published the convergent point of the Hyades in 1908, from the proper motions of 41
stars and the radial velocities of three. For the first time, a star cluster had a distance
that didn't depend on knowing how bright any of its stars were.

{{< clear >}}

You can see the convergence for yourself in modern data. Take the Hyades stars measured by
Hipparcos, draw each one's motion across the sky, and extend it. The lines close in on one
region of sky in Monoceros, about 9° east of Betelgeuse: the direction the cluster is heading.
(We did this exercise for the figure below, and our convergent point lands within about a third
of a degree of the published Hipparcos values.)

{{< nbas-image src="fig-moving-cluster.webp" fullwidth="true"
caption="The Hyades' motions converge. Each arrow is one member star's motion across the sky over 50,000 years; the faint lines simply extend each star's own direction of motion. They close in near one point in Monoceros, the direction the cluster is heading through space. Data: Hipparcos, via the HYG database v4.1 (CC BY-SA 4.0); 110 members selected by space velocity."
alt="Map of the sky around the Hyades, north up and east left. About a hundred star dots, each with a short gold arrow pointing down and to the left. Faint lines extending the arrows converge on a blue X labeled convergent point, a little beyond Betelgeuse. Aldebaran is circled and labeled as a foreground star, not a member." >}}

The lines in the figure don't meet at a perfect point, and that's real. The method has its own
weaknesses, and they're instructive. It assumes the cluster is neither
expanding nor contracting, and it assumes you know which stars are really members. In 1974 one
review noted that the Hyades' proper-motion lines didn't meet at a point at all: they crossed
in a patch about 15° by 10°. Picking one plausible subset of members gave a distance of only 27
parsecs. For most of the twentieth century the accepted distance was about 40 parsecs; the
modern value is nearly 20% larger.

The settled answer came only with space astrometry. Hipparcos measured parallaxes for
individual Hyades stars and put the cluster center at 46.34 ± 0.27 parsecs (Perryman and
colleagues, 1998). Gaia's second data release puts it at 47.5 parsecs, about 155 light-years.
The moving-cluster method and the trigonometric parallaxes now agree, and the Hyades is no
longer an estimate. It's the first anchor above parallax itself.

{{< clear >}}

---

## Main-Sequence Fitting: The Hyades as a Template

Once you know the Hyades' distance, you know the true brightness of every star in it. Plot
them on an H-R diagram (color against brightness) and you get a clean main sequence: the band
where stars spend most of their lives burning hydrogen.

{{< nbas-image src="fig-hyades-cmd.webp" width="500" align="right"
caption="The Hyades on an H-R diagram. Gold: 132 cluster members, each placed by its own Hipparcos parallax. Gray: every Hipparcos star within 25 parsecs, a mix of ages. The cluster's stars, all born together, trace a narrow main sequence, with four red giants above it. Hipparcos stops near magnitude 12, so the cluster's faint end is missing. Data: HYG database v4.1 (CC BY-SA 4.0)."
alt="Scatter plot of true brightness against color. Gray dots from nearby stars form a broad diagonal band from bright blue at upper left to faint red at lower right. Gold dots for Hyades members lie along a narrow track within the upper part of that band, with four gold dots well above it at upper right labeled as the red giants gamma, delta-1, epsilon and theta-1 Tauri. The Sun is circled in the middle of the band." >}}

Now take any other cluster. Its stars form the same main sequence, but shifted fainter,
because the cluster is farther away. Slide the second cluster's main sequence up until it
lies on top of the Hyades', and the size of that shift, in magnitudes, *is* the distance
difference. This is **main-sequence fitting**, and it's the first true standard-candle method
in this chapter. The "lamp" isn't a single star; it's the whole main sequence, a pattern you
can recognize in any cluster with enough stars.

Main-sequence fitting is why the Hyades matters so much. A 1974 review put it plainly: the
Hyades provides the zero point for the Galactic distance scale, and, through the Cepheids that
sit in open clusters, a zero point for the extragalactic scale too. Perryman's team called
the Hyades one of the foundations on which the extragalactic distance scale ultimately rests.
Every distance farther out inherits whatever error the Hyades has.

That's not hypothetical. Harold Johnson's 1957 calibration of the main sequence shaped
open-cluster distances for about half a century. The Hyades distance he used turned out to be
about 15% too short, which pushed cluster distances off by around 0.3 magnitudes. Because the
Hyades was the zero point, every cluster distance tied to it came out short by the same amount.
One rung, one small error, carried upward into everything above it.

### What this rung reaches

With main-sequence fitting, the open clusters of our part of the Galaxy fall into reach. A few
examples:

- **The Pleiades** (M45), about 136 parsecs (444 light-years).
- **M35** in Gemini, about 2,800 light-years (0.86 kiloparsecs).
- **NGC 2158**, the faint, rich cluster right next to M35 in the sky, about 4.3 kiloparsecs
  (14,000 light-years) away: nearly five times farther, and more than ten times older.

How far can this candle shine? As far as you can measure the individual stars along a
cluster's main sequence. With the Hubble Space Telescope, astronomers have fitted the main
sequence of a star cluster in the Large Magellanic Cloud, a neighboring galaxy, and tied it
directly to the Hyades.

{{< nbas-image src="m_35-s50-5m.webp" width="480" align="right"
caption="M35 and NGC 2158. Bob Donahue, NBAS, Seestar S50, 5 min"
alt="Photograph of the open cluster M35, a loose spray of bright stars, with the smaller, fainter and more compact cluster NGC 2158 beside it." >}}

M35 and NGC 2158 in one view are a good way to feel this rung. They look like neighbors.
They're nowhere near each other, and main-sequence fitting is how we know.

The method has limits. Main sequences also shift with a cluster's chemical makeup and age, and dust
(more on that below) dims and reddens the whole thing. So main-sequence fitting works best with
few additional "complications," and, like all of the standard candles we'll encounter, it's only
as good as the corrections that go with it.

---

## The Break: The Pleiades and Hipparcos

When the Hipparcos satellite published its parallaxes in 1997, it gave astronomers what they
had wanted for a century: direct, space-based distances to the nearest clusters, free of any
assumption about stars. For the Hyades it agreed with main-sequence fitting nicely. But for the
Pleiades it didn't.

{{< nbas-image src="m_45-s30-69m.webp" width="380" align="right"
caption="Pleiades, Bob Donahue, NBAS, Seestar S30, 69 min"
alt="Photograph of the Pleiades: a tight group of bright blue-white stars wrapped in faint blue reflection nebulosity." >}}

Main-sequence fitting had long put the Pleiades at about 130 parsecs or a bit more. But Hipparcos 
said about 118 parsecs: roughly 10% closer. If Hipparcos was right, then the Pleiades' stars
were fainter than stellar models said they should be, implying that something was fundamentally wrong with our
understanding of young stars. If main-sequence fitting was right, then something was wrong
with Hipparcos, putting every one of its 118,000 stellar parallaxes in question.

The argument lasted more than fifteen years, and it got sharp. The resolution came from three independent directions:

- **The Hubble Space Telescope** measured parallaxes for three Pleiades stars directly in 2005:
  134.6 ± 3.1 parsecs.
- **Radio astronomers** used very long baseline interferometry (radio telescopes around the
  world working as one instrument) to measure four Pleiades star systems directly. Their 2014
  result: 136.2 ± 1.2 parsecs, with individual stars good to better than 1%.
- **Gaia**, the successor to Hipparcos, put the cluster at 135.8 parsecs in its 2018 data
  release.

So what was the problem?
The problem turned out to be in Hipparcos, specifically in how its data were reduced. 
The errors in its parallaxes weren't independent from star to star: stars close together in the
sky, within the satellite's field of view of about a degree, shared a common error. 
The Pleiades is compact, so its stars all shared the same offset. The Hyades is spread over many
degrees, so its errors largely averaged out, which is why it came through fine.

{{< nbas-image src="fig-pleiades-distances.webp" fullwidth="true"
caption="Distances to the Pleiades by method, in parsecs, with quoted uncertainties. The main-sequence value is a typical pre-1997 result. Sources: Percival et al. 2005; van Leeuwen 1999, 2009; Soderblom et al. 2005; Melis et al. 2014; Gaia Collaboration 2018."
alt="Dot chart of six Pleiades distance measurements. Two Hipparcos values sit near 118 and 120 parsecs. Main-sequence fitting (132), Hubble (134.6), radio VLBI (136.2) and Gaia (135.8) cluster together in a shaded band from 132 to 138 parsecs." >}}

The Pleiades is the cleanest example in this series of the ladder's logic. Two methods that
should have agreed didn't. Nobody could tell which was wrong until a third and fourth method, each
with its own independent weaknesses, weighed in. That's how a rung gets repaired: not by a
better measurement of the same kind, but via a measurement of a *different* kind.

---

## One Star at a Time: Spectroscopic Parallax

Clusters stand out in the sky, but most stars in the Galaxy don't belong to one; they're on their
own or in pairs. For them, astronomers needed a way to read true brightness off a single star.

In 1914, at Mount Wilson, Walter Adams and Arnold Kohlschütter found a way. Kohlschütter
noticed that certain ratios of spectral lines disagreed between stars of the same spectral type, and
that the disagreement tracked proper motion, which hinted at distance and therefore at true
brightness. The cause is physical. A giant star and a dwarf star of the same temperature have
very different atmospheres. The giant's is enormous and thin, at low pressure. In thin gas,
atoms collide less often, so spectral lines are narrower; and atoms that lose an electron are
slower to recapture one, so lines from ionized atoms are relatively stronger. Some lines respond
to these differences and some don't. Compare the two kinds and you can tell a giant from a
dwarf, and more finely, how luminous a star is.

{{< nbas-image src="fig-luminosity-spectra.webp" fullwidth="true"
caption="Same temperature, different size. Spectra of A0 stars, all about the same surface temperature, as a supergiant, a giant and a dwarf. The supergiant's thin, low-pressure atmosphere gives much narrower, shallower hydrogen lines (close-up of Hδ at right). At this resolution the giant and dwarf look nearly alike. Data: Pickles 1998 stellar spectral library (STScI)."
alt="Left: three stacked spectra from 382 to 500 nanometers, labeled supergiant, giant and dwarf, each with deep dips at the hydrogen lines H8, H-epsilon, H-delta, H-gamma and H-beta. The supergiant's dips are much narrower and shallower. Right: the H-delta line overlaid for all three; the dwarf and giant profiles are wide and deep, the supergiant's narrow and shallow." >}}

Calibrate those line ratios against stars with real parallaxes, and you can read a star's true
brightness from its spectrum: **spectroscopic parallax**. (The name is unfortunate. No parallax
is involved. It means "a distance, obtained from a spectrum.") The Mount Wilson astronomers
turned this revelation into a production line; within a few decades they had spectroscopic distances for
thousands of stars.

But we need to be honest about what this rung can and can't do. It's a calibration, not a 
measurement: a star gets sorted into a type and a luminosity class, then assigned the 
_typical_ true brightness for that class. In reality, stars of the same class aren't entirely identical. 
A 1921 review quoted an accuracy of about 20% for the Mount Wilson method, and that's in 
the right range for a single star, but still only a rough answer. Nonetheless, for thousands of stars, 
it was the first real map of the solar neighborhood beyond parallax.

---

## Leavitt's Law

At this point we're reaching a few thousand light-years at most. To go farther you need stars
that are both luminous (so you can see them far away) and recognizable (so you know what kind
of lamp they are). The breakthrough came from a stack of photographic plates at Harvard.

{{< nbas-image src="Leavitt_henrietta_b1.webp" width="350" align="left"
caption="Henrietta Swan Leavitt. Photographer unknown, before 1921, public domain, via Wikimedia Commons."
alt="Black-and-white portrait photograph of Henrietta Swan Leavitt." >}}

Henrietta Swan Leavitt was one of the Harvard "computers," the women who measured and
catalogued stars on the observatory's plates. She was assigned the Magellanic Clouds, two
star clouds visible from the Southern Hemisphere, photographed at Harvard's station in
Arequipa, Peru. In 1908 she published discoveries of 1,777 variable stars in the Clouds, and noted, 
almost in passing, that among a small group of them the brighter variables had the longer periods.

In 1912 she followed up with 25 variable stars in the Small Magellanic Cloud: stars of the same
type as δ Cephei, now called Cepheids. Plotted against the logarithm of their periods, their
brightnesses fell on a straight line. The paper was a Harvard circular signed by the director,
Edward Pickering, but its first sentence says the statement was prepared by Miss Leavitt. It's
her result, and it's now called **Leavitt's law**.

{{< clear >}}

Here's why it worked. Leavitt had no idea how far away the Small Magellanic Cloud was, and she
didn't need to. All its stars are at about the same distance from us, so differences in
*apparent* brightness between them are differences in *true* brightness. The Cloud was a
laboratory: a sample of Cepheids with the distance held constant.

Leavitt's law is a streetlight catalog. It says: tell me how long the lamp takes to flicker,
and I'll tell you its wattage. A Cepheid with a 10-day period is always more luminous than one
with a 3-day period, no matter how far away it is.

But there was a catch, and Leavitt saw it. She had the *slope* of the relation, not its *zero
point*. She knew how many times brighter a 10-day Cepheid was than a 3-day one, but not how bright
either one actually was, because she didn't know the distance to the Cloud. She wrote
that she hoped parallaxes of some variables of this type might be measured. None were near enough. 
Even today the nearest Cepheid is a subject of argument (see "Watch the Original Cepheid," below).

{{< nbas-image src="fig-leavitt-1912.svg" fullwidth="true"
caption="Leavitt's 25 Cepheids in the Small Magellanic Cloud, replotted from Table I of Harvard College Observatory Circular 173 (1912). Gold: brightness at maximum light; blue: at minimum. Against period (left) the stars trace a curve; against the logarithm of the period (right) they fall on straight lines. Lines are modern least-squares fits."
alt="Two side-by-side scatter plots of apparent magnitude for 25 variable stars. Left, against period in days, the points rise steeply and then level off. Right, against the logarithm of the period, the points at maximum and at minimum light each fall along a straight rising line." >}}

If you'd like the whole story of the Harvard computers, two good books tell it: Dava Sobel's
*The Glass Universe* (2016) and George Johnson's *Miss Leavitt's Stars* (2005).

---

## Hertzsprung Sets the Zero Point

A zero point came almost immediately, from Ejnar Hertzsprung in 1913, and it came by way of
the statistical method from earlier in this chapter. No single Cepheid in our Galaxy was close
enough for a parallax. But Hertzsprung could take thirteen of them, use their proper motions
and the Sun's motion through space, and find their *average* distance. That gave him their
average true brightness, and that gave Leavitt's line its first zero point. It was a rough one,
and the rest of this chapter is partly the story of fixing it.

{{< nbas-image src="fig-zero-point.svg" width="600"
caption="Slope and zero point. Leavitt's 25 stars (blue) show how bright Cepheids look: the slope of the line. One calibration (gold star) says how bright they really are, sliding the whole line up. The size of that slide is the Cloud's distance. Schematic: the gap is not drawn to scale. Data: Harvard College Observatory Circular 173 (1912), Table I."
alt="Graph of brightness against pulsation period. A lower blue line runs through 25 blue dots labeled how bright they look, Leavitt's 25 stars, 1912. A parallel gold line higher up is labeled how bright they really are, with a gold star on it labeled Hertzsprung's anchor: 13 Milky Way Cepheids, their average distance found by secular parallax. A double arrow between the lines reads the gap equals the Cloud's distance." >}}

Then he did the obvious next thing: he turned it around and asked how far away the Small
Magellanic Cloud must be. His answer, a parallax of 0.0001 arcseconds, corresponds to about
33,000 light-years. That was, by a wide margin, the largest distance ever measured for anything.
Walter Baade later recalled that the second-largest at the time was the Hyades, at about 130
light-years.

Hertzsprung's paper, however, said 3,000 light-years. Somewhere between the parallax and the
printed page, a factor of ten went missing. Shapley and Russell later noticed and corrected it.
It's a small story, but it fits the theme of this series: even the first great leap outward
came with an error you had to catch.

From 1913 until 1952, astronomers treated this as settled: one period–luminosity relation for
all Cepheids, calibrated by statistical parallaxes. Harlow Shapley used it to map the globular
clusters and move the center of our Galaxy tens of thousands of light-years away from the Sun.
Edwin Hubble used it to measure the distance to the Andromeda galaxy. Both stories belong to
later chapters. What matters here is that the rung looked solid, and it was being used to hold
up everything.

---

## Why Would a Star Obey a Law?

Leavitt's law is a strange thing to find in nature. Why should a star's pulsation period have
anything to do with how much light it gives off?

Part of the answer was worked out by Arthur Eddington in the late 1910s. A pulsating star rings
like a bell, and a bell's pitch depends on its size and density. For a star, the pulsation
period depends on its average density: big, puffy stars of low density pulsate slowly, and
compact ones quickly. Cepheids are yellow supergiants, and among them the bigger ones are both
less dense and more luminous. So a longer period means a bigger star, and a bigger star means
more light.

{{< nbas-image src="fig-instability-strip.webp" width="500" align="right"
caption="Where the pulsating stars live. Gray: Hipparcos stars within 200 parsecs, showing the main sequence and the giants. Stars that wander into the instability strip (shaded; drawn schematically) pulsate: bright supergiants there are Cepheids, like δ Cephei; old helium-burning stars there are RR Lyrae stars. Dashed lines mark stars of equal size, in units of the Sun's radius. Data: HYG database v4.1 (CC BY-SA 4.0)."
alt="H-R diagram of luminosity against surface temperature on logarithmic scales, hot stars at left. A dense gray band of nearby stars runs from upper left to lower right (the main sequence), with a branch of giants rising to the right. A shaded blue strip slants up through the middle near 6,000 to 7,500 kelvin. Gold stars mark delta Cephei high in the strip, RR Lyrae lower in the strip at about 50 times the Sun's luminosity, and the Sun on the main sequence. Dashed diagonal lines mark radii of 0.1, 1, 10 and 100 Suns." >}}

Why they pulsate at all took longer. Eddington compared a Cepheid to a heat engine with a valve:
a layer that traps heat when the star is squeezed and releases it when the star expands. In the
1950s Sergei Zhevakin identified the valve as a layer of helium in the star's outer envelope,
where the degree of ionization changes the layer's opacity as the star is compressed and
expanded. Only stars of the right temperature have that layer at the right depth, which is why
Cepheids occupy a narrow strip in the H-R diagram.

For the ladder, this matters because it turns Leavitt's law from a lucky pattern into physics.
Nature makes standard lamps when a phase of a star's life pins its brightness. Cepheids are
one such phase. The next rung is another.

---

## RR Lyrae: The Streetlights of the Halo

RR Lyrae stars are also pulsating variables, but smaller and older than Cepheids: their periods
run from a few hours to about a day. They're the most useful lamps among the oldest stars in the
Galaxy, the ones in the halo and in globular clusters.

The reason they work as a standard is unusually clear. An RR Lyrae star is an old, low-mass star
that has finished burning hydrogen in its core and is now burning helium there. Stars like this
arrive at the helium-burning stage with cores of nearly the same mass, about half the Sun's,
almost regardless of how massive they were to begin with. The core sets the luminosity. So RR
Lyrae stars all have nearly the same true brightness: about 50 times the Sun's, absolute
magnitude around +0.6. The exact value depends a little on the star's chemical makeup, and
pinning it down has been a long effort. But as lamps go, they're very consistent.

The star the class is named for, RR Lyrae itself, varies between magnitude 7.1 and 8.1 every 13
hours and 36 minutes, at a distance of about 270 parsecs (900 light-years). It's a binocular
star, but a summer one: at 6:30 PM EST at the end of December it's about 30° up in the west-northwest
and sinking.

### What this rung reaches

RR Lyrae stars are faint compared with Cepheids, but they're everywhere old stars are, and
that opens up the oldest parts of the Galaxy:

- **The globular clusters.** M13 in Hercules, the best-known in the northern sky, is about 7.4
  kiloparsecs (24,000 light-years) away.
- **The center of the Galaxy.** In the 1940s, Walter Baade found a small gap in the dust clouds
  of Sagittarius, now called Baade's Window, and saw crowds of RR Lyrae stars through it. In 1951
  he used them to estimate the distance to the center of the Galaxy: 8.7 kiloparsecs. The best
  modern value is 8.2 kiloparsecs (about 26,700 light-years). For a first try at measuring the
  distance to the middle of the Galaxy using variable stars, that's remarkably close.

{{< nbas-image src="m_13-s50-16m-square.webp" width="280" align="left"
caption="M13, the Great Globular Cluster in Hercules. Bob Donahue, NBAS, Seestar S50, 16 min"
alt="Photograph of the globular cluster M13: a dense ball of hundreds of thousands of stars, brightest at the center and thinning toward the edges." >}}

{{< nbas-image src="ngc_6522-s50-17m.webp" width="480" align="right"
caption="Baade's Window, a gap in the dust about 4° from the direction of the Galactic center. The globular clusters NGC 6522 and NGC 6528 sit in it, and the dark nebulae B298 and LDN 41 mark its edge. Through windows like this, Baade found crowds of RR Lyrae stars and used them to measure the distance to the center of the Galaxy. Bob Donahue, NBAS, Seestar S50, 17 min"
alt="Dense star field crowded with faint orange stars, with two compact globular clusters labeled NGC 6522 and NGC 6528. Below NGC 6528, darker star-poor patches are circled and labeled B298 and LDN 41. Coordinate grid lines cross the field." >}}

{{< clear >}}

The same Walter Baade is about to break the rung that Hertzsprung built.

---

## The Rung That Was Two Rungs

When the 200-inch telescope at Palomar came into service, Walter Baade had a specific test in
mind. If Hubble's distance to the Andromeda galaxy was right, then Andromeda's RR Lyrae stars,
with their well-known true brightness, should appear just at the limit of the new telescope's
plates, around magnitude 22.

They weren't there. With the biggest telescope in the world, Baade could see Andromeda's
brightest old stars but not a single RR Lyrae variable star.

The only way out was that Andromeda had to be farther away than everyone thought, and the reason was
that there are **two kinds of Cepheid variables**: bright, young ones in the disks of galaxies
(the ones Leavitt studied, and the ones Hubble found in Andromeda), and older, fainter ones
found among old stars, now called Type II Cepheids. Both kinds pulsate with periods of a
few days to a few weeks, so a period alone doesn't tell you which kind you're looking at. But
at the same period, the young ones are about 1.5 magnitudes brighter. The early calibrations had
lumped the two together. In streetlight terms, the road had two kinds of lamp, LED and sodium,
that flicker at the same rates, and the catalog had treated them as the same thing.

{{< nbas-image src="fig-two-cepheid-relations.svg" width="500"
caption="Two kinds of Cepheid. At the same period, a classical Cepheid is about 1.5 magnitudes brighter than a Type II Cepheid, a factor of two in distance. Schematic: only the gap between the lines is to scale."
alt="Schematic graph of true brightness against pulsation period. Two parallel rising lines: a solid gold line labeled classical Cepheids above a dashed blue line labeled Type II Cepheids. A double arrow between them reads 1.5 magnitudes equals 2 times in distance." >}}

At the International Astronomical Union meeting in Rome in September 1952, Baade announced the
correction. A difference of 1.5 magnitudes is a factor of two in distance. Every distance
measured with classical Cepheids beyond our Galaxy doubled overnight, and so did the size of the
known universe. At the same meeting, David Thackeray reported RR Lyrae stars in the Magellanic
Clouds, fainter than the old scale predicted, another crack in the rung.

Who deserves the credit has been argued since. Shapley presented the corrected scale to the
American Astronomical Society the following year, and his name appeared on early press accounts.
The discovery that drove it was Baade's.

From here on in this series, "Cepheid" means a classical Cepheid, on the corrected scale.

---

## The Fog: Interstellar Dust

There's one more correction every rung in this chapter needs, and it came from checking one
rung against another.

In 1930 Robert Trumpler at Lick Observatory measured about 100 open clusters two ways. First by
brightness: from the types and magnitudes of their stars, he worked out how far away they must
be. Second by size: assuming clusters of a given kind are about the same physical size, he worked
out distances from how big they looked. The two methods should agree.

They didn't. The brightness distances were systematically larger than the size distances, and
the gap grew with distance. The stars looked fainter than they should for how far away their
clusters were. Something between us and the clusters was absorbing light: dust, spread through
the disk of the Galaxy, dimming starlight by roughly 0.7 magnitudes per kiloparsec. (In [The
Galactic Anticenter](/articles/2026/12/galactic-anticenter/) we met the same dust from the
observer's side.)

{{< nbas-image src="fig-dust-extinction.webp" fullwidth="true"
caption="Trumpler's test, repeated with modern data. Each dot is an open cluster, with its distance and how much dust dims it, from Gaia data (Cantat-Gaudin et al. 2020). The gold line follows the median; the blue dashed line is Trumpler's 1930 average of about 0.7 magnitudes per kiloparsec. The farther the cluster, the more fog in the way, with a lot of scatter from direction to direction. Beyond about 2 kpc the median levels off; one likely reason is that the catalog misses clusters hidden behind the thickest dust."
alt="Scatter plot of about 1,900 open clusters: dimming by dust, in magnitudes, against distance up to 6 kiloparsecs. The points spread widely but rise with distance. A gold median line climbs along a blue dashed reference line of 0.7 magnitudes per kiloparsec out to about 2 kiloparsecs, then flattens near 1.5 magnitudes. The Pleiades, M35 and NGC 2158 are circled." >}}

In our streetlight metaphor, that's fog on the road. A lamp seen through fog looks dimmer than it is, so it looks farther away
than it is, and the farther away it is, the more fog its light passes through. Every
brightness-based rung (main-sequence fitting, spectroscopic parallax, Cepheids, RR Lyrae) has
needed an extinction correction ever since. Shapley's 1918 map of the globular clusters, made before Trumpler, had none.

The logic is the same as the Pleiades: two rungs that should agree didn't, and the disagreement was the discovery.

---

## Wrapup: The Lower Ladder as It Stands

Here's what the lower rungs reach, with a landmark for each. Most of them are in the winter
evening sky.

| Rung | What it rests on | Landmark | Distance |
|------|------------------|----------|----------|
| Trigonometric parallax | Earth's orbit | 61 Cygni | 3.5 pc (11 ly) |
| Moving cluster | Proper motions + Doppler shifts | Hyades | 47.5 pc (155 ly) |
| Main-sequence fitting | The Hyades | Pleiades | 136 pc (444 ly) |
| Main-sequence fitting | The Hyades | M35 | 0.86 kpc (2,800 ly) |
| Cepheids | Statistical, then direct, parallaxes | δ Cephei | ~245–275 pc (~800–900 ly) |
| RR Lyrae | Statistical, then direct, parallaxes | M13 | 7.4 kpc (24,000 ly) |
| RR Lyrae | as above | Center of the Galaxy | 8.2 kpc (26,700 ly) |

{{< nbas-image src="fig-rung-reach.svg" fullwidth="true"
caption="Landmarks of the lower ladder, each with the rung that put it in reach. The shaded band shows roughly how far parallax reached around 1900. Distance scale is logarithmic."
alt="Chart with one row per landmark, sorted by distance on a logarithmic scale from a few parsecs to tens of kiloparsecs: 61 Cygni 3.5 pc by parallax; Hyades 47.5 pc by the moving-cluster method; Pleiades 136 pc and M35 860 pc and NGC 2158 4.3 kpc by main-sequence fitting; delta Cephei about 260 pc as a Cepheid calibrator; M13 7.4 kpc and the Galactic center 8.2 kpc by RR Lyrae. A shaded band covers distances out to 25 parsecs, labeled parallax circa 1900." >}}

Each rung rests on the one below. The Hyades rests on parallax and on the moving-cluster method,
now in agreement. Main-sequence fitting of other clusters rests on the Hyades. Cepheids and RR Lyrae rest on
statistical parallaxes first, and now on direct parallaxes from Hubble and Gaia. Every
brightness-based rung carries a correction for dust. And the Cepheids carry a label, "classical,"
because they were once two rungs pretending to be one.

Each of these rungs broke, and each break was found the same way: by checking one method against
another that should have agreed. That's the lesson of the ladder. No single method is trusted on
its own; the confidence comes from methods with different weaknesses giving the same answer.

The next time you look at the Hyades and the Pleiades on a winter night, you're looking at the
two clusters that held up the distance scale and, for more than fifteen years, argued over it. The Hyades
is the foundation; the Pleiades is the warning. Everything farther out in this series stands on
both.

---

{{< nbas-callout title="Watch the Original Cepheid" >}}
You can watch a rung of the distance ladder from your backyard.

On October 19, 1784, a young English amateur named John Goodricke began a run of observations of
δ Cephei, a modest star at the base of the "house" of Cepheus. Over the next two months he found
that it brightened and faded on a precise cycle: 5 days, 8 hours, and about 37 minutes. (His
friend and neighbor Edward Pigott had found the first star of this kind, η Aquilae, a few weeks
earlier.) δ Cephei gave the whole class its name.

It varies between about magnitude 3.5 and 4.4, rising quickly to maximum and fading more slowly.
On winter evenings it's well up in the northwest: about 60° high at 6:30 PM EST at the end of
December, and still about 44° high at the end of January. From a dark site it's a naked-eye
star; from town, binoculars help.

{{< nbas-image src="fig-delta-cep-chart.svg" width="500"
caption="Finder chart for δ Cephei. Comparison-star magnitudes are given without the decimal point, as on AAVSO charts: 34 is ζ Cephei (3.4), 42 is ε Cephei (4.2). μ Cephei is itself variable; don't use it for comparison. Stars to magnitude 5.5; data from the HYG database v4.1 (CC BY-SA 4.0)."
alt="Star chart of Cepheus, north up, drawn as a house shape: γ at the peak, β and ι at the eaves, α and ζ at the base. δ Cephei is marked with a gold variable-star symbol just east of ζ, labeled 3.5 to 4.4. Nearby comparison stars carry blue magnitude labels: 34 for ζ, 42 for ε, 50 for λ, 43 for ν, and 35 for ι." >}}

To follow it, compare it each clear evening with its neighbors. ζ Cephei (magnitude 3.4), about
2½° to the west, is a little brighter than δ ever gets. ε Cephei (4.2), just south of ζ, is a
little brighter than δ at its faintest. λ Cephei (5.0), just north of ζ, is fainter than δ ever
gets. Each night, decide where δ falls between them. Over a week or two, the cycle shows itself.

{{< nbas-image src="fig-delta-cep-size.svg" width="380" align="right"
caption="δ Cephei to scale with the Sun and Mercury's orbit. Over each 5.4-day cycle its radius swings between about 41 and 45 times the Sun's (pale ring: its largest). Radius from Bailleul et al. 2026, via Wikipedia."
alt="To-scale diagram: a large gold disk labeled delta Cephei, 41 to 45 times the Sun's radius, with a paler ring around it showing its largest size. A tiny white dot labeled the Sun sits nearby. A dashed circle, Mercury's orbit, surrounds the disk at about twice its radius." >}}

What you're watching is a yellow supergiant, about 1,900 times as luminous as the Sun,
swelling and shrinking. Its radius swings between about 41 and 45 times the Sun's; put in the
Sun's place, its surface would reach about halfway to the orbit of Mercury. Its distance is among the
best measured of any Cepheid, which makes it one of the anchors of Leavitt's law: the Hubble Space Telescope 
put it at 273 parsecs (about 890 light-years) in 2002, from a parallax of 3.66 thousandths of an arcsecond; 
a later analysis gives 244 ± 10 parsecs.

Strangely, the *nearest* Cepheid isn't δ Cephei. It's **Polaris**, the North Star, which also pulsates, with a
period of almost exactly four days, but by only a few hundredths of a magnitude: too little to see
by eye. Polaris shows how hard this rung is even close to home. Hipparcos put it at about 133
parsecs; one group argued for 99 pc; a Hubble measurement of its companion gave 160 pc; Gaia's
measurement of the companion gives about 137 pc. For the North Star, of all stars, the distance has
been genuinely in dispute for years.

{{< clear >}}
{{< /nbas-callout >}}

---

### Footnotes

[^stellarium]: Star fields rendered with Stellarium (stellarium.org); Stellarium contributors, Stellarium v26.2 (2026), doi:10.5281/zenodo.23020615; G. Zotti et al., "The Simulated Sky: Stellarium for Cultural Astronomy Research," *Journal of Skyscape Archaeology* 6(2), 221–258 (2021), doi:10.1558/jsa.17822.
