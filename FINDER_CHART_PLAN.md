# Finder Chart Refactor — Plan

Goal: mirror the starmap pattern. One branded JPG per finder chart, no separate PDF, kept printable.

## STATUS: Done, as of 2026-07-05

All items in the work breakdown below are complete:
- `finder_charts.py` rewritten: single branded JPG output (`_make_branded_jpg`, replacing `_make_png`/`_make_pdf`), raw chart is now a transient tempfile (never written into the output dir), `--output-dir` points directly at `<article-dir>/finder/`. Also: removed the legacy `FIELDS`/`--fields` mode, fixed a real bug in the high-declination (StereoNorth) path near the pole, added brightest/faintest-aware star marker sizing, and pointed the shared ephemeris at `scripts/assets/de421.bsp` (deduped from a separate copy that used to live in this script's own directory).
- `finder-chart-set.html` rewritten: single branded image display (like `nbas-image`), no PDF/PNG buttons, reads `{name, image, caption}` per chart. **Not verified against a real Hugo build** — no Hugo binary available in the session sandbox that did this work. Worth a `hugo server` sanity check before trusting it live.
- Frontmatter shape settled: `{name, image, caption}` per chart, dropping `raw`/`png`/`pdf`. The `title`/`intro` top-level fields some articles had were dropped too — turned out the old shortcode never actually read them, so they were dead frontmatter.
- All 4 existing articles migrated (`object-c12`, `object-gliese-710`, `ink-spot-and-cluster`, `old-star-clusters` — 10 chart entries total across the four, since `old-star-clusters` has 7). Migration was done as a **repackage**, not a regeneration: existing branded PNG/WebP charts were converted to JPG via PIL and moved into each article's new `finder/` subdirectory; old `raw`/`pdf`/branded-original files deleted. The underlying star data and chart layout are unchanged from before — this only changed the storage/output format. (Note: at migration time, contrary to what this doc previously said, all 4 articles' frontmatter still had the full `raw`/`png`/`pdf` fields intact and matching files on disk — no drift was actually present by the time this was tackled.)

Also since done:
- Directory renamed `finder/` → `printable/` across all 4 migrated articles (Bob's naming choice — reads better for a directory whose defining property is "stays real-format/full-res for printing," not "only used by finder charts").
- `media_efficiency.py` now auto-exempts any directory named `printable` (constant `DEFAULT_PRINT_DIR`, overridable via `--print-dir NAME`, disable entirely with `--no-print-dir-skip`) from resize/reformat — verified against both `object-c12` (1 exempt file) and `old-star-clusters` (7 exempt files across subdirectories, while confirming the *other* WebP images living in those same subdirectories, e.g. CMD diagrams, still get normal FORMAT flagging — the match is scoped to the directory name, not "any file near a chart"). UNREFERENCED checking still runs on printable/ contents; only OVERSIZED/FORMAT/fixability are skipped.

Remaining, deliberately not done here:
- Regenerating any of the 4 charts for real (new star fetch, new branding pass) — the session that did this migration had no network access to SIMBAD/Vizier, so only repackaging was possible. If you want fresh charts (e.g. to pick up the new adaptive marker sizing), run `finder_charts.py --objects ...` locally.

## Original planning notes (superseded by STATUS above, kept for history)

### Current state (as of 2026-07-04)

**Generator**: `scripts/finder_charts/finder_charts.py`
- `make_raw_chart()` / `make_raw_chart_stereonorth()` produce an unbranded intermediate: `{slug}_raw.png`
- `apply_branding(raw_png, out_stem, title, subtitle)` (line ~858) then produces TWO branded outputs:
  - `_make_png(chart, title, subtitle, out_stem + ".png")`
  - `_make_pdf(chart, title, subtitle, out_stem + ".pdf")`
- Output directory defaults to the script's own directory (`--output-dir` flag, defaults to `HERE`), not the article bundle. Nothing currently writes into a per-article location automatically.

**Shortcode**: `layouts/shortcodes/finder-chart-set.html`
- Reads `.Page.Params.finder_charts.charts[]` frontmatter, each chart having `name`, `raw`, `png`, `pdf`, `caption` fields (plain filename strings, not Hugo resources - not run through `.Resize()`/`.Fill()` at all).
- Displays the **unbranded `raw` file inline** (`<img src="{{.raw}}">`), wrapped in a link to `.png`. Separately offers "Download PDF" (`.pdf`) and "View PNG" (`.png`) buttons.
- Note: today's display is backwards from the target — it shows the *unbranded* raw image and only offers the branded PNG as a click-through/download. The refactor should display the **branded** image directly, like nbas-image/starmap already do.

**4 articles currently use this** (frontmatter `finder_charts:` block): `content/articles/2026/07/object-c12`, `content/articles/2026/07/old-star-clusters`, `content/articles/2026/07/ink-spot-and-cluster`, `content/articles/2026/08/object-gliese-710`. All will need frontmatter + files migrated.

**⚠️ These 4 are NOT in a uniform state — checked directly on 2026-07-04, do not batch-migrate blindly:**
- `object-c12`: matches the pattern cleanly. `raw:`/`png:`/`pdf:` frontmatter fields present, files present (`ngc_6946_raw.jpg`, `ngc_6946.jpg`, `ngc_6946.pdf`), none WebP-converted yet.
- `object-gliese-710`: also matches cleanly (`gliese_710_raw.png`, `gliese_710.png`, `gliese_710.pdf`, matching frontmatter). Has one unrelated `.webp` file (`gl710-prob.webp`) that isn't part of the finder chart trio.
- `old-star-clusters`: frontmatter has **no** `raw:`/`png:`/`pdf:` fields anymore (already edited away from the old shape), and **every image in the directory is already `.webp`**, including whatever its finder chart was. Bob confirmed the finder-chart generator "has gone through several revisions away from the customization used for the extant finder charts" - this article is the clearest evidence of that drift. Needs manual inspection of what's actually there and what the current frontmatter is doing before deciding whether to regenerate or just rename/reformat in place.
- `ink-spot-and-cluster`: frontmatter also has no `raw:`/`png:`/`pdf:` fields, but the old-pattern files (`inkspot_raw.png`, `inkspot.png`, `inkspot.pdf`) are still sitting on disk. Frontmatter and files have already diverged here too.

Net: treat this as 4 separate, individual migrations, not one batch script. Two (`object-c12`, `object-gliese-710`) are straightforward. Two (`old-star-clusters`, `ink-spot-and-cluster`) need someone to first figure out what's actually being rendered today before deciding how to migrate them - the generator's "several revisions" of drift mean the current script may not faithfully reproduce what these two articles currently show.

## Target state (per Bob's spec)

1. One branded JPG per finder chart (no raw PNG, no PDF kept around).
2. No PDF output at all.
3. Output files live in a `finder/` subdirectory inside the article's page bundle (e.g. `content/articles/2026/07/object-c12/finder/ngc_6946.jpg`), so they stay printable (avoids the WebP-can't-print-in-Preview problem) and so `media_efficiency.py`'s planned `--print-dir` exemption (see below) can protect them from resize/reformat.
4. `index.md` frontmatter updated to point at the new `finder/...` path(s) - almost certainly collapsing the current `raw`/`png`/`pdf` three-field-per-chart shape down to a single `image:` (or similar) field.
5. `finder-chart-set.html` shortcode rewritten to match: single branded image, no PNG/PDF download buttons, path resolved under `finder/`.

## Work breakdown for next session

- [ ] Decide the new frontmatter shape for a chart entry (currently `{name, raw, png, pdf, caption}` → probably `{name, image, caption}`).
- [ ] Rewrite `apply_branding()` in `finder_charts.py` to emit a single branded JPG instead of separate `_make_png()`/`_make_pdf()` calls. Can likely reuse the same PIL compositing approach (and the cross-platform font-resolution fix) already built for starmaps in `scripts/starmaps/generate.py`'s `_composite_chart()`/`_load_font()`.
- [ ] Decide whether the unbranded `_raw.png` intermediate needs to exist as a real file at all going forward, or can stay purely in-memory/temp and never get written into the article bundle.
- [ ] Add an `--output-dir`-style option (or just always write) so the generator writes directly into `<article-dir>/finder/`, not its own script directory.
- [ ] Rewrite `finder-chart-set.html` to display the single branded JPG directly (matching nbas-image's own display pattern), remove the PDF/PNG button row.
- [ ] Migrate the 4 existing articles: regenerate or move their chart files into `finder/`, update frontmatter, delete the old raw/png/pdf trio.
- [ ] Implement the deferred `--print-dir` flag in `media_efficiency.py` (see task list item, already designed: fully exempt from resize/reformat, still scanned for orphaned files) alongside this, since the two are directly linked.
- [ ] Re-run `media_efficiency.py` report mode on the 4 migrated articles to confirm `finder/` is correctly excluded and nothing else regressed.

## Context carried over from this session (media/PDF efficiency work)

- `scripts/media_efficiency.py` and `scripts/site_size_report.py` exist and are working (recursive subdirectory support, newsletter-pdf shortcode awareness, substring-collision guard, PDF delete safety gate, format-relative-to-target flagging).
- `scripts/newsletter-pdf.py` now automatically recompresses embedded PDF images after generation (pikepdf-based, ~80% size reduction verified) - unrelated to finder charts directly, but same "PDF pipeline discards source image efficiency" lesson applies: don't assume a print PDF stays small just because its source images are small.
- Site-wide size crisis is resolved (~318.8MB deployed, room for 300+ articles / ~2028 runway) - this finder-chart work is no longer urgent, just next on the list.
