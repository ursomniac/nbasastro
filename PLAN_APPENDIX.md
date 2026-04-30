# PROJECT PLAN: NBAS ASTRO (V0.20.0 PREP)
**DATE:** 2026-04-29
**STATUS:** ACTIVE | [V: 0.19.2 AGENT]

## A. Sidebar widgets

Must not have a CORS block issue.  FEEDS of infomation are OK, if we can use that and design our own widget to filter/format/display the content therein.

1. DONE - Aurora / Space weather? - current Kp index with 12-24h forecast...
2. DOES NOT WORK - APOD (Astronomy Picture of the Day)
3. DONE - Sunspots / H-alpha image?
4. DONE - Local Weather  (temp, and anything that would be relevant to planning observing sessions)
5. WORKED NOW BROKEN - Meteoblue - Astronomy Seeing (supposedly no CORS)
6. TODO - ISS (NASA) - direct HTML/JS snippet - show upcoming passes for the ISS at our location

### A.1. OR External Links:

1. Jupiter Moons and GRS: https://theskylive.com/galilean-moons
2. etc.?

## B. v0.20 proposal
Use https://github.com/commenthol/astronomia with the site (JS library)
to generate widgets or reports ...

1. NEED to test a separate install - if that succeeds
    - we'll know what we can do
2. INTEGRATE with our repo
3. SELECT a small number of test apps to try but here's a general list
    1. Jupiter (a single Jupiter widget would be GREAT)
        - Jupiter moons
        - Jupiter GRS
        - Jupiter moon events (transits, etc.)
    2. Saturn (a single Saturn widget would be GREAT)
        - Saturn rings
        - Saturn moons
    3. Mars (if there are Mars map images - otherwise skip)
    4. SSO
        - Sun?
        - Planet positions (this might be on its own page, updated hourly?)
        - Dwarf planets?
    5. Generate Date and time
        - Sidereal Time (if this can work like a clock in real-time that'd be cool)
        - Julian Date (ditto)

Site performance will be of CRITICAL IMPORTANCE!

## C. TECHNICAL DEBT / BACKLOG
Next in series might be a nice-to-have for pages that are part of a Series!

- [X] **"Next in Series" Logic:** Evaluate feasibility of a "Next Article" footer for series-driven content.
- [X] inhibit "Related Articles" if there's nothing related.
- [ ] **Content Modeling:** Refine `knowledgetopics` taxonomy. --- TBD, defer for now.



