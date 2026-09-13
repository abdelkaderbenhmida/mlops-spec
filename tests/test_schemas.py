# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Tests for the credit risk API schemas (German Credit Data)."""
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))

from schemas import PredictRequest, PredictResponse, HealthResponse


def valid_kwargs(**overrides):
    base = {
        "checking_status": "A12",
        "duration": 24,
        "credit_history": "A34",
        "purpose": "A43",
        "credit_amount": 4000,
        "savings_status": "A61",
        "employment": "A73",
        "installment_rate": 3,
        "personal_status": "A93",
        "other_parties": "A101",
        "residence_since": 4,
        "property_magnitude": "A121",
        "age": 35,
        "other_payment_plans": "A143",
        "housing": "A152",
        "existing_credits": 2,
        "job": "A173",
        "num_dependents": 1,
        "own_telephone": "A192",
        "foreign_worker": "A201",
    }
    base.update(overrides)
    return base


class TestPredictRequest:
    def test_valid_request(self):
        r = PredictRequest(**valid_kwargs())
        assert r.age == 35
        assert r.checking_status == "A12"
        assert r.credit_amount == 4000

    def test_rejects_unknown_checking_status(self):
        with pytest.raises(ValidationError):
            PredictRequest(**valid_kwargs(checking_status="A99"))

    def test_rejects_duration_out_of_range(self):
        with pytest.raises(ValidationError):
            PredictRequest(**valid_kwargs(duration=0))

    def test_rejects_negative_credit_amount(self):
        with pytest.raises(ValidationError):
            PredictRequest(**valid_kwargs(credit_amount=-100))


class TestPredictResponse:
    def test_valid_response(self):
        r = PredictResponse(prediction=1, probability=0.75, risk_tier="high")
        assert r.prediction == 1
        assert r.risk_tier == "high"


class TestHealthResponse:
    def test_default_status(self):
        h = HealthResponse()
        assert h.status == "ok"