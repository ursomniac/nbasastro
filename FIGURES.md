# FIGURES.md — How We Make Figures

For AI agents: read this before making any figure. It applies to all NBAS
work (articles, newsletters, and eventually the book).

---

## Principles

- **Accuracy first.** A wrong figure teaches the wrong thing faster than a
  wrong sentence. Every number, label, scale, and position in a figure goes
  through the same fact pass as the prose.
- **Code-generated, not drawn blind.** Figures are written as code, rendered,
  and visually checked before delivery. Never hand-write SVG coordinates
  without rendering and looking at the result.
- **No AI image generation** for scientific or technical figures. It produces
  plausible-looking geometry, labels, and numbers that are wrong — exactly the
  kind of content PHILOSOPHY.md exists to counter.
- **Reproducible.** Every figure can be regenerated from its source. Fixing a
  number is a one-line change, not a redraw.

## The Three Files

Every figure has one base name and three files:

| File                   | Purpose                                                    |
|------------------------|------------------------------------------------------------|
| `fig-<name>.py`        | Source: Python script (or `.tex` for TikZ, or a hand-edited `.svg` master) |
| `fig-<name>.svg`       | Vector version                                              |
| `fig-<name>.png`       | Raster version, ~2x display size for sharp screens          |

- Sources live **outside the Hugo repo**, in version control.
- SVG/PNG go in the article's page bundle alongside `index.md`.
- For print (the book), re-render at high resolution from the same source.

## Tools

- **matplotlib** — charts and most orbit/geometry diagrams.
- **astropy** — when positions should come from real ephemerides rather than
  idealized circles (e.g., Mars opposition geometry).
- **TikZ (LaTeX)** — clean textbook-style geometry (parallax triangle, parsec
  definition, transit geometry).
- **Inkscape** — the last 10%: when a figure is almost right, the author
  nudges a label by hand instead of another round-trip.

## Collaboration Loop

1. Author describes the figure in plain language (what it must show, what
   point it makes, where it goes).
2. Claude writes the source, renders it, looks at the output, and fixes
   problems.
3. Claude delivers all three files.
4. Author approves or marks up — uploading the PNG with notes or scribbles
   is fine.
5. Repeat 2–4 as needed. Small final tweaks: Inkscape.

## Quality Checks (before delivery)

- **Facts:** every number and label traceable to a verified source.
- **Legibility at actual display size:** check label and tick sizes at the
  article's display width, not full-screen zoom.
- **Accessibility:** colorblind-safe palette; never let color alone carry
  meaning (use labels, line styles, or markers too).
- **Alt text:** write real alt text describing what the figure shows (helps
  screen-reader users and SEO).

## Style — Two Layers

### Layer 1: render-time style (the figure file itself)
A shared matplotlib style file, `nbas.mplstyle` (fonts, colors, line
weights, label sizes), used for all matplotlib figures so the site and book
share one look. **Does not exist yet** — to be created from the first test
figure (candidate: Mars opposition geometry), then uploaded to project
knowledge. Until it exists, match the look of any previously approved
figure.

### Layer 2: site-side CSS (how the page presents the figure)
Consistent presentation of figures on the page: captions, spacing,
max-width/responsiveness, borders or backgrounds, and dark-mode behavior.
This lives in the Hugo theme's CSS and affects what `nbas-image` outputs.
**Not done yet.**

Key technical constraint (verify before relying on it): page CSS can only
restyle an SVG's internals if the SVG is inlined in the HTML. If
`nbas-image` embeds SVGs via an `<img>` tag, page CSS cannot reach inside
the SVG — the SVG's own colors are what display. That decides how dark mode
has to be handled.

## Open Decisions

- [ ] Does the site have a dark mode? If yes, figures need a strategy
      (transparent backgrounds with colors that work on both, separate
      light/dark renders, or inline SVG themed by CSS).
- [ ] How does `nbas-image` embed SVG — `<img>` or inline? (Author believes
      SVG support was retrofitted; test with one SVG on a draft page.)
- [ ] Should SVG text stay as text (so it's searchable and could pick up
      site fonts) or be converted to paths (so it looks identical
      everywhere)? matplotlib has a setting for this (`svg.fonttype`) —
      verify behavior at https://matplotlib.org/stable/users/explain/customizing.html
      before choosing.
- [ ] Create `nbas.mplstyle` from the first test figure.
- [ ] Draft site-side figure CSS once the dark-mode and embedding questions
      are answered.
