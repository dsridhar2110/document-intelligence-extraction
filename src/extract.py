"""Text-extraction stage (skeleton).

Native PDFs -> text via pdfplumber/PyMuPDF; scanned PDFs -> OCR via pytesseract/docTR.
Returns raw page text; the LLM+RAG structuring stage (src/structure.py) turns it into a
FinancialRecord. Implement incrementally — the schema + tests already lock the contract.
"""

from __future__ import annotations

from pathlib import Path


def is_scanned(pdf_path: str | Path) -> bool:
    """Heuristic: a PDF with (almost) no extractable text is a scan needing OCR.

    TODO: implement with pdfplumber page.extract_text() length check.
    """
    raise NotImplementedError


def extract_text(pdf_path: str | Path) -> str:
    """Return the document's text. Route scanned PDFs through OCR, native PDFs through a parser.

    TODO: pdfplumber/PyMuPDF for native; pytesseract/docTR (or AWS Textract) for scanned.
    """
    raise NotImplementedError
