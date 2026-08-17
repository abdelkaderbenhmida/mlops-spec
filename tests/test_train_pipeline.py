"""Tests for the credit risk training pipeline."""
import sys
from pathlib import Path

import mlflow
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))

import train
import preprocess
from _data import build_subset_df


class TestTrain:
    def test_train_end_to_end(self, tmp_path, monkeypatch):
        """Full pipeline: train -> register -> save artifact."""
        mlruns = str(tmp_path / "mlruns")
        monkeypatch.setenv("MLFLOW_TRACKING_URI", f"file://{mlruns}")
        monkeypatch.setenv("MLFLOW_ALLOW_FILE_STORE", "true")

        # PATCH the module-level constant (already evaluated at import time)
        monkeypatch.setattr(train, "TRACKING_URI", f"file://{mlruns}")

        df = build_subset_df(500)
        monkeypatch.setattr(preprocess, "load_data", lambda: df)
        monkeypatch.setattr(train, "load_data", lambda: df)
        monkeypatch.setattr(train, "_REPO_ROOT", str(tmp_path))

        # Ensure ml/ subdir exists for model.pkl save
        (tmp_path / "ml").mkdir(exist_ok=True)

        train.main()

        model_pkl = tmp_path / "ml" / "model.pkl"
        assert model_pkl.exists()
        assert model_pkl.stat().st_size > 0

        client = mlflow.tracking.MlflowClient(f"file://{mlruns}")
        versions = client.get_latest_versions("credit-risk-model", stages=["Staging", "None"])
        assert versions, "credit-risk-model not registered"
        assert versions[0].name == "credit-risk-model"

        run = client.get_run(versions[0].run_id)
        assert "roc_auc" in run.data.metrics
        assert "ks" in run.data.metrics

    def test_compute_ks(self):
        import numpy as np
        y_true = [0, 0, 1, 1]
        y_prob = [0.1, 0.4, 0.6, 0.9]
        ks = train.compute_ks(y_true, y_prob)
        assert 0.0 <= ks <= 1.0

    def test_preprocess_encode_features(self):
        df = build_subset_df(100)
        X, y = preprocess.encode_features(df)
        assert len(X) == 100
        assert len(y) == 100
        assert set(y.unique()).issubset({0, 1})
