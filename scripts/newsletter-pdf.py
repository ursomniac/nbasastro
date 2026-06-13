#!/usr/bin/env python3
"""
newsletter-pdf.py
Generates a print-quality PDF of an NBAS newsletter from a local Hugo server.

Usage:
    python scripts/newsletter-pdf.py <local-url> <article-directory>

Example:
    python scripts/newsletter-pdf.py \
        http://localhost:1313/articles/2026/07/july-2026-newsletter/ \
        content/articles/2026/07/nbas-newsletter-2607/

Requirements:
    pip install playwright python-frontmatter pypdf
    playwright install chromium
"""

import sys
import re
import calendar
import json
from pathlib import Path
from datetime import date

import frontmatter
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader


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
    break-after: avoid;
    page-break-after: avoid;
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

figure.nbas-media-container.align-right {{
    float: right !important;
    margin: 0 0 8pt 10pt !important;
    clear: right;
}}

figure.nbas-media-container.align-left {{
    float: left !important;
    margin: 0 10pt 8pt 0 !important;
    clear: left;
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

.clear {{ clear: both; display: block; }}
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

        page.evaluate(f"""() => {{
            document.querySelectorAll('figure.nbas-media-container').forEach(fig => {{
                const img = fig.querySelector('img');
                if (img && img.src.includes('{stem}')) {{
                    img.style.cssText += ' {img_style_str}';
                    if ('{fig_style_str}') {{
                        fig.style.cssText += ' {fig_style_str}';
                    }}
                }}
            }});
        }}""")


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
                            <p>&#x2728; The Monthly Starmap for {calendar.month_name[issue_date.month]} {issue_date.year} is attached as the next page of this newsletter.</p>
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

        # Apply per-image overrides from YAML
        apply_image_overrides(page, pdf_meta)

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

    # ── Append starmap PDF if present ───────────────────────────
    year_short   = str(issue_date.year)[2:]
    month_str    = f"{issue_date.month:02d}"
    starmap_name = f"starmap-{year_short}{month_str}.pdf"
    starmap_path = output_path / starmap_name

    writer = PdfWriter()
    reader = PdfReader(str(temp_pdf_path))
    for pg in reader.pages:
        writer.add_page(pg)

    if starmap_path.exists():
        print(f"  Appending starmap: {starmap_name}")
        for pg in PdfReader(str(starmap_path)).pages:
            writer.add_page(pg)
    else:
        print(f"  No starmap found at {starmap_path} — skipping")

    with open(pdf_path, "wb") as f:
        writer.write(f)

    temp_pdf_path.unlink()
    print(f"  Done: {pdf_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/newsletter-pdf.py <local-url> <article-directory>")
        sys.exit(1)
    generate_pdf(sys.argv[1], sys.argv[2])
