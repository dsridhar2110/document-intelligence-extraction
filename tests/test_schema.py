"""TDD tests for the extraction schema + review-routing logic.

These lock the contract the LLM/RAG stage must satisfy. Std-lib only — run with `pytest -q`.
"""

import pytest

from src.schema import (
    FinancialRecord,
    ValidationError,
    needs_human_review,
)


def _good() -> FinancialRecord:
    return FinancialRecord(
        company="Acme Corp",
        period="FY2023",
        revenue=1_000_000.0,
        net_income=120_000.0,
        eps=1.24,
        currency="USD",
    )


def test_valid_record_passes():
    assert _good().validate() is not None


def test_blank_company_rejected():
    r = _good()
    r.company = "   "
    with pytest.raises(ValidationError):
        r.validate()


def test_bad_period_rejected():
    r = _good()
    r.period = "March 2023"
    with pytest.raises(ValidationError):
        r.validate()


@pytest.mark.parametrize("period", ["FY2023", "Q4-2023", "2023"])
def test_period_formats_accepted(period):
    r = _good()
    r.period = period
    assert r.validate()


def test_negative_revenue_rejected():
    r = _good()
    r.revenue = -5.0
    with pytest.raises(ValidationError):
        r.validate()


def test_unknown_currency_rejected():
    r = _good()
    r.currency = "XYZ"
    with pytest.raises(ValidationError):
        r.validate()


def test_low_confidence_routes_to_review():
    assert needs_human_review(_good(), confidence=0.5) is True


def test_high_confidence_straight_through():
    assert needs_human_review(_good(), confidence=0.95) is False


def test_net_income_exceeding_revenue_routes_to_review():
    r = _good()
    r.net_income = r.revenue + 1  # implausible -> human check even at high confidence
    assert needs_human_review(r, confidence=0.99) is True
