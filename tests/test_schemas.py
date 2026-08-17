"""Tests for the credit risk API schemas."""
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))

from schemas import PredictRequest, PredictResponse, HealthResponse


class TestPredictRequest:
    def test_valid_request(self):
        r = PredictRequest(
            age=35, income=65000, monthly_income=5416.67,
            debt_ratio=0.35, revolving_utilization=45.2,
            num_open_credit_lines=6, num_dependents=1,
            num_30_59_days_late=0, num_60_89_days_late=0,
            num_90_days_late=0, num_mortgages=1,
            number_real_estate_loans=1,
        )
        assert r.age == 35
        assert r.income == 65000

    def test_rejects_age_below_18(self):
        with pytest.raises(ValidationError):
            PredictRequest(
                age=15, income=65000, monthly_income=5416.67,
                debt_ratio=0.35, revolving_utilization=45.2,
                num_open_credit_lines=6, num_dependents=1,
                num_30_59_days_late=0, num_60_89_days_late=0,
                num_90_days_late=0, num_mortgages=1,
                number_real_estate_loans=1,
            )

    def test_rejects_negative_income(self):
        with pytest.raises(ValidationError):
            PredictRequest(
                age=35, income=-100, monthly_income=5416.67,
                debt_ratio=0.35, revolving_utilization=45.2,
                num_open_credit_lines=6, num_dependents=1,
                num_30_59_days_late=0, num_60_89_days_late=0,
                num_90_days_late=0, num_mortgages=1,
                number_real_estate_loans=1,
            )


class TestPredictResponse:
    def test_valid_response(self):
        r = PredictResponse(prediction=1, probability=0.75, risk_tier="high")
        assert r.prediction == 1
        assert r.risk_tier == "high"


class TestHealthResponse:
    def test_default_status(self):
        h = HealthResponse()
        assert h.status == "ok"
