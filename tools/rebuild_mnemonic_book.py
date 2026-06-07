# -*- coding: utf-8 -*-
"""Rebuild mnemonic-book sections from mnemonic_data.py."""
import re
from pathlib import Path

from mnemonic_data import SW01, SW02

ROOT = Path(__file__).resolve().parent.parent
MARKER = "<!-- MNEMONIC_BOOK -->"

SW02_H4_IDS = [
    ('<h4>테스트 오라클 유형</h4>', '<h4 id="s3-oracle">테스트 오라클 유형</h4>'),
    ('<h4>테스트 완료조건: 완·목·기·커·리·스</h4>',
     '<h4 id="s3-완료조건">테스트 완료조건: 완·목·기·커·리·스</h4>'),
    ('<h4>경계값 분석 유형: 싱·로·오·로·라</h4>',
     '<h4 id="s7-경계값">경계값 분석 유형: 싱·로·오·로·라</h4>'),
    ('<h4>상태전이 구성요소: 상·전·이·가·액·초·종</h4>',
     '<h4 id="s7-상태전이">상태전이 구성요소: 상·전·이·가·액·초·종</h4>'),
    ('<h4>커버리지 강도 비교</h4>', '<h4 id="s8-mccabe">커버리지 강도 비교</h4>'),
    ('<h4>테스트 레벨 비교</h4>', '<h4 id="s10-시스템">테스트 레벨 비교</h4>'),
    ('<h4>몽키·고릴라·회귀 비교</h4>', '<h4 id="s11-몽키">몽키·고릴라·회귀 비교</h4>'),
    ('<h4>사용성 테스트 방법론</h4>', '<h4 id="s11-사용성">사용성 테스트 방법론</h4>'),
    ('<h4>전략적 테스트 비교</h4>', '<h4 id="s12-rbt">전략적 테스트 비교</h4>'),
    ('<h4>Mutation Test 절차</h4>', '<h4 id="s12-mutation">Mutation Test 절차</h4>'),
]

FILTER_JS = """
function filterMnemonics(inp){
  const q=(inp.value||'').toLowerCase().trim();
  const list=inp.closest('.mnemonic-book-section');
  if(!list) return;
  list.querySelectorAll('.mnemonic-item').forEach(el=>{
    el.classList.toggle('hidden', q && !el.textContent.toLowerCase().includes(q));
  });
}"""


def render_item(key, source, split, explain, link):
    if link == "extra":
        raise ValueError("use extra_links tuple")
    links_html = f'<p><a href="{link}">→ 본문 이동</a></p>'
    if isinstance(link, list):
        links_html = "<p>" + " · ".join(
            f'<a href="{h}">{t}</a>' for h, t in link
        ) + "</p>"
    return f'''<details class="mnemonic-item">
<summary><span class="mn-from">{source}</span><span class="mn-key">{key}</span></summary>
<div class="mn-body">
<p class="mn-split"><b>풀이:</b> {split}</p>
<details class="mn-more">
<summary>설명 보기</summary>
{explain}
{links_html}
</details>
</div>
</details>'''


def render_book(title, items):
    rows = []
    for row in items:
        key, source, split, explain, link = row[:5]
        if link == "extra":
            links = row[5] if len(row) > 5 else []
            links_html = "<p>" + " · ".join(
                f'<a href="{h}">{t}</a>' for h, t in links
            ) + "</p>"
            rows.append(f'''<details class="mnemonic-item">
<summary><span class="mn-from">{source}</span><span class="mn-key">{key}</span></summary>
<div class="mn-body">
<p class="mn-split"><b>풀이:</b> {split}</p>
<details class="mn-more">
<summary>설명 보기</summary>
{explain}
{links_html}
</details>
</div>
</details>''')
        else:
            rows.append(render_item(key, source, split, explain, link))
    items_html = "\n".join(rows)
    return f'''{MARKER}
<section class="panel mnemonic-book-section" id="mnemonic-book">
<details class="mnemonic-book-wrap" open>
<summary><span class="mn-wrap-title">{title}</span><span class="mn-wrap-hint">전체 접기/펼치기</span></summary>
<div class="mnemonic-book-body">
<p class="subtle">본식 docx 두음법칙 기준 · 출처 → 두음 → 풀이 → 설명 (접기/펼치기)</p>
<input class="mn-filter" type="search" placeholder="두음 검색 (예: 작방, 결완, 명완…)" oninput="filterMnemonics(this)"/>
<div class="mnemonic-list">
{items_html}
</div>
</div>
</details>
</section>
'''


def patch_sw02_anchors():
    path = ROOT / "pages/02-sw테스트.html"
    text = path.read_text(encoding="utf-8")
    for old, new in SW02_H4_IDS:
        if old == new:
            continue
        if 'id="' in old and old in text:
            continue
        if old in text and new not in text:
            text = text.replace(old, new, 1)
    if 'id="s14-33063"' not in text:
        text = text.replace(
            '<li><b>ISO 33063</b><span>테스트 프로세스 평가 모델</span></li>',
            '<li id="s14-33063"><b>ISO 33063</b><span>테스트 프로세스 평가 모델</span></li>',
            1,
        )
    path.write_text(text, encoding="utf-8")
    print("patched SW02 anchors")


def rebuild_page(path_key, book_html, insert_before):
    path = ROOT / path_key
    text = path.read_text(encoding="utf-8")
    pat = re.compile(
        r'<!-- MNEMONIC_BOOK -->\s*<section class="panel mnemonic-book-section" id="mnemonic-book">.*?</section>',
        re.DOTALL,
    )
    if pat.search(text):
        text = pat.sub(book_html, text, count=1)
    else:
        text = text.replace(insert_before, book_html + "\n" + insert_before, 1)
    if "function filterMnemonics" not in text:
        text = text.replace("</script>", FILTER_JS + "\n</script>", 1)
    path.write_text(text, encoding="utf-8")
    print(f"rebuilt: {path_key}")


def main():
    patch_sw02_anchors()
    # fix SW01 extra link tuples in data
    sw01_fixed = []
    for row in SW01:
        if row[4] == "extra":
            sw01_fixed.append((*row[:4], "extra", row[5]))
        else:
            sw01_fixed.append(row)

    rebuild_page(
        "pages/01-sw공학.html",
        render_book("📖 두음 모음집 — SW공학", sw01_fixed),
        '<section class="panel" id="analysis">',
    )
    rebuild_page(
        "pages/02-sw테스트.html",
        render_book("📖 두음 모음집 — SW테스트", SW02),
        '<section id="s0" class="topic">',
    )
    print(f"SW01 items: {len(sw01_fixed)}, SW02 items: {len(SW02)}")


if __name__ == "__main__":
    main()
