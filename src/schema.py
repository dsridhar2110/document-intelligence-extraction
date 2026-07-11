"""Target schema + validation for extracted financial records.

Std-lib only so the test suite runs anywhere. When the LLM/RAG stage lands, this same
schema + validate() guards its output before anything reaches the pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import re

# A small ISO-4217 subset — extend as the corpus grows.
VALID_CURRENCIES = {"USD", "GBP", "EUR", "INR", "AUD", "JPY", "CHF", "CAD"}
# Reporting period like "FY2023", "Q4-2023", or "2023".
PERIOD_RE = re.compile(r"^(FY\d{4}|Q[1-4]-\d{4}|\d{4})$")


class ValidationError(ValueError):
    """Raised when an extracted record fails a hard validation rule."""


@dataclass
class FinancialRecord:
    company: str
    period: str
    revenue: float
    net_income: Optional[float] = None
    eps: Optional[float] = None
    currency: str = "USD"

    def validate(self) -> "FinancialRecord":
        """Hard guardrails. Returns self so calls can chain; raises on violation."""
        if not self.company or not self.company.strip():
            raise ValidationError("company must be non-empty")
        if not PERIOD_RE.match(self.period):
            raise ValidationError(f"period '{self.period}' not in FY/Q/year format")
        if self.revenue is None or self.revenue < 0:
            raise ValidationError("revenue must be present and non-negative")
        if self.currency not in VALID_CURRENCIES:
            raise ValidationError(f"currency '{self.currency}' is not a recognised ISO code")
        return self


def needs_human_review(record: FinancialRecord, confidence: float) -> bool:
    """Route to a human when the model is unsure or a soft sanity check trips.

    Straight-through only when confidence is high AND the numbers are internally consistent
    (net income should not exceed revenue for a normal filing).
    """
    if confidence < 0.80:
        return True
    if record.net_income is not None and record.net_income > record.revenue:
        return True
    return False
