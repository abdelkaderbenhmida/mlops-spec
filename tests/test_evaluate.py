# TODO: high - Add quality gate with thresholds
# TODO: medium - Implement comparison vs current production model
# TODO: low - Add metrics export for Evidence Pack
"""Tests for the credit risk evaluation gate."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))

import evaluate


class TestEvaluateGate:
    def test_auc_threshold_value(self):
        assert evaluate.AUC_THRESHOLD == 0.75

    def test_f1_threshold_value(self):
        assert evaluate.F1_THRESHOLD == 0.30