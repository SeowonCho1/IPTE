# -*- coding: utf-8 -*-
"""Expand 경영컨설팅 page with answer-writing structure."""
import re
from pathlib import Path

from consulting_topic_depth import render_depth

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "pages/03-경영컨설팅.html"

STUDY_EXTRA = """
<article id="study-1" class="topic-card">
<div class="topic-head"><div><h3>경영컨설팅 답안 작성법</h3><p class="pages">기술사 1·2교시 공통</p></div><span class="mnemonic">암기: 키-사-시</span></div>
<div class="chips"><span>1교시 30줄</span><span>2교시 70줄</span><span>프레임워크</span><span>사례</span><span>시사점</span></div>
<div class="diagram"><pre>1교시: [정의 2줄] → [구성요소·도식] → [사례 1개] → [시사점 2줄]
2교시: [개요] → [분석·비교표] → [사례·적용] → [한계·발전방향]</pre></div>
<div class="table-wrap"><table><thead><tr><th>단계</th><th>작성 요령</th><th>경영컨설팅 예시</th></tr></thead><tbody>
<tr><td>키워드</td><td>두음·프레임워크 항목만 나열</td><td>정-경-사-기+환-법 / 원-차-집 / 재-고-내-학</td></tr>
<tr><td>한 줄 확장</td><td>항목마다 「무엇을·왜·어떻게」</td><td>PESTEL은 통제 불가 외부요인을 분석해 기회·위협 도출</td></tr>
<tr><td>사례 붙이기</td><td>기업명 + 문제 + 적용 + 결과</td><td>하이트맥주 ERRC로 브랜드 재창조 → 젊은층 확보</td></tr>
<tr><td>시사점</td><td>효과·한계·전략방향</td><td>차별화 전략 수립, 실행 시 조직·문화 정합성 필요</td></tr>
<tr><td>3단표</td><td>구분 / 키워드 / 답안·사례</td><td>본문 각 topic-card 표 그대로 활용</td></tr>
</tbody></table></div>
<div class="answer-outline"><strong>2교시 답안 목차 템플릿 (복사해서 쓰기)</strong>
<ol>
<li><b>1. 개요</b> — 가. 정의(2~3줄) · 나. 필요성(환경·문제) · 다. 분석/적용 틀(도식 1개)</li>
<li><b>2. 핵심 내용</b> — 가. 구성요소·절차 · 나. 비교·특징(표 1개) · 다. IT·경영 연계(해당 시)</li>
<li><b>3. 사례·적용</b> — 가. 국내외 사례 · 나. 적용 고려사항 · 다. 기대효과</li>
<li><b>4. 결론</b> — 한계 2~3개 · 대응·발전방향 · 전략적 시사점 2줄</li>
</ol></div>
<div class="answer-box"><strong>답안 확장 문장</strong><p>경영·컨설팅 과목은 프레임워크 정의만 쓰면 감점되므로, 반드시 「키워드 풀어쓰기 → 표/도식 → 기업 사례 → 시사점」 순으로 2교시 4단 구조를 채워야 한다.</p></div>
</article>
"""

TEMPLATE_SECTION = """
<section id="answer-template" class="section"><h2>9. 기술사 답안 템플릿</h2>
<article class="template-card"><h3>9.1 경영컨설팅 1교시형 (약 30줄)</h3>
<div class="diagram"><pre>① 개념 정의 (2~3줄)
② 핵심 구성·도식 (키워드 5~7개 풀어쓰기)
③ 대표 사례 1개 (기업·적용·효과)
④ 시사점·결론 (2~3줄)</pre></div>
<div class="table-wrap"><table><thead><tr><th>문단</th><th>분량</th><th>체크</th></tr></thead><tbody>
<tr><td>정의</td><td>3~5줄</td><td>개념명 + 목적 + 효과</td></tr>
<tr><td>본론</td><td>15~18줄</td><td>표 1개 또는 도식 1개 필수</td></tr>
<tr><td>사례</td><td>5~7줄</td><td>기업명·상황·적용·결과</td></tr>
<tr><td>결론</td><td>3~5줄</td><td>시사점 + 한계 1개</td></tr>
</tbody></table></div></article>
<article class="template-card"><h3>9.2 경영컨설팅 2교시형 (약 70줄)</h3>
<div class="diagram"><pre>1. 개요 — 정의 · 배경 · 전체 흐름도
2. 핵심 — 구성요소 · 비교표 · 프레임워크 연계
3. 적용 — 사례 2개 · 고려사항 · 기대효과
4. 결론 — 한계 · 대응 · 발전방향</pre></div>
<div class="table-wrap"><table><thead><tr><th>공식</th><th>예시</th></tr></thead><tbody>
<tr><td>개념 = A를 위해 B를 적용하여 C를 달성하는 방법</td><td>BSC는 전략을 KPI로 연결해 균형 성과관리를 달성하는 프레임워크</td></tr>
<tr><td>환경 변화 → 기존 한계 → 새 접근 필요</td><td>경쟁 심화 → 단순 재무지표 한계 → BSC 4관점 도입</td></tr>
<tr><td>분석 → 사례 → 시사점</td><td>BCG 분석 → LG전자 포트폴리오 → Question Mark 투자·Dog 철수 검토</td></tr>
</tbody></table></div></article>
<article class="template-card"><h3>9.3 유형별 사례 연결표</h3>
<div class="table-wrap"><table><thead><tr><th>유형</th><th>추천 사례</th><th>답안에 넣을 한 줄</th></tr></thead><tbody>
<tr><td>전략·환경</td><td>산후조리원 STEEP, 하이트 ERRC, LG BCG</td><td>외부환경 분석 후 포트폴리오·차별화 전략 수립</td></tr>
<tr><td>혁신·방법론</td><td>Oral-B·BoA DT, TRIZ 자동차·체인, 오바마 A/B</td><td>사용자 관찰·데이터 검증 기반 혁신</td></tr>
<tr><td>정보화·거버넌스</td><td>공공 ISMP, COBIT 통제, ERP-EAI 연계</td><td>전사 로드맵·통제·성과 연계</td></tr>
<tr><td>디지털·ESG</td><td>코닥 DX 실패, SK RE100, 맥카페 SCM</td><td>기술만이 아닌 모델·조직·지속가능성</td></tr>
</tbody></table></div></article>
</section>
<!-- exam-sample-env: see pages/03-경영컨설팅.html#exam-sample-env -->
"""

# topic-specific extras (outline body points, effects, limits, intro, conclusion)
TOPIC_EXTRAS = {
    "strategy-1": {
        "exam": "1·2교시 빈출",
        "effects": "외부 기회·위협 식별, 중장기 전략 방향 설정, SWOT·CSF 도출 기반 마련",
        "limits": "거시환경만으로는 산업·경쟁 구조 설명 부족 → 5 Force·3C 병행",
        "intro": "기업 경영환경은 정치·경제·사회·기술·환경·법률 요인에 의해 지속 변화하므로, PESTEL 등 거시환경 분석을 통해 통제 불가 외부요인을 체계적으로 파악할 필요가 있다.",
        "conclusion": "PESTEL 분석 결과를 SWOT의 O/T와 연결하고, STEEP·산후조리원 ICT 사례처럼 구체적 요인을 제시하면 답안 설득력이 높아진다.",
    },
    "investment-2": {
        "exam": "2교시 빈출",
        "effects": "사업 포트폴리오 균형, 투자·유지·철수 의사결정, 자원 배분 최적화",
        "limits": "시장성장률·점유율 2지표 단순화 → GE Matrix 등 보완",
        "intro": "다사업 기업은 사업부별 성장성과 경쟁력이 상이하므로, BCG Matrix로 포트폴리오를 평가하고 Build·Hold·Harvest·Divest 전략을 수립해야 한다.",
        "conclusion": "LG전자 HA·AC(Cash Cow), MC·HE(Question Mark) 사례를 들며 투자 우선순위와 철수 검토 기준을 제시하면 실무형 답안이 된다.",
    },
    "investment-3": {
        "exam": "1·2교시",
        "effects": "경쟁 회피, 신규 고객층 창출, 가치혁신",
        "limits": "실행 시 브랜드·조직 저항, 기존 고객 이탈 리스크",
        "intro": "레드오션 경쟁이 심화될 때 ERRC 그리드로 경쟁요소를 재구성하면 블루오션 전략을 수립할 수 있다.",
        "conclusion": "하이트맥주 사례(제거·감소·증대·창조)를 ERRC 4칸 표와 함께 쓰면 답안 완성도가 높아진다.",
    },
    "system-0": {
        "exam": "2교시 빈출",
        "effects": "전략-성과 연계, 비재무 균형, KPI 기반 의사결정",
        "limits": "지표 과다·형식화, 전략맵-실행 단절 주의",
        "intro": "재무지표 중심 경영의 한계를 보완하기 위해 BSC 4관점(재무·고객·내부프로세스·학습성장)으로 전략을 성과지표화한다.",
        "conclusion": "SEM·ERP·DW와 연계해 KPI를 모니터링하는 구조를 그리면 IT 경영과 연결된 답안이 된다.",
    },
    "process-1": {
        "exam": "2교시 빈출",
        "effects": "전사 IT 정렬, 중복투자 감소, RFP·발주 품질 향상, 표준화",
        "limits": "EA 수립·유지 비용, 조직 저항, ISP-EA-프로젝트 단절 주의",
        "intro": "정보화가 부처·시스템별로 단절되면 중복투자와 과업변경이 발생하므로, ISP로 전사 로드맵을, ISMP로 사업 요구를, EA/EAP로 표준 아키텍처를 수립해야 한다.",
        "conclusion": "EA 4계층(BA·DA·AA·TA)과 ISP 4단계, ISMP RFP·FP 산정을 표로 비교하고 공공 SW 발주 사례를 붙이면 실무형 답안이 된다.",
    },
    "process-2": {
        "exam": "2교시",
        "effects": "IT-경영 전략 정렬, 가치·위험·자원·성과 통합 관리",
        "limits": "형식적 거버넌스, 이사회·CIO 역할 불명확 시 실효 저하",
        "intro": "IT 투자 확대와 디지털 전환 환경에서 IT Governance 5도메인과 ISO 38500 Evaluate-Direct-Monitor로 통제체계를 수립해야 한다.",
        "conclusion": "ISP·EA·성과측정과 연계한 거버넌스 체계를 제시하고, 책임·전략·성과 6원칙을 언급하면 가점 요소가 된다.",
    },
    "digital-1": {
        "exam": "2교시 빈출",
        "effects": "고객경험·운영효율·신규 수익모델 창출",
        "limits": "기술 도입만으로는 실패(코닥) → 조직·BM·문화 동반 변화",
        "intro": "디지털 트랜스포메이션은 단순 IT 도입이 아니라 전략·조직·프로세스·비즈니스 모델·문화를 근본 변화시키는 경영전략이다.",
        "conclusion": "코닥 실패와 FK·싱글 ERP 성공 사례를 대비하면 「기술+모델 전환」 메시지가 명확해진다.",
    },
}


def extract_text(html: str, pattern: str) -> str:
    m = re.search(pattern, html, re.DOTALL)
    if not m:
        return ""
    text = re.sub(r"<[^>]+>", " ", m.group(1))
    return re.sub(r"\s+", " ", text).strip()


def strip_generated_blocks(html: str) -> str:
    html = re.sub(
        r'<details class="topic-depth-wrap"[^>]*>.*?</details>',
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<details class="answer-extra-wrap">.*?</details>\s*',
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(r'<div class="answer-extra">.*?</div>\s*', "", html, flags=re.DOTALL)
    return html


def build_depth(article_html: str, art_id: str) -> str:
    article_html = re.sub(
        r'<details class="topic-depth-wrap"[^>]*>.*?</details>\s*',
        "",
        article_html,
        flags=re.DOTALL,
    )
    h3 = extract_text(article_html, r"<h3>([^<]+)</h3>")
    depth = render_depth(art_id, h3)
    if not depth:
        return article_html
    for anchor in (
        '<div class="case-box">',
        '<div class="answer-outline">',
        '<div class="answer-box">',
    ):
        if anchor in article_html:
            return article_html.replace(anchor, depth + anchor, 1)
    return article_html + depth


def build_extras(article_html: str, art_id: str) -> str:
    if 'class="answer-extra-wrap"' in article_html or 'class="answer-extra"' in article_html:
        article_html = strip_generated_blocks(article_html)

    h3 = extract_text(article_html, r"<h3>([^<]+)</h3>")
    mnemonic = extract_text(article_html, r'<span class="mnemonic">([^<]+)</span>')
    case_text = extract_text(article_html, r'<div class="case-box">.*?<p>([^<]+)</p>')
    answer_text = extract_text(article_html, r'<div class="answer-box">.*?<p>([^<]+)</p>')

    extra = TOPIC_EXTRAS.get(art_id, {})
    exam = extra.get("exam", "기출 가능")
    effects = extra.get("effects", "의사결정 품질 향상, 전략 실행력 강화, 이해관계자 설득력 제고")
    limits = extra.get("limits", "프레임워크 남용·사례 없는 나열·시사점 누락 시 답안 건조")
    intro = extra.get(
        "intro",
        f"{h3}은(는) 경영·컨설팅 분석에서 핵심 프레임워크로, {answer_text[:80]}…" if answer_text else f"{h3} 개념의 정의와 적용 배경을 먼저 제시한다.",
    )
    if answer_text and "…" not in intro and len(intro) < 40:
        intro = answer_text.split(".")[0] + " 필요성을 다음과 같이 설명할 수 있다."

    conclusion = extra.get(
        "conclusion",
        f"따라서 {h3}을 적용할 때는 {case_text[:60] + '…' if case_text else '구체적 사례'}를 근거로 시사점과 한계를 함께 도출해야 한다.",
    )

    mn_short = mnemonic.replace("암기:", "").strip() if mnemonic else "키워드"

    block = f"""
<details class="answer-extra-wrap">
<summary><span class="answer-extra-title">✍️ 답안 템플릿 · {h3}</span><span class="answer-extra-hint">접기/펼치기</span></summary>
<div class="answer-extra">
<span class="exam-tag">{exam}</span>
<div class="answer-outline"><strong>답안 목차 (2교시형 · {h3})</strong>
<ol>
<li><b>1. 개요</b> — 정의 · 필요성 · {mn_short} 키워드 소개</li>
<li><b>2. 핵심</b> — 구성요소·도식 · 비교표(본문 표 활용) · IT/경영 연계</li>
<li><b>3. 사례·적용</b> — {('「' + case_text[:40] + '…」') if case_text else '교재·기출 사례'} · 적용 고려사항</li>
<li><b>4. 결론</b> — 기대효과 · 한계 · 발전방향</li>
</ol></div>
<blockquote><strong>서론 예시</strong> {intro}</blockquote>
<div class="effect-box"><strong>기대효과</strong><p>{effects}</p></div>
<div class="limit-box"><strong>한계·주의</strong><p>{limits}</p></div>
<blockquote><strong>결론 예시</strong> {conclusion}</blockquote>
</div>
</details>"""

    article_html = build_depth(article_html, art_id)
    return article_html + block


def update_nav(html: str) -> str:
    old = '<a href="#flashcards">9. 암기카드</a>'
    new = '<a href="#answer-template">9. 답안 템플릿</a><a href="#flashcards">10. 암기카드</a>'
    return html.replace(old, new)


def main():
    html = PAGE.read_text(encoding="utf-8")

    if 'id="study-1"' not in html:
        html = html.replace(
            '</article></section><section id="strategy"',
            '</article>' + STUDY_EXTRA + '</section><section id="strategy"',
            1,
        )

    if 'id="answer-template"' not in html:
        html = html.replace(
            '<section id="flashcards" class="flash-section">',
            TEMPLATE_SECTION + '\n<section id="flashcards" class="flash-section">',
            1,
        )
        html = html.replace(
            '<h2>9. 클릭형 암기카드</h2>',
            '<h2>10. 클릭형 암기카드</h2>',
            1,
        )

    html = update_nav(html)

    if 'id="past-exams"' not in html:
        html = html.replace(
            '<a href="#flashcards">10. 암기카드</a></nav>',
            '<a href="#flashcards">10. 암기카드</a><a href="#past-exams">11. 기출문제</a></nav>',
        )
        html = html.replace(
            '<a href="#flashcards">10. 암기카드</a></div></details>',
            '<a href="#flashcards">10. 암기카드</a><a href="#past-exams">11. 기출문제</a></div></details>',
        )

    def repl_article(m):
        art_id = m.group(1)
        body = strip_generated_blocks(m.group(2))
        return f'<article id="{art_id}" class="topic-card">{build_extras(body, art_id)}</article>'

    html = re.sub(
        r'<article id="([^"]+)" class="topic-card">(.*?)</article>',
        repl_article,
        html,
        flags=re.DOTALL,
    )

    PAGE.write_text(html, encoding="utf-8")
    extra = len(re.findall(r'class="answer-extra-wrap"', html))
    depth = len(re.findall(r'class="topic-depth-wrap"', html))
    print(f"expanded: {PAGE.name}, depth: {depth}, answer-extra: {extra}")


if __name__ == "__main__":
    main()
