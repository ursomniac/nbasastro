---
title: "Bright Winter Stars"
date: 2027-01-19
series: ["astronomy-quiz"]
knowledgetopics: ["quizzes"]
level: "intermediate"
description: "Twelve questions on winter's brightest stars: why Canopus never rises here, what's hiding inside Castor and Capella, how Procyon got its name, and more."
byline: "Test your knowledge on some of winter's brightest stars!"
banner: "banner.webp"
thumbnail: "thumbnail.webp"
quiz:
  renderer: "text-choice"
  passing_score: 70
  questions:

    # Q1 — Canopus never rises from here (4 options) — correct at position 3
    - id: 1
      image: "fig-canopus-meridian.webp"
      text: >-
        Which bright star never rises above the horizon as seen from North
        Adams (about 42.7° N)?
      answers:
        - text: >-
            Rigel
          correct: false
          explanation: >-
            Rigel is about 8° south of the celestial equator. From here it
            climbs to about 39° above the southern horizon.
        - text: >-
            Adhara
          correct: false
          explanation: >-
            Adhara stays low, but it still reaches about 18° above our
            southern horizon.
        - text: >-
            Canopus
          correct: true
          explanation: >-
            Canopus sits at declination −52.7°, so even at its highest it is
            about 5° below our southern horizon. You have to be south of
            about 37° N to see it.
        - text: >-
            Sirius
          correct: false
          explanation: >-
            Sirius gets about 30° up at its highest — low, but easy to see.

    # Q2 — Castor is six stars (3 options) — correct at position 2
    - id: 2
      image: "fig-castor-naked-eye.webp"
      text: >-
        To the naked eye, Castor looks like a single star. How many stars
        is it really?
      answers:
        - text: >-
            Two: a close pair that a small telescope can split.
          correct: false
          explanation: >-
            That's only the first layer. Each star in that pair is itself a
            close pair.
        - text: >-
            Six: three pairs, all bound together.
          correct: true
          explanation: >-
            Castor A and B are each spectroscopic binaries, and faint
            Castor C, a pair of red dwarfs, orbits them all.
        - text: >-
            One star, surrounded by a dust shell that makes it look double.
          correct: false
          explanation: >-
            Castor's companions are real stars, measured in orbit around
            each other.

    # Q3 — "Before the dog" (4 options) — correct at position 4
    - id: 3
      image: "fig-two-dogs.webp"
      text: >-
        Which winter star's name means "before the dog"?
      answers:
        - text: >-
            Sirius
          correct: false
          explanation: >-
            Sirius is the dog — the Dog Star itself. Its name comes from
            Greek for "scorching" or "glowing."
        - text: >-
            Mirzam
          correct: false
          explanation: >-
            Mirzam does rise a little before Sirius from here, and its
            Arabic name is traditionally translated "the herald" — but the
            name means something else.
        - text: >-
            Adhara
          correct: false
          explanation: >-
            Adhara comes from Arabic for "the virgins," a name once shared
            by several Canis Major stars.
        - text: >-
            Procyon
          correct: true
          explanation: >-
            From Greek "pro" (before) + "kyon" (dog). From here Procyon
            rises about half an hour before Sirius; south of about 30° N,
            Sirius rises first.

    # Q4 — Epsilon Aurigae's eclipses (3 options) — correct at position 3
    - id: 4
      image: "fig-eps-aur-eclipses.webp"
      text: >-
        Every 27 years, Epsilon Aurigae, near Capella, fades from about
        magnitude 3.0 to 3.8 and stays dim for nearly two years. What passes
        in front of it?
      answers:
        - text: >-
            A giant planet orbiting the star.
          correct: false
          explanation: >-
            Even a giant planet is far too small to block about half of a
            supergiant's light.
        - text: >-
            A dark interstellar cloud drifting through our line of sight.
          correct: false
          explanation: >-
            The fading repeats every 27 years, so the culprit is in orbit,
            not drifting past.
        - text: >-
            A huge, dark disk of dust around a hidden companion star.
          correct: true
          explanation: >-
            Interferometers imaged the disk crossing the star during the
            2009–2011 eclipse. The next one is due around 2036.

    # Q5 — Capella is almost circumpolar (3 options) — correct at position 1
    - id: 5
      image: "fig-capella-overhead.webp"
      text: >-
        From North Adams, Capella seems to be up all night long in winter.
        Is it circumpolar here — always above the horizon?
      answers:
        - text: >-
            Almost, but not quite: it dips just below the northern horizon
            for roughly two hours a day.
          correct: true
          explanation: >-
            Circumpolar here takes a declination above +47.3°. Capella's is
            +46.0°, so it sinks about 1.3° below a flat northern horizon.
        - text: >-
            Yes — every star north of the celestial equator is circumpolar.
          correct: false
          explanation: >-
            Only stars within 42.7° of the celestial pole (our latitude)
            never set. Most northern stars still rise and set.
        - text: >-
            No — like Orion, it's below the horizon about half of every day.
          correct: false
          explanation: >-
            Only stars near the celestial equator spend about half their
            time below the horizon. Capella is far north of it.

    # Q6 — Why Castor is alpha (3 options) — correct at position 2
    - id: 6
      image: "fig-gemini-bayer.webp"
      text: >-
        Pollux is the brightest star in Gemini, yet it's Beta (β) Geminorum,
        while slightly fainter Castor is Alpha (α). Why?
      answers:
        - text: >-
            The Greek letters rank stars by distance, nearest first.
          correct: false
          explanation: >-
            Pollux is the nearer of the two: about 34 light-years, versus
            about 51 for Castor.
        - text: >-
            Johann Bayer's letters (1603) weren't a strict brightness
            ranking. Within a rough brightness class, he used other orders.
          correct: true
          explanation: >-
            Bayer sometimes lettered by position or rising order. Castor
            rises first, and it's named first in "Castor and Pollux."
        - text: >-
            Astronomers re-lettered Gemini's stars in 1930, when the
            constellation boundaries became official.
          correct: false
          explanation: >-
            The 1930 boundaries kept Bayer's letters. Nobody re-lettered
            stars by brightness.

    # Q7 — Sirius B predicted before seen (4 options) — correct at position 1
    - id: 7
      image: "fig-sirius-b-orbit.webp"
      text: >-
        Sirius has a faint companion, the white dwarf Sirius B. How did
        astronomers first learn it was there?
      answers:
        - text: >-
            In 1844, Friedrich Bessel noticed Sirius wobbling as it moved
            across the sky and deduced an unseen companion.
          correct: true
          explanation: >-
            Nobody saw it until 1862, when Alvan Graham Clark tested a new
            18.5-inch telescope lens on Sirius.
        - text: >-
            Galileo spotted it with his first telescope in 1610.
          correct: false
          explanation: >-
            Sirius B hides in Sirius's glare. It wasn't seen until 1862.
        - text: >-
            An X-ray satellite picked up its hot surface.
          correct: false
          explanation: >-
            Sirius B was known about a century before X-ray astronomy began
            in the 1960s.
        - text: >-
            It passed in front of Sirius and dimmed it.
          correct: false
          explanation: >-
            We don't see the orbit edge-on, so Sirius B never eclipses
            Sirius.

    # Q8 — Winter Hexagon (4 options) — correct at position 2
    - id: 8
      image: "fig-winter-bright.webp"
      text: >-
        The Winter Hexagon links six of the season's brightest stars. Which
        bright star sits inside it, rather than on it?
      answers:
        - text: >-
            Pollux
          correct: false
          explanation: >-
            Pollux is a corner of the Hexagon (some versions use Castor
            alongside it).
        - text: >-
            Betelgeuse
          correct: true
          explanation: >-
            Betelgeuse sits near the middle. With Sirius and Procyon it
            forms a different pattern, the Winter Triangle.
        - text: >-
            Capella
          correct: false
          explanation: >-
            Capella is the Hexagon's northernmost corner.
        - text: >-
            Procyon
          correct: false
          explanation: >-
            Procyon is a corner of both the Hexagon and the Winter Triangle.

    # Q9 — Mintaka rises due east (4 options) — correct at position 4
    - id: 9
      image: "fig-orion.webp"
      text: >-
        Which bright winter star rises almost exactly due east, from almost
        anywhere on Earth?
      answers:
        - text: >-
            Betelgeuse
          correct: false
          explanation: >-
            Betelgeuse is about 7° north of the celestial equator. From here
            it rises about 10° north of east.
        - text: >-
            Sirius
          correct: false
          explanation: >-
            Sirius is well south of the celestial equator. From here it rises
            more than 20° south of east.
        - text: >-
            Rigel
          correct: false
          explanation: >-
            Rigel is about 8° south of the celestial equator. From here it
            rises about 11° south of east.
        - text: >-
            Mintaka, the westernmost star of Orion's Belt
          correct: true
          explanation: >-
            Mintaka sits only about 0.3° from the celestial equator, which
            meets every horizon due east and due west.

    # Q10 — Adhara and extreme ultraviolet (4 options) — correct at position 3
    - id: 10
      image: "fig-canis-major.webp"
      text: >-
        Adhara, in Canis Major, is only about the 22nd-brightest star in our
        sky, but at one kind of light it outshines every other star. Which?
      answers:
        - text: >-
            Radio waves
          correct: false
          explanation: >-
            Ordinary stars are faint radio sources. The radio sky is ruled
            by the Sun, the Milky Way, and remnants like Cassiopeia A.
        - text: >-
            Infrared
          correct: false
          explanation: >-
            Cool stars and dust shine brightest in the infrared. Adhara is a
            hot blue giant.
        - text: >-
            Extreme ultraviolet
          correct: true
          explanation: >-
            Adhara is hot, and its light reaches us through unusually thin
            interstellar gas. NASA's EUVE satellite measured it in the 1990s.
        - text: >-
            X-rays
          correct: false
          explanation: >-
            The X-ray sky beyond the Sun is led by Scorpius X-1, a neutron
            star feeding on a companion.

    # Q11 — Sirius and the Egyptian calendar (3 options) — correct at position 1
    - id: 11
      image: "fig-sirius-dawn-egypt.webp"
      text: >-
        Ancient Egyptians watched for the morning when Sirius first
        reappeared in the dawn sky. Why?
      answers:
        - text: >-
            Its return came around the start of the Nile's yearly flood, and
            it marked the New Year.
          correct: true
          explanation: >-
            Their 365-day calendar slipped against Sirius by about a day
            every four years, so the two lined up again only every ~1,460
            years.
        - text: >-
            It marked the winter solstice and the start of planting.
          correct: false
          explanation: >-
            Sirius returned to the dawn sky in summer, not winter.
        - text: >-
            Sirius turned red that morning, signalling the harvest.
          correct: false
          explanation: >-
            Sirius doesn't change color. Low in the dawn it can twinkle in
            many colors, but that's our atmosphere.

    # Q12 — Capella is two giants (2 options) — correct at position 2
    - id: 12
      image: "fig-auriga.webp"
      text: >-
        Capella looks like one golden star. What do telescopes and spectra
        show it really is?
      answers:
        - text: >-
            A single giant star about 12 times the Sun's width.
          correct: false
          explanation: >-
            That describes one of them — but there are two.
        - text: >-
            Two giant stars, each about 2.5 times the Sun's mass, circling
            each other every 104 days.
          correct: true
          explanation: >-
            They're about 0.74 AU apart, closer than Earth is to the Sun. A
            pair of faint red dwarfs orbits far beyond them.
---

{{< quiz >}}

---

## Image Credits

All figures are by NBAS, drawn in Python (matplotlib, astropy).

- **Banner:** Stellarium screen capture by NBAS.
- **Thumbnail:** Sirius A and B, Hubble Space Telescope — NASA, ESA, H. Bond (STScI) and M. Barstow (University of Leicester).

- **Star charts (Q2, Q3, Q6, Q8, Q9, Q10, Q12):** star positions and brightnesses from the Yale Bright Star Catalogue, 5th edition (Hoffleit & Warren 1991).
- **Q1 — Canopus:** the sky's north–south line as seen from 42.7° N.
- **Q4 — Epsilon Aurigae:** simplified eclipse curves using published eclipse timings and depths (Gyldenkerne 1970; Maravelias et al. 2012); real light curves show more detail.
- **Q5 — Capella:** the sky overhead from North Adams, 15 January 2027, 9 p.m.
- **Q7 — Sirius B:** orbit computed from the elements of Bond et al. (2017).
- **Q11 — Sirius and Egypt:** dawn sky from Memphis, Egypt, about 2500 BC, computed with astropy; approximate.
