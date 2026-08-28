---
title: "Why Do Variable Stars Do That?"
date: 2026-10-20
series: ["astronomy-quiz"]
level: "expert"
description: "An advanced quiz on the mechanisms behind ten kinds of variable stars — not recognizing light curves, but understanding why each one behaves the way it does."
banner: "banner.webp"
thumbnail: "star-icon.png"
quiz:
  renderer: "text-choice"
  passing_score: 70
  questions:

    # Q1 — T Coronae Borealis: predicting an unpredictable event (3 options) — correct at position 2
    - id: 1
      image: "TCrBLightCurve-1946.webp"
      text: >-
        As of late 2026, T Coronae Borealis ("the Blaze Star") still hasn't
        erupted, despite predictions pointing to 2025 and 2026. Why the
        ongoing uncertainty?
      answers:
        - text: >-
            Recurrent novae like T CrB erupt on an exact, unvarying schedule.
          correct: false
          explanation: >-
            Other recurrent novae recur anywhere from about a decade to over
            a century apart — there's no universal clock.
        - text: >-
            The ~80-year pattern rests on just a couple of confirmed
            eruptions, and predictions are statistical, not exact.
          correct: true
          explanation: >-
            Only two eruptions (1866, 1946) are well confirmed, and
            recurrence timescales vary wildly across different recurrent
            novae.
        - text: >-
            The eruption already happened quietly and went unnoticed.
          correct: false
          explanation: >-
            A 1,500-fold brightening to naked-eye visibility wouldn't go
            unnoticed under continuous AAVSO monitoring.

    # Q2 — Cepheid rise vs. decline (2 options) — correct at position 2
    - id: 2
      text: >-
        A Cepheid's brightness rises to peak faster than it fades back down.
        Why?
      image: "Delta_Cephei_lightcurve.webp"
      answers:
        - text: >-
            The star heats gradually during compression, then releases the
            energy suddenly during expansion.
          correct: false
          explanation: >-
            This reverses the real compression/expansion cycle.
        - text: >-
            Compression heats and brightens the star quickly; expansion cools
            it more gradually.
          correct: true
          explanation: >-
            Compression heats the star fast; expansion cools it slowly.

    # Q3 — Period-luminosity relation (3 options) — correct at position 3
    - id: 3
      image: "lmc-Storm2011_Cepheid_Data_svg-flat.webp"
      text: >-
        Why do more luminous Cepheids pulsate *more slowly* than dimmer ones?
      answers:
        - text: >-
            More luminous Cepheids are farther away, stretching out the
            observed period.
          correct: false
          explanation: >-
            Distance doesn't change a star's intrinsic pulsation period.
        - text: >-
            Overlapping pulsation modes beat together, producing a longer
            apparent cycle.
          correct: false
          explanation: >-
            Mode-beating happens in stars like Betelgeuse, not classical
            Cepheids.
        - text: >-
            Larger, lower-density stars pulsate more slowly — period tracks
            stellar density.
          correct: true
          explanation: >-
            Lower density means a longer pulsation period.

    # Q4 — RR Lyrae vs. Cepheids (2 options) — correct at position 1
    - id: 4
      image: "HR-diag-instability-strip_svg-flat.webp"
      text: >-
        Why are RR Lyrae stars found in old globular clusters and the
        galactic halo, while Cepheids are found in young spiral-arm regions?
      answers:
        - text: >-
            They're different stellar populations — RR Lyrae are old halo
            stars, Cepheids are young.
          correct: true
          explanation: >-
            They're separate populations — old halo stars vs. young disk
            stars.
        - text: >-
            RR Lyrae stars are simply older Cepheids that have used up more
            fuel.
          correct: false
          explanation: >-
            RR Lyrae aren't an older stage of Cepheids at all.

    # Q5 — Mira's amplitude (3 options) — correct at position 1
    - id: 5
      image: "Mira_light_curve-flat.webp"
      text: >-
        Why does Mira's brightness swing by several magnitudes — far more
        than a Cepheid's?
      answers:
        - text: >-
            Cool giant atmospheres have temperature-sensitive molecular
            opacity, so small temperature swings cause huge brightness
            changes.
          correct: true
          explanation: >-
            Cool, opaque molecules make small temperature swings look huge.
        - text: >-
            Mira is simply a much larger star, so radius changes produce big
            brightness swings.
          correct: false
          explanation: >-
            Size isn't the main driver of Mira's brightness swing.
        - text: >-
            Mira is secretly an eclipsing binary with a dim companion passing
            in front of it.
          correct: false
          explanation: >-
            Mira does have a companion — just not why it varies.

    # Q6 — Betelgeuse (4 options) — correct at position 3
    - id: 6
      image: "Betelgeuse_AAVSO_2019.webp"
      text: >-
        Why isn't Betelgeuse's brightness variation as clean and periodic as
        a Cepheid's?
      answers:
        - text: >-
            It pulsates in one single, clean mode, like a Cepheid.
          correct: false
          explanation: >-
            Betelgeuse's variation is messier than a single clean mode.
        - text: >-
            A companion star directly eclipses it, blocking its light.
          correct: false
          explanation: >-
            The companion clears dust — it doesn't eclipse directly.
        - text: >-
            A mix of pulsation-mode beating, convection, and a newly
            confirmed companion star.
          correct: true
          explanation: >-
            Mode-beating, convection, and a newly confirmed companion star
            all combine.
        - text: >-
            It's undergoing random, unpredictable death throes before core
            collapse.
          correct: false
          explanation: >-
            The variation is modeled, not random.

    # Q7 — The Algol paradox: mass transfer (2 options) — correct at position 2
    - id: 7
      image: "Algol_TESS_lightcurve.webp"
      text: >-
        In the Algol system, the less massive star is a more evolved
        subgiant, while the more massive star is still an ordinary
        main-sequence star. Normally the more massive star evolves faster —
        so why is it the other way around here?
      answers:
        - text: >-
            The two stars simply formed at different times, so the subgiant
            is just older.
          correct: false
          explanation: >-
            Both stars formed together — the mismatch comes from mass
            transfer, not different ages.
        - text: >-
            The subgiant used to be more massive, evolved first, and
            transferred most of its mass onto its companion.
          correct: true
          explanation: >-
            Mass transfer reversed the original mass ratio after the
            subgiant evolved and overflowed onto its companion.

    # Q8 — Nova decline timescale (3 options) — correct at position 3
    - id: 8
      image: "V1500.Cyg.JD2442500-2444500.LightCurve.webp"
      text: >-
        Why does a classical nova's decline after peak brightness take weeks
        to months, rather than happening instantly?
      answers:
        - text: >-
            The white dwarf itself takes weeks to cool down after the
            explosion.
          correct: false
          explanation: >-
            The white dwarf itself isn't what's slowly cooling.
        - text: >-
            Radioactive decay of freshly synthesized elements powers the slow
            fade.
          correct: false
          explanation: >-
            That's a supernova mechanism, not a nova's.
        - text: >-
            The detonation is instant, but the ejected material takes time
            to expand and cool.
          correct: true
          explanation: >-
            The ejected material, not the detonation, sets the fade time.

    # Q9 — R Coronae Borealis (3 options) — correct at position 2
    - id: 9
      image: "R_Coronae_Borealis_light_curve.webp"
      text: >-
        Why do R Coronae Borealis stars sometimes dim dramatically and
        unpredictably, rather than brightening like a nova?
      answers:
        - text: >-
            The star's outer layers pulsate irregularly, blocking and
            revealing the hot interior.
          correct: false
          explanation: >-
            RCB stars don't dim by pulsating irregularly.
        - text: >-
            They periodically puff out carbon dust clouds that drift into
            the line of sight.
          correct: true
          explanation: >-
            Dust clouds drift into view and clear on their own schedule.
        - text: >-
            A binary companion on a wide, poorly-constrained orbit
            periodically eclipses it.
          correct: false
          explanation: >-
            There's no eclipsing companion involved.

    # Q10 — Type Ia standard candle (2 options) — correct at position 1
    - id: 10
      image: "SN1994DLightCurve.webp"
      text: >-
        Why can Type Ia supernovae be used as reliable "standard candles"
        for measuring cosmic distances, while core-collapse supernovae
        can't?
      answers:
        - text: >-
            Type Ia detonates at a consistent mass limit, giving a repeatable
            peak brightness every time.
          correct: true
          explanation: >-
            A consistent detonation mass makes Type Ia's peak brightness
            repeatable.
        - text: >-
            Type Ia supernovae are simply closer to Earth on average, easier
            to measure precisely.
          correct: false
          explanation: >-
            Distance is what's being measured here — not a given.
---

{{< quiz >}}

---

## Image Credits

- **Q1 — T Coronae Borealis:** T CrB light curve of the 1946 eruption — PopePompus, CC BY-SA 4.0, via Wikimedia Commons
- **Q2 — Cepheid rise/decline:** Delta Cephei light curve — Warrickball, CC BY-SA 4.0, via Wikimedia Commons
- **Q3 — Period-luminosity relation:** Period-luminosity relation for LMC Cepheids — Dbenford, CC BY-SA 4.0, via Wikimedia Commons
- **Q4 — RR Lyrae vs. Cepheids:** HR diagram with instability strip — Rursus, CC BY-SA 3.0, via Wikimedia Commons
- **Q5 — Mira's amplitude:** Mira light curve, AAVSO 2011–2017 — Lithopsian, CC BY-SA 4.0, via Wikimedia Commons
- **Q6 — Betelgeuse:** Betelgeuse light curve, AAVSO 2019 — AAVSO, CC BY 2.5, via Wikimedia Commons
- **Q7 — The Algol paradox:** Algol light curve, TESS — Warrickball, CC BY-SA 4.0, via Wikimedia Commons
- **Q8 — Nova decline timescale:** V1500 Cygni (Nova Cygni 1975) light curve — AAVSO/Vladimir Kurg, Public domain, via Wikimedia Commons
- **Q9 — R Coronae Borealis:** R Coronae Borealis light curve — Lithopsian, CC BY-SA 4.0, via Wikimedia Commons
- **Q10 — Type Ia standard candle:** Type Ia supernova light curve, SN 1994D — PopePompus, CC BY-SA 4.0, via Wikimedia Commons
