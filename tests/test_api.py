"""Tests for the credit risk prediction API."""
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))

import main
import model
from _data import build_subset_df

from sklearn.ensemble import GradientBoostingClassifier

import preprocess

VALID_PAYLOAD = {
    "age": 35,
    "income": 65000.0,
    "monthly_income": 5416.67,
    "debt_ratio": 0.35,
    "revolving_utilization": 45.2,
    "num_open_credit_lines": 6,
    "num_dependents": 1,
    "num_30_59_days_late": 0,
    "num_60_89_days_late": 0,
    "num_90_days_late": 0,
    "num_mortgages": 1,
    "number_real_estate_loans": 1,
}


class FakeSession:
    def __init__(self):
        self.added = []
        self.committed = 0

    def add(self, obj):
        self.added.append(obj)

    def commit(self):
        self.committed += 1

    def close(self):
        pass

    def query(self, *a, **kw):
        return self

    def order_by(self, *a, **kw):
        return self

    def limit(self, *a, **kw):
        return self

    def all(self):
        return []


class TestHealth:
    def test_health_ok(self, monkeypatch):
        monkeypatch.setattr(main, "load_model", lambda: None)
        monkeypatch.setattr(main, "init_db", lambda: None)
        monkeypatch.setattr(main, "get_session", lambda: FakeSession())
        monkeypatch.setattr(main, "get_model_version", lambda: "test-1.0")
        with TestClient(main.app) as c:
            r = c.get("/health")
        assert r.status_code == 200
        body = r.json()
        assert body["status"] == "ok"
        assert body["model_version"] == "test-1.0"


class TestPredict:
    def test_predict_returns_200_with_valid_payload(self, monkeypatch):
        df = build_subset_df()
        X, y = preprocess.encode_features(df)
        clf = GradientBoostingClassifier(n_estimators=20, random_state=42)
        clf.fit(X, y)

        monkeypatch.setattr(main, "load_model", lambda: None)
        monkeypatch.setattr(model, "_model", clf)
        monkeypatch.setattr(model, "_model_version", "test-1.0")
        monkeypatch.setattr(main, "init_db", lambda: None)
        monkeypatch.setattr(main, "get_session", lambda: FakeSession())

        with TestClient(main.app) as c:
            r = c.post("/predict", json=VALID_PAYLOAD)
        assert r.status_code == 200
        body = r.json()
        assert body["prediction"] in (0, 1)
        assert isinstance(body["probability"], float)
        assert 0.0 <= body["probability"] <= 1.0
        assert body["risk_tier"] in ("low", "medium", "high", "critical")

    def test_predict_422_on_missing_fields(self, monkeypatch):
        monkeypatch.setattr(main, "load_model", lambda: None)
        monkeypatch.setattr(main, "init_db", lambda: None)
        monkeypatch.setattr(main, "get_session", lambda: FakeSession())

        with TestClient(main.app) as c:
            r = c.post("/predict", json={"age": 30})
        assert r.status_code == 422
