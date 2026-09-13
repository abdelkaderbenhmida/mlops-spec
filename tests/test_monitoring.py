# TODO: high - Add alert rule for ingestion stalls
# TODO: medium - Implement dashboard for drift detection
# TODO: low - Add prediction distribution monitoring
"""Tests for the drift detector + retraining trigger (ml/monitoring/)."""
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ml"))

from monitoring import drift_detector, retraining_trigger


def _make_credit(tmp_path, n=200, seed=0):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "duration": rng.integers(4, 72, n),
            "credit_amount": rng.integers(200, 20000, n),
            "installment_rate": rng.integers(1, 5, n),
            "residence_since": rng.integers(1, 5, n),
            "age": rng.integers(18, 80, n),
            "existing_credits": rng.integers(1, 5, n),
            "num_dependents": rng.integers(0, 3, n),
            "target": rng.binomial(1, 0.7, n),
        }
    )
    path = tmp_path / "credit.csv"
    df.to_csv(path, index=False)
    return path


def test_no_drift_when_identical(tmp_path):
    ref = _make_credit(tmp_path, seed=1)
    det = drift_detector.detect_drift(ref, ref)
    assert det["drift_score"] == 0.0
    assert det["drift_detected"] is False


def test_drift_detected_on_shift(tmp_path):
    ref = _make_credit(tmp_path, seed=2)
    cur = pd.read_csv(_make_credit(tmp_path, seed=3))
    rng = np.random.default_rng(9)
    cur["credit_amount"] = cur["credit_amount"] * rng.normal(3.0, 0.5, size=len(cur))
    cur_path = tmp_path / "credit_shifted.csv"
    cur.to_csv(cur_path, index=False)
    det = drift_detector.detect_drift(ref, cur_path)
    assert det["drift_score"] > 0.0
    assert "credit_amount" in det["drifted_features"]


def test_trigger_fires_when_drifted(tmp_path):
    ref = _make_credit(tmp_path, seed=4)
    cur = pd.read_csv(ref)
    rng = np.random.default_rng(5)
    for col, mult, sd in [("credit_amount", 4.0, 0.6), ("age", 1.5, 0.4), ("duration", 2.0, 0.5)]:
        cur[col] = cur[col] * rng.normal(mult, sd, size=len(cur))
    cur_path = tmp_path / "credit_shifted2.csv"
    cur.to_csv(cur_path, index=False)
    det = drift_detector.detect_drift(ref, cur_path)

    report_path = drift_detector.REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(det))

    result = retraining_trigger.trigger_retraining(dry_run=True)
    assert result["triggered"] is True
    assert result["dry_run"] is True


def test_trigger_does_not_fire_without_drift(tmp_path):
    ref = _make_credit(tmp_path, seed=6)
    det = drift_detector.detect_drift(ref, ref)
    report_path = drift_detector.REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(det))
    result = retraining_trigger.trigger_retraining(dry_run=True)
    assert result["triggered"] is False
