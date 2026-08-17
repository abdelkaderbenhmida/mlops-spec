"""Tests for the evaluation / CI gate (ml/evaluate.py).

TODO: ml/evaluate.py, ml/preprocess.py are pending — they are being built by
the backend agent in its own worktree. These tests skip until the backend code
lands on this branch.

The accuracy gate (exit 1 if accuracy < 0.70) is tested deterministically by
stubbing the loaded model so predictions are either all-correct (gate passes)
or all-wrong (gate fails). An end-to-end test registers a real classifier in a
local sqlite MLflow file store and runs the full evaluation.
"""
import pytest

pytest.importorskip("mlflow", reason="mlflow not installed")
pytest.importorskip("sklearn", reason="scikit-learn not installed")

evaluate = pytest.importorskip(
    "evaluate", reason="ml/evaluate.py pending (backend agent builds ml/ in parallel)"
)
preprocess = pytest.importorskip(
    "preprocess", reason="ml/preprocess.py pending (backend agent)"
)

from _data import build_subset_df


class _FakeClient:
    def __init__(self, version="1"):
        self._version = version

    def get_latest_versions(self, name, stages=None):
        from types import SimpleNamespace

        return [SimpleNamespace(name=name, version=self._version)]


class _StubClf:
    def __init__(self, preds):
        self._preds = preds

    def predict(self, X):
        return self._preds


def _stub_pipeline(monkeypatch, preds):
    """Wire evaluate.main's dependencies onto a synthetic frame."""
    df = build_subset_df()
    X_all, y_all, encoders = preprocess.encode_features(df)
    monkeypatch.setattr(evaluate, "MlflowClient", lambda *a, **k: _FakeClient())
    monkeypatch.setattr("mlflow.sklearn.load_model", lambda uri: _StubClf(preds))
    monkeypatch.setattr(evaluate, "load_data", lambda: df)
    monkeypatch.setattr(evaluate, "encode_features", lambda d: (X_all, y_all, encoders))
    monkeypatch.setattr(evaluate, "train_test_split", lambda d: (d, d))
    monkeypatch.setattr(evaluate, "apply_encoders", lambda d, e: X_all)
    return df


class TestAccuracyGate:
    def test_exits_1_when_accuracy_below_threshold(self, monkeypatch, capsys):
        df = build_subset_df()
        y_all = preprocess.encode_features(df)[1]
        wrong = 1 - y_all
        _stub_pipeline(monkeypatch, wrong)

        with pytest.raises(SystemExit) as exc:
            evaluate.main()

        assert exc.value.code == 1
        assert "Classification report" in capsys.readouterr().out

    def test_exits_0_when_accuracy_above_threshold(self, monkeypatch, capsys):
        df = build_subset_df()
        y_all = preprocess.encode_features(df)[1]
        _stub_pipeline(monkeypatch, y_all.to_numpy())

        with pytest.raises(SystemExit) as exc:
            evaluate.main()

        assert exc.value.code == 0
        assert "PASS" in capsys.readouterr().out

    def test_threshold_is_0_70(self):
        assert evaluate.ACCURACY_THRESHOLD == 0.70

    def test_exits_1_when_model_not_registered(self, monkeypatch):
        class NoModels:
            def get_latest_versions(self, name, stages=None):
                return []

        def _unexpected_load(uri):
            raise AssertionError("load_model should not be called when no model is registered")

        monkeypatch.setattr(evaluate, "MlflowClient", lambda *a, **k: NoModels())
        monkeypatch.setattr("mlflow.sklearn.load_model", _unexpected_load)

        with pytest.raises(SystemExit) as exc:
            evaluate.main()

        assert exc.value.code == 1


class TestEvaluateEndToEnd:
    def test_registered_model_passes_gate(self, tmp_path, monkeypatch):
        import mlflow
        import mlflow.sklearn
        from sklearn.ensemble import RandomForestClassifier

        df = build_subset_df()
        train_df, _ = preprocess.train_test_split(df)
        X_train, y_train, _ = preprocess.encode_features(train_df)
        clf = RandomForestClassifier(n_estimators=50, random_state=42)
        clf.fit(X_train, y_train)

        uri = f"sqlite:///{tmp_path / 'mlflow.db'}"
        mlflow.set_tracking_uri(uri)
        with mlflow.start_run():
            mlflow.sklearn.log_model(
                clf, artifact_path="model", registered_model_name="churn-model"
            )

        monkeypatch.setattr(evaluate, "TRACKING_URI", uri)
        monkeypatch.setattr(evaluate, "load_data", lambda: df)

        with pytest.raises(SystemExit) as exc:
            evaluate.main()

        assert exc.value.code == 0
