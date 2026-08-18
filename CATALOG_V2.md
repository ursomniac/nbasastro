# v1.3 Plan: Object Metadata Corpus & Cross-Referencing

**Status:** Discovery / analysis only. Nothing in this document is scheduled or started.
**Owner:** Bob Donahue
**Supersedes:** the original `PLAN-v1.3-object-metadata.md` and `CATALOG_RULES.md`, both of which
independently converged on the same core mechanism (data-driven objects, generated alias index,
normalize-then-lookup) but disagreed on real specifics. This document reconciles both and captures
everything decided since. Where the two source documents conflicted, the resolution is noted
explicitly so the reasoning isn't lost.

---

## 1. Problem statement

Article front matter (`dso_messier`, `dso_ngc`, `dso_caldwell`, `dso_other`, and eventually
`sso_*`/`star_*`) is plain text with no relationship to anything else. There's no shared source of
truth for an object's metadata, no way to cross-reference a constellation page to the articles that
discuss objects in it, and no clean way to handle an article that focuses on more than one object
(which catalog value "wins" the page's metadata block?). Inconsistent catalog-number formatting
(`Sh2-188` vs `Sh 2-188`) has already caused a real, live bug.

## 2. Goals

1. Constellation pages get a generated section listing articles relevant to objects in that
   constellation, without hand-maintaining that list.
2. Astro Explorer object pages (already existing as page-per-object shells) gain a real metadata
   block pulled from a shared corpus, not whatever one article happened to assert.
3. A lookup shortcode lets an article embed an object's metadata card anywhere it's relevant in the
   body -- solving the "which object wins the page-level metadata block" problem outright, and
   letting a multi-object article (an AWV comparison piece, for instance) embed several.
4. Article front matter stays simple -- one taxonomy reference per object, same complexity as today.
   All the relational/curatorial complexity lives in the corpus, never in what a writer has to type.
5. None of this should meaningfully grow the Hugo site-image bundle before the planned move off
   GitHub Pages removes the 1GB ceiling.

## 3. Non-goals (explicit)

- **Not a public "browse all N,000 objects" feature.** Only surfaced when an article actually
  references an object.
- **Corpus `description` fields are not bulk AI-generated content.** Directly guarded against --
  see SS7.
- **No retroactive rewrite of existing articles required.** Resolution happens at build time by
  scanning existing front matter. Cleanup of inconsistent formatting is optional tidiness.
- **No dedicated one-off Explorer imagery as a blanket policy** -- see SS6.

## 4. Why not native Hugo taxonomies

Hugo's built-in taxonomy matching is exact-string -- it has no concept that `"C 17"` and `"NGC 147"`
mean the same object, which would produce duplicate taxonomy terms instead of one merged object. A
custom pre-build alias-resolution step (SS5.3) is required regardless of how appealing "just use
taxonomies" looks at first glance. Recorded here so it doesn't get re-proposed later without the
context of why it was rejected.

---

## 5. Architecture

### 5.1 Corpus storage -- one directory per object

Resolved as directory-per-object, not flat-file-per-object as originally proposed -- this is a real
upgrade over the first draft, not a stylistic choice:

```
data/
  dso/
    m-31/
      m-31.yaml
      media/
        m31-2026-08-15.yaml       # per-item metadata: telescope, date, exposure, contributor
        m31-2026-08-15.webp
        m31-hst-archival.yaml     # a second image, different contributor/source
        m31-hst-archival.jpg
  stars/
    cas-eta/
      cas-eta.yaml
  exoplanets/
    peg-51-b/
      peg-51-b.yaml
  sso/
    planet-jupiter/
      planet-jupiter.yaml
  aliases.yaml                    # generated, see SS5.3
```

Why this over a flat file: it directly supports (a) more than one image per object -- the exact
situation already hit in the M31 Family article -- without over-designing a whole separate image
service; (b) other contributors adding their own images alongside an existing one, so this doesn't
stay "a Bob show"; (c) non-photo media (orbit diagrams, light curves) living the same way, with
their own small metadata file describing source/type instead of telescope/exposure; (d) trivial
tooling later -- a directory walk answers "which Messier objects have no folder yet" for free; and
(e) an object is still perfectly valid with nothing but its own main YAML -- the media folder is
optional, never required.

**Deliberate scope note:** this is being adopted a little naively for v1.3, on the explicit
understanding that it may need revisiting once the corpus is large -- accepted as a reasonable
near-term risk rather than a solved problem.

### 5.2 Schema shape

```yaml
id: ngc-7635
class: dso                      # dso | sso | star | exoplanet | other
primary_id: "NGC 7635"
aliases: ["c-11", "bubble nebula"]
constellation: cas              # single scalar; not applicable to class: sso (see SS5.5)
coordinates:                    # not applicable to sso (no fixed position)
  ra: "23h20m48s"
  dec: "+61 12'"
  epoch: J2000

dso:                            # class-specific block; star: / sso: / exoplanet: are siblings
  object_type: emission_nebula
  angular_size: "15' x 8'"
  discoverer: "William Herschel"
  discovery_date: "1787"

sourced:                        # only for measured, genuinely-debatable physical properties --
  distance:                     # never for identifiers, coordinates, or orbital elements
    - value: "7,100 ly"
      source: "1990AJ....100..032S"     # ADS bibcode where one exists
    - value: "11,000 ly"
      source: "Annals of the Deep Sky, vol. 4"

extra:                          # catch-all for "we know this for this object, not others"
  central_star: "BD+60d2522"

description: ""
description_status: pending     # pending | drafted | reviewed
last_updated: 2026-08-17
```

**Binary/multiple stars** resolve through a `components:` list rather than separate files per star
-- this closes both the 61 Cygni ("does this deserve its own file, or two?") and the Sirius
A/B-vs-system naming ambiguity in one move:

```yaml
id: cas-eta
class: star
pairing_type: gravitationally_bound   # gravitationally_bound | optical | common_proper_motion
components:
  - label: A
    spectral_class: G0V
  - label: B
    spectral_class: K7V
```

`pairing_type` sits at the object level, not per-component, since it describes the relationship
between the stars, not either star individually.

### 5.3 Alias resolution

Unchanged in mechanism from the original plan, and independently converged on by CATALOG_RULES.md
-- good confirmation the approach is sound:

1. A pre-build script walks every object directory.
2. Every string in each object's `aliases` (normalized: lowercase, trim, collapse internal
   whitespace) maps to that object's canonical `id`.
3. This produces a generated `data/aliases.yaml` -- flat map, `alias -> canonical id`.
4. A second pass resolves every article's `dso_*`/`sso_*`/`star_*` reference through that map to
   produce the reference index constellation pages and Explorer pages consume.

**Lookup flow at render time** (confirms and formalizes CATALOG_RULES.md's description):

```
input "c63"
  -> normalize
  -> direct match against data.dso["c63"]?  found -> done
  -> else look up data.aliases["c63"]  ->  resolves to "ngc-7293"
  -> data.dso["ngc-7293"]  ->  found -> done
  -> not found -> fallback (skip or stub, see SS5.4)
```

**Regeneration trigger:** manual command -- confirmed. Only needs to run when objects are added or
removed; editing an existing file needs no regeneration since the alias set didn't change.

### 5.4 The lookup shortcode

Adopting CATALOG_RULES.md's fuller specification, which supersedes the placeholder name in the
original plan:

```
{{< astro-lookup dso="m42,c63,ngc891" star="sirius" display="table" >}}
{{< astro-lookup dso="m31" display="panel" >}}
{{< astro-lookup dso="m57" display="modal" >}}
```

- `dso`, `star`, `sso` -- comma-separated ids, any alias accepted.
- `display` -- `panel` (single object, full card -- replaces the existing Object Info panel),
  `table` (multiple objects, compact comparison rows), or `modal` (inline linked badge in prose;
  click opens the full card without breaking reading flow -- needs a small vanilla-JS snippet, no
  framework).
- `missing` -- `skip` (default; unresolved ids silently dropped) or `stub` (renders a greyed
  placeholder, e.g. "m99 -- not in library" -- useful as a visible to-do marker for what still needs
  a file).

**Open, not resolved:** live lookup vs. frozen-at-publish. Decided to proceed naively for v1.3 --
`astro-lookup` reads `site.Data` at build time, so every rebuild reflects whatever the corpus
currently says, with no snapshotting. That's a deliberate, named tradeoff (always-current vs.
"what a reader saw then still matches what they see now"), not an accidental default.

### 5.5 SSOs and constellations

Resolved: `constellation:` does not apply to `class: sso` at all, and SSOs do not participate in
the constellation cross-reference feature. This isn't a milder version of the DSO
dual-constellation case below -- a DSO is spatially near a boundary and picks a side by convention;
an SSO is in a genuinely different constellation depending on the date, with no "usual" one to
default to. There's no boundary-based fix for a moving object. If a future article wants something
like "Jupiter and Saturn were both in Pisces this month," that needs its own date-based mechanism
entirely, not an extension of this one.

**DSO dual-constellation case, for contrast:** objects straddling a boundary (e.g. NGC 6946 / C 12,
which straddles Cepheus/Cygnus but is conventionally assigned to Cygnus) get a single assigned
constellation by convention, with the article author's judgment as tiebreaker. `constellation:`
stays a scalar, never a list. Jagged IAU boundaries exist partly to minimize exactly this
situation, though it can't eliminate it for newly-discovered objects.

### 5.6 Images and media

Rather than a separate `nbas-image-lookup` shortcode (considered and set aside -- it would preclude
mixing article-local and library-referenced images within one gallery, and the M31 Family article
already needed exactly that mix), extend the existing `nbas-image` / `nbas-gallery` shortcodes with
a `lookup=` parameter alongside the current `src=`. A gallery's pipe-delimited item list can then
freely combine an article-local file and a corpus-referenced one in the same block.

**Size policy, reaffirmed:** the corpus's text (coordinates, aliases, sourced citations) is
negligible regardless of scale. The real size risk is *dedicated, one-off* imagery created solely
for an Explorer page. Policy: reuse an existing article image via `lookup=`, or show none -- no new
upload created just for an Explorer page -- until the GitHub Pages move removes the 1GB constraint.
Optionally, DSS2 or similar archival imagery could fill gaps where no contributor photo exists yet,
without violating this policy, since it wouldn't be a new original upload competing for bundle
space in the same way.

## 6. Object classes and naming rules

Canonical filename = the object's `id`. Protocol, decided explicitly: **`-` separates distinct
fields or disambiguates between them; `_` replaces a space within a single field.** Applied
consistently below; this corrects several inconsistent examples from earlier drafts (`m_31` ->
`m-31`, `cma_alpha` -> `cma-alp`, `asteroid_2006-xx-94` -> `asteroid-2006-xx-94`).

All filenames lowercase, no exceptions.

### 6.1 DSO

**Canonical priority (Bob's Canon, confirmed -- this is the resolution of a real conflict with the
original plan doc, which had proposed NGC/IC first; CATALOG_RULES.md's order wins):**
`Messier > Caldwell > NGC > Other`

| catalog | format | example |
|---|---|---|
| Messier | `m-##` | `m-42` |
| Caldwell | `c-##` | `c-63` |
| NGC | `ngc-####` | `ngc-891` |
| IC | `ic-####` | `ic-1613` |
| Coordinate-based / other | `cat-xxxxxxx` | `pgc-123456` |

### 6.2 Stars

Constellation prefix (3-letter IAU abbreviation) is present regardless of what follows. Precedent
order for what follows it, most-preferred first:

1. **Bayer** (Greek letter, 3-letter abbreviation, numbered when duplicated): `ori-alp`, `umi-alp`,
   `tau-gam`. Bayer numbering handles genuinely distinct, unrelated stars sharing a Greek letter --
   `eri-tau-4` and `eri-tau-5` are different stars, not components of one system. (Highest known
   count is around psi Aurigae, up to `aur-psi-10`.) Superscripted forms follow the same pattern:
   `ori-pi-3`.
2. **Flamsteed** (numbered east-to-west): `tau-10`. **Known gap, accepted as unsolved:** roughly
   twenty Flamsteed numbers cross constellation boundaries, since they predate the IAU's official
   boundary lines (the "10 UMa" group is the standard example). Not worth solving for this project.
3. **Variable star designation overrides everything below this point when one exists** --
   see the dedicated format below.
4. Rare minor-catalog exceptions (Groombridge 1830, Lalande 21185) -- expected to be uncommon in
   practice, since stars odd/interesting enough to lack any of the above usually turn out to have a
   variable-star designation anyway.
5. **HR** (Bright Star Catalog): `tau-hr-1099`
6. **HD** (Henry Draper): `xxx-hd-nnnnnn`
7. **Other catalogs** (SAO, BD, CD, CPD, GJ/Gliese, Kepler/TESS ids, etc.), same field-based pattern.
   Occasionally a genuine judgment call between a double-star catalog id and a standard catalog id
   for the same star -- decided case by case, not by fixed rule.
8. **Double stars** -- acknowledged as the messiest corner of the whole scheme, given the number of
   overlapping catalogs (Sigma, Sigma-Sigma, O-Sigma-Sigma, h, and others). Since all stars already
   sort under one `stars/` tree with a constellation prefix, this self-organizes somewhat -- bright
   components already get clean ids (`cas-eta`, `cyg-61`) before the double-star-specific catalogs
   are ever needed. **Still open, not yet resolved:** an explicit ASCII mapping table for
   Sigma/Sigma-Sigma/O-Sigma-Sigma/h and other double-star catalog symbols. One tentative example
   exists (`cas-0s-398` for a Sigma number) but a single example isn't a rule.

**Variable stars** -- confirmed simple: `con-designation`, e.g. `cet-omi` (Mira), `cas-gam`
(Gamma Cas), `leo-r` (R Leonis), `cyg-v1500` (Nova Cygni). **Still open:** Greek-letter abbreviation
length is inconsistent across examples given so far (`cas-gam` vs. `cas-gamma`) -- needs one
fixed convention, not decided yet. Genuinely unlikely edge case, noted rather than solved: a star
with no variable-star id at all despite being flagged (e.g. a fresh NSV designation).

**Proper names are explicitly not used as the canonical id** (a real change from the original
CATALOG_RULES.md example, which had used `sirius` as canonical) -- the IAU's official proper-name
list and historical/cultural naming don't fully align, the IAU list keeps growing, and different
cultures have different names for the same star. Instead, `proper_name:` is a metadata *field*
inside the YAML (a list, to hold multiple cultural names), never the filename and never listed
under `aliases`.

**Binaries/multiples** use `components:` (SS5.2) rather than a separate file per star, closing the
61 Cygni and Sirius naming questions together.

### 6.3 Exoplanets

Given their own top-level class rather than nested inside a star's YAML or dumped into `other/`:
mass, radius, orbital period, and discovery method don't fit comfortably as bolted-on star fields,
and an object like 51 Pegasi b is exactly the kind of thing worth its own curated page (own media,
own sourced citations, own description) rather than a buried list entry.

```yaml
id: peg-51-b
class: exoplanet
host_star: peg-51        # same foreign-key pattern as a moon's parent_body
```

Lowercase letters starting at `b` per real IAU convention -- `a` implicitly refers to the star
itself, so there's no `peg-51-a` file to account for.

**Rogue planets** (no host star) are the true edge case here -- leaning toward `host_star: null`
within the same `exoplanet` class rather than demoting the whole category to `other/` over one
outlier, but not fully decided.

### 6.4 SSO

| type | format | example |
|---|---|---|
| Planet | `planet-name` | `planet-jupiter` |
| Dwarf planet (named) | `dwarf_planet-name` | `dwarf_planet-eris` |
| Comet | `comet-designation` | `comet-1p-halley`, `comet-c2025-a3` |
| Asteroid (numbered+named) | `asteroid-number-name` | `asteroid-1-ceres` |
| Asteroid (numbered only) | `asteroid-number` | `asteroid-348473` |
| Asteroid (provisional) | `asteroid-year-stuff` | `asteroid-2006-xx-94` |
| Meteor shower | `meteor-name` | `meteor-perseids`, `meteor-alpha-capricornids` |
| Moon | `moon-planet-name` | `moon-sat-titan` |

**Still open:** whether Ceres specifically should get the `dwarf_planet-` treatment like Eris,
rather than sitting under generic asteroid numbering as `asteroid-1-ceres` -- raised but not
answered; worth deciding on purpose rather than by accident of which examples got typed first.
**Also still open:** interstellar objects (1I/2I/3I -- e.g. 3I/ATLAS) aren't gravitationally bound
to the Sun and are their own IAU-recognized class, distinct from both asteroids and periodic
comets. Filing them under `asteroid-` is a pragmatic option but hasn't been decided on purpose, and
this is a live topic (an interstellar object was discovered as recently as last year) rather than a
hypothetical.

**SSO taxonomy fields**, mirroring the `dso_*` pattern but split by subtype rather than by
catalog (SSOs don't have the multi-catalog-alias problem DSOs do, so there's no need to collapse
several fields into one the way DSO catalogs do): `sso_planet`, `sso_moons`, `sso_asteroid`,
`sso_comet`, `sso_meteor`. Each stays a simple, single-field reference in article front matter --
the moon-to-planet relationship (`parent_body:`) lives entirely inside the corpus and never adds
complexity to what an article author has to type.

## 7. The description field -- guardrail against bulk AI content

Retained from the original plan; CATALOG_RULES.md's flatter `description: ""` field has no
equivalent guardrail, so this section is being carried forward deliberately rather than dropped in
the merge:

- Blank by default for the large majority of the initial corpus generation pass -- never
  bulk-generated.
- Filling one in becomes a normal checklist item when an article introduces a new reference to that
  object -- piecemeal, tied to real editorial attention.
- Explorer pages render nothing at all when the field is blank -- no placeholder text.
- `description_status` (`pending` / `drafted` / `reviewed`) lets a future census distinguish
  untouched entries from first-pass drafts once the corpus is large enough for that to matter.
- Never feeds back into ACL/AWV article prose as content -- at most a casual glance while drafting,
  never copied in as authoritative.

## 8. Default icons

Unchanged from CATALOG_RULES.md, not contradicted by anything since -- three SVGs, keyed by each
object's `type:` field:

| type value(s) | icon |
|---|---|
| star, variable_star | `_defaults/default-star.svg` |
| galaxy, nebula, cluster, etc. | `_defaults/default-galaxy.svg` |
| planet, comet, asteroid, dwarf_planet | `_defaults/default-planet.svg` |

## 9. Open questions (carried forward, unresolved)

1. Live lookup vs. frozen snapshot for `astro-lookup` -- deliberately deferred, proceeding naively
   for v1.3 (SS5.4).
2. Double-star catalog symbol table (Sigma/Sigma-Sigma/O-Sigma-Sigma/h -> ASCII) -- only one
   example exists so far, needs a real table (SS6.2).
3. Variable-star Greek-letter abbreviation length -- `cas-gam` vs. `cas-gamma` inconsistency,
   unresolved (SS6.2).
4. Ceres: `dwarf_planet-` or `asteroid-`? (SS6.4)
5. Interstellar objects (1I/2I/3I) -- no decided bucket yet (SS6.4)
6. Rogue planets within the exoplanet class -- leaning `host_star: null`, not finalized (SS6.3)
7. How would `astro-lookup` ever reference a single binary component (e.g. Sirius B alone) when the
   pair is stored as one object with `components: []`? Flagged as low-priority/rare, not resolved.

## 10. Phasing

Unchanged in structure from the original plan -- DSOs first, then SSOs, then stars, per explicit
preference (stars are real but not a near-term priority; a lot of the underlying hard cases have
already been fought through once, imperfectly, in SkyTour v2).

**Phase 1 -- DSO cross-referencing, no corpus required yet**
- Pre-build alias-index / reference-index generator, running against existing article front matter.
- Constellation pages gain a generated "articles about objects here" section.
- Build-time consistency checker for `dso_*` formatting -- directly motivated by real bugs already
  hit (`Sh2-188` vs `Sh 2-188`, a stray unresolved `IC 11`). High value, low risk, arguably worth
  doing before anything else in this plan.

**Phase 2 -- DSO metadata corpus**
- Generate the initial DSO corpus from the SkyTour database (itself sourced from SIMBAD/HyperLeda),
  Stellarium, and supplementary print sources (Skiff & Lam 1990, the Annals of the Deep Sky), with
  `sourced` attribution preserved.
- Explorer object pages upgrade to real metadata cards.
- Ship `astro-lookup`.
- Description workflow (SS7) goes live.
- `lookup=` parameter on `nbas-image`/`nbas-gallery` (SS5.6), contingent on confirming the right
  Hugo resource-resolution mechanism against the site's actual Hugo version.

**Phase 3 -- SSO extension**
- Reuses Phase 1/2 machinery. Adds `sso_*` fields and the `sso:` schema block.
- Resolves the open Ceres and interstellar-object questions (SS9.4-5) before/during this phase.

**Phase 4 -- Star extension**
- Reuses Phase 1/2 machinery. Adds `star_*` fields, the `star:` schema block, `components:`/
  `pairing_type:` for binaries, and the exoplanet class.
- Resolves the double-star symbol table and variable-star abbreviation questions (SS9.2-3).

**Deferred indefinitely:**
- Dedicated per-object Explorer imagery beyond reused/library-sourced images -- revisit after the
  GitHub Pages move.
- Retroactive rewrite of existing articles -- optional cleanup only, never required.
