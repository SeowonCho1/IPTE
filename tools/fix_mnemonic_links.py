# -*- coding: utf-8 -*-
"""Point mnemonic-book 본문 이동 links to exact content anchors."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# value: anchor id OR full <p>...</p> for multi-link items
LINK_MAP = {
    "pages/01-sw공학.html": {
        "타요설개테운폐": "#1-4-SDLC",
        "비복비복변순무개": "#1-1-소프트웨어의-개념과-특성",
        "작방산관기도": "#3-1-주요-구성",
        "캡추다정상": "#3-3-객체지향-핵심-원리",
        "개변동고": "#4-1-Agile",
        "용단커피존": "#4-2-XP",
        "CALMS / 빈·리·복·실": (
            '<p><a href="#5-2-1-CALMS">→ CALMS 본문</a> · '
            '<a href="#5-2-2-DORA">→ DORA 본문</a></p>'
        ),
        "코드·버전·멱등·GitOps": "#5-2-3-IaC",
        "아동아식품분우분발": "#6-4-아키텍처-평가",
        "도분명검관": "#9-2-요구공학-프로세스",
        "기신사효유이": "#10-3-ISO-IEC-9126",
        "기성호상신보유유안": "#10-5-ISO-IEC-25010-2023-품질-특성",
        "요모관측평확": "#10-4-ISO-IEC-25000-SQuaRE",
        "기지조 / 초관정관최": (
            '<p><a href="#11-1-ISO-IEC-12207">→ 기지조(12207)</a> · '
            '<a href="#11-3-CMM-CMMI">→ 초관정관최(CMMI)</a></p>'
        ),
        "고응집·저결합": "#12-2-모듈화",
        "심노제": "#13-4-ISO-26262과-ASIL",
    },
    "pages/02-sw테스트.html": {
        "결완초집살정오": "#s1-7원리",
        "식항입출환특의": "#s3-케이스",
        "완목기커리스": "#s3-완료조건",
        "동경결상유페직원분": "#s7-명세기반",
        "탐분체특오혹": "#s9-경험기반",
        "백빅상하샌": "#s10-통합",
        "사운계규알베": "#s10-인수",
        "단복임 / 루스확가티 / 부스내볼": "#s11-성능",
        "버프독기키": "#s14-29119",
        "초관정관최 ↔ TMMi": "#s14-tmmi",
        "차박노디": "#s9-탐색적",
    },
    "pages/03-경영컨설팅.html": {
        "키-사-시": "#study-0",
        "목-이-평-전": "#strategy-0",
        "정-경-사-기 + 환-법": "#strategy-1",
        "기-잠-대-구-공": "#strategy-2",
        "투-운-산-마-서 / 조-기-인-구": "#strategy-3",
        "강약기위 / 자경고 / 세목위": "#strategy-5",
        "원-차-집": "#investment-1",
        "별-돈-물-개": "#investment-2",
        "제-감-증-창": "#investment-3",
        "발-정-개-전 / 공-정-상-시-검": "#innovation-2",
        "모순-분리-발명원리": "#innovation-1",
    },
}

# Add fragment ids to SW테스트 h4 headings (content anchors)
SW02_H4_IDS = [
    ('<h4>테스트 7원리</h4>', '<h4 id="s1-7원리">테스트 7원리</h4>'),
    ('<h4>테스트 케이스 구성요소: 식·항·입·출·환·특·의</h4>',
     '<h4 id="s3-케이스">테스트 케이스 구성요소: 식·항·입·출·환·특·의</h4>'),
    ('<h4>테스트 완료조건: 완·목·기·커·리·스</h4>',
     '<h4 id="s3-완료조건">테스트 완료조건: 완·목·기·커·리·스</h4>'),
    ('<h4>명세기반 기법: 동·경·결·상·유·페·직·원·분</h4>',
     '<h4 id="s7-명세기반">명세기반 기법: 동·경·결·상·유·페·직·원·분</h4>'),
    ('<h4>경험기반 기법: 탐·분·체·특·오·혹</h4>',
     '<h4 id="s9-경험기반">경험기반 기법: 탐·분·체·특·오·혹</h4>'),
    ('<h4>탐색적 테스트 구성요소: 차·박·노·디</h4>',
     '<h4 id="s9-탐색적">탐색적 테스트 구성요소: 차·박·노·디</h4>'),
    ('<h4>통합 테스트 방식: 백·빅·상·하·샌</h4>',
     '<h4 id="s10-통합">통합 테스트 방식: 백·빅·상·하·샌</h4>'),
    ('<h4>인수 테스트 유형: 사·운·계·규·알·베</h4>',
     '<h4 id="s10-인수">인수 테스트 유형: 사·운·계·규·알·베</h4>'),
    ('<h4>성능 테스트 유형: 단·복·임 / 루·스·확·가·티 / 부·스·내·볼</h4>',
     '<h4 id="s11-성능">성능 테스트 유형: 단·복·임 / 루·스·확·가·티 / 부·스·내·볼</h4>'),
    ('<h4>TMMi 성숙도 개요</h4>', '<h4 id="s14-tmmi">TMMi 성숙도 개요</h4>'),
    ('<h4>ISO/IEC/IEEE 29119 구성: 버·프·독·기·키</h4>',
     '<h4 id="s14-29119">ISO/IEC/IEEE 29119 구성: 버·프·독·기·키</h4>'),
]

ITEM_RE = re.compile(
    r'(<details class="mnemonic-item">\s*'
    r'<summary><span class="mn-from">[^<]*</span><span class="mn-key">)([^<]+)(</span></summary>.*?'
    r'<details class="mn-more">\s*<summary>설명 보기</summary>.*?'
    r')(<p><a href="[^"]*">[^<]*</a>(?:\s*·\s*<a href="[^"]*">[^<]*</a>)?</p>)',
    re.DOTALL,
)


def link_html(target):
    if target.startswith("<p>"):
        return target
    return f'<p><a href="{target}">→ 본문 이동</a></p>'


def patch_page(path_key, mapping):
    path = ROOT / path_key
    text = path.read_text(encoding="utf-8")
    changed = 0

    def repl(m):
        nonlocal changed
        key = m.group(2)
        if key not in mapping:
            return m.group(0)
        changed += 1
        return m.group(1) + key + m.group(3) + link_html(mapping[key])

    text = ITEM_RE.sub(repl, text)
    path.write_text(text, encoding="utf-8")
    print(f"{path_key}: updated {changed} mnemonic links")


def add_sw02_ids():
    path = ROOT / "pages/02-sw테스트.html"
    text = path.read_text(encoding="utf-8")
    n = 0
    for old, new in SW02_H4_IDS:
        if old in text and new not in text:
            text = text.replace(old, new, 1)
            n += 1
    path.write_text(text, encoding="utf-8")
    print(f"pages/02-sw테스트.html: added {n} h4 anchors")


def main():
    add_sw02_ids()
    for path_key, mapping in LINK_MAP.items():
        patch_page(path_key, mapping)


if __name__ == "__main__":
    main()
