#!/usr/bin/env python3
"""
site_size_report.py - rank article directories by size, worst offenders first

Like `du -sh public/articles/* | sort -rh | head -20`, but:
  - walks page-bundle leaf directories (any dir containing an index.md),
    not just the top-level year/month folders
  - defaults to content/articles (the source you can actually act on;
    public/articles is a build artifact)
  - breaks each offender down by media type (image/pdf/other) so you can
    see what's actually driving the size, not just the total

Usage:
  python scripts/site_size_report.py
  python scripts/site_size_report.py --root content/articles --top 30
  python scripts/site_size_report.py --built            # scan public/articles instead
  python scripts/site_size_report.py --root content/finder_charts --top 10
"""

import argparse
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".svg"}
PDF_EXTS = {".pdf"}


def human_size(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f}{unit}" if unit != "B" else f"{int(n)}{unit}"
        n /= 1024


def find_bundles(root, index_filename="index.md"):
    """Return every directory under root that directly contains index_filename
    (i.e. a Hugo page bundle leaf). For --built mode there's no index.md, so
    fall back to treating each immediate child of root as a unit."""
    bundles = []
    if index_filename:
        for p in root.rglob(index_filename):
            bundles.append(p.parent)
    else:
        bundles = [p for p in root.iterdir() if p.is_dir()]
    return sorted(set(bundles))


def dir_breakdown(directory):
    total = 0
    images = 0
    pdfs = 0
    other = 0
    file_count = 0
    image_count = 0
    for p in directory.rglob("*"):
        if not p.is_file():
            continue
        file_count += 1
        size = p.stat().st_size
        total += size
        ext = p.suffix.lower()
        if ext in IMAGE_EXTS:
            images += size
            image_count += 1
        elif ext in PDF_EXTS:
            pdfs += size
        else:
            other += size
    return {
        "path": directory,
        "total": total,
        "images": images,
        "pdfs": pdfs,
        "other": other,
        "file_count": file_count,
        "image_count": image_count,
        "avg_image": (images / image_count) if image_count else 0,
    }


def main():
    ap = argparse.ArgumentParser(description="Rank article/media directories by disk size, worst offenders first.")
    ap.add_argument("--root", default=None, help="root directory to scan (default: content/articles, or public/articles with --built)")
    ap.add_argument("--built", action="store_true", help="scan public/articles (post-build output) instead of content/articles (source)")
    ap.add_argument("--top", type=int, default=20, help="how many offenders to show (default 20)")
    args = ap.parse_args()

    if args.root:
        root = Path(args.root).resolve()
        index_filename = "index.md" if not args.built else None
    elif args.built:
        root = Path("public/articles").resolve()
        index_filename = None
    else:
        root = Path("content/articles").resolve()
        index_filename = "index.md"

    if not root.is_dir():
        print(f"TASK FAILURE: not a directory: {root}")
        return

    bundles = find_bundles(root, index_filename)
    if not bundles:
        print(f"TASK FAILURE: no {'directories' if index_filename is None else index_filename + ' bundles'} found under {root}")
        return

    results = [dir_breakdown(b) for b in bundles]
    results.sort(key=lambda r: r["total"], reverse=True)

    grand_total = sum(r["total"] for r in results)
    print(f"Root: {root}")
    print(f"Bundles scanned: {len(results)}   Combined size: {human_size(grand_total)}")
    print(f"Showing top {min(args.top, len(results))} by size")
    print("-" * 110)
    print(f"{'directory':<55} {'total':>9} {'images':>9} {'pdfs':>9} {'other':>9} {'files':>6} {'avg/img':>9}")
    print("-" * 110)
    for r in results[: args.top]:
        rel = r["path"].relative_to(root.parent) if root.parent in r["path"].parents else r["path"]
        avg_str = human_size(r["avg_image"]) if r["image_count"] else "-"
        print(
            f"{str(rel):<55} {human_size(r['total']):>9} {human_size(r['images']):>9} "
            f"{human_size(r['pdfs']):>9} {human_size(r['other']):>9} {r['file_count']:>6} {avg_str:>9}"
        )
    print("-" * 110)
    over_goal = [r for r in results if r["total"] > 2_000_000]
    print(f"{len(over_goal)} of {len(results)} bundles exceed the 2MB goal (combined {human_size(sum(r['total'] for r in over_goal))})")
    print("(total size alone conflates 'many efficient images' with 'bloated images' - see")
    print(" the ranking below, sorted by average size per image instead, to tell them apart)")

    by_avg = [r for r in results if r["image_count"] > 0]
    by_avg.sort(key=lambda r: r["avg_image"], reverse=True)
    print()
    print(f"Same bundles, ranked by average size per image (top {min(args.top, len(by_avg))}):")
    print("-" * 80)
    print(f"{'directory':<55} {'avg/img':>9} {'images':>6}")
    print("-" * 80)
    for r in by_avg[: args.top]:
        rel = r["path"].relative_to(root.parent) if root.parent in r["path"].parents else r["path"]
        print(f"{str(rel):<55} {human_size(r['avg_image']):>9} {r['image_count']:>6}")


if __name__ == "__main__":
    main()
