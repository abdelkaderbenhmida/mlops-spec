"""API tests for the FastAPI churn prediction service (api/main.py).

TODO: api/main.py, api/model.py, api/db.py are pending — they are being
built by the backend agent in its own worktree. These tests skip until the
backend code lands on this branch.

The test client never talks to a real MLflow server or PostgreSQL:
  - MLflow loading is stubbed (load_model is a no-op, model globals are set
    directly) so no external tracking server is required.
  - DB persistence is stubbed with a FakeSession so no Postgres is needed.
"""
import pytest

mlflow = pytest.importorskip("mlflow", reason="mlflow not installed")
sklearn = pytest.importorskip("sklearn", reason="scikit-learn not installed")

main = pytest.importorskip(
    "api.main",
    reason="api/main.py pending (backend agent builds api/ in parallel)",
)

from fastapi.testclient import TestClient

import model
import db as api_db

VALID_PAYLOAD = {
    "tenure": 12,
    "monthly_charges": 65.5,
    "total_charges": 786.0,
    "contract": "Month-to-month",
    "payment_method": "Electronic check",
}


class FakeSession:
    """Drop-in stand-in for a SQLAlchemy session (no DB connection)."""

    def __init__(self):
        self.added = []
        self.commits = 0
        self.closed = False

    def add(self, record):
        self.added.append(record)

    def commit(self):
        self.commits += 1

    def close(self):
        self.closed = True

    def query(self, *args, **kwargs):
        class Query:
            def order_by(self, *a, **k):
                return self

            def limit(self, *a, **k):
                return self

            def all(self):
                return []

        return Query()


@pytest.fixture
def fake_session():
    return FakeSession()


@pytest.fixture
def client(monkeypatch, fake_session):
    monkeypatch.setattr(model, "_model_version", "test-1.0")
    monkeypatch.setattr(main, "init_db", lambda: None)
    monkeypatch.setattr(main, "load_model", lambda: None)
    monkeypatch.setattr(main, "get_session", lambda: fake_session)
    monkeypatch.setattr(main, "predict", lambda input_data: (1, 0.87))
    with TestClient(main.app) as c:
        yield c


class TestHealth:
    def test_health_ok(self, client):
        r = client.get("/health")
        assert r.status_code == 200
        body = r.json()
        assert body["status"] == "ok"
        assert body["model_version"] == "test-1.0"


class TestPredict:
    def test_valid_payload(self, client):
        r = client.post("/predict", json=VALID_PAYLOAD)
        assert r.status_code == 200
        body = r.json()
        assert body["prediction"] in (0, 1)
        assert isinstance(body["probability"], float)
        assert 0.0 <= body["probability"] <= 1.0

    def test_invalid_payload_returns_422(self, client):
        cases = [
            {},  # missing all required fields
            {"tenure": -5, "monthly_charges": 10.0, "total_charges": 50.0,
             "contract": "One year", "payment_method": "Mailed check"},  # tenure < 0
            {"tenure": 12, "monthly_charges": 65.5, "total_charges": 786.0,
             "contract": "Month-to-month"},  # missing payment_method
            {"tenure": "twelve", "monthly_charges": 65.5, "total_charges": 786.0,
             "contract": "Month-to-month", "payment_method": "Mailed check"},  # bad type
        ]
        for payload in cases:
            r = client.post("/predict", json=payload)
            assert r.status_code == 422, payload

    def test_prediction_persisted(self, client, fake_session):
        client.post("/predict", json=VALID_PAYLOAD)
        assert len(fake_session.added) == 1
        record = fake_session.added[0]
        assert record.input_json == VALID_PAYLOAD
        assert record.prediction == 1
        assert record.probability == "0.87"
        assert fake_session.commits == 1

    @pytest.mark.xfail(
        strict=False,
        reason=(
            "backend bug QA-REPORT H4: model.predict feeds snake_case fields "
            "(monthly_charges/total_charges) to preprocess.apply_encoders, which "
            "expects MonthlyCharges/TotalCharges -> KeyError -> HTTP 500. "
            "Un-xfail when api/model.py maps the fields."
        ),
    )
    def test_real_predict_path(self, tmp_path, monkeypatch):
        """Exercises model.predict end-to-end with a real trained classifier.

        MLflow server is avoided by setting the module globals directly and
        stubbing load_model; preprocessing runs on a small synthetic frame.
        """
        preprocess = pytest.importorskip(
            "preprocess", reason="ml/preprocess.py pending (backend agent)"
        )
        from _data import build_subset_df

        from sklearn.ensemble import RandomForestClassifier

        df = build_subset_df()
        monkeypatch.setattr(preprocess, "load_data", lambda: df)
        X, y, _ = preprocess.encode_features(df)
        clf = RandomForestClassifier(n_estimators=20, random_state=42)
        clf.fit(X, y)

        monkeypatch.setattr(model, "_model", clf)
        monkeypatch.setattr(model, "_model_version", "test-1.0")
        monkeypatch.setattr(main, "init_db", lambda: None)
        monkeypatch.setattr(main, "load_model", lambda: None)
        monkeypatch.setattr(main, "get_session", lambda: FakeSession())

        with TestClient(main.app) as c:
            r = c.post("/predict", json=VALID_PAYLOAD)
        assert r.status_code == 200
        body = r.json()
        assert body["prediction"] in (0, 1)
        assert isinstance(body["probability"], float)
        assert 0.0 <= body["probability"] <= 1.0

    def test_out_of_vocab_category_rejected(self, tmp_path, monkeypatch):
        """Unknown categorical values crash the LabelEncoder at prediction time.

        Observed: model.predict() raises ValueError -> endpoint returns 500.
        Ideally the schema would constrain contract/payment_method to the
        training vocabulary so the client gets a 422. See tests/QA-REPORT.md.
        """
        preprocess = pytest.importorskip(
            "preprocess", reason="ml/preprocess.py pending (backend agent)"
        )
        from _data import build_subset_df

        from sklearn.ensemble import RandomForestClassifier

        df = build_subset_df()
        monkeypatch.setattr(preprocess, "load_data", lambda: df)
        X, y, _ = preprocess.encode_features(df)
        clf = RandomForestClassifier(n_estimators=20, random_state=42)
        clf.fit(X, y)

        monkeypatch.setattr(model, "_model", clf)
        monkeypatch.setattr(main, "init_db", lambda: None)
        monkeypatch.setattr(main, "load_model", lambda: None)
        monkeypatch.setattr(main, "get_session", lambda: FakeSession())

        bad = dict(VALID_PAYLOAD, contract="Zero-year platinum")
        with TestClient(main.app) as c:
            r = c.post("/predict", json=bad)
        assert r.status_code >= 400


class TestMetrics:
    def test_metrics_exposes_prometheus(self, client):
        r = client.get("/metrics")
        assert r.status_code == 200
        assert "text/plain" in r.headers.get("content-type", "")
        assert "http_requests_total" in r.text


class TestPredictions:
    def test_predictions_empty(self, client):
        r = client.get("/predictions")
        assert r.status_code == 200
        assert r.json() == []


class TestDbConfig:
    def test_default_url(self, monkeypatch):
        for var in ("DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"):
            monkeypatch.delenv(var, raising=False)
        assert api_db.get_database_url() == (
            "postgresql://postgres:postgres@postgres-service:5432/mlops"
        )

    def test_url_reads_env(self, monkeypatch):
        monkeypatch.setenv("DB_HOST", "db.example.com")
        monkeypatch.setenv("DB_PORT", "5433")
        monkeypatch.setenv("DB_USER", "svc")
        monkeypatch.setenv("DB_PASSWORD", "s3cret")
        monkeypatch.setenv("DB_NAME", "churn")
        assert api_db.get_database_url() == (
            "postgresql://svc:s3cret@db.example.com:5433/churn"
        )
