---
title: "Guess the Astronomer!"
date: 2026-06-02
authors: ["nbas-staff"]
series: ["astronomy-quiz"]
knowledgetopics: ["quizzes"]
level: "intermediate"
description: "Match the discoverer with their discovery!"
thumbnail: "gal-moons.jpg"
quiz:
  passing_score: 80
  scoring: "first-only"
  renderer: "identify-image"
  questions:

    - id: 1
      text: "I discovered that sunspots were depressions and not \"clouds\" on the surface of the Sun."
      image: "sunspots.jpeg"
      answers:
        - text: "Maria Mitchell"
          image: "maria-mitchell.jpeg"
          correct: true
          explanation: "Maria Mitchell was a pioneering American astronomer, who had her own observatory on Nantucket, and taught at Vassar college.  She started observing the Sun daily in 1868 and determined the physical nature of sunspots."
        - text: "Richard Carrington"
          image: "richard_carrington.jpg"
          correct: false
          explanation: "Carrington measured the surface differential rotation of the Sun looking at the change of latitude of sunspots over the 11-yr sunspot cycle."
        - text: "Heinrich Schwabe"
          image: "Samuel_Heinrich_Schwabe.jpg"
          correct: false
          explanation: "Heinrich Schwabe was the first to determine the 11-year sunspot cycle."
        - text: "Galileo Galilei"
          image: "galileo.jpg"
          correct: false
          explanation: "Galileo made early observations of the Sun, but imagined they were clouds."

    - id: 2
      text: "I discovered 4 moons of Saturn: Tethys, Dione, Iapetus, and Rhea"
      image: "cassini_moons.webp"
      answers:
        - text: "Christiaan Huygens"
          image: "huygens.jpeg"
          correct: false
          explanation: "Huygens did discover Titan in 1655 - and resolved the true nature of Saturn's rings."
        - text: "Jeremiah Horrocks"
          image: "jeremiah_horrocks.jpg"
          correct: false
          explanation: "Jeremiah Horrocks demonstrated the Moon's orbit around the Earth was an ellipse, and predicted and observed the Transit of Venus in 16349."
        - text: "Giovanni Cassini"
          image: "cassini.jpeg"
          correct: true
          explanation: "Between 1671 and 1684, Cassini found these four moons orbiting Saturn.  After this, no moons were discovered for 100 years!  He also found the Cassini Division in the rings."
        - text: "Maria Cunitz"
          image: "maria-cunitz.jpg"
          correct: false
          explanation: "Maria Cunitz refined Kepler's mathematics, correcting errors and created the most accurate predictions of the positions of the planets for this era."

    - id: 3
      text: "Herschel discovered Uranus in 1781.  Who holds the record for observing Uranus before then, but completely failed to recognize it as a planet 12 times?"
      image: "34_tauri.jpg"
      answers:
        - text: "Pierre Charles Le Monnier"
          image: "le-monnier.jpg"
          correct: true
          explanation: "Observed Uranus 12 times over 19 years.  He actually observed Uranus four nights in a row, but when it was at it's orbital turning point, so didn't notice it moved."
        - text: "John Flamsteed"
          image: "john-flamsteed.jpeg"
          correct: false
          explanation: "Flamsteed recorded Uranus in 1690, mistaking it for a star which he added to his atlas as 34 Tauri."
        - text: "Tobias Mayer"
          image: "tobias-mayer.jpeg"
          correct: false
          explanation: "Recorded Uranus in observations in 1756, but didn't recognize it as a planet."
        - text: "James Bradley"
          image: "james-bradley.jpeg"
          correct: false
          explanation: "Saw Uranus three times between 1748 and 1753 in Capricornus and Aquarius without recognizing it was the same object."

    - id: 4
      text: "I discovered a planet, which then wasn't a planet, but is now a planet again."
      image: "ceres.jpg"
      answers:
        - text: "Edmond Modeste Lescarbault"
          image: "edmond-modeste-lescarbault.jpeg"
          correct: false
          explanation: "Thought he had seen the planet Vulcan crossing the disk of the Sun in 1859."
        - text: "Heinrich Olbers"
          image: "heinrich-olbers.jpg"
          correct: false
          explanation: "Olbers discovered Pallas in 1802 and Vesta in 1807.  At first they and Juno were listed as planets (although Herschel argued they were not), until being reclassified as asteroids."
        - text: "William Lassell"
          image: "william-lassell.jpg"
          correct: false
          explanation: "Lassell discovered Triton orbiting Neptune in 1846, which probably is a captured dwarf planet from the Kuiper Belt."
        - text: "Giuseppe Piazzi"
          image: "giuseppe-piazzi.jpg"
          correct: true
          explanation: "Ceres was first classified as a planet, then was determined to be an asteroid, then recently as the only dwarf planet not in the Kuiper belt."

    - id: 5
      text: "I discovered Proxima Centauri, the closest star to the Sun."
      image: "proxima-centauri.jpg"
      answers:
        - text: "Thomas Henderson"
          image: "thomas-henderson.jpg"
          correct: false
          explanation: "He first measured the parallax of Alpha Centauri in the 1830s, but wasn't aware of the trinary nature of the star."
        - text: "Edward Emerson Barnard"
          image: "ee-barnard.jpeg"
          correct: false
          explanation: "Discovered Barnard's star which has the highest measured proper motion, but is actually the 4th closest star to the Sun."
        - text: "Robert Innes"
          image: "robert-innes.jpeg"
          correct: true
          explanation: "Discovered in 1915.  Innes also was the first person to see the Great January Comet of 1910."
        - text: "Friedrich Bessel"
          image: "friedrich-wilhelm-bessel.jpg"
          correct: false
          explanation: "Bessel is credited with the first published measurement of stellar parallax (61 Cygni) in 1838."

    - id: 6
      text: "My observations of the timing of eclipses of Io proved that light travels as a finite speed."
      image: "jupiter-diagram.jpg"
      answers:
        - text: "Christiaan Huygens"
          image: "huygens.jpeg"
          correct: false
          explanation: "Used Rømer's data to calculate the speed of light (about 30% off)"
        - text: "Giovanni Cassini"
          image: "cassini.jpeg"
          correct: false
          explanation: "Cassini didn't think that light had a finite speed, and blamed the observed time shifts on errors in the moon's orbit instead."
        - text: "Robert Hooke"
          image: "robert-hooke.jpg"
          correct: false
          explanation: "Hooke also didn't believe Rømer's proof the light had a finite measurable speed, instead thinking that light should be instantaneous."
        - text: "Ole Rømer"
          image: "ole-romer.jpg"
          correct: true
          explanation: "Noticed in 1676 that eclipses occur later when Earth is moving away from Jupiter, but earlier when Earth is moving closer."

    - id: 7
      text: "Until my discovery, it was thought we couldn't know what stars were made of!"
      image: "solar-spectrum.jpg"
      answers:
        - text: "Joseph von Fraunhofer"
          image: "joseph-von-fraunhofer.jpg"
          correct: false
          explanation: "Mapped and cataloged those lines in the solar spectrum.  and that stars had a different spectrum than the Sun, but wasn't aware of what physically caused them."
        - text: "Gustav Robert Kirchhoff"
          image: "gustav-robert-kirchhoff.jpg"
          correct: true
          explanation: "In 1859, showed that burning elements on Earth produces a spectrum that could be used as fingerprints for specifically identifying the elements of stars and the Sun."
        - text: "William Huggins"
          image: "william-huggins.jpg"
          correct: false
          explanation: "The \"father of stellar spectroscopy\" obtaining spectra of stars and nabulae in the 1860s, but was applying the laboratory physics that Kirchhoff and Bunsen had demonstrated."
        - text: "Angelo Secchi"
          image: "angelo-secchi.jpg"
          correct: false
          explanation: "Created the first spectral classification for stars in the late 1860s.  It would be later improved by Williamina Fleming in 1890, and then further by Antonia Maury and Annie Jump Cannon in 1901."

    - id: 8
      text: "I solved a long-standing mystery about Saturn's rings.  I proved they couldn't be a solid or liquid sheet without breaking up under gravity, and instead must be countless, tiny particles orbiting the planet."
      image: "saturn.jpg"
      answers:
        - text: "Pierre-Simon Laplace"
          image: "pierre-simon-laplace.jpg"
          correct: false
          explanation: "He understood that the ring couldn't be completely solid, but suggested a system of multiple, solid, non-uniform rings."
        - text: "James Clerk Maxwell"
          image: "james-clerk-maxwell.jpg"
          correct: true
          explanation: "This earned him the Adams Prize in 1859, and was directly confirmed by the Voyager images in 1980.  But the ring particles are not in stable orbits and will vanish over the next 300 million years."
        - text: "Urbain Le Verrier"
          image: "urbain-leverrier.jpg"
          correct: false
          explanation: "Calculated orbits of the planets, and especially predicting the pre-discovery location of Neptune, but didn't have a theory on the nature of Saturn's rings."
        - text: "Lord Kelvin (William Thomson)"
          image: "lord-kelvin.jpg"
          correct: false
          explanation: "Studied fluid dynamics, thermodynamics, and the stability of mechanical systems, but Saturn was not of his objects of interest."

---
{{< quiz >}}
