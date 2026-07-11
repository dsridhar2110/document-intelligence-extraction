# Document Intelligence — LSEG JD → evidence coverage map

> ✅ proven · ⚠️ partial · ❌ gap. This project exists to turn the ⚠️/❌ document-extraction rows ✅.

| LSEG JD requirement | Status | Where |
|---|---|---|
| Sourcing / scraping / crawling | ⚠️→✅ | `src/source.py` (scraper) — building |
| Extraction from **PDF & scanned documents** | ⚠️→✅ | `src/extract.py` (native + OCR) — building |
| Pre-/post-processing | ✅ | `src/schema.py` validation + guardrails |
| Structured / semi-/unstructured data | ✅ | doc text → schema-validated JSON |
| **LLMs / RAG workflow** | ✅ | `src/structure.py` (LLM + RAG) — building |
| **Prompt engineering** | ✅ | extraction templates |
| Python + libraries + model building | ✅ | whole repo |
| Statistics / evaluation | ✅ | gold-set field-level accuracy / F1 |
| MLOps approaches | ✅ | versioned pipeline, tests, human-in-loop review |
| Cloud (AWS) | ✅ | deployment target |
| Data management framework (acquisition→transformation) | ✅ | the pipeline itself |
| Financial content | ✅ | financial-filings corpus |

## Open gaps to close before applying (~1 month runway)
- [ ] Implement OCR + native extraction (`extract.py`)
- [ ] Implement LLM+RAG structuring (`structure.py`)
- [ ] Implement scraper (`source.py`)
- [ ] Hand-label gold set (~15–20 docs) + compute accuracy/F1, straight-through %
- [ ] Streamlit review UI + deploy; swap real metrics onto the resume line

## Notes
Resume currently carries this as an **"(in progress)"** project with "(metrics being finalised)". By the
time the LSEG application goes in, this must be built and the placeholder numbers replaced with real ones.
