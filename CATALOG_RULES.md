# NBAS Astro Object Library — Implementation Plan

## Overview

A data-driven object library for the NBAS Hugo site that allows article writers
to reference astronomical objects (DSOs, stars, solar system objects) with a
simple shortcode. Object metadata lives in YAML files under `data/`, and a Hugo
shortcode handles rendering in multiple display modes.

---

## Directory Structure

```
data/
  dso/
    m_31.yaml
    c_63.yaml
    ngc_891.yaml
    ic_1613.yaml
    ...
  stars/
    sirius.yaml          # proper name canonical (bright/well-known stars)
    cma_alpha.yaml       # Bayer designation
    cma_9.yaml           # Flamsteed designation
    peg_51.yaml          # Flamsteed
    peg_51_b.yaml        # exoplanet — appended letter
    hr_1099.yaml         # HR catalog
    hd_123456.yaml       # HD catalog
    gj_710.yaml          # Gliese-Jahreiß (nearby stars)
    bd+00_409.yaml       # Bonner Durchmusterung (positive dec)
    bd-00_394.yaml       # Bonner Durchmusterung (negative dec)
    cet_omicron.yaml     # Bayer with spelled-out Greek
    # double stars: wing it case by case
    ...
  sso/
    jupiter.yaml         # planets: just the name
    eris.yaml            # dwarf planets: just the name if named
    1p_halley.yaml       # comets: slash or space → underscore
    c2023_a1.yaml
    2006_dp14.yaml       # asteroids: year_stuff
    388188.yaml          # numbered asteroids
    274301_wikipedia.yaml  # named asteroids: number_name
    lyrids.yaml          # meteor showers: just the name
    jup_io.yaml          # moons: planet abbreviation + name
    sat_titan.yaml
    sat_2009s1.yaml      # provisional moon designations
    ...
  sso/
    jupiter.yaml
    ...
  aliases.yaml          # maps all alternate IDs to canonical filenames

assets/images/objects/
  dso/
    m31-thumb.jpg
    ...
  stars/
    ...
  sso/
    ...
  _defaults/
    default-star.svg
    default-galaxy.svg
    default-planet.svg
```

---

## YAML Schema

### DSO

```yaml
id: m_42                         # canonical ID = filename without .yaml
aliases:
  - ngc_1976
  - orion nebula
  - great orion nebula
display_name: "Orion Nebula"
type: emission_nebula            # drives default icon
constellation: Orion
ra: "05h 35m 17s"
dec: "−05° 23′ 28″"
magnitude: 4.0
distance_ly: 1344
thumbnail: dso/m42-thumb.jpg     # relative to assets/images/objects/
description: "Brief blurb for panel/modal display."
```

### Star

```yaml
id: sirius                       # canonical ID = proper name where unambiguous
aliases:
  - cma_alpha
  - hr_2491
  - hd_48915
display_name: "Sirius (α CMa)"
proper_name: Sirius
bayer: "α CMa"
type: star
constellation: Canis Major
ra: "06h 45m 09s"
dec: "−16° 42′ 58″"
magnitude: -1.46
distance_ly: 8.6
spectral_class: A1V
thumbnail: stars/sirius-thumb.jpg
description: "Brief blurb for panel/modal display."
```

### Variable Star

```yaml
id:                              # canonical ID per naming rules document
aliases: []
display_name: ""
type: variable_star
subtype:                         # e.g. cepheid, mira, eclipsing_binary
constellation:
ra:
dec:
magnitude_range:                 # e.g. "3.3 – 4.4"
period_days:
thumbnail:
description:
```

### SSO

Planets and named dwarf planets:

```yaml
id: jupiter
aliases:
  - jup
display_name: "Jupiter"
type: planet
thumbnail: sso/jupiter-thumb.jpg
description: "Brief blurb for panel/modal display."
```

Comets (slash or space → underscore):

```yaml
id: 1p_halley
aliases:
  - halley
  - halley's comet
display_name: "1P/Halley"
type: comet
thumbnail:
description:
```

Asteroids:

```yaml
id: 274301_wikipedia          # number_name after naming; year_stuff for provisionals
aliases:
  - wikipedia                 # informal name alone as alias
display_name: "274301 Wikipedia"
type: asteroid
thumbnail:
description:
```

Meteor showers:

```yaml
id: lyrids
aliases:
  - lyrid meteor shower
display_name: "Lyrids"
type: meteor_shower
peak_date: "April 22"
parent_body: c1861_g1_thatcher
thumbnail:
description:
```

Moons (planet abbreviation + name; provisional designations as-is):

```yaml
id: sat_titan
aliases:
  - titan
display_name: "Titan"
type: moon
parent_body: saturn
thumbnail:
description:
```

---

## Naming Rules (Bob's Canon)

These rules determine the canonical filename (without `.yaml`) for each object.
The alias system handles all other ways to reference the same object.

### DSO — priority order: Messier > Caldwell > NGC > Other

| catalog | format | example |
|---------|--------|---------|
| Messier | `m_##` | `m_42` |
| Caldwell | `c_##` | `c_63` |
| NGC | `ngc_####` | `ngc_891` |
| IC | `ic_####` | `ic_1613` |
| Coordinate-based | `cat[+-]xxxxxxx` or `cat_xxx[+-]yy.yy` | `pgc+123456` |

### Stars — priority order: constellation+id > catalog > proper name

| designation | format | example |
|-------------|--------|---------|
| Bayer (Greek) | `con_greek` | `cma_alpha`, `cet_omicron` |
| Bayer (superscript) | `con_greek#` | `ori_pi3` |
| Flamsteed | `con_##` | `cma_9`, `peg_51` |
| Exoplanet | `con_##_letter` | `peg_51_b` |
| Variable | `con_vardesig` | `cyg_ss`, `cyg_v404` |
| HR catalog | `hr_####` | `hr_1099` |
| HD catalog | `hd_######` | `hd_123456` |
| Gliese-Jahreiß | `gj_###` | `gj_710` |
| Bonner Durchmusterung | `bd[+-]dec_###` | `bd+00_409`, `bd-00_394` |
| Proper name | name only | `sirius` (for well-known stars where name IS the canonical) |
| Double stars | case by case | — |

### SSO

| type | format | example |
|------|--------|---------|
| Planet | name | `jupiter` |
| Dwarf planet | name (if named) | `eris` |
| Comet | designation, slash/space → `_` | `1p_halley`, `c2023_a1` |
| Asteroid (provisional) | `year_stuff` | `2006_dp14` |
| Asteroid (numbered) | number | `388188` |
| Asteroid (named) | `number_name` | `274301_wikipedia` |
| Meteor shower | name | `lyrids` |
| Moon | `planet_name` | `jup_io`, `sat_titan`, `sat_2009s1` |

---



Aliases are stored in two places that must stay in sync:

1. **In each object's YAML file** — the `aliases` list is the source of truth
2. **In `data/aliases.yaml`** — a flat map used by the Hugo lookup partial for
   fast resolution at build time

```yaml
# data/aliases.yaml  — auto-generated by scripts/build_aliases.py
ngc_1976: m_42
orion nebula: m_42
great orion nebula: m_42
cma_alpha: sirius
hr_2491: sirius
hd_48915: sirius
```

### Lookup Flow

```
input string "c63"
  → normalize: lowercase, trim whitespace
  → try site.Data.dso["c63"] → found? load it
  → try site.Data.aliases["c63"] → resolves to "ngc7293"
  → try site.Data.dso["ngc7293"] → found? load it
  → not found → return nil (trigger fallback rendering)
```

Normalization rules applied to all input before lookup:

- Lowercase
- Trim leading/trailing whitespace
- Collapse internal whitespace to single space

---

## Default Icons

Three SVG icons cover all categories. The `type` field in each YAML drives
which icon is used when no thumbnail is present.

| type value(s)                          | icon file                     |
|----------------------------------------|-------------------------------|
| star, variable_star                    | _defaults/default-star.svg    |
| galaxy, nebula, cluster, etc.          | _defaults/default-galaxy.svg  |
| planet, comet, asteroid, dwarf_planet  | _defaults/default-planet.svg  |

---

## Shortcode

### Signature

```
{{< astro-lookup dso="m42,c63,ngc891" star="sirius" display="table" >}}
{{< astro-lookup dso="m31" display="panel" >}}
{{< astro-lookup dso="m57" display="modal" >}}
```

- `dso`, `star`, `sso` — comma-separated IDs (any alias accepted)
- `display` — one of `panel`, `table`, `modal`
- `missing` — one of `skip` (default) or `stub` — controls fallback behavior

### Display Modes

**panel** — single object, full metadata card. Replaces the existing
"Object Info" panel. Best for articles centered on one object.

**table** — multiple objects, compact comparison rows. Each ID is resolved
and rendered as a table row. Good for "objects in this article" summaries.

**modal** — renders an inline linked badge in prose. Clicking opens a
lightweight modal with the full object card. Best for prose-heavy articles
where you want to reference an object without breaking reading flow.

### Fallback Behavior

| `missing=` | behavior |
|------------|----------|
| `skip`     | unresolved objects are silently dropped from output |
| `stub`     | unresolved objects render a greyed placeholder ("m99 — not in library") |

Stub rows are useful as a reminder of what still needs a YAML file.

---

## Implementation Steps

1. Write naming rules document (separate file — drives all filenames)
2. Define final YAML schemas for each category
3. Create `data/` directory structure
4. Create `assets/images/objects/_defaults/` with three default SVGs
5. Build `layouts/partials/astro-lookup.html` — the lookup partial
6. Build `layouts/shortcodes/astro-lookup.html` — calls the partial,
   handles display mode branching
7. Write CSS for panel, table, and modal styles
8. Seed with a small number of test YAML files covering each category
   and each display mode
9. Migrate existing "Object Info" pages to use the new shortcode
10. Add to library as articles require new objects

---

## Notes

- The modal display mode requires a small JavaScript snippet (~30 lines,
  vanilla JS) for open/close behavior. No framework dependency.
- Aliases must be maintained in both the object YAML and `aliases.yaml`.
  If these drift out of sync, lookups will silently fail. Consider a
  build-time check or linting step.
- The existing Astro Explorer references ~250 objects. Its metadata may
  be a useful source for bulk-generating initial YAML files rather than
  hand-authoring them.
- SSO canonical naming is straightforward — IAU designations are
  unambiguous for planets, standard packed format for minor planets.
- Naming rules for DSOs and stars are defined separately in the naming
  rules document. File names follow those rules exactly.
