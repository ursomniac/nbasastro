#!/usr/bin/env python3
"""
media_backlog.py - find the worst image offenders across the whole site,
so they can be fed one at a time to media_efficiency.py.

Companion to:
  site_size_report.py   - ranks bundles by TOTAL size (efficient or not)
  media_efficiency.py   - fixes ONE bundle (resize / reformat / clean up)

This script ranks bundles by how much is still LEFT TO FIX:
  legacy  = bytes in .jpg/.jpeg/.png/.bmp/.tif/.tiff (not yet WebP)
  over    = bytes in images whose long edge exceeds --ceiling px (any format,
            incl. WebP that was converted without resizing)
  gif     = bytes in .gif (animations; media_efficiency does not convert
            these -- listed separately for a later MP4/WebM decision)
Files under a 'printable' directory are skipped, matching
media_efficiency.py's default (print material stays full-res, real format).

Read-only: it never changes a file.

Usage:
  python scripts/media_backlog.py                     # top 25 bundles under content/
  python scripts/media_backlog.py --top 50
  python scripts/media_backlog.py --root content/articles/2024
  python scripts/media_backlog.py --ceiling 1600
  python scripts/media_backlog.py --static            # also scan static/ (not bundles)

Each listed bundle comes with the command to fix it, e.g.
  python scripts/media_efficiency.py content/articles/2024/05/x --fix --format webp
Run media_efficiency.py WITHOUT --fix first to see what it would do.

Requires: Pillow (already in requirements.txt). Pillow reads only the image
header for .size, so the scan is fast.
"""

import argparse
from pathlib import Path

from PIL import Image

LEGACY_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
RASTER_EXTS = LEGACY_EXTS | {".webp", ".gif"}
DEFAULT_CEILING = 1600     # same default as media_efficiency.py
PRINT_DIR = "printable"    # same default as media_efficiency.py
SKIP_NAMES = {".DS_Store"}


def human(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{int(n)}B" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024


def long_edge(path):
    try:
        with Image.open(path) as im:
            return max(im.size)
    except Exception:
        return 0


def scan_dir(directory, ceiling, recurse_into_bundles=True):
    """Tally one directory. For a bundle, include its subdirs (galleries etc.)
    but skip any 'printable' subtree."""
    t = {"path": directory, "legacy": 0, "over": 0, "gif": 0,
         "n_legacy": 0, "n_over": 0, "n_gif": 0, "worst": []}
    files = directory.rglob("*") if recurse_into_bundles else directory.iterdir()
    for p in files:
        if not p.is_file() or p.name in SKIP_NAMES:
            continue
        if PRINT_DIR in p.relative_to(directory).parts[:-1]:
            continue
        ext = p.suffix.lower()
        if ext not in RASTER_EXTS:
            continue
        size = p.stat().st_size
        if ext == ".gif":
            t["gif"] += size
            t["n_gif"] += 1
            continue
        is_legacy = ext in LEGACY_EXTS
        is_over = long_edge(p) > ceiling
        if is_legacy:
            t["legacy"] += size
            t["n_legacy"] += 1
        if is_over:
            t["over"] += size
            t["n_over"] += 1
        if is_legacy or is_over:
            t["worst"].append((size, p.name))
    t["backlog"] = sum(s for s, _ in t["worst"])  # each file counted once, legacy OR oversized
    t["worst"].sort(reverse=True)
    return t


def main():
    ap = argparse.ArgumentParser(description="Rank page bundles by remaining image backlog (non-WebP or oversized).")
    ap.add_argument("--root", default="content", help="where to look for page bundles (default: content)")
    ap.add_argument("--top", type=int, default=25, help="how many bundles to list (default 25)")
    ap.add_argument("--ceiling", type=int, default=DEFAULT_CEILING, help=f"long-edge px limit (default {DEFAULT_CEILING})")
    ap.add_argument("--static", action="store_true", help="also report static/ folders (fix these by hand)")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"TASK FAILURE: not a directory: {root}")
        return

    bundles = sorted({p.parent for p in root.rglob("index.md")})
    rows = [scan_dir(b, args.ceiling) for b in bundles]
    rows = [r for r in rows if r["backlog"] or r["gif"]]
    rows.sort(key=lambda r: r["backlog"], reverse=True)

    total_backlog = sum(r["backlog"] for r in rows)
    total_gif = sum(r["gif"] for r in rows)
    pending = [r for r in rows if r["backlog"]]
    print(f"Root: {root}   bundles scanned: {len(bundles)}   ceiling: {args.ceiling}px")
    print(f"Bundles still needing work: {len(pending)}   backlog: {human(total_backlog)}   (+ GIFs: {human(total_gif)})")
    print("-" * 104)
    print(f"{'bundle':<58} {'backlog':>9} {'legacy':>11} {'oversized':>11} {'gif':>9}")
    print("-" * 104)
    for r in pending[: args.top]:
        print(f"{str(r['path']):<58} {human(r['backlog']):>9} "
              f"{human(r['legacy']):>7}/{r['n_legacy']:<3} {human(r['over']):>7}/{r['n_over']:<3} "
              f"{human(r['gif']) if r['gif'] else '-':>9}")
        for size, name in r["worst"][:3]:
            print(f"    {human(size):>9}  {name}")
    print("-" * 104)
    print("Next (report first, then fix):")
    for r in pending[: min(5, args.top)]:
        print(f"  python scripts/media_efficiency.py {r['path']}")
        print(f"  python scripts/media_efficiency.py {r['path']} --fix --format webp")

    gifs = sorted((r for r in rows if r["gif"]), key=lambda r: r["gif"], reverse=True)
    if gifs:
        print()
        print("Largest GIF totals (not handled by media_efficiency.py):")
        for r in gifs[:10]:
            print(f"  {human(r['gif']):>9}  {r['n_gif']:>3} file(s)  {r['path']}")

    if args.static:
        print()
        print("static/ folders (not page bundles - fix by hand, then update references):")
        sdirs = sorted({p.parent for p in Path("static").rglob("*") if p.is_file() and p.suffix.lower() in RASTER_EXTS})
        srows = [scan_dir(d, args.ceiling, recurse_into_bundles=False) for d in sdirs]
        srows = [r for r in srows if r["backlog"]]
        srows.sort(key=lambda r: r["backlog"], reverse=True)
        for r in srows[:15]:
            print(f"  {human(r['backlog']):>9}  {r['n_legacy']:>3} legacy, {r['n_over']:>3} oversized  {r['path']}")


if __name__ == "__main__":
    main()
