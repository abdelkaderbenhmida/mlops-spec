"""Tests for the credit risk evaluation gate."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))

import evaluate


class TestEvaluateGate:
    def test_compute_ks(self):
        import numpy as np
        y_true = [0, 0, 1, 1, 0, 1, 0, 1]
        y_prob = [0.1, 0.2, 0.7, 0.9, 0.3, 0.8, 0.15, 0.85]
        ks = evaluate.compute_ks(y_true, y_prob)
        assert 0.0 <= ks <= 1.0
        assert ks > 0.3  # good discrimination

    def test_auc_threshold_value(self):
        assert evaluate.AUC_THRESHOLD == 0.75
