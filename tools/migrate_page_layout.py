# -*- coding: utf-8 -*-
"""Migrate SW공학/SW테스트 pages to 경영컨설팅 layout shell."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

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

PAGES = {
    "pages/01-sw공학.html": {
        "title": "SW공학 기술사 분석 키워드 & 암기카드",
        "sidebar_h1": "SW공학<br>기술사 정리",
        "sidebar_sub": "키워드 + 도식 + 암기카드",
        "hero_h1": "SW공학 기술사 분석 키워드 & 암기카드",
        "hero_p1": "「01. 소프트웨어공학 기본반」 교재 흐름 · 기출 주제 · 1·2교시 답안 확장용",
        "hero_note": "PC: 왼쪽 고정 목차 / 모바일: 상단 접기형 목차 / 표: 가로 스크롤 지원",
    },
    "pages/02-sw테스트.html": {
        "title": "SW 테스트 기술사 분석 키워드 & 암기카드",
        "sidebar_h1": "SW테스트<br>기술사 정리",
        "sidebar_sub": "키워드 + 도식 + 암기카드",
        "hero_h1": "SW 테스트 기술사 분석 키워드 & 암기카드",
        "hero_p1": "「02. SW테스트 기본반」 교재 흐름 · 기출 주제 · 1·2교시 답안 확장용",
        "hero_note": "PC: 왼쪽 고정 목차 / 모바일: 상단 접기형 목차 / 표: 가로 스크롤 지원",
    },
}


def extract_nav_links(html: str) -> str:
    m = re.search(r'<aside class="sidebar"[^>]*>(.*?)</aside>', html, re.DOTALL)
    if not m:
        m = re.search(r'class="sidebar"[^>]*>(.*?)</aside>', html, re.DOTALL)
    block = m.group(1) if m else ""
    links = re.findall(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', block)
    return "".join(f'<a href="{h}">{t}</a>' for h, t in links)


def extract_content(html: str) -> str:
    start = html.find("<!-- MNEMONIC_BOOK -->")
    if start < 0:
        start = html.find('<section class="panel"')
    end = html.rfind("</main>")
    if end < 0:
        end = html.rfind('<script>')
    if start < 0 or end < 0:
        raise ValueError("content bounds not found")
    before = html[:start]
    usage = ""
    um = re.search(
        r'<section class="panel"><span class="kicker">.*?</section>\s*',
        before,
        re.DOTALL,
    )
    if um:
        usage = um.group(0)
    elif "class=\"card note\"" in before:
        um2 = re.search(r'<div class="card note">.*?</div>\s*', before, re.DOTALL)
        if um2:
            usage = f'<section class="panel">{um2.group(0)}</section>\n'
    return usage + html[start:end].strip()


def extract_scripts(html: str) -> str:
    scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)
    body = "\n".join(s.strip() for s in scripts if s.strip())
    if "navLinks" not in body:
        body += NAV_OBSERVER
    return body


def build_shell(meta: dict, nav: str, content: str, scripts: str) -> str:
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{meta['title']}</title>
<link rel="stylesheet" href="../assets/study-page.css"/>
<link rel="stylesheet" href="../assets/diagrams.css"/>
<link rel="stylesheet" href="../assets/mnemonic-book.css"/>
</head>
<body>
<aside class="sidebar">
  <a class="back-home" href="../index.html">← 목차로</a>
  <h1>{meta['sidebar_h1']}</h1>
  <p class="sub">{meta['sidebar_sub']}</p>
  <nav>{nav}</nav>
</aside>
<main class="main">
  <a class="back-home back-home-main" href="../index.html">← 목차로</a>
  <details class="mobile-toc"><summary>목차 열기</summary><div class="toc-links">{nav}</div></details>
  <div class="hero">
    <h1>{meta['hero_h1']}</h1>
    <p>{meta['hero_p1']}</p>
    <p class="note">{meta['hero_note']}</p>
  </div>
{content}
</main>
<button class="top-btn" type="button" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑ 위로</button>
<script>
{scripts}
</script>
</body>
</html>
"""


def migrate(rel: str):
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    if 'class="main"' in html and 'study-page.css' in html:
        print(f"skip (already migrated): {rel}")
        return
    meta = PAGES[rel]
    nav = extract_nav_links(html)
    content = extract_content(html)
    scripts = extract_scripts(html)
    path.write_text(build_shell(meta, nav, content, scripts), encoding="utf-8")
    print(f"migrated: {rel}")


def update_page3_css():
    path = ROOT / "pages/03-경영컨설팅.html"
    html = path.read_text(encoding="utf-8")
    if "study-page.css" in html:
        print("skip page3 (already uses shared css)")
        return
    html = re.sub(r"<style>.*?</style>\s*", "", html, count=1, flags=re.DOTALL)
    html = html.replace(
        '<link rel="stylesheet" href="../assets/diagrams.css"/>',
        '<link rel="stylesheet" href="../assets/study-page.css"/>\n<link rel="stylesheet" href="../assets/diagrams.css"/>',
        1,
    )
    html = html.replace('<a class="top-btn"', '<button class="top-btn" type="button" onclick="window.scrollTo({top:0,behavior:\'smooth\'})"')
    # page3 might already use button - check
    path.write_text(html, encoding="utf-8")
    print("updated page3 css link")


def main():
    for rel in PAGES:
        migrate(rel)
    update_page3_css()


if __name__ == "__main__":
    main()
