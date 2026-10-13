"""Comoros: convert the downloaded PDFs to Markdown (French). Usage: python km_convert.py <repo_dir>"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km_text import pdf_text, clean_pages, structure, write_md, text_quality  # noqa: E402

RAW = os.environ.get("KM_RAW", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_raw", "km"))
TODAY = datetime.date.today().isoformat()


def main(repo):
    for it in json.load(open(os.path.join(RAW, "index.json"))):
        if not it.get("file"):
            continue
        pages, _ = pdf_text(it["file"])
        full = re.sub(r"(\.\s?){4,}", " ", "\n".join(pages))
        if text_quality(full) < 0.75:
            print("SKIP (poor text):", it["title"], round(text_quality(full), 2))
            continue
        lines = [x for x in clean_pages(pages) if not re.search(r"(\.\s?){6,}\s*\d*$", x)]
        meta = {"title": it["title"], "identifier": it["identifier"], "type": it["type"], "jurisdiction": "km",
                "language": "fr", "date": it["date"], "status": "unknown", "source": it["file_url"],
                "retrieved": TODAY, "note": "Texte officiel reproduit par WIPO Lex (fiche %s)" % it["source"]}
        write_md(os.path.join(repo, it["path"]), meta, it["title"], structure(lines, "fr"))
        print("written", it["path"])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
