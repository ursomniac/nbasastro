# NBAS Starmap Refactor — Sequential Plan (starmap2 branch, local only)

Design record: GitHub issues #36 (three-tier architecture) and #37 (newsletter, depends on #36).
Nothing pushed, nothing merged, nothing deployed. Live site (main, commit 4fb0efd) is untouched.

Note on the earlier "8 steps": no verbatim record of that original numbering exists — it was
summarized during a context compaction rather than kept word-for-word. Rather than guess at
reconstructing it, this is a fresh plan built from the actual current state of the code,
verified directly (git diff, py_compile, yaml parse, file inspection, real script execution),
not from memory or prior status docs.

Rule for this plan: each step is done ALONE, then verified ALONE, before the next one starts.
No bundling. "Owner" says who can actually do the step — several require your machine, since
this sandbox has no Hugo binary, no external network, no git push credentials, and the repo's
.venv was built for macOS (Homebrew path), so Python here can't run generate.py's real deps.

---

## PHASE 0 — Baseline (done)
1. [x] Full audit of current branch vs main — diff stat, commit log, reflog, live-site fetch.
       Verified against your own `git status` / `git diff main...starmap2 --stat`.

## PHASE 1 — Repo hygiene (done, committed, confirmed)
2. [x] Untracked scripts/starmaps/__pycache__/generate.cpython-312.pyc; added __pycache__/ and
       *.pyc to .gitignore. Root cause: committed directly in 8870a32, no prior gitignore rule.
3. [x] Fixed scripts/starmaps/smoke_test.py — line 1 was literally `a#!/usr/bin/env python3`
       (confirmed byte-for-byte via xxd), a stray character corrupting the shebang. Fixed by you.
4. [x] Committed steps 2+3 as one isolated hygiene commit: 7f14797
       "HYGIENE: untrack __pycache__, fix .gitignore, fix corrupted shebang in smoke_test.py"
       Confirmed via `git log -1` on your machine.
5. [x] node_modules (1,357 files, predates this branch, traced to 3ddd2c8/ea54cb8) — confirmed
       no CI dependency on it being tracked (hugo.yml only runs `npx pagefind`, which
       auto-installs). Added to .gitignore, untracked via `git rm -r --cached`, committed
       separately (a26aa53). Will be gone from the active repo once this branch merges.

## PHASE 2 — Verify each existing piece in isolation (done)
6. [x] generate.py: actually executed on your machine (not just read/compiled) —
       `--evergreen` produced 24 files (12 months × light/dark, ~650-700KB each, matches spec),
       `--slots --pdf` produced 5 slots, only slot1 got a PDF (matches tier-2-only design).
       Zero errors. Confirmed real, not guessed.
       Minor stale artifact found (not fixed, flagged): generate.py lines 517-518 print
       "list.html doesn't read this file yet" — no longer true, list.html was rewritten. Leftover
       message from before that rewrite, harmless but inaccurate. Not yet corrected.
7. [x] list.html (original tier-2/3 dropdown logic): confirmed rendering correctly via your
       screenshot. Redundant-header "issue" closed as intentional (branding-on-images decision).
8. [x] reference.html + content/starmap/reference.md: confirmed on your machine via
       `hugo server -D` — all 12 months show, thumbnails link correctly, dark-mode toggle works.
9. [x] hugo.yml: valid YAML (checked directly with a parser). --pdf flag addition confirmed
       safe (generate_slots() gates PDF to slot 1 only — checked in code). Full CI behavior
       (Actions actually running this) still unverified — only provable in Phase 5, by pushing.

## PHASE 3 — Decisions (both made)
10. [x] Reference-link placement: your UX diagnosis — /starmap/ has one prominent entry point
        for the whole starmap section, and now two things on it that could visually compete
        (current map w/ planets vs. evergreen reference w/o planets), and the distinction
        between them isn't self-evident to a reader. Decision: a "teaser card" (thumbnail +
        explanatory copy naming the planets-vs-no-planets distinction directly + button),
        not just a styled link. Implemented in Phase 4 step 12.
11. [x] Scope: #37 IS in scope for this branch. Per user: #36/#37 were split into separate
        tickets only because they were separate steps in one plan; intention was always to do
        both here, close both together.
        Real numbers gathered for the newsletter-PDF sub-decision (still open, see step 15):
        - Shared evergreen JPG: ~650-700 KB each (confirmed by actually running generate.py).
        - Current per-newsletter bundled files (5 newsletters, PNG+PDF each): 7.2 MB total,
          inconsistent sizes (300 KB-1.8 MB per newsletter) — part of the original problem.

## PHASE 4 — Execute decisions from Phase 3
12. [x] Reference-link design, REVISED per user feedback on the first attempt (single thumbnail
        card looked too similar to the current-map UI, competed with it visually). Current
        version in layouts/starmap/list.html: a card headed "Monthly Star Charts" (no jargon
        like "evergreen" in user-facing copy), one-line description, then a 12-image mini-grid
        (one thumbnail per month, dark variant, deliberately grid-shaped so it reads as
        "browse by month" navigation rather than a second single-image UI), the whole grid is
        one link to /starmap/reference/, plus an explicit button below it.
        Also updated to match: content/starmap/reference.md's description no longer says
        "evergreen"; layouts/starmap/reference.html's toggle changed from a checkbox to two
        buttons ("Light on Dark" / "Dark on Light") behaving like radio buttons, defaulting to
        "Light on Dark" (dark variant) per user's reasoning: the weekly map above uses the
        LIGHT/print-friendly style (BLUE_MEDIUM, confirmed in generate.py's generate_slot()),
        so defaulting the reference grid to the opposite (dark) style visually signals "this is
        a different, separate set of images" rather than repeating what they just saw.
        Brace/comment balance checked with a script (56/56, 8 end/8 needed) on list.html;
        reference.html checked too (26/26, 2 end/2 needed) — NOT YET build-verified against
        real Hugo.
        Build-verified on your machine — confirmed working. Follow-up fix also applied and
        confirmed: month labels on the reference grid (January, February, etc.) changed from
        #8a9cb3 to var(--gold-base) (#f8d44e, the site's actual nav/explore gold token, found in
        assets/css/01-variables.css rather than guessed). Step 12 CLOSED.
13. [x] layouts/shortcodes/starmap.html rewritten: derives month from .Page.Date, references
        canonical /starmap/evergreen/starmap-{MM-mon}-light.jpg, links to /starmap/ for
        current-sky-with-planets. Old file=/month=/invert= params no longer read (existing
        newsletter shortcode calls need no edits, per #37). Print-download links straight to
        the JPG, not a bundled PDF, per #36's own "PDF twin is redundant" principle.
        NOT YET build-verified against real Hugo.
        Build-verified on your machine via screenshot — July chart, title, button, and link all
        correct. One inconsistency found during that verification and fixed: the shortcode's own
        description still said "Evergreen chart (no planets)" — same wording bug as reference.md/
        reference.html, just missed in this file. Fixed. Step 13 CLOSED.
14. [x] Deleted all old bundled per-newsletter starmap PNG/PDF files: 2511 (1 file), 2604 (2),
        2605 (2), 2606 (2), 2607 (2) = 9 files total. Confirmed via `git status --short` showing
        exactly these as deleted, nothing else touched. Note: content/articles/2026/06/
        starmap-announcement, content/newsflash/starmap.md, and the constellations/cepheus
        test file were correctly left alone — not part of this cleanup. Step 14 CLOSED.
15. [x] Newsletter-PDF embed decision: Option A, per user — remove the embedded/appended starmap
        entirely, just point to the site. Checked the actual mechanism in scripts/newsletter-pdf.py
        first (it wasn't embedding an image inline — it was appending the whole per-newsletter
        starmap-{YYMM}.pdf as extra page(s) via pypdf, after replacing the in-content section
        with a "the map is attached as the next page" note). Changed: the note now reads
        "For {month}'s star chart, visit nbasastro.org/starmap/ ... or .../starmap/reference/ ..."
        instead of promising an attached page; removed the whole append-starmap-PDF block,
        replaced with a direct `temp_pdf_path.rename(pdf_path)`; removed the now-unused
        `from pypdf import PdfWriter, PdfReader` import (confirmed via grep: pypdf isn't used
        anywhere else in scripts/); removed pypdf from the script's own Requirements docstring
        and from requirements.txt. py_compile passes.
        Build-verified on your machine — confirmed: PDF generates, no starmap page appended,
        in-content note text correct. Step 15 CLOSED.

## FLAGGED — separate future initiative, NOT part of this branch's plan
- Site-wide image/media size constraint problem, raised while testing newsletter-pdf.py:
  the generated PDF came back ~6MB even though the actually-used source images in that one
  newsletter total only ~2MB (confirmed: checked index.md's actual image references directly).
  The "light on dark" appearance reported alongside it was investigated and RULED OUT as a real
  bug: confirmed by user (checked Preview.app / browser dark-mode setting) — it was Chrome's
  PDF.js viewer auto-dark-mode display setting inverting the view, not the actual PDF content.
  build_css()'s `body { background: white }` is correct as-is. No code change needed for that
  part. The file-size question (~6MB vs ~2MB of actually-used source images) is still open and
  still belongs in its own future plan, not bolted onto #36/#37.
  Additional data point from user: ran `sips` to shrink the 3 source photos in the July
  newsletter directly — PDF output size was unaffected, still ~6MB. Confirms the bloat is NOT
  primarily coming from source image file size on disk; something structural in the Playwright
  print-to-PDF pipeline itself (fonts, image re-rasterization, etc.) is the real cause. Strengthens
  the case this needs real investigation as its own project, not a source-image resize.

## PHASE 5 — Integration (only after every step above is done and verified — not before)
16. [x] Final full-branch check done. All committed: 7f14797 (hygiene), 7be3a35 (main starmap
        refactor + #37 work), a26aa53 (node_modules untrack). Confirmed via `git log --oneline`
        on your machine — matches expected history exactly, main untouched at 4fb0efd. No open
        decisions remain (only the two explicitly-deferred future items: node_modules history
        cleanup — not needed, already untracked — and the newsletter-PDF file-size problem,
        which is its own future project).
17. [ ] YOU push starmap2 to GitHub (I have no push credentials — confirmed by trying).
18. [ ] Open the PR, watch the first Actions run specifically for the new "Generate current +
        upcoming starmaps" step — this is the first real-world test of generate.py's actual
        dependencies in a clean CI environment.
19. [ ] Merge to main only after that Actions run is green.

---
Current position: Phase 4 fully closed (steps 12-15 all done and verified). Next: Phase 5,
step 16 — final full-branch check before you push anything.
