#!/usr/bin/env python3
"""
newsletter-pdf.py
Generates a print-quality PDF of an NBAS newsletter from a local Hugo server.

VERSION: 1.2.0  <-- bump this on every change. This is the number to quote
when reporting a bug or asking "is this the latest one" - it is also
printed to the console on every run and stamped into each PDF's Document
Properties (Producer field), so a generated file always tells you which
version of this script made it.

Version history:
  1.0.0  Original script (Playwright -> Chromium -> page.pdf(), JPEG
         recompression, volume/issue calculation).
  1.1.x  Iterative pagination patches (float handling, break-after rules) -
         not individually tracked, hence "something like v1.1.11."
  1.2.0  Real fixes, tracked from here on:
           - apply_auto_image_sizing(): images sized from real source pixel
             dimensions at AUTO_SIZE_DPI, capped per column, instead of
             trusting the website-oriented shortcode width.
           - prevent_heading_orphans(): a heading and whatever immediately
             follows it (image, paragraph, subheading - any type) are
             wrapped so a page break can't strand the heading alone.
           - neutralize_clear_shortcode(): the {{< clear >}} shortcode's
             inline clear:both is neutralized in print, so content doesn't
             wait on a much-taller sidebar float.
           - SCRIPT_VERSION + stamp_pdf_metadata(): this version block.

Usage:
    python scripts/newsletter-pdf.py <local-url> <article-directory>

Example:
    python scripts/newsletter-pdf.py \
        http://localhost:1313/articles/2026/07/july-2026-newsletter/ \
        content/articles/2026/07/nbas-newsletter-2607/

Requirements:
    pip install playwright python-frontmatter pikepdf
    playwright install chromium

Image size note:
    Chromium's page.pdf() doesn't embed your source image files - it
    rasterizes whatever's on the rendered page and re-encodes it as a
    lossless raw bitmap. That means the source image's format/compression
    (JPEG, WebP, PNG - doesn't matter) is discarded before the PDF step ever
    happens, and a full-width image gets rasterized at ~300 DPI regardless
    of its native resolution, which is where most of the file size comes
    from. So there is no "set up efficient source images and it stays
    efficient" option here - the bloat is structural to how Chromium prints
    a page to PDF, not a property of the source files.
    recompress_pdf_images() below runs automatically after every PDF is
    generated: it finds each raw/lossless embedded image, downsamples
    anything above IMAGE_MAX_LONG_EDGE, and re-encodes as JPEG - but only
    keeps the JPEG version if it's actually smaller than the original (a
    few small graphics, like icons, compress worse as JPEG and are left
    untouched). No per-image configuration is required; this is not tunable
    per run by design, so nobody has to remember to do it.

Image sizing note (rewritten 2026-08):
    Image *display* size in the PDF is handled separately from the file-size
    recompression above, by apply_auto_image_sizing() (see below). It reads
    each image's real source pixel dimensions from the rendered page
    (img.naturalWidth/naturalHeight) and converts them to PDF points at
    AUTO_SIZE_DPI, instead of trusting the width the nbas-image shortcode
    declares - that value is tuned for the live website's column width and
    has no fixed relationship to the print page's much narrower columns.
    Any image can still be manually sized via the `pdf.images` block in
    front matter (see apply_image_overrides); that always wins and
    auto-sizing skips it.

Pagination note (rewritten 2026-08):
    Chromium's page.pdf() does not paginate CSS "keep together" directives
    gracefully. Three specific patterns were causing large blank gaps,
    either mid-page or followed by content stranded alone on the next page:

      1. float: left/right on images - when a floated figure doesn't fit in
         the remaining space on a page, Chromium moves the whole float to
         the next page but does NOT reclaim the space it had reserved on
         the current page, leaving a blank gap behind.
         Fix: floats are kept (text still wraps beside align-left/right
         images), but apply_auto_image_sizing() caps every floated image to
         FLOAT_IMAGE_MAX_WIDTH_PCT of its column width *and*
         INLINE_IMAGE_MAX_HEIGHT_PT in height. A float that small is very
         unlikely to be taller than the remaining space on a page, which is
         what actually triggers the bug - but this is a mitigation, not a
         hard guarantee, since Chromium's float-break behavior isn't
         something CSS can fully control.

      2. A heading immediately followed by an image, where the image alone
         doesn't fit in the remaining page space: the heading renders at
         the bottom of the current page, and the (non-splittable) image
         moves whole to the next page, stranding the heading with blank
         space below it. h3 keeps its pre-existing break-after: avoid /
         page-break-after: avoid rule below (it hasn't caused problems), but
         that only stops a break *immediately after* an h3 with nothing
         between it and the next element - it does nothing for h2, and does
         nothing to keep a heading and the figure *after* it together as one
         unit. prevent_heading_orphans() (see below) fixes this directly: it
         wraps every heading that's immediately followed by a
         figure.nbas-media-container in a break-inside: avoid container, so
         Chromium either fits the whole heading+image pair on the current
         page or pushes the whole pair to the next one - never just the
         heading.

      3. Mismatched float heights under an explicit clear. The sidebar
         (.newsletter-stats-grid) and the Telescope Donation photo are both
         float: left, and the article content uses a `{{< clear >}}`
         shortcode right after the Donation section to force a clean
         full-width break before "Perseids". That's fine as long as the two
         floats are roughly the same height - which, before
         apply_auto_image_sizing() existed, they coincidentally were,
         because the Donation photo was rendering oversized (see the
         "Image sizing note" above) and happened to run about as tall as the
         sidebar. Now that the photo is correctly sized (a few inches, not
         most of the page), it finishes well before the much longer sidebar
         does, and clear: both still waits for the sidebar - leaving a
         multi-inch blank gap in the main column before "Perseids" can
         start.
         IMPORTANT: `{{< clear >}}` renders as a bare
         `<div style="clear: both;"></div>` with no class attribute at all -
         it is NOT `<div class="clear">`. An earlier version of this fix
         tried to neutralize it via a `.clear { clear: none }` rule in the
         print stylesheet; that rule matched nothing, since the element has
         no class to match, and an inline style always beats an external
         stylesheet rule regardless of !important anyway. The actual fix is
         neutralize_clear_shortcode() (see below), which finds that exact
         empty-div-with-inline-clear pattern in the DOM and clears the
         inline style property directly - the only thing that can override
         an inline style. Content after the Donation section now flows
         immediately once the Donation text ends, wrapping beside whatever's
         left of the sidebar rather than waiting for it - the same pattern
         most print newsletters use for a long-running sidebar. Worth a
         visual check after the sidebar list length changes issue to issue,
         since a very short sidebar plus a very tall floated image could in
         principle reverse which one "wins" - but that's a much smaller
         mismatch than what caused this bug.
"""

import io
import sys
import re
import calendar
import hashlib
import json
from pathlib import Path
from datetime import date, datetime

import frontmatter
import pikepdf
from PIL import Image
from playwright.sync_api import sync_playwright


# The real version number - see the "VERSION" line and "Version history" in
# the module docstring above. Bump this by hand every time this file
# changes. This is what gets printed on every run and stamped into every
# generated PDF's Document Properties.
SCRIPT_VERSION = "1.2.0"


def _script_build_fingerprint() -> str:
    """Secondary, auto-derived identifier: a short hash of this file's own
    source. This is NOT the version - SCRIPT_VERSION above is the number
    that matters and the one to quote. This is just a backstop in case
    SCRIPT_VERSION ever isn't bumped when it should have been (or a stale
    file gets passed around under an unchanged name): two files with
    identical SCRIPT_VERSION but different code will still show different
    fingerprints.
    """
    try:
        return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:10]
    except Exception:
        return "unknown"


SCRIPT_BUILD_FINGERPRINT = _script_build_fingerprint()

IMAGE_MAX_LONG_EDGE = 1500
IMAGE_JPEG_QUALITY = 82
INLINE_IMAGE_MAX_HEIGHT_PT = 160  # print-reasonable cap for images meant to float beside text

# ── Auto image sizing: real source pixels -> print points ──────────
# Governs every image that does NOT have an explicit override in the
# `pdf.images` front-matter block (see apply_image_overrides).
AUTO_SIZE_DPI = 150                # typical print DPI target for a home-printed newsletter
FLOAT_IMAGE_MAX_WIDTH_PCT = 0.40   # align-left/align-right images: never more than this share
                                    # of their column's width (ceiling agreed at 50%; kept a
                                    # bit under that to guarantee a readable text gutter)
CENTER_IMAGE_MAX_HEIGHT_PT = 240   # centered/unaligned images: matches the existing
                                    # full-width img max-height rule in build_css()


def recompress_pdf_images(pdf_path: Path, max_long_edge: int = IMAGE_MAX_LONG_EDGE, quality: int = IMAGE_JPEG_QUALITY) -> None:
    """Downsample and JPEG-recompress every raw/lossless image embedded in a
    PDF, in place. Images with real alpha transparency are left untouched
    (JPEG has no alpha channel). Any image where the JPEG version isn't
    actually smaller is left untouched too, so this can never make an
    individual image bigger. Runs automatically - no configuration needed."""
    pdf = pikepdf.open(pdf_path, allow_overwriting_input=True)
    touched = 0
    saved_bytes = 0

    for page in pdf.pages:
        if "/Resources" not in page or "/XObject" not in page["/Resources"]:
            continue
        for name, xobj in page["/Resources"]["/XObject"].items():
            if xobj.get("/Subtype") != "/Image":
                continue
            if str(xobj.get("/Filter")) != "/FlateDecode":
                continue  # already compressed (e.g. DCTDecode/JPEG) - nothing to gain

            try:
                pil = pikepdf.PdfImage(xobj).as_pil_image()
            except Exception:
                continue  # unusual colorspace/encoding - leave it alone rather than guess

            w, h = pil.size
            has_alpha = pil.mode in ("RGBA", "LA")
            real_alpha = False
            if has_alpha:
                real_alpha = pil.convert("RGBA").getchannel("A").getextrema()[0] < 255
            if real_alpha:
                continue  # would need to preserve transparency; JPEG can't, so skip

            long_edge = max(w, h)
            if long_edge > max_long_edge:
                scale = max_long_edge / float(long_edge)
                pil = pil.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)

            rgb = pil.convert("RGB")
            buf = io.BytesIO()
            rgb.save(buf, "JPEG", quality=quality, optimize=True)
            jpeg_bytes = buf.getvalue()

            old_len = int(xobj.get("/Length", 0))
            if len(jpeg_bytes) >= old_len:
                continue  # JPEG isn't actually smaller for this one - leave it alone

            xobj.write(jpeg_bytes, filter=pikepdf.Name("/DCTDecode"))
            xobj["/Width"] = rgb.width
            xobj["/Height"] = rgb.height
            xobj["/ColorSpace"] = pikepdf.Name("/DeviceRGB")
            xobj["/BitsPerComponent"] = 8
            if "/SMask" in xobj:
                del xobj["/SMask"]

            touched += 1
            saved_bytes += old_len - len(jpeg_bytes)

    pdf.save(pdf_path)
    pdf.close()
    print(f"  Recompressed {touched} image(s), saved {saved_bytes / 1024 / 1024:.2f} MB")


def stamp_pdf_metadata(pdf_path: Path, version: str, build_fingerprint: str, generated_at: str) -> None:
    """Embed the script version + generation timestamp into the PDF's own
    Document Properties, so opening ANY copy of a PDF - renamed, reuploaded,
    whatever - in any PDF viewer answers "which version of the script made
    this, and when" without depending on a filename or on memory of which
    fix came before which. This is the actual fix for "impossible to tell
    which of these is the most recent broken version": the answer now
    travels inside the file itself.

    Written to /Producer since every PDF viewer surfaces that field (macOS
    Preview's Get Info, Adobe's Document Properties, `pdfinfo`, etc.);
    duplicated into a couple of custom Info keys for anything that reads
    metadata programmatically.
    """
    pdf = pikepdf.open(pdf_path, allow_overwriting_input=True)
    pdf.docinfo["/Producer"] = (
        f"newsletter-pdf.py v{version} (build {build_fingerprint}) - generated {generated_at}"
    )
    pdf.docinfo["/NewsletterScriptVersion"] = version
    pdf.docinfo["/NewsletterBuildFingerprint"] = build_fingerprint
    pdf.docinfo["/NewsletterGeneratedAt"] = generated_at
    pdf.save(pdf_path)
    pdf.close()


# ── Volume/Issue calculation ─────────────────────────────────────
# Vol. 1 started October 2023. Resets each October.

def calc_volume_issue(dt: date) -> tuple[int, int]:
    anchor_year = 2023
    anchor_month = 10
    total_months = (dt.year - anchor_year) * 12 + (dt.month - anchor_month)
    volume = (total_months // 12) + 1
    issue  = (total_months % 12) + 1
    return volume, issue


def derive_pdf_filename(url: str) -> str:
    match = re.search(r'/(\d{4})/(\d{2})/', url)
    if not match:
        raise ValueError(f"Could not extract YYYY/MM from URL: {url}")
    return f"{match.group(1)}-{match.group(2)}_nbas-newsletter.pdf"


def derive_date(url: str) -> date:
    match = re.search(r'/(\d{4})/(\d{2})/', url)
    if not match:
        raise ValueError(f"Could not extract YYYY/MM from URL: {url}")
    return date(int(match.group(1)), int(match.group(2)), 1)


def load_pdf_meta(article_dir: Path) -> dict:
    index_path = article_dir / "index.md"
    if not index_path.exists():
        return {}
    post = frontmatter.load(str(index_path))
    return post.metadata.get("pdf", {}) or {}


GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Marcellus&"
    "family=Barlow+Condensed:wght@300;400;600&"
    "family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&"
    "display=swap"
)


def build_css(pdf_meta: dict) -> str:
    global_brightness = pdf_meta.get("brightness", 1.0)
    return f"""
@import url('{GOOGLE_FONTS_URL}');

*, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1a1a1a;
    background: white;
    width: 100%;
}}

body > *:not(#newsletter-root) {{
    display: none !important;
}}

#newsletter-root {{
    width: 100%;
}}

/* ── PRINT HEADER ── */
.print-header-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 0;
}}
.print-header-table td {{
    vertical-align: middle;
    padding: 0;
    border: none;
    background: white;
}}
.print-header-logo {{
    height: 72pt;
    width: auto;
    display: block;
}}
.print-header-qr-wrap {{
    text-align: center;
}}
.print-header-qr {{
    height: 72pt;
    width: 72pt;
    display: block;
}}
.print-header-qr-label {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 7pt;
    color: #888;
    display: block;
    text-align: center;
    margin-top: 2pt;
}}
.header-content-table {{
    width: 100%;
    border-collapse: collapse;
    text-align: center;
}}
.header-content-table td {{
    border: none;
    background: white;
    padding: 1pt 0;
}}
.header-h1 {{
    font-family: 'Marcellus', Georgia, serif;
    font-size: 16pt;
    color: #1a2a44;
    letter-spacing: 0.02em;
    line-height: 1.2;
}}
.header-tagline {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 9pt;
    color: #555;
    font-style: italic;
}}
.header-meta-left {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 8pt;
    color: #555;
    text-align: left;
    padding-top: 3pt;
}}
.header-meta-center {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 8pt;
    color: #1a2a44;
    text-align: center;
    font-weight: 600;
    letter-spacing: 0.04em;
    padding-top: 3pt;
}}
.header-meta-right {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 8pt;
    color: #555;
    text-align: right;
    padding-top: 3pt;
}}
.header-rule {{
    border: none;
    border-top: 2px solid #1a2a44;
    margin: 6pt 0 10pt 0;
}}

/* ── TWO-COLUMN LAYOUT ── */
.newsletter-stats-grid {{
    float: left;
    width: 27%;
    margin: 0 14pt 8pt 0;
    padding: 7pt 9pt;
    background: #f4f6f9;
    border: 1px solid #1a2a44;
    border-right: 2px solid #d4af37;
    border-radius: 3pt;
    overflow: visible;
}}

/* ── STATS SIDEBAR ── */
.stat-column {{
    margin-bottom: 9pt;
}}
.stat-column h4 {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 7.5pt;
    color: #1a2a44;
    border-bottom: 1px solid #d4af37;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4pt;
    padding-bottom: 2pt;
    background: transparent;
}}
.stat-list {{
    list-style: none;
    padding: 0;
    margin: 0;
}}
.stat-list li {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 8pt;
    border-bottom: 1px solid #eee;
    padding: 2pt 0;
    line-height: 1.3;
    background: transparent;
}}
.dso-sub {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 7.5pt;
    color: #222;
    margin-bottom: 4pt;
    line-height: 1.35;
    background: transparent;
}}
.dso-sub strong {{
    font-family: 'Barlow Condensed', sans-serif;
    color: #1a2a44;
    display: block;
    font-size: 7.5pt;
    background: transparent;
}}
.icon {{ font-family: emoji, sans-serif; margin-right: 3pt; }}

/* ── INTERACTING SIDEBAR SECTION ── */
.sidebar-interacting {{
    margin-top: 8pt;
    border-top: 1px solid #d4af37;
    padding-top: 6pt;
}}
.sidebar-interacting h4 {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 7.5pt;
    color: #1a2a44;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4pt;
    background: transparent;
    border-bottom: none;
}}
.sidebar-interacting p {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 7.5pt;
    line-height: 1.4;
    color: #222;
    margin-bottom: 3pt;
    background: transparent;
}}
.sidebar-interacting a {{
    color: #1a2a44;
    font-size: 7.5pt;
    word-break: break-all;
}}

/* ── ARTICLE BODY ── */
.article-body {{
    display: block;
    width: 100%;
}}

h2 {{
    font-family: 'Marcellus', Georgia, serif;
    font-size: 12pt;
    color: #1a2a44;
    border-bottom: 1px solid #d4af37;
    padding-bottom: 2pt;
    margin: 10pt 0 5pt 0;
}}

h3 {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 10pt;
    font-weight: 600;
    color: #1a2a44;
    margin: 7pt 0 3pt 0;
    break-after: avoid;
    page-break-after: avoid;
}}

p {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 10pt;
    line-height: 1.55;
    margin: 0 0 5pt 0;
    color: #1a1a1a;
}}

ul, ol {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 10pt;
    margin: 0 0 5pt 0;
    padding-left: 18pt;
}}

li {{
    font-size: 10pt;
    line-height: 1.45;
    margin-bottom: 2pt;
    color: #1a1a1a;
}}

blockquote {{
    border-left: 3px solid #d4af37;
    margin: 5pt 0 5pt 8pt;
    padding: 4pt 8pt;
    background: #f9f9f9;
    font-size: 9.5pt;
    font-style: italic;
    font-family: 'Source Serif 4', Georgia, serif;
}}

a {{
    color: #1a2a44;
    text-decoration: none;
}}

/* ── IMAGES ── */
/* Base: all images get global brightness */
img {{
    max-width: 100%;
    height: auto;
    filter: brightness({global_brightness});
}}

/* nbas-image figure containers */
figure.nbas-media-container {{
    margin: 6pt 0 !important;
}}

/* Floats are kept intentionally (text wraps beside align-left/align-right
   images). What keeps this from re-triggering the Chromium blank-gap
   pagination bug is apply_auto_image_sizing() in the Python step below,
   which caps every floated image's width/height so it's small enough to
   reliably fit remaining page space instead of overflowing onto the next
   page. See the "Pagination note" in the module docstring. */
figure.nbas-media-container.align-right {{
    float: right !important;
    margin: 0 0 8pt 10pt !important;
}}

figure.nbas-media-container.align-left {{
    float: left !important;
    margin: 0 10pt 8pt 0 !important;
}}

figure.nbas-media-container.align-center {{
    display: block !important;
    margin: 6pt auto !important;
    clear: both;
}}

figure.nbas-media-container.full-width {{
    width: 100% !important;
    clear: both;
}}

figure.nbas-media-container.full-width img {{
    width: 100% !important;
    max-height: 240pt;
    object-fit: contain;
    height: auto;
}}

/* Remove link styling around images */
figure.nbas-media-container a {{
    display: block;
    line-height: 0;
}}

figcaption,
.nbas-media-caption {{
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 8pt !important;
    color: #555 !important;
    font-style: italic;
    text-align: center !important;
    margin-top: 3pt;
    padding: 0 !important;
    clear: both;
    display: block;
}}

/* This rule is vestigial - kept only in case some future shortcode ever
   emits an actual class="clear" element. The real `{{{{< clear >}}}}`
   shortcode output has no class (see neutralize_clear_shortcode() in the
   Python step, and "Pagination note" item 3 in the module docstring),
   so this selector currently matches nothing. */
.clear {{ clear: none; display: block; }}
.float-table-left {{ float: none; width: auto; margin: 0 0 5pt 0; }}

/* ── TABLES ── */
table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9pt;
    margin: 4pt 0 7pt 0;
    font-family: 'Source Serif 4', Georgia, serif;
}}
th {{
    background: #1a2a44;
    color: white;
    padding: 3pt 6pt;
    font-size: 8.5pt;
    font-family: 'Barlow Condensed', sans-serif;
    text-align: left;
    letter-spacing: 0.04em;
}}
td {{
    padding: 2pt 6pt;
    border-bottom: 1px solid #ddd;
    color: #1a1a1a;
    background: transparent;
}}
tr:nth-child(even) td {{ background: #f4f6f9; }}

/* ── STARMAP NOTE ── */
.starmap-note {{
    border: 1px solid #d4af37;
    border-radius: 3pt;
    padding: 6pt 10pt;
    background: #f9f8f0;
    margin: 6pt 0;
    clear: both;
}}
.starmap-note p {{
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 9pt;
    color: #1a2a44;
    margin: 0;
}}

/* ── HIDE UNWANTED ELEMENTS ── */
.starmap-card,
.newsletter-card {{ display: none !important; }}

/* ── PRINT FOOTER ── */
.print-footer {{
    clear: both;
    border-top: 1px solid #1a2a44;
    margin-top: 14pt;
    padding-top: 4pt;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 8pt;
    color: #555;
    display: flex;
    justify-content: space-between;
}}
"""


def build_header_html(issue_date: date, volume: int, issue: int) -> str:
    month_year = f"{calendar.month_name[issue_date.month]} {issue_date.year}"
    return f"""
<table class="print-header-table">
  <tr>
    <td style="width:72pt; padding-right:8pt;">
      <img class="print-header-logo"
           src="http://localhost:1313/images/nbas-logo.png"
           alt="NBAS Logo">
    </td>
    <td>
      <table class="header-content-table">
        <tr>
          <td colspan="3" class="header-h1">Northern Berkshire Astronomical Society</td>
        </tr>
        <tr>
          <td colspan="3" class="header-tagline">Whatever your experience, you belong under our skies</td>
        </tr>
        <tr>
          <td class="header-meta-left">Founded 2023</td>
          <td class="header-meta-center">https://nbasastro.org/</td>
          <td class="header-meta-right">Volume {volume}, Issue {issue}</td>
        </tr>
      </table>
    </td>
    <td style="width:72pt; padding-left:8pt;">
      <div class="print-header-qr-wrap">
        <img class="print-header-qr"
             src="http://localhost:1313/images/qrcode.svg"
             alt="QR code">
        <span class="print-header-qr-label">nbasastro.org</span>
      </div>
    </td>
  </tr>
</table>
<hr class="header-rule">
"""


def build_meetings_html(pdf_meta: dict) -> str:
    meetings = pdf_meta.get("meetings", []) or []
    if not meetings:
        return ""
    items = "".join(f"<li>{m}</li>" for m in meetings)
    return f"""
<div class="sidebar-interacting">
  <h4>Upcoming Meetings</h4>
  <ul class="stat-list">{items}</ul>
  <p style="font-size:7pt; margin-top:3pt; color:#555;">1st Wed · 6 PM · North Adams Public Library</p>
</div>
"""


def build_interacting_html(pdf_meta: dict) -> str:
    interacting = pdf_meta.get("interacting", {}) or {}
    if not interacting:
        # Default fallback
        return """
<div class="sidebar-interacting">
  <h4>Interacting</h4>
  <p>Check out our Facebook Group</p>
  <p><a href="https://www.facebook.com/groups/nberkastro">facebook.com/groups/nberkastro</a></p>
</div>
"""
    lines = []
    if interacting.get("facebook"):
        lines.append(f'<p>Facebook: <a href="{interacting["facebook"]}">{interacting["facebook"]}</a></p>')
    if interacting.get("reddit"):
        lines.append(f'<p>Reddit: <a href="{interacting["reddit"]}">{interacting["reddit"]}</a></p>')
    for item in interacting.get("custom", []):
        lines.append(f'<p>{item}</p>')
    return f"""
<div class="sidebar-interacting">
  <h4>Interacting</h4>
  {''.join(lines)}
</div>
"""


def build_footer_html() -> str:
    return """<div class="print-footer">
  <span>NBAS Newsletter</span>
  <span id="page-num"></span>
</div>"""


def apply_image_overrides(page, pdf_meta: dict) -> None:
    """Apply per-image width and brightness from YAML.

    width and max-height YAML values are in PDF points (pt).
    Playwright renders at 96 dpi; 1 pt = 96/72 CSS px.

    Any image handled here is flagged with fig.dataset.manualSize = '1' so
    apply_auto_image_sizing() (below) leaves it alone - a manual override
    always wins over automatic sizing.
    """
    PT_TO_PX = 96 / 72  # 1.3333...
    images_meta = pdf_meta.get("images", {}) or {}
    if not images_meta:
        return

    for filename, img_cfg in images_meta.items():
        brightness    = img_cfg.get("brightness")
        width_pt      = img_cfg.get("width")
        max_height_pt = img_cfg.get("max-height")

        # Convert pt → CSS px
        width_px   = round(width_pt      * PT_TO_PX) if width_pt      is not None else None
        max_height = round(max_height_pt * PT_TO_PX) if max_height_pt is not None else None

        img_styles = []
        if brightness is not None:
            img_styles.append(f"filter: brightness({brightness});")
        if width_px is not None:
            img_styles.append(f"width: {width_px}px;")
        if max_height is not None:
            img_styles.append(f"max-height: {max_height}px;")
            img_styles.append("width: auto;")
        if width_px is not None and max_height is None:
            img_styles.append("height: auto;")

        # brightness-only entries (e.g. sct-dark-*.webp) don't set a size,
        # so they should NOT block auto-sizing - only flag manualSize when
        # an actual dimension was given.
        has_size_override = width_px is not None or max_height is not None

        if not img_styles:
            continue

        img_style_str = " ".join(img_styles)

        fig_styles = []
        if width_px is not None and max_height is None:
            fig_styles.append(f"width: {width_px}px;")
            fig_styles.append("max-width: 100%;")
        if max_height is not None:
            fig_styles.append(f"max-height: {max_height}px;")
            fig_styles.append("width: auto;")
        fig_style_str = " ".join(fig_styles)

        # Hugo renames resized images: photo.png → photo_hu[hash]_WxH_resize_q75.png
        # Match on stem only so includes() survives the renamed URL.
        stem = filename.rsplit('.', 1)[0]

        page.evaluate(f"""(hasSizeOverride) => {{
            document.querySelectorAll('figure.nbas-media-container').forEach(fig => {{
                const img = fig.querySelector('img');
                if (img && img.src.includes('{stem}')) {{
                    img.style.cssText += ' {img_style_str}';
                    if ('{fig_style_str}') {{
                        fig.style.cssText += ' {fig_style_str}';
                    }}
                    if (hasSizeOverride) {{
                        fig.dataset.manualSize = '1';
                    }}
                }}
            }});
        }}""", has_size_override)


def apply_auto_image_sizing(page, dpi: int = AUTO_SIZE_DPI) -> None:
    """Size every image that wasn't manually overridden in YAML, using its
    real source pixel dimensions rather than the width the nbas-image
    shortcode declared for the *website* layout.

    For each eligible figure:
      1. Read the image's natural (source) pixel width/height.
      2. Convert that to PDF points at `dpi`: native_px / dpi * 72. This is
         the size the image would print at genuine print resolution.
      3. Cap that size against the column it will actually sit in:
           - align-left / align-right (floated) images are capped to
             FLOAT_IMAGE_MAX_WIDTH_PCT of the containing column's width,
             and to INLINE_IMAGE_MAX_HEIGHT_PT in height, so a float can
             never crowd out the text it's meant to sit beside, and is
             unlikely to be tall enough to trigger Chromium's float
             pagination bug.
           - centered/unaligned images are capped to CENTER_IMAGE_MAX_HEIGHT_PT
             so a single photo can't dominate a whole page.
      The DPI-correct size is only ever shrunk to fit - never enlarged, so
      small source images aren't blown up past their native resolution.

    full-width images and anything flagged fig.dataset.manualSize are left
    untouched (full-width already has its own sizing rule in build_css();
    manualSize means a YAML override already handled it).
    """
    PT_TO_PX = 96 / 72

    # Images must have finished loading before naturalWidth/naturalHeight
    # are meaningful.
    page.wait_for_function(
        """() => Array.from(document.querySelectorAll('figure.nbas-media-container img'))
            .every(img => img.complete && img.naturalWidth > 0)""",
        timeout=15000,
    )

    page.evaluate(
        """(cfg) => {
            const { dpi, ptToPx, floatMaxPct, floatMaxHeightPt, centerMaxHeightPt } = cfg;

            document.querySelectorAll('figure.nbas-media-container').forEach(fig => {
                if (fig.classList.contains('full-width')) return;
                if (fig.dataset.manualSize === '1') return;

                const img = fig.querySelector('img');
                if (!img || !img.naturalWidth || !img.naturalHeight) return;

                const isFloat = fig.classList.contains('align-left') ||
                                 fig.classList.contains('align-right');
                const parentPt = fig.parentElement.getBoundingClientRect().width / ptToPx;
                const aspect = img.naturalHeight / img.naturalWidth;

                // Steps 1+2: real source pixels -> print points at target DPI
                const nativeWidthPt = (img.naturalWidth / dpi) * 72;

                // Step 3: cap against the column, never upscale past native size
                let widthPt;
                if (isFloat) {
                    widthPt = Math.min(nativeWidthPt, parentPt * floatMaxPct);
                    const heightAtWidth = widthPt * aspect;
                    if (heightAtWidth > floatMaxHeightPt) {
                        widthPt = Math.min(widthPt, floatMaxHeightPt / aspect);
                    }
                } else {
                    widthPt = Math.min(nativeWidthPt, parentPt);
                    const heightAtWidth = widthPt * aspect;
                    if (heightAtWidth > centerMaxHeightPt) {
                        widthPt = centerMaxHeightPt / aspect;
                    }
                }

                const widthPx = widthPt * ptToPx;
                fig.style.setProperty('width', widthPx + 'px', 'important');
                fig.style.setProperty('max-width', '100%', 'important');
                img.style.setProperty('width', '100%', 'important');
                img.style.setProperty('height', 'auto', 'important');
                fig.dataset.autoSized = '1';
            });
        }""",
        {
            "dpi": dpi,
            "ptToPx": PT_TO_PX,
            "floatMaxPct": FLOAT_IMAGE_MAX_WIDTH_PCT,
            "floatMaxHeightPt": INLINE_IMAGE_MAX_HEIGHT_PT,
            "centerMaxHeightPt": CENTER_IMAGE_MAX_HEIGHT_PT,
        },
    )


def prevent_heading_orphans(page) -> None:
    """Wrap every heading together with whatever immediately follows it in a
    break-inside: avoid container, so Chromium's page.pdf() either fits the
    heading + that first element on the current page or pushes the whole
    pair to the next one - never just the heading, stranded alone with
    everything it introduces pushed to the following page. See "Pagination
    note" item 2 in the module docstring.

    Originally this only fired when the next sibling was an image
    (figure.nbas-media-container), which fixed "This Month's Image" but
    missed the same bug in a different shape: "Upcoming Events" (h2)
    immediately followed by "August 8th..." (h3), no image involved at all,
    still got orphaned the same way. A heading can be stranded by ANY kind
    of following content - a paragraph, a list, a subheading - so this now
    wraps a heading with its immediate next sibling regardless of type.

    Runs generically over every h2/h3 in the article, not just the cases
    seen so far - so future issues get the same protection without needing
    special-casing.
    """
    page.evaluate("""() => {
        document.querySelectorAll('.article-body h2, .article-body h3').forEach(h => {
            const next = h.nextElementSibling;
            if (!next) return;
            if (h.parentElement && h.parentElement.dataset.orphanGuard === '1') return;

            const wrapper = document.createElement('div');
            wrapper.dataset.orphanGuard = '1';
            wrapper.style.breakInside = 'avoid-page';
            wrapper.style.pageBreakInside = 'avoid';
            h.parentNode.insertBefore(wrapper, h);
            wrapper.appendChild(h);
            wrapper.appendChild(next);
        });
    }""")


def neutralize_clear_shortcode(page) -> None:
    """The `{{< clear >}}` content shortcode renders as a bare
    <div style="clear: both;"></div> - confirmed from the actual page
    source, not assumed - with no class attribute. It is NOT
    <div class="clear">, so a `.clear { clear: none }` rule in the print
    stylesheet cannot reach it: it has no class to match, and even if it
    did, an inline style always wins over an external stylesheet rule.

    This finds that exact pattern - an empty div whose only styling is an
    inline `clear` - and clears the inline property directly, which is the
    only way to actually override it. See "Pagination note" item 3 in the
    module docstring for why this needs to happen at all (mismatched float
    heights between the sidebar and a now-correctly-sized floated image).

    Deliberately narrow: only touches empty divs with nothing but a `clear`
    inline style, so it can't accidentally neutralize `clear: both` on
    unrelated elements (e.g. figcaption, .align-center figures) that need
    to keep it.
    """
    page.evaluate("""() => {
        document.querySelectorAll('div').forEach(div => {
            if (div.children.length !== 0) return;
            if (div.textContent.trim() !== '') return;
            if (!div.style.clear) return;
            div.style.clear = 'none';
        });
    }""")


def generate_pdf(url: str, output_dir: str) -> None:
    output_path = Path(output_dir).resolve()
    if not output_path.exists():
        raise FileNotFoundError(f"Output directory does not exist: {output_path}")

    pdf_filename = derive_pdf_filename(url)
    pdf_path = output_path / pdf_filename
    issue_date = derive_date(url)
    pdf_meta = load_pdf_meta(output_path)

    calc_vol, calc_issue = calc_volume_issue(issue_date)
    volume = pdf_meta.get("vol", calc_vol)
    issue  = pdf_meta.get("issue", calc_issue)

    generated_at = datetime.now().isoformat(timespec="seconds")
    print(f"  newsletter-pdf.py v{SCRIPT_VERSION} (build {SCRIPT_BUILD_FINGERPRINT}, generated {generated_at})")
    print(f"  Loading:  {url}")
    print(f"  Output:   {pdf_path}")
    print(f"  Volume {volume}, Issue {issue}")

    temp_pdf_path = pdf_path.with_suffix(".tmp.pdf")

    meetings_html    = build_meetings_html(pdf_meta)
    interacting_html = build_interacting_html(pdf_meta)
    header_html      = build_header_html(issue_date, volume, issue)
    footer_html      = build_footer_html()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 816, "height": 1056})
        page.goto(url.rstrip("/") + "/", wait_until="domcontentloaded", timeout=60000)

        # Strip all existing CSS
        page.evaluate("""() => {
            document.querySelectorAll('link[rel="stylesheet"], style').forEach(el => el.remove());
        }""")

        # Rebuild body with only newsletter content
        page.evaluate(f"""() => {{
            const article = document.querySelector('article.nbas-article');
            if (!article) return;

            // Remove unwanted elements
            ['.article-header', '.series-navigation', '.related-articles',
             '.article-separator', '.social-share'].forEach(sel => {{
                const el = article.querySelector(sel);
                if (el) el.remove();
            }});

            // Find the stats grid and append interacting section to it
            const statsGrid = article.querySelector('.newsletter-stats-grid');
            if (statsGrid) {{
                statsGrid.insertAdjacentHTML('beforeend', `{meetings_html}`);
                statsGrid.insertAdjacentHTML('beforeend', `{interacting_html}`);
            }}

            // Replace Monthly Starmap section content with a note
            const h2s = article.querySelectorAll('h2');
            h2s.forEach(h2 => {{
                if (h2.textContent.includes('Starmap')) {{
                    // Remove everything after this h2 until end of content wrapper
                    // except the h2 itself — replace siblings after it
                    let next = h2.nextSibling;
                    while (next) {{
                        const toRemove = next;
                        next = next.nextSibling;
                        toRemove.remove();
                    }}
                    h2.insertAdjacentHTML('afterend', `
                        <div class="starmap-note">
                            <p>&#x2728; For {calendar.month_name[issue_date.month]}'s star chart, visit
                            nbasastro.org/starmap/ (this week, with planets) or
                            nbasastro.org/starmap/reference/ (any night, any year, no planets).</p>
                        </div>
                    `);
                }}
            }});

            const contentWrapper = article.querySelector('.article-content-wrapper');
            const content = contentWrapper ? contentWrapper.innerHTML : article.innerHTML;

            document.body.innerHTML = `
                <div id="newsletter-root">
                    {header_html}
                    <div class="article-body">
                        ${{content}}
                    </div>
                    {footer_html}
                </div>
            `;
        }}""")

        # Inject standalone CSS
        page.add_style_tag(content=build_css(pdf_meta))

        # Keep each heading glued to an image that immediately follows it,
        # so a page break can't strand the heading alone (see docstring).
        prevent_heading_orphans(page)

        # Neutralize the {{< clear >}} shortcode's inline clear:both so
        # content doesn't wait for the (much taller) sidebar float to end
        # before continuing - see "Pagination note" item 3 and this
        # function's own docstring.
        neutralize_clear_shortcode(page)

        # Apply per-image overrides from YAML (manual sizes always win)
        apply_image_overrides(page, pdf_meta)

        # Size every remaining image from its real pixel dimensions at
        # AUTO_SIZE_DPI, capped to fit its column (see docstring at top of
        # file and the function's own docstring for the full rationale).
        apply_auto_image_sizing(page)

        # Wait for fonts and images to settle
        page.wait_for_timeout(3000)

        page.pdf(
            path=str(temp_pdf_path),
            format="Letter",
            margin={
                "top":    "0.6in",
                "right":  "0.65in",
                "bottom": "0.65in",
                "left":   "0.65in",
            },
            print_background=True,
        )

        browser.close()

    # ── No starmap PDF appended, per issue #37 ──────────────────
    # The newsletter no longer bundles or appends a per-newsletter starmap
    # PDF. The in-content note above points readers to nbasastro.org/starmap/
    # instead, so the newsletter PDF stays exactly the size of the article
    # content itself.
    print("  Recompressing embedded images...")
    recompress_pdf_images(temp_pdf_path)

    stamp_pdf_metadata(temp_pdf_path, SCRIPT_VERSION, SCRIPT_BUILD_FINGERPRINT, generated_at)

    temp_pdf_path.rename(pdf_path)
    print(f"  Done: {pdf_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/newsletter-pdf.py <local-url> <article-directory>")
        sys.exit(1)
    generate_pdf(sys.argv[1], sys.argv[2])
