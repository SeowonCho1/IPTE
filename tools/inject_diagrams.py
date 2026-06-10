# -*- coding: utf-8 -*-
"""Insert SVG flow diagrams into study HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_LINK = '<link rel="stylesheet" href="../assets/diagrams.css"/>'

DEFS = '''<defs>
  <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#64748b"/></marker>
  <marker id="arrowhead-blue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#2563eb"/></marker>
</defs>'''

DIAGRAMS = {
    "sdlc": f'''<figure class="svg-diagram" aria-label="SDLC 7단계">
<svg viewBox="0 0 420 520" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="110" y="10" width="200" height="44" rx="8"/><text class="label" x="210" y="38" text-anchor="middle">타당성 검토</text>
<line class="arrow-blue" x1="210" y1="54" x2="210" y2="74"/>
<rect class="box" x="110" y="74" width="200" height="44" rx="8"/><text class="label" x="210" y="102" text-anchor="middle">요구분석</text>
<line class="arrow-blue" x1="210" y1="118" x2="210" y2="138"/>
<rect class="box" x="110" y="138" width="200" height="44" rx="8"/><text class="label" x="210" y="166" text-anchor="middle">설계</text>
<line class="arrow-blue" x1="210" y1="182" x2="210" y2="202"/>
<rect class="box" x="110" y="202" width="200" height="44" rx="8"/><text class="label" x="210" y="230" text-anchor="middle">개발(구현)</text>
<line class="arrow-blue" x1="210" y1="246" x2="210" y2="266"/>
<rect class="box" x="110" y="266" width="200" height="44" rx="8"/><text class="label" x="210" y="294" text-anchor="middle">테스트</text>
<line class="arrow-blue" x1="210" y1="310" x2="210" y2="330"/>
<rect class="box-alt" x="110" y="330" width="200" height="44" rx="8"/><text class="label" x="210" y="358" text-anchor="middle">운영·유지보수</text>
<line class="arrow-blue" x1="210" y1="374" x2="210" y2="394"/>
<rect class="box-warn" x="110" y="394" width="200" height="44" rx="8"/><text class="label" x="210" y="422" text-anchor="middle">폐기</text>
<text class="label-sm" x="210" y="470" text-anchor="middle">암기: 타요설개테운폐 — 순차 진행, 단계별 산출물</text>
</svg>
<figcaption>SDLC 7단계 순서도</figcaption>
</figure>''',

    "waterfall": f'''<figure class="svg-diagram" aria-label="폭포수 모델">
<svg viewBox="0 0 360 430" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="80" y="8" width="200" height="40" rx="8"/><text class="label" x="180" y="34" text-anchor="middle">요구사항 분석</text>
<line class="arrow-blue" x1="180" y1="48" x2="180" y2="68"/>
<rect class="box" x="80" y="68" width="200" height="40" rx="8"/><text class="label" x="180" y="94" text-anchor="middle">설계</text>
<line class="arrow-blue" x1="180" y1="108" x2="180" y2="128"/>
<rect class="box" x="80" y="128" width="200" height="40" rx="8"/><text class="label" x="180" y="154" text-anchor="middle">구현(코딩)</text>
<line class="arrow-blue" x1="180" y1="168" x2="180" y2="188"/>
<rect class="box" x="80" y="188" width="200" height="40" rx="8"/><text class="label" x="180" y="214" text-anchor="middle">테스트</text>
<line class="arrow-blue" x1="180" y1="228" x2="180" y2="248"/>
<rect class="box-alt" x="80" y="248" width="200" height="40" rx="8"/><text class="label" x="180" y="274" text-anchor="middle">운영·유지보수</text>
<polygon points="180,310 130,360 230,360" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
<text class="label-sm" x="180" y="345" text-anchor="middle">순차·문서화</text>
<text class="label-sm" x="180" y="400" text-anchor="middle">변경 대응 어려움 — 요구가 명확할 때 적합</text>
</svg>
<figcaption>폭포수(Waterfall) 모델 — 위에서 아래로 한 방향 진행</figcaption>
</figure>''',

    "prototype": f'''<figure class="svg-diagram" aria-label="프로토타입 모델">
<svg viewBox="0 0 440 280" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="20" y="100" width="90" height="40" rx="8"/><text class="label" x="65" y="126" text-anchor="middle">요구</text>
<line class="arrow-blue" x1="110" y1="120" x2="130" y2="120"/>
<rect class="box-warn" x="130" y="100" width="90" height="40" rx="8"/><text class="label" x="175" y="126" text-anchor="middle">시제품</text>
<line class="arrow-blue" x1="220" y1="120" x2="240" y2="120"/>
<rect class="box" x="240" y="100" width="90" height="40" rx="8"/><text class="label" x="285" y="126" text-anchor="middle">평가</text>
<line class="arrow-blue" x1="330" y1="120" x2="350" y2="120"/>
<rect class="box-alt" x="350" y="100" width="70" height="40" rx="8"/><text class="label" x="385" y="126" text-anchor="middle">개선</text>
<path class="dash" d="M385 100 Q385 40 175 40 Q65 40 65 100"/>
<text class="label-sm" x="220" y="28" text-anchor="middle">피드백 반복 → 요구 구체화</text>
<text class="label-sm" x="220" y="250" text-anchor="middle">UI·요구 불명확할 때 — 사용자 피드백 중심</text>
</svg>
<figcaption>프로토타입 모델 — 시제품으로 요구를 구체화</figcaption>
</figure>''',

    "spiral": f'''<figure class="svg-diagram" aria-label="나선형 모델">
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<circle cx="200" cy="200" r="150" fill="none" stroke="#e2e8f0" stroke-width="2"/>
<path d="M200 200 L200 50 A150 150 0 0 1 350 200 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
<path d="M200 200 L350 200 A150 150 0 0 1 200 350 Z" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
<path d="M200 200 L200 350 A150 150 0 0 1 50 200 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
<path d="M200 200 L50 200 A150 150 0 0 1 200 50 Z" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5"/>
<text class="label" x="260" y="115">계획</text>
<text class="label" x="285" y="230">위험분석</text>
<text class="label" x="155" y="285">개발·검증</text>
<text class="label" x="90" y="170">고객평가</text>
<circle cx="200" cy="200" r="35" fill="#1e293b"/><text class="label-light" x="200" y="205" text-anchor="middle">반복</text>
<text class="label-sm" x="200" y="375" text-anchor="middle">대규모·고위험 프로젝트 — 매 회전마다 위험 분석</text>
</svg>
<figcaption>나선(Spiral) 모델 — 4단계를 나선형으로 반복</figcaption>
</figure>''',

    "vmodel": f'''<figure class="svg-diagram" aria-label="V 모델">
<svg viewBox="0 0 520 340" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="130" y="22" text-anchor="middle">개발(Verification)</text>
<text class="label-sm" x="390" y="22" text-anchor="middle">테스트(Validation)</text>
<rect class="box" x="20" y="40" width="130" height="36" rx="6"/><text class="label-sm" x="85" y="63" text-anchor="middle">요구분석</text>
<rect class="box-test" x="370" y="40" width="130" height="36" rx="6"/><text class="label-sm" x="435" y="63" text-anchor="middle">인수 테스트</text>
<line class="dash" x1="150" y1="58" x2="370" y2="58"/>
<rect class="box" x="35" y="90" width="115" height="36" rx="6"/><text class="label-sm" x="92" y="113" text-anchor="middle">시스템 설계</text>
<rect class="box-test" x="355" y="90" width="130" height="36" rx="6"/><text class="label-sm" x="420" y="113" text-anchor="middle">시스템 테스트</text>
<line class="dash" x1="150" y1="108" x2="355" y2="108"/>
<rect class="box" x="50" y="140" width="110" height="36" rx="6"/><text class="label-sm" x="105" y="163" text-anchor="middle">아키텍처 설계</text>
<rect class="box-test" x="340" y="140" width="130" height="36" rx="6"/><text class="label-sm" x="405" y="163" text-anchor="middle">통합 테스트</text>
<line class="dash" x1="160" y1="158" x2="340" y2="158"/>
<rect class="box" x="65" y="190" width="100" height="36" rx="6"/><text class="label-sm" x="115" y="213" text-anchor="middle">모듈 설계</text>
<rect class="box-test" x="325" y="190" width="130" height="36" rx="6"/><text class="label-sm" x="390" y="213" text-anchor="middle">단위 테스트</text>
<line class="dash" x1="165" y1="208" x2="325" y2="208"/>
<polygon points="260,250 220,290 300,290" class="box-dark"/><text class="label-light" x="260" y="278" text-anchor="middle">코딩</text>
<text class="label-sm" x="260" y="325" text-anchor="middle">좌: 올바르게 만들고 있는가(검증) ↔ 우: 올바른 제품인가(확인)</text>
</svg>
<figcaption>V-모델 — 개발 단계와 테스트 단계 1:1 대응</figcaption>
</figure>''',

    "scrum": f'''<figure class="svg-diagram" aria-label="Scrum 스프린트">
<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="10" y="70" width="100" height="44" rx="8"/><text class="label-sm" x="60" y="97" text-anchor="middle">Product</text><text class="label-sm" x="60" y="108" text-anchor="middle">Backlog</text>
<line class="arrow-blue" x1="110" y1="92" x2="130" y2="92"/>
<rect class="box-warn" x="130" y="70" width="110" height="44" rx="8"/><text class="label-sm" x="185" y="97" text-anchor="middle">Sprint</text><text class="label-sm" x="185" y="108" text-anchor="middle">Planning</text>
<line class="arrow-blue" x1="240" y1="92" x2="260" y2="92"/>
<rect class="box" x="260" y="55" width="90" height="34" rx="6"/><text class="label-sm" x="305" y="76" text-anchor="middle">Daily Scrum</text>
<rect class="box" x="260" y="95" width="90" height="34" rx="6"/><text class="label-sm" x="305" y="116" text-anchor="middle">개발</text>
<line class="arrow-blue" x1="350" y1="92" x2="370" y2="92"/>
<rect class="box-alt" x="370" y="70" width="110" height="44" rx="8"/><text class="label-sm" x="425" y="97" text-anchor="middle">Review</text><text class="label-sm" x="425" y="108" text-anchor="middle">Retro</text>
<path class="dash" d="M480 92 Q490 160 60 160 Q10 160 10 114"/>
<text class="label-sm" x="250" y="185" text-anchor="middle">2~4주 스프린트 반복 — Increment 누적</text>
</svg>
<figcaption>Scrum 스프린트 흐름</figcaption>
</figure>''',

    "test_process": f'''<figure class="svg-diagram" aria-label="테스트 프로세스">
<svg viewBox="0 0 380 420" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="90" y="10" width="200" height="40" rx="8"/><text class="label" x="190" y="36" text-anchor="middle">Test Basis</text>
<line class="arrow-blue" x1="190" y1="50" x2="190" y2="70"/>
<rect class="box" x="70" y="70" width="240" height="40" rx="8"/><text class="label-sm" x="190" y="96" text-anchor="middle">Test Case → Suite → Procedure</text>
<line class="arrow-blue" x1="190" y1="110" x2="190" y2="130"/>
<rect class="box-warn" x="50" y="130" width="280" height="40" rx="8"/><text class="label-sm" x="190" y="156" text-anchor="middle">Test Bed (Target·Harness·Driver·Stub)</text>
<line class="arrow-blue" x1="190" y1="170" x2="190" y2="190"/>
<rect class="box" x="60" y="190" width="260" height="40" rx="8"/><text class="label-sm" x="190" y="216" text-anchor="middle">Test Log / Incident / Report</text>
<line class="arrow-blue" x1="190" y1="230" x2="190" y2="250"/>
<rect class="box-test" x="80" y="250" width="220" height="40" rx="8"/><text class="label-sm" x="190" y="276" text-anchor="middle">Oracle 비교 → 완료조건 판단</text>
<text class="label-sm" x="190" y="330" text-anchor="middle">Basis → Case → Bed → 실행 → Oracle → Exit</text>
</svg>
<figcaption>테스트 프로세스 흐름</figcaption>
</figure>''',

    "test_levels": f'''<figure class="svg-diagram" aria-label="테스트 레벨">
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" role="img">
<polygon points="200,20 370,280 30,280" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<polygon points="200,70 320,260 80,260" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
<polygon points="200,120 270,240 130,240" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<polygon points="200,170 220,220 180,220" fill="#1d4ed8" stroke="#1e40af" stroke-width="1.5"/>
<text class="label" x="200" y="55" text-anchor="middle">인수 테스트</text>
<text class="label-sm" x="200" y="100" text-anchor="middle">시스템 테스트</text>
<text class="label-sm" x="200" y="155" text-anchor="middle">통합 테스트</text>
<text class="label-light" x="200" y="200" text-anchor="middle">단위</text>
<text class="label-sm" x="200" y="300" text-anchor="middle">아래→위로 확장 · Driver(상향) / Stub(하향)</text>
</svg>
<figcaption>기능 테스트 레벨 — 단위 → 통합 → 시스템 → 인수</figcaption>
</figure>''',

    "porter5": f'''<figure class="svg-diagram" aria-label="포터 5 Forces">
<svg viewBox="0 0 420 380" xmlns="http://www.w3.org/2000/svg" role="img">
<rect class="box-dark" x="150" y="150" width="120" height="60" rx="10"/><text class="label-light" x="210" y="185" text-anchor="middle">기존</text><text class="label-light" x="210" y="198" text-anchor="middle">경쟁사</text>
<rect class="box-warn" x="150" y="16" width="120" height="50" rx="8"/><text class="label-sm" x="210" y="40" text-anchor="middle">잠재적</text><text class="label-sm" x="210" y="54" text-anchor="middle">경쟁자</text>
<rect class="box" x="160" y="300" width="100" height="44" rx="8"/><text class="label-sm" x="210" y="327" text-anchor="middle">대체재</text>
<rect class="box-alt" x="20" y="158" width="100" height="44" rx="8"/><text class="label-sm" x="70" y="185" text-anchor="middle">구매자</text>
<rect class="box-test" x="300" y="158" width="100" height="44" rx="8"/><text class="label-sm" x="350" y="185" text-anchor="middle">공급자</text>
<line class="arrow" x1="210" y1="66" x2="210" y2="150"/>
<line class="arrow" x1="210" y1="210" x2="210" y2="300"/>
<line class="arrow" x1="120" y1="180" x2="150" y2="180"/>
<line class="arrow" x1="300" y1="180" x2="270" y2="180"/>
<text class="label-sm" x="210" y="370" text-anchor="middle">암기: 기-잠-대-구-공 — 산업 수익성·경쟁강도 분석</text>
</svg>
<figcaption>마이클 포터 5 Forces</figcaption>
</figure>''',

    "value_chain": f'''<figure class="svg-diagram" aria-label="Value Chain">
<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg" role="img">
<rect fill="#f1f5f9" stroke="#94a3b8" x="10" y="10" width="540" height="36" rx="6"/><text class="label-sm" x="280" y="33" text-anchor="middle">지원활동: 인프라 · HR · 기술개발 · 구매조달</text>
<rect class="box" x="10" y="60" width="95" height="50" rx="6"/><text class="label-sm" x="57" y="90" text-anchor="middle">투입물류</text>
<rect class="box" x="115" y="60" width="95" height="50" rx="6"/><text class="label-sm" x="162" y="90" text-anchor="middle">운영</text>
<rect class="box" x="220" y="60" width="95" height="50" rx="6"/><text class="label-sm" x="267" y="90" text-anchor="middle">출력물류</text>
<rect class="box" x="325" y="60" width="95" height="50" rx="6"/><text class="label-sm" x="372" y="90" text-anchor="middle">마케팅</text>
<rect class="box-alt" x="430" y="60" width="95" height="50" rx="6"/><text class="label-sm" x="477" y="90" text-anchor="middle">서비스</text>
<line class="arrow-blue" x1="105" y1="85" x2="115" y2="85"/><line class="arrow-blue" x1="210" y1="85" x2="220" y2="85"/>
<line class="arrow-blue" x1="315" y1="85" x2="325" y2="85"/><line class="arrow-blue" x1="420" y1="85" x2="430" y2="85"/>
<text class="label-sm" x="280" y="145" text-anchor="middle">주활동: 투-운-산-마-서</text>
<text class="label-sm" x="280" y="195" text-anchor="middle">마진·경쟁우위 = 활동별 비용·가치 분석</text>
</svg>
<figcaption>포터 Value Chain — 주활동 + 지원활동</figcaption>
</figure>''',

    "bcg": f'''<figure class="svg-diagram" aria-label="BCG Matrix">
<svg viewBox="0 0 360 340" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="180" y1="30" x2="180" y2="300" stroke="#cbd5e1" stroke-width="2"/>
<line x1="30" y1="165" x2="330" y2="165" stroke="#cbd5e1" stroke-width="2"/>
<text class="label-sm" x="180" y="20" text-anchor="middle">시장성장률 ↑</text>
<text class="label-sm" transform="rotate(-90 18 165)" x="18" y="165" text-anchor="middle">상대시장점유율 →</text>
<rect class="box-warn" x="40" y="40" width="130" height="110" rx="8"/><text class="label" x="105" y="90" text-anchor="middle">Question Mark</text><text class="label-sm" x="105" y="108" text-anchor="middle">물음표</text>
<rect class="box-alt" x="190" y="40" width="130" height="110" rx="8"/><text class="label" x="255" y="90" text-anchor="middle">Star</text><text class="label-sm" x="255" y="108" text-anchor="middle">별</text>
<rect class="box" x="40" y="180" width="130" height="110" rx="8"/><text class="label" x="105" y="230" text-anchor="middle">Dog</text><text class="label-sm" x="105" y="248" text-anchor="middle">개</text>
<rect class="box-test" x="190" y="180" width="130" height="110" rx="8"/><text class="label" x="255" y="230" text-anchor="middle">Cash Cow</text><text class="label-sm" x="255" y="248" text-anchor="middle">돈벌이</text>
<text class="label-sm" x="180" y="325" text-anchor="middle">LG전자: HA·AC=Cow, MC·HE=Question Mark</text>
</svg>
<figcaption>BCG Matrix — 성장률 × 점유율 포트폴리오</figcaption>
</figure>''',

    "swot": f'''<figure class="svg-diagram" aria-label="SWOT">
<svg viewBox="0 0 360 300" xmlns="http://www.w3.org/2000/svg" role="img">
<rect class="box-alt" x="20" y="20" width="150" height="110" rx="8"/><text class="label" x="95" y="55" text-anchor="middle">Strengths</text><text class="label-sm" x="95" y="75" text-anchor="middle">강점 (내부)</text><text class="label-sm" x="95" y="105" text-anchor="middle">→ SO 공격</text>
<rect class="box-warn" x="190" y="20" width="150" height="110" rx="8"/><text class="label" x="265" y="55" text-anchor="middle">Weaknesses</text><text class="label-sm" x="265" y="75" text-anchor="middle">약점 (내부)</text><text class="label-sm" x="265" y="105" text-anchor="middle">→ WO 전환</text>
<rect class="box" x="20" y="150" width="150" height="110" rx="8"/><text class="label" x="95" y="185" text-anchor="middle">Opportunities</text><text class="label-sm" x="95" y="205" text-anchor="middle">기회 (외부)</text>
<rect class="box-test" x="190" y="150" width="150" height="110" rx="8"/><text class="label" x="265" y="185" text-anchor="middle">Threats</text><text class="label-sm" x="265" y="205" text-anchor="middle">위협 (외부)</text><text class="label-sm" x="265" y="235" text-anchor="middle">→ WT 방어</text>
<text class="label-sm" x="180" y="285" text-anchor="middle">ST: 다양화 · WO: 방향전환 · WT: 방어·철수</text>
</svg>
<figcaption>SWOT 2×2 매트릭스</figcaption>
</figure>''',

    "inspection": f'''<figure class="svg-diagram" aria-label="인스펙션 절차">
<svg viewBox="0 0 480 120" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="5" y="35" width="68" height="40" rx="6"/><text class="label-sm" x="39" y="60" text-anchor="middle">계획</text>
<line class="arrow-blue" x1="73" y1="55" x2="83" y2="55"/>
<rect class="box" x="83" y="35" width="68" height="40" rx="6"/><text class="label-sm" x="117" y="60" text-anchor="middle">교육</text>
<line class="arrow-blue" x1="151" y1="55" x2="161" y2="55"/>
<rect class="box" x="161" y="35" width="68" height="40" rx="6"/><text class="label-sm" x="195" y="60" text-anchor="middle">준비</text>
<line class="arrow-blue" x1="229" y1="55" x2="239" y2="55"/>
<rect class="box-warn" x="239" y="35" width="68" height="40" rx="6"/><text class="label-sm" x="273" y="60" text-anchor="middle">회의</text>
<line class="arrow-blue" x1="307" y1="55" x2="317" y2="55"/>
<rect class="box" x="317" y="35" width="68" height="40" rx="6"/><text class="label-sm" x="351" y="60" text-anchor="middle">수정</text>
<line class="arrow-blue" x1="385" y1="55" x2="395" y2="55"/>
<rect class="box-alt" x="395" y="35" width="80" height="40" rx="6"/><text class="label-sm" x="435" y="60" text-anchor="middle">후속조치</text>
<text class="label-sm" x="240" y="105" text-anchor="middle">회의: 결함 기록만 — 현장 해결 금지</text>
</svg>
<figcaption>인스펙션 6단계 절차</figcaption>
</figure>''',

    "devops": f'''<figure class="svg-diagram" aria-label="DevOps DevSecOps 파이프라인">
<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="320" y="18" text-anchor="middle">DevSecOps 파이프라인 (Plan → Monitor)</text>
<rect class="box" x="8" y="40" width="72" height="36" rx="6"/><text class="label-sm" x="44" y="63" text-anchor="middle">Plan</text>
<line class="arrow-blue" x1="80" y1="58" x2="88" y2="58"/>
<rect class="box" x="88" y="40" width="72" height="36" rx="6"/><text class="label-sm" x="124" y="63" text-anchor="middle">Code</text>
<line class="arrow-blue" x1="160" y1="58" x2="168" y2="58"/>
<rect class="box" x="168" y="40" width="72" height="36" rx="6"/><text class="label-sm" x="204" y="63" text-anchor="middle">Build</text>
<line class="arrow-blue" x1="240" y1="58" x2="248" y2="58"/>
<rect class="box" x="248" y="40" width="72" height="36" rx="6"/><text class="label-sm" x="284" y="63" text-anchor="middle">Test</text>
<line class="arrow-blue" x1="320" y1="58" x2="328" y2="58"/>
<rect class="box-warn" x="328" y="40" width="88" height="36" rx="6"/><text class="label-sm" x="372" y="63" text-anchor="middle">Security</text>
<line class="arrow-blue" x1="416" y1="58" x2="424" y2="58"/>
<rect class="box-alt" x="424" y="40" width="80" height="36" rx="6"/><text class="label-sm" x="464" y="63" text-anchor="middle">Deploy</text>
<line class="arrow-blue" x1="504" y1="58" x2="512" y2="58"/>
<rect class="box-test" x="512" y="40" width="80" height="36" rx="6"/><text class="label-sm" x="552" y="63" text-anchor="middle">Monitor</text>
<text class="label-sm" x="372" y="105" text-anchor="middle">보안: SAST · SCA/SBOM · DAST · Image Scan · Runtime</text>
<ellipse cx="120" cy="155" rx="55" ry="28" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
<text class="label-sm" x="120" y="160" text-anchor="middle">Develop</text>
<ellipse cx="320" cy="155" rx="55" ry="28" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
<text class="label-sm" x="320" y="160" text-anchor="middle">DevOps</text>
<ellipse cx="520" cy="155" rx="55" ry="28" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
<text class="label-sm" x="520" y="160" text-anchor="middle">Operate</text>
<path class="dash" d="M175 155 Q250 120 265 155 Q380 190 395 155 Q470 120 465 155"/>
<text class="label-sm" x="320" y="192" text-anchor="middle">개발·운영 협업 · 자동화 · 측정 · 지속 개선</text>
</svg>
<figcaption>DevOps / DevSecOps — CI/CD 파이프라인 + Dev↔Ops 협업</figcaption>
</figure>''',

    "cmmi": f'''<figure class="svg-diagram" aria-label="CMMI 성숙도 5단계">
<svg viewBox="0 0 420 340" xmlns="http://www.w3.org/2000/svg" role="img">
<text class="label-sm" x="210" y="18" text-anchor="middle">CMMI 성숙도 — 암기: 초관정관최</text>
<rect class="box-warn" x="60" y="260" width="300" height="44" rx="8"/><text class="label" x="210" y="280" text-anchor="middle">1 Initial</text><text class="label-sm" x="210" y="296" text-anchor="middle">초기 — 개인 역량, 비정형</text>
<rect class="box" x="80" y="210" width="260" height="40" rx="8"/><text class="label-sm" x="210" y="235" text-anchor="middle">2 Managed · 관리 — 프로젝트 단위</text>
<rect class="box" x="100" y="162" width="220" height="40" rx="8"/><text class="label-sm" x="210" y="187" text-anchor="middle">3 Defined · 정의 — 조직 표준</text>
<rect class="box-alt" x="120" y="114" width="180" height="40" rx="8"/><text class="label-sm" x="210" y="139" text-anchor="middle">4 Quant · 정량관리</text>
<rect class="box-test" x="140" y="66" width="140" height="40" rx="8"/><text class="label-sm" x="210" y="91" text-anchor="middle">5 Optimizing · 최적화</text>
<line class="arrow-blue" x1="210" y1="106" x2="210" y2="114"/>
<line class="arrow-blue" x1="210" y1="154" x2="210" y2="162"/>
<line class="arrow-blue" x1="210" y1="202" x2="210" y2="210"/>
<line class="arrow-blue" x1="210" y1="250" x2="210" y2="260"/>
<text class="label-sm" x="210" y="330" text-anchor="middle">SPICE: 프로세스×능력 2차원 · CMMI: 조직 성숙도</text>
</svg>
<figcaption>CMMI 성숙도 5단계 (계단식 상승)</figcaption>
</figure>''',

    "oop": f'''<figure class="svg-diagram" aria-label="객체지향 핵심 원리">
<svg viewBox="0 0 520 380" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="260" y="20" text-anchor="middle">객체지향 5원리 — 암기: 캡추다정상</text>
<rect class="box-dark" x="190" y="40" width="140" height="52" rx="8"/><text class="label-light" x="260" y="64" text-anchor="middle">부모 Class</text><text class="label-sm" x="260" y="80" text-anchor="middle" fill="#cbd5e1">공통 속성·행위</text>
<line class="arrow-blue" x1="230" y1="92" x2="130" y2="118"/>
<line class="arrow-blue" x1="290" y1="92" x2="390" y2="118"/>
<rect class="box" x="60" y="118" width="140" height="52" rx="8"/><text class="label" x="130" y="142" text-anchor="middle">자식 A</text><text class="label-sm" x="130" y="158" text-anchor="middle">extends</text>
<rect class="box-alt" x="320" y="118" width="140" height="52" rx="8"/><text class="label" x="390" y="142" text-anchor="middle">자식 B</text><text class="label-sm" x="390" y="158" text-anchor="middle">override</text>
<text class="label-sm" x="260" y="108" text-anchor="middle">상속 · 다형성(동일 메시지→다른 동작)</text>
<rect class="box-warn" x="155" y="195" width="210" height="110" rx="12" stroke-width="2"/>
<text class="label" x="260" y="218" text-anchor="middle">객체 Object</text>
<rect fill="#fff" stroke="#ea580c" x="170" y="228" width="180" height="28" rx="4"/><text class="label-sm" x="260" y="247" text-anchor="middle">private 데이터 (정보은닉)</text>
<rect fill="#fff" stroke="#ea580c" x="170" y="262" width="180" height="28" rx="4"/><text class="label-sm" x="260" y="281" text-anchor="middle">public 메서드 (외부 인터페이스)</text>
<text class="label-sm" x="260" y="192" text-anchor="middle">캡슐화 = 데이터 + 메서드 한 객체로 묶음</text>
<rect class="box-test" x="30" y="330" width="110" height="36" rx="8"/><text class="label-sm" x="85" y="353" text-anchor="middle">추상화</text>
<rect class="box" x="155" y="330" width="110" height="36" rx="8"/><text class="label-sm" x="210" y="353" text-anchor="middle">캡슐화</text>
<rect class="box-alt" x="280" y="330" width="110" height="36" rx="8"/><text class="label-sm" x="335" y="353" text-anchor="middle">다형성</text>
<rect class="box-warn" x="405" y="330" width="85" height="36" rx="8"/><text class="label-sm" x="447" y="345" text-anchor="middle">정보</text><text class="label-sm" x="447" y="358" text-anchor="middle">은닉</text>
<line class="dash" x1="85" y1="330" x2="220" y2="305"/>
<line class="dash" x1="210" y1="330" x2="240" y2="305"/>
<line class="dash" x1="335" y1="330" x2="280" y2="305"/>
<line class="dash" x1="447" y1="330" x2="310" y2="268"/>
<text class="label-sm" x="260" y="375" text-anchor="middle">추상화: 공통만 추출 · 정보은닉: private / public / protected</text>
</svg>
<figcaption>객체지향 구조 — 상속·다형성 + 객체(캡슐화·정보은닉) + 5원리</figcaption>
</figure>''',

    "design_thinking": f'''<figure class="svg-diagram" aria-label="Design Thinking Double Diamond">
<svg viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="280" y="18" text-anchor="middle">Double Diamond + Design Thinking</text>
<polygon points="40,80 120,40 200,80 120,120" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
<text class="label-sm" x="120" y="78" text-anchor="middle">Discover</text><text class="label-sm" x="120" y="92" text-anchor="middle">발견·확산</text>
<polygon points="210,80 270,60 330,80 270,100" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<text class="label-sm" x="270" y="78" text-anchor="middle">Define</text><text class="label-sm" x="270" y="92" text-anchor="middle">정의·수렴</text>
<polygon points="340,80 420,40 500,80 420,120" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
<text class="label-sm" x="420" y="78" text-anchor="middle">Develop</text><text class="label-sm" x="420" y="92" text-anchor="middle">개발·확산</text>
<polygon points="510,80 530,70 550,80 530,90" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
<text class="label-sm" x="530" y="84" text-anchor="middle">Deliver</text>
<line class="arrow-blue" x1="200" y1="80" x2="210" y2="80"/><line class="arrow-blue" x1="330" y1="80" x2="340" y2="80"/><line class="arrow-blue" x1="500" y1="80" x2="510" y2="80"/>
<rect class="box-warn" x="20" y="155" width="88" height="40" rx="8"/><text class="label-sm" x="64" y="180" text-anchor="middle">공감</text>
<line class="arrow-blue" x1="108" y1="175" x2="118" y2="175"/>
<rect class="box" x="118" y="155" width="88" height="40" rx="8"/><text class="label-sm" x="162" y="180" text-anchor="middle">정의</text>
<line class="arrow-blue" x1="206" y1="175" x2="216" y2="175"/>
<rect class="box-alt" x="216" y="155" width="88" height="40" rx="8"/><text class="label-sm" x="260" y="180" text-anchor="middle">아이디어</text>
<line class="arrow-blue" x1="304" y1="175" x2="314" y2="175"/>
<rect class="box-test" x="314" y="155" width="100" height="40" rx="8"/><text class="label-sm" x="364" y="180" text-anchor="middle">프로토타입</text>
<line class="arrow-blue" x1="414" y1="175" x2="424" y2="175"/>
<rect class="box-dark" x="424" y="155" width="88" height="40" rx="8"/><text class="label-light" x="468" y="180" text-anchor="middle">테스트</text>
<path class="dash" d="M512 175 Q540 220 64 220 Q20 220 20 195"/>
<text class="label-sm" x="280" y="250" text-anchor="middle">암기: 발-정-개-전 / 공-정-상-시-검 — Oral-B·BoA·현대카드 사례</text>
</svg>
<figcaption>Double Diamond(4단계) + Design Thinking(5단계) 흐름</figcaption>
</figure>''',
}

INJECTIONS = [
    (ROOT / "pages" / "01-sw공학.html", [
        ('<p><strong>암기/키워드</strong></p>\n<pre class="diagram"><code>암기: 타요설개테운폐',
         '<p><strong>암기/키워드</strong></p>\n' + DIAGRAMS["sdlc"] + '\n<pre class="diagram"><code>암기: 타요설개테운폐'),
        ('<h4 id="폭포수-모델">폭포수 모델</h4>\n<p>요구사항',
         '<h4 id="폭포수-모델">폭포수 모델</h4>\n' + DIAGRAMS["waterfall"] + '\n<p>요구사항'),
        ('<h4 id="프로토타입-모델">프로토타입 모델</h4>\n<p>시제품',
         '<h4 id="프로토타입-모델">프로토타입 모델</h4>\n' + DIAGRAMS["prototype"] + '\n<p>시제품'),
        ('<h4 id="나선형-모델">나선형 모델</h4>\n<p>반복',
         '<h4 id="나선형-모델">나선형 모델</h4>\n' + DIAGRAMS["spiral"] + '\n<p>반복'),
        ('<h4 id="V-모델">V 모델</h4>\n<p>개발',
         '<h4 id="V-모델">V 모델</h4>\n' + DIAGRAMS["vmodel"] + '\n<p>개발'),
        ('<h3 id="4-3-Scrum">4.3 Scrum</h3>\n<p><strong>흐름/도식</strong></p>',
         '<h3 id="4-3-Scrum">4.3 Scrum</h3>\n' + DIAGRAMS["scrum"] + '\n<p><strong>흐름/도식</strong></p>'),
        ('<p><strong>도식: DevOps·DevSecOps 파이프라인</strong></p>\n<pre class="diagram"><code>[Plan]',
         '<p><strong>도식: DevOps·DevSecOps 파이프라인</strong></p>\n' + DIAGRAMS["devops"] + '\n<pre class="diagram"><code>[Plan]'),
        ('<h3 id="11-3-CMM-CMMI">11.3 CMM, CMMI</h3>\n<p><strong>암기/키워드</strong></p>',
         '<h3 id="11-3-CMM-CMMI">11.3 CMM, CMMI</h3>\n' + DIAGRAMS["cmmi"] + '\n<p><strong>암기/키워드</strong></p>'),
        ('<h3 id="3-3-객체지향-핵심-원리">3.3 객체지향 핵심 원리</h3>\n<p><strong>암기/키워드</strong></p>',
         '<h3 id="3-3-객체지향-핵심-원리">3.3 객체지향 핵심 원리</h3>\n' + DIAGRAMS["oop"] + '\n<p><strong>암기/키워드</strong></p>'),
    ]),
    (ROOT / "pages" / "02-sw테스트.html", [
        ('<section id="s3" class="topic">\n  <div class="section-head">\n    <h2>3. 테스트 프로세스',
         None),  # skip marker-only
        ('  <h3>도식</h3>\n  <pre class="diagram">[Test Basis]',
         '  <h3>도식</h3>\n' + DIAGRAMS["test_process"] + '\n  <pre class="diagram">[Test Basis]'),
        ('  <h3>도식</h3>\n  <pre class="diagram">[요구사항 분석] ↔ [인수 테스트]',
         '  <h3>도식</h3>\n' + DIAGRAMS["vmodel"] + '\n  <pre class="diagram">[요구사항 분석] ↔ [인수 테스트]'),
        ('  <h3>도식</h3>\n  <pre class="diagram">[단위 테스트]',
         '  <h3>도식</h3>\n' + DIAGRAMS["test_levels"] + '\n  <pre class="diagram">[단위 테스트]'),
        ('  <h3>도식</h3>\n  <pre class="diagram">[산출물 준비]',
         '  <h3>도식</h3>\n' + DIAGRAMS["inspection"] + '\n  <pre class="diagram">[산출물 준비]'),
    ]),
    (ROOT / "pages" / "03-경영컨설팅.html", [
        ('</div><div class="diagram"><pre>          [잠재적 경쟁자]',
         '</div>\n' + DIAGRAMS["porter5"] + '\n<div class="diagram"><pre>          [잠재적 경쟁자]'),
        ('<article id="strategy-3" class="topic-card"><div class="topic-head"><div><h3>Value Chain</h3>',
         '<article id="strategy-3" class="topic-card">' + DIAGRAMS["value_chain"] + '<div class="topic-head"><div><h3>Value Chain</h3>'),
        ('<article id="investment-2" class="topic-card"><div class="topic-head"><div><h3>BCG / GE Matrix</h3>',
         '<article id="investment-2" class="topic-card">' + DIAGRAMS["bcg"] + '<div class="topic-head"><div><h3>BCG / GE Matrix</h3>'),
        ('<article id="strategy-5" class="topic-card"><div class="topic-head"><div><h3>SWOT / 3C / STP</h3>',
         '<article id="strategy-5" class="topic-card">' + DIAGRAMS["swot"] + '<div class="topic-head"><div><h3>SWOT / 3C / STP</h3>'),
        ('<article id="innovation-2" class="topic-card"><div class="topic-head"><div><h3>Double Diamond / Design Thinking</h3>',
         '<article id="innovation-2" class="topic-card">' + DIAGRAMS["design_thinking"] + '<div class="topic-head"><div><h3>Double Diamond / Design Thinking</h3>'),
    ]),
]


def ensure_css_link(html: str) -> str:
    if "diagrams.css" in html:
        return html
    return html.replace("</head>", CSS_LINK + "\n</head>", 1)


def inject_file(path: Path, rules: list) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    text = ensure_css_link(text)
    count = 0
    for old, new in rules:
        if new is None:
            continue
        if old not in text:
            print(f"  WARN missing marker in {path.name}: {old[:60]}...")
            continue
        if new in text:
            continue
        text = text.replace(old, new, 1)
        count += 1
    if text != original:
        path.write_text(text, encoding="utf-8")
    return count


def main():
    total = 0
    for path, rules in INJECTIONS:
        if not path.exists():
            print(f"SKIP {path}")
            continue
        n = inject_file(path, rules)
        print(f"{path.name}: inserted {n} diagram(s)")
        total += n
    print(f"Done. Total new diagrams: {total}")


if __name__ == "__main__":
    main()
