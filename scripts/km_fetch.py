"""Comoros: no official Comorian legislation website was reachable (Assemblée de l'Union, Journal officiel,
Ministry of Justice), so the official texts are taken from WIPO Lex (World Intellectual Property Organization),
whose FAQ allows reproduction of official legal texts with credit to the source. Only texts that are official
editions are used (texts reproduced from private publishers such as Droit-Afrique / comores-droit.com and
translations are excluded).

  (WIPO Lex 19948, Code des douanes 2016, was examined but its text layer is a poor OCR of a scan: not used.)
  WIPO Lex 8669   Code pénal (Loi n° 082 P/A.F, Loi n° 95-012/AF)
Cache: _raw/km/. Usage: python km_fetch.py
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km_text import fetch  # noqa: E402

RAW = os.environ.get("KM_RAW", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_raw", "km"))
TEXTS = {
    "8669": {"title": "Code pénal", "identifier": "Loi n° 082 P/A.F ; Loi n° 95-012/AF", "type": "code", "date": "",
             "path": "codes/code-penal.md"},
}


def main():
    items = []
    for wid, meta in TEXTS.items():
        page = "https://www.wipo.int/wipolex/fr/legislation/details/%s" % wid
        p = fetch(page, os.path.join(RAW, "html", "wipo-%s.html" % wid), delay=4)
        h = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r'href="(https://wipolex-res\.wipo\.int/edocs/lexdocs/laws/fr/km/[^"]+)"', h)
        if not m:
            print("no pdf link", wid)
            continue
        url = html.unescape(m.group(1))
        f = fetch(url, os.path.join(RAW, "pdf", "wipo-%s.pdf" % wid), delay=4, check_pdf=True, timeout=300)
        items.append(dict(meta, wipo_id=wid, source=page, file_url=url.split("?")[0], file=f))
        print("ok " if f else "FAIL", meta["title"])
    json.dump(items, open(os.path.join(RAW, "index.json"), "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    main()
