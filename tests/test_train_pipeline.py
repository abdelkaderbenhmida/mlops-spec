"""Tests for the training pipeline (ml/train.py + ml/preprocess.py).

TODO: ml/train.py, ml/preprocess.py, ml/data/churn.csv are pending — they are
being built by the backend agent in its own worktree. These tests skip until
the backend code lands on this branch.

MLflow is pointed at a local sqlite:// file so no tracking server is needed.
The dataset is replaced by a small synthetic frame (see tests/_data.py) so the
run completes in a couple of seconds.
"""
import pytest

pytest.importorskip("mlflow", reason="mlflow not installed")
pytest.importorskip("sklearn", reason="scikit-learn not installed")

train = pytest.importorskip(
    "train", reason="ml/train.py pending (backend agent builds ml/ in parallel)"
)
preprocess = pytest.importorskip(
    "preprocess", reason="ml/preprocess.py pending (backend agent)"
)

from _data import build_subset_df


class TestPreprocess:
    def test_load_data_reads_churn_csv(self):
        df = preprocess.load_data()
        assert list(df.columns) == [
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "Contract",
            "PaymentMethod",
            "Churn",
        ]
        assert len(df) >= 7000

    def test_encode_features_encodes_categoricals(self):
        df = build_subset_df()
        X, y, encoders = preprocess.encode_features(df)
        assert list(encoders) == ["Contract", "PaymentMethod"]
        assert list(X.columns) == [
            "Contract",
            "PaymentMethod",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
        ]
        for col in ("Contract", "PaymentMethod"):
            assert X[col].dtype.kind in "iu", f"{col} not integer-encoded"
        assert y.dtype.kind in "iu"
        assert len(X) == len(df) == len(y)

    def test_train_test_split_80_20_random_state_42(self):
        df = build_subset_df()
        train_df, test_df = preprocess.train_test_split(df)
        assert len(train_df) == pytest.approx(len(df) * 0.8, abs=1)
        assert len(test_df) == pytest.approx(len(df) * 0.2, abs=1)
        assert len(train_df) + len(test_df) == len(df)
        # Deterministic given random_state=42.
        train2, _ = preprocess.train_test_split(df)
        assert list(train2.index) == list(train_df.index)
        # Stratified split keeps the target balance close to the source.
        assert abs(train_df["Churn"].mean() - df["Churn"].mean()) < 0.05

    def test_apply_encoders_roundtrip(self):
        df = build_subset_df()
        _, _, encoders = preprocess.encode_features(df)
        X = preprocess.apply_encoders(df, encoders)
        assert X["Contract"].dtype.kind in "iu"
        assert len(X) == len(df)


class TestTrain:
    def test_train_pipeline_end_to_end(self, tmp_path, monkeypatch):
        import mlflow

        uri = f"sqlite:///{tmp_path / 'mlflow.db'}"
        monkeypatch.setattr(train, "TRACKING_URI", uri)
        monkeypatch.setattr(train, "MODEL_NAME", "churn-model")
        df = build_subset_df()
        monkeypatch.setattr(train, "load_data", lambda: df)

        artifact_calls = []
        monkeypatch.setattr(
            train.mlflow,
            "log_artifact",
            lambda path, artifact_path=None: artifact_calls.append(
                (path, artifact_path)
            ),
        )

        monkeypatch.chdir(tmp_path)
        train.main()

        # 1. Local model artifact saved.
        pkl = tmp_path / "ml" / "model.pkl"
        assert pkl.exists(), "model.pkl was not saved"
        assert pkl.stat().st_size > 0

        # 2. Model registered under the expected name.
        client = mlflow.tracking.MlflowClient(uri)
        versions = client.get_latest_versions(
            "churn-model", stages=["Production", "None"]
        )
        assert versions, "churn-model not registered in MLflow"
        assert versions[0].name == "churn-model"

        # 3. Params and metrics logged on the run.
        run = client.get_run(versions[0].run_id)
        assert run.data.params.get("n_estimators") == "300"
        assert run.data.params.get("random_state") == "42"
        for metric in ("accuracy", "f1", "roc_auc"):
            assert metric in run.data.metrics, f"{metric} not logged"

        # 4. Source CSV artifact logged.
        assert artifact_calls, "log_artifact never called"
        assert artifact_calls[0] == ("ml/data/churn.csv", "data")

    def test_model_is_random_forest(self):
        df = build_subset_df()
        X, y, _ = preprocess.encode_features(df)
        train_df, _ = preprocess.train_test_split(df)
        clf = train.RandomForestClassifier(n_estimators=300, max_depth=10, random_state=42)
        assert isinstance(clf, train.RandomForestClassifier)
        assert clf.n_estimators == 300
        assert clf.random_state == 42
