---
title: "Parallax"
date: 2026-12-07
description: "Every star traces a tiny copy of Earth's orbit each year; its size gives the distance. Why it took until 1838 to see one, and how Gaia measured a billion."
byline: "Seeing one tiny motion through all the others"
authors: ["bob-donahue"]
series: ["historical-perspectives"]
thumbnail: "thumbnail.webp"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 5
---

<!-- TRY 2 — v5: author pass through "Three Bets" merged with drafted later sections (2026-10-17). Framing: project doc measuring-distances-framing.md.
     Each section has an OUTLINE comment: beats, budget, figure, what to reuse from TRY1 v4.
     BOOK-INSERT comments mark where book-only "going deeper" material hangs. Same skeleton
     for article and book. Target: ~3,000–3,500 words for the article. -->
<!-- description/byline: new (v7). Alternatives in chat 2026-10-18. -->

## Introduction

{{< nbas-image src="banner.webp" fullwidth="true"
caption="The sky around 61 Cygni as Bessel measured it in 1837–38. Instead of fixing the star's position, he measured its distance from two fainter stars nearby, *a* and *b*, night after night for more than a year. Over a year those two gaps grow and shrink by a fraction of an arcsecond: the parallax. Rendered with Stellarium.[^stellarium]"
alt="Star field with 61 Cygni near the center. Two thin lines run from it to two fainter stars labeled a (SAO 70898) and b (SAO 70930)." >}}

The [last article](/articles/2026/11/measuring-the-astronomical-unit/) ended with the astronomical unit in hand — the size of Earth's orbit, in real miles — and a suggestion: use that orbit itself as a baseline. Look at a star in January, look again in July, from two points 186 million miles apart, and see whether it shifts.

You already know the trick. Hold up a thumb at arm's length and look at it with one eye, then the other: your thumb jumps against the wall behind it. Your eyes are a few inches apart, and that's enough. Bring your thumb closer and it jumps more; move it away and it jumps less. That jump is a *parallax*, and its size tells you how far away your thumb is.


Now do it with the whole Earth as one eye, and the Earth six months later as the other. Over a full year, something incredible happens:

**Every star in the sky traces a tiny copy of Earth's orbit, once a year. The farther away the star, the smaller the copy. Measure the size of that copy, and you have the distance.**

{{< nbas-image src="fig-parallax-geometry.svg" fullwidth="true"
caption="In January and in July, Earth sits on opposite sides of the Sun, and a star appears in slightly different places against much more distant stars. Over the whole year, its image traces a small ellipse — a copy of Earth's orbit — with the January and July positions at its two ends. The parallax p is the angle that the radius of Earth's orbit, 1 AU, makes as seen from the star. A more distant star (right) traces a smaller copy. Not to scale."
alt="Two side-by-side diagrams. In each, Earth is shown in January and[O July on opposite sides of its orbit around the Sun, with sight lines crossing at a star and continuing to the distant background stars, where they land at the two ends of a gold ellipse. Left, a nearby star: wide sight lines and a large ellipse, with the angle p at the star and the 1 AU orbital radius marked. Right, a more distant star: narrower sight lines and a much smaller ellipse." >}}


That's the entire model, and nobody doubted it would happen. Copernicus's Sun-centered system required it to be true. And yet it took nearly three centuries after Copernicus for anyone to see a single star doing it, and almost two more before a spacecraft could do it for a billion stars.

The catch is that the angle is minuscule — and it isn't the only thing moving. **Everything** in the sky is moving: the stars, the Earth, the air you look through, even the telescope you look with. For the first time in this series, motion isn't the tool. It's what's in the way.

This is the story of how astronomers learned to see one very small motion through all the others.

{{< clear >}}

## How Small Is the Copy?

Just how tiny are we talking about? Picture a friend, about 5 feet 7 inches tall, standing next to you — who then starts walking away.

{{< article-table align="right" >}}

| Your friend is… | …this far away |
|---|---|
| 1° tall | 100 m — a football field |
| 1′ tall | 5.8 km — 3.6 miles |
| 1″ tall | 350 km — 218 miles |
| 0.29″ tall | 1,200 km — 760 miles |

{{< /article-table >}}

A football field away, your friend stands one degree tall — about two full Moons, one on top of the other, just enough to cover with your pinky finger at arm's length. Keep walking. At 3.6 miles your friend is now one *arcminute* tall: a sixtieth of a degree, and coincidentally, about the finest detail the human eye can make out. Your friend has become a dot.

But even finding a clear view over such a relatively short distance to see your arcminute-tall friend is hard: hills, buildings, trees and haze are already in the way. 
Stand downtown in North Adams and look up at the summit of Mount Greylock, about five miles away: anyone standing up there is already too small for your eye to make out. So suppose your friend has brought a big, brightly colored flag. Through a pair of 10× binoculars, five miles looks like half a mile, and there it is: a bright speck of color on the summit.

But it won’t hold still. However steadily your friend holds that flag, it shimmers and jumps around in your binoculars, because there are five miles of churning air between you, the same shimmer you see over a hot road in summer. Keep that picture in mind. It’s exactly what happens to starlight, and it’s the problem at the center of this whole story.

For smaller angles you need a telescope. At 218 miles your friend is now one *arcsecond* tall, a sixtieth of an arcminute.  From here (in North Adams) that's Philadelphia, or if you're not from here, the distance between New York City and Washington DC.  That's a distance we can "feel", but it's already a chore to traverse: a few hours by car.  And of course it's impossible to *see* because of the curvature of the Earth.

And 61 Cygni — the star at the center of this story, one of the nearest to the Sun — traces a copy of Earth's orbit only 0.29 arcseconds in radius. That's your friend, 760 miles away — in Chicago (measured from North Adams), or between New York City and Atlanta. Distances we can "feel" from travels, but effectively impossible to visualize line of sight:  they've reached "far away" - even a plane trip is going to take up a chunk of your day.

Here is the real problem. Even on a good night, the air turns every star into a shimmering blur at least an arcsecond wide, and often more. The shift astronomers were hunting was at a scale already far smaller than the blur they were looking through. They weren't watching the crisp point of light of a star move; they were finding the center of a smudge, night after night, to a small fraction of its width.

And the blur doesn't sit still. From moment to moment the star's image dances around inside it — that's the twinkling — so every single measurement lands in a slightly different place, and only many of them, averaged, find the center.   All of a sudden that child's lullaby has become something from the soundtrack of a horror movie!

{{< nbas-image src="fig-seeing-blur.svg" fullwidth="true"
caption="What the parallax hunters were up against. Left: in any one instant, the air breaks a star's light into speckles, and the whole pattern jumps around. Right: averaged over time, it settles into a smooth blur about an arcsecond and a half wide on a good night. The gold ellipse is 61 Cygni's yearly parallax, at the same scale. Simulated; the speckle pattern is schematic."
alt="Two square panels with a one-arcsecond scale bar. Left: a cluster of bright blue-white speckles scattered around and off-center from a gold cross marking the star's true position. Right: a smooth round glow about one and a half arcseconds wide, with a small gold ellipse at its center, much smaller than the glow." >}}

{{< clear >}}

## Nothing Holds Still

Every other science can take its question into a lab. A chemist can weigh the same sample twice, or monitor a reaction. A physicist can hold a ruler against a bench that doesn't move, or even collide particles at close to the speed of light.

Astronomy's lab is the entire cosmos, and it can't even hold the ruler still. To see a star's tiny copy of Earth's orbit, you have to strip away everything else that moves it around on the sky — and almost everything does.  Even for something that ought to be a steady point of light, like a faraway star, our observations have to contend with:

- **The observer.** Earth isn't just *where* it is; it's moving, 18 miles every second, and it's not even steady as a globe - its axis slowly drifts and nods.
- **The target.** The stars themselves drift across the sky - and through space.
- **The medium.** The air bends and blurs starlight, by different amounts on different nights.
- **The reference.** Whatever you measure the star against is moving too.
- **The ruler.** Telescopes and measuring screws change size with the temperature.
- **The zero.** Even the point you call "no shift at all" has to be checked.

{{< nbas-image src="fig-onion-layers.svg" fullwidth="true"
caption="Everything that moves 61 Cygni's apparent position, compared with the one motion astronomers wanted: its parallax (gold). The scale is logarithmic — each step to the right is ten times larger. Values for 61 Cygni; ranges show how much the effect varies. Differential refraction is calculated for Bessel's two comparison stars."
alt="Horizontal bar chart on a logarithmic scale. From largest to smallest: precession 50 arcseconds per year, aberration 20.5, nutation 9.2, proper motion 5.3 per year, seeing 1 to 3, differential refraction 0.14 to 0.4, then the parallax at 0.286 highlighted in gold, temperature effects 0.04 to 0.1, comparison stars' parallax 0.002, and Gaia's zero-point 0.000017 arcseconds." >}}

The parallax sits in the middle of that list, outweighed by almost everything above it, with smaller errors from everything below it hiding inside the measurement. Getting to the precise value is like peeling an onion: one layer at a time, from the outside in, and then sorting out the lower layers, to arrive at just the _one_ layer we're after.

And that's roughly how the history went. The biggest layers were understood first; the smallest took until this century. So that's the order this article follows.

## Peeling the Parallax "Onion"

### The Observer Moves

If the Earth goes around the Sun, the stars have to shift their positions. In the old Earth-centered picture there should be no shift at all, so when Copernicus put the Sun at the center and nobody could see the stars move, that null result became an argument *against* him. The only way out was that the stars would have to be unimaginably far away.

People kept looking anyway. In 1674 Robert Hooke announced that he'd found the parallax of Gamma (&gamma;) Draconis — a star that passes almost straight overhead in London, where the atmosphere bends its light least. He'd cut a hole in his roof to watch it, and claimed a shift of about 30 arcseconds from just four observations. Few were convinced.[^perryman]

Then in 1725, Samuel Molyneux and James Bradley set out to check Hooke's claim, with the same star.[^timberlake] Gamma Draconis _did_ move — by about 20 arcseconds — but not the way Hooke had reported, and three months out of step with where a parallax shift should be. It wasn't parallax at all. It was *aberration*: the tilt in starlight caused by Earth's motion through it, which gave the [speed of light](/articles/2026/11/the-speed-of-light/) its first good value.

{{< nbas-image src="fig-parallax-vs-aberration.svg" fullwidth="true"
caption="Earth's orbit, seen twice. Over a year, aberration moves 61 Cygni around an ellipse about 40″ across (left); parallax moves it around an ellipse of the same shape, 70 times smaller (right, magnified). The two are three months out of step: aberration follows Earth's velocity, parallax follows its position. On the left, the parallax ellipse is drawn at the same scale — it's the dot in the middle."
alt="Two panels. Left: a large gold ellipse about 40 arcseconds across, with months marked, and a tiny blue dot at its center labeled as the parallax ellipse at the same scale. Right: the blue parallax ellipse magnified 70 times, the same shape, with its months three months out of step with the left panel." >}}

<!-- RESOLVED: yes — semi-major axis p, semi-minor p·|sin β| (β = ecliptic latitude). Circle at the ecliptic pole, line on the ecliptic. -->

Here is the first layer of the onion, and it's Earth itself. Earth's orbit shows up in the sky *twice*. Its **position** — where Earth is along its orbit — draws the parallax ellipse, the one astronomers wanted. Its **velocity** — which way Earth is moving — draws the aberration ellipse: the same shape, seventy times larger, and a quarter of a year out of step. Anyone looking for parallax first had to understand aberration, or risk mistaking one for the other.

But Bradley's discovery did something else, too. It proved - directly - that the Earth moves.[^perryman] So, from 1729 on, nobody needed to detect parallax to prove Copernicus right. Now it was needed to comprehend how big the universe is.

Half a century later, William Herschel tried a different approach: find two stars close together on the sky but very different in brightness. The faint one is presumably far behind the bright one (he assumed, incorrectly, that all stars have roughly the same intrinsic brightness), so the bright one should wobble back and forth against its partner over a year. He catalogued hundreds of such pairs in the 1780s. When he came back to them, decades later, many had moved — not back and forth with the seasons, but around each other. In 1803 he announced that many double stars are real pairs, orbiting each other — he coined the term "binary star." He'd found binary stars, but still no parallax.[^williams]

### The Star Moves

The stars move too. In 1718 Edmond Halley compared his own positions for Sirius, Arcturus and Aldebaran with those recorded by Greek astronomers and found that all three had shifted.[^perryman] The "fixed" stars weren't fixed at all: each one drifts slowly across the sky, its individual *proper motion*.

That presented both a problem and a clue at the same time. A problem, because the drift doesn't stop: 61 Cygni moves 5.3 arcseconds every year — eighteen times its parallax, every single year. The parallax is a small wiggle riding on a long, steady slide.


{{< nbas-image src="fig-61cyg-sky-track.svg" fullwidth="true"
caption="Left: 61 Cygni's path across the sky over three years — a steady drift of about 5.3″ a year, with a small yearly wobble on top. Right: the same path with the steady drift removed, leaving the parallax ellipse, with the first of each month marked. Computed from modern values."
alt="Two panels. Left: a nearly straight diagonal line across about 13 arcseconds, with a slight wiggle, marked 2026 through 2029. Right: an ellipse about half an arcsecond across, with the first of each month marked around it." >}}

To separate them you have to watch for more than a year. Over a few months, part of the wiggle looks exactly like drift — the star happens to be swinging the same way it's sliding. Only full cycles tell the two apart.

But the drift was a clue, too. A star that crosses the sky that fast is _probably_ close — the same way a nearby car seems to race past while a distant airplane barely crawls. 61 Cygni moves faster across the sky than any other star you can see without a telescope; Giuseppe Piazzi had nicknamed it the "Flying Star" in 1804. It's only a hint, though: stars move in three dimensions, and a star heading mostly toward or away from us barely drifts across the sky at all, however close it is. Still, it was a good hint — and it's why such an otherwise unassuming star became one of the three "bets" for which star would yield its true distance.

{{< nbas-image src="61cyg-field-1837-2026.webp" fullwidth="true"
caption="The same patch of sky in 1837 (left) and today (right). Bessel's comparison stars, a and b, have barely moved; 61 Cygni has slid about 16½ arcminutes — roughly half the width of the full Moon. Its parallax, the thing Bessel was after, would be far smaller than a single pixel in these pictures. Rendered with Stellarium.[^stellarium]"
alt="Two framed star fields side by side. Left, 1837: 61 Cygni near the center with stars a and b below it, and an empty circle up and to the left marking where it is in 2026. Right, 2026: 61 Cygni now up and to the left, with an empty circle marking its 1837 position; stars a and b are in the same places in both." >}}

### Three Bets, and the Race

Before you can measure a star's parallax, you have to choose which star to measure — and nobody knew which stars were close enough to make the first attempts. Each of the three astronomers who first succeeded selected different targets, for different reasons.

**Friedrich Georg Wilhelm Struve**, at Dorpat (now Tartu, Estonia), chose Vega, one of the brightest stars in the sky. Bright, he reasoned, probably means close.

**Friedrich Wilhelm Bessel**, at Königsberg, chose 61 Cygni, dimly visible to the naked eye. His bet was on speed: Piazzi's Flying Star.

**Thomas Henderson**, at the Cape of Good Hope, had Alpha Centauri: both bright *and* fast.

All three bets paid off. And notice what each bet was: a guess about distance, made from brightness or motion, even before any distance had ever been measured.

But what had changed by the 1830s to make the attempts practical?  It was the glass. Joseph von Fraunhofer, in Munich, was making the finest lenses in the world, and two of his instruments were now in the hands of astronomers who meant to use them for exactly this.

{{< clear >}}

<!-- RESOLVED comparison stars (Reid & Menten 2020; SIMBAD):
     a = BD+37 4173 = SAO 70898 = Gaia DR3 1871944114244360960, V 8.85, K0, plx 2.448 mas; 462″ at PA 201° (1838)
     b = BD+37 4179 = SAO 70930 = Gaia DR3 1872026646335106688, V 8.28, M0, plx 1.976 mas; 706″ at PA 109° (1838) -->

**Peeling three layers at once.** The trick was not to measure where 61 Cygni was at all. Instead, Bessel measured the *gap* between 61 Cygni and two faint stars right next to it on the sky, one about 8 arcminutes away and one about 12.[^rm] Stars that close together are bent by the air almost equally, shifted by aberration almost equally, and carried along by the drift of Earth's axis almost equally. In the gap between them, those big effects nearly cancel. What's left is the difference in their parallaxes — plus 61 Cygni's own steady drift.

{{< nbas-image src="heliometer.webp" fullwidth="true"
caption="How a heliometer measures: the main lens is cut in half, and each half makes its own image of the sky. Slide one half along the cut until one star’s image sits on top of the other’s, then read how far you slid it off a calibrated dial: that’s the angle between the two stars."
alt="Two-part diagram of a heliometer. Left: the telescope’s main lens drawn as a circle cut in half along a horizontal line, with two stars visible in the field of view. Right: the two halves slid sideways past each other along the cut, so that the images of the two stars now sit on top of each other; the distance the halves had to slide is labeled as the angular distance between the stars." >}}

His instrument was a *heliometer*: a telescope whose main lens is cut in half, so the two halves can slide past each other and make two images of the sky. Slide until the image of 61 Cygni sits on the image of the comparison star, read off how far you had to slide, and you've measured the gap — to a few hundredths of an arcsecond, with care. Night after night, for more than a year.

**Here's the clever part.** You know the *shape* of the yearly wiggle before you start: it's Earth's orbit, as seen from the star. For a star straight above or below the plane of Earth's orbit — at the ecliptic poles, in Draco and Dorado — it's a circle. The closer a star sits to that plane, the flatter the ellipse, until a star right on the ecliptic just slides back and forth along a line. You know its *timing* too. The only thing you don't know is its *size*. So a year of measurements comes down to three numbers: where the gap started, how fast it drifts, and how big the yearly wobble is. The third number is the parallax.  And whatever you observe has to follow those rules — a built-in check on whether what you've found is parallax at all.

{{< nbas-image src="fig-parallax-ellipses-trio.svg" fullwidth="true"
caption="The parallax ellipses of the first three stars measured, drawn at the same scale: the modern values (solid) and the values first announced (dashed). Each ellipse's shape is set by where the star sits relative to the plane of Earth's orbit; only its size depends on distance. Struve's first value for Vega lies almost exactly on the modern one — see below for why that was luck."
alt="Three panels at the same scale. Alpha Centauri: a dashed announced ellipse noticeably larger than the solid modern one. 61 Cygni: dashed and solid ellipses nearly matching, about half an arcsecond across. Vega: a tiny ellipse - almost circular - dashed and solid almost identical." >}}

**The finish line.** Henderson *measured* first. He was at the Cape for only thirteen months, in 1832 and 1833, observing Alpha Centauri with a mural circle — a large instrument for measuring star positions. He left in ill health, became Scotland's first Astronomer Royal, and didn't work through his Alpha Centauri observations for years. His paper was read to the Royal Astronomical Society in January 1839: a parallax of 1.16 arcseconds, putting the star about 2.8 light-years away.[^hend]

Struve *published* first. In 1837, after seventeen measurements, he announced a tentative parallax for Vega of 0.125 arcseconds — about 26 light-years — and promised more data.

Bessel announced in the autumn of 1838: 0.314 arcseconds, give or take 0.020, putting 61 Cygni about 657,000 AU — 10.4 light-years — away.[^bessel] The AU itself was still Encke's value from the last article, about 2.5% too large — but next to a 6% uncertainty in the parallax, that hardly mattered.


| Star | Observer | The bet | Observed | Published | Parallax | Distance | Modern |
|------|----------|---------|----------|-----------|----------|----------|--------|
| Alpha Centauri | Henderson | bright *and* fast | 1832–33 | Jan 1839 | 1.16″ ± 0.11″ | 2.8 ly | 0.751″ — 4.34 ly[^acen] |
| Vega | Struve | bright | 1835–36 | 1837 | 0.125″ ± 0.055″ | 26 ly | 0.130″ — 25.0 ly |
| 61 Cygni | Bessel | fast | 1837–38 | Nov 1838 | 0.314″ ± 0.020″ | 10.4 ly | 0.286″ — 11.40 ly |
<!-- Modern values: alpha Cen 750.81 ± 0.38 mas (ALMA, Akeson et al. 2021); Vega 130.23 ± 0.36 mas (Hipparcos 2007 reduction); 61 Cyg A 285.99 mas (Gaia DR3). Struve's 1840 revision moved to "The Ruler Moves". -->

It's Bessel who is remembered as being first, and it was Bessel his rivals credited — Struve included. His wasn't the first measurement, or the first publication. It was the first that was *convincing*: more than a year of dense measurements, two comparison stars, a careful accounting of his errors, and a result that held up.

{{< nbas-callout kind="note" title="Who Was First?" >}}
Measured first: Henderson, 1832–33.
Published first: Struve, 1837.
Believed first: Bessel, 1838.

Three different "firsts." Credit went to the case that convinced — which is often how it goes. We'll see another priority argument when we reach the cosmic distance ladder.
{{< /nbas-callout >}}

### The Reference Moves

Nonetheless, there's an obvious problem with measuring gaps. The comparison star is a star. It has its own tiny copy of Earth's orbit — exactly the same shape and timing, just smaller, provided it's farther away. So the gap doesn't wobble by 61 Cygni's parallax. It wobbles by 61 Cygni's parallax *minus* the comparison star's.

{{< nbas-image src="fig-relative-parallax.svg" width="380" align="right"
caption="Both stars wobble. A comparison star a few arcminutes away traces an ellipse of exactly the same shape and timing as the target star, just smaller - depending on how much further away the comparison star is. What you measure — the gap between them — traces the difference. Illustrative numbers."
alt="Three nested ellipses of the same shape: a large blue one for the target star, a small gold one for the comparison star, and a dashed one in between labeled what you measure, the gap." >}}

Every parallax measured from the ground this way is *relative*: it's measured against stars that are moving too. If a comparison star happens to be closer than your target, the answer can even come out *negative* — a star apparently farther away than infinity, a sure sign that something is wrong.

The defense is to choose comparison stars much fainter than the target. Faint doesn't guarantee far, but it's a good bet: most faint stars in any small patch of sky are hundreds of light-years away or more. Bessel's two turn out, by modern measurement, to have parallaxes less than a hundredth of 61 Cygni's — far smaller than his own uncertainty.[^rm]

Using several comparison stars helps too, because a bad one shows itself by disagreeing with the others. What no amount of checking can do is prove that the whole set has zero parallax. If every star in the field were a little closer than you assumed, every gap would stay exactly the same. For the next 150 years, astronomers corrected for that leftover with an estimate of how far away faint background stars typically are.

{{< clear >}}

<!-- BOOK-INSERT: "Measuring a Star Field" — heliometer gaps vs photographic plates (fig-gaps-vs-plates);
     the n(n−1)/2 discussion (positions contain every gap); plate solutions and rejected reference stars;
     the statistical relative→absolute correction (TODO: size, Yale catalogue intro). -->

### The Ruler Moves

And then, for a while, things got *worse*.

Struve and Bessel both went back to improve their first results — more nights, more measurements — and both revised answers came out further from the truth, not closer. That sounds backward, but it's a trap every precise measurement has to watch for. More measurements shrink the *random* scatter. They do nothing about an error that every measurement shares — and the harder you beat down the scatter, the more that shared error is all that's left.

In 1840 Struve published again, with 96 measurements instead of 17. His new parallax for Vega was 0.261 arcseconds — twice his first value, and twice the truth. He had measured the gap between Vega and his comparison star two ways: *how far apart* the two stars were, and the *direction* from one to the other. In his early data those two disagreed badly — the direction measurements, taken alone, actually gave a negative parallax — and averaged together, they happened to land almost exactly on the right answer. By 1840 he'd decided the direction measurements were the less trustworthy, and dropped them. A 2020 re-analysis of his data found they weren't less precise at all; it was the separations he kept that were being pulled off by temperature.[^rm]
<!-- REPLY: "two directions" = the two things a micrometer measures about a pair of stars: their separation, and the direction (position angle) from one to the other. R&M fits: separation only 0.252″, direction only −0.225″, combined 0.125″ (1837). 1840 used separations only. Rewritten above; also moved the "why" set-up to the top of the section per your note below. -->

{{< nbas-image src="fig-parallax-race.svg" fullwidth="true"
caption="The race, as it happened. Bars show when each astronomer was observing (approximate); solid diamonds show when each result was announced, and open diamonds the 1840 revisions. Henderson finished observing first and announced last."
alt="Timeline from 1832 to 1841 with three rows. Henderson, Alpha Centauri: observing 1832 to 1833, announced January 1839. Struve, Vega: observing 1835 to 1836, published 1837, revised 1840. Bessel, 61 Cygni: observing 1837 to 1838, announced November 1838, revised 1840." >}}

Bessel revised too. In 1840 he gave 0.348 arcseconds for 61 Cygni — also further from the truth than his first number.[^hog] And it didn't settle quickly. A catalogue compiled in 1889, fifty years after Bessel, listed 55 separate measurements of 61 Cygni's parallax, averaging 0.40 arcseconds — further off than Bessel's very first.[^hog]

<!-- REPLY: done — the set-up paragraph is now at the top of the section. -->

If that sounds familiar, it should. It's Encke's story from the last article: more thorough work, worse answer.

Part of the reason is the ruler itself. Temperature changes the size of a brass telescope and its measuring screws, slightly, between a January night and a July night. No two nights are the same temperature, of course, but on average winter is colder than summer — so the error has a yearly rhythm, rising and falling with the seasons, *just like parallax*. Whatever part of it you haven't corrected ends up in your answer, and more measurements won't average it away, because every measurement shares it. Bessel understood this and published temperature corrections in 1838. The 2020 re-analysis found that the effect in his data was really larger than he'd allowed for: correct it _fully_, and his 61 Cygni result lands almost exactly on the modern value. Struve's Vega data shows the same thing.[^rm]

{{< nbas-image src="fig-61cyg-ruler.svg" fullwidth="true"
caption="61 Cygni's parallax over time. The published values (blue) moved away from the modern one (dashed line). Below: Bessel's 1838 data, measured against each comparison star separately, before (open circle) and after (gold) the 2020 re-analysis corrected fully for temperature. The two corrected values bracket Gaia's."
alt="Dot chart on a scale from 240 to 420 milliarcseconds, with a dashed vertical line at Gaia's 286. Bessel 1838: 314 plus or minus 20. Bessel 1840: 348 plus or minus 14. 1889 average of 55 measurements: 400. Bessel's data against star a: 369 moving to 270 after correction. Against star b: 260 moving to 297." >}}

Thus, precise isn't the same as *accurate*. A pile of measurements can agree with each other but still all be wrong in the same way — and from the ground, there was no way to step outside the pile and check.

<!-- BOOK-INSERT: "The Parallax of the First Three Stars, 1806–2022" — fig-parallax-history + data
     (needs Hopkins 1916 JRASC; the 1849 360.2 mas value — whose?; gaps 1889–2007 etc.). -->

### The Air

Photography changed the pace. In 1903, at Yerkes Observatory, Frank Schlesinger showed that photographic plates, carefully exposed and measured, could do the job: a plate records every star in the field at the same instant, to be measured afterward at leisure. His method stayed essentially unchanged for most of a century.[^perryman]

But it hit a ceiling. The last great ground-based catalogue, published by Yale in 1995, held 8,112 stars, each measured to about 10 *milli*arcseconds — a hundredth of an arcsecond.[^hog2] What that's worth depends on the star. 61 Cygni's parallax is 286 milliarcseconds, so an uncertainty of 10 is small: a few percent. But the farther away a star is, the smaller its parallax — and the uncertainty doesn't shrink with it. A star 30 light-years away has a parallax of about 100 milliarcseconds, so the same 10 is now a 10% uncertainty in its distance. At 300 light-years the parallax is only about 10 milliarcseconds, the same size as the uncertainty, and the measurement can no longer tell you whether the star is 150 light-years away or far beyond. A century and a half of work from the ground had mapped our immediate neighborhood well — out to about 30 light-years — and not much beyond it.
<!-- REPLY: yes, that's exactly the point — rewritten to walk through it with 61 Cyg (286 mas), 30 ly (~100 mas) and 300 ly (~10 mas). The fig-parallax-reach chart right below shows the same thing. --> In friend terms: 10 milliarcseconds is your friend 35,000 kilometers away — about as high as the communications satellites that hang over the equator.

{{< nbas-image src="fig-parallax-reach.svg" fullwidth="true" caption="How far each era could measure a star's distance to within about 10% — which takes a parallax at least ten times its own uncertainty. From the ground, about 33 light-years; Hipparcos, about 330; Gaia, from about 650 light-years for the faintest stars it measures to about 13,000 for well-measured brighter ones. A rule of thumb, worked out from the typical uncertainties quoted in the text. The center of the Milky Way is about 26,700 light-years away." alt="Horizontal bars on a logarithmic distance scale from 1 to 100,000 light-years. From the ground: about 33 light-years. Hipparcos: about 330. Gaia: about 650 for faint stars, extending to about 13,000 for bright stars. Dashed lines mark Proxima, 61 Cygni, Vega, and the center of the Milky Way at about 26,700 light-years." >}}

The remaining layers were the air itself, and the reference stars. The way past both was to leave the Earth entirely.

Hipparcos — the High Precision Parallax Collecting Satellite, a name chosen to echo Hipparchus, the Greek astronomer who made one of the first star catalogues — was launched by the European Space Agency on August 8, 1989. It nearly failed almost immediately. The rocket motor that was supposed to lift it into a circular, high orbit never fired, leaving it stranded in a stretched 10½-hour orbit that dipped through the Van Allen radiation belts twice a day. The mission team rebuilt the operations around the wrong orbit, and Hipparcos observed from November 1989 until radiation damage ended its work in 1993.[^hipp]

It still met its goals anyway. The Hipparcos Catalogue, published in 1997, gave parallaxes for 118,218 stars with typical errors of about one milliarcsecond — ten times better than the best from the ground, for fourteen times as many stars.

One milliarcsecond: that's your friend standing on the Moon. By the same rule as before, it stretched the reach for a 10% distance from about 30 light-years to about 300.
<!-- REPLY: yes — ~330 ly by the 10× rule (1 mas error → 10 mas parallax → 100 pc). -->

{{< nbas-image src="fig-two-fields.svg" fullwidth="true"
caption="How Hipparcos and Gaia measure. Each spun slowly while looking in two directions at once — 58° apart for Hipparcos, 106.5° for Gaia — and measured the large angles between stars along the circle its view swept across the sky. Schematic, not to scale."
alt="Two diagrams of a spinning satellite at the center of a dashed circle representing its path across the sky. Two lines of sight run from the satellite to stars on the circle, 58 degrees apart for Hipparcos and 106.5 degrees apart for Gaia, with a dashed arc marking the angle measured between the two stars." >}}

Leaving the atmosphere was only half of what made Hipparcos different. The other half was the geometry. It looked in two directions at once, 58 degrees apart, combining both views on one detector as the satellite slowly spun. Instead of measuring a star against a faint neighbor a few arcminutes away, it measured angles between stars far apart on the sky, all the way around, over and over.

That's what peeled away the reference layer. Within a small patch of sky, every star's copy of Earth's orbit has the same shape and timing, so if all of them were a little larger, nothing you measure would change. Stars 58 degrees apart have *different* shapes and timing. If all the parallaxes were off by the same amount, the big angles between them would come out wrong, and you'd see it. So Hipparcos didn't need background stars at all. It solved for the parallax of every star at once, and the answers were *absolute* — measured against nothing but geometry.

<!-- BOOK-INSERT: "Why Two Telescopes Make It Absolute" (the uniform-shift argument in depth);
     fig-precision-vs-stars or the "How far could you reach?" table (ground / Hipparcos / Gaia). -->

### The Zero Point - Down to Microarcseconds

ESA's Gaia was launched on December 19, 2013, to a point about a million miles beyond Earth, directly away from the Sun — L2, the same gravitational parking spot as the James Webb Space Telescope (see [Distance at Solar System Scale](/articles/2026/10/distance-at-solar-system-scale/)).
Like Hipparcos, it spun slowly, looking in two directions at once, now 106.5 degrees apart. It observed from 2014 until January 2025, and in March 2025 its controllers switched it off and sent it into a retirement orbit around the Sun.[^gaiaend]

Its third data release, in 2022, gave parallaxes for about 1.47 billion stars.[^dr3] For stars too faint to see with the naked eye but easy in a small telescope, its errors are 20 to 30 *micro*arcseconds — millionths of an arcsecond. That's your friend 14 million kilometers away: more than thirty-five times farther than the Moon. (ESA's own comparison: the width of a human hair, seen from 1,000 kilometers.[^esa])

For 61 Cygni, Gaia's answer is 285.9949 milliarcseconds: 11.404 light-years.[^dr3] Bessel was about 9% short.
<!-- NOTE: Gaia DR4 is due 2 Dec 2026, five days before this publishes. Keeping DR3 (decided). Optional one-liner: "Gaia's fourth data release arrived just as this article was published; the final one is expected around 2030." -->

That leaves one layer — the smallest, and the hardest to see: the *zero*. Gaia's whole method depends on knowing the angle between its two telescopes. If that angle wobbles slightly as the spacecraft spins, in step with the direction of the Sun, the effect is mathematically indistinguishable from every star's parallax being shifted by the same amount. Gaia carries a laser system to monitor the angle, but this one pattern can't be fully calibrated out of the data alone.[^butk]

So astronomers check it against quasars: the brilliant centers of galaxies billions of light-years away. Their true parallax is effectively zero. Whatever Gaia measures for them *is* the error. In Gaia's third release, the quasars come out at about −17 microarcseconds on average — and the offset varies with a star's brightness, color and position on the sky.[^lind]

How can a parallax be negative? Because a parallax isn't read off directly: it's the size of the yearly wobble that best fits the data, and a fit can come out backward. If the measured positions happen to swing the wrong way for the time of year, the best fit is a wobble running *opposite* to Earth's orbit — a negative parallax. (Struve's direction measurements did exactly that.) For any one quasar, random noise nudges the answer a little positive or a little negative. Averaged over an enormous number of them, the noise cancels, and what's left is Gaia's own error: its zero sits about 17 microarcseconds too low. So astronomers correct for it, star by star, with a formula that depends on brightness, color and position.[^lind]
<!-- REPLY: added the paragraph above. -->

For 61 Cygni, that's irrelevant: a few parts in a hundred thousand. For a faint star thousands of light-years away, whose whole parallax is a few dozen microarcseconds, it matters a great deal. It's Bessel's thermometer, 180 years later: something that repeats in step with the Sun, hiding inside the parallax.

{{< nbas-image src="fig-friend-ladder.svg" fullwidth="true" caption="Every angle in this article, as your friend walking away: the distance at which a person 5 feet 7 inches tall would look that small. From a football field for one degree to more than fifty times the Moon's distance for Gaia's zero-point." alt="A ladder of eight points on a logarithmic distance scale. 1 degree: a football field. 1 arcminute: 3.6 miles, the limit of your eye. 1 arcsecond: 218 miles, the blur of the air. 0.29 arcsecond, highlighted: 760 miles, 61 Cygni's parallax. 10 milliarcseconds: 35,000 kilometers, best from the ground. 1 milliarcsecond: the Moon, Hipparcos. 25 microarcseconds: 14 million kilometers, Gaia. 17 microarcseconds: 21 million kilometers, Gaia's zero-point." >}}

<!-- BOOK-INSERT: "The Nearest Star System Still Disagrees" — α Cen modern values 742–751 mas
     (Hipparcos 1997/2007, orbital fits, ALMA). [^acen] -->

## Back to the First Three

There's a small irony at the end of the story of the first three stars. Gaia was built to measure faint stars, and the very brightest are too bright for it. Vega and Alpha Centauri A and B are all beyond its limit.[^dr3] Of the three stars that started it all, only 61 Cygni has a Gaia parallax.

But Alpha Centauri has a faint third member: Proxima Centauri, far too dim to see without a telescope, and the nearest star to the Sun. Gaia measured it: 768.07 milliarcseconds, 4.25 light-years.[^reyle] Gaia couldn't measure Henderson's star — but it measured that star's small companion.

## Wrapup

Three articles in a row now have followed the same shape. The speed of light, the size of the AU and the distance to the stars each began with a rough first number, went backward at least once — Encke, Struve, Bessel's own revision — and converged as instruments improved and as astronomers learned which errors they hadn't been counting.

But something changed this time. In the earlier articles, motion was the *tool*. Rømer timed Jupiter's moons as Earth moved away from them; Bradley measured the speed of light from Earth's velocity; Gill let Earth's rotation carry him across a baseline overnight. Here, one motion is the signal and every other motion is noise — even Earth's own, which shows up twice. Astronomers knew *how* to measure a star's distance from the start. The work was peeling away everything else.

That's the shape of everything still to come in this series. From here on, the methods are known; the hard part is what's hiding inside the measurement.

There's one more difference. The speed of light and the AU each became so well measured that they were turned into definitions: their values are now exact by agreement. Stellar distances can't follow them there. Every star is its own measurement.

And those measurements are the foundation for what comes next. Distances to stars too far for parallax — across the galaxy, and then to other galaxies — are worked out by comparing them with stars whose distances parallax has already given us. Parallax also gave astronomy a unit of its own: a star with a parallax of exactly one arcsecond is at a distance called a *parsec*. Why astronomers kept that unit alongside the light-year is where the next article picks up.

<!-- TRY IT YOURSELF → separate interstitial (phone parallax; walk a circle around the yard watching a
     fencepost against distant hills = the ellipse). Not in this article. -->

## Footnotes

[^perryman]: M. Perryman, "The History of Astrometry," *European Physical Journal H* 37 (2012); arXiv:1209.3563.

[^timberlake]: T. K. Timberlake, "Seeing Earth's Orbit in the Stars: Parallax and Aberration" (2012), Phys. Teach. 51, 478–481 (2013): arXiv:1208.2061; doi:10.1119/1.4824942.

[^williams]: M. Williams, "Beyond the Planets: Early Nineteenth-Century Studies of Double Stars," *British Journal for the History of Science* 17, no. 3 (1984), 295–309; W. Herschel, "Account of the Changes that have happened, during the last Twenty-five Years, in the relative Situation of Double-stars; with an Investigation of the Cause to which they are owing," *Philosophical Transactions of the Royal Society* 93 (1803), 339–382.

[^rm]: M. J. Reid & K. M. Menten, "The First Stellar Parallaxes Revisited," *Astronomische Nachrichten* (2020); arXiv:2009.11913.

[^hend]: Biographical Encyclopedia of Astronomers and Dictionary of Scientific Biography, "Henderson, Thomas" (via MacTutor, St Andrews); B. Warner, "Thomas Henderson and α Centauri," IAU Colloquium 196 (2005).

[^bessel]: F. W. Bessel, "Bestimmung der Entfernung des 61sten Sterns des Schwans," *Astronomische Nachrichten* 16, nos. 365–366 (December 1838), 65–96; doi:10.1002/asna.18390160502. First announced in a letter to Alexander von Humboldt, read to the Paris Academy on 5 November 1838 (*Comptes Rendus* 7, 785–793).

[^acen]: R. Akeson et al., "Precision Millimeter Astrometry of the α Centauri AB System," *Astronomical Journal* 162, 14 (2021): 750.81 ± 0.38 mas.

[^hog]: E. Høg, "Astrometric accuracy during the past 2000 years," arXiv:1707.01020 — Bessel's 1840 value (0.3483″ ± 0.0141″, after Arenou 2008); Oudemans's 1889 compilation.

[^hog2]: E. Høg, "Selected astrometric catalogues," arXiv:1706.08097, Table 3.

[^hipp]: ESA, "Hipparcos overview" and "Launch and Operations Phase" (cosmos.esa.int).

[^gaiaend]: ESA, "Farewell Gaia! Spacecraft operations come to an end," 27 March 2025.

[^dr3]: ESA, Gaia Data Release 3 contents summary (bright limit about G ≈ 3); L. Lindegren et al., "Gaia Early Data Release 3: The astrometric solution," *Astronomy & Astrophysics* 649, A2 (2021); arXiv:2012.03380.

[^esa]: ESA, "Cosmic distances" (Gaia).

[^reyle]: C. Reylé et al., "The 10 parsec sample in the Gaia era," *Astronomy & Astrophysics* (2021); arXiv:2104.14972 (Gaia EDR3 value).

[^butk]: A. G. Butkevich et al., "Impact of basic angle variations on the parallax zero point for a scanning astrometric satellite," *Astronomy & Astrophysics* 603, A45 (2017).

[^lind]: L. Lindegren et al., "Gaia Early Data Release 3: Parallax bias versus magnitude, colour, and position," *Astronomy & Astrophysics* 649, A4 (2021).

[^stellarium]: Star fields rendered with Stellarium (stellarium.org); Stellarium contributors, Stellarium v26.2 (2026), doi:10.5281/zenodo.23020615; G. Zotti et al., "The Simulated Sky: Stellarium for Cultural Astronomy Research," *Journal of Skyscape Archaeology* 6(2), 221–258 (2021), doi:10.1558/jsa.17822.
