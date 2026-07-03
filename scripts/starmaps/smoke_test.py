a#!/usr/bin/env python3
"""
Smoke test for generate.py's compositing/branding/JPEG logic, bypassing the
real starplot render (which needs a JPL ephemeris download this sandbox can't
reach). Stubs _build_plot() to return a fake chart of the right resolution,
then runs the real generate() function unmodified so the header/footer/JPEG
code path gets exercised for real.
"""
import sys
from pathlib import Path
from datetime import date as date_cls

from PIL import Image, ImageDraw

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import generate as gen

# --- create placeholder branding assets (logo PNG + QR SVG) matching the ---
# --- real filenames/format now used: nbas-logo.png, nbas-qrcode.svg       ---
gen.ASSETS.mkdir(exist_ok=True)
gen.LOGO_PATH = gen.ASSETS / "nbas-logo.png"
gen.QR_PATH   = gen.ASSETS / "nbas-qrcode.svg"

logo = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
d = ImageDraw.Draw(logo)
d.ellipse((20, 20, 380, 380), fill=(255, 200, 60, 255))
logo.save(gen.LOGO_PATH)

# Real QR asset is an SVG -- write one directly to exercise the svglib/renderPM
# rasterization path in _load_icon(), not just the raster PNG path.
qr_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<rect width="100" height="100" fill="white"/>
<rect x="10" y="10" width="20" height="20" fill="black"/>
<rect x="70" y="10" width="20" height="20" fill="black"/>
<rect x="10" y="70" width="20" height="20" fill="black"/>
<rect x="45" y="45" width="10" height="10" fill="black"/>
</svg>'''
gen.QR_PATH.write_text(qr_svg)


# --- stub out the network-dependent render step ---
# Real PlotStyle objects (BLUE_MEDIUM, EVERGREEN_DARK_EXTENSION, etc.) don't
# need network/ephemeris access -- only the actual star/planet DATA calls
# (p.stars(), p.planets(), etc.) do. So we can pull the REAL background and
# milky-way colors straight from the style passed in, and only fake the
# star-scatter/constellation positions. That lets this stub actually verify
# the light vs. dark color fix (no more arbitrary fake navy/blue guesses).
def _style_colors(style):
    bg_rgb = style.figure_background_color.as_rgb_tuple()[:3]
    mw_rgb = style.milky_way.fill_color.as_rgb_tuple()[:3]
    return bg_rgb, mw_rgb


class FakeFig:
    def __init__(self, bg_rgb):
        self._bg_rgb = bg_rgb

    def get_facecolor(self):
        return (self._bg_rgb[0] / 255, self._bg_rgb[1] / 255, self._bg_rgb[2] / 255, 1.0)


class FakePlot:
    def __init__(self, resolution, style):
        self.resolution = resolution
        bg_rgb, self.mw_rgb = _style_colors(style)
        self.fig = FakeFig(bg_rgb)
        self.bg_rgb = bg_rgb

    def export(self, path, padding=0.0, format=None, pil_kwargs=None):
        # Simulate a starplot export: a square raster at the requested resolution,
        # using the REAL style's background + milky-way colors.
        size = self.resolution
        img = Image.new("RGB", (size, size), self.bg_rgb)
        d = ImageDraw.Draw(img)
        # scatter some "stars" (dark on light bg, light on dark bg)
        star_color = (20, 20, 30) if sum(self.bg_rgb) > 380 else (240, 240, 250)
        import random
        random.seed(42)
        for _ in range(2000):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            r = random.choice([1, 1, 1, 2, 2, 3])
            d.ellipse((x - r, y - r, x + r, y + r), fill=star_color)
        # the real milky-way fill color, semi-transparent over the real bg
        band = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        bd = ImageDraw.Draw(band)
        bd.line((0, size * 0.3, size, size * 0.7), fill=(*self.mw_rgb, 90), width=int(size * 0.18))
        img = Image.alpha_composite(img.convert("RGBA"), band).convert("RGB")
        fmt = format or (Path(path).suffix.lstrip(".") or "png").upper()
        if fmt.lower() in ("jpg", "jpeg"):
            img.save(path, format="JPEG", quality=(pil_kwargs or {}).get("quality", 90))
        else:
            img.save(path, format="PNG")


def fake_build_plot(observer, style, resolution=gen.CHART_RESOLUTION, include_planets=True):
    return FakePlot(resolution, style)


gen._build_plot = fake_build_plot

# generate.py calls plt.close(p.fig) to avoid leaking real matplotlib figures
# across a batch run -- but our FakeFig stub isn't a real Figure, so no-op
# this in the test rather than changing production code to accommodate a stub.
gen.plt.close = lambda *a, **k: None

# Keep the sidecar write inside the sandbox's output folder rather than
# reaching for a real ../data/ sibling that doesn't exist in this test env.
gen.SIDECAR_PATH = gen.OUTPUT / "starmap_slots.yaml"

# --- 1. legacy ad hoc mode (existing behavior, unchanged) ---
print("=== ad hoc (legacy) ===")
test_date = date_cls(2026, 7, 8)
gen.generate(test_date, make_pdf=True)

jpg = gen.OUTPUT / "2026-07-08.jpg"
pdf = gen.OUTPUT / "2026-07-08.pdf"
print()
print(f"JPG exists: {jpg.exists()}  size: {jpg.stat().st_size / 1024:.1f} KB" if jpg.exists() else "JPG MISSING")
print(f"PDF exists: {pdf.exists()}  size: {pdf.stat().st_size / 1024:.1f} KB" if pdf.exists() else "PDF MISSING")
im = Image.open(jpg)
print(f"JPG dimensions: {im.size}")

# --- 2. tier 2/3 slot-shifting mode ---
print("\n=== --slots (tier 2/3) ===")
gen.generate_slots(weeks=5, make_pdf=True, start=date_cls(2026, 7, 8))

for i in range(1, 6):
    jpg = gen.OUTPUT / f"starmap-slot{i}.jpg"
    pdf = gen.OUTPUT / f"starmap-slot{i}.pdf"
    print(f"slot{i}: jpg={'OK' if jpg.exists() else 'MISSING'}"
          f"  pdf={'OK' if pdf.exists() else 'none (expected: only slot1)'}")

assert (gen.OUTPUT / "starmap-slot1.pdf").exists(), "slot1 (current) should have a PDF"
assert not (gen.OUTPUT / "starmap-slot2.pdf").exists(), "only slot1 should have a PDF"

print("\nsidecar contents:")
print(gen.SIDECAR_PATH.read_text())

# --- 3. tier 1 evergreen mode ---
print("=== --evergreen (tier 1) ===")
gen.generate_evergreen(year=2026)

evergreen_dir = gen.OUTPUT / "evergreen"
months = sorted(evergreen_dir.glob("*.jpg"))
print(f"\n{len(months)} evergreen files written (expect 24 = 12 months x light/dark):")
for m in months[:4]:
    print(f"  {m.name}")
print("  ...")

light = Image.open(evergreen_dir / "starmap-01-jan-light.jpg")
dark  = Image.open(evergreen_dir / "starmap-01-jan-dark.jpg")
print(f"\nlight dimensions: {light.size}  dark dimensions: {dark.size}")
# sanity check the dark variant really is inverted relative to light
lp = light.convert("RGB").getpixel((5, 5))
dp = dark.convert("RGB").getpixel((5, 5))
print(f"light corner pixel: {lp}  dark corner pixel: {dp}  (should look inverted)")

print("\nAll smoke tests completed.")
