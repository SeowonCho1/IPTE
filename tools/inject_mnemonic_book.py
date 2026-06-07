# -*- coding: utf-8 -*-
"""Inject collapsible mnemonic book into study pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_LINK = '<link rel="stylesheet" href="../assets/mnemonic-book.css"/>'
MARKER = '<!-- MNEMONIC_BOOK -->'
FILTER_JS = """
function filterMnemonics(inp){
  const q=(inp.value||'').toLowerCase().trim();
  const list=inp.closest('.mnemonic-book-section');
  if(!list) return;
  list.querySelectorAll('.mnemonic-item').forEach(el=>{
    el.classList.toggle('hidden', q && !el.textContent.toLowerCase().includes(q));
  });
}"""

def item(key, source, split, explain, link="#", link_text="→ 본문 이동", extra_links=None):
    if extra_links:
        links = " · ".join(f'<a href="{h}">{t}</a>' for h, t in extra_links)
        links_html = f"<p>{links}</p>"
    else:
        links_html = f'<p><a href="{link}">{link_text}</a></p>'
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

def book(title, items_html):
    return f'''{MARKER}
<section class="panel mnemonic-book-section" id="mnemonic-book">
<details class="mnemonic-book-wrap" open>
<summary><span class="mn-wrap-title">{title}</span><span class="mn-wrap-hint">전체 접기/펼치기</span></summary>
<div class="mnemonic-book-body">
<p class="subtle">두음 → 출처(몇 장) → 풀이 → 설명을 단계별로 접었다 펼칠 수 있습니다.</p>
<input class="mn-filter" type="search" placeholder="두음 검색 (예: 작방, 결완, 기신…)" oninput="filterMnemonics(this)"/>
<div class="mnemonic-list">
{items_html}
</div>
</div>
</details>
</section>
'''

SW01 = book("📖 두음 모음집 — SW공학", "\n".join([
    item("타요설개테운폐", "1. SW·SDLC",
         "타(당성) · 요(구) · 설(계) · 개(발) · 테(스트) · 운(영) · 폐(기)",
         "<p>SW 생명주기 7단계 순서입니다. 타당성검토부터 폐기까지 전 과정을 체계적으로 관리한다는 답안 골격에 씁니다.</p>",
         "#1-4-SDLC"),
    item("비복비복변순무개", "1. SW 특성",
         "비(가시) · 복(잡) · 비(마모) · 복(제) · 변(경) · 순(응) · 무(형) · 개(발중심)",
         "<p>소프트웨어의 대표 특성 두음입니다. 비가시·복잡·변경 때문에 문서화·모듈화·형상관리·품질 측정이 필요하다는 논리로 연결합니다.</p>",
         "#1-1-소프트웨어의-개념과-특성"),
    item("작방산관기도", "3. SW 개발방법론",
         "작(업절차) · 방(법) · 산(출물) · 관(리) · 기(법) · 도(구)",
         "<p>개발방법론의 6대 구성요소입니다. SDLC 단계를 <em>어떤 순서·방식</em>으로 수행하고, <em>무엇을 산출</em>하며, <em>어떻게 관리</em>할지, <em>기법·도구</em>까지 표준화한 것이 방법론입니다. 구조적·OO·CBD 비교 답안의 공통 틀입니다.</p>",
         "#3-1-주요-구성"),
    item("캡추다정상", "3. 객체지향",
         "캡(슐화) · 추(상화) · 다(형성) · 정(보은닉) · 상(속)",
         "<p>객체지향 5대 원리(캡추다정상)입니다. 변경 영향 최소화·재사용·유지보수성 답안에 필수 키워드로 연결합니다.</p>",
         "#3-3-객체지향-핵심-원리"),
    item("개변동고", "4. Agile",
         "개(인과 상호작용) · 변(화 대응) · 동(작하는 SW) · 고(객 협력)",
         "<p>애자일 선언 4가지 핵심 가치(왼쪽 우선)입니다. 계획·문서보다 사람·변화·동작 SW·고객 협력을 강조합니다.</p>",
         "#4-1-Agile"),
    item("용단커피존", "4. XP",
         "용(기) · 단(순성) · 커(뮤니케이션) · 피(드백) · 존(중)",
         "<p>익스트림 프로그래밍(XP) 5가지 가치입니다. 페어 프로그래밍·TDD·CI와 함께 씁니다.</p>",
         "#4-2-XP"),
    item("CALMS / 빈·리·복·실", "5. DevOps",
         "CALMS: Culture·Automation·Lean·Measurement·Sharing / DORA: 빈(도) · 리(드타임) · 복(구) · 실(패율)",
         "<p>DevOps는 CALMS 5원칙으로 Dev·Ops를 통합하고, DORA 4 Metrics로 배포 성과를 정량 평가합니다.</p>",
         extra_links=[("#5-2-1-CALMS", "→ CALMS 본문"), ("#5-2-2-DORA", "→ DORA 본문")]),
    item("코드·버전·멱등·GitOps", "5. IaC",
         "코드 정의 · Git 버전관리 · 멱등 적용 · GitOps 자동 반영",
         "<p>Infrastructure as Code 핵심입니다. 인프라를 코드로 관리해 재현성·일관성을 확보하고 CI/CD·GitOps와 결합합니다.</p>",
         "#5-2-3-IaC"),
    item("아동아식품분우분발", "6. ATAM",
         "아(TAM소개) · 동(인) · 아(키텍처소개) · 식(별) · 품(질속성트리) · 분(석) · 우(선순위) · 분(석반복) · 발(표)",
         "<p>아키텍처 평가 기법 ATAM 9단계 순서입니다. 품질속성 Trade-off 분석 답안 구조로 활용합니다.</p>",
         "#6-4-아키텍처-평가"),
    item("도분명검관", "9. 요구공학",
         "도(출) · 분(석) · 명(세) · 검(증) · 관(리)",
         "<p>요구공학 5대 프로세스입니다. 이해관계자 요구를 수집·분석·명세·검증·변경관리하는 흐름입니다.</p>",
         "#9-2-요구공학-프로세스"),
    item("기신사효유이", "10. ISO 9126",
         "기(능) · 신(뢰) · 사(용) · 효(율) · 유(지보수) · 이(식)",
         "<p>구 ISO/IEC 9126 제품 품질 6특성입니다. 25010으로 확장·개편되었으나 기출 암기용으로 자주 나옵니다.</p>",
         "#10-3-ISO-IEC-9126"),
    item("기성호상신보유유안", "10. ISO 25010",
         "기능적합 · 성능효율 · 호환 · 상호작용 · 신뢰 · 보안 · 유지보수 · 유연 · 안전",
         "<p>ISO/IEC 25010:2023 품질 모델 9특성입니다. 비기능 요구·테스트(SW테스트)와 1:1 연결됩니다.</p>",
         "#10-5-ISO-IEC-25010-2023-품질-특성"),
    item("요모관측평확", "10. SQuaRE",
         "요(구) · 모(델) · 관(리) · 측(정) · 평(가) · 확(장)",
         "<p>ISO/IEC 25000 SQuaRE 시리즈 구성입니다. 9126·14598·12119를 통합한 품질 표준 체계입니다.</p>",
         "#10-4-ISO-IEC-25000-SQuaRE"),
    item("기지조 / 초관정관최", "11. 프로세스 품질",
         "기지조: 기(본)·지(원)·조(직) 프로세스 / 초관정관최: CMMI 1~5단계",
         "<p>12207 생명주기 프로세스 분류와 CMMI 성숙도 5단계입니다. SPICE·TMMi(SW테스트)와 성숙도 비교 답안에 활용합니다.</p>",
         extra_links=[("#11-1-ISO-IEC-12207", "→ 기지조(12207)"), ("#11-3-CMM-CMMI", "→ 초관정관최(CMMI)")]),
    item("고응집·저결합", "12. 모듈화",
         "응집도는 높게, 결합도는 낮게",
         "<p>모듈화·설계 원칙의 핵심 한 줄입니다. 변경 영향 최소화·유지보수성 답안의 결론 문장으로 씁니다.</p>",
         "#12-2-모듈화"),
    item("심노제", "13. ASIL",
         "심(각도 Severity) · 노(출도 Exposure) · 제(어가능성 Controllability)",
         "<p>자동차 기능안전 ISO 26262에서 ASIL 등급을 정하는 3가지 지표입니다.</p>",
         "#13-4-ISO-26262과-ASIL"),
]))

SW02 = book("📖 두음 모음집 — SW테스트", "\n".join([
    item("결완초집살정오", "1. 테스트 7원리",
         "결(함존재) · 완(벽불가) · 초(기테스트) · 집(중) · 살(충제) · 정(황의존) · 오(류부재궤변)",
         "<p>SW 테스트 7원리 최고 빈출 두음입니다. 각 원리별로 정의+적용 방향 한 줄씩 붙여 답안을 만듭니다.</p>",
         "#s1-7원리"),
    item("식항입출환특의", "3. 테스트 케이스",
         "식(별자) · 항(목) · 입(력) · 출(력) · 환(경) · 특(수절차) · 의(존성)",
         "<p>테스트 케이스 7대 구성요소입니다. 케이스 설계·명세 답안에서 표로 풀어 씁니다.</p>",
         "#s3-케이스"),
    item("완목기커리스", "3. 완료조건",
         "완(전성) · 목(적) · 기(준) · 커(버리지) · 리(스크) · 스(케줄)",
         "<p>테스트 종료(Exit) 판단 6가지 기준입니다. MTP·완료조건 답안에 필수입니다.</p>",
         "#s3-완료조건"),
    item("동경결상유페직원분", "7. 명세기반",
         "동(등분할) · 경(계값) · 결(정테이블) · 상(태전이) · 유(스케이스) · 페(어와이즈) · 직(교) · 원(인결과) · 분(류트리)",
         "<p>블랙박스(명세기반) 설계기법 9종입니다. 기법별 개념·적용 상황 비교표와 함께 씁니다.</p>",
         "#s7-명세기반"),
    item("탐분체특오혹", "9. 경험기반",
         "탐(색적) · 분(류트리) · 체(크리스트) · 특(성) · 오(류추정) · 혹(애드혹)",
         "<p>경험기반 테스트 6기법입니다. 명세 부족·탐색적 상황 답안에 활용합니다.</p>",
         "#s9-경험기반"),
    item("백빅상하샌", "10. 통합 테스트",
         "백(본) · 빅(뱅) · 상(향식) · 하(향식) · 샌(드위치)",
         "<p>통합 테스트 5방식입니다. 상향=Stub, 하향=Driver 필요 여부와 함께 비교합니다.</p>",
         "#s10-통합"),
    item("사운계규알베", "10. 인수 테스트",
         "사(용자) · 운(영) · 계(약) · 규(정) · 알(파) · 베(타)",
         "<p>인수 테스트 유형 6가지입니다. 확인(Validation) 관점 답안에 연결합니다.</p>",
         "#s10-인수"),
    item("단복임 / 루스확가티 / 부스내볼", "11. 성능 테스트",
         "단·복·임(목적) / 루프백·스파이크·확장·가용·티어(병목) / 부하·스트레스·내구·볼륨(부하관리)",
         "<p>성능 테스트 분류 3축입니다. 비기능 테스트 답안에서 표로 정리합니다.</p>",
         "#s11-성능"),
    item("버프독기키", "14. ISO 29119",
         "버(전개념) · 프(로세스) · 독(문서) · 기(법) · 키(워드)",
         "<p>ISO/IEC/IEEE 29119 5파트 구성입니다. 테스트 프로세스 국제 표준 답안 골격입니다.</p>",
         "#s14-29119"),
    item("초관정관최 ↔ TMMi", "14. 성숙도",
         "TMMi 1~5: Initial·Managed·Defined·Measured·Optimization (CMMI·SPICE와 병렬 비교)",
         "<p>테스트 성숙도 모델 TMMi입니다. SW공학 CMMI·SPICE와 단계별 비교표로 쓰면 가산점에 유리합니다.</p>",
         "#s14-tmmi"),
    item("차박노디", "9. 탐색적 테스트",
         "차(터) · 박(싱) · 노(트) · 디(브리프)",
         "<p>탐색적 테스트 4요소입니다. 애드혹과 달리 목표·시간·기록이 있습니다.</p>",
         "#s9-탐색적"),
]))

SW03 = book("📖 두음 모음집 — 경영컨설팅", "\n".join([
    item("키-사-시", "0. 답안 확장",
         "키(워드) · 사(례) · 시(사점)",
         "<p>경영컨설팅 답안 기본 공식입니다. 프레임워크만 쓰지 말고 기업 사례와 전략적 시사점을 반드시 붙입니다.</p>",
         "#study-0"),
    item("목-이-평-전", "1. 경영전략",
         "목(표) · 이(해) · 평(가) · 전(략)",
         "<p>경영전략 수립 흐름: 목표 설정 → 환경 이해 → 평가 → 전략 수립. IT전략은 프로세스·시스템으로 구체화합니다.</p>",
         "#strategy-0"),
    item("정-경-사-기 + 환-법", "1. PESTEL",
         "정(치) · 경(제) · 사(회) · 기(술) · 환(경) · 법(률)",
         "<p>거시환경 분석 PEST/STEEP/PESTEL 두음입니다. 외부 기회·위협 도출에 씁니다.</p>",
         "#strategy-1"),
    item("기-잠-대-구-공", "1. Porter 5 Force",
         "기(존경쟁) · 잠(재진입) · 대(체재) · 구(매자) · 공(급자)",
         "<p>산업 구조·수익성 분석 5요인입니다. 경쟁 강도와 산업 매력도 평가에 활용합니다.</p>",
         "#strategy-2"),
    item("투-운-산-마-서 / 조-기-인-구", "1. Value Chain",
         "주활동: 투입·운영·산출·마케팅·서비스 / 지원: 조직·기술·인적·구매",
         "<p>포터 밸류체인 주활동 5 + 지원활동 4입니다. 원가우위·차별화 원천 분석에 씁니다.</p>",
         "#strategy-3"),
    item("강약기위 / 자경고 / 세목위", "1. SWOT·3C·STP",
         "SWOT: 강·약·기·위 / 3C: 자사·경쟁·고객 / STP: 세분·목표·포지셔닝",
         "<p>내부·외부 환경 통합 전략 프레임워크 묶음입니다. SO/ST/WO/WT 전략대안과 연결합니다.</p>",
         "#strategy-5"),
    item("원-차-집", "2. Porter 경쟁전략",
         "원(가주도) · 차(별화) · 집(중화)",
         "<p>본원적 경쟁전략 3가지입니다. 전사·사업부 전략 답안의 핵심 분기입니다.</p>",
         "#investment-1"),
    item("별-돈-물-개", "2. BCG Matrix",
         "별(Star) · 돈(Cash Cow) · 물(Question Mark) · 개(Dog)",
         "<p>BCG 4사분면 암기입니다. LG전자 HA·AC=Cash Cow, MC·HE=Question Mark 사례와 함께 씁니다.</p>",
         "#investment-2"),
    item("제-감-증-창", "2. ERRC",
         "제(거) · 감(소) · 증(대) · 창(조)",
         "<p>블루오션 ERRC 그리드입니다. 하이트맥주 사례(조선·크라운 이미지 제거, 청량감 창조)와 함께 씁니다.</p>",
         "#investment-3"),
    item("발-정-개-전 / 공-정-상-시-검", "3. Design Thinking",
         "Double Diamond: 발견·정의·개발·전달 / DT 5단계: 공감·정의·아이디어·시제품·검증",
         "<p>디자인 씽킹·더블다이아몬드 두 흐름입니다. Oral-B·BoA·현대카드 사례와 연결합니다.</p>",
         "#innovation-2"),
    item("모순-분리-발명원리", "3. TRIZ",
         "기술적·물리적 모순 → 분리 원리 → 40발명 원리",
         "<p>TRIZ 핵심 흐름입니다. 자동차 가변실린더·자전거 체인 사례로 모순 해결을 설명합니다.</p>",
         "#innovation-1"),
]))

PAGES = {
    "pages/01-sw공학.html": {
        "book": SW01,
        "sidebar_old": '<p class="sidebar-title">📌 목차</p><a href="#0-공부',
        "sidebar_new": '<p class="sidebar-title">📌 목차</p><a href="#mnemonic-book">📖 두음 모음집</a><a href="#0-공부',
        "mobile_old": '<details><summary>목차 열기</summary><a href="#0-공부',
        "mobile_new": '<details><summary>목차 열기</summary><a href="#mnemonic-book">📖 두음 모음집</a><a href="#0-공부',
        "insert_before": '<section class="panel" id="analysis">',
    },
    "pages/02-sw테스트.html": {
        "book": SW02,
        "sidebar_old": '<p class="sidebar-title">📌 목차</p>\n    <a href="#s0">',
        "sidebar_new": '<p class="sidebar-title">📌 목차</p>\n    <a href="#mnemonic-book">📖 두음 모음집</a>\n    <a href="#s0">',
        "mobile_old": '<summary>목차 열기</summary>\n        <a href="#s0">',
        "mobile_new": '<summary>목차 열기</summary>\n        <a href="#mnemonic-book">📖 두음 모음집</a>\n        <a href="#s0">',
        "insert_before": '<section id="s0" class="topic">',
    },
    "pages/03-경영컨설팅.html": {
        "book": SW03,
        "sidebar_old": '<nav><a href="#study">',
        "sidebar_new": '<nav><a href="#mnemonic-book">📖 두음 모음집</a><a href="#study">',
        "mobile_old": '<div class="toc-links"><a href="#study">',
        "mobile_new": '<div class="toc-links"><a href="#mnemonic-book">📖 두음 모음집</a><a href="#study">',
        "insert_before": '  <section id="study" class="section">',
    },
}

def inject(path_key, cfg):
    path = ROOT / path_key
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        print(f"skip (already injected): {path_key}")
        return
    if CSS_LINK not in text:
        text = text.replace('<link rel="stylesheet" href="../assets/diagrams.css"/>',
                            '<link rel="stylesheet" href="../assets/diagrams.css"/>\n' + CSS_LINK)
    text = text.replace(cfg["sidebar_old"], cfg["sidebar_new"], 1)
    if "mobile_old" in cfg and cfg["mobile_old"] in text:
        text = text.replace(cfg["mobile_old"], cfg["mobile_new"], 1)
    text = text.replace(cfg["insert_before"], cfg["book"] + "\n" + cfg["insert_before"], 1)
    if "function filterMnemonics" not in text:
        text = text.replace("</script>", FILTER_JS + "\n</script>", 1)
    path.write_text(text, encoding="utf-8")
    print(f"injected: {path_key}")

def main():
    for k, v in PAGES.items():
        inject(k, v)

if __name__ == "__main__":
    main()
