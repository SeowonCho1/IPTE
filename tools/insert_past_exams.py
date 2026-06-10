# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
page = ROOT / "pages/03-경영컨설팅.html"
section = (ROOT / "tools/past_exams_section.html").read_text(encoding="utf-8")
html = page.read_text(encoding="utf-8")

if 'id="past-exams"' in html:
    print("already exists")
else:
    html = html.replace("  </section>\n</main>", "  </section>\n" + section + "\n</main>", 1)
    nav_old = '<a href="#flashcards">10. 암기카드</a></nav>'
    nav_new = '<a href="#flashcards">10. 암기카드</a><a href="#past-exams">11. 기출문제</a></nav>'
    html = html.replace(nav_old, nav_new)
    page.write_text(html, encoding="utf-8")
    print("done")
