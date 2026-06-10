# -*- coding: utf-8 -*-
"""답안 작성용 상세 본문 — topic id별 정의·특징·구성요소."""

from html import escape

from consulting_textbook_data import TOPIC_DEPTH, TOPIC_FORMULAS


def _rows(items):
    out = []
    for label, detail, tip in items:
        out.append(
            f"<tr><td>{escape(label)}</td><td>{escape(detail)}</td>"
            f"<td>{escape(tip)}</td></tr>"
        )
    return "".join(out)


def _section(title, items):
    return (
        f'<h4 class="depth-sub">{escape(title)}</h4>'
        f'<div class="table-wrap"><table><thead><tr>'
        f"<th>항목</th><th>내용</th><th>답안 포인트</th></tr></thead>"
        f"<tbody>{_rows(items)}</tbody></table></div>"
    )


def _formula_block(art_id: str) -> str:
    text = TOPIC_FORMULAS.get(art_id)
    if not text:
        return ""
    return (
        '<div class="formula-box"><strong>📐 계산식 · 판정기준</strong>'
        f"<pre>{escape(text)}</pre></div>"
    )


def render_depth(art_id: str, h3: str) -> str:
    sections = TOPIC_DEPTH.get(art_id)
    if not sections:
        return ""

    body = "".join(_section(title, items) for title, items in sections)
    body += _formula_block(art_id)
    return f"""<details class="topic-depth-wrap" open>
<summary><span class="depth-title">📋 답안용 핵심 정리 · {escape(h3)}</span><span class="depth-hint">접기/펼치기</span></summary>
<div class="topic-depth-body">{body}</div>
</details>"""
