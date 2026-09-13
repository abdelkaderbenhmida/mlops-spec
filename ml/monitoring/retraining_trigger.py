# TODO: high - Add alert rule for ingestion stalls
# TODO: medium - Implement dashboard for drift detection
# TODO: low - Add prediction distribution monitoring
"""Drift-driven automatic retraining trigger for the credit risk pipeline.

Reads ml/data/monitoring/drift_report.json; when the drift score exceeds the
threshold it launches an automatic retrain (ml/train.py) followed by the
promotion-gate evaluation (ml/evaluate.py). Human sign-off still gates the
Staging -> Production promotion, so automation never bypasses approval.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = _REPO_ROOT / "ml" / "data" / "monitoring" / "drift_report.json"
DEFAULT_THRESHOLD = 0.3


def read_drift_report(path: Path = REPORT_PATH) -> dict:
    if not path.exists():
        return {"drift_score": 0.0, "threshold": DEFAULT_THRESHOLD, "drift_detected": False}
    return json.loads(path.read_text())


def should_retrain(report: dict, threshold: float | None = None) -> bool:
    score = float(report.get("drift_score", 0.0))
    thr = threshold if threshold is not None else float(
        os.environ.get("DRIFT_THRESHOLD", report.get("threshold", DEFAULT_THRESHOLD))
    )
    return score > thr


def trigger_retraining(dry_run: bool = False) -> dict:
    report = read_drift_report()
    score = float(report.get("drift_score", 0.0))
    threshold = float(report.get("threshold", DEFAULT_THRESHOLD))
    trigger = should_retrain(report)
    logger.info("Drift score=%.3f threshold=%.3f trigger=%s", score, threshold, trigger)

    if trigger and not dry_run:
        _launch_retraining()
    return {
        "drift_score": score,
        "threshold": threshold,
        "triggered": trigger,
        "dry_run": dry_run,
        "drifted_features": report.get("drifted_features", []),
    }


def _launch_retraining() -> None:
    for script in ["ml/train.py", "ml/evaluate.py"]:
        cmd = [sys.executable, script]
        logger.info("AUTOMATED_RETRAINING -> %s", " ".join(cmd))
        subprocess.run(cmd, cwd=_REPO_ROOT, check=False)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Drift-based retraining trigger")
    parser.add_argument("--dry-run", action="store_true", help="Only report, don't retrain")
    args = parser.parse_args()
    print(json.dumps(trigger_retraining(dry_run=args.dry_run), indent=2))


if __name__ == "__main__":
    main()
