# -*- coding: utf-8 -*-
"""Build answer-format practice gallery pages from assets/format-practice/."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets/format-practice"
OUT_DIR = ROOT / "pages/format"
CSS = "../../assets/format-gallery.css"
SITE_TITLE = "도식화 참고자료"

CATEGORIES = [
    {
        "id": "분류",
        "dir": "분류",
        "title": "분류형",
        "desc": "매트릭스·사분면·우선순위 등 분류·구분 중심 답안",
    },
    {
        "id": "표",
        "dir": "표",
        "title": "표형",
        "desc": "SDLC 산출물·비교표·체크리스트 등 표 중심 답안",
    },
    {
        "id": "그림",
        "dir": "그림",
        "title": "그림·도식형",
        "desc": "아키텍처·구조도·개념도 등 그림 중심 답안",
    },
    {
        "id": "절차",
        "dir": "절차",
        "title": "절차·흐름형",
        "desc": "단계별 절차·프로세스·순서도 중심 답안",
    },
    {
        "id": "그래프",
        "dir": "그래프",
        "title": "그래프형",
        "desc": "차트·곡선·추이 등 그래프 중심 답안",
    },
    {
        "id": "2교시-1단락",
        "dir": "2교시 1단락",
        "title": "2교시 1단락형",
        "desc": "2교시 서술형 — 한 단락·한 주제 집중 답안",
    },
    {
        "id": "최창환",
        "dir": "최창환",
        "title": "합격자 답안 (최창환)",
        "desc": "실제 기술사 답안지 사진 모음 — 전체 흐름·분량 참고용",
    },
]

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}


def esc(s):
    return escape(str(s))


def list_images(folder: Path):
    if not folder.is_dir():
        return []
    files = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXT]
    return sorted(files, key=lambda p: p.name.lower())


def gallery_html(cat, images):
    cards = []
    for i, img in enumerate(images, 1):
        rel = f"../../assets/format-practice/{cat['dir']}/{img.name}"
        cards.append(
            f'<figure class="shot" id="img-{i}">'
            f'<a href="{esc(rel)}" target="_blank" rel="noopener">'
            f'<img src="{esc(rel)}" alt="{esc(cat["title"])} {i}" loading="lazy" />'
            f"</a>"
            f'<figcaption>{esc(img.name)}</figcaption></figure>'
        )
    body = "\n".join(cards) if cards else '<p class="empty">이미지가 없습니다.</p>'
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(cat["title"])} — {esc(SITE_TITLE)}</title>
<link rel="stylesheet" href="{CSS}" />
</head>
<body>
<header class="top">
  <a class="back" href="index.html">← {esc(SITE_TITLE)}</a>
  <a class="back home" href="../../index.html">목차로</a>
  <h1>{esc(cat["title"])}</h1>
  <p>{esc(cat["desc"])} · <b>{len(images)}</b>장</p>
</header>
<main class="gallery">{body}</main>
</body>
</html>"""


def index_html():
    cards = []
    total = 0
    for cat in CATEGORIES:
        n = len(list_images(ASSETS / cat["dir"]))
        total += n
        cards.append(
            f'<a class="cat-card" href="{esc(cat["id"])}.html">'
            f'<h2>{esc(cat["title"])}</h2>'
            f'<p>{esc(cat["desc"])}</p>'
            f'<span class="count">{n}장</span></a>'
        )
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(SITE_TITLE)}</title>
<link rel="stylesheet" href="{CSS}" />
</head>
<body>
<header class="top hub">
  <a class="back home" href="../../index.html">← 목차로</a>
  <h1>{esc(SITE_TITLE)}</h1>
  <p>기술사 답안 도식·표·그림·절차 참고 · 총 <b>{total}</b>장</p>
</header>
<main class="hub-main">
  <h2 class="hub-section">목차</h2>
  <section class="cat-grid">{"".join(cards)}</section>
</main>
</body>
</html>"""


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (ROOT / "assets/format-gallery.css").write_text(GALLERY_CSS, encoding="utf-8")
    OUT_DIR.joinpath("index.html").write_text(index_html(), encoding="utf-8")
    for cat in CATEGORIES:
        images = list_images(ASSETS / cat["dir"])
        OUT_DIR.joinpath(f"{cat['id']}.html").write_text(gallery_html(cat, images), encoding="utf-8")
        print(f"  {cat['id']}: {len(images)} images")
    print(f"built: {OUT_DIR}")


GALLERY_CSS = """\
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: "Malgun Gothic", "Apple SD Gothic Neo", sans-serif;
  line-height: 1.5;
  color: #222;
  background: #f0f2f5;
}
.top {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  padding: 1rem 1.25rem 1.25rem;
  position: sticky;
  top: 0;
  z-index: 10;
}
.top.hub { position: static; }
.back {
  display: inline-block;
  font-size: .85rem;
  color: #1a5fb4;
  text-decoration: none;
  margin-bottom: .5rem;
}
.back.home { margin-left: 1rem; }
.top h1 { font-size: 1.35rem; margin-bottom: .25rem; }
.top p { color: #555; font-size: .9rem; }
.hub-main { max-width: 960px; margin: 0 auto; padding: 1.25rem; }
.hub-section {
  font-size: .95rem;
  color: #444;
  margin-bottom: .75rem;
  padding-bottom: .35rem;
  border-bottom: 1px solid #e5e7eb;
}
.cat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: .75rem;
}
.cat-card {
  display: block;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1rem 1.1rem;
  text-decoration: none;
  color: inherit;
  transition: box-shadow .15s, border-color .15s;
}
.cat-card:hover {
  border-color: #1a5fb4;
  box-shadow: 0 2px 8px rgba(26,95,180,.12);
}
.cat-card h2 { font-size: 1rem; margin-bottom: .35rem; color: #1a5fb4; }
.cat-card p { font-size: .82rem; color: #666; margin-bottom: .5rem; }
.count { font-size: .78rem; color: #888; background: #f3f4f6; padding: .15rem .45rem; border-radius: 4px; }
.gallery {
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.shot {
  background: #fff;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,.06);
}
.shot a { display: block; line-height: 0; }
.shot img {
  width: 100%;
  height: auto;
  display: block;
  cursor: zoom-in;
}
.shot figcaption {
  padding: .45rem .75rem;
  font-size: .75rem;
  color: #888;
  border-top: 1px solid #f0f0f0;
}
.empty { padding: 2rem; text-align: center; color: #888; }
@media (max-width: 600px) {
  .top h1 { font-size: 1.15rem; }
  .cat-grid { grid-template-columns: 1fr; }
}
"""


if __name__ == "__main__":
    build()
