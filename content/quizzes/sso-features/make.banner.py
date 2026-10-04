#!/usr/bin/env python3
"""Build the 1200x630 banner for the sso-features quiz.

A 4x3 contact sheet: one 300x210 tile per question image, in quiz order.

Usage:  python3 banner-sso-features.py <page-bundle-dir> [output.png]
Needs:  Pillow
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

W, H = 1200, 630
COLS, ROWS = 4, 3
TW, TH = W // COLS, H // ROWS          # 300 x 210
GUTTER = 4                             # px, drawn over the tile edges
GUTTER_COLOR = (11, 11, 15)
GREYSCALE = False                      # True: convert every tile to grey

# (file, centre-x, centre-y, width) -- all as fractions of the source image.
# The crop height follows from the tile's 300:210 shape.
TILES = [
    ("olympus-mons.jpg",            0.53, 0.50, 1.00),
    ("caloris.jpg",                 0.45, 0.47, 0.70),
    ("maxwell-montes.jpg",          0.50, 0.47, 0.80),
    ("io-pele.jpg",                 0.40, 0.58, 0.60),
    ("conamara-chaos.jpg",          0.50, 0.45, 0.95),
    ("enceladus-tiger-stripes.jpg", 0.45, 0.42, 0.85),
    ("kraken-mare.jpg",             0.50, 0.55, 1.00),
    ("verona-rupes.jpg",            0.55, 0.55, 0.90),
    ("sputnik-planitia.jpg",        0.50, 0.42, 1.00),
    ("occator.jpg",                 0.50, 0.52, 1.00),
    ("saturn-hexagon.jpg",          0.50, 0.56, 0.80),
    ("great-dark-spot.jpg",         0.50, 0.50, 1.00),
]


def tile(path, cx, cy, w):
    im = Image.open(path).convert("RGB")
    iw, ih = im.size
    cw = w * iw
    ch = cw * TH / TW
    if ch > ih:                        # too tall for the source: shrink
        ch = ih
        cw = ch * TW / TH
    x0 = min(max(cx * iw - cw / 2, 0), iw - cw)
    y0 = min(max(cy * ih - ch / 2, 0), ih - ch)
    im = im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch)))
    im = im.resize((TW, TH), Image.LANCZOS)
    if GREYSCALE:
        im = im.convert("L").convert("RGB")
    return im


def main():
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src / "banner.png"
    sheet = Image.new("RGB", (W, H), GUTTER_COLOR)
    for i, (name, cx, cy, w) in enumerate(TILES):
        sheet.paste(tile(src / name, cx, cy, w), ((i % COLS) * TW, (i // COLS) * TH))
    d = ImageDraw.Draw(sheet)
    g = GUTTER // 2
    for c in range(1, COLS):
        d.rectangle((c * TW - g, 0, c * TW + g - 1, H), fill=GUTTER_COLOR)
    for r in range(1, ROWS):
        d.rectangle((0, r * TH - g, W, r * TH + g - 1), fill=GUTTER_COLOR)
    sheet.save(out, optimize=True)
    print(out, sheet.size)


if __name__ == "__main__":
    main()
