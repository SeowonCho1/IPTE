# -*- coding: utf-8 -*-
"""Insert SVG diagrams into 02-sw테스트.html for exam answer visuals."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "pages" / "02-sw테스트.html"
DEFS = '''<defs>
  <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#64748b"/></marker>
  <marker id="arrowhead-blue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#2563eb"/></marker>
</defs>'''

D = {
"error_flow": f'''<figure class="svg-diagram" aria-label="Error Fault Failure">
<svg viewBox="0 0 480 130" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box-warn" x="10" y="45" width="80" height="40" rx="8"/><text class="label-sm" x="50" y="70" text-anchor="middle">Error</text><text class="label-sm" x="50" y="82" text-anchor="middle">실수</text>
<line class="arrow-blue" x1="90" y1="65" x2="100" y2="65"/>
<rect class="box" x="100" y="45" width="90" height="40" rx="8"/><text class="label-sm" x="145" y="65" text-anchor="middle">Fault/Defect</text><text class="label-sm" x="145" y="78" text-anchor="middle">결함</text>
<line class="arrow-blue" x1="190" y1="65" x2="200" y2="65"/>
<rect class="box-alt" x="200" y="45" width="80" height="40" rx="8"/><text class="label-sm" x="240" y="70" text-anchor="middle">Failure</text><text class="label-sm" x="240" y="82" text-anchor="middle">장애</text>
<line class="arrow-blue" x1="280" y1="65" x2="290" y2="65"/>
<rect class="box-test" x="290" y="45" width="80" height="40" rx="8"/><text class="label-sm" x="330" y="70" text-anchor="middle">Test</text><text class="label-sm" x="330" y="82" text-anchor="middle">결함발견</text>
<line class="arrow-blue" x1="370" y1="65" x2="380" y2="65"/>
<rect class="box-dark" x="380" y="45" width="90" height="40" rx="8"/><text class="label-light" x="425" y="70" text-anchor="middle">Debug</text><text class="label-sm" x="425" y="82" text-anchor="middle" fill="#cbd5e1">수정</text>
<text class="label-sm" x="240" y="22" text-anchor="middle">실수 → 결함 → 실행장애 → 테스트(발견) → 디버깅(수정)</text>
<text class="label-sm" x="240" y="118" text-anchor="middle">테스트 목적: 무결함 증명 X · 결함 존재 증명 O</text>
</svg>
<figcaption>Error → Fault → Failure → Test → Debug</figcaption>
</figure>''',

"seven_principles": f'''<figure class="svg-diagram" aria-label="테스트 7원리">
<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" role="img">
<text class="label-sm" x="280" y="16" text-anchor="middle">테스트 7원리 — 암기: 결·완·초·집·살·정·오</text>
<rect class="box" x="8" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="44" y="52" text-anchor="middle">결함존재</text>
<rect class="box" x="86" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="122" y="52" text-anchor="middle">완벽불가</text>
<rect class="box-warn" x="164" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="200" y="52" text-anchor="middle">초기시작</text>
<rect class="box-alt" x="242" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="278" y="52" text-anchor="middle">결함집중</text>
<rect class="box-test" x="320" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="356" y="52" text-anchor="middle">살충제</text>
<rect class="box" x="398" y="30" width="72" height="36" rx="6"/><text class="label-sm" x="434" y="52" text-anchor="middle">정황의존</text>
<rect class="box-dark" x="476" y="30" width="76" height="36" rx="6"/><text class="label-light" x="514" y="52" text-anchor="middle">오류부재</text>
<text class="label-sm" x="44" y="82" text-anchor="middle">증명O</text>
<text class="label-sm" x="200" y="82" text-anchor="middle">비용↓</text>
<text class="label-sm" x="278" y="82" text-anchor="middle">Pareto</text>
<text class="label-sm" x="356" y="82" text-anchor="middle">케이스갱신</text>
<text class="label-sm" x="514" y="82" text-anchor="middle">궤변주의</text>
<text class="label-sm" x="280" y="130" text-anchor="middle">답안: 각 원리 정의 + 한 줄 적용 (조기테스트·위험모듈 집중 등)</text>
</svg>
<figcaption>SW 테스트 7원리 한눈에</figcaption>
</figure>''',

"test_lifecycle": f'''<figure class="svg-diagram" aria-label="테스트 생명주기">
<svg viewBox="0 0 560 160" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box-warn" x="10" y="55" width="90" height="44" rx="8"/><text class="label-sm" x="55" y="75" text-anchor="middle">테스트</text><text class="label-sm" x="55" y="89" text-anchor="middle">정책</text>
<line class="arrow-blue" x1="100" y1="77" x2="115" y2="77"/>
<rect class="box" x="115" y="55" width="90" height="44" rx="8"/><text class="label-sm" x="160" y="82" text-anchor="middle">MTP</text>
<line class="arrow-blue" x1="205" y1="77" x2="220" y2="77"/>
<rect class="box-alt" x="220" y="55" width="90" height="44" rx="8"/><text class="label-sm" x="265" y="82" text-anchor="middle">TMO</text>
<line class="arrow-blue" x1="310" y1="77" x2="325" y2="77"/>
<rect class="box-test" x="325" y="40" width="220" height="74" rx="10"/><text class="label-sm" x="435" y="62" text-anchor="middle">테스트 생명주기</text>
<text class="label-sm" x="435" y="78" text-anchor="middle">계획/제어 → 분석/설계</text>
<text class="label-sm" x="435" y="92" text-anchor="middle">구현/실행 → 평가/리포팅</text>
<text class="label-sm" x="435" y="106" text-anchor="middle">→ 마감</text>
<text class="label-sm" x="280" y="145" text-anchor="middle">MTP: 목표·범위·전략·리스크 · TMO: Non / Internal / External</text>
</svg>
<figcaption>테스트 정책 → MTP → TMO → 생명주기 5단계</figcaption>
</figure>''',

"classification": f'''<figure class="svg-diagram" aria-label="테스트 분류">
<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" role="img">
<text class="label-sm" x="260" y="18" text-anchor="middle">테스트 분류 5축 — 답안에 분류 기준별 비교표 병행</text>
<rect class="box-dark" x="210" y="35" width="100" height="36" rx="8"/><text class="label-light" x="260" y="58" text-anchor="middle">테스트</text>
<line class="dash" x1="260" y1="71" x2="80" y2="100"/><line class="dash" x1="260" y1="71" x2="180" y2="100"/>
<line class="dash" x1="260" y1="71" x2="260" y2="100"/><line class="dash" x1="260" y1="71" x2="340" y2="100"/>
<line class="dash" x1="260" y1="71" x2="440" y2="100"/>
<rect class="box" x="20" y="100" width="120" height="50" rx="8"/><text class="label-sm" x="80" y="122" text-anchor="middle">실행 여부</text><text class="label-sm" x="80" y="138" text-anchor="middle">정적 / 동적</text>
<rect class="box-warn" x="150" y="100" width="120" height="50" rx="8"/><text class="label-sm" x="210" y="122" text-anchor="middle">접근법</text><text class="label-sm" x="210" y="138" text-anchor="middle">블랙 / 화이트</text>
<rect class="box-alt" x="280" y="100" width="120" height="50" rx="8"/><text class="label-sm" x="340" y="122" text-anchor="middle">설계 근원</text><text class="label-sm" x="340" y="138" text-anchor="middle">명세·구조·경험</text>
<rect class="box-test" x="410" y="100" width="100" height="50" rx="8"/><text class="label-sm" x="460" y="122" text-anchor="middle">레벨</text><text class="label-sm" x="460" y="138" text-anchor="middle">단·통·시·인</text>
<rect class="box" x="170" y="175" width="180" height="50" rx="8"/><text class="label-sm" x="260" y="197" text-anchor="middle">목적</text><text class="label-sm" x="260" y="213" text-anchor="middle">기능 / 비기능 / 확인 / 회귀</text>
<line class="dash" x1="260" y1="225" x2="260" y2="250"/>
<rect fill="#f1f5f9" stroke="#94a3b8" x="60" y="250" width="400" height="36" rx="6"/><text class="label-sm" x="260" y="272" text-anchor="middle">혼동 주의: 블랙박스≠명세기반만 · 화이트박스≠구조기반만</text>
</svg>
<figcaption>테스트 분류 체계 5가지 관점</figcaption>
</figure>''',

"blackbox": f'''<figure class="svg-diagram" aria-label="명세기반 블랙박스">
<svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box" x="180" y="10" width="140" height="36" rx="8"/><text class="label-sm" x="250" y="33" text-anchor="middle">요구사항·명세서</text>
<line class="arrow-blue" x1="250" y1="46" x2="250" y2="58"/>
<rect class="box-warn" x="160" y="58" width="180" height="32" rx="8"/><text class="label-sm" x="250" y="78" text-anchor="middle">입력·조건·상태·시나리오 분석</text>
<line class="arrow-blue" x1="250" y1="90" x2="250" y2="102"/>
<text class="label-sm" x="250" y="118" text-anchor="middle">블랙박스 설계기법 — 암기: 동·경·결·상·유·페·직·원·분</text>
<rect class="box-alt" x="15" y="130" width="88" height="36" rx="6"/><text class="label-sm" x="59" y="152" text-anchor="middle">동등분할</text>
<rect class="box-alt" x="108" y="130" width="88" height="36" rx="6"/><text class="label-sm" x="152" y="152" text-anchor="middle">경계값</text>
<rect class="box-alt" x="201" y="130" width="88" height="36" rx="6"/><text class="label-sm" x="245" y="152" text-anchor="middle">결정테이블</text>
<rect class="box-alt" x="294" y="130" width="88" height="36" rx="6"/><text class="label-sm" x="338" y="152" text-anchor="middle">상태전이</text>
<rect class="box-alt" x="387" y="130" width="98" height="36" rx="6"/><text class="label-sm" x="436" y="152" text-anchor="middle">유스케이스</text>
<rect class="box" x="80" y="178" width="100" height="32" rx="6"/><text class="label-sm" x="130" y="198" text-anchor="middle">페어와이즈</text>
<rect class="box" x="200" y="178" width="100" height="32" rx="6"/><text class="label-sm" x="250" y="198" text-anchor="middle">직교배열</text>
<rect class="box" x="320" y="178" width="100" height="32" rx="6"/><text class="label-sm" x="370" y="198" text-anchor="middle">원인-결과</text>
</svg>
<figcaption>명세기반(블랙박스) 테스트 설계기법</figcaption>
</figure>''',

"coverage": f'''<figure class="svg-diagram" aria-label="커버리지 피라미드">
<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" role="img">
<polygon points="200,20 360,250 40,250" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<polygon points="200,55 320,250 80,250" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
<polygon points="200,95 280,250 120,250" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<polygon points="200,140 240,250 160,250" fill="#1d4ed8" stroke="#1e40af" stroke-width="1.5"/>
<text class="label-sm" x="200" y="42" text-anchor="middle">MCC / MC/DC</text>
<text class="label-sm" x="200" y="82" text-anchor="middle">C/DC · CC</text>
<text class="label-sm" x="200" y="125" text-anchor="middle">DC (분기)</text>
<text class="label-light" x="200" y="175" text-anchor="middle">SC</text>
<text class="label-sm" x="200" y="265" text-anchor="middle">강도 ↑ · 비용 ↑ · 화이트박스 · McCabe V(G)=E-N+2</text>
</svg>
<figcaption>구조기반 커버리지 강도 — 문장(SC) → 분기(DC) → MC/DC</figcaption>
</figure>''',

"integration": f'''<figure class="svg-diagram" aria-label="통합 테스트 방식">
<svg viewBox="0 0 520 180" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="260" y="18" text-anchor="middle">통합 테스트 방식 — 암기: 백·빅·상·하·샌</text>
<rect class="box" x="15" y="40" width="85" height="50" rx="8"/><text class="label-sm" x="57" y="62" text-anchor="middle">빅뱅</text><text class="label-sm" x="57" y="78" text-anchor="middle">일괄</text>
<rect class="box-warn" x="110" y="40" width="85" height="50" rx="8"/><text class="label-sm" x="152" y="62" text-anchor="middle">상향식</text><text class="label-sm" x="152" y="78" text-anchor="middle">+Driver</text>
<rect class="box-alt" x="205" y="40" width="85" height="50" rx="8"/><text class="label-sm" x="247" y="62" text-anchor="middle">하향식</text><text class="label-sm" x="247" y="78" text-anchor="middle">+Stub</text>
<rect class="box-test" x="300" y="40" width="85" height="50" rx="8"/><text class="label-sm" x="342" y="62" text-anchor="middle">샌드위치</text><text class="label-sm" x="342" y="78" text-anchor="middle">상+하</text>
<rect class="box-dark" x="395" y="40" width="85" height="50" rx="8"/><text class="label-light" x="437" y="68" text-anchor="middle">백본</text>
<rect class="box" x="80" y="110" width="70" height="36" rx="6"/><text class="label-sm" x="115" y="132" text-anchor="middle">모듈A</text>
<rect class="box" x="160" y="110" width="70" height="36" rx="6"/><text class="label-sm" x="195" y="132" text-anchor="middle">모듈B</text>
<rect class="box" x="240" y="110" width="70" height="36" rx="6"/><text class="label-sm" x="275" y="132" text-anchor="middle">모듈C</text>
<line class="arrow-blue" x1="150" y1="128" x2="160" y2="128"/><line class="arrow-blue" x1="230" y1="128" x2="240" y2="128"/>
<text class="label-sm" x="380" y="132" text-anchor="middle">인터페이스·데이터흐름 검증</text>
<text class="label-sm" x="260" y="168" text-anchor="middle">상향: 하위→상위 · 하향: 상위→하위 · Driver/Stub 역할 구분</text>
</svg>
<figcaption>통합 테스트 5방식 + Driver/Stub</figcaption>
</figure>''',

"performance": f'''<figure class="svg-diagram" aria-label="성능 테스트">
<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img">
<text class="label-sm" x="260" y="18" text-anchor="middle">비기능·성능 테스트 — TPS = 동시사용자 / (응답+Think)</text>
<rect class="box-alt" x="20" y="40" width="110" height="50" rx="8"/><text class="label-sm" x="75" y="60" text-anchor="middle">부하 Load</text><text class="label-sm" x="75" y="78" text-anchor="middle">정상 부하</text>
<rect class="box-warn" x="145" y="40" width="110" height="50" rx="8"/><text class="label-sm" x="200" y="60" text-anchor="middle">스트레스</text><text class="label-sm" x="200" y="78" text-anchor="middle">한계 초과</text>
<rect class="box" x="270" y="40" width="110" height="50" rx="8"/><text class="label-sm" x="325" y="60" text-anchor="middle">내구성</text><text class="label-sm" x="325" y="78" text-anchor="middle">장시간</text>
<rect class="box-test" x="395" y="40" width="110" height="50" rx="8"/><text class="label-sm" x="450" y="60" text-anchor="middle">볼륨</text><text class="label-sm" x="450" y="78" text-anchor="middle">대량 데이터</text>
<rect class="box-dark" x="20" y="110" width="150" height="44" rx="8"/><text class="label-light" x="95" y="130" text-anchor="middle">몽키 Monkey</text><text class="label-sm" x="95" y="146" text-anchor="middle" fill="#cbd5e1">무작위·예외탐색</text>
<rect class="box" x="185" y="110" width="150" height="44" rx="8"/><text class="label-sm" x="260" y="130" text-anchor="middle">회귀 Regression</text><text class="label-sm" x="260" y="146" text-anchor="middle">변경 영향 확인</text>
<rect class="box-alt" x="350" y="110" width="155" height="44" rx="8"/><text class="label-sm" x="427" y="130" text-anchor="middle">사용성 Usability</text><text class="label-sm" x="427" y="146" text-anchor="middle">효과·효율·만족</text>
<text class="label-sm" x="260" y="188" text-anchor="middle">성능: Response Time · Throughput · TPS · Concurrent User</text>
</svg>
<figcaption>성능·비기능 테스트 유형</figcaption>
</figure>''',

"strategic": f'''<figure class="svg-diagram" aria-label="전략적 테스트">
<svg viewBox="0 0 540 170" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="270" y="16" text-anchor="middle">전략적 테스트 4대 기법</text>
<rect class="box-warn" x="10" y="35" width="120" height="70" rx="8"/><text class="label-sm" x="70" y="55" text-anchor="middle">RBT</text><text class="label-sm" x="70" y="72" text-anchor="middle">위험식별</text><text class="label-sm" x="70" y="86" text-anchor="middle">→우선순위</text><text class="label-sm" x="70" y="98" text-anchor="middle">→집중</text>
<rect class="box" x="145" y="35" width="120" height="70" rx="8"/><text class="label-sm" x="205" y="55" text-anchor="middle">Mutation</text><text class="label-sm" x="205" y="72" text-anchor="middle">변이생성</text><text class="label-sm" x="205" y="86" text-anchor="middle">→테스트</text><text class="label-sm" x="205" y="98" text-anchor="middle">→Score</text>
<rect class="box-alt" x="280" y="35" width="120" height="70" rx="8"/><text class="label-sm" x="340" y="55" text-anchor="middle">Back-to-Back</text><text class="label-sm" x="340" y="72" text-anchor="middle">2시스템</text><text class="label-sm" x="340" y="86" text-anchor="middle">결과비교</text>
<rect class="box-test" x="415" y="35" width="115" height="70" rx="8"/><text class="label-sm" x="472" y="55" text-anchor="middle">MBT</text><text class="label-sm" x="472" y="72" text-anchor="middle">모델→</text><text class="label-sm" x="472" y="86" text-anchor="middle">케이스자동</text>
<text class="label-sm" x="270" y="155" text-anchor="middle">답안: 개념 + 절차 + 효과 + 한계 (자원 제한 시 RBT 우선)</text>
</svg>
<figcaption>RBT · Mutation · Back-to-Back · MBT</figcaption>
</figure>''',

"shift": f'''<figure class="svg-diagram" aria-label="Shift Left Right">
<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" role="img">
<line x1="40" y1="80" x2="520" y2="80" stroke="#cbd5e1" stroke-width="3"/>
<text class="label-sm" x="280" y="25" text-anchor="middle">Shift Left ←—— 개발 생명주기 ——→ Shift Right</text>
<rect class="box-warn" x="50" y="45" width="130" height="44" rx="8"/><text class="label-sm" x="115" y="65" text-anchor="middle">Shift Left</text><text class="label-sm" x="115" y="80" text-anchor="middle">리뷰·SAST·단위</text>
<rect class="box" x="215" y="45" width="130" height="44" rx="8"/><text class="label-sm" x="280" y="65" text-anchor="middle">CI/CD</text><text class="label-sm" x="280" y="80" text-anchor="middle">자동빌드·테스트</text>
<rect class="box-alt" x="380" y="45" width="130" height="44" rx="8"/><text class="label-sm" x="445" y="65" text-anchor="middle">Shift Right</text><text class="label-sm" x="445" y="80" text-anchor="middle">모니터·카나리</text>
<ellipse cx="280" cy="115" rx="100" ry="22" fill="#f0fdf4" stroke="#16a34a"/><text class="label-sm" x="280" y="120" text-anchor="middle">DevTestOps 품질 내재화</text>
<text class="label-sm" x="280" y="145" text-anchor="middle">Left=조기결함·비용↓ · Right=실사용피드백 · 자동화≠품질보장</text>
</svg>
<figcaption>Shift Left / Shift Right / DevTestOps</figcaption>
</figure>''',

"tmmi": f'''<figure class="svg-diagram" aria-label="TMMi 성숙도">
<svg viewBox="0 0 420 280" xmlns="http://www.w3.org/2000/svg" role="img">
<text class="label-sm" x="210" y="18" text-anchor="middle">TMMi 5단계 + ISO 29119 (버·프·독·기·키)</text>
<rect class="box-warn" x="60" y="210" width="300" height="36" rx="8"/><text class="label-sm" x="210" y="232" text-anchor="middle">1 Initial — 비정형</text>
<rect class="box" x="80" y="170" width="260" height="32" rx="8"/><text class="label-sm" x="210" y="190" text-anchor="middle">2 Managed — 프로젝트 관리</text>
<rect class="box-alt" x="100" y="132" width="220" height="32" rx="8"/><text class="label-sm" x="210" y="152" text-anchor="middle">3 Defined — 조직 표준</text>
<rect class="box-test" x="120" y="94" width="180" height="32" rx="8"/><text class="label-sm" x="210" y="114" text-anchor="middle">4 Measured — 측정</text>
<rect class="box-dark" x="140" y="56" width="140" height="32" rx="8"/><text class="label-light" x="210" y="76" text-anchor="middle">5 Optimization</text>
<rect fill="#f1f5f9" stroke="#94a3b8" x="30" y="252" width="360" height="24" rx="4"/><text class="label-sm" x="210" y="268" text-anchor="middle">ISO29119: 개념·프로세스·문서·기법·키워드</text>
</svg>
<figcaption>TMMi 성숙도 + ISO/IEC/IEEE 29119 구성</figcaption>
</figure>''',

"experience": f'''<figure class="svg-diagram" aria-label="경험기반 테스트">
<svg viewBox="0 0 480 120" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<rect class="box-dark" x="180" y="10" width="120" height="36" rx="8"/><text class="label-light" x="240" y="33" text-anchor="middle">테스터 경험</text>
<line class="arrow-blue" x1="240" y1="46" x2="240" y2="56"/>
<rect class="box-warn" x="160" y="56" width="160" height="28" rx="6"/><text class="label-sm" x="240" y="74" text-anchor="middle">오류 가능 영역 추정</text>
<rect class="box-alt" x="20" y="92" width="100" height="24" rx="5"/><text class="label-sm" x="70" y="108" text-anchor="middle">탐색적</text>
<rect class="box" x="130" y="92" width="100" height="24" rx="5"/><text class="label-sm" x="180" y="108" text-anchor="middle">오류추정</text>
<rect class="box-test" x="240" y="92" width="100" height="24" rx="5"/><text class="label-sm" x="290" y="108" text-anchor="middle">체크리스트</text>
<rect class="box-warn" x="350" y="92" width="110" height="24" rx="5"/><text class="label-sm" x="405" y="108" text-anchor="middle">애드혹</text>
<text class="label-sm" x="240" y="118" text-anchor="middle">탐·분·체·특·오·혹 · 차터·타임박싱·노트·회고</text>
</svg>
<figcaption>경험기반 — 탐색적 vs 애드혹(계획 없음)</figcaption>
</figure>''',

"review_formality": f'''<figure class="svg-diagram" aria-label="리뷰 공식성">
<svg viewBox="0 0 520 90" xmlns="http://www.w3.org/2000/svg" role="img">
{DEFS}
<text class="label-sm" x="260" y="16" text-anchor="middle">정적 테스트 — 리뷰 공식성 ↑ (답안 비교표용)</text>
<rect class="box" x="10" y="30" width="88" height="40" rx="6"/><text class="label-sm" x="54" y="55" text-anchor="middle">비공식</text>
<line class="arrow-blue" x1="98" y1="50" x2="108" y2="50"/>
<rect class="box" x="108" y="30" width="88" height="40" rx="6"/><text class="label-sm" x="152" y="55" text-anchor="middle">워크스루</text>
<line class="arrow-blue" x1="196" y1="50" x2="206" y2="50"/>
<rect class="box-warn" x="206" y="30" width="88" height="40" rx="6"/><text class="label-sm" x="250" y="55" text-anchor="middle">기술리뷰</text>
<line class="arrow-blue" x1="294" y1="50" x2="304" y2="50"/>
<rect class="box-alt" x="304" y="30" width="88" height="40" rx="6"/><text class="label-sm" x="348" y="55" text-anchor="middle">인스펙션</text>
<line class="arrow-blue" x1="392" y1="50" x2="402" y2="50"/>
<rect class="box-test" x="402" y="30" width="88" height="40" rx="6"/><text class="label-sm" x="446" y="55" text-anchor="middle">감사</text>
</svg>
<figcaption>리뷰 유형 — 공식성 낮음 → 높음</figcaption>
</figure>''',
}

INJECTIONS = [
    ('  <pre class="diagram">[Error: 사람의 실수]', D["error_flow"] + '\n  ' + D["seven_principles"] + '\n  <pre class="diagram">[Error: 사람의 실수]'),
    ('  <pre class="diagram">[테스트 정책]', D["test_lifecycle"] + '\n  <pre class="diagram">[테스트 정책]'),
    ('  <pre class="diagram">[프로그램 실행 여부]', D["classification"] + '\n  <pre class="diagram">[프로그램 실행 여부]'),
    ('  <pre class="diagram">[산출물 준비]', D["review_formality"] + '\n  <pre class="diagram">[산출물 준비]'),
    ('  <pre class="diagram">[요구사항/명세서]', D["blackbox"] + '\n  <pre class="diagram">[요구사항/명세서]'),
    ('  <pre class="diagram">[소스 코드 / 제어 흐름]', D["coverage"] + '\n  <pre class="diagram">[소스 코드 / 제어 흐름]'),
    ('  <pre class="diagram">[단위 테스트]\n   ↓ 모듈', D["integration"] + '\n  <pre class="diagram">[단위 테스트]\n   ↓ 모듈'),
    ('  <pre class="diagram">[비기능 요구사항]', D["performance"] + '\n  <pre class="diagram">[비기능 요구사항]'),
    ('  <pre class="diagram">[위험·변경·모델·결함 주입]', D["strategic"] + '\n  <pre class="diagram">[위험·변경·모델·결함 주입]'),
    ('  <pre class="diagram">[요구사항 단계] Shift Left', D["shift"] + '\n  <pre class="diagram">[요구사항 단계] Shift Left'),
    ('  <pre class="diagram">[테스터 경험·도메인 지식]', D["experience"] + '\n  <pre class="diagram">[테스터 경험·도메인 지식]'),
    ('  <pre class="diagram">[테스트 프로세스 개선]', D["tmmi"] + '\n  <pre class="diagram">[테스트 프로세스 개선]'),
]


def main():
    text = FILE.read_text(encoding="utf-8")
    count = 0
    for old, new in INJECTIONS:
        if new in text:
            continue
        if old not in text:
            print(f"WARN missing: {old[:50]}...")
            continue
        text = text.replace(old, new, 1)
        count += 1
    FILE.write_text(text, encoding="utf-8")
    print(f"Inserted {count} diagram block(s) into {FILE.name}")


if __name__ == "__main__":
    main()
