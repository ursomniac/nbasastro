#!/usr/bin/env python3
"""
media_efficiency.py - per-article media efficiency analyzer/fixer

Run against a Hugo page-bundle directory (a directory containing index.md
and its sibling media files, e.g. content/articles/2026/07/some-article/).

Detects media referenced via the nbas-image and nbas-gallery shortcodes
(and, as a backstop, any other literal filename reference in index.md,
e.g. frontmatter cover-image fields), flags:
  - unreferenced files (present on disk, not used anywhere in index.md)
  - oversized files (long edge exceeds --ceiling pixels)
  - format-inefficient files (PNG/BMP/TIFF photos with no real alpha
    channel that would be smaller as JPEG/WebP)

Report mode (default) only prints findings. --fix actually resizes /
reformats files, rewrites index.md if a filename changes, deletes files
confirmed unreferenced, and reports savings.

Usage:
  python scripts/media_efficiency.py <article-dir>
  python scripts/media_efficiency.py <article-dir> --fix
  python scripts/media_efficiency.py <article-dir> --fix --yes
  python scripts/media_efficiency.py <article-dir> --fix --format webp --ceiling 1600 --quality 82

Requires: Pillow (already in requirements.txt)
"""

import argparse
import re
import sys
from pathlib import Path

from PIL import Image

RASTER_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff"}
VECTOR_EXTS = {".svg"}
OTHER_TRACKED_EXTS = {".pdf"}
ALL_TRACKED_EXTS = RASTER_EXTS | VECTOR_EXTS | OTHER_TRACKED_EXTS

DEFAULT_CEILING = 1600  # long-edge px ceiling for click-through originals
DEFAULT_QUALITY = 82
DEFAULT_FORMAT = "jpeg"  # safe default; --format webp is opt-in

SHORTCODE_TAG_RE = re.compile(r"\{\{[%<]\s*(nbas-image|nbas-gallery)\s+(.*?)\s*/?\s*[%>]\}\}", re.DOTALL)
GALLERY_BLOCK_RE = re.compile(
    r"\{\{[%<]\s*nbas-gallery[^%>]*[%>]\}\}(.*?)\{\{[%<]\s*/\s*nbas-gallery\s*[%>]\}\}",
    re.DOTALL,
)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


def human_size(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f}{unit}" if unit != "B" else f"{int(n)}{unit}"
        n /= 1024


def parse_references(index_text):
    """Return dict: filename -> list of context tags, e.g. ['nbas-image'], ['nbas-gallery'], ['expand'], ['other']."""
    refs = {}

    def add(fname, tag):
        fname = fname.strip()
        if not fname:
            return
        refs.setdefault(fname, []).append(tag)

    for m in SHORTCODE_TAG_RE.finditer(index_text):
        tag, attrs_str = m.group(1), m.group(2)
        attrs = dict(ATTR_RE.findall(attrs_str))
        if tag == "nbas-image":
            if "src" in attrs:
                add(attrs["src"], "nbas-image")
            if "expand" in attrs:
                add(attrs["expand"], "expand")
        # nbas-gallery attrs (style/size/title) carry no filenames; handled below via block body

    for m in GALLERY_BLOCK_RE.finditer(index_text):
        body = m.group(1)
        for line in body.splitlines():
            line = line.strip().strip("\r")
            if not line:
                continue
            parts = line.split("|")
            fname = parts[0].strip()
            add(fname, "nbas-gallery")

    return refs


def find_literal_backstop_refs(index_text, filenames_not_yet_referenced):
    """Catch frontmatter fields or other literal mentions of a filename not
    picked up by shortcode parsing."""
    found = set()
    for fname in filenames_not_yet_referenced:
        if fname in index_text:
            found.add(fname)
    return found


def _has_real_transparency(im):
    """True only if the image actually uses transparency somewhere, not
    merely if its pixel format includes an alpha channel. Many exported
    PNGs (chart renders, screenshots) are RGBA with alpha fixed at 255
    (fully opaque) everywhere - those must NOT be treated as needing
    alpha preservation, or they'll never get flagged as format-inefficient."""
    if im.mode in ("RGBA", "LA"):
        alpha = im.getchannel("A")
        return alpha.getextrema()[0] < 255
    if im.mode == "P" and "transparency" in im.info:
        converted = im.convert("RGBA")
        alpha = converted.getchannel("A")
        return alpha.getextrema()[0] < 255
    return False


def analyze_image(path):
    """Return dict with dims, format, has_alpha, is_animated, size for a raster file."""
    info = {
        "size": path.stat().st_size,
        "width": None,
        "height": None,
        "format": None,
        "has_alpha": False,
        "is_animated": False,
        "error": None,
    }
    try:
        with Image.open(path) as im:
            info["width"], info["height"] = im.size
            info["format"] = (im.format or path.suffix.lstrip(".").upper())
            info["is_animated"] = getattr(im, "is_animated", False)
            info["has_alpha"] = _has_real_transparency(im)
    except Exception as e:
        info["error"] = str(e)
    return info


def classify(path, rel, refs, ceiling):
    ext = path.suffix.lower()
    fname = rel
    referenced_via = refs.get(fname, [])
    flags = []

    if ext in OTHER_TRACKED_EXTS:
        if not referenced_via:
            flags.append("UNREFERENCED")
        return {
            "file": fname,
            "size": path.stat().st_size,
            "dims": None,
            "format": ext.lstrip(".").upper(),
            "referenced_via": referenced_via,
            "flags": flags,
            "fixable": False,
        }

    if ext in VECTOR_EXTS:
        if not referenced_via:
            flags.append("UNREFERENCED")
        return {
            "file": fname,
            "size": path.stat().st_size,
            "dims": None,
            "format": "SVG",
            "referenced_via": referenced_via,
            "flags": flags,
            "fixable": False,
        }

    info = analyze_image(path)
    if info["error"]:
        flags.append(f"UNREADABLE ({info['error']})")
        return {
            "file": fname,
            "size": info["size"],
            "dims": None,
            "format": ext.lstrip(".").upper(),
            "referenced_via": referenced_via,
            "flags": flags,
            "fixable": False,
        }

    if not referenced_via:
        flags.append("UNREFERENCED")

    long_edge = max(info["width"], info["height"])
    oversized = long_edge > ceiling
    if oversized:
        flags.append(f"OVERSIZED ({long_edge}px > {ceiling}px)")

    format_inefficient = (
        info["format"] in ("PNG", "BMP", "TIFF")
        and not info["has_alpha"]
        and not info["is_animated"]
    )
    if format_inefficient:
        flags.append(f"FORMAT ({info['format']} photo with no alpha - JPEG/WebP would be smaller)")

    if info["is_animated"]:
        flags.append("ANIMATED (left alone)")

    fixable = bool(referenced_via) and not info["is_animated"] and (oversized or format_inefficient)

    return {
        "file": fname,
        "size": info["size"],
        "dims": (info["width"], info["height"]),
        "format": info["format"],
        "referenced_via": referenced_via,
        "flags": flags,
        "fixable": fixable,
        "has_alpha": info["has_alpha"],
        "is_animated": info["is_animated"],
    }


def build_fix_plan(path, record, ceiling, target_format, quality):
    """Compute a candidate output in memory-adjacent temp file; return
    (new_path, new_size, changed_ext) without touching the original yet."""
    ext = path.suffix.lower()
    with Image.open(path) as im:
        im = im.convert("RGBA") if im.mode in ("P", "LA") and record["has_alpha"] else im.convert("RGB") if not record["has_alpha"] else im.convert("RGBA")
        w, h = im.size
        long_edge = max(w, h)
        if long_edge > ceiling:
            scale = ceiling / float(long_edge)
            new_w, new_h = int(round(w * scale)), int(round(h * scale))
            im = im.resize((new_w, new_h), Image.LANCZOS)

        if record["has_alpha"]:
            # keep a lossless-alpha-capable format; do not force JPEG (no alpha channel)
            out_format = "PNG" if target_format == "jpeg" else "WEBP"
            out_ext = ".png" if out_format == "PNG" else ".webp"
        else:
            out_format = "JPEG" if target_format == "jpeg" else "WEBP"
            out_ext = ".jpg" if out_format == "JPEG" else ".webp"
            if im.mode != "RGB":
                im = im.convert("RGB")

        new_path = path.with_suffix(out_ext)
        tmp_path = path.with_suffix(out_ext + ".tmp")
        save_kwargs = {"quality": quality, "optimize": True}
        if out_format == "WEBP":
            save_kwargs = {"quality": quality, "method": 6}
        im.save(tmp_path, out_format, **save_kwargs)

    new_size = tmp_path.stat().st_size
    changed_ext = out_ext != ext
    return tmp_path, new_path, new_size, changed_ext


def rewrite_index_references(index_path, index_text, old_name, new_name):
    """Replace old_name with new_name, but only whole-token matches - not
    where old_name occurs merely as a substring of a different, longer
    filename (e.g. "80mm+25mm.png" inside "06180130-moon-80mm+25mm.png").
    A blind str.replace() would corrupt that unrelated file's reference."""
    boundary = r"[\w./+-]"
    pattern = re.compile(r"(?<!" + boundary + r")" + re.escape(old_name) + r"(?!" + boundary + r")")
    updated = pattern.sub(new_name.replace("\\", "\\\\"), index_text)
    index_path.write_text(updated, encoding="utf-8")
    return updated


def safe_unlink(path):
    """Delete a file; on failure, warn and leave it in place rather than crash."""
    try:
        path.unlink()
        return True
    except OSError as e:
        print(f"  WARNING: could not delete {path.name} ({e}). Remove it manually.")
        return False


def main():
    ap = argparse.ArgumentParser(description="Analyze (and optionally fix) media efficiency in a Hugo article bundle.")
    ap.add_argument("directory", help="path to the article's page-bundle directory (containing index.md)")
    ap.add_argument("--fix", action="store_true", help="actually resize/reformat/clean up (default: report only)")
    ap.add_argument("--yes", action="store_true", help="skip confirmation prompts in --fix mode")
    ap.add_argument("--ceiling", type=int, default=DEFAULT_CEILING, help=f"long-edge px ceiling for originals (default {DEFAULT_CEILING})")
    ap.add_argument("--quality", type=int, default=DEFAULT_QUALITY, help=f"JPEG/WebP quality (default {DEFAULT_QUALITY})")
    ap.add_argument("--format", choices=["jpeg", "webp"], default=DEFAULT_FORMAT, help=f"target format for format-inefficient/oversized photos (default {DEFAULT_FORMAT})")
    args = ap.parse_args()

    directory = Path(args.directory).resolve()
    index_path = directory / "index.md"
    if not directory.is_dir():
        print(f"TASK FAILURE: not a directory: {directory}")
        sys.exit(1)
    if not index_path.is_file():
        print(f"TASK FAILURE: no index.md in {directory}")
        sys.exit(1)

    index_text = index_path.read_text(encoding="utf-8", errors="replace")
    refs = parse_references(index_text)

    # recurse into subdirectories (e.g. a gallery's own tts/ or slides/ folder) -
    # shortcodes reference those files by relative path (e.g. "tts/foo.jpg"),
    # so that's the identity used for matching, display, and index.md rewrites.
    media_files = sorted(
        (p, p.relative_to(directory).as_posix())
        for p in directory.rglob("*")
        if p.is_file() and p.name != "index.md" and p.suffix.lower() in ALL_TRACKED_EXTS
    )

    # backstop pass: catch any file not picked up by shortcode parsing but
    # literally named somewhere else in index.md (frontmatter fields etc.)
    unreferenced_candidates = [rel for _, rel in media_files if rel not in refs]
    backstop_hits = find_literal_backstop_refs(index_text, unreferenced_candidates)
    for fname in backstop_hits:
        refs.setdefault(fname, []).append("other-literal")

    records = [classify(p, rel, refs, args.ceiling) for p, rel in media_files]

    total_before = sum(r["size"] for r in records)
    print(f"Directory: {directory}")
    print(f"Files: {len(records)}   Total size: {human_size(total_before)}")
    print(f"Goal: < 2MB (ideal ~1MB)   {'MEETS IDEAL' if total_before <= 1_000_000 else ('MEETS GOAL' if total_before <= 2_000_000 else 'OVER GOAL')}")

    referenced_images = [r for r in records if r["referenced_via"] and r["format"] != "PDF"]
    if referenced_images:
        avg_img = sum(r["size"] for r in referenced_images) / len(referenced_images)
        print(f"Referenced images: {len(referenced_images)}   Avg size/image: {human_size(avg_img)}")
        print("  (the 2MB/1MB total is a rough guide - a gallery with many images will legitimately")
        print("   exceed it even when every image is already efficient; use the average above, not")
        print("   just the total, to judge whether the images themselves still need work)")
    print("-" * 100)
    for r in records:
        dims = f"{r['dims'][0]}x{r['dims'][1]}" if r["dims"] else "-"
        ref = ",".join(sorted(set(r["referenced_via"]))) if r["referenced_via"] else "-"
        flags = "; ".join(r["flags"]) if r["flags"] else "ok"
        print(f"{r['file']:<45} {human_size(r['size']):>9} {dims:>11} {r['format']:<6} ref=[{ref:<20}] {flags}")
    print("-" * 100)

    unreferenced = [r for r in records if "UNREFERENCED" in r["flags"]]
    fixable = [r for r in records if r["fixable"]]
    print(f"Unreferenced: {len(unreferenced)} file(s), {human_size(sum(r['size'] for r in unreferenced))}")
    print(f"Fixable (oversized/format): {len(fixable)} file(s), {human_size(sum(r['size'] for r in fixable))} currently")

    if not args.fix:
        print("\nReport only. Re-run with --fix to apply changes.")
        return

    print("\n--- FIX ---")
    text = index_text
    total_saved = 0

    if unreferenced:
        print(f"\nUnreferenced files ({len(unreferenced)}):")
        for r in unreferenced:
            print(f"  {r['file']}  ({human_size(r['size'])})")
        proceed = args.yes
        if not proceed:
            ans = input("Delete these unreferenced files? [y/N]: ").strip().lower()
            proceed = ans == "y"
        if proceed:
            for r in unreferenced:
                fp = directory / r["file"]
                size = fp.stat().st_size
                if safe_unlink(fp):
                    total_saved += size
                    print(f"  deleted {r['file']}")
        else:
            print("  skipped deletion")

    for r in fixable:
        fp = directory / r["file"]
        if not fp.exists():
            continue  # may have been deleted above if it was also unreferenced (shouldn't happen: fixable requires referenced)
        print(f"\n{r['file']}: {human_size(r['size'])}, {r['dims'][0]}x{r['dims'][1]}, {r['format']} -> flags: {'; '.join(r['flags'])}")
        tmp_path, new_path, new_size, changed_ext = build_fix_plan(fp, r, args.ceiling, args.format, args.quality)
        new_rel = new_path.relative_to(directory).as_posix()
        print(f"  proposed: {new_rel}  {human_size(new_size)}  (was {human_size(r['size'])}, saves {human_size(r['size'] - new_size)})")
        proceed = args.yes
        if not proceed:
            ans = input("  apply? [y/N]: ").strip().lower()
            proceed = ans == "y"
        if not proceed:
            safe_unlink(tmp_path)
            print("  skipped")
            continue

        old_size = fp.stat().st_size
        if changed_ext:
            tmp_path.rename(new_path)
            if safe_unlink(fp):
                text = rewrite_index_references(index_path, text, r["file"], new_rel)
                print(f"  wrote {new_rel}, removed {r['file']}, updated index.md")
            else:
                # old file couldn't be removed; still repoint index.md at the new
                # file since that's what should render going forward
                text = rewrite_index_references(index_path, text, r["file"], new_rel)
                print(f"  wrote {new_rel}, updated index.md ({r['file']} still on disk, see warning above)")
        else:
            tmp_path.rename(fp)
            print(f"  overwrote {r['file']} in place")
        total_saved += old_size - new_size

    final_total = sum(
        p.stat().st_size for p in directory.rglob("*") if p.is_file() and p.name != "index.md"
    )
    print(f"\nTotal saved: {human_size(total_saved)}")
    print(f"Directory total: {human_size(total_before)} -> {human_size(final_total)}")
    print(f"Goal: < 2MB (ideal ~1MB)   {'MEETS IDEAL' if final_total <= 1_000_000 else ('MEETS GOAL' if final_total <= 2_000_000 else 'OVER GOAL')}")


if __name__ == "__main__":
    main()
