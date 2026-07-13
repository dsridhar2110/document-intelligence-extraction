# Document Intelligence & Data Extraction

> **Status: early scaffold — not a working pipeline yet.**
> What exists today is the data contract: a validated `pydantic`-style schema and its tests.
> Text extraction, OCR, the LLM structuring stage, the scraper and the review UI are **designed
> but not implemented** — `src/extract.py` currently raises `NotImplementedError`.
> Everything below the line describes the *intended* system, not a built one.

An in-progress portfolio project: turn messy financial documents — native PDFs, scanned PDFs and
web pages — into clean, schema-validated, query-ready records, with a human-review checkpoint for
anything the system isn't confident about.

Built as interview preparation for an **LSEG** Data / Emerging-Tech role, targeting the *"automated
sourcing and extraction"* part of a financial data-management framework — at toy scale, and honestly
measured.

## What actually works today

| Component | State |
|---|---|
| Target schema + field validation (`src/schema.py`) | ✅ Implemented |
| Schema tests (`tests/test_schema.py`, TDD-first) | ✅ Passing |
| Text extraction, native + OCR (`src/extract.py`) | ⬜ Skeleton — `NotImplementedError` |
| LLM structuring → JSON (`src/structure.py`) | ⬜ Not started |
| Sourcing / scraper (`src/source.py`) | ⬜ Not started |
| Gold set + accuracy metrics | ⬜ Not started |
| Streamlit review UI | ⬜ Not started |

The schema and its tests came first on purpose: they lock the contract every later stage has to
satisfy, so the extraction work has something to be measured against rather than the other way round.

## The intended pipeline (design, not yet built)

`source (scrape/crawl)` → `extract text (native + OCR)` → `structure (LLM → JSON)` → `validate + route to human review`

**Planned stack:** Python · pdfplumber / PyMuPDF · pytesseract / docTR for OCR · a hosted LLM with
structured outputs, grounded by retrieval over the document text · pydantic · Streamlit.

**Planned measurement:** field-level extraction accuracy / F1 against a hand-labelled gold set of
15–20 documents, plus the share of records auto-accepted versus routed to a human. Those numbers
don't exist yet, because the pipeline that would produce them doesn't exist yet.

## Run what's here

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q                     # schema + validation tests — these pass
```

## Docs

- `CLAUDE.md` — full context: problem, data, mechanism, model, metrics, build plan
- `SPEC.md` — day-zero build spec
- `requirements.md` — JD → evidence coverage map
- `presentation/interview-walkthrough.html` — walkthrough page

---
*Independent portfolio project · interview preparation · public/synthetic data · not affiliated with LSEG.*
