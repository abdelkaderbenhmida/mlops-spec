# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Tests for the credit risk prediction API."""
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))

import main
from _data import build_subset_df

from xgboost import XGBClassifier

import preprocess

VALID_PAYLOAD = {
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


def install_trained_model(monkeypatch, n_rows: int = 300, n_estimators: int = 20):
    """Fit a tiny model and make the app serve it instead of training at startup."""
    df = build_subset_df(n_rows)
    X, y = preprocess.encode_features(df)
    clf = XGBClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X, y)

    def fake_train():
        main.MODEL = clf
        main.FEATURE_NAMES = preprocess.get_feature_names()
        main.MODEL_METRICS.update({
            "model_name": type(clf).__name__,
            "n_estimators": clf.n_estimators,
            "max_depth": clf.max_depth,
            "auc": 0.85,
            "f1": 0.62,
        })

    monkeypatch.setattr(main, "train_model", fake_train)


class TestHealth:
    def test_health_ok(self, monkeypatch):
        install_trained_model(monkeypatch)
        with TestClient(main.app) as c:
            r = c.get("/health")
        assert r.status_code == 200
        body = r.json()
        assert body["status"] == "ok"
        assert body["model_loaded"] is True
        assert body["model_version"] == "1.0"


class TestPredict:
    def test_predict_returns_200_with_valid_payload(self, monkeypatch):
        install_trained_model(monkeypatch)
        with TestClient(main.app) as c:
            r = c.post("/predict", json=VALID_PAYLOAD)
        assert r.status_code == 200
        body = r.json()
        assert body["prediction"] in (0, 1)
        assert isinstance(body["probability"], float)
        assert 0.0 <= body["probability"] <= 1.0
        assert body["risk_tier"] in ("low", "medium", "high", "critical")

    def test_predict_422_on_missing_fields(self, monkeypatch):
        install_trained_model(monkeypatch)
        with TestClient(main.app) as c:
            r = c.post("/predict", json={"age": 35})
        assert r.status_code == 422

    def test_predict_422_on_unknown_category(self, monkeypatch):
        install_trained_model(monkeypatch)
        payload = dict(VALID_PAYLOAD)
        payload["checking_status"] = "A99"
        with TestClient(main.app) as c:
            r = c.post("/predict", json=payload)
        assert r.status_code == 422


class TestHistoryStats:
    def test_history_and_stats_record_predictions(self, monkeypatch):
        install_trained_model(monkeypatch)
        main.PREDICTIONS.clear()
        with TestClient(main.app) as c:
            r = c.post("/predict", json=VALID_PAYLOAD)
            assert r.status_code == 200
            hist = c.get("/history").json()
            stats = c.get("/stats").json()
        assert hist["total"] == 1
        assert hist["items"][0]["prediction"] == r.json()["prediction"]
        assert stats["total_predictions"] == 1
        assert stats["risk_tier_distribution"] == {
            "low": 0, "medium": 0, "high": 0, "critical": 0
        } or sum(stats["risk_tier_distribution"].values()) == 1

    def test_model_info(self, monkeypatch):
        install_trained_model(monkeypatch)
        with TestClient(main.app) as c:
            info = c.get("/model-info").json()
        assert info["model_name"] == "XGBClassifier"
        assert "auc" in info["metrics"]
        assert len(info["feature_importance"]) > 0