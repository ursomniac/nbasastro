---
title: "Smart Scope Holiday Present? What Now?"
date: 2026-12-24
description: "Unwrapped a smart telescope? What it can really show you, from planets and comets to quasars and supernovae, and how a little effort turns pretty pictures into real observing."
byline: "From pretty pictures to real observing: what a little effort buys you"
series: ["smart-scopes"]
authors: ["bob-donahue"]
thumbnail: "thumbnail.jpg"
banner: "banner.png"

# Tag only objects the text discusses (Bob's call). sso_* key names: Bob to fill.
dso_messier: ["101"]
dso_other: ["PG 1634+706", "Q0957+561"]
---
<!-- v3 (2026-10-27): Bob's v2 + editorial/fact pass. [TK] = unverified or missing; fill before publishing.
     Links marked [TK link] = page exists on the site, URL needed (no forward links). -->

## Introduction

{{< nbas-image src="banner.png" fullwidth="true"
caption="[TK caption]"
alt="[TK alt]" >}}

So someone gave you a smart telescope.  Or you gave yourself one.

Well, first congratulations!   Smart scopes are the 21st-century way of observing, and
while they can't replace traditional optical scopes (there's something visceral about
seeing Saturn through an eyepiece) they _do_ offer beginners (and even seasoned amateurs)
an exciting view of the cosmos.  Moreover, they're a great introduction to the world of
digital astrophotography, and once you understand their limitations, it's really quite
amazing what these little scopes *can* do.

The app you use to control the scope and the camera will have lots of suggestions of "what
to observe" and it'll pick from what seems to be everyone's "Top 100".  But there's
a lot more than the app's target list suggests. That list is the front
door, and it's a good one. Behind it is everything else in the sky, much of it changing from
night to night: comets, asteroids, supernovae in other galaxies, variable stars, even planets
around other stars. A smart scope can reach a surprising amount of it. A century ago, some of those things
would have needed a professional observatory.

It helps to know going in what to expect. Your images will not look like Hubble's or Webb's,
and some targets that sound exciting will look like a smudge or a dot. That isn't failure.
Often just seeing the dot *is* the remarkable part, once you know what it is. This article is a tour of
what these scopes do well, what they don't, and what a little effort buys you.

### What Your Scope Actually Sees

Except for a few cases, you don't "look" through a smart scope -- there's no eyepiece.
What you have is your phone or tablet and an app that controls the telescope and camera.

A few numbers explain most of what you'll see, good and bad. The most useful is the **plate
scale**: how much sky lands on one pixel, in arcseconds. 
It comes straight from two specifications, the pixel size and the focal
length, and it decides how much detail a scope can record on small targets.

| Scope | Aperture | Focal length | Image (px) | Plate scale | Field of view | Jupiter across |
|---|---|---|---|---|---|---|
| Seestar S30 Pro | 30 mm | 160 mm | 3840 × 2160 | 3.7″/px | 4.0° × 2.2° | ~12 px |
| Dwarf Mini | 30 mm | 150 mm | 1920 × 1080 | 4.0″/px | 2.1° × 1.2° | ~11 px |
| Seestar S50 Pro | 50 mm | 260 mm | 3840 × 2160 | 2.3″/px | 2.4° × 1.4° | ~20 px |
| Vaonis Vespera 3 | 50 mm | 245 mm | 3840 × 2160 | 2.4″/px | 2.6° × 1.5° | ~18 px |
| Vaonis Vespera Pro 2 | 50 mm | 245 mm | 3536 × 3536 | 1.7″/px | 1.6° × 1.6° | ~27 px |
| Dwarf Draco | 90 mm | 340 mm | 4096 × 3072 | 1.5″/px | 1.7° × 1.2° | ~31 px |
| Unistellar eQuinox 2 | 114 mm | 450 mm | 2048 × 1536 | 1.3″/px | 45′ × 34′ | ~34 px |
| Celestron Origin Mk II | 152 mm | 335 mm | 3856 × 2180 | 1.2″/px | 1.3° × 0.75° | ~37 px |

<!-- Table notes (computed from published pixel sizes and focal lengths; plate scale =
     206.265 × pixel µm / focal length mm). eQuinox 2 values measured from Bob's own files.
     Jupiter at 45″ [verify]. Replace retailer/review sources with manufacturer pages. -->

Remembering your high-school geometry, an arcsecond is 1/3600 of a degree.
As a comparison, the Moon (and the Sun) are about &frac12;° across (or 1800 arcseconds).
Jupiter near opposition is only 45";  Saturn and Mars are even smaller.   Most of the 
deep-sky objects you'll be imaging are several arcminutes across.

Two things jump out. The fields of view are wide, several times the full Moon for the smaller
scopes, which is why they're so good at big nebulae and star clusters. 
And it's also why Jupiter covers only a dozen to a few dozen pixels. Keep that in mind for the next section.

Many of the images in this article come from the original Seestar S30 (150 mm focal length,
4.0″ per pixel) and S50 (250 mm, 2.4″ per pixel), the models these replaced. Each caption
says which scope took it.

---

## Things To Observe: Solar System Objects

### Planets (and Dwarf Planets)

Let's get the disappointment out of the way first. Planets are the one place where a smart scope
does worse than a modest traditional telescope. A small traditional refractor at 100× will
often show Saturn's rings far more crisply than the smaller scopes in the table above.

The reason is in the table. These instruments are built for things that are big and faint:
short focal lengths, wide fields, and long stacks of exposures that pile up light. Planets are
the opposite: small and bright. They need a _long_ focal length and a camera that shoots video
fast enough to catch the brief moments when the air is steady. Jupiter at its biggest spans
about 45 arcseconds, and on a 2.3″-per-pixel sensor that's about 20 pixels across. You'll see
the belts and the four big moons, and not much more.

This is getting better. Some newer scopes have planetary modes, and a few read their sensors at
full resolution for bright targets: the Dwarf Draco's native mode roughly triples Jupiter's
size compared with a Seestar S50 Pro. The Unistellar scopes do a digital blowup to _try_ to
capture planets, and given their limitations, they do *OK*. 
But if planets are your main interest, a smart scope isn't the right tool for the job, and that's fine.

### But It's Not *All* Bad News!

That's not to say you can't have fun with _some_ planets!

{{< nbas-gallery style="carousel" size="300px" title="Outer planets and their moons" >}}
{{< /nbas-gallery >}}

Uranus and Neptune are a different story. They're only a few arcseconds across, so at
smart-scope plate scales they look like bright stars, and a smart scope captures their color nicely: the pale blue-green of Uranus, the
deeper blue of Neptune.   What's very interesting is that you can capture their moons readily
(if the sky is cooperative and there's decent seeing).

### And Even Further Out!

Then there are the dwarf planets, and this is where a smart scope oddly starts to shine.

[Pluto](/articles/2026/08/smart-scope-challenge-pluto/) is a fun first target: a faint dot that moves against the stars from night to
night.  In any smart scope -- once you've looked up its coordinates at the [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/)<!-- verify URL -->
site -- Pluto can be tracked down in just a few minutes.   Come back a few days later and you can
see that it has moved against the background stars (exactly in the same way it was first discovered
by Clyde Tombaugh in 1930).  

That's worth a moment. Tombaugh's Pluto was a
15th-magnitude speck on glass plates from Lowell Observatory's 13-inch telescope, each plate
exposed for about an hour. The difference isn't the optics. A photographic plate
recorded seldom more than 1% of the light that fell on it. A modern camera sensor records most
of it [TK: QE figure from a manufacturer data sheet], and the scope can stack hundreds of
exposures into one image. Your gift is, in that one respect, better equipped than the
observatory that found Pluto.

{{< clear >}}
{{< nbas-image src="pluto-230812-9m.png" width="380" align="right" caption="Pluto - 12 Aug 2023" >}}
{{< nbas-image src="pluto-230810-9m.png" width="380" align="right" caption="Pluto - 10 Aug 2023" >}}
{{< clear >}}

In the two images above, can you spot Pluto?

Pluto is currently in Capricornus, so for the next several years, 
it'll be a late Summer target -- but definitely put it on your "To Do" list! 

### But why stop there?

{{< nbas-image src="makemake-equ-27m-annotated.jpg" width="380" align="right" caption="Makemake, eQuinox 2, 27 min" >}}
{{< nbas-image src="haumea-equ-23m-annotated.jpg" width="380" align="right" caption="Haumea, eQuinox 2, 23 min" >}}
{{< clear >}}

[Haumea and Makemake](/articles/2026/05/smart-scope-challenge-haumea-and-makemake/) are a step harder, 
around magnitude 17 (Haumea is about 17.3).  But that just means a longer exposure (though getting close 
to the workable limit for the smallest smart scopes -- still worth the
challenge, however).   The same principle applies: images taken a few days apart will show their motion.
When you consider that both were only discovered ~20 years ago, and now they're within reach of 
amateur imaging that's remarkable.  Haumea is in Boötes, about 6° from Arcturus, and Makemake is next door in Coma Berenices,
so they make a great spring challenge you can try once you've gotten the hang of the scope and the app.

(Each app has a way to enter in coordinates manually - you'll have to consult your app's documentation
for the particulars.)

[Eris](/articles/2026/10/whats-up-outer-planets/), at magnitude 18.7, is the real challenge.   It's _still_ on my own "To Do" list,
though I have seen postings online where others have managed to do it.

Of course none of these objects are going to look like anything other than a faint star.  So, in terms
of "beautiful" imagery, they don't offer a lot.   The fun here is the chase: peering out to the outer
Solar System, and capturing a distant world.

### The Moon and Sun

{{< nbas-image src="2024-04-08-ingress.jpg" width="380" align="right"
caption="Ingress of the April 2024 eclipse from West Glover VT, Bob Donahue, NBAS, Seestar S50, showing sunspots." >}}
{{< nbas-image src="gareth-moon-261010.jpg" width="360" align="right"
caption="Gibbous Moon, Gareth Williams, NBAS, Seestar S30" >}}
{{< clear >}}

The Moon is an easy, satisfying target: big, bright, and full of detail along the line
between day and night. 

{{< nbas-image src="2024-04-08-152819-Solar_thn.jpg" width="350" align="right"
caption="Totality of the April 2024 eclipse from West Glover VT, Bob Donahue, NBAS, Seestar S50" >}}
The Sun is satisfying too, with sunspots that change from day to day, but it comes with a
rule that has no exceptions: **fit the solar filter before the scope points anywhere near the
Sun.** Use the filter that came with your scope, or the one its maker specifies, and **NOTHING
ELSE**. Unfiltered sunlight through any telescope can destroy the camera and, if anyone looks
through an eyepiece, an eye.  Seestars come with a solar filter made for each model: push-fit on the S50, magnetic on
the S30 and S30 Pro. <!-- verify S50 Pro; other brands vary -->

Now - one thing that Seestar users complain about is that even though you'd think that the 
two brightest and largest objects in the sky would be easy to find, that the scope frequently
can't find them!   For the Moon - here's the trick: once you're all powered up and ready to go,
*first* send the scope to find a star or bright deep sky object.  *Then* send it to the Moon.
(For the Sun you basically try to get it lined up in azimuth, attempt finding the Sun, then 
manually slew the scope using the background to find the Sun.)

### Comets

{{< nbas-image src="c2023_a3-s50-4m-full-rotated.jpg" 
caption="C/2023 A3 Tsuchinshan/ATLAS, Seestar S50, 4 min" >}}


A comet is one of the most exciting things you can catch, and also one of the most likely to
look grainy. There are two reasons. A comet's glow is spread out and faint, so it needs a lot
of exposure time. But it's also moving against the stars, more so when it's closer to the Sun. 
Stack the frames to keep the stars sharp, and the comet smears (it'll look like a line); stack them 
on the comet, and the stars turn into streaks.  If the comet is bright, try to keep the total 
integration time to a few minutes.  Some apps do have a "comet stacking mode" which gives you more leeway.
Either way, a faint, fuzzy comet with a hint of tail is a real result. Few of them ever get 
bright, and every one is a visitor that won't look the same next week.

Most comets you can reach won't be in your app's list. The best place to find out what's up is
Seiichi Yoshida's [Weekly Information about Bright Comets](TK verify URL: aerith.net), which
lists every comet within amateur reach with its brightness and a finder chart. Most smart
scopes let you enter coordinates directly. [TK: verify per app.]

What you might find surprising is that there are usually a few comets around on any given night.
With a smart scope you don't have to wait months or years for a really bright one:  even fainter
comets are now within your grasp!

{{< nbas-gallery style="grid" size="300px" title="A Few Comets" >}}
c_62p-equ-8m-square.jpg | 62P/Tsuchinshan | eQuinox 2, 8 min
13P_Olbers-equ-16m-square.jpg | 13P/Olbers | eQuinox 2, 15 min
{{< /nbas-gallery >}}

### Asteroids

Point a smart scope anywhere near the ecliptic, the path the planets follow across the sky, and
there's a good chance an asteroid is in the frame. You won't notice it in a single image. You
might notice it in a time-lapse, as a "star" that moves.

{{< nbas-gallery style="carousel" size="300px" title="Asteroids" >}}
6_hebe-equ-8m-annotated.jpg | 6 Hebe | eQuinox 2, 8 min
m_44-s30-36m-annotated-rotated_D2QwfLa.jpg | 135 Hertha photobombs Praesepe! | Seestar S30, 36 min
ngc_6583-equ-15m.jpg | 980 Anacostia photobombs NGC 6583 | eQuinox 2 | 15 min
{{< /nbas-gallery >}}

These photobombers are worth tracking down, because they turn a pretty picture into a
measurement: every frame records where the asteroid was at a known time. The Minor Planet
Center's [MPChecker](https://minorplanetcenter.org/cgi-bin/checkmp.cgi) will list every known
asteroid in your field: give it the date and time of your image, the coordinates of the
center, and a search radius. Two minutes, and your mystery dot has a name.

You can also go after asteroids on purpose. The four first ones found, Ceres, Pallas, Juno
and Vesta, are easy smart-scope targets, especially at opposition, and their story is 
in [Eleven Planets: The First Asteroids](/articles/2026/12/eleven-planets-the-first-asteroids/). 
Image one a few hours or days apart, and you can watch it move.

(And see below for more "Fun with Asteroids".)

---

## Things To Observe: Deep Sky Objects

This is what smart scopes do best. The galleries below are a sample of what's possible with no
special equipment, from a backyard in the Berkshires. They're not tied to the season: some of
these objects are up on a winter evening, others you'll meet over the coming year.

### Nebulae (of all kinds)

Nebulae come in several kinds, and a smart scope captures them all. Emission nebulae glow
red from hydrogen lit up by hot young stars. Reflection nebulae shine blue with borrowed
starlight. Planetary nebulae are shells of gas thrown off by dying stars, often small and
colorful. Dark nebulae are clouds of dust that show up only as holes against a starry
background.

{{< nbas-gallery style="carousel" size="300px" title="Nebulae Smart Scope Images" >}}
b_84-w50-80m.jpg | Dark Nebula Barnard 84 | Seestar S50, 80 min
c_4-equ2-140m.jpg | Iris Nebula | eQuinox 2, 140 min
c_63-equ-48m.jpg | Helix Nebula | eQuinox 2, 48 min
ic_1795-s50-35m-LP.jpg | Fish Head Nebula | Seestar S50, 35 min
m_20-s50-62m.jpg | Trifid Nebula | Seestar S50, 62 min
m_27-equ-31m.jpg | Dumbbell Nebula | eQuinox 2, 31 min
c_27-s30-112m-LP.jpg | Crescent Nebula | Seestar S30, 112 min
c_22-equ-18m.jpg | Blue Snowball | eQuinox 2, 18 min
{{< /nbas-gallery >}}

Your smart scope might have a built-in filter.  Typically these are dual-passband
filters centered on specific spectral lines:  Hydrogen in the red (H&alpha; at 656 nm) and 
Oxygen in the bluish-green part of the spectrum  ([O III] at 501 nm). Here's where they 
are useful:

- Emission nebulae emit _mostly_ in hydrogen
- Many planetary nebulae emit in hydrogen and oxygen

So, if you're going to look at the Eagle Nebula in Serpens, or the Lagoon in Sagittarius,
etc., using the filter brings out more detail.   Similarly, the Ring Nebula, or the Dumbbell,
will show up more using the filter.

The same filter has a bonus: moonlight and light pollution are spread across the whole
spectrum, so a filter that passes only those two narrow colors blocks most of them and keeps
most of the nebula. A full Moon, like the one over Christmas week, doesn't have to end your
observing. It just changes what you point at.

Another thing about planetary nebulae: aside from a few cases (the Ring Nebula in Lyra or
the Dumbbell in Vulpecula) most are either very small or large but very faint.  For setups
with large FOV and "fat" pixel sizes, you might not see much if the size is smaller than
a couple of arcminutes (there are tricks you can do in post-processing that'll help).  For
the large faint ones (like the Helix in Aquarius, but other less-famous ones as well), expose
as long as you can, and hope for the best.

### Star Clusters

Open clusters are loose groups of young stars, born together and slowly drifting apart.
Globular clusters are ancient balls of hundreds of thousands of stars orbiting in the halo of
our Galaxy. In a smart scope, the difference is obvious at a glance.

<!-- GALLERY (clusters): M 11, M 92 (link TK), C 14, M 75. -->
{{< nbas-gallery style="carousel" size="300px" title="Open and Globular Clusters" >}}
c_14-s30-65m.jpg | Double Cluster (Perseus) | Seestar S30, 65 min
m_92-equ-16m.jpg | Messier 92 (Hercules) | eQuinox 2, 16 min
m_37-s50-8m.jpg | Salt &amp; Pepper Cluster (M 37, Auriga) | Seestar S50, 8 min
m_55-equ-13m.jpg | Messier 55 (Sagittarius) | eQuinox 2, 13 min
m_67-s30-17m-square.jpg | Goldeneye Cluster (M 67, Cancer) | Seestar S30, 17 min
ngc_5466-s50-26m.jpg | NGC 5466 (Boötes) | Seestar S50, 26 min
{{< /nbas-gallery >}}

One of the things you might notice comparing eyepiece impression of clusters with your images,
is how much more color shows up: our eyes are _terrible_ cameras, and our dark adaptation really
centers on light sensitivity, not color sensitivity.

Open clusters mostly are bright and large and you'll see structure in a few minutes.
Globulars are a little tougher in that they have many faint stars, but the central concentration
can become a little over-exposed.  There's usually a good medium which you'll see as you go along.


### Galaxies

Galaxies are where expectations need the most adjusting, and where patience pays the most.
Most are small and faint, so a few minutes give you a smudge. An hour or more, stacked, and
spiral arms, dust lanes and star-forming regions start to appear. The galleries show a range of
types: spirals seen face-on and edge-on, ellipticals, and irregulars. [TK: match to Bob's
selection.]

{{< nbas-gallery style="carousel" size="300px" title="Galaxy Smart Scope Images" >}}
c_57-equ-27m.jpg | Barnard's Galaxy (Sagittarius) | eQuinox 2, 27 min
c_44-equ-42m.jpg | Superman Galaxy (Pegasus) | eQuinox 2, 42 min
m_51-s30-54m.jpg | Whirlpool Galaxy (Canes Venatici) | Seestar S30, 54 min
m_74-s50-61m.jpg | Phantom Galaxy (Pisces) | Seestar S50, 61 min
ngc_4565-s30-92m.jpg | Flying Saucer Galaxy (Coma Berenices) | Seestar S30, 92 min
ngc_4302-s50-97m.jpg | NGC 4298 and 4302 (Coma Berenices) | Seestar S50, 97 min
ngc_4656-equ-31m.jpg | Crowbar Galaxy (Canes Venatici) | eQuinox 2, 31 min
{{< /nbas-gallery >}}

### Quasars and Other Exotic Objects

Here's a target that will look like nothing at all, and that's the point.

{{< nbas-image src="pg_1634706-92U-8m-square.jpg" width="420" align="right"
caption="PG 1634+706, eQuinox 2, 8 min. The quasar is the faint star at [TK position]. Its light left about 9 billion years ago."
alt="[TK alt]" >}}

PG 1634+706, in the constellation Draco just below the bowl of the Little Dipper, is a
quasar: the blazing core of a galaxy, powered by matter falling into a supermassive black
hole. It shines at about magnitude 14.5, varying a little as the rate of infall changes. In
your image, it's one faint star among many. But its light left it about 9 billion years ago,
when the universe was about a third of its present age. Visual observers need an 8- to
12-inch telescope and a dark sky to glimpse it. A smart scope records it in minutes. It's
likely the most distant thing you'll ever photograph, and it sits in a part of the sky that
never sets from here.

For a harder challenge, try the Twin Quasar (Q0957+561) in Ursa Major: one quasar seen twice,
because a giant galaxy between us and it bends its light into two images 6 arcseconds apart.
The two images are magnitude 16.5 and 16.7. Whether you can split them depends on your plate
scale. At 2.3″ per pixel they're less than three pixels apart and blend together; at about
1.3″ per pixel they're four or five pixels apart, and on a steady night they can separate.

{{< clear >}}

---

## How Long Should I Expose?

This doesn't have a straightforward answer.   When I started, I wanted to see *EVERYTHING*,
and was very impatient, stopping after a few minutes, maybe 20-30 minutes if I were more
patient.  But then I started to see other people's images taken over successive nights
exposing for *hours* and I was jealous.  (This is why I have four smart scopes now - they
keep me busy, but I am able to get longer exposures.)

Many scopes have a "plan" mode - you can schedule what you want to look at and when.
Set it up for the night, and walk away, spending as much time as you want without 
babysitting it.  

---

## Citizen Science!

Everything so far is for your own enjoyment, and that's reason enough. But a smart scope can
also contribute real data to real science. I'll be honest: I haven't done most of what
follows yet. These are doors I know are open, not ones I've walked through, and each section
says what it takes, whether a smart scope can do it, and who wants the results.

(My "To Do" list never empties!  Once you get hooked, there's *always* another cool object,
or challenge, or going back to get a deeper stack on something.)

### Comet Monitoring

Comets change, sometimes suddenly, and observers who record their brightness over weeks
build a picture professionals use. [TK: COBS — what it accepts (visual/CCD magnitudes), URL;
whether smart-scope photometry qualifies.] The same aerith.net pages that tell you what's up
are a good starting point.

### Asteroid Occultations

When an asteroid passes in front of a star, the star blinks out for a few seconds, but only
along a narrow track on the ground. Observers spread across the track record the timing, and
together they measure the asteroid's size and shape, sometimes discovering moons. I tried this
once and saw nothing; that's common, and a "miss" outside the track is still useful data.

Predictions for your location come from the International Occultation Timing Association's
[OccultWatcher](https://cloud.occultwatcher.net/), which draws on the predictions posted at
[asteroidoccultation.com](http://www.asteroidoccultation.com/). Unistellar runs its own program
for its scopes. [TK: what a non-Unistellar smart scope needs for timing — video mode, accurate
time stamps.]

### Variable Stars

Thousands of stars change in brightness, some in hours, some over years, and the American
Association of Variable Star Observers ([AAVSO](https://www.aavso.org/)) has been collecting
amateur measurements for over a century. The latest software release for Seestars includes a variable-star mode.
[TK: Seestar's mode — what it does; borrowed light curve with permission.] We'll come back to
this in more depth in a future article.

### Supernova Monitoring

{{< nbas-image src="m_101-sn-equ-20m.jpeg" width="380" align="right"
caption="SN 2023ixf in M 101, eQuinox 2, 20 min" 
alt="[TK alt]" >}}
{{< nbas-image src="c_30SN2025rbs-equ-36m.jpg" width="380" align="right"
caption="NGC 7331 with SN 2025rbs, eQuinox 2, 36 min" 
alt="[TK alt]" >}}

Every so often a star in another galaxy explodes, and for a few weeks it can outshine
billions of its neighbors. Bright supernovae (magnitude 12 to 14) turn up several times a
year [TK: verify frequency], and the [Latest Supernovae](TK verify URL) page lists current
ones with finder charts. An image of the host galaxy before and after is one of the most
striking results a smart scope can produce. 

In May 2023, Japanese amateur Koichi Itagaki discovered a supernova in M 101, the Pinwheel
Galaxy, about 21 million light-years away: SN 2023ixf, the closest supernova in nine years.
It was a Type II, the collapse of a massive star, and it peaked around magnitude 10.8, easily
within reach of a smart scope.

<!-- NOTE: get light curve of 2023ixf with Unistellar observations -->

Here's where the story gets interesting. M 101 is a favorite target: bright, easy to find,
and, well, pretty. Some Unistellar owners had imaged it just for enjoyment in the hours
before anyone knew there was a supernova, and their pictures caught it. The earliest came
within about five hours of the first known detection of the explosion. Catching a supernova
that early is extremely hard, because nobody knows when or where the next one will go off.
In all, 115 Unistellar telescopes contributed 252 observations to a light curve published in
a research journal, and "pretty pictures" became data for testing models of how massive stars
explode.

{{< clear >}}

### Even Exoplanets!

In September 1999, a Harvard graduate student named David Charbonneau watched the star
HD 209458 dim slightly, twice, a week apart. It was the first time anyone had seen a planet
cross in front of another star. The telescope was STARE, with a 10-centimeter lens: about
twice the aperture of a Seestar S50.

HD 209458 is a 7.65-magnitude star in Pegasus, and its planet still crosses every 3.52 days,
dimming it by about 1.5% for a little over three hours. That's a small signal, but well-made
measurements from small telescopes catch it routinely. The Czech Astronomical Society's
[Exoplanet Transit Database](https://var.astro.cz/en/Exoplanets/31) collects amateur transit
light curves, and Unistellar's network runs an exoplanet program. [TK: has anyone done this
with a Seestar/Dwarf? Borrowed light curve with permission.]

### Capturing the ISS

[TK: Bob hasn't done this. Verify which scopes, if any, can track satellites; otherwise frame
as a solar or lunar transit of the ISS, timed from a prediction site (verify name/URL).
Borrowed image with permission.]

---

## Some Tips

The manual will tell you how to run your scope. These are the things it won't.

- **Be patient.** Integration time is the single biggest difference between a disappointing
  image and a good one. If a target looks thin after ten minutes, give it an hour, or come
  back another night and add to it.
- **Always save your raw data.** The picture the app gives you is one rendition that it 
  tries to generate on the fly, using the meager computing power and memory of your device.
  So grabbing all of the individual frames allows you to improve upon your image through
  *post-processing* using software like Siril (free) or PixInsight (not free, but very good).
  You'll need copious disk space - each frame is a few MB, but they'll add up quickly to GB
  even over one night.  So invest in SSD drives (4 TB will last several months).
- **Back it up.** Keep a second copy on a separate drive.  You don't want a failure to cause
  you to lose months of hard work.
- **Get into post-processing when you're ready, not before.** The app's results are a fine
  place to start, and when you want to learn the art of post-processing all those nights
  will be there for you to re-explore!  (Plus what else are cloudy nights good for?)   There
  are more and more guides, videos, etc. to help you get started -- dedicated astrophotographers
  are always developing better tools, and some really specialized ones for certain types of
  objects.
- **Have fun.** You're not on a schedule, and the sky will be there tomorrow.


---

## Wrapup

A smart scope is a remarkably capable instrument. It won't make Hubble pictures, and it won't
show planets the way a traditional telescope does. What it will do is let you collect light
from a comet that may never come back, an asteroid you didn't expect to be there, a star that exploded
in another galaxy, or a quasar whose light set out before the Earth existed, not to mention
all the amazing images of nebulae, clusters, and galaxies.  With a little effort, it can even 
contribute data to real research.

When you're ready for a goal, keep an eye out for one of our [observing challenges](TK link); several are
written for smart scopes and appear throughout the year. And bring what you capture to an NBAS meeting, 
or share it on [Members' Skies](TK link) or our Facebook page.  We'd love to see it.

Clear skies.
