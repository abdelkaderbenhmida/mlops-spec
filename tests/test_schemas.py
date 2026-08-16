"""Pydantic schema validation tests for api/schemas.py.

TODO: api/schemas.py is pending — it is being built by the backend agent in
its own worktree. These tests skip until api/schemas.py lands on this branch.
"""
import pytest

pydantic = pytest.importorskip(
    "pydantic", reason="pydantic not installed"
)
ValidationError = pydantic.ValidationError

schemas = pytest.importorskip(
    "api.schemas",
    reason="api/schemas.py pending (backend agent builds api/ in parallel)",
)

VALID_PAYLOAD = {
    "tenure": 12,
    "monthly_charges": 65.5,
    "total_charges": 786.0,
    "contract": "Month-to-month",
    "payment_method": "Electronic check",
}


class TestPredictRequest:
    def test_valid_payload(self):
        req = schemas.PredictRequest(**VALID_PAYLOAD)
        assert req.tenure == 12
        assert req.monthly_charges == 65.5
        assert req.total_charges == 786.0
        assert req.contract == "Month-to-month"
        assert req.payment_method == "Electronic check"

    def test_boundary_tenure_zero(self):
        payload = dict(VALID_PAYLOAD, tenure=0)
        assert schemas.PredictRequest(**payload).tenure == 0

    def test_boundary_tenure_max(self):
        payload = dict(VALID_PAYLOAD, tenure=100)
        assert schemas.PredictRequest(**payload).tenure == 100

    def test_missing_required_field(self):
        payload = dict(VALID_PAYLOAD)
        del payload["payment_method"]
        with pytest.raises(ValidationError) as exc:
            schemas.PredictRequest(**payload)
        assert "payment_method" in str(exc.value)

    def test_negative_tenure_rejected(self):
        payload = dict(VALID_PAYLOAD, tenure=-1)
        with pytest.raises(ValidationError):
            schemas.PredictRequest(**payload)

    def test_tenure_above_max_rejected(self):
        payload = dict(VALID_PAYLOAD, tenure=101)
        with pytest.raises(ValidationError):
            schemas.PredictRequest(**payload)

    def test_negative_monthly_charges_rejected(self):
        payload = dict(VALID_PAYLOAD, monthly_charges=-0.01)
        with pytest.raises(ValidationError):
            schemas.PredictRequest(**payload)

    def test_wrong_type_rejected(self):
        payload = dict(VALID_PAYLOAD, tenure="twelve")
        with pytest.raises(ValidationError):
            schemas.PredictRequest(**payload)

    def test_extra_fields_ignored(self):
        payload = dict(VALID_PAYLOAD, hacker_field="x")
        req = schemas.PredictRequest(**payload)
        assert "hacker_field" not in req.model_dump()

    def test_model_dump_matches_input(self):
        req = schemas.PredictRequest(**VALID_PAYLOAD)
        assert req.model_dump() == VALID_PAYLOAD


class TestPredictResponse:
    def test_valid(self):
        resp = schemas.PredictResponse(prediction=1, probability=0.87)
        assert resp.prediction == 1
        assert resp.probability == 0.87

    def test_prediction_must_be_int(self):
        with pytest.raises(ValidationError):
            schemas.PredictResponse(prediction="yes", probability=0.5)


class TestHealthResponse:
    def test_default_status_ok(self):
        resp = schemas.HealthResponse()
        assert resp.status == "ok"

    def test_model_version_optional(self):
        assert schemas.HealthResponse(model_version="1").model_version == "1"
