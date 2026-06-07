# -*- coding: utf-8 -*-
"""Wrap mnemonic-book section in outer collapse (all 3 pages)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "pages/01-sw공학.html",
    "pages/02-sw테스트.html",
    "pages/03-경영컨설팅.html",
]

OPEN_OLD = re.compile(
    r'(<section class="panel mnemonic-book-section" id="mnemonic-book">\s*)'
    r'<h2>([^<]+)</h2>\s*'
    r'(<p class="subtle">[^<]+</p>\s*)'
    r'(<input class="mn-filter"[^>]+/>\s*)'
    r'<details class="mnemonic-book" open>\s*'
    r'<summary>📖 전체 두음 목록 접기/펼치기</summary>\s*'
    r'<div class="mnemonic-list">',
    re.DOTALL,
)

OPEN_NEW = (
    r'\1'
    r'<details class="mnemonic-book-wrap" open>\n'
    r'<summary><span class="mn-wrap-title">\2</span>'
    r'<span class="mn-wrap-hint">전체 접기/펼치기</span></summary>\n'
    r'<div class="mnemonic-book-body">\n'
    r'\3\4'
    r'<div class="mnemonic-list">'
)

CLOSE_OLD = re.compile(
    r'(</div>\s*)</details>\s*</section>\s*(?=<!--|\s*<section|\s*<article|\s*<div class="card)'
    r'(?=.*id="mnemonic-book")',
    re.DOTALL,
)


def patch_page(rel: str) -> bool:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if "mnemonic-book-wrap" in text:
        print(f"skip (already patched): {rel}")
        return False
    if not OPEN_OLD.search(text):
        print(f"skip (pattern not found): {rel}")
        return False

    text = OPEN_OLD.sub(OPEN_NEW, text, count=1)

    # Close inner details + add body/wrap closers before </section>
    marker = 'id="mnemonic-book"'
    idx = text.find(marker)
    if idx < 0:
        return False
    section_end = text.find("</section>", idx)
    if section_end < 0:
        return False
    section = text[idx:section_end]
    if section.count("</div>") < 1:
        return False
    # Replace last </div></details></section> chunk inside mnemonic book
    new_tail = "</div>\n</div>\n</details>\n</section>"
    text = text[:section_end] + new_tail + text[section_end + len("</section>") :]

    path.write_text(text, encoding="utf-8")
    print(f"patched: {rel}")
    return True


def main():
    for rel in PAGES:
        patch_page(rel)


if __name__ == "__main__":
    main()
