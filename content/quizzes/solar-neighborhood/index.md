---
title: "The Solar Neighborhood"
byline: "How well do you know the Sun's stellar backyard?"
date: 2026-07-21
authors: ["nbas-staff"]
series: ["astronomy-quiz"]
knowledgetopics: ["quizzes"]
level: "intermediate"
description: "Ten questions about the stars within roughly 10 parsecs of the Sun — nearest neighbors, most common types, and a few surprises about what lurks in the cosmic backyard."
thumbnail: "solar-neighborhood.jpg"
quiz:
  passing_score: 80
  scoring: "first-only"
  renderer: "choose-star"
  questions:

    - id: 1
      text: "Which of these nearby star systems was discovered most recently — unknown to science until the era of infrared space surveys?"
      answers:
        - text: "Proxima Centauri"
          image: "proxima-centauri.jpg"
          correct: false
          explanation: "Proxima Centauri was discovered in 1915 by Robert Innes at the Cape Observatory, who noticed it shared the large proper motion of Alpha Centauri. Despite being the nearest star to the Sun at 4.24 light-years, it is far too faint to see without a telescope."
        - text: "Barnard's Star"
          image: "barnards-star.png"
          correct: false
          explanation: "Barnard's Star was discovered in 1916 by E.E. Barnard, who identified it by its exceptionally large motion across the sky — the fastest proper motion of any known star. At 5.96 light-years, it is the second nearest star system to the Sun."
        - text: "Wolf 359"
          image: "wolf-359.png"
          correct: false
          explanation: "Wolf 359 was catalogued in the early 20th century by Max Wolf during systematic surveys of high-proper-motion stars. At 7.86 light-years, it is the third nearest main-sequence star and one of the intrinsically faintest stars known."
        - text: "Luhman 16"
          image: "luhman-16.jpg"
          correct: true
          explanation: "Correct! Luhman 16 — a brown dwarf binary at 6.5 light-years — was discovered in 2013 by astronomer Kevin Luhman mining archival data from the WISE satellite. It is the third nearest known star system to the Sun, and no one knew it existed until the 21st century."

    - id: 2
      text: "Of the roughly 50 star systems within 10 parsecs of the Sun, which type of star is by far the most common — yet not one is bright enough to see with the naked eye?"
      answers:
        - text: "Red dwarf (M-type)"
          image: "type-m-dwarf.png"
          correct: true
          explanation: "Correct! M-type red dwarfs make up roughly 70–75% of all stars in the solar neighborhood. They are intrinsically so dim that not one of the ~35 red dwarfs within 10 parsecs is visible without optical aid — the nearest, Proxima Centauri, shines at magnitude +11 from just 4.24 light-years away."
        - text: "Orange dwarf (K-type)"
          image: "type-k-dwarf.png"
          correct: false
          explanation: "K-type orange dwarfs are the second most common type in the solar neighborhood, making up roughly 12% of nearby stars. Several are naked-eye objects — Epsilon Eridani and Alpha Centauri B are both K-type — but they are far outnumbered by red dwarfs."
        - text: "Sun-like star (G-type)"
          image: "type-g-dwarf.png"
          correct: false
          explanation: "G-type stars like the Sun represent only about 7% of stars in the solar neighborhood. The Sun is actually somewhat unusual — most of its stellar neighbors are smaller, dimmer, and considerably redder."
        - text: "White dwarf"
          image: "white-dwarf.png"
          correct: false
          explanation: "White dwarfs — the dense remnants of Sun-like and smaller stars — make up roughly 10% of stars in the solar neighborhood. They are common, but far from the most common type: red dwarfs outnumber them by a factor of seven or more."

    - id: 3
      text: "Which star system is the third nearest to the Sun, after the Alpha Centauri system and Barnard's Star?"
      answers:
        - text: "Sirius"
          image: "sirius.jpg"
          correct: false
          explanation: "Sirius is a genuine neighbor at 8.6 light-years, but it is the fifth nearest star system, not the third. Its brilliance makes it feel like the Sun's closest companion, but Wolf 359, Lalande 21185, and Luhman 16 are all closer."
        - text: "Wolf 359"
          image: "wolf-359.png"
          correct: true
          explanation: "Correct! Wolf 359 lies 7.86 light-years from the Sun — the third nearest known star system. It is an extremely dim M6Ve red dwarf with a luminosity only 0.1% of the Sun's, and it is one of the most active flare stars known."
        - text: "Lalande 21185"
          image: "lalande-21185.png"
          correct: false
          explanation: "Lalande 21185 (GJ 411) is the fourth nearest star system at 8.29 light-years — only 0.43 light-years farther than Wolf 359. This M2V red dwarf is faintly visible in large binoculars under dark skies."
        - text: "Epsilon Eridani"
          image: "epsilon-eridani.png"
          correct: false
          explanation: "Epsilon Eridani lies 10.5 light-years away, making it the ninth nearest star system to the Sun. It is one of the nearest naked-eye stars and a long-studied target in exoplanet and SETI searches, but it is not among the three nearest."

    - id: 4
      text: "Which star has the highest proper motion of any known star — drifting so steadily across the sky that it covers the apparent width of the full Moon in about 180 years?"
      image: "barnards-star-motion.gif"
      answers:
        - text: "Proxima Centauri"
          image: "proxima-centauri.jpg"
          correct: false
          explanation: "Proxima Centauri has a proper motion of about 3.85 arcseconds per year — significant, but less than 40% of Barnard's Star's 10.4 arcseconds. Proxima is the nearest star to the Sun, but Barnard's holds the proper motion record by a wide margin."
        - text: "61 Cygni"
          image: "61-cygni.jpg"
          correct: false
          explanation: "61 Cygni earned the nickname 'Flying Star' in the 18th century for its proper motion of 5.28 arcseconds per year — and became the first star beyond the solar system to have its distance measured (Bessel, 1838). But Barnard's Star moves nearly twice as fast."
        - text: "Sirius"
          image: "sirius.jpg"
          correct: false
          explanation: "Sirius has a proper motion of about 1.34 arcseconds per year — modest for a nearby star. Its prominence comes from intrinsic brightness and proximity, not from fast apparent motion across the sky."
        - text: "Barnard's Star"
          image: "barnards-star.png"
          correct: true
          explanation: "Correct! Barnard's Star moves 10.4 arcseconds per year — the fastest proper motion of any known star. It is also approaching the Sun and will reach its closest point of about 3.75 light-years in approximately 9,800 years, at which point it will briefly be the nearest star system."

    - id: 5
      text: "Three of these well-known nearby stars are binary or multiple systems. Which one is a single star with no known stellar companion?"
      answers:
        - text: "Sirius"
          image: "sirius.jpg"
          correct: false
          explanation: "Sirius is a binary: Sirius A (the brilliant A1V star) and Sirius B, a white dwarf discovered in 1862 — the first white dwarf ever identified. At the time its existence baffled astronomers, as it had nearly the Sun's mass packed into the size of Earth."
        - text: "Alpha Centauri"
          image: "alpha-centauri.jpg"
          correct: false
          explanation: "Alpha Centauri is a triple system: Alpha Cen A (G2V) and B (K1V) orbit each other every 80 years, while Proxima Centauri — an M-dwarf 4.24 light-years away — is the gravitationally bound third member in a very wide orbit."
        - text: "Vega"
          image: "vega.jpg"
          correct: true
          explanation: "Correct! Vega is a single A0V star — no companion of any kind has been confirmed. It is a rapid rotator spinning so fast it noticeably bulges at its equator, and it is surrounded by a debris disk first detected in 1983, but it travels alone."
        - text: "Procyon"
          image: "procyon.jpg"
          correct: false
          explanation: "Procyon is a binary: Procyon A (the bright F5 subgiant) and Procyon B, a white dwarf confirmed in 1896. Like Sirius B, Procyon B was suspected before it was seen because its gravity caused the visible star to wobble slightly in its path across the sky."

    - id: 6
      text: "Which of these bright, nearby, extensively-studied stars has no confirmed exoplanet?"
      answers:
        - text: "Sirius"
          image: "sirius.jpg"
          correct: true
          explanation: "Correct! Despite being the brightest star in the night sky, just 8.6 light-years away, and intensively observed, Sirius has no confirmed exoplanet. Its hot A-type primary and the dynamically complex history of its white dwarf companion may help explain why no planets have been found."
        - text: "Proxima Centauri"
          image: "proxima-centauri.jpg"
          correct: false
          explanation: "Proxima Centauri has at least one confirmed exoplanet — Proxima b, an approximately Earth-mass planet in the habitable zone confirmed in 2016. A second candidate, Proxima d, has been reported more recently."
        - text: "Ross 128"
          image: "ross-128.png"
          correct: false
          explanation: "Ross 128 b was confirmed in 2017: a planet roughly 1.35 times Earth's mass, orbiting every 9.9 days at a distance that puts it at or near the habitable zone. Ross 128's unusually low flare activity makes this one of the more interesting nearby exoplanets."
        - text: "Tau Ceti"
          image: "tau-ceti.png"
          correct: false
          explanation: "Tau Ceti has multiple planet candidates — recent analyses suggest at least four, with Tau Ceti e and f in or near the habitable zone. It has been a prime target in SETI searches for decades, partly because it is the nearest Sun-like single star."

    - id: 7
      text: "Most red dwarfs near the Sun are highly active flare stars that periodically blast their planets with intense UV and X-ray radiation. Which of these nearby red dwarfs is notably quiet — and whose planet is considered more habitable partly because of it?"
      answers:
        - text: "Proxima Centauri"
          image: "proxima-centauri.jpg"
          correct: false
          explanation: "Proxima Centauri is an EV Lacertae-type flare star and one of the most active in the solar neighborhood. It regularly produces flares energetic enough to bathe Proxima b in intense UV and X-ray radiation, making any surface life a challenging proposition."
        - text: "Ross 128"
          image: "ross-128.png"
          correct: true
          explanation: "Correct! Ross 128 is one of the calmest red dwarfs in the solar neighborhood, showing significantly lower flare activity than Proxima Centauri, Wolf 359, or UV Ceti. Ross 128 b is considered a more promising habitability candidate than Proxima b partly for this reason."
        - text: "Wolf 359"
          image: "wolf-359.png"
          correct: false
          explanation: "Wolf 359 — also catalogued as CN Leonis — is one of the most active flare stars known, producing frequent and powerful outbursts. Its proximity and extreme activity make it a well-studied example of what a hostile stellar environment looks like."
        - text: "UV Ceti"
          image: "uv-ceti.png"
          correct: false
          explanation: "UV Ceti (Luyten 726-8 B) is so active that the entire class of stellar flare stars — UV Ceti variables — is named after it. It produces some of the most dramatic flares ever observed on any nearby star."

    - id: 8
      text: "Which of these nearby stars hosts a confirmed planet in or near its habitable zone — the range of distances where liquid water could exist on a rocky surface?"
      answers:
        - text: "Epsilon Eridani"
          image: "epsilon-eridani.png"
          correct: false
          explanation: "Epsilon Eridani has a planet candidate orbiting at roughly 3.4 AU — but for a K2V star, the habitable zone spans only about 0.5–0.9 AU. At 3.4 AU the planet sits far outside the HZ, in a region analogous to Jupiter's orbit around the Sun."
        - text: "Barnard's Star"
          image: "barnards-star.png"
          correct: false
          explanation: "A planet candidate called Barnard b was announced in 2018, but subsequent analysis has not confirmed it and the claim has been largely withdrawn. No planet is currently confirmed around Barnard's Star."
        - text: "Proxima Centauri"
          image: "proxima-centauri.jpg"
          correct: true
          explanation: "Correct! Proxima b, confirmed in 2016, orbits Proxima Centauri every 11.2 days at roughly 0.049 AU — squarely within the habitable zone of an M-dwarf star. Whether it retains an atmosphere despite Proxima's intense flare activity is the central open question."
        - text: "Alpha Centauri"
          image: "alpha-centauri.jpg"
          correct: false
          explanation: "A planet around Alpha Centauri B was announced in 2012 but retracted in 2015 — the signal was an artifact of the data processing. No confirmed exoplanet exists in either the A or B system, though the search continues."

    - id: 9
      text: "Three of these nearby star systems contain at least one white dwarf — the dense remnant of a burned-out star. Which one does not?"
      answers:
        - text: "Sirius"
          image: "sirius.jpg"
          correct: false
          explanation: "Sirius B is a white dwarf — the first ever identified, spotted by Alvan Graham Clark in 1862. It is roughly the size of Earth but contains near the mass of the Sun, compressed to a density roughly a million times that of water."
        - text: "Procyon"
          image: "procyon.jpg"
          correct: false
          explanation: "Procyon B is a white dwarf confirmed in 1896, orbiting the bright F5 primary every 41 years. Its existence was suspected before it was seen because Procyon A followed a subtly wavy path across the sky — a wobble produced by the companion's gravity."
        - text: "40 Eridani"
          image: "40-eridani.png"
          correct: false
          explanation: "40 Eridani B is a white dwarf and actually the most easily observed white dwarf accessible to amateur telescopes — visible in a 3-inch scope. The 40 Eri system is triple: a K1V primary, the white dwarf, and a red dwarf further out. William Herschel discovered the BC pair in 1783."
        - text: "Tau Ceti"
          image: "tau-ceti.png"
          correct: true
          explanation: "Correct! Tau Ceti is a single G8.5V star at 11.9 light-years with no known stellar companion — just a debris disk and a family of planet candidates. It is one of the nearest and most Sun-like solitary stars in the solar neighborhood."

    - id: 10
      text: "Which star is predicted to make the closest known approach to our solar system within the next few million years — passing well inside the Oort Cloud and potentially triggering a comet shower toward the inner solar system?"
      image: "gliese-710-flyby.svg"
      answers:
        - text: "Gliese 710"
          image: "gliese-710.jpg"
          correct: true
          explanation: "Correct! Gliese 710, a K7/M0 dwarf currently 63 light-years away, will pass within roughly 0.2 light-years (~13,000 AU) of the Sun in about 1.35 million years — well inside the Oort Cloud's outer boundary. Its gravitational influence may scatter Oort Cloud comets onto paths that bring them into the inner solar system."
        - text: "Barnard's Star"
          image: "barnards-star.png"
          correct: false
          explanation: "Barnard's Star is approaching the Sun and will reach closest approach — about 3.75 light-years — in roughly 9,800 years. That is the closest any star will come in recorded history, but it is still far outside the Oort Cloud and will cause no significant gravitational disruption."
        - text: "Scholz's Star"
          image: "scholzs-star.jpg"
          correct: false
          explanation: "Scholz's Star (WISE J0720−0846) made the closest confirmed past flyby of the solar system — passing about 0.82 light-years from the Sun roughly 70,000 years ago, within the Oort Cloud. That was a closer approach than Barnard's Star will manage, but Gliese 710's predicted passage will be closer still."
        - text: "Alpha Centauri"
          image: "alpha-centauri.jpg"
          correct: false
          explanation: "Alpha Centauri is the Sun's nearest stellar neighbor now, but its trajectory over the next million years carries it away rather than toward a dramatic close approach. It will never come significantly closer than its current distance of about 4.4 light-years."
---
{{< quiz >}}
