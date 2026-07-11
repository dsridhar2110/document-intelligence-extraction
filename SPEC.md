# Document Intelligence & Data Extraction POC — build spec

> **Why this exists:** closes the single biggest gap in the **LSEG Senior Associate (Emerging Tech / D&A Operations)** JD —
> *"expertise in sourcing, scraping, crawling, extraction, pre/post-processing… processing structured, semi-structured &
> unstructured data from PDF & scanned documents"*. Build this over the ~1 month before the application goes in, then
> swap the placeholder line on the resume for real metrics. Ship the explainable version; frame anything heavier as roadmap.

## 1. The one-line problem
Turn messy documents (native PDFs, **scanned** PDFs, and a few web pages) into **clean, schema-validated, query-ready records** — automatically, with a human-review checkpoint.

## 2. Scope (keep it small and finishable)
Pick ONE document type with a public, financial-flavoured corpus so it reads as relevant to LSEG. Good options:
- **Company financial filings / annual reports** (PDF, some scanned) → extract fields: company, period, revenue, net income, EPS, currency.
- **Invoices / contracts** (if filings are too heavy) → vendor, date, line items, totals.

Target: **20–50 documents**, mix of native + scanned. Enough to quote an accuracy number, small enough to finish.

## 3. Pipeline (the 4 stages to demo)
1. **Source** — a small scraper/crawler that pulls the documents (e.g. `requests` + `BeautifulSoup`, or an API). Log provenance (URL, timestamp).
2. **Extract** —
   - Native PDFs: `pdfplumber` / `PyMuPDF` for text + tables.
   - **Scanned** PDFs: OCR with `pytesseract` (Tesseract) or `docTR` / AWS Textract for layout-aware extraction.
3. **Structure** — an **LLM + RAG** step: prompt-engineered template that reads the extracted text and returns **schema-validated JSON** (use `pydantic` + function-calling / structured outputs). RAG = retrieve the relevant page/section before asking the LLM, so it scales past context limits.
4. **Validate / post-process** — type & range checks, guardrails, confidence flags; anything low-confidence routes to a **human-review** queue (a simple Streamlit table).

## 4. Evaluation (this is what makes it a real bullet)
- Hand-label a **gold set** (~15–20 docs) with the correct field values.
- Report **field-level extraction accuracy / F1**, and **% straight-through vs. sent to review**.
- Note throughput (docs/min) and cost/doc if using a hosted model.
- These numbers replace *"(metrics being finalised)"* on the resume.

## 5. Stack
`Python` · `pdfplumber`/`PyMuPDF` · `pytesseract`/`docTR` (or AWS Textract) · `requests`+`BeautifulSoup` · an LLM API (structured outputs) · `pydantic` · `Streamlit` (review UI) · deploy on `AWS` (or Vercel/Render for the UI).

## 6. Deliverables (so it presents — workspace convention)
- [ ] Repo pushed to `github.com/dsridhar2110` (commits authored as dsridhar2110).
- [ ] Short README/case-study: problem → pipeline → gold-set metrics → screenshots (use the `case-study` skill).
- [ ] Streamlit demo link (the review UI over a few sample docs).
- [ ] Portfolio card on deeksh.com.

## 7. Resume line — swap in once built
> **Document Intelligence & Data Extraction Pipeline** — Python · LLM/RAG · OCR · Prompt Engineering · AWS
> Built a sourcing-to-structured-data pipeline: scrape → OCR/parse (native + scanned PDFs) → LLM+RAG extraction into
> schema-validated JSON → validation with human-review routing. Achieved **XX% field-level accuracy** across a gold set of
> NN documents, **YY% straight-through** with the rest flagged for review.

## 8. Stretch (roadmap only — don't block the ship)
Fine-tuned extraction model; table-structure recognition; a knowledge-graph layer over extracted entities; evaluation dashboard.
