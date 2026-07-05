# Finder Chart Refactor — Plan

Goal: mirror the starmap pattern. One branded JPG per finder chart, no separate PDF, kept printable.

## Current state (as of 2026-07-04)

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
