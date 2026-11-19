---
title: "How Far Can We See?"
date: 2027-03-08
description: "How far can we see? The universe is 13.8 billion years old, yet the most distant light we receive comes from places now 46 billion light-years away -- and for galaxies past a redshift of about 1.85, the light they send today will never reach us. Three horizons, what disappears when, and why we live in a privileged moment to be measuring the universe at all."
byline: "Three horizons, and a window that's closing."
authors: ["bob-donahue"]
series: ["astronomical-frameworks"]
thumbnail: "thumbnail.webp"
banner: "banner-horizons.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 14

---
<!-- NOTE: can't have [^refs] in captions - they come out verbatim -->
<!--
D14 v8 (2026-11-18, Claude): final editorial pass on Bob's v7 (torus CHECK resolved by Bob: "never this
  thin again"). Intro: "most of the observable universe" (was "most of the galaxies we can see" -- true
  by volume, not by catalog). "For everything". (1 + z) notation made consistent. "What stays" moved to
  the end of the timeline list (chronology). "Merged" removed where the merger is only 50/50. Loeb
  footnote: posted 2001.
D14 v6 (2026-11-18, Claude): from Bob's v5. Spectrum passage fact-checked and reworded (4.6 um; 851 nm;
  Gunn-Peterson trough, footnoted). Table + z 0.5 and 1.0. Fading: Bob's 'IR to radio' wording. M31 ->
  'What stays'. 'thinned' -> 'dimmed'. Epilogue titles matched to Bob's list. 'supposed' -> 'hypothetical'.
D14 v4 (2026-11-18, Claude): from Bob's v3 (index-d14-v3-bob.md) and his NOTEs:
  - "Reply" dropped (we only ever receive). Event-horizon section rebuilt around TODAY'S LIGHT: will the
    light a galaxy sends today ever reach us? (Bob's "replay": the same arithmetic as our light reaching
    it.) Round-trip zone (8.3 Gly) and its table removed; new table = when today's light arrives.
  - Five-zone table -> four zones, receiving only.
  - "What Disappears When" now separates two kinds of disappearing: the horizon (a galaxy's present never
    reaches us) and fading (its old light stretched and slowed until no detector can catch it) -- Bob's point.
  - Ceiling (63) explained with ants that all set off at the beginning (Bob: "can't comprehend").
  - "the faster it grows, the faster it grows" -> compound interest.
  - Bob's Planck chart dropped (source unknown; F2 shows the same thing).
  - NEW fig-ant-on-rope (Bob's cartoon idea): real numbers for the z = 6 quasar's light.
  - Density NOTE answered in prose: denser AND busier (cosmic noon, Gaia-Enceladus) but less clumpy.
  - CMB NOTE answered: z ~ 1,090; ~3,000 K then, 2.7 K now.
  - Re-applied from v2 after Bob's v3 branched: CMB-"galaxies like ours" sentence; ant footnote source.
  - Banner and F1 relabeled for the receiving framing; F1 axis "scaled to today".
Numbers: claude/how-far-can-we-see-facts.md + scripts (Planck 2018 via astropy unless footnoted).
OPEN: none.
-->

## Introduction

{{< nbas-image src="banner-horizons.webp" fullwidth="true"
caption="Two horizons over 80 billion years of cosmic time, with distances scaled to today. Gold: the farthest places whose light has reached us. Blue: the farthest places whose light, sent at that moment, will ever reach us. The gap between them only grows."
alt="Two curves against time, with a thin vertical line marking today. A gold curve labeled light has reached us rises steeply and levels off near 63; a dashed blue curve labeled light sent today will reach us falls from the top left toward zero. They cross early on, and the region between them is shaded." >}}

The last article ended with a hypothetical galaxy reported "at redshift 7," with no distance attached. That wasn't
an oversight. Out there, "how far away is it?" stops having one answer, and so does the question this
whole series has been building toward: how far can we see?

The universe is about 13.8 billion years old, so the obvious answer is 13.8 billion light-years. It's
wrong, and the ways it's wrong are the subject of this article. "How far can we see" turns out to be at
least three different questions:

- **How long has the light been travelling?** At most, 13.8 billion years.
- **How far away is its source *now*?** For the most distant light we receive, about 46 billion
  light-years.
- **How far away can a galaxy be, and still have the light it sends *today* reach us someday?** About
  17 billion light-years -- and most of the observable universe is already beyond it.

Each answer is a different horizon. Together they say something the earlier rungs of the ladder never
hinted at: we're measuring the universe during a particular, temporary window, and it is slowly closing.

---

## How Long vs. How Far

In everyday life, travel time and distance are interchangeable. A star 100 light-years away sent the
light you see 100 years ago, and it's (very nearly) still 100 light-years away today. For everything 
in this series up to now, that has been close enough to true.

It stops being true when the trip is long enough for the universe to change while the light is on its
way. Space keeps stretching beneath the light during its whole journey, and the source keeps moving
off with the expansion. So two numbers come apart: how long the light travelled (astronomers call it
the **lookback time**), and how far away its source is today.

{{< nbas-image src="fig-distance-vs-redshift.webp" fullwidth="true"
caption="How long the light has travelled, and how far away its source is today, by redshift (Planck 2018 cosmology). Travel time levels off at 13.8 billion years; distance keeps climbing toward 46 billion light-years. The vertical line marks the event horizon, explained below."
alt="Graph against redshift on a log axis. A blue dashed curve, light travel time, levels at 13.8 billion years. A gold curve, distance today, climbs toward 46 billion light-years. A vertical line at redshift 1.85 marks the event horizon. Points mark a redshift-6 quasar at 27.5 billion light-years and 12.9 billion years, and the cosmic microwave background at 45.3 and 13.8." >}}

At small redshifts the two curves lie on top of each other: that's the range where the simple division
of the last article worked. Then they part company. The travel time levels off -- no light can have
been travelling longer than the universe has existed -- while the distance keeps climbing.

### An ant on a rubber rope

There's an old puzzle that captures this better than any equation. An ant sets off along a rubber
rope, crawling at a steady pace toward the far end. While it crawls, someone stretches the rope --
evenly, everywhere, including the stretch ahead of the ant and the stretch behind it.

When the ant arrives, three numbers describe its trip, and they're all different: how long the rope was
when it set out, how long it is when it arrives, and how long the ant was crawling. Measure the trip by
the time it took, and you'll badly underestimate how long the rope is *now*.

Light crossing the universe is the ant. The rope is the space between a galaxy and us. And the three
numbers are the galaxy's distance when the light left, its distance today, and the lookback time. The
redshift adds a fourth: one plus the redshift (1 + *z*) is how many times longer the rope is now than when the
ant set out. Redshift is a label on the *light* -- how much stretching happened during its trip. It
doesn't say where the galaxy is now; we have to work that out.

{{< nbas-image src="fig-ant-on-rope.webp" fullwidth="true"
caption="The ant on the rope, with real numbers: light from a quasar at redshift 6 (Planck 2018 cosmology). Each row is one moment, drawn to scale. The tick marks are fixed points on the rope; they spread apart as it stretches. For its first few billion years the light actually got farther from us, then the stretching slowed enough for it to close in."
alt="Four horizontal bars, one above the other, each running from a blue dot labeled us to a gold star labeled quasar. At 0.9 billion years after the Big Bang the bar is 3.9 billion light-years long and the light is just setting out. At 4 billion years it is 10.5 long and the light, a white dot, is 5.9 from us. At 9 billion years it is 19.0 long and the light is 4.0 from us. Today it is 27.5 long and the light has arrived. Evenly spaced tick marks on each bar spread farther apart from row to row." >}}

Take a quasar at redshift 6 -- a brilliant young galaxy core, the kind found by the hundred in deep
surveys. Its light has been travelling for 12.9 billion years. It is now 27.5 billion light-years
away. And when that light set out, the quasar was only about 4 billion light-years from the spot where
our galaxy would one day be.[^z6]
<!-- COMPUTED: Planck18 comoving distance z=6: 27.48 Gly; lookback 12.86 Gyr; distance then 27.48/7 = 3.93 Gly.
Snapshots (proper, Gly): t=0.93 quasar 3.93 light 3.93; t=4 10.51/5.88; t=9 19.01/4.05; today 27.48/0. -->

Wait -- 12.9 billion years to cross a gap of 4 billion light-years? That's the ant. The rope kept
stretching while the light crawled along it. For its first 3 billion years or so, the light actually
lost ground: the rope between it and us was stretching faster than it could crawl, and the gap grew to
almost 6 billion light-years. Only as the expansion rate dropped did it begin to close in. And a
redshift of 6 says the rope is now seven times as long as when the light set out. Every wave of the
quasar's light has been stretched by the same factor of seven, exactly as much as the universe itself
has grown since the light left.

You can see that stretching in the quasar's spectrum. The hydrogen-alpha line, red light at 656.3 nm
in the lab, arrives far into the infrared, at about 4.6 micrometres. Hydrogen's Lyman-alpha line, at
121.6 nm deep in the ultraviolet, arrives just past the red end of what our eyes can see, at about
851 nm. And across the whole visible range, the quasar's spectrum is almost completely dark. That light
started out bluer than Lyman-alpha, and on its way here it passed through hydrogen gas between the
galaxies, which soaked it up. The spectrum only switches on at the stretched Lyman-alpha line.[^gp]

Two more things the rope makes easy. First, the tick marks: a galaxy stays at the same mark on the rope
however much it stretches, so astronomers often label places by where they are *today* -- their distance
"scaled to today." That's the scale of the figures in this article. Second, turning a redshift into
today's distance takes more than the redshift itself. You need to know how fast the rope was being
stretched at every moment along the way -- the universe's whole expansion history, which comes from
the same standard model the last article ended on.

### Your neighborhood used to be a city

Run that stretching backward and the universe gets crowded. If distances between galaxy groups have
grown by a factor of seven since that quasar's light set out, then everything was packed seven times closer in
each direction. In [Beyond the Local
Group](/articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/) we gave our corner of the
universe neighborhoods: groups, clusters, the sheet we live in. Those neighborhoods used to be denser.
Five billion years ago, around the time the Sun was forming, the universe on average was about three
times as dense as today. Ten billion years ago, about twenty times.[^density]
<!-- COMPUTED: lookback 5 Gyr -> z = 0.47, (1+z)^3 = 3.2; 10 Gyr -> z = 1.72, (1+z)^3 = 20. -->

That's an average, and two cautions come with it. Our own Local Group never took part: it's held
together by its own gravity, so it didn't expand, and the crowding happened *between* groups like ours.
And "the same galaxies, closer together" isn't quite right either. Galaxies merge, so there were more,
smaller ones then.

A denser city is a busier one, and the record shows it. Around ten billion years ago, the universe as a
whole was making stars faster than at any time before or since -- astronomers call that era "cosmic
noon."[^noon] Collisions were more common too: each galaxy then could expect more mergers than one
today.[^mergers] Our own galaxy has the scar to prove it. Its last big collision, with a smaller galaxy
now called Gaia-Enceladus, happened about ten billion years ago, and that galaxy's stars still make up
much of the Milky Way's inner halo.[^ge]

But denser didn't mean lumpier. The big structures of today -- rich clusters, long filaments, empty
voids -- were still gathering themselves then; gravity has been pulling matter out of the voids and
into the clusters ever since. The neighborhood used to be a crowded but fairly even city. It has been
spreading out and clumping up at the same time.

---

## Everything That Has Reached Us: The Particle Horizon

Now push the redshift as far as it will go. The farthest light we can see at all is the **cosmic
microwave background** (CMB), released when the universe was about 380,000 years old and first became
transparent. Its light has travelled for almost the entire 13.8 billion years. It has the biggest
redshift we can measure, about 1,090: the rope has stretched more than a thousand times since it left.
It set out as the glow of gas at about 3,000 degrees -- close to the temperature of a cool star's
surface -- and arrives as microwaves at 2.7 degrees above absolute zero. The gas that released it is
now about 45 billion light-years away.[^cmbdist] By now, that gas has had 13.8 billion years to become
galaxies like ours. We see it as it was, 380,000 years after the beginning.
<!-- COMPUTED: 2.7255 K x 1,091 = 2,974 K. -->

Earlier than that, the universe was an opaque glowing fog, so no light from before the CMB can reach
us. But in principle there's a boundary just beyond it: the distance from which *anything* -- light,
or any signal at all -- could have reached us by now, if it had set out at the very beginning. That's
the **particle horizon**, and today it sits about 46 billion light-years away.[^ph]

The particle horizon is what people usually mean by the edge of the **observable universe**: a sphere
about 46 billion light-years in radius, centered on us. It isn't 13.8 billion light-years, because
13.8 billion years is how long the light has travelled, not how far away its source is now. (Double it
and you get its diameter: a little over 90 billion light-years.)

Two things are worth noticing about this edge. It isn't a wall in space -- there's no reason to think
the universe ends there. It's a boundary in *time*: the farthest anything could be and still have had
time for its light to reach us. And it grows. Every year, light from a little farther away arrives for the first
time, and the observable universe gets a little bigger.

So the observable universe is growing. That would seem to be the whole story -- wait long enough and
we'll see everything. It isn't, and the reason is the expansion's acceleration.

---

## Today's Light: The Event Horizon

Everything we see is a replay. The quasar's light shows us the quasar as it was 12.9 billion years ago;
the CMB shows us gas that has long since become galaxies. So here's the question that matters: the
light a galaxy is sending *today* -- the light that would show us what it's like now -- will it ever
get here?

Back to the ant. The puzzle's surprise is that if the rope is pulled at a steady speed, the ant
*always* gets there. It may take an absurdly long time: each step covers a smaller and smaller
fraction of the whole rope, but those fractions, added up, grow without limit.[^ant] A universe whose
expansion keeps slowing down is gentler still: light from anywhere eventually arrives. But suppose the
rope grows by a fixed *percentage* every second, like money earning compound interest -- the longer the
rope gets, the faster it grows. Then there's a point on it beyond which the ant can crawl forever and
never arrive.

That's our universe. Since about 1998 we've known that the expansion is speeding up -- the "dark energy"
of the last article -- and it's heading toward exactly that compound-interest stretching.

So there's a boundary. Light that a galaxy inside it sends today will reach us eventually. Light that a
galaxy beyond it sends today never will -- not in a billion years, not ever. That boundary is the
**cosmological event horizon**. Today it lies about 17 billion light-years away (16.6, in Planck's
cosmology), and a galaxy sitting exactly on it has a redshift of about 1.85.[^eh]
<!-- COMPUTED: Planck18, integral of c dt/a from now to infinity = 16.58 Gly; z where comoving distance = 16.58: 1.852. -->

Close to the horizon, the wait gets absurd. Here's when the light a galaxy sends today will arrive:

| Galaxy's distance today (billions of light-years) | Its redshift | Its light from today arrives in |
|---|---|---|
| 1 | 0.07 | 1.0 billion years |
| 5 | 0.38 | 6.1 billion years |
| 6.4 | 0.5 | 8.2 billion years |
| 10 | 0.87 | 16 billion years |
| 11.1 | 1.0 | 19 billion years |
| 15 | 1.57 | 41 billion years |
| 16 | 1.74 | 58 billion years |
| beyond 16.6 | beyond 1.85 | never |
<!-- COMPUTED (Planck18): integrate c dt/a from today until it equals the comoving distance. -->

The same boundary works in the other direction: light *we* send today reaches only galaxies inside it.
Point a laser at our redshift-6 quasar now, 27.5 billion light-years away, and the beam chases it for
all eternity without arriving.

Every galaxy past a redshift of about 1.85 is already beyond the horizon, and galaxies at redshift 2,
3, 6 are routine targets for large telescopes. We're still receiving their *old* light, seeing what they looked like *then*. 
But the light that would show us what they've become never will arrive. We'll go on watching their pasts, and their
replays will slow, redden and fade, each one stuck short of some moment in the galaxy's life that never
reaches us -- like a clock that never quite reaches a particular hour. Abraham Loeb worked this out in
2001: a galaxy at redshift 5 to 10 will only ever be seen up to an age of about 4 to 6 billion years.
We will never see what it looks like at the age our own galaxy is now.[^loeb]

### The farthest we will ever see

The event horizon puts a limit on the particle horizon, too. Picture ants setting off toward us at the
very beginning, from every mark on the rope. Today, the ants from marks within 46 billion light-years
(scaled to today) have arrived: that's the particle horizon. Ants from farther marks are still
crawling. Some of them will make it someday, so the particle horizon keeps creeping outward. But with
the rope stretching like compound interest, ants that started past about 63 billion light-years never
will.[^ceiling]

So there's a ceiling. Every galaxy whose mark on the rope is within about 63 billion light-years will
eventually send us at least a little light; nothing beyond will ever be seen at all. The observable
universe isn't just big. It's bounded.

---

## A Gap That Only Grows

So we have two horizons. The particle horizon, about 46 billion light-years away, marks the farthest
places whose light has reached us. The event horizon, about 17 billion light-years away, marks the
farthest places whose light from today will ever reach us. Between them lies a band: galaxies we can
see, but only in replay. Put it all together, and everything sorts into four zones by distance today:

| Distance today (billions of light-years) | Redshift | What we get |
|---|---|---|
| 0 to 16.6 | up to about 1.85 | Their past now, and eventually their present |
| 16.6 to 46 | 1.85 to the CMB and beyond | Their past only, slowing and fading |
| 46 to 63 | -- | Nothing yet; their first light is still on its way |
| beyond 63 | -- | Nothing, ever |
<!-- COMPUTED (Planck18): event horizon 16.58 (z 1.852); particle horizon 46.2; ceiling 62.8. -->

The second row is the band. By volume, it holds about 95 percent of the observable universe: most of
what we can see, we can only ever see as it was.
<!-- COMPUTED: 1 - (16.58/46.20)^3 = 0.954. -->

{{< nbas-image src="fig-horizons-over-time.webp" fullwidth="true"
caption="The two horizons over 60 billion years (Planck 2018 cosmology), with distances scaled to today. Inside the shaded band are galaxies whose past we can see but whose present will never reach us. The band opened 4.2 billion years after the Big Bang and only grows."
alt="Graph of distance, scaled to today, against time since the Big Bang. A rising gold curve, the particle horizon, reaches 46 billion light-years today and levels toward a ceiling of 63. A falling blue dashed curve, the event horizon, is at 17 today. The curves cross at 4.2 billion years, and the region between them, labeled we see their past, never their present, is shaded." >}}

That band hasn't always been there. The event horizon depends on the universe's whole future -- it
asks whether light sent now will *ever* arrive -- so in a universe that will keep accelerating forever,
it has always existed. But for the first 4.2 billion years it lay *beyond* the particle horizon: every
galaxy whose past we could see, we would eventually see in the present too. Then the two lines
crossed, and the band opened.[^cross] Curiously, that was more than three billion years before the
expansion actually began to speed up, about 7.6 billion years after the Big Bang. The future was already
shaping what could be seen long before it arrived.
<!-- COMPUTED: PH = EH at a = 0.395, z = 1.53, t = 4.19 Gyr, 31.4 Gly. Acceleration starts where
Om(1+z)^3 = 2 OL: z = 0.645, t = 7.62 Gyr. -->

Without that acceleration, there'd be no band at all. In a universe containing only matter, the
expansion keeps slowing, and wait long enough and light from everywhere -- from any moment in any
galaxy's life -- eventually arrives. There's no event horizon.

From here on, the band only widens. The particle horizon creeps up toward its 63-billion-light-year
ceiling; the event horizon, on the same scaled-to-today map, shrinks toward nothing. Today the band is
about 30 billion light-years deep. It will never be this thin again.

One more thing the figure doesn't show: none of this is about our special place. Every galaxy has its
own pair of horizons, centered on itself, and an observer in a galaxy past our event horizon will never
see *our* present, either. Nobody is at the edge. Everybody is at the center of their own window.

---

## What Disappears When

There are two ways for a galaxy to disappear, and they're easy to confuse.

The first is the horizon. Once a galaxy is past it, its *present* never reaches us. But that doesn't
make it vanish: its older light is still on the way, and keeps arriving.

The second is fading, and that's what actually empties the sky. For a galaxy past the horizon, each
new batch of old light that arrives has been stretched more than the last: its redshift keeps climbing,
without limit. Its light slides from the visible into the infrared and on toward radio waves. And it's
stretched in time as well: every second of the galaxy's life arrives spread over more and more of ours,
so each second's worth of light is dimmer. The replay slows, reddens and dims, until no telescope or
detector we know how to build can catch what's left.
<!-- Certain for every galaxy beyond the event horizon: z of arriving light -> infinity. (Today, for
z > ~2, the redshift drifts slightly DOWN; in the long run, under accelerating expansion, it rises
without limit. Not needed in the prose.) -->

{{< nbas-image src="fig-what-disappears-when.webp" fullwidth="true"
caption="What disappears when, in billions of years after the Big Bang (log scale; future times are rough). Sources: Planck 2018 calculation; Sawala et al. 2025; Krauss & Scherrer 2007."
alt="Timeline on a logarithmic scale. Past: 4.2, the event horizon slips inside what we can see; 7.6, expansion starts to speed up. Today, 13.8. Future: about 21 to 22, a 50/50 Milky Way and Andromeda merger; about 100, every galaxy beyond the Local Group gone and the cosmic background at radio wavelengths; before about 700, the background blocked by our galaxy's own gas." >}}

**Already cut off.** For everything past a redshift of about 1.85, we'll never see the present. We
still see those galaxies, and will for a very long time -- but only as they were.

**The next few billion years.** The most distant galaxies freeze and fade, each stuck at an earlier
point in its life the farther away it is.

**About 100 billion years.** By then, every galaxy beyond the Local Group has long since slipped past
the event horizon, and the last of its old light has been stretched and dimmed beyond any hope of
detection. Lawrence Krauss and Robert Scherrer, who worked out this timetable in 2007, put it on the
order of 100 billion years.[^ks] The night sky of that era holds the Local Group and nothing else.

**The CMB fades, then vanishes.** By about 100 billion years after the Big Bang, the background's
brightest wavelengths have stretched to about a meter -- radio waves -- and its brightness has dropped by
a factor of about a trillion. Before the universe is 50 times its present age, its waves become too
long to pass through even the thin gas between the stars of our own galaxy. The glow that showed us our
own motion in the last article will be shut out by our own back yard.[^cmbfade]

**What stays.** One thing never disappears: the Local Group. It's bound by its own gravity, so the
expansion won't pull it apart. Whether the Milky Way and Andromeda merge in the meantime -- the latest
analysis puts the odds at about even[^m31] -- doesn't change that. Either way, the Local Group is what
the far-future sky will hold.

---

## The End of Cosmology

Krauss and Scherrer's paper had a provocative title: "The Return of a Static Universe and the End of
Cosmology." Their question was simple. Suppose astronomers live in the Local Group 100 billion years
from now. What can they learn about the universe?

Modern cosmology rests on three observations, and each one disappears:

- **The expansion.** Hubble's law needs distant galaxies, receding. There are none left to see.
- **The CMB.** Our best snapshot of the early universe will be stretched out of detection and screened
  by the gas of their own galaxy.
- **The light elements.** The amounts of hydrogen, helium and deuterium made in the first minutes are
  a third pillar of the Big Bang. By then, generations of stars will have buried the original helium
  under their own, and the fragile deuterium will be largely gone.

Those far-future astronomers could still work out that their island of stars has a finite age. But they
would have every reason to conclude that they live in a single galaxy, alone in an endless, empty,
unchanging void.[^ks]

That picture should sound familiar. It's close to the picture many astronomers held before 1925: one
great star system, with nothing of note beyond it, in a universe that wasn't expanding. [The Local
Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/) told the story of how a
distance measurement to Andromeda overturned it. In a hundred billion years, the evidence that
overturned it will be gone. The future astronomers won't be careless; they'll simply be right about
everything they can see.

Which leaves us in an odd position. We live early enough that the distant galaxies are still visible,
the CMB is still bright, and the original helium is still mostly unburied -- and late enough that
there are astronomers around to look. The window for doing cosmology at all is open now. It won't
stay open.

---

## Epilogue: The Window We're Standing In

If you've followed this miniseries from the beginning, this is the last stop. (If you've landed here
first: welcome. What follows looks back over thirteen earlier articles, and every one of them is linked
below.)

<!-- 
1. Measuring Distance | /articles/2026/10/measuring-distance/
2. Distance at Solar System Scale | /articles/2026/10/distance-at-solar-system-scale/
3. The Speed of Light | /articles/2026/11/the-speed-of-light/
4. /articles/2026/11/measuring-the-astronomical-unit/
5. /articles/2026/12/parallax/
6. Parsecs vs. Light Years | /articles/2026/12/parsecs-vs.-light-years/
7. Building the Distance Ladder | /articles/2026/12/building-the-distance-ladder/
8. Distance at Galactic Scale | /articles/2027/01/distance-at-galactic-scale/
9. A Tour of the Milky Way Galaxy | /articles/2027/01/a-tour-of-the-milky-way-galaxy/
10. The Local Group: A Distance That Changed the Universe | /articles/2027/01/the-local-group-a-distance-that-changed-the-universe/
11. Extending the Ladder: Beyond the Cepheids | /articles/2027/02/extending-the-ladder-beyond-the-cepheids/
12. Beyond the Local Group: The Universe in Megaparsecs | /articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/
13. Velocities and the Hubble Tension | /articles/2027/02/velocities-and-the-hubble-tension/
14. How Far Can We See? | /articles/2027/03/how-far-can-we-see/
-->

The series started by asking how anyone builds an intuition for scale, in [Measuring
Distance](/articles/2026/10/measuring-distance/). [Distance at Solar System Scale](/articles/2026/10/distance-at-solar-system-scale/) made the
first rung something you could feel. [The Speed of Light](/articles/2026/11/the-speed-of-light/), [Measuring the
Astronomical Unit](/articles/2026/11/measuring-the-astronomical-unit/) and [Parallax](/articles/2026/12/parallax/) built the first tools, 
and [Parsecs vs. Light Years](/articles/2026/12/parsecs-vs.-light-years/) gave the stars a ruler and a neighborhood.

[Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/) built the lower rungs,
and showed that every rung can break and be repaired. [Distance at Galactic Scale](/articles/2027/01/distance-at-galactic-scale/) 
made the Galaxy a place we toured in [A Tour of the Milky Way Galaxy](/articles/2027/01/a-tour-of-the-milky-way-galaxy/), 
and [The Local Group: A Distance That Changed the Universe](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/) 
crossed the first fence, out of the Milky Way and into a universe of galaxies. [Extending the
Ladder: Beyond the Cepheids](/articles/2027/02/extending-the-ladder-beyond-the-cepheids/) built the upper rungs, [Beyond the
Local Group: The Universe in Megaparsecs](/articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/) made the wider
universe a place, and [Velocities and the Hubble
Tension](/articles/2027/02/velocities-and-the-hubble-tension/) ended on the one crack not yet repaired.

Finally, this article adds a condition to all of it. Every rung -- the parallaxes, the Cepheids, the
supernovae, the redshifts -- depends on light that is still arriving from places that are still
visible. That's a fact about *when* we live, not just where.

Every article in this series has been about a window we happen to be standing inside of, at a moment in
the universe's life when it's still open. It's open tonight. Go outside and look through it.
<!-- Closing-line direction from the notes ("not final"). Last sentence added to point back at the sky
(PHILOSOPHY: "everything here should ultimately point toward the sky"). Bob's call. -->

## Footnotes

[^z6]: Our calculation with astropy's Planck 2018 cosmology: comoving distance 27.5 billion light-years, lookback time 12.9 billion years. The distance when the light set out is the comoving distance divided by 1 + *z* = 7. The figure's snapshots are from the same calculation.

[^gp]: Line wavelengths times 1 + *z* = 7 (our arithmetic). The dark stretch is called a Gunn–Peterson trough; it was first seen completely in a quasar at redshift 6.28 (R. H. Becker et al. 2001, *AJ* 122, 2850).

[^density]: Our calculation, same cosmology: the average density scales as (1 + *z*)³; lookback 5 billion years is *z* = 0.47 (factor 3.2), 10 billion years is *z* = 1.72 (factor 20). The Sun's age, about 4.6 billion years, is the standard value.

[^noon]: P. Madau & M. Dickinson 2014, *Annual Review of Astronomy and Astrophysics* 52 (arXiv:1403.0007): the cosmic star-formation rate peaked about 3.5 billion years after the Big Bang, at redshift about 1.9.

[^mergers]: E.g., "Observational constraints on the merger history of galaxies since z ≈ 6: probabilistic galaxy pair counts in the CANDELS fields" (arXiv:1903.12188): the number of mergers per galaxy goes down toward the present.

[^ge]: A. Helmi et al., *Nature*, 1 November 2018; ESA, "A major event in the formation of the Milky Way" (30 October 2018).

[^cmbdist]: Our calculation, same cosmology, for redshift 1,090 (Planck Collaboration 2020, *A&A* 641, A6): 45.3 billion light-years. The age at that time, about 380,000 years, is the standard-model value. The temperature then is today's 2.7255 K times 1 + *z*.

[^ph]: Our calculation, same cosmology, including radiation: 46.2 billion light-years.

[^eh]: Our calculation, same cosmology: event horizon 16.6 billion light-years today; redshift of a galaxy on it, 1.85. Arrival times in the table are from the same calculation. In the far future the event horizon's real size approaches 17.4 billion light-years.

[^ant]: The "ant on a rubber rope" is a classic recreational-mathematics puzzle, popularized by Martin Gardner in *Scientific American* (see Wikipedia, "Ant on a rubber rope"; T.-Y. Hsiao 2021, arXiv:2101.03890); who first posed it is not established. The answer for a steady pull follows from the harmonic series, which grows without limit. For stretching by a fixed percentage, the ant's progress adds up to a finite total, so beyond a certain starting distance it never arrives.

[^loeb]: A. Loeb 2002, *Physical Review D* 65, 047301 (arXiv:astro-ph/0107568, posted 2001).

[^ceiling]: Our calculation, same cosmology: today's particle horizon plus today's event horizon, 46.2 + 16.6 ≈ 63 billion light-years, scaled to today.

[^cross]: Our calculation, same cosmology: the horizons cross 4.2 billion years after the Big Bang (redshift 1.53); acceleration begins at redshift 0.64, 7.6 billion years after the Big Bang.

[^m31]: T. Sawala et al. 2025, *Nature Astronomy*: a merger probability of about 50 percent within 10 billion years; if a merger happens, it is more likely 7–8 billion years from now. See also [The Andromeda Family of Galaxies](/articles/2026/09/the-andromeda-family-of-galaxies/).

[^ks]: L. M. Krauss & R. J. Scherrer 2007, "The Return of a Static Universe and the End of Cosmology," arXiv:0704.0221; one of the Gravity Research Foundation's essay prizes for 2007.

[^cmbfade]: Krauss & Scherrer 2007: at about 100 billion years the CMB peaks near 1 m, with its intensity down by about 12 orders of magnitude; the interstellar medium's plasma frequency (about 1 kHz) blocks it once the universe has expanded by about 10⁸ more, "when the universe is less than 50 times its present age."
