# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "pages"
PAT = re.compile(
    r'<summary><span class="mn-key">([^<]*)</span><span class="mn-from">([^<]*)</span></summary>'
)
REPL = r'<summary><span class="mn-from">\2</span><span class="mn-key">\1</span></summary>'

for name in ("01-sw공학.html", "02-sw테스트.html", "03-경영컨설팅.html"):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    new_text, n = PAT.subn(REPL, text)
    if n:
        path.write_text(new_text, encoding="utf-8")
    print(f"{name}: swapped {n}")
