# -*- coding: utf-8 -*-
"""Compress format-practice images: resize + JPEG re-encode."""
import sys
from pathlib import Path
from typing import Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent / ".pydeps"))

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets/format-practice"
MAX_WIDTH = 1200
JPEG_QUALITY = 78
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}


def compress_one(path: Path) -> Tuple[int, int, Optional[str]]:
    """Return (before_bytes, after_bytes, new_name_or_none)."""
    before = path.stat().st_size
    ext = path.suffix.lower()

    with Image.open(path) as im:
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        elif im.mode != "RGB":
            im = im.convert("RGB")

        w, h = im.size
        if w > MAX_WIDTH:
            ratio = MAX_WIDTH / w
            im = im.resize((MAX_WIDTH, int(h * ratio)), Image.Resampling.LANCZOS)

        out = path.with_suffix(".jpg") if ext in (".bmp", ".png", ".gif", ".webp") else path
        im.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True)

    if out != path and path.exists():
        path.unlink()

    after = out.stat().st_size
    new_name = out.name if out != path else None
    return before, after, new_name


def main():
    total_before = total_after = 0
    converted = 0
    for path in sorted(ASSETS.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXT:
            continue
        try:
            before, after, new_name = compress_one(path)
            total_before += before
            total_after += after
            if new_name:
                converted += 1
            pct = (1 - after / before) * 100 if before else 0
            label = new_name or path.name
            print(f"  {label}: {before//1024}KB → {after//1024}KB ({pct:.0f}%↓)")
        except Exception as e:
            print(f"  SKIP {path.name}: {e}")

    saved = total_before - total_after
    print(f"\nTotal: {total_before/1024/1024:.1f}MB → {total_after/1024/1024:.1f}MB "
          f"({saved/1024/1024:.1f}MB saved, {converted} renamed to .jpg)")


if __name__ == "__main__":
    main()
