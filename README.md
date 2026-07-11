# Document Intelligence & Data Extraction

Turn messy financial documents — native PDFs, **scanned** PDFs and web pages — into clean,
schema-validated, query-ready records, automatically, with a human-review checkpoint.

Built as a portfolio project for an **LSEG** Data / Emerging-Tech role: the *"automated sourcing and
extraction"* plank of a financial data-management framework, at toy scale but honestly measured.

## Pipeline
`source (scrape/crawl)` → `extract text (native + OCR)` → `structure (LLM + RAG → JSON)` → `validate + route to human review`

## Stack
Python · pdfplumber / PyMuPDF · pytesseract / docTR (OCR) · an LLM with structured outputs + RAG · pydantic · Streamlit · AWS

## Status
Scaffold + schema + validation + TDD tests are in. Extraction, structuring, scraper, gold-set metrics
and the review UI are the build plan (see `CLAUDE.md` §7, `requirements.md`).

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Docs
- `CLAUDE.md` — single source of truth (problem → data → mechanism → model → metrics → plan)
- `SPEC.md` — day-zero build spec
- `requirements.md` — JD → evidence coverage map
- `presentation/interview-walkthrough.html` — the rehearsal / send-ahead page

---
*Independent portfolio project · interview preparation · public/synthetic data · not affiliated with LSEG.*
