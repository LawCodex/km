# Comores (KM) — législation en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal corpus.** Only the **Code pénal** of the Comoros (Loi n° 082 P/A.F, as amended by Loi n° 95-012/AF),
in **French**, as reproduced from an official edition by **WIPO Lex** (World Intellectual Property Organization).
Retrieved 2026-10-13.

| Category | Files |
|---|---|
| Codes | 1 |

## Structure

```
codes/code-penal.md      Code pénal (dispositions préliminaires, Livres, Chapitres, Articles)
```

Text extracted with poppler `pdftotext`; LIVRE / TITRE / CHAPITRE / SECTION become headings and each article an
`Article N` heading. `status: unknown` — the code has been amended since (a new penal code was adopted in 2020/2021
and is not available from an official online source).

## Not covered / known gaps

* **The Constitution and all other legislation are missing.** No official Comorian legislation website was
  reachable: the Assemblée de l'Union, the Journal officiel, the Government and Ministry of Justice sites were all
  unreachable or do not publish legal texts; the Presidency site (beit-salam.km) publishes news and a few decree
  scans only; the Ministry of Finance (finances.gouv.km) publishes the annual finance laws as scanned PDFs (the
  only one with a text layer, the Loi de finances 2026, is a low-quality OCR of a scan and was not used).
* WIPO Lex also lists the Constitution of 2018 (but only as an English translation from the Constitute Project),
  the 2001/2009 Constitution (reproduced from the private publisher Droit-Afrique), the Code de la santé publique
  (from the private site comores-droit.com) and the Code des douanes 2016 (official Customs edition, but its text
  layer is a poor OCR of a scan): none of these were used.

## Sources and licence

| Source | URL |
|---|---|
| WIPO Lex — Comoros, Code pénal | https://www.wipo.int/wipolex/fr/legislation/details/8669 |

WIPO Lex's FAQ states that official legal texts may be reproduced provided the source is credited
(https://www.wipo.int/en/web/wipolex/faq); the text is credited to WIPO Lex in the front matter. Two pages were
requested, with an identifying User-Agent.

## Regenerate

```
pip install -r scripts/requirements.txt     # plus poppler (pdftotext, pdfinfo)
python scripts/km_fetch.py                  # downloads into ../_raw/km/
python scripts/km_convert.py .
```
