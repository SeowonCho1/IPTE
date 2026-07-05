# -*- coding: utf-8 -*-
"""Inject per-topic '이해 못함' checkboxes + 이해도율 bar into the 10
암기장 정리 pages (01~10). Safe to re-run (skips already-patched pages).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "01-법제도", "02-신기술", "03-보안", "04-빅데이터", "05-프로젝트관리",
    "06-네트워크", "07-caos", "08-알고리즘", "09-uml디자인패턴", "10-it뉴스",
]

TOPIC_CARD_OPEN = re.compile(r'<article([^>]*)\bclass="topic-card"([^>]*)>')

CHECKBOX_TPL = (
    '<label class="understand-toggle">'
    '<input type="checkbox" class="understand-check" data-tid="{tid}"> 이해 못함'
    '</label>'
)


def inject_checkboxes(html: str) -> tuple[str, int]:
    tid = 0

    def repl(m: re.Match) -> str:
        nonlocal tid
        tid += 1
        return (
            f'<article{m.group(1)} class="topic-card"{m.group(2)}>'
            + CHECKBOX_TPL.format(tid=tid)
        )

    return TOPIC_CARD_OPEN.sub(repl, html), tid


def inject_hero_bar(html: str) -> str:
    bar = (
        '<div class="understand-bar">'
        '<div class="understand-rate">'
        '<span class="urate-label">이해도</span>'
        '<span class="urate-value" id="urate-value">100%</span>'
        '<span class="urate-detail" id="urate-detail"></span>'
        '</div>'
        '<button type="button" id="toggle-unclear-btn" class="toggle-unclear-btn">'
        '🔖 이해 못한 토픽만 보기</button>'
        '</div>'
    )
    return re.sub(r'(<p class="note">.*?</p>\s*)(</div>\s*(?=<section|<div class="panel))',
                  r'\1' + bar + r'\2', html, count=1, flags=re.DOTALL)


def patch_page(stem: str) -> None:
    path = ROOT / "pages" / f"{stem}.html"
    text = path.read_text(encoding="utf-8")
    if "understand-tracker" in text:
        print(f"skip (already patched): {stem}")
        return

    text = text.replace(
        '<link rel="stylesheet" href="../assets/mnemonic-book.css"/>',
        '<link rel="stylesheet" href="../assets/mnemonic-book.css"/>\n'
        '<link rel="stylesheet" href="../assets/understand-tracker.css"/>',
        1,
    )
    text = text.replace("<body>", f'<body data-page-id="{stem}">', 1)
    text = inject_hero_bar(text)
    text, count = inject_checkboxes(text)
    text = text.replace(
        "</body>",
        '<script src="../assets/understand-tracker.js"></script>\n</body>',
        1,
    )

    path.write_text(text, encoding="utf-8")
    print(f"patched: {stem} ({count} topic-cards)")


def main():
    for stem in PAGES:
        patch_page(stem)


if __name__ == "__main__":
    main()
