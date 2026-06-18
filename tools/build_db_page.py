# -*- coding: utf-8 -*-
"""Build pages/04-db.html from db_textbook_data.py."""
from html import escape
from pathlib import Path

from db_textbook_data import FLASHCARDS, MNEMONICS, PAST_EXAMS, SECTIONS

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "pages/04-db.html"

NAV_OBSERVER = """
const navLinks = Array.from(document.querySelectorAll('.sidebar nav a'));
if (navLinks.length) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
      }
    });
  }, { rootMargin: '-35% 0px -60% 0px', threshold: 0 });
  document.querySelectorAll('section[id], article[id]').forEach(s => obs.observe(s));
}
"""


def esc(s):
    return escape(str(s))


def rows_html(rows):
    body = "".join(
        f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>"
        for a, b, c in rows
    )
    return (
        '<div class="table-wrap"><table><thead><tr>'
        "<th>구분</th><th>키워드/개념</th><th>답안 활용</th></tr></thead>"
        f"<tbody>{body}</tbody></table></div>"
    )


def depth_html(depth_sections):
    if not depth_sections:
        return ""
    parts = []
    for title, items in depth_sections:
        body = "".join(
            f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>"
            for a, b, c in items
        )
        parts.append(
            f'<h4 class="depth-sub">{esc(title)}</h4>'
            '<div class="table-wrap"><table><thead><tr>'
            "<th>항목</th><th>내용</th><th>답안 포인트</th></tr></thead>"
            f"<tbody>{body}</tbody></table></div>"
        )
    return (
        '<details class="topic-depth-wrap" open>'
        '<summary><span class="depth-title">📋 답안용 핵심 정리</span>'
        '<span class="depth-hint">접기/펼치기</span></summary>'
        f'<div class="topic-depth-body">{"".join(parts)}</div></details>'
    )


def topic_card(topic):
    chips = "".join(f"<span>{esc(c)}</span>" for c in topic["chips"])
    diagram = topic.get("diagram", "")
    diagram_html = f'<div class="diagram"><pre>{esc(diagram)}</pre></div>' if diagram else ""
    return f"""<article id="{esc(topic['id'])}" class="topic-card">
<div class="topic-head"><div><h3>{esc(topic['title'])}</h3><p class="pages">교재 범위: {esc(topic['pages'])}</p></div>
<span class="mnemonic">암기: {esc(topic['mnemonic'])}</span></div>
<div class="chips">{chips}</div>
{diagram_html}
{rows_html(topic['rows'])}
{depth_html(topic.get('depth', []))}
<div class="answer-box"><strong>답안 확장 문장</strong><p>{esc(topic['answer'])}</p></div>
</article>"""


def section_html(sec):
    cards = "".join(topic_card(t) for t in sec["topics"])
    return f'<section id="{esc(sec["id"])}" class="section"><h2>{esc(sec["title"])}</h2>{cards}</section>'


def mnemonic_book():
    items = []
    for src, key, split, desc, anchor in MNEMONICS:
        items.append(
            f"""<details class="mnemonic-item">
<summary><span class="mn-from">{esc(src)}</span><span class="mn-key">{esc(key)}</span></summary>
<div class="mn-body">
<p class="mn-split"><b>풀이:</b> {esc(split)}</p>
<details class="mn-more">
<summary>설명 보기</summary>
<p>{esc(desc)}</p>
<p><a href="#{esc(anchor)}">→ 본문 이동</a></p>
</details>
</div>
</details>"""
        )
    return f"""<!-- MNEMONIC_BOOK -->
<section class="panel mnemonic-book-section" id="mnemonic-book">
<details class="mnemonic-book-wrap" open>
<summary><span class="mn-wrap-title">📖 두음 모음집 — DB</span><span class="mn-wrap-hint">전체 접기/펼치기</span></summary>
<div class="mnemonic-book-body">
<p class="subtle">기본반 NewDB 교재 기준 · 출처 → 두음 → 풀이 → 설명</p>
<input class="mn-filter" type="search" placeholder="두음 검색 (예: ACID, 통저운공, 개도참사…)" oninput="filterMnemonics(this)"/>
<div class="mnemonic-list">{''.join(items)}</div>
</div>
</details>
</section>"""


def past_exams():
    rows = "".join(
        f"<tr><td>{esc(r)}</td><td>{esc(t)}</td><td>{esc(q)}</td></tr>"
        for r, t, q in PAST_EXAMS
    )
    return f"""<section id="past-exams" class="section"><h2>11. 기출문제 (교재 p.2~3)</h2>
<div class="table-wrap"><table><thead><tr><th>회차</th><th>구분</th><th>문제</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="note">135·134·133·132·131회 DB 관련 기출을 교재 목차와 함께 정리했습니다.</p>
</section>"""


def flashcards():
    cards = []
    for cat, q, a in FLASHCARDS:
        cards.append(
            f"""<div class="flash-card" data-cat="{esc(cat)}">
<div class="flash-front"><span class="flash-cat">{esc(cat)}</span><p>{esc(q)}</p></div>
<div class="flash-back"><p>{esc(a)}</p></div>
</div>"""
        )
    return f"""<section id="flashcards" class="flash-section">
<h2>10. 암기카드</h2>
<div class="flash-controls">
<input id="search" type="search" placeholder="검색…"/>
<select id="catFilter"><option value="">전체 분류</option></select>
<button id="shuffleBtn" type="button">섞기</button>
<button id="revealBtn" type="button">전체 뒤집기</button>
<button id="resetBtn" type="button">초기화</button>
</div>
<div class="flash-grid" id="cards">{''.join(cards)}</div>
</section>"""


def answer_template():
    return """<section id="answer-template" class="section"><h2>9. 기술사 답안 템플릿</h2>
<article class="template-card"><h3>9.1 DB 1교시형 (약 30줄)</h3>
<div class="diagram"><pre>① 개념 정의 (2~3줄)
② 핵심 구성·표 (키워드 5~7개)
③ 비교·도식 1개 (정적/동적, 식별/비식별 등)
④ 결론·시사점 (2~3줄)</pre></div></article>
<article class="template-card"><h3>9.2 DB 2교시형 (약 70줄)</h3>
<div class="diagram"><pre>1. 개요 — 정의 · 배경 · 전체 흐름도
2. 핵심 — 구성요소 · 비교표 · 절차/알고리즘
3. 적용 — 사례·고려사항 · 기대효과
4. 결론 — 한계 · 대응 · 발전방향</pre></div>
<div class="table-wrap"><table><thead><tr><th>유형</th><th>추천 구조</th></tr></thead><tbody>
<tr><td>회복·동시성</td><td>ACID → 장애유형 → 회복기법 표 → 락/MVCC 비교</td></tr>
<tr><td>모델링</td><td>3단계 → ER 변환 → 정규화/반정규화 Trade-off</td></tr>
<tr><td>NoSQL</td><td>RDB 한계 → CAP → 유형 표 → RDB 비교</td></tr>
</tbody></table></div></article>
</section>"""


def nav_links():
    links = [
        ("#mnemonic-book", "📖 두음 모음집"),
    ]
    for sec in SECTIONS:
        links.append((f"#{sec['id']}", sec["title"]))
    links.extend([
        ("#answer-template", "9. 기술사 답안 템플릿"),
        ("#flashcards", "10. 암기카드"),
        ("#past-exams", "11. 기출문제"),
    ])
    return "".join(f'<a href="{h}">{esc(t)}</a>' for h, t in links)


def build():
    nav = nav_links()
    content = "\n".join([
        '<section class="panel"><span class="kicker">사용법</span>'
        "<p>① <b>두음 모음집</b>으로 암기 포인트 확인 → ② <b>도식·표</b>로 흐름 복원 "
        "→ ③ <b>답안 확장 문장</b>으로 1·2교시 연습 → ④ <b>암기카드·기출</b>로 복원 훈련.</p>"
        '<div class="note">「04. NewDB 기본반」 교재(179p) 흐름 기준 · 기출 131~135회 연계</div></section>',
        mnemonic_book(),
        *[section_html(s) for s in SECTIONS],
        answer_template(),
        flashcards(),
        past_exams(),
    ])

    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>DB 기술사 분석 키워드 &amp; 암기카드</title>
<link rel="stylesheet" href="../assets/study-page.css"/>
<link rel="stylesheet" href="../assets/diagrams.css"/>
<link rel="stylesheet" href="../assets/mnemonic-book.css"/>
</head>
<body>
<aside class="sidebar">
  <a class="back-home" href="../index.html">← 목차로</a>
  <h1>DB<br>기술사 정리</h1>
  <p class="sub">키워드 + 도식 + 암기카드</p>
  <nav>{nav}</nav>
</aside>
<main class="main">
  <a class="back-home back-home-main" href="../index.html">← 목차로</a>
  <details class="mobile-toc"><summary>목차 열기</summary><div class="toc-links">{nav}</div></details>
  <div class="hero">
    <h1>DB 기술사 분석 키워드 &amp; 암기카드</h1>
    <p>「04. NewDB 기본반」 교재 흐름 · 기출 주제 · 1·2교시 답안 확장용</p>
    <p class="note">PC: 왼쪽 고정 목차 / 모바일: 상단 접기형 목차 / 표: 가로 스크롤 지원</p>
  </div>
{content}
</main>
<button class="top-btn" type="button" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑ 위로</button>
<script>
const cards = Array.from(document.querySelectorAll('.flash-card'));
cards.forEach(c => c.addEventListener('click', () => c.classList.toggle('flipped')));
const catFilter = document.getElementById('catFilter');
if (catFilter) {{
  [...new Set(cards.map(c => c.dataset.cat))].sort().forEach(cat => {{
    const opt = document.createElement('option'); opt.value = cat; opt.textContent = cat; catFilter.appendChild(opt);
  }});
  function applyFilter() {{
    const q = (document.getElementById('search').value || '').toLowerCase();
    const cat = catFilter.value;
    cards.forEach(c => {{
      const text = c.textContent.toLowerCase();
      const show = (!q || text.includes(q)) && (!cat || c.dataset.cat === cat);
      c.style.display = show ? '' : 'none';
    }});
  }}
  document.getElementById('search').addEventListener('input', applyFilter);
  catFilter.addEventListener('change', applyFilter);
  document.getElementById('shuffleBtn').addEventListener('click', () => {{
    const wrap = document.getElementById('cards');
    cards.sort(() => Math.random() - 0.5).forEach(c => wrap.appendChild(c));
  }});
  document.getElementById('revealBtn').addEventListener('click', () => cards.forEach(c => c.classList.add('flipped')));
  document.getElementById('resetBtn').addEventListener('click', () => {{
    document.getElementById('search').value=''; catFilter.value=''; cards.forEach(c => {{ c.style.display=''; c.classList.remove('flipped'); }});
  }});
}}
function filterMnemonics(inp){{
  const q=(inp.value||'').toLowerCase().trim();
  const list=inp.closest('.mnemonic-book-section');
  if(!list) return;
  list.querySelectorAll('.mnemonic-item').forEach(el=>{{
    el.classList.toggle('hidden', q && !el.textContent.toLowerCase().includes(q));
  }});
}}
{NAV_OBSERVER}
</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"built: {OUT}")


if __name__ == "__main__":
    build()
