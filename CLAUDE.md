# Document Intelligence & Data Extraction — Project Context (CLAUDE.md)

> Single source of truth for this repository. Read this first.
>
> **Disclaimer:** Independent portfolio project built as interview preparation for an LSEG role.
> Data is public financial documents / synthetic samples. Not affiliated with or endorsed by LSEG.

---

## 0. What this is (one paragraph)
A **document-intelligence pipeline** that turns messy financial documents — native PDFs, **scanned** PDFs,
and a few web pages — into **clean, schema-validated, query-ready records**, automatically, with a
human-review checkpoint for anything low-confidence. It sources the documents, extracts text (OCR for
scans), uses an **LLM + RAG** step to pull the fields into structured JSON, validates them, and routes
uncertain ones to a small review UI.

## 1. Why this exists (the objective)
- **Target role / JD:** Senior Associate — Emerging Tech Standard Delivery, D&A Operations, **LSEG, Bangalore (R0113916)**.
- **The gap it closes:** the JD's most specific, hardest-to-fake ask — *"sourcing, scraping, crawling, extraction,
  pre/post-processing… processing structured, semi-structured & unstructured data from PDF & scanned documents."*
  Deekshita's resume proves NLP/LLM/RAG but had no document-extraction artifact. This is that artifact.
- **Strategy:** build a working miniature of the sourcing-to-structured-data capability at the core of a
  data-management framework; present with humility.

**Locked decisions:**
- **Corpus:** financial documents (company filings / annual reports) — keeps it LSEG-relevant.
- **Model posture:** ship the explainable LLM+RAG extraction; a fine-tuned/table-structure model is roadmap only.
- **Ship shape:** Python engine → structured JSON → Streamlit review UI; push to `dsridhar2110`.

## 2. The business problem
Financial-analytics platforms are only as good as the data feeding them, and huge amounts of that data
arrive as **unstructured documents** — filings, reports, scanned statements. Keying them in by hand is slow,
expensive and error-prone; it doesn't scale to a growing document volume. **The product's job:** convert a
document into a structured, validated record automatically, and only ask a human when it isn't sure.

## 3. The data
- **Source:** public company filings / annual reports (PDF) — a mix of **native** (text) and **scanned** (image) PDFs,
  plus a couple of web pages for the scraping/sourcing stage. Small synthetic samples included for tests.
- **Target schema:** `company`, `period`, `revenue`, `net_income`, `eps`, `currency` (see `src/schema.py`).
- **Grain:** one record per document (company × reporting period).
- **Honesty note:** the corpus is small (20–50 docs) and public; metrics are reported on a hand-labelled gold set.

## 4. Architecture & mechanism (the 4 stages)
1. **Source / acquire** — a small scraper/crawler pulls documents (`requests` + `BeautifulSoup` or an API); provenance logged.
2. **Extract text** — native PDFs via `pdfplumber`/`PyMuPDF`; **scanned** PDFs via OCR (`pytesseract` / `docTR`, or AWS Textract for layout).
3. **Structure** — an **LLM + RAG** step: retrieve the relevant page/section, then a prompt-engineered template
   returns **schema-validated JSON** (`pydantic` + structured outputs / function calling).
4. **Validate / post-process** — type & range checks, currency/format guardrails, a confidence flag; low-confidence
   records route to a **human-review** queue (a Streamlit table).

## 5. The model(s)
- **Primary (shipped):** a hosted **LLM with structured outputs**, grounded by **RAG** retrieval over the document text.
  Extraction is prompt-engineered, not trained — cheap to explain and defend.
- **Baseline to beat:** regex / rule-based field extraction (brittle on layout changes).
- **Roadmap (documented, not swapped in):** fine-tuned extraction model, table-structure recognition, a knowledge-graph
  layer over extracted entities, an evaluation dashboard.

## 6. Success metrics
- **Primary:** **field-level extraction accuracy / F1** on a hand-labelled gold set (~15–20 docs).
- **Operational:** **% straight-through** (auto-accepted) vs. **% routed to human review**; throughput (docs/min); cost/doc.
- **Business translation:** every point of accuracy + every straight-through % is manual keying removed from the pipeline.
- *(Numbers finalised once built — they replace the "(metrics being finalised)" line on the resume.)*

## 7. Build plan
| Step | What | Output |
|---|---|---|
| 1 | Schema + validation + tests (TDD) | `src/schema.py`, `tests/` green |
| 2 | Text extraction (native + OCR) | `src/extract.py` |
| 3 | LLM+RAG structuring | `src/structure.py` |
| 4 | Sourcing/scraper | `src/source.py` |
| 5 | Gold set + evaluation | `eval/` + metrics |
| 6 | Streamlit review UI + deploy | demo link |

## 8. How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q                     # schema + validation tests
python -m src.extract <path>  # (as stages land)
```

## 9. Results & status
- **Built:** project scaffold, schema + validation + TDD tests. *(as of first commit)*
- **Pending:** OCR extraction, LLM+RAG structuring, scraper, gold-set metrics, Streamlit UI.
- **Live demo:** _pending_ · **GitHub:** github.com/dsridhar2110/document-intelligence-extraction

## 10. Interview bridge
This is the "automated sourcing and extraction" plank of LSEG's data-management framework, at toy scale.
Honest framing: *"a small, honest version of the sourcing-to-structured-data problem — here's the pipeline,
here's how I measured it, and here's what I'd do next to make it production-grade."*
