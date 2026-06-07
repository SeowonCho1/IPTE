# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for rel in ("pages/01-sw공학.html", "pages/02-sw테스트.html"):
    text = (ROOT / rel).read_text(encoding="utf-8")
    ids = set(re.findall(r'id="([^"]+)"', text))
    book = re.search(r'id="mnemonic-book".*?</section>', text, re.DOTALL)
    links = set(re.findall(r'href="(#[^"]+)"', book.group())) if book else set()
    missing = sorted(h[1:] for h in links if h[1:] not in ids)
    print(f"{rel}: {len(links)} links, {len(missing)} missing")
    for m in missing:
        print(f"  - #{m}")
