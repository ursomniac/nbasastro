# NBASAstro — Article Production Checklist

**For AI agents and Bob:** This is a working checklist distilled from producing the Phoebe (Observing Challenges) and galaxy-inclination (AWV) articles. Meant to be pasted into or referenced alongside PHILOSOPHY.md / CLAUDE2.md. Update it as new failure modes show up — it exists specifically to catch the steps that get skipped once an article gets complicated.

---

## 1. Define the story before writing anything

- [ ] For ACL/GS/WUS/etc: confirm the fixed formula for that series still applies.
- [ ] For AWV specifically: the article needs a real astronomical/astrophysical throughline, not just "N objects loosely grouped by season or constellation." If the working title doesn't imply a theme, stop and find one before drafting.
- [ ] Explicitly decide what the article is *not* about (e.g., "Fall" is a visibility filter, not a theme; constellation-based grouping belongs to Constellation Highlights, not AWV).
- [ ] Check upcoming schedule for object overlap with other planned articles (e.g., don't reuse an object already slated for a different series in the same season).

## 2. Research and fact-check — before drafting, not after

- [ ] Verify every technical/quantitative claim via search — magnitudes, sizes, distances, formulas, classifications, discovery history. Never draft numbers from memory into an article with the accuracy bar this site holds.
- [ ] Where sources disagree, keep the disagreement visible (a range, a footnote) rather than silently picking one.
- [ ] Flag anything that's a real, cited-but-uncertain claim (e.g., a debated origin theory, a discordant measurement) as uncertain in the text itself, not just in your own notes.

## 3. Object/image roster (AWV-style multi-object articles)

- [ ] Pull all candidate images before culling — identify/verify each one against its actual filename or catalog data, don't guess from a thumbnail.
- [ ] Watch for image-count mismatches (files present vs. images actually reviewed/discussed) and reconcile them explicitly rather than assuming a round number.
- [ ] Cull to a final roster with deliberate balance across sub-categories — check for pile-ups (e.g., 9 examples in one bucket, 1 in another) before locking the list.
- [ ] Within each sub-category, aim for both a "clean textbook example" and a "test yourself" example with a genuine point of comparison.
- [ ] Reconcile the final roster count in the article's own prose (e.g., "fifteen images" vs. "seventeen galaxies" when some images contain paired/interacting objects) — don't leave an implied number that doesn't match the actual content.

## 4. Media pipeline

- [ ] **Archive the raw media before compressing for the site.** Keep an unmodified copy of every original image/exposure somewhere durable, separate from the web-ready compressed version — full-resolution originals are the thing you can't regenerate later (this matters even more if a "collected articles into a book" project ever happens).
- [ ] Compress/convert to the site's web format (currently WEBP) at appropriate dimensions — don't ship an oversized file just because the source was large.
- [ ] **Create a banner/hero image.** This is the single most commonly forgotten step once an article's content gets complicated — check for it explicitly before considering the article done, don't assume it'll get remembered along the way.
- [ ] Create a thumbnail image.
- [ ] Confirm all image paths referenced in the article body actually exist in the expected directory (e.g., `WEBP/`) — a broken path fails silently in a way that's easy to miss in a text review.

## 5. Front matter

- [ ] Confirm field names against the site's actual schema rather than copying from a different series' article on autopilot (e.g., `author` vs `authors` has appeared inconsistently — verify which the templates expect).
- [ ] Fill in `description` for real before publishing — a placeholder is fine mid-draft but should never survive to publish.
- [ ] Double-check any hand-typed array/list front matter (missing commas, mismatched brackets) — this is regular YAML/TOML syntax, not Hugo-specific, but it's an easy silent breakage.
- [ ] Remove or intentionally adapt any boilerplate carried over from a copy-pasted scaffold (e.g., a stray `finder_charts` block referencing a different article's objects).

## 6. Drafting

- [ ] AWV articles: expect a "mostly full first pass," then iterative add/delete/move/alter passes — don't try to perfect one section before moving to the next.
- [ ] ACL/formula-driven articles: linear section-by-section drafting works better, since the structure is already fixed.
- [ ] Keep prose consistent with PHILOSOPHY.md's voice: curious and direct, not academic, not breathless, accuracy non-negotiable, treat the reader as a capable adult.

## 7. Shortcode / rendering QA — do this before calling an article done

- [ ] **A markdown table needs its header-separator row** (`|---|---|...`) or it silently renders as plain text through *any* Hugo shortcode wrapper — this isn't shortcode-specific, it's basic CommonMark/GFM table syntax, but it's an easy miss.
- [ ] `{{< article-table >}}` specifically needs a **blank line immediately after the opening tag** (apparently a leftover artifact from a title parameter used in an earlier article) — leave that blank line even though it looks unnecessary.
- [ ] Actually preview-render the article locally before treating a rendering issue as fixed — don't assume a syntax change worked just because it looks plausible in the source.
- [ ] If a shortcode does something unexpected, don't guess at Hugo internals — check the actual shortcode template file, or flag it as unverified in the response rather than asserting confidence.

## 8. Sync / file-handling discipline

- [ ] When re-uploading an edited draft, use a distinct filename (or confirm the AI agent is reading the newest file by timestamp) — stale files with identical names are the single biggest source of "why doesn't this match what I see" confusion on this project.
- [ ] Before making further edits, the agent should explicitly verify it's working from the current version, not assume.

## 9. Pre-publish pass

- [ ] Full read-through for factual accuracy, one more time, after all the piecemeal edits.
- [ ] Confirm every "how many X" claim in the prose still matches the actual final content (roster size, image count, etc.) after all the back-and-forth edits.
- [ ] Confirm the banner/hero and thumbnail actually exist and are referenced correctly (see §4 — this is worth checking twice given how often it's forgotten).
