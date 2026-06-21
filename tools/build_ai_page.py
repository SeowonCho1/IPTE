# -*- coding: utf-8 -*-
"""Build pages/05-ai.html from ai_textbook_data.py."""
from pathlib import Path

from ai_textbook_data import FLASHCARDS, MNEMONICS, PAST_EXAMS, PAST_EXAMS_NOTE, SECTIONS
from study_page_builder import answer_template_ai, build_page

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "pages/05-ai.html"

META = {
    "title": "인공지능 기술사 분석 키워드 & 암기카드",
    "sidebar_h1": "인공지능<br>기술사 정리",
    "sidebar_sub": "키워드 + 도식 + 암기카드",
    "hero_h1": "인공지능 기술사 분석 키워드 & 암기카드",
    "hero_p": "「04. 인공지능 기본반 v1.1」 교재 흐름 · 기출 주제 · 1·2교시 답안 확장용",
    "hero_note": "PC: 왼쪽 고정 목차 / 모바일: 상단 접기형 목차 / 표: 가로 스크롤 지원",
    "mnemonic_title": "AI",
    "usage": (
        "① <b>두음 모음집</b>으로 암기 포인트 확인 → ② <b>도식·표</b>로 알고리즘·흐름 복원 "
        "→ ③ <b>답안 확장 문장</b>으로 1·2교시 연습 → ④ <b>암기카드·기출</b>로 복원 훈련."
    ),
    "note": "「04. 인공지능 for 기본반 v1.1」 교재(197p) 흐름 기준 · 기출 108~135회 연계",
}

EXTRA_NAV = [
    ("#answer-template", "10. 기술사 답안 템플릿"),
    ("#flashcards", "11. 암기카드"),
    ("#past-exams", "12. 기출문제"),
]


def build():
    build_page(
        out_path=OUT,
        meta=META,
        sections=SECTIONS,
        mnemonics=MNEMONICS,
        flashcards_list=FLASHCARDS,
        past_exams_list=PAST_EXAMS,
        past_exams_note=PAST_EXAMS_NOTE,
        answer_template_html=answer_template_ai(),
        extra_nav=EXTRA_NAV,
    )


if __name__ == "__main__":
    build()
