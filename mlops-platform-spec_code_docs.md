# mlops-platform-spec: __init__.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/__init__.py`
- **Total lines:** 4
- **File size:** 183 bytes

## Line Type Summary
- **Code:** 1
- **Comment:** 0
- **Empty:** 0
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Tests for the credit risk MLOps platform."""`
> **Type:** Logical operation

## Summary
- **Total lines:** 4
- **Code lines:** 1
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 0

---
*Documentation generated for: mlops-platform-spec*
*File: __init__.py*
---

# mlops-platform-spec: conftest.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/conftest.py`
- **Total lines:** 27
- **File size:** 959 bytes

## Line Type Summary
- **Code:** 19
- **Comment:** 0
- **Empty:** 5
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Pytest bootstrap for the mlops-platform-spec repo.`
> **Type:** Arithmetic operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Adds the repo root, api/, and ml/ to sys.path so that production modul...`
> **Type:** Arithmetic operation

### Line   7
> **Code:** `can be imported both as packages (``import api.main``) and as top-leve...`
> **Type:** Arithmetic operation

### Line   8
> **Code:** `modules (``import db``, ``import train``, ``import preprocess``) the w...`
> **Type:** Logical operation

### Line   9
> **Code:** `backend code imports them.`
> **Type:** Logical operation

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `When run from the repo root, ``import api.main`` works because ``api/`...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `inserted first. ``ml/`` is inserted so that api/model.py, ml/train.py ...`
> **Type:** Arithmetic operation

### Line  13
> **Code:** `ml/evaluate.py can do ``from preprocess import ...``.`
> **Type:** Arithmetic operation

### Line  14
> **Code:** `"""`
> **Type:** Code statement

### Line  15
> **Code:** `import sys`
> **Type:** Imports a module

### Line  16
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `ROOT = Path(__file__).resolve().parents[1]`
> **Type:** Assignment/comparison

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `for subdir in ("api", "ml"):`
> **Type:** For loop

### Line  21
> **Code:** `path = str(ROOT / subdir)`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `if path not in sys.path:`
> **Type:** Conditional statement

### Line  23
> **Code:** `sys.path.insert(0, path)`
> **Type:** Function call

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `for path in (str(ROOT), str(ROOT / "tests")):`
> **Type:** For loop

### Line  26
> **Code:** `if path not in sys.path:`
> **Type:** Conditional statement

### Line  27
> **Code:** `sys.path.insert(0, path)`
> **Type:** Function call

## Summary
- **Total lines:** 27
- **Code lines:** 19
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 5

---
*Documentation generated for: mlops-platform-spec*
*File: conftest.py*
---

# mlops-platform-spec: test_train_pipeline.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/test_train_pipeline.py`
- **Total lines:** 56
- **File size:** 1983 bytes

## Line Type Summary
- **Code:** 40
- **Comment:** 0
- **Empty:** 13
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add data validation before training`
> **Type:** TODO: high - Add data validation before training

### Line   2
> **Code:** `# TODO: medium - Implement hyperparameter logging`
> **Type:** TODO: medium - Implement hyperparameter logging

### Line   3
> **Code:** `# TODO: low - Add model explainability integration`
> **Type:** TODO: low - Add model explainability integration

### Line   4
> **Code:** `"""Tests for the credit risk training pipeline."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line   9
> **Code:** `import pytest`
> **Type:** Imports a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))`
> **Type:** Arithmetic operation

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** `import train`
> **Type:** Imports a module

### Line  14
> **Code:** `import preprocess`
> **Type:** Imports a module

### Line  15
> **Code:** `from _data import build_subset_df`
> **Type:** Imports specific names from a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `class TestTrain:`
> **Type:** Class definition

### Line  19
> **Code:** `def test_train_end_to_end(self, tmp_path, monkeypatch):`
> **Type:** Function definition

### Line  20
> **Code:** `"""Full pipeline: train -> register -> save artifact."""`
> **Type:** Arithmetic operation

### Line  21
> **Code:** `mlruns = str(tmp_path / "mlruns")`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `monkeypatch.setenv("MLFLOW_TRACKING_URI", f"file://{mlruns}")`
> **Type:** Arithmetic operation

### Line  23
> **Code:** `monkeypatch.setenv("MLFLOW_ALLOW_FILE_STORE", "true")`
> **Type:** Function call

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `monkeypatch.setattr(train, "TRACKING_URI", f"file://{mlruns}")`
> **Type:** Arithmetic operation

### Line  26
> **Code:** ``
> **Type:** Empty line

### Line  27
> **Code:** `df = build_subset_df(500)`
> **Type:** Assignment/comparison

### Line  28
> **Code:** `monkeypatch.setattr(preprocess, "load_data", lambda: df)`
> **Type:** Function call

### Line  29
> **Code:** `monkeypatch.setattr(train, "load_data", lambda: df)`
> **Type:** Function call

### Line  30
> **Code:** `monkeypatch.setattr(train, "_REPO_ROOT", str(tmp_path))`
> **Type:** Function call

### Line  31
> **Code:** ``
> **Type:** Empty line

### Line  32
> **Code:** `(tmp_path / "ml").mkdir(exist_ok=True)`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `(tmp_path / "ml" / "data").mkdir(exist_ok=True)`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `(tmp_path / "ml" / "data" / "credit.csv").write_text("dummy\n")`
> **Type:** Arithmetic operation

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** `train.main()`
> **Type:** Function call

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `model_pkl = tmp_path / "ml" / "model.pkl"`
> **Type:** Assignment/comparison

### Line  39
> **Code:** `assert model_pkl.exists()`
> **Type:** Enforces a condition

### Line  40
> **Code:** `assert model_pkl.stat().st_size > 0`
> **Type:** Enforces a condition

### Line  41
> **Code:** ``
> **Type:** Empty line

### Line  42
> **Code:** `client = mlflow.tracking.MlflowClient(f"file://{mlruns}")`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `versions = client.get_latest_versions("credit-risk-model", stages=["St...`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `assert versions, "credit-risk-model not registered"`
> **Type:** Enforces a condition

### Line  45
> **Code:** `assert versions[0].name == "credit-risk-model"`
> **Type:** Enforces a condition

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `run = client.get_run(versions[0].run_id)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `assert "roc_auc" in run.data.metrics`
> **Type:** Enforces a condition

### Line  49
> **Code:** `assert "f1" in run.data.metrics`
> **Type:** Enforces a condition

### Line  50
> **Code:** ``
> **Type:** Empty line

### Line  51
> **Code:** `def test_preprocess_encode_features(self):`
> **Type:** Function definition

### Line  52
> **Code:** `df = build_subset_df(100)`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `X, y = preprocess.encode_features(df)`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `assert len(X) == 100`
> **Type:** Enforces a condition

### Line  55
> **Code:** `assert len(y) == 100`
> **Type:** Enforces a condition

### Line  56
> **Code:** `assert set(y).issubset({0, 1})`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 56
- **Code lines:** 40
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 13

---
*Documentation generated for: mlops-platform-spec*
*File: test_train_pipeline.py*
---

# mlops-platform-spec: test_monitoring.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/test_monitoring.py`
- **Total lines:** 83
- **File size:** 2954 bytes

## Line Type Summary
- **Code:** 65
- **Comment:** 0
- **Empty:** 15
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add alert rule for ingestion stalls`
> **Type:** TODO: high - Add alert rule for ingestion stalls

### Line   2
> **Code:** `# TODO: medium - Implement dashboard for drift detection`
> **Type:** TODO: medium - Implement dashboard for drift detection

### Line   3
> **Code:** `# TODO: low - Add prediction distribution monitoring`
> **Type:** TODO: low - Add prediction distribution monitoring

### Line   4
> **Code:** `"""Tests for the drift detector + retraining trigger (ml/monitoring/)....`
> **Type:** Arithmetic operation

### Line   5
> **Code:** `import json`
> **Type:** Imports a module

### Line   6
> **Code:** `import os`
> **Type:** Imports a module

### Line   7
> **Code:** `import sys`
> **Type:** Imports a module

### Line   8
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  11
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  12
> **Code:** `import pytest`
> **Type:** Imports a module

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ml"))`
> **Type:** Arithmetic operation

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `from monitoring import drift_detector, retraining_trigger`
> **Type:** Imports specific names from a module

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `def _make_credit(tmp_path, n=200, seed=0):`
> **Type:** Function definition

### Line  20
> **Code:** `rng = np.random.default_rng(seed)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `df = pd.DataFrame(`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `{`
> **Type:** Data structure operation

### Line  23
> **Code:** `"duration": rng.integers(4, 72, n),`
> **Type:** Code statement

### Line  24
> **Code:** `"credit_amount": rng.integers(200, 20000, n),`
> **Type:** Code statement

### Line  25
> **Code:** `"installment_rate": rng.integers(1, 5, n),`
> **Type:** Code statement

### Line  26
> **Code:** `"residence_since": rng.integers(1, 5, n),`
> **Type:** Code statement

### Line  27
> **Code:** `"age": rng.integers(18, 80, n),`
> **Type:** Code statement

### Line  28
> **Code:** `"existing_credits": rng.integers(1, 5, n),`
> **Type:** Code statement

### Line  29
> **Code:** `"num_dependents": rng.integers(0, 3, n),`
> **Type:** Code statement

### Line  30
> **Code:** `"target": rng.binomial(1, 0.7, n),`
> **Type:** Code statement

### Line  31
> **Code:** `}`
> **Type:** Code statement

### Line  32
> **Code:** `)`
> **Type:** Code statement

### Line  33
> **Code:** `path = tmp_path / "credit.csv"`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `df.to_csv(path, index=False)`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `return path`
> **Type:** Returns a value from a function

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `def test_no_drift_when_identical(tmp_path):`
> **Type:** Function definition

### Line  39
> **Code:** `ref = _make_credit(tmp_path, seed=1)`
> **Type:** Assignment/comparison

### Line  40
> **Code:** `det = drift_detector.detect_drift(ref, ref)`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `assert det["drift_score"] == 0.0`
> **Type:** Enforces a condition

### Line  42
> **Code:** `assert det["drift_detected"] is False`
> **Type:** Enforces a condition

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** `def test_drift_detected_on_shift(tmp_path):`
> **Type:** Function definition

### Line  46
> **Code:** `ref = _make_credit(tmp_path, seed=2)`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `cur = pd.read_csv(_make_credit(tmp_path, seed=3))`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `rng = np.random.default_rng(9)`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `cur["credit_amount"] = cur["credit_amount"] * rng.normal(3.0, 0.5, siz...`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `cur_path = tmp_path / "credit_shifted.csv"`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `cur.to_csv(cur_path, index=False)`
> **Type:** Assignment/comparison

### Line  52
> **Code:** `det = drift_detector.detect_drift(ref, cur_path)`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `assert det["drift_score"] > 0.0`
> **Type:** Enforces a condition

### Line  54
> **Code:** `assert "credit_amount" in det["drifted_features"]`
> **Type:** Enforces a condition

### Line  55
> **Code:** ``
> **Type:** Empty line

### Line  56
> **Code:** ``
> **Type:** Empty line

### Line  57
> **Code:** `def test_trigger_fires_when_drifted(tmp_path):`
> **Type:** Function definition

### Line  58
> **Code:** `ref = _make_credit(tmp_path, seed=4)`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `cur = pd.read_csv(ref)`
> **Type:** Assignment/comparison

### Line  60
> **Code:** `rng = np.random.default_rng(5)`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `for col, mult, sd in [("credit_amount", 4.0, 0.6), ("age", 1.5, 0.4), ...`
> **Type:** For loop

### Line  62
> **Code:** `cur[col] = cur[col] * rng.normal(mult, sd, size=len(cur))`
> **Type:** Assignment/comparison

### Line  63
> **Code:** `cur_path = tmp_path / "credit_shifted2.csv"`
> **Type:** Assignment/comparison

### Line  64
> **Code:** `cur.to_csv(cur_path, index=False)`
> **Type:** Assignment/comparison

### Line  65
> **Code:** `det = drift_detector.detect_drift(ref, cur_path)`
> **Type:** Assignment/comparison

### Line  66
> **Code:** ``
> **Type:** Empty line

### Line  67
> **Code:** `report_path = drift_detector.REPORT_PATH`
> **Type:** Assignment/comparison

### Line  68
> **Code:** `report_path.parent.mkdir(parents=True, exist_ok=True)`
> **Type:** Assignment/comparison

### Line  69
> **Code:** `report_path.write_text(json.dumps(det))`
> **Type:** Logical operation

### Line  70
> **Code:** ``
> **Type:** Empty line

### Line  71
> **Code:** `result = retraining_trigger.trigger_retraining(dry_run=True)`
> **Type:** Assignment/comparison

### Line  72
> **Code:** `assert result["triggered"] is True`
> **Type:** Enforces a condition

### Line  73
> **Code:** `assert result["dry_run"] is True`
> **Type:** Enforces a condition

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** ``
> **Type:** Empty line

### Line  76
> **Code:** `def test_trigger_does_not_fire_without_drift(tmp_path):`
> **Type:** Function definition

### Line  77
> **Code:** `ref = _make_credit(tmp_path, seed=6)`
> **Type:** Assignment/comparison

### Line  78
> **Code:** `det = drift_detector.detect_drift(ref, ref)`
> **Type:** Assignment/comparison

### Line  79
> **Code:** `report_path = drift_detector.REPORT_PATH`
> **Type:** Assignment/comparison

### Line  80
> **Code:** `report_path.parent.mkdir(parents=True, exist_ok=True)`
> **Type:** Assignment/comparison

### Line  81
> **Code:** `report_path.write_text(json.dumps(det))`
> **Type:** Logical operation

### Line  82
> **Code:** `result = retraining_trigger.trigger_retraining(dry_run=True)`
> **Type:** Assignment/comparison

### Line  83
> **Code:** `assert result["triggered"] is False`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 83
- **Code lines:** 65
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 15

---
*Documentation generated for: mlops-platform-spec*
*File: test_monitoring.py*
---

# mlops-platform-spec: test_evaluate.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/test_evaluate.py`
- **Total lines:** 20
- **File size:** 550 bytes

## Line Type Summary
- **Code:** 11
- **Comment:** 0
- **Empty:** 6
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add quality gate with thresholds`
> **Type:** TODO: high - Add quality gate with thresholds

### Line   2
> **Code:** `# TODO: medium - Implement comparison vs current production model`
> **Type:** TODO: medium - Implement comparison vs current production model

### Line   3
> **Code:** `# TODO: low - Add metrics export for Evidence Pack`
> **Type:** TODO: low - Add metrics export for Evidence Pack

### Line   4
> **Code:** `"""Tests for the credit risk evaluation gate."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))`
> **Type:** Arithmetic operation

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `import evaluate`
> **Type:** Imports a module

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** ``
> **Type:** Empty line

### Line  15
> **Code:** `class TestEvaluateGate:`
> **Type:** Class definition

### Line  16
> **Code:** `def test_auc_threshold_value(self):`
> **Type:** Function definition

### Line  17
> **Code:** `assert evaluate.AUC_THRESHOLD == 0.75`
> **Type:** Enforces a condition

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `def test_f1_threshold_value(self):`
> **Type:** Function definition

### Line  20
> **Code:** `assert evaluate.F1_THRESHOLD == 0.30`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 20
- **Code lines:** 11
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 6

---
*Documentation generated for: mlops-platform-spec*
*File: test_evaluate.py*
---

# mlops-platform-spec: test_schemas.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/test_schemas.py`
- **Total lines:** 73
- **File size:** 2163 bytes

## Line Type Summary
- **Code:** 56
- **Comment:** 0
- **Empty:** 14
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Tests for the credit risk API schemas (German Credit Data)."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** `from pydantic import ValidationError`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api")...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** `from schemas import PredictRequest, PredictResponse, HealthResponse`
> **Type:** Imports specific names from a module

### Line  14
> **Code:** ``
> **Type:** Empty line

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `def valid_kwargs(**overrides):`
> **Type:** Function definition

### Line  17
> **Code:** `base = {`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `"checking_status": "A12",`
> **Type:** Code statement

### Line  19
> **Code:** `"duration": 24,`
> **Type:** Code statement

### Line  20
> **Code:** `"credit_history": "A34",`
> **Type:** Logical operation

### Line  21
> **Code:** `"purpose": "A43",`
> **Type:** Code statement

### Line  22
> **Code:** `"credit_amount": 4000,`
> **Type:** Code statement

### Line  23
> **Code:** `"savings_status": "A61",`
> **Type:** Code statement

### Line  24
> **Code:** `"employment": "A73",`
> **Type:** Code statement

### Line  25
> **Code:** `"installment_rate": 3,`
> **Type:** Code statement

### Line  26
> **Code:** `"personal_status": "A93",`
> **Type:** Code statement

### Line  27
> **Code:** `"other_parties": "A101",`
> **Type:** Code statement

### Line  28
> **Code:** `"residence_since": 4,`
> **Type:** Code statement

### Line  29
> **Code:** `"property_magnitude": "A121",`
> **Type:** Code statement

### Line  30
> **Code:** `"age": 35,`
> **Type:** Code statement

### Line  31
> **Code:** `"other_payment_plans": "A143",`
> **Type:** Code statement

### Line  32
> **Code:** `"housing": "A152",`
> **Type:** Code statement

### Line  33
> **Code:** `"existing_credits": 2,`
> **Type:** Code statement

### Line  34
> **Code:** `"job": "A173",`
> **Type:** Code statement

### Line  35
> **Code:** `"num_dependents": 1,`
> **Type:** Code statement

### Line  36
> **Code:** `"own_telephone": "A192",`
> **Type:** Code statement

### Line  37
> **Code:** `"foreign_worker": "A201",`
> **Type:** Logical operation

### Line  38
> **Code:** `}`
> **Type:** Code statement

### Line  39
> **Code:** `base.update(overrides)`
> **Type:** Function call

### Line  40
> **Code:** `return base`
> **Type:** Returns a value from a function

### Line  41
> **Code:** ``
> **Type:** Empty line

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `class TestPredictRequest:`
> **Type:** Class definition

### Line  44
> **Code:** `def test_valid_request(self):`
> **Type:** Function definition

### Line  45
> **Code:** `r = PredictRequest(**valid_kwargs())`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `assert r.age == 35`
> **Type:** Enforces a condition

### Line  47
> **Code:** `assert r.checking_status == "A12"`
> **Type:** Enforces a condition

### Line  48
> **Code:** `assert r.credit_amount == 4000`
> **Type:** Enforces a condition

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** `def test_rejects_unknown_checking_status(self):`
> **Type:** Function definition

### Line  51
> **Code:** `with pytest.raises(ValidationError):`
> **Type:** Context manager

### Line  52
> **Code:** `PredictRequest(**valid_kwargs(checking_status="A99"))`
> **Type:** Assignment/comparison

### Line  53
> **Code:** ``
> **Type:** Empty line

### Line  54
> **Code:** `def test_rejects_duration_out_of_range(self):`
> **Type:** Function definition

### Line  55
> **Code:** `with pytest.raises(ValidationError):`
> **Type:** Context manager

### Line  56
> **Code:** `PredictRequest(**valid_kwargs(duration=0))`
> **Type:** Assignment/comparison

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `def test_rejects_negative_credit_amount(self):`
> **Type:** Function definition

### Line  59
> **Code:** `with pytest.raises(ValidationError):`
> **Type:** Context manager

### Line  60
> **Code:** `PredictRequest(**valid_kwargs(credit_amount=-100))`
> **Type:** Assignment/comparison

### Line  61
> **Code:** ``
> **Type:** Empty line

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** `class TestPredictResponse:`
> **Type:** Class definition

### Line  64
> **Code:** `def test_valid_response(self):`
> **Type:** Function definition

### Line  65
> **Code:** `r = PredictResponse(prediction=1, probability=0.75, risk_tier="high")`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `assert r.prediction == 1`
> **Type:** Enforces a condition

### Line  67
> **Code:** `assert r.risk_tier == "high"`
> **Type:** Enforces a condition

### Line  68
> **Code:** ``
> **Type:** Empty line

### Line  69
> **Code:** ``
> **Type:** Empty line

### Line  70
> **Code:** `class TestHealthResponse:`
> **Type:** Class definition

### Line  71
> **Code:** `def test_default_status(self):`
> **Type:** Function definition

### Line  72
> **Code:** `h = HealthResponse()`
> **Type:** Assignment/comparison

### Line  73
> **Code:** `assert h.status == "ok"`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 73
- **Code lines:** 56
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 14

---
*Documentation generated for: mlops-platform-spec*
*File: test_schemas.py*
---

# mlops-platform-spec: test_api.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/test_api.py`
- **Total lines:** 127
- **File size:** 4321 bytes

## Line Type Summary
- **Code:** 105
- **Comment:** 0
- **Empty:** 19
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Tests for the credit risk prediction API."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** `from fastapi.testclient import TestClient`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api")...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests...`
> **Type:** Arithmetic operation

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `import main`
> **Type:** Imports a module

### Line  15
> **Code:** `from _data import build_subset_df`
> **Type:** Imports specific names from a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `from sklearn.ensemble import GradientBoostingClassifier`
> **Type:** Imports specific names from a module

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `import preprocess`
> **Type:** Imports a module

### Line  20
> **Code:** ``
> **Type:** Empty line

### Line  21
> **Code:** `VALID_PAYLOAD = {`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `"checking_status": "A12",`
> **Type:** Code statement

### Line  23
> **Code:** `"duration": 24,`
> **Type:** Code statement

### Line  24
> **Code:** `"credit_history": "A34",`
> **Type:** Logical operation

### Line  25
> **Code:** `"purpose": "A43",`
> **Type:** Code statement

### Line  26
> **Code:** `"credit_amount": 4000,`
> **Type:** Code statement

### Line  27
> **Code:** `"savings_status": "A61",`
> **Type:** Code statement

### Line  28
> **Code:** `"employment": "A73",`
> **Type:** Code statement

### Line  29
> **Code:** `"installment_rate": 3,`
> **Type:** Code statement

### Line  30
> **Code:** `"personal_status": "A93",`
> **Type:** Code statement

### Line  31
> **Code:** `"other_parties": "A101",`
> **Type:** Code statement

### Line  32
> **Code:** `"residence_since": 4,`
> **Type:** Code statement

### Line  33
> **Code:** `"property_magnitude": "A121",`
> **Type:** Code statement

### Line  34
> **Code:** `"age": 35,`
> **Type:** Code statement

### Line  35
> **Code:** `"other_payment_plans": "A143",`
> **Type:** Code statement

### Line  36
> **Code:** `"housing": "A152",`
> **Type:** Code statement

### Line  37
> **Code:** `"existing_credits": 2,`
> **Type:** Code statement

### Line  38
> **Code:** `"job": "A173",`
> **Type:** Code statement

### Line  39
> **Code:** `"num_dependents": 1,`
> **Type:** Code statement

### Line  40
> **Code:** `"own_telephone": "A192",`
> **Type:** Code statement

### Line  41
> **Code:** `"foreign_worker": "A201",`
> **Type:** Logical operation

### Line  42
> **Code:** `}`
> **Type:** Code statement

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** `def install_trained_model(monkeypatch, n_rows: int = 300, n_estimators...`
> **Type:** Function definition

### Line  46
> **Code:** `"""Fit a tiny model and make the app serve it instead of training at s...`
> **Type:** Logical operation

### Line  47
> **Code:** `df = build_subset_df(n_rows)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `X, y = preprocess.encode_features(df)`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `clf = GradientBoostingClassifier(n_estimators=n_estimators, random_sta...`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `clf.fit(X, y)`
> **Type:** Function call

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `def fake_train():`
> **Type:** Function definition

### Line  53
> **Code:** `main.MODEL = clf`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `main.FEATURE_NAMES = preprocess.get_feature_names()`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `main.MODEL_METRICS.update({`
> **Type:** Code statement

### Line  56
> **Code:** `"model_name": type(clf).__name__,`
> **Type:** Code statement

### Line  57
> **Code:** `"n_estimators": clf.n_estimators,`
> **Type:** Logical operation

### Line  58
> **Code:** `"max_depth": clf.max_depth,`
> **Type:** Code statement

### Line  59
> **Code:** `"auc": 0.85,`
> **Type:** Code statement

### Line  60
> **Code:** `"f1": 0.62,`
> **Type:** Code statement

### Line  61
> **Code:** `})`
> **Type:** Code statement

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** `monkeypatch.setattr(main, "train_model", fake_train)`
> **Type:** Function call

### Line  64
> **Code:** ``
> **Type:** Empty line

### Line  65
> **Code:** ``
> **Type:** Empty line

### Line  66
> **Code:** `class TestHealth:`
> **Type:** Class definition

### Line  67
> **Code:** `def test_health_ok(self, monkeypatch):`
> **Type:** Function definition

### Line  68
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line  69
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line  70
> **Code:** `r = c.get("/health")`
> **Type:** Assignment/comparison

### Line  71
> **Code:** `assert r.status_code == 200`
> **Type:** Enforces a condition

### Line  72
> **Code:** `body = r.json()`
> **Type:** Assignment/comparison

### Line  73
> **Code:** `assert body["status"] == "ok"`
> **Type:** Enforces a condition

### Line  74
> **Code:** `assert body["model_loaded"] is True`
> **Type:** Enforces a condition

### Line  75
> **Code:** `assert body["model_version"] == "1.0"`
> **Type:** Enforces a condition

### Line  76
> **Code:** ``
> **Type:** Empty line

### Line  77
> **Code:** ``
> **Type:** Empty line

### Line  78
> **Code:** `class TestPredict:`
> **Type:** Class definition

### Line  79
> **Code:** `def test_predict_returns_200_with_valid_payload(self, monkeypatch):`
> **Type:** Function definition

### Line  80
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line  81
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line  82
> **Code:** `r = c.post("/predict", json=VALID_PAYLOAD)`
> **Type:** Assignment/comparison

### Line  83
> **Code:** `assert r.status_code == 200`
> **Type:** Enforces a condition

### Line  84
> **Code:** `body = r.json()`
> **Type:** Assignment/comparison

### Line  85
> **Code:** `assert body["prediction"] in (0, 1)`
> **Type:** Enforces a condition

### Line  86
> **Code:** `assert isinstance(body["probability"], float)`
> **Type:** Enforces a condition

### Line  87
> **Code:** `assert 0.0 <= body["probability"] <= 1.0`
> **Type:** Enforces a condition

### Line  88
> **Code:** `assert body["risk_tier"] in ("low", "medium", "high", "critical")`
> **Type:** Enforces a condition

### Line  89
> **Code:** ``
> **Type:** Empty line

### Line  90
> **Code:** `def test_predict_422_on_missing_fields(self, monkeypatch):`
> **Type:** Function definition

### Line  91
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line  92
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line  93
> **Code:** `r = c.post("/predict", json={"age": 35})`
> **Type:** Assignment/comparison

### Line  94
> **Code:** `assert r.status_code == 422`
> **Type:** Enforces a condition

### Line  95
> **Code:** ``
> **Type:** Empty line

### Line  96
> **Code:** `def test_predict_422_on_unknown_category(self, monkeypatch):`
> **Type:** Function definition

### Line  97
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line  98
> **Code:** `payload = dict(VALID_PAYLOAD)`
> **Type:** Assignment/comparison

### Line  99
> **Code:** `payload["checking_status"] = "A99"`
> **Type:** Assignment/comparison

### Line 100
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line 101
> **Code:** `r = c.post("/predict", json=payload)`
> **Type:** Assignment/comparison

### Line 102
> **Code:** `assert r.status_code == 422`
> **Type:** Enforces a condition

### Line 103
> **Code:** ``
> **Type:** Empty line

### Line 104
> **Code:** ``
> **Type:** Empty line

### Line 105
> **Code:** `class TestHistoryStats:`
> **Type:** Class definition

### Line 106
> **Code:** `def test_history_and_stats_record_predictions(self, monkeypatch):`
> **Type:** Function definition

### Line 107
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line 108
> **Code:** `main.PREDICTIONS.clear()`
> **Type:** Function call

### Line 109
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line 110
> **Code:** `r = c.post("/predict", json=VALID_PAYLOAD)`
> **Type:** Assignment/comparison

### Line 111
> **Code:** `assert r.status_code == 200`
> **Type:** Enforces a condition

### Line 112
> **Code:** `hist = c.get("/history").json()`
> **Type:** Assignment/comparison

### Line 113
> **Code:** `stats = c.get("/stats").json()`
> **Type:** Assignment/comparison

### Line 114
> **Code:** `assert hist["total"] == 1`
> **Type:** Enforces a condition

### Line 115
> **Code:** `assert hist["items"][0]["prediction"] == r.json()["prediction"]`
> **Type:** Enforces a condition

### Line 116
> **Code:** `assert stats["total_predictions"] == 1`
> **Type:** Enforces a condition

### Line 117
> **Code:** `assert stats["risk_tier_distribution"] == {`
> **Type:** Enforces a condition

### Line 118
> **Code:** `"low": 0, "medium": 0, "high": 0, "critical": 0`
> **Type:** Code statement

### Line 119
> **Code:** `} or sum(stats["risk_tier_distribution"].values()) == 1`
> **Type:** Assignment/comparison

### Line 120
> **Code:** ``
> **Type:** Empty line

### Line 121
> **Code:** `def test_model_info(self, monkeypatch):`
> **Type:** Function definition

### Line 122
> **Code:** `install_trained_model(monkeypatch)`
> **Type:** Function call

### Line 123
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line 124
> **Code:** `info = c.get("/model-info").json()`
> **Type:** Assignment/comparison

### Line 125
> **Code:** `assert info["model_name"] == "GradientBoostingClassifier"`
> **Type:** Enforces a condition

### Line 126
> **Code:** `assert "auc" in info["metrics"]`
> **Type:** Enforces a condition

### Line 127
> **Code:** `assert len(info["feature_importance"]) > 0`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 127
- **Code lines:** 105
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 19

---
*Documentation generated for: mlops-platform-spec*
*File: test_api.py*
---

# mlops-platform-spec: _data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/tests/_data.py`
- **Total lines:** 74
- **File size:** 2970 bytes

## Line Type Summary
- **Code:** 64
- **Comment:** 0
- **Empty:** 7
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Shared test data for the credit risk ML pipeline (German Credit Dat...`
> **Type:** Logical operation

### Line   5
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line   6
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `RNG = np.random.default_rng(99)`
> **Type:** Assignment/comparison

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `CHECKING_STATUS = ["A11", "A12", "A13", "A14"]`
> **Type:** Assignment/comparison

### Line  11
> **Code:** `CREDIT_HISTORY = ["A30", "A31", "A32", "A33", "A34"]`
> **Type:** Assignment/comparison

### Line  12
> **Code:** `PURPOSE = ["A40", "A41", "A42", "A43", "A44", "A45", "A46", "A47", "A4...`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `SAVINGS_STATUS = ["A61", "A62", "A63", "A64", "A65"]`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `EMPLOYMENT = ["A71", "A72", "A73", "A74", "A75"]`
> **Type:** Assignment/comparison

### Line  15
> **Code:** `PERSONAL_STATUS = ["A91", "A92", "A93", "A94", "A95"]`
> **Type:** Assignment/comparison

### Line  16
> **Code:** `OTHER_PARTIES = ["A101", "A102", "A103"]`
> **Type:** Assignment/comparison

### Line  17
> **Code:** `PROPERTY_MAGNITUDE = ["A121", "A122", "A123", "A124"]`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `OTHER_PAYMENT_PLANS = ["A141", "A142", "A143"]`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `HOUSING = ["A151", "A152", "A153"]`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `JOB = ["A171", "A172", "A173", "A174"]`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `OWN_TELEPHONE = ["A191", "A192"]`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `FOREIGN_WORKER = ["A201", "A202"]`
> **Type:** Assignment/comparison

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `def build_subset_df(n: int = 500) -> pd.DataFrame:`
> **Type:** Function definition

### Line  26
> **Code:** `"""Build a small synthetic German Credit Data dataframe for tests."""`
> **Type:** Logical operation

### Line  27
> **Code:** `rows = []`
> **Type:** Assignment/comparison

### Line  28
> **Code:** `for _ in range(n):`
> **Type:** For loop

### Line  29
> **Code:** `age = int(RNG.integers(18, 76))`
> **Type:** Assignment/comparison

### Line  30
> **Code:** `duration = int(RNG.integers(1, 73))`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `credit_amount = int(RNG.integers(250, 20001))`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `checking_status = RNG.choice(CHECKING_STATUS)`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `credit_history = RNG.choice(CREDIT_HISTORY)`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `savings_status = RNG.choice(SAVINGS_STATUS)`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `purpose = RNG.choice(PURPOSE)`
> **Type:** Assignment/comparison

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** `logit = (`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `-1.8`
> **Type:** Arithmetic operation

### Line  39
> **Code:** `+ 1.2 * (credit_history == "A34")`
> **Type:** Assignment/comparison

### Line  40
> **Code:** `+ 0.7 * (credit_history == "A33")`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `+ 0.6 * (checking_status in ("A11", "A12"))`
> **Type:** Arithmetic operation

### Line  42
> **Code:** `- 0.5 * (savings_status in ("A64", "A65"))`
> **Type:** Arithmetic operation

### Line  43
> **Code:** `+ 0.02 * (duration - 36) / 10`
> **Type:** Arithmetic operation

### Line  44
> **Code:** `- 0.03 * (age - 40) / 10`
> **Type:** Arithmetic operation

### Line  45
> **Code:** `- 0.2 * np.log1p(credit_amount / 1000)`
> **Type:** Arithmetic operation

### Line  46
> **Code:** `)`
> **Type:** Code statement

### Line  47
> **Code:** `p_default = 1 / (1 + np.exp(-logit))`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `target = int(RNG.random() < p_default)`
> **Type:** Assignment/comparison

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** `rows.append({`
> **Type:** Code statement

### Line  51
> **Code:** `"checking_status": checking_status,`
> **Type:** Code statement

### Line  52
> **Code:** `"duration": duration,`
> **Type:** Code statement

### Line  53
> **Code:** `"credit_history": credit_history,`
> **Type:** Logical operation

### Line  54
> **Code:** `"purpose": purpose,`
> **Type:** Code statement

### Line  55
> **Code:** `"credit_amount": credit_amount,`
> **Type:** Code statement

### Line  56
> **Code:** `"savings_status": savings_status,`
> **Type:** Code statement

### Line  57
> **Code:** `"employment": RNG.choice(EMPLOYMENT),`
> **Type:** Code statement

### Line  58
> **Code:** `"installment_rate": int(RNG.integers(1, 5)),`
> **Type:** Code statement

### Line  59
> **Code:** `"personal_status": RNG.choice(PERSONAL_STATUS),`
> **Type:** Code statement

### Line  60
> **Code:** `"other_parties": RNG.choice(OTHER_PARTIES),`
> **Type:** Code statement

### Line  61
> **Code:** `"residence_since": int(RNG.integers(1, 5)),`
> **Type:** Code statement

### Line  62
> **Code:** `"property_magnitude": RNG.choice(PROPERTY_MAGNITUDE),`
> **Type:** Code statement

### Line  63
> **Code:** `"age": age,`
> **Type:** Code statement

### Line  64
> **Code:** `"other_payment_plans": RNG.choice(OTHER_PAYMENT_PLANS),`
> **Type:** Code statement

### Line  65
> **Code:** `"housing": RNG.choice(HOUSING),`
> **Type:** Code statement

### Line  66
> **Code:** `"existing_credits": int(RNG.integers(1, 5)),`
> **Type:** Code statement

### Line  67
> **Code:** `"job": RNG.choice(JOB),`
> **Type:** Code statement

### Line  68
> **Code:** `"num_dependents": int(RNG.integers(1, 3)),`
> **Type:** Code statement

### Line  69
> **Code:** `"own_telephone": RNG.choice(OWN_TELEPHONE),`
> **Type:** Code statement

### Line  70
> **Code:** `"foreign_worker": RNG.choice(FOREIGN_WORKER),`
> **Type:** Logical operation

### Line  71
> **Code:** `"target": target,`
> **Type:** Code statement

### Line  72
> **Code:** `})`
> **Type:** Code statement

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** `return pd.DataFrame(rows)`
> **Type:** Returns a value from a function

## Summary
- **Total lines:** 74
- **Code lines:** 64
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 7

---
*Documentation generated for: mlops-platform-spec*
*File: _data.py*
---

# mlops-platform-spec: __init__.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/api/__init__.py`
- **Total lines:** 4
- **File size:** 201 bytes

## Line Type Summary
- **Code:** 1
- **Comment:** 0
- **Empty:** 0
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Credit risk API — FastAPI service for real-time prediction."""`
> **Type:** Arithmetic operation

## Summary
- **Total lines:** 4
- **Code lines:** 1
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 0

---
*Documentation generated for: mlops-platform-spec*
*File: __init__.py*
---

# mlops-platform-spec: db.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/api/db.py`
- **Total lines:** 52
- **File size:** 1819 bytes

## Line Type Summary
- **Code:** 36
- **Comment:** 0
- **Empty:** 13
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Database configuration and models for the credit risk prediction AP...`
> **Type:** Logical operation

### Line   5
> **Code:** `import os`
> **Type:** Imports a module

### Line   6
> **Code:** `from datetime import datetime`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `from sqlalchemy import JSON, DateTime, Integer, String, create_engine,...`
> **Type:** Imports specific names from a module

### Line   9
> **Code:** `from sqlalchemy.orm import declarative_base, sessionmaker`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `Base = declarative_base()`
> **Type:** Assignment/comparison

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `class Prediction(Base):`
> **Type:** Class definition

### Line  15
> **Code:** `__tablename__ = "predictions"`
> **Type:** Assignment/comparison

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `id = Column(Integer, primary_key=True, index=True)`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `input_json = Column(JSON, nullable=False)`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `prediction = Column(Integer, nullable=False)`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `probability = Column(String(20), nullable=False)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `created_at = Column(DateTime, default=datetime.utcnow, nullable=False)`
> **Type:** Assignment/comparison

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `def get_database_url() -> str:`
> **Type:** Function definition

### Line  25
> **Code:** `"""Construct database URL from environment variables."""`
> **Type:** Code statement

### Line  26
> **Code:** `sqlite_path = os.environ.get("SQLITE_DB", os.path.join(os.path.dirname...`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `if os.environ.get("DB_HOST"):`
> **Type:** Conditional statement

### Line  28
> **Code:** `host = os.environ["DB_HOST"]`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `port = os.environ.get("DB_PORT", "5432")`
> **Type:** Assignment/comparison

### Line  30
> **Code:** `user = os.environ.get("DB_USER", "postgres")`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `password = os.environ.get("DB_PASSWORD", "postgres")`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `database = os.environ.get("DB_NAME", "mlops")`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `return f"postgresql://{user}:{password}@{host}:{port}/{database}"`
> **Type:** Returns a value from a function

### Line  34
> **Code:** `return f"sqlite:///{sqlite_path}"`
> **Type:** Returns a value from a function

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** `def get_engine():`
> **Type:** Function definition

### Line  38
> **Code:** `"""Create and return SQLAlchemy engine."""`
> **Type:** Logical operation

### Line  39
> **Code:** `return create_engine(get_database_url(), pool_pre_ping=True)`
> **Type:** Returns a value from a function

### Line  40
> **Code:** ``
> **Type:** Empty line

### Line  41
> **Code:** ``
> **Type:** Empty line

### Line  42
> **Code:** `def get_session():`
> **Type:** Function definition

### Line  43
> **Code:** `"""Create and return a database session."""`
> **Type:** Logical operation

### Line  44
> **Code:** `engine = get_engine()`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=en...`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `return SessionLocal()`
> **Type:** Returns a value from a function

### Line  47
> **Code:** ``
> **Type:** Empty line

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `def init_db():`
> **Type:** Function definition

### Line  50
> **Code:** `"""Initialize the database tables."""`
> **Type:** Code statement

### Line  51
> **Code:** `engine = get_engine()`
> **Type:** Assignment/comparison

### Line  52
> **Code:** `Base.metadata.create_all(bind=engine)`
> **Type:** Assignment/comparison

## Summary
- **Total lines:** 52
- **Code lines:** 36
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 13

---
*Documentation generated for: mlops-platform-spec*
*File: db.py*
---

# mlops-platform-spec: schemas.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/api/schemas.py`
- **Total lines:** 119
- **File size:** 4282 bytes

## Line Type Summary
- **Code:** 103
- **Comment:** 0
- **Empty:** 13
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Pydantic schemas for the credit risk prediction API (German Credit ...`
> **Type:** Logical operation

### Line   5
> **Code:** `from pydantic import BaseModel, Field`
> **Type:** Imports specific names from a module

### Line   6
> **Code:** `from typing import Literal`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** ``
> **Type:** Empty line

### Line   9
> **Code:** `class PredictRequest(BaseModel):`
> **Type:** Class definition

### Line  10
> **Code:** `checking_status: Literal[`
> **Type:** Code statement

### Line  11
> **Code:** `"A11", "A12", "A13", "A14"`
> **Type:** Code statement

### Line  12
> **Code:** `] = Field(..., description="Status of existing checking account")`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `duration: int = Field(..., ge=1, le=72, description="Duration in month...`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `credit_history: Literal[`
> **Type:** Logical operation

### Line  15
> **Code:** `"A30", "A31", "A32", "A33", "A34"`
> **Type:** Code statement

### Line  16
> **Code:** `] = Field(..., description="Credit history")`
> **Type:** Assignment/comparison

### Line  17
> **Code:** `purpose: Literal[`
> **Type:** Code statement

### Line  18
> **Code:** `"A40", "A41", "A42", "A43", "A44", "A45", "A46", "A47", "A48", "A49", ...`
> **Type:** Code statement

### Line  19
> **Code:** `] = Field(..., description="Credit purpose")`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `credit_amount: int = Field(..., ge=250, le=20000, description="Credit ...`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `savings_status: Literal[`
> **Type:** Code statement

### Line  22
> **Code:** `"A61", "A62", "A63", "A64", "A65"`
> **Type:** Code statement

### Line  23
> **Code:** `] = Field(..., description="Savings account/bonds")`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `employment: Literal[`
> **Type:** Code statement

### Line  25
> **Code:** `"A71", "A72", "A73", "A74", "A75"`
> **Type:** Code statement

### Line  26
> **Code:** `] = Field(..., description="Present employment since")`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `installment_rate: int = Field(..., ge=1, le=4, description="Installmen...`
> **Type:** Assignment/comparison

### Line  28
> **Code:** `personal_status: Literal[`
> **Type:** Code statement

### Line  29
> **Code:** `"A91", "A92", "A93", "A94", "A95"`
> **Type:** Code statement

### Line  30
> **Code:** `] = Field(..., description="Personal status and sex")`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `other_parties: Literal[`
> **Type:** Code statement

### Line  32
> **Code:** `"A101", "A102", "A103"`
> **Type:** Code statement

### Line  33
> **Code:** `] = Field(..., description="Other debtors/guarantors")`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `residence_since: int = Field(..., ge=1, le=4, description="Present res...`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `property_magnitude: Literal[`
> **Type:** Code statement

### Line  36
> **Code:** `"A121", "A122", "A123", "A124"`
> **Type:** Code statement

### Line  37
> **Code:** `] = Field(..., description="Property magnitude")`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `age: int = Field(..., ge=18, le=100, description="Age in years")`
> **Type:** Assignment/comparison

### Line  39
> **Code:** `other_payment_plans: Literal[`
> **Type:** Code statement

### Line  40
> **Code:** `"A141", "A142", "A143"`
> **Type:** Code statement

### Line  41
> **Code:** `] = Field(..., description="Other payment plans")`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `housing: Literal[`
> **Type:** Code statement

### Line  43
> **Code:** `"A151", "A152", "A153"`
> **Type:** Code statement

### Line  44
> **Code:** `] = Field(..., description="Housing situation")`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `existing_credits: int = Field(..., ge=1, le=4, description="Number of ...`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `job: Literal[`
> **Type:** Code statement

### Line  47
> **Code:** `"A171", "A172", "A173", "A174"`
> **Type:** Code statement

### Line  48
> **Code:** `] = Field(..., description="Job classification")`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `num_dependents: int = Field(..., ge=1, le=2, description="Number of pe...`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `own_telephone: Literal[`
> **Type:** Code statement

### Line  51
> **Code:** `"A191", "A192"`
> **Type:** Code statement

### Line  52
> **Code:** `] = Field(..., description="Own telephone")`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `foreign_worker: Literal[`
> **Type:** Logical operation

### Line  54
> **Code:** `"A201", "A202"`
> **Type:** Code statement

### Line  55
> **Code:** `] = Field(..., description="Foreign worker")`
> **Type:** Assignment/comparison

### Line  56
> **Code:** ``
> **Type:** Empty line

### Line  57
> **Code:** `class Config:`
> **Type:** Class definition

### Line  58
> **Code:** `json_schema_extra = {`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `"example": {`
> **Type:** Code statement

### Line  60
> **Code:** `"checking_status": "A11",`
> **Type:** Code statement

### Line  61
> **Code:** `"duration": 6,`
> **Type:** Code statement

### Line  62
> **Code:** `"credit_history": "A34",`
> **Type:** Logical operation

### Line  63
> **Code:** `"purpose": "A43",`
> **Type:** Code statement

### Line  64
> **Code:** `"credit_amount": 1169,`
> **Type:** Code statement

### Line  65
> **Code:** `"savings_status": "A65",`
> **Type:** Code statement

### Line  66
> **Code:** `"employment": "A75",`
> **Type:** Code statement

### Line  67
> **Code:** `"installment_rate": 4,`
> **Type:** Code statement

### Line  68
> **Code:** `"personal_status": "A93",`
> **Type:** Code statement

### Line  69
> **Code:** `"other_parties": "A101",`
> **Type:** Code statement

### Line  70
> **Code:** `"residence_since": 4,`
> **Type:** Code statement

### Line  71
> **Code:** `"property_magnitude": "A121",`
> **Type:** Code statement

### Line  72
> **Code:** `"age": 67,`
> **Type:** Code statement

### Line  73
> **Code:** `"other_payment_plans": "A143",`
> **Type:** Code statement

### Line  74
> **Code:** `"housing": "A152",`
> **Type:** Code statement

### Line  75
> **Code:** `"existing_credits": 2,`
> **Type:** Code statement

### Line  76
> **Code:** `"job": "A173",`
> **Type:** Code statement

### Line  77
> **Code:** `"num_dependents": 1,`
> **Type:** Code statement

### Line  78
> **Code:** `"own_telephone": "A192",`
> **Type:** Code statement

### Line  79
> **Code:** `"foreign_worker": "A201"`
> **Type:** Logical operation

### Line  80
> **Code:** `}`
> **Type:** Code statement

### Line  81
> **Code:** `}`
> **Type:** Code statement

### Line  82
> **Code:** ``
> **Type:** Empty line

### Line  83
> **Code:** ``
> **Type:** Empty line

### Line  84
> **Code:** `class PredictResponse(BaseModel):`
> **Type:** Class definition

### Line  85
> **Code:** `prediction: int = Field(..., description="0=Good (repaid), 1=Bad (defa...`
> **Type:** Assignment/comparison

### Line  86
> **Code:** `probability: float = Field(..., description="Probability of default")`
> **Type:** Assignment/comparison

### Line  87
> **Code:** `risk_tier: str = Field(..., description="Risk tier: low/medium/high/cr...`
> **Type:** Assignment/comparison

### Line  88
> **Code:** ``
> **Type:** Empty line

### Line  89
> **Code:** ``
> **Type:** Empty line

### Line  90
> **Code:** `class HealthResponse(BaseModel):`
> **Type:** Class definition

### Line  91
> **Code:** `status: str = "ok"`
> **Type:** Assignment/comparison

### Line  92
> **Code:** `model_version: str | None = None`
> **Type:** Assignment/comparison

### Line  93
> **Code:** `model_loaded: bool = False`
> **Type:** Assignment/comparison

### Line  94
> **Code:** ``
> **Type:** Empty line

### Line  95
> **Code:** ``
> **Type:** Empty line

### Line  96
> **Code:** `class PredictionRecord(BaseModel):`
> **Type:** Class definition

### Line  97
> **Code:** `id: int`
> **Type:** Code statement

### Line  98
> **Code:** `timestamp: str`
> **Type:** Code statement

### Line  99
> **Code:** `input: dict`
> **Type:** Code statement

### Line 100
> **Code:** `prediction: int`
> **Type:** Code statement

### Line 101
> **Code:** `probability: float`
> **Type:** Code statement

### Line 102
> **Code:** `risk_tier: str`
> **Type:** Code statement

### Line 103
> **Code:** `latency_ms: float`
> **Type:** Code statement

### Line 104
> **Code:** ``
> **Type:** Empty line

### Line 105
> **Code:** ``
> **Type:** Empty line

### Line 106
> **Code:** `class StatsResponse(BaseModel):`
> **Type:** Class definition

### Line 107
> **Code:** `total_predictions: int`
> **Type:** Code statement

### Line 108
> **Code:** `default_rate: float`
> **Type:** Code statement

### Line 109
> **Code:** `risk_tier_distribution: dict`
> **Type:** Code statement

### Line 110
> **Code:** `avg_probability: float`
> **Type:** Code statement

### Line 111
> **Code:** `avg_latency_ms: float`
> **Type:** Code statement

### Line 112
> **Code:** ``
> **Type:** Empty line

### Line 113
> **Code:** ``
> **Type:** Empty line

### Line 114
> **Code:** `class ModelInfoResponse(BaseModel):`
> **Type:** Class definition

### Line 115
> **Code:** `model_name: str`
> **Type:** Code statement

### Line 116
> **Code:** `n_estimators: int`
> **Type:** Logical operation

### Line 117
> **Code:** `max_depth: int`
> **Type:** Code statement

### Line 118
> **Code:** `metrics: dict`
> **Type:** Code statement

### Line 119
> **Code:** `feature_importance: list[dict]`
> **Type:** Logical operation

## Summary
- **Total lines:** 119
- **Code lines:** 103
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 13

---
*Documentation generated for: mlops-platform-spec*
*File: schemas.py*
---

# mlops-platform-spec: model.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/api/model.py`
- **Total lines:** 77
- **File size:** 2231 bytes

## Line Type Summary
- **Code:** 54
- **Comment:** 0
- **Empty:** 20
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Model loading and prediction logic for the credit risk prediction A...`
> **Type:** Logical operation

### Line   5
> **Code:** `import os`
> **Type:** Imports a module

### Line   6
> **Code:** `import sys`
> **Type:** Imports a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line   9
> **Code:** `import mlflow.sklearn`
> **Type:** Imports a module

### Line  10
> **Code:** `from mlflow.tracking import MlflowClient`
> **Type:** Imports specific names from a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file_...`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `ML_DIR = os.path.join(PROJECT_ROOT, "ml")`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `for _path in (PROJECT_ROOT, ML_DIR):`
> **Type:** For loop

### Line  15
> **Code:** `if _path not in sys.path:`
> **Type:** Conditional statement

### Line  16
> **Code:** `sys.path.insert(0, _path)`
> **Type:** Function call

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `from preprocess import apply_encoders  # noqa: E402`
> **Type:** Imports specific names from a module

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `_model = None`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `_model_version = None`
> **Type:** Assignment/comparison

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `def load_model():`
> **Type:** Function definition

### Line  25
> **Code:** `"""Load the registered model from MLflow on startup."""`
> **Type:** Code statement

### Line  26
> **Code:** `global _model, _model_version`
> **Type:** Code statement

### Line  27
> **Code:** ``
> **Type:** Empty line

### Line  28
> **Code:** `tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `model_name = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  30
> **Code:** ``
> **Type:** Empty line

### Line  31
> **Code:** `mlflow.set_tracking_uri(tracking_uri)`
> **Type:** Function call

### Line  32
> **Code:** `client = MlflowClient()`
> **Type:** Assignment/comparison

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** `try:`
> **Type:** Code statement

### Line  35
> **Code:** `versions = client.get_latest_versions(model_name, stages=["Production"...`
> **Type:** Assignment/comparison

### Line  36
> **Code:** `if not versions:`
> **Type:** Conditional statement

### Line  37
> **Code:** `raise ValueError(f"No registered model found: {model_name}")`
> **Type:** Raises an exception

### Line  38
> **Code:** `version = versions[0]`
> **Type:** Assignment/comparison

### Line  39
> **Code:** `model_uri = f"models:/{model_name}/{version.version}"`
> **Type:** Assignment/comparison

### Line  40
> **Code:** ``
> **Type:** Empty line

### Line  41
> **Code:** `_model = mlflow.sklearn.load_model(model_uri)`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `_model_version = str(version.version)`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `print(f"Loaded model {model_name} version {_model_version} from {track...`
> **Type:** Prints output to console

### Line  44
> **Code:** `except Exception as e:`
> **Type:** Code statement

### Line  45
> **Code:** `print(f"ERROR loading model: {e}")`
> **Type:** Prints output to console

### Line  46
> **Code:** `raise`
> **Type:** Raises an exception

### Line  47
> **Code:** ``
> **Type:** Empty line

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `def get_model_version() -> str | None:`
> **Type:** Function definition

### Line  50
> **Code:** `return _model_version`
> **Type:** Returns a value from a function

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `def predict(input_data: dict) -> tuple[int, float]:`
> **Type:** Function definition

### Line  54
> **Code:** `"""Run prediction on input data and return (prediction, probability)."...`
> **Type:** Logical operation

### Line  55
> **Code:** `if _model is None:`
> **Type:** Conditional statement

### Line  56
> **Code:** `load_model()`
> **Type:** Function call

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** `df = pd.DataFrame([input_data])`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `X = apply_encoders(df)`
> **Type:** Assignment/comparison

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** `prediction = int(_model.predict(X)[0])`
> **Type:** Assignment/comparison

### Line  64
> **Code:** `probability = float(_model.predict_proba(X)[0][1])`
> **Type:** Assignment/comparison

### Line  65
> **Code:** ``
> **Type:** Empty line

### Line  66
> **Code:** `return prediction, probability`
> **Type:** Returns a value from a function

### Line  67
> **Code:** ``
> **Type:** Empty line

### Line  68
> **Code:** ``
> **Type:** Empty line

### Line  69
> **Code:** `def risk_tier(probability: float) -> str:`
> **Type:** Function definition

### Line  70
> **Code:** `if probability < 0.1:`
> **Type:** Conditional statement

### Line  71
> **Code:** `return "low"`
> **Type:** Returns a value from a function

### Line  72
> **Code:** `elif probability < 0.3:`
> **Type:** Else-if branch

### Line  73
> **Code:** `return "medium"`
> **Type:** Returns a value from a function

### Line  74
> **Code:** `elif probability < 0.6:`
> **Type:** Else-if branch

### Line  75
> **Code:** `return "high"`
> **Type:** Returns a value from a function

### Line  76
> **Code:** `else:`
> **Type:** Else block

### Line  77
> **Code:** `return "critical"`
> **Type:** Returns a value from a function

## Summary
- **Total lines:** 77
- **Code lines:** 54
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 20

---
*Documentation generated for: mlops-platform-spec*
*File: model.py*
---

# mlops-platform-spec: main.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/api/main.py`
- **Total lines:** 174
- **File size:** 5455 bytes

## Line Type Summary
- **Code:** 135
- **Comment:** 0
- **Empty:** 36
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add request validation and error handling`
> **Type:** TODO: high - Add request validation and error handling

### Line   2
> **Code:** `# TODO: medium - Implement request/response logging`
> **Type:** TODO: medium - Implement request/response logging

### Line   3
> **Code:** `# TODO: low - Add health check endpoint improvement`
> **Type:** TODO: low - Add health check endpoint improvement

### Line   4
> **Code:** `"""FastAPI app for Credit Risk (P1) — self-contained, trains at startu...`
> **Type:** Arithmetic operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `import sys`
> **Type:** Imports a module

### Line   7
> **Code:** `import os`
> **Type:** Imports a module

### Line   8
> **Code:** `_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
> **Type:** Assignment/comparison

### Line   9
> **Code:** `sys.path.insert(0, _ROOT)`
> **Type:** Function call

### Line  10
> **Code:** `sys.path.insert(0, os.path.join(_ROOT, "ml"))`
> **Type:** Function call

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `import time`
> **Type:** Imports a module

### Line  13
> **Code:** `from datetime import datetime, timezone`
> **Type:** Imports specific names from a module

### Line  14
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  17
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  18
> **Code:** `from contextlib import asynccontextmanager`
> **Type:** Imports specific names from a module

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `from fastapi import FastAPI`
> **Type:** Imports specific names from a module

### Line  21
> **Code:** `from fastapi.staticfiles import StaticFiles`
> **Type:** Imports specific names from a module

### Line  22
> **Code:** `from fastapi.responses import FileResponse`
> **Type:** Imports specific names from a module

### Line  23
> **Code:** `from sklearn.ensemble import GradientBoostingClassifier`
> **Type:** Imports specific names from a module

### Line  24
> **Code:** `from sklearn.model_selection import train_test_split`
> **Type:** Imports specific names from a module

### Line  25
> **Code:** `from sklearn.metrics import roc_auc_score, f1_score`
> **Type:** Imports specific names from a module

### Line  26
> **Code:** ``
> **Type:** Empty line

### Line  27
> **Code:** `from preprocess import load_data, encode_features, apply_encoders, get...`
> **Type:** Imports specific names from a module

### Line  28
> **Code:** `from schemas import PredictRequest`
> **Type:** Imports specific names from a module

### Line  29
> **Code:** ``
> **Type:** Empty line

### Line  30
> **Code:** `UI_DIR = Path(__file__).parent.parent / "ui"`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `MODEL = None`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `FEATURE_NAMES = None`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `PREDICTIONS = []`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `MODEL_METRICS = {}`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `MAX_LOG = 500`
> **Type:** Assignment/comparison

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `def risk_tier(prob: float) -> str:`
> **Type:** Function definition

### Line  39
> **Code:** `if prob < 0.1:`
> **Type:** Conditional statement

### Line  40
> **Code:** `return "low"`
> **Type:** Returns a value from a function

### Line  41
> **Code:** `if prob < 0.3:`
> **Type:** Conditional statement

### Line  42
> **Code:** `return "medium"`
> **Type:** Returns a value from a function

### Line  43
> **Code:** `if prob < 0.6:`
> **Type:** Conditional statement

### Line  44
> **Code:** `return "high"`
> **Type:** Returns a value from a function

### Line  45
> **Code:** `return "critical"`
> **Type:** Returns a value from a function

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** ``
> **Type:** Empty line

### Line  48
> **Code:** `def train_model():`
> **Type:** Function definition

### Line  49
> **Code:** `global MODEL, FEATURE_NAMES, MODEL_METRICS`
> **Type:** Code statement

### Line  50
> **Code:** `df = load_data()`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `print(f"P1: Loaded {len(df)} records, default rate={df['target'].mean(...`
> **Type:** Prints output to console

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `X, y = encode_features(df)`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `FEATURE_NAMES = get_feature_names()`
> **Type:** Assignment/comparison

### Line  55
> **Code:** ``
> **Type:** Empty line

### Line  56
> **Code:** `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0....`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `MODEL = GradientBoostingClassifier(n_estimators=300, max_depth=6, lear...`
> **Type:** Assignment/comparison

### Line  58
> **Code:** `MODEL.fit(X_train, y_train)`
> **Type:** Function call

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** `proba = MODEL.predict_proba(X_test)[:, 1]`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `preds = MODEL.predict(X_test)`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `auc = roc_auc_score(y_test, proba)`
> **Type:** Assignment/comparison

### Line  63
> **Code:** `f1 = f1_score(y_test, preds)`
> **Type:** Assignment/comparison

### Line  64
> **Code:** ``
> **Type:** Empty line

### Line  65
> **Code:** `MODEL_METRICS.update({`
> **Type:** Code statement

### Line  66
> **Code:** `"model_name": type(MODEL).__name__,`
> **Type:** Code statement

### Line  67
> **Code:** `"n_estimators": MODEL.n_estimators,`
> **Type:** Logical operation

### Line  68
> **Code:** `"max_depth": MODEL.max_depth,`
> **Type:** Code statement

### Line  69
> **Code:** `"learning_rate": MODEL.learning_rate,`
> **Type:** Code statement

### Line  70
> **Code:** `"subsample": MODEL.subsample,`
> **Type:** Code statement

### Line  71
> **Code:** `"random_state": MODEL.random_state,`
> **Type:** Logical operation

### Line  72
> **Code:** `"auc": round(float(auc), 4),`
> **Type:** Code statement

### Line  73
> **Code:** `"f1": round(float(f1), 4),`
> **Type:** Code statement

### Line  74
> **Code:** `})`
> **Type:** Code statement

### Line  75
> **Code:** `print(f"P1: AUC={auc:.4f}, F1={f1:.4f}")`
> **Type:** Prints output to console

### Line  76
> **Code:** ``
> **Type:** Empty line

### Line  77
> **Code:** ``
> **Type:** Empty line

### Line  78
> **Code:** `@asynccontextmanager`
> **Type:** Code statement

### Line  79
> **Code:** `async def lifespan(app: FastAPI):`
> **Type:** Code statement

### Line  80
> **Code:** `train_model()`
> **Type:** Function call

### Line  81
> **Code:** `yield`
> **Type:** Code statement

### Line  82
> **Code:** ``
> **Type:** Empty line

### Line  83
> **Code:** ``
> **Type:** Empty line

### Line  84
> **Code:** `app = FastAPI(title="Credit Risk Prediction API", version="1.0.0", lif...`
> **Type:** Assignment/comparison

### Line  85
> **Code:** ``
> **Type:** Empty line

### Line  86
> **Code:** ``
> **Type:** Empty line

### Line  87
> **Code:** `@app.get("/health")`
> **Type:** Arithmetic operation

### Line  88
> **Code:** `async def health():`
> **Type:** Code statement

### Line  89
> **Code:** `return {"status": "ok", "model_version": "1.0", "model_loaded": MODEL ...`
> **Type:** Returns a value from a function

### Line  90
> **Code:** ``
> **Type:** Empty line

### Line  91
> **Code:** ``
> **Type:** Empty line

### Line  92
> **Code:** `@app.post("/predict", response_model=dict)`
> **Type:** Assignment/comparison

### Line  93
> **Code:** `async def predict_endpoint(request: PredictRequest):`
> **Type:** Code statement

### Line  94
> **Code:** `t0 = time.perf_counter()`
> **Type:** Assignment/comparison

### Line  95
> **Code:** `input_data = request.model_dump()`
> **Type:** Assignment/comparison

### Line  96
> **Code:** `df = pd.DataFrame([input_data])`
> **Type:** Assignment/comparison

### Line  97
> **Code:** `X = apply_encoders(df)`
> **Type:** Assignment/comparison

### Line  98
> **Code:** `prob = float(MODEL.predict_proba(X)[0][1])`
> **Type:** Assignment/comparison

### Line  99
> **Code:** `pred = 1 if prob >= 0.5 else 0`
> **Type:** Assignment/comparison

### Line 100
> **Code:** `latency_ms = (time.perf_counter() - t0) * 1000`
> **Type:** Assignment/comparison

### Line 101
> **Code:** `tier = risk_tier(prob)`
> **Type:** Assignment/comparison

### Line 102
> **Code:** ``
> **Type:** Empty line

### Line 103
> **Code:** `PREDICTIONS.append({`
> **Type:** Code statement

### Line 104
> **Code:** `"id": len(PREDICTIONS) + 1,`
> **Type:** Arithmetic operation

### Line 105
> **Code:** `"timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),`
> **Type:** Assignment/comparison

### Line 106
> **Code:** `"input": input_data,`
> **Type:** Code statement

### Line 107
> **Code:** `"prediction": pred,`
> **Type:** Code statement

### Line 108
> **Code:** `"probability": round(prob, 4),`
> **Type:** Code statement

### Line 109
> **Code:** `"risk_tier": tier,`
> **Type:** Code statement

### Line 110
> **Code:** `"latency_ms": round(latency_ms, 2),`
> **Type:** Code statement

### Line 111
> **Code:** `})`
> **Type:** Code statement

### Line 112
> **Code:** `if len(PREDICTIONS) > MAX_LOG:`
> **Type:** Conditional statement

### Line 113
> **Code:** `del PREDICTIONS[: len(PREDICTIONS) - MAX_LOG]`
> **Type:** Arithmetic operation

### Line 114
> **Code:** ``
> **Type:** Empty line

### Line 115
> **Code:** `return {"prediction": pred, "probability": round(prob, 4), "risk_tier"...`
> **Type:** Returns a value from a function

### Line 116
> **Code:** ``
> **Type:** Empty line

### Line 117
> **Code:** ``
> **Type:** Empty line

### Line 118
> **Code:** `@app.get("/history")`
> **Type:** Arithmetic operation

### Line 119
> **Code:** `async def history(limit: int = 50):`
> **Type:** Assignment/comparison

### Line 120
> **Code:** `limit = max(1, min(limit, MAX_LOG))`
> **Type:** Assignment/comparison

### Line 121
> **Code:** `return {"total": len(PREDICTIONS), "limit": limit,`
> **Type:** Returns a value from a function

### Line 122
> **Code:** `"items": list(reversed(PREDICTIONS[-limit:]))}`
> **Type:** Arithmetic operation

### Line 123
> **Code:** ``
> **Type:** Empty line

### Line 124
> **Code:** ``
> **Type:** Empty line

### Line 125
> **Code:** `@app.get("/stats")`
> **Type:** Arithmetic operation

### Line 126
> **Code:** `async def stats():`
> **Type:** Code statement

### Line 127
> **Code:** `n = len(PREDICTIONS)`
> **Type:** Assignment/comparison

### Line 128
> **Code:** `tiers = {t: 0 for t in ("low", "medium", "high", "critical")}`
> **Type:** Assignment/comparison

### Line 129
> **Code:** `if n == 0:`
> **Type:** Conditional statement

### Line 130
> **Code:** `return {"total_predictions": 0, "default_rate": 0.0,`
> **Type:** Returns a value from a function

### Line 131
> **Code:** `"risk_tier_distribution": tiers, "avg_probability": 0.0,`
> **Type:** Code statement

### Line 132
> **Code:** `"avg_latency_ms": 0.0}`
> **Type:** Code statement

### Line 133
> **Code:** `defaults = sum(1 for p in PREDICTIONS if p["prediction"] == 1)`
> **Type:** Assignment/comparison

### Line 134
> **Code:** `for p in PREDICTIONS:`
> **Type:** For loop

### Line 135
> **Code:** `tiers[p["risk_tier"]] += 1`
> **Type:** Assignment/comparison

### Line 136
> **Code:** `return {`
> **Type:** Returns a value from a function

### Line 137
> **Code:** `"total_predictions": n,`
> **Type:** Code statement

### Line 138
> **Code:** `"default_rate": round(defaults / n, 4),`
> **Type:** Arithmetic operation

### Line 139
> **Code:** `"risk_tier_distribution": tiers,`
> **Type:** Code statement

### Line 140
> **Code:** `"avg_probability": round(sum(p["probability"] for p in PREDICTIONS) / ...`
> **Type:** Arithmetic operation

### Line 141
> **Code:** `"avg_latency_ms": round(sum(p["latency_ms"] for p in PREDICTIONS) / n,...`
> **Type:** Arithmetic operation

### Line 142
> **Code:** `}`
> **Type:** Code statement

### Line 143
> **Code:** ``
> **Type:** Empty line

### Line 144
> **Code:** ``
> **Type:** Empty line

### Line 145
> **Code:** `@app.get("/model-info")`
> **Type:** Arithmetic operation

### Line 146
> **Code:** `async def model_info():`
> **Type:** Code statement

### Line 147
> **Code:** `fi = sorted(`
> **Type:** Assignment/comparison

### Line 148
> **Code:** `({"feature": f, "importance": round(float(i), 4)}`
> **Type:** Logical operation

### Line 149
> **Code:** `for f, i in zip(FEATURE_NAMES, MODEL.feature_importances_)),`
> **Type:** For loop

### Line 150
> **Code:** `key=lambda x: x["importance"], reverse=True,`
> **Type:** Assignment/comparison

### Line 151
> **Code:** `)`
> **Type:** Code statement

### Line 152
> **Code:** `return {`
> **Type:** Returns a value from a function

### Line 153
> **Code:** `"model_name": MODEL_METRICS.get("model_name"),`
> **Type:** Code statement

### Line 154
> **Code:** `"n_estimators": MODEL_METRICS.get("n_estimators"),`
> **Type:** Logical operation

### Line 155
> **Code:** `"max_depth": MODEL_METRICS.get("max_depth"),`
> **Type:** Code statement

### Line 156
> **Code:** `"learning_rate": MODEL_METRICS.get("learning_rate"),`
> **Type:** Code statement

### Line 157
> **Code:** `"subsample": MODEL_METRICS.get("subsample"),`
> **Type:** Code statement

### Line 158
> **Code:** `"metrics": {"auc": MODEL_METRICS.get("auc"), "f1": MODEL_METRICS.get("...`
> **Type:** Code statement

### Line 159
> **Code:** `"feature_importance": fi,`
> **Type:** Logical operation

### Line 160
> **Code:** `}`
> **Type:** Code statement

### Line 161
> **Code:** ``
> **Type:** Empty line

### Line 162
> **Code:** ``
> **Type:** Empty line

### Line 163
> **Code:** `@app.get("/")`
> **Type:** Arithmetic operation

### Line 164
> **Code:** `async def serve_ui():`
> **Type:** Code statement

### Line 165
> **Code:** `return FileResponse(UI_DIR / "index.html")`
> **Type:** Returns a value from a function

### Line 166
> **Code:** ``
> **Type:** Empty line

### Line 167
> **Code:** ``
> **Type:** Empty line

### Line 168
> **Code:** `if UI_DIR.exists():`
> **Type:** Conditional statement

### Line 169
> **Code:** `app.mount("/ui", StaticFiles(directory=str(UI_DIR)), name="ui")`
> **Type:** Assignment/comparison

### Line 170
> **Code:** ``
> **Type:** Empty line

### Line 171
> **Code:** ``
> **Type:** Empty line

### Line 172
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line 173
> **Code:** `import uvicorn`
> **Type:** Imports a module

### Line 174
> **Code:** `uvicorn.run(app, host="0.0.0.0", port=8000)`
> **Type:** Assignment/comparison

## Summary
- **Total lines:** 174
- **Code lines:** 135
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 36

---
*Documentation generated for: mlops-platform-spec*
*File: main.py*
---

# mlops-platform-spec: generate_churn_data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/generate_churn_data.py`
- **Total lines:** 76
- **File size:** 2162 bytes

## Line Type Summary
- **Code:** 57
- **Comment:** 2
- **Empty:** 14
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   3
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   4
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   5
> **Code:** `"""Generate realistic synthetic Telco customer churn data (Kaggle-styl...`
> **Type:** Arithmetic operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Produces ~7000 rows with the same columns and value distributions as t...`
> **Type:** Logical operation

### Line   8
> **Code:** `public Telco Customer Churn dataset (minus customerID).`
> **Type:** Code statement

### Line   9
> **Code:** `"""`
> **Type:** Code statement

### Line  10
> **Code:** `import random`
> **Type:** Imports a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `random.seed(42)`
> **Type:** Logical operation

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `CONTRACTS = ["Month-to-month", "One year", "Two year"]`
> **Type:** Assignment/comparison

### Line  15
> **Code:** `PAYMENT_METHODS = [`
> **Type:** Assignment/comparison

### Line  16
> **Code:** `"Electronic check",`
> **Type:** Code statement

### Line  17
> **Code:** `"Mailed check",`
> **Type:** Code statement

### Line  18
> **Code:** `"Bank transfer (automatic)",`
> **Type:** Code statement

### Line  19
> **Code:** `"Credit card (automatic)",`
> **Type:** Code statement

### Line  20
> **Code:** `]`
> **Type:** Code statement

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `# Churn probability per contract type (longer contracts churn less)`
> **Type:** Comment: Churn probability per contract type (longer contracts churn less)

### Line  23
> **Code:** `CONTRACT_CHURN = {`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `"Month-to-month": 0.45,`
> **Type:** Arithmetic operation

### Line  25
> **Code:** `"One year": 0.16,`
> **Type:** Code statement

### Line  26
> **Code:** `"Two year": 0.03,`
> **Type:** Code statement

### Line  27
> **Code:** `}`
> **Type:** Code statement

### Line  28
> **Code:** `PAYMENT_CHURN = {`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `"Electronic check": 0.35,`
> **Type:** Code statement

### Line  30
> **Code:** `"Mailed check": 0.22,`
> **Type:** Code statement

### Line  31
> **Code:** `"Bank transfer (automatic)": 0.12,`
> **Type:** Code statement

### Line  32
> **Code:** `"Credit card (automatic)": 0.10,`
> **Type:** Code statement

### Line  33
> **Code:** `}`
> **Type:** Code statement

### Line  34
> **Code:** ``
> **Type:** Empty line

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** `def rand_tenure(contract):`
> **Type:** Function definition

### Line  37
> **Code:** `if contract == "Month-to-month":`
> **Type:** Conditional statement

### Line  38
> **Code:** `return random.randint(0, 24)`
> **Type:** Returns a value from a function

### Line  39
> **Code:** `if contract == "One year":`
> **Type:** Conditional statement

### Line  40
> **Code:** `return random.randint(12, 24)`
> **Type:** Returns a value from a function

### Line  41
> **Code:** `return random.randint(24, 72)`
> **Type:** Returns a value from a function

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** `def generate_row():`
> **Type:** Function definition

### Line  45
> **Code:** `contract = random.choices(CONTRACTS, weights=[0.55, 0.24, 0.21])[0]`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `payment = random.choices(`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `PAYMENT_METHODS, weights=[0.35, 0.20, 0.23, 0.22]`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `)[0]`
> **Type:** Data structure operation

### Line  49
> **Code:** `tenure = rand_tenure(contract)`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `monthly = round(random.uniform(18.0, 120.0), 2)`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `total = round(monthly * tenure, 2)`
> **Type:** Assignment/comparison

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `p = 0.04  # base churn`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `p += CONTRACT_CHURN[contract]`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `p += PAYMENT_CHURN[payment]`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `p += max(0.0, (monthly - 60.0) / 300.0)`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `p -= min(0.25, tenure / 200.0)`
> **Type:** Assignment/comparison

### Line  58
> **Code:** `p = min(max(p, 0.0), 0.97)`
> **Type:** Assignment/comparison

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** `churn = 1 if random.random() < p else 0`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `return tenure, monthly, total, contract, payment, churn`
> **Type:** Returns a value from a function

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `def main():`
> **Type:** Function definition

### Line  65
> **Code:** `rows = ["tenure,MonthlyCharges,TotalCharges,Contract,PaymentMethod,Chu...`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `for _ in range(7000):`
> **Type:** For loop

### Line  67
> **Code:** `t, m, tot, c, pm, ch = generate_row()`
> **Type:** Assignment/comparison

### Line  68
> **Code:** `rows.append(f"{t},{m},{tot},{c},{pm},{ch}")`
> **Type:** Function call

### Line  69
> **Code:** `out = "ml/data/churn.csv"`
> **Type:** Assignment/comparison

### Line  70
> **Code:** `with open(out, "w", encoding="utf-8") as f:`
> **Type:** Context manager

### Line  71
> **Code:** `f.write("\n".join(rows) + "\n")`
> **Type:** Arithmetic operation

### Line  72
> **Code:** `print(f"wrote {out} with {len(rows) - 1} data rows")`
> **Type:** Prints output to console

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  76
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 76
- **Code lines:** 57
- **Comments:** 2
- **TODO items:** 3
- **Empty lines:** 14

---
*Documentation generated for: mlops-platform-spec*
*File: generate_churn_data.py*
---

# mlops-platform-spec: __init__.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/__init__.py`
- **Total lines:** 4
- **File size:** 210 bytes

## Line Type Summary
- **Code:** 1
- **Comment:** 0
- **Empty:** 0
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Credit risk ML pipeline — training, evaluation, and data generation...`
> **Type:** Logical operation

## Summary
- **Total lines:** 4
- **Code lines:** 1
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 0

---
*Documentation generated for: mlops-platform-spec*
*File: __init__.py*
---

# mlops-platform-spec: evaluate.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/evaluate.py`
- **Total lines:** 75
- **File size:** 2493 bytes

## Line Type Summary
- **Code:** 54
- **Comment:** 1
- **Empty:** 17
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: high - Add quality gate with thresholds`
> **Type:** TODO: high - Add quality gate with thresholds

### Line   3
> **Code:** `# TODO: medium - Implement comparison vs current production model`
> **Type:** TODO: medium - Implement comparison vs current production model

### Line   4
> **Code:** `# TODO: low - Add metrics export for Evidence Pack`
> **Type:** TODO: low - Add metrics export for Evidence Pack

### Line   5
> **Code:** `"""Evaluate the credit risk model against the hold-out test set.`
> **Type:** Arithmetic operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Loads the registered model from MLflow, computes AUC, F1, precision, r...`
> **Type:** Code statement

### Line   8
> **Code:** `and gates on AUC >= 0.75, F1 >= 0.30.`
> **Type:** Assignment/comparison

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `Exit codes:`
> **Type:** Code statement

### Line  11
> **Code:** `0  AUC >= 0.75 AND F1 >= 0.30 (gate passed)`
> **Type:** Assignment/comparison

### Line  12
> **Code:** `1  gate failed or any error`
> **Type:** Logical operation

### Line  13
> **Code:** `"""`
> **Type:** Code statement

### Line  14
> **Code:** `import os`
> **Type:** Imports a module

### Line  15
> **Code:** `import sys`
> **Type:** Imports a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line  18
> **Code:** `from mlflow.tracking import MlflowClient`
> **Type:** Imports specific names from a module

### Line  19
> **Code:** `from sklearn.metrics import classification_report, f1_score, precision...`
> **Type:** Imports specific names from a module

### Line  20
> **Code:** ``
> **Type:** Empty line

### Line  21
> **Code:** `from preprocess import encode_features, load_data, train_test_split`
> **Type:** Imports specific names from a module

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** `MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `AUC_THRESHOLD = 0.75`
> **Type:** Assignment/comparison

### Line  26
> **Code:** `F1_THRESHOLD = 0.30`
> **Type:** Assignment/comparison

### Line  27
> **Code:** ``
> **Type:** Empty line

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** `def main():`
> **Type:** Function definition

### Line  30
> **Code:** `mlflow.set_tracking_uri(TRACKING_URI)`
> **Type:** Function call

### Line  31
> **Code:** ``
> **Type:** Empty line

### Line  32
> **Code:** `client = MlflowClient()`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `versions = client.get_latest_versions(MODEL_NAME, stages=["Production"...`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `if not versions:`
> **Type:** Conditional statement

### Line  35
> **Code:** `print(f"ERROR: no registered model named '{MODEL_NAME}' found")`
> **Type:** Prints output to console

### Line  36
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  37
> **Code:** `version = versions[0]`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `print(f"Evaluating {MODEL_NAME} version {version.version}")`
> **Type:** Prints output to console

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** `model_uri = f"models:/{MODEL_NAME}/{version.version}"`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `clf = mlflow.sklearn.load_model(model_uri)`
> **Type:** Assignment/comparison

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `df = load_data()`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `X, y = encode_features(df)`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `train_df, test_df = train_test_split(df)`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `X_test = X[test_df.index]`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `y_test = y[test_df.index]`
> **Type:** Assignment/comparison

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `proba = clf.predict_proba(X_test)[:, 1]`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `preds = clf.predict(X_test)`
> **Type:** Assignment/comparison

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `auc = float(roc_auc_score(y_test, proba))`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `f1 = float(f1_score(y_test, preds, zero_division=0))`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `prec = float(precision_score(y_test, preds, zero_division=0))`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `rec = float(recall_score(y_test, preds, zero_division=0))`
> **Type:** Assignment/comparison

### Line  56
> **Code:** ``
> **Type:** Empty line

### Line  57
> **Code:** `print("Classification report:")`
> **Type:** Prints output to console

### Line  58
> **Code:** `print(classification_report(y_test, preds, target_names=["Good", "Bad"...`
> **Type:** Prints output to console

### Line  59
> **Code:** `print(f"AUC:  {auc:.4f}  (threshold: {AUC_THRESHOLD})")`
> **Type:** Prints output to console

### Line  60
> **Code:** `print(f"F1:   {f1:.4f}  (threshold: {F1_THRESHOLD})")`
> **Type:** Prints output to console

### Line  61
> **Code:** `print(f"Precision: {prec:.4f}  Recall: {rec:.4f}")`
> **Type:** Prints output to console

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** `if auc < AUC_THRESHOLD:`
> **Type:** Conditional statement

### Line  64
> **Code:** `print(f"FAIL: AUC {auc:.4f} < {AUC_THRESHOLD}")`
> **Type:** Prints output to console

### Line  65
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  66
> **Code:** `if f1 < F1_THRESHOLD:`
> **Type:** Conditional statement

### Line  67
> **Code:** `print(f"FAIL: F1 {f1:.4f} < {F1_THRESHOLD}")`
> **Type:** Prints output to console

### Line  68
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  69
> **Code:** ``
> **Type:** Empty line

### Line  70
> **Code:** `print(f"PASS: AUC={auc:.4f} >= {AUC_THRESHOLD}, F1={f1:.4f} >= {F1_THR...`
> **Type:** Prints output to console

### Line  71
> **Code:** `sys.exit(0)`
> **Type:** Function call

### Line  72
> **Code:** ``
> **Type:** Empty line

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  75
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 75
- **Code lines:** 54
- **Comments:** 1
- **TODO items:** 3
- **Empty lines:** 17

---
*Documentation generated for: mlops-platform-spec*
*File: evaluate.py*
---

# mlops-platform-spec: preprocess.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/preprocess.py`
- **Total lines:** 91
- **File size:** 2930 bytes

## Line Type Summary
- **Code:** 68
- **Comment:** 0
- **Empty:** 20
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Shared preprocessing for the credit risk ML pipeline.`
> **Type:** Logical operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Encodes categorical features with OneHotEncoder, scales numeric featur...`
> **Type:** Logical operation

### Line   7
> **Code:** `and splits the data. Both train.py and evaluate.py import from here so`
> **Type:** Logical operation

### Line   8
> **Code:** `the encoding is identical between training and evaluation.`
> **Type:** Logical operation

### Line   9
> **Code:** `"""`
> **Type:** Code statement

### Line  10
> **Code:** `import os`
> **Type:** Imports a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  13
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  14
> **Code:** `from sklearn.compose import ColumnTransformer`
> **Type:** Imports specific names from a module

### Line  15
> **Code:** `from sklearn.preprocessing import OneHotEncoder, StandardScaler`
> **Type:** Imports specific names from a module

### Line  16
> **Code:** `from sklearn.model_selection import train_test_split as _split`
> **Type:** Imports specific names from a module

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `FEATURE_COLS = [`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `"checking_status", "duration", "credit_history", "purpose", "credit_am...`
> **Type:** Logical operation

### Line  20
> **Code:** `"savings_status", "employment", "installment_rate", "personal_status",`
> **Type:** Code statement

### Line  21
> **Code:** `"other_parties", "residence_since", "property_magnitude", "age",`
> **Type:** Code statement

### Line  22
> **Code:** `"other_payment_plans", "housing", "existing_credits", "job",`
> **Type:** Code statement

### Line  23
> **Code:** `"num_dependents", "own_telephone", "foreign_worker"`
> **Type:** Logical operation

### Line  24
> **Code:** `]`
> **Type:** Code statement

### Line  25
> **Code:** ``
> **Type:** Empty line

### Line  26
> **Code:** `CATEGORICAL_COLS = [`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `"checking_status", "credit_history", "purpose", "savings_status",`
> **Type:** Logical operation

### Line  28
> **Code:** `"employment", "personal_status", "other_parties", "property_magnitude"...`
> **Type:** Code statement

### Line  29
> **Code:** `"other_payment_plans", "housing", "job", "own_telephone", "foreign_wor...`
> **Type:** Logical operation

### Line  30
> **Code:** `]`
> **Type:** Code statement

### Line  31
> **Code:** ``
> **Type:** Empty line

### Line  32
> **Code:** `NUMERIC_COLS = [`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `"duration", "credit_amount", "installment_rate", "residence_since",`
> **Type:** Code statement

### Line  34
> **Code:** `"age", "existing_credits", "num_dependents"`
> **Type:** Code statement

### Line  35
> **Code:** `]`
> **Type:** Code statement

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** `TARGET = "target"`
> **Type:** Assignment/comparison

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)...`
> **Type:** Assignment/comparison

### Line  40
> **Code:** `DATA_PATH = os.environ.get(`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `"CREDIT_DATA_PATH", os.path.join(_REPO_ROOT, "ml", "data", "credit.csv...`
> **Type:** Function call

### Line  42
> **Code:** `)`
> **Type:** Code statement

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** `_preprocessor = None`
> **Type:** Assignment/comparison

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `def load_data(path=None):`
> **Type:** Function definition

### Line  48
> **Code:** `path = path or DATA_PATH`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `df = pd.read_csv(path)`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `return df`
> **Type:** Returns a value from a function

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `def _get_preprocessor():`
> **Type:** Function definition

### Line  54
> **Code:** `global _preprocessor`
> **Type:** Logical operation

### Line  55
> **Code:** `if _preprocessor is None:`
> **Type:** Conditional statement

### Line  56
> **Code:** `_preprocessor = ColumnTransformer(`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `transformers=[`
> **Type:** Assignment/comparison

### Line  58
> **Code:** `("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), C...`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `("num", StandardScaler(), NUMERIC_COLS),`
> **Type:** Logical operation

### Line  60
> **Code:** `],`
> **Type:** Code statement

### Line  61
> **Code:** `remainder="drop",`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `verbose_feature_names_out=False,`
> **Type:** Assignment/comparison

### Line  63
> **Code:** `)`
> **Type:** Code statement

### Line  64
> **Code:** `return _preprocessor`
> **Type:** Returns a value from a function

### Line  65
> **Code:** ``
> **Type:** Empty line

### Line  66
> **Code:** ``
> **Type:** Empty line

### Line  67
> **Code:** `def encode_features(df):`
> **Type:** Function definition

### Line  68
> **Code:** `"""Return (X, y) with all features encoded as numeric matrix."""`
> **Type:** Code statement

### Line  69
> **Code:** `preprocessor = _get_preprocessor()`
> **Type:** Assignment/comparison

### Line  70
> **Code:** `X = preprocessor.fit_transform(df[FEATURE_COLS])`
> **Type:** Assignment/comparison

### Line  71
> **Code:** `y = df[TARGET].astype(int).values`
> **Type:** Assignment/comparison

### Line  72
> **Code:** `return X, y`
> **Type:** Returns a value from a function

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** `def apply_encoders(df, encoders=None):`
> **Type:** Function definition

### Line  76
> **Code:** `"""Apply fitted preprocessor to new data (for API inference)."""`
> **Type:** Logical operation

### Line  77
> **Code:** `preprocessor = _get_preprocessor()`
> **Type:** Assignment/comparison

### Line  78
> **Code:** `X = preprocessor.transform(df[FEATURE_COLS])`
> **Type:** Assignment/comparison

### Line  79
> **Code:** `return X`
> **Type:** Returns a value from a function

### Line  80
> **Code:** ``
> **Type:** Empty line

### Line  81
> **Code:** ``
> **Type:** Empty line

### Line  82
> **Code:** `def train_test_split(df, test_size=0.2, random_state=42):`
> **Type:** Function definition

### Line  83
> **Code:** `return _split(`
> **Type:** Returns a value from a function

### Line  84
> **Code:** `df, test_size=test_size, random_state=random_state, stratify=df[TARGET...`
> **Type:** Assignment/comparison

### Line  85
> **Code:** `)`
> **Type:** Code statement

### Line  86
> **Code:** ``
> **Type:** Empty line

### Line  87
> **Code:** ``
> **Type:** Empty line

### Line  88
> **Code:** `def get_feature_names():`
> **Type:** Function definition

### Line  89
> **Code:** `"""Get feature names after one-hot encoding."""`
> **Type:** Arithmetic operation

### Line  90
> **Code:** `preprocessor = _get_preprocessor()`
> **Type:** Assignment/comparison

### Line  91
> **Code:** `return preprocessor.get_feature_names_out().tolist()`
> **Type:** Returns a value from a function

## Summary
- **Total lines:** 91
- **Code lines:** 68
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 20

---
*Documentation generated for: mlops-platform-spec*
*File: preprocess.py*
---

# mlops-platform-spec: train.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/train.py`
- **Total lines:** 102
- **File size:** 3313 bytes

## Line Type Summary
- **Code:** 79
- **Comment:** 1
- **Empty:** 19
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: high - Add data validation before training`
> **Type:** TODO: high - Add data validation before training

### Line   3
> **Code:** `# TODO: medium - Implement hyperparameter logging`
> **Type:** TODO: medium - Implement hyperparameter logging

### Line   4
> **Code:** `# TODO: low - Add model explainability integration`
> **Type:** TODO: low - Add model explainability integration

### Line   5
> **Code:** `"""Train a credit risk classifier and log it to MLflow.`
> **Type:** Logical operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Steps:`
> **Type:** Code statement

### Line   8
> **Code:** `1. Load ml/data/credit.csv (German Credit Data)`
> **Type:** Arithmetic operation

### Line   9
> **Code:** `2. Encode categorical features with OneHotEncoder, scale numeric with ...`
> **Type:** Logical operation

### Line  10
> **Code:** `3. Train/test split 80/20, stratified, random_state=42`
> **Type:** Assignment/comparison

### Line  11
> **Code:** `4. Train GradientBoostingClassifier`
> **Type:** Code statement

### Line  12
> **Code:** `5. Log params + metrics (AUC, F1, precision, recall) to MLflow`
> **Type:** Arithmetic operation

### Line  13
> **Code:** `6. Register model in MLflow Model Registry as "credit-risk-model"`
> **Type:** Arithmetic operation

### Line  14
> **Code:** `7. Save model artifact model.pkl`
> **Type:** Code statement

### Line  15
> **Code:** `"""`
> **Type:** Code statement

### Line  16
> **Code:** `import os`
> **Type:** Imports a module

### Line  17
> **Code:** `import pickle`
> **Type:** Imports a module

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line  20
> **Code:** `import mlflow.sklearn`
> **Type:** Imports a module

### Line  21
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  22
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  23
> **Code:** `from sklearn.ensemble import GradientBoostingClassifier`
> **Type:** Imports specific names from a module

### Line  24
> **Code:** `from sklearn.metrics import (`
> **Type:** Imports specific names from a module

### Line  25
> **Code:** `f1_score,`
> **Type:** Logical operation

### Line  26
> **Code:** `precision_score,`
> **Type:** Logical operation

### Line  27
> **Code:** `recall_score,`
> **Type:** Logical operation

### Line  28
> **Code:** `roc_auc_score,`
> **Type:** Logical operation

### Line  29
> **Code:** `)`
> **Type:** Code statement

### Line  30
> **Code:** ``
> **Type:** Empty line

### Line  31
> **Code:** `from preprocess import encode_features, load_data, train_test_split`
> **Type:** Imports specific names from a module

### Line  32
> **Code:** ``
> **Type:** Empty line

### Line  33
> **Code:** `MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** `_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)...`
> **Type:** Assignment/comparison

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `def main():`
> **Type:** Function definition

### Line  40
> **Code:** `mlflow.set_tracking_uri(TRACKING_URI)`
> **Type:** Function call

### Line  41
> **Code:** `mlflow.set_experiment("credit-risk")`
> **Type:** Arithmetic operation

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `df = load_data()`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `X, y = encode_features(df)`
> **Type:** Assignment/comparison

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** `train_df, test_df = train_test_split(df)`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `X_train = X[train_df.index]`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `y_train = y[train_df.index]`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `X_test = X[test_df.index]`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `y_test = y[test_df.index]`
> **Type:** Assignment/comparison

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `params = {`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `"n_estimators": 300,`
> **Type:** Logical operation

### Line  54
> **Code:** `"max_depth": 6,`
> **Type:** Code statement

### Line  55
> **Code:** `"learning_rate": 0.05,`
> **Type:** Code statement

### Line  56
> **Code:** `"subsample": 0.8,`
> **Type:** Code statement

### Line  57
> **Code:** `"min_samples_split": 5,`
> **Type:** Code statement

### Line  58
> **Code:** `"min_samples_leaf": 2,`
> **Type:** Code statement

### Line  59
> **Code:** `"random_state": 42,`
> **Type:** Logical operation

### Line  60
> **Code:** `}`
> **Type:** Code statement

### Line  61
> **Code:** `clf = GradientBoostingClassifier(**params)`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `clf.fit(X_train, y_train)`
> **Type:** Function call

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `preds = clf.predict(X_test)`
> **Type:** Assignment/comparison

### Line  65
> **Code:** `proba = clf.predict_proba(X_test)[:, 1]`
> **Type:** Assignment/comparison

### Line  66
> **Code:** ``
> **Type:** Empty line

### Line  67
> **Code:** `metrics = {`
> **Type:** Assignment/comparison

### Line  68
> **Code:** `"f1": float(f1_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  69
> **Code:** `"roc_auc": float(roc_auc_score(y_test, proba)),`
> **Type:** Logical operation

### Line  70
> **Code:** `"precision": float(precision_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  71
> **Code:** `"recall": float(recall_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  72
> **Code:** `}`
> **Type:** Code statement

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** `print(f"metrics: {metrics}")`
> **Type:** Prints output to console

### Line  75
> **Code:** ``
> **Type:** Empty line

### Line  76
> **Code:** `with mlflow.start_run() as run:`
> **Type:** Context manager

### Line  77
> **Code:** `mlflow.log_params(params)`
> **Type:** Function call

### Line  78
> **Code:** `mlflow.log_metrics(metrics)`
> **Type:** Function call

### Line  79
> **Code:** `mlflow.log_param("n_features", X_train.shape[1])`
> **Type:** Function call

### Line  80
> **Code:** `mlflow.log_param("data_source", "german.data (UCI Statlog)")`
> **Type:** Function call

### Line  81
> **Code:** `mlflow.log_param("default_rate", f"{y_train.mean():.4f}")`
> **Type:** Function call

### Line  82
> **Code:** ``
> **Type:** Empty line

### Line  83
> **Code:** `mlflow.sklearn.log_model(clf, "model")`
> **Type:** Function call

### Line  84
> **Code:** `mlflow.log_artifact(os.path.join(_REPO_ROOT, "ml", "data", "credit.csv...`
> **Type:** Assignment/comparison

### Line  85
> **Code:** ``
> **Type:** Empty line

### Line  86
> **Code:** `model_uri = f"runs:/{run.info.run_id}/model"`
> **Type:** Assignment/comparison

### Line  87
> **Code:** `registered = mlflow.register_model(model_uri, MODEL_NAME)`
> **Type:** Assignment/comparison

### Line  88
> **Code:** `client = mlflow.MlflowClient()`
> **Type:** Assignment/comparison

### Line  89
> **Code:** `client.transition_model_version_stage(`
> **Type:** Code statement

### Line  90
> **Code:** `name=MODEL_NAME, version=registered.version, stage="Staging"`
> **Type:** Assignment/comparison

### Line  91
> **Code:** `)`
> **Type:** Code statement

### Line  92
> **Code:** `print(f"Registered {MODEL_NAME} version {registered.version} in Stagin...`
> **Type:** Prints output to console

### Line  93
> **Code:** ``
> **Type:** Empty line

### Line  94
> **Code:** `model_path = os.path.join(_REPO_ROOT, "ml", "model.pkl")`
> **Type:** Assignment/comparison

### Line  95
> **Code:** `with open(model_path, "wb") as f:`
> **Type:** Context manager

### Line  96
> **Code:** `pickle.dump(clf, f)`
> **Type:** Function call

### Line  97
> **Code:** `print(f"Saved model to {model_path}")`
> **Type:** Prints output to console

### Line  98
> **Code:** `print(f"AUC={metrics['roc_auc']:.4f} F1={metrics['f1']:.4f}")`
> **Type:** Prints output to console

### Line  99
> **Code:** ``
> **Type:** Empty line

### Line 100
> **Code:** ``
> **Type:** Empty line

### Line 101
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line 102
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 102
- **Code lines:** 79
- **Comments:** 1
- **TODO items:** 3
- **Empty lines:** 19

---
*Documentation generated for: mlops-platform-spec*
*File: train.py*
---

# mlops-platform-spec: drift_detector.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/monitoring/drift_detector.py`
- **Total lines:** 89
- **File size:** 3185 bytes

## Line Type Summary
- **Code:** 69
- **Comment:** 0
- **Empty:** 17
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add alert rule for ingestion stalls`
> **Type:** TODO: high - Add alert rule for ingestion stalls

### Line   2
> **Code:** `# TODO: medium - Implement dashboard for drift detection`
> **Type:** TODO: medium - Implement dashboard for drift detection

### Line   3
> **Code:** `# TODO: low - Add prediction distribution monitoring`
> **Type:** TODO: low - Add prediction distribution monitoring

### Line   4
> **Code:** `"""Data drift detection for the credit risk pipeline.`
> **Type:** Logical operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Compares current/inference data against the reference (training) data ...`
> **Type:** Arithmetic operation

### Line   7
> **Code:** `numeric feature with a two-sample Kolmogorov-Smirnov test. Writes an a...`
> **Type:** Arithmetic operation

### Line   8
> **Code:** `drift score to ml/data/monitoring/drift_report.json for the retraining...`
> **Type:** Arithmetic operation

### Line   9
> **Code:** `"""`
> **Type:** Code statement

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `from __future__ import annotations`
> **Type:** Imports specific names from a module

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** `import argparse`
> **Type:** Imports a module

### Line  14
> **Code:** `import json`
> **Type:** Imports a module

### Line  15
> **Code:** `import logging`
> **Type:** Imports a module

### Line  16
> **Code:** `import os`
> **Type:** Imports a module

### Line  17
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  20
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  21
> **Code:** `from scipy import stats`
> **Type:** Imports specific names from a module

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** `logger = logging.getLogger(__name__)`
> **Type:** Assignment/comparison

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `import sys`
> **Type:** Imports a module

### Line  26
> **Code:** `sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))`
> **Type:** Function call

### Line  27
> **Code:** `from preprocess import NUMERIC_COLS, DATA_PATH`
> **Type:** Imports specific names from a module

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** `_REPO_ROOT = Path(__file__).resolve().parents[2]`
> **Type:** Assignment/comparison

### Line  30
> **Code:** `DEFAULT_REFERENCE = os.environ.get("CREDIT_DATA_PATH", DATA_PATH)`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `DEFAULT_CURRENT = os.environ.get("CURRENT_DATA_PATH", DEFAULT_REFERENC...`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `REPORT_PATH = _REPO_ROOT / "ml" / "data" / "monitoring" / "drift_repor...`
> **Type:** Assignment/comparison

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** `KS_ALPHA = 0.05`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `KS_STAT_THRESHOLD = 0.1`
> **Type:** Assignment/comparison

### Line  36
> **Code:** `DRIFT_HARD_THRESHOLD = float(os.environ.get("DRIFT_THRESHOLD", "0.3"))`
> **Type:** Assignment/comparison

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `def detect_drift(reference_path: str | Path, current_path: str | Path ...`
> **Type:** Function definition

### Line  40
> **Code:** `ref = pd.read_csv(reference_path)`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `cur = pd.read_csv(current_path)`
> **Type:** Assignment/comparison

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `features = {}`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `flagged = []`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `for col in NUMERIC_COLS:`
> **Type:** For loop

### Line  46
> **Code:** `if col not in ref.columns or col not in cur.columns:`
> **Type:** Conditional statement

### Line  47
> **Code:** `features[col] = {"error": "column missing"}`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `continue`
> **Type:** Code statement

### Line  49
> **Code:** `r = pd.to_numeric(ref[col], errors="coerce").dropna().to_numpy()`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `c = pd.to_numeric(cur[col], errors="coerce").dropna().to_numpy()`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `if r.size == 0 or c.size == 0:`
> **Type:** Conditional statement

### Line  52
> **Code:** `features[col] = {"error": "empty column"}`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `continue`
> **Type:** Code statement

### Line  54
> **Code:** `stat, p = stats.ks_2samp(r, c)`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `drifted = bool(p < KS_ALPHA and stat > KS_STAT_THRESHOLD)`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `features[col] = {"ks_statistic": float(stat), "p_value": float(p), "dr...`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `if drifted:`
> **Type:** Conditional statement

### Line  58
> **Code:** `flagged.append(col)`
> **Type:** Function call

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** `drift_score = len(set(flagged)) / max(len(NUMERIC_COLS), 1)`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `report = {`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `"reference_path": str(reference_path),`
> **Type:** Code statement

### Line  63
> **Code:** `"current_path": str(current_path),`
> **Type:** Code statement

### Line  64
> **Code:** `"n_features": len(NUMERIC_COLS),`
> **Type:** Code statement

### Line  65
> **Code:** `"drift_score": drift_score,`
> **Type:** Logical operation

### Line  66
> **Code:** `"threshold": DRIFT_HARD_THRESHOLD,`
> **Type:** Code statement

### Line  67
> **Code:** `"drift_detected": drift_score > DRIFT_HARD_THRESHOLD,`
> **Type:** Comparison operation

### Line  68
> **Code:** `"drifted_features": flagged,`
> **Type:** Code statement

### Line  69
> **Code:** `"features": features,`
> **Type:** Code statement

### Line  70
> **Code:** `}`
> **Type:** Code statement

### Line  71
> **Code:** ``
> **Type:** Empty line

### Line  72
> **Code:** `REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)`
> **Type:** Assignment/comparison

### Line  73
> **Code:** `REPORT_PATH.write_text(json.dumps(report, indent=2))`
> **Type:** Assignment/comparison

### Line  74
> **Code:** `logger.info("Drift score=%.3f threshold=%.3f detected=%s", drift_score...`
> **Type:** Assignment/comparison

### Line  75
> **Code:** `return report`
> **Type:** Returns a value from a function

### Line  76
> **Code:** ``
> **Type:** Empty line

### Line  77
> **Code:** ``
> **Type:** Empty line

### Line  78
> **Code:** `def main() -> None:`
> **Type:** Function definition

### Line  79
> **Code:** `logging.basicConfig(level=logging.INFO)`
> **Type:** Assignment/comparison

### Line  80
> **Code:** `parser = argparse.ArgumentParser(description="Drift detection")`
> **Type:** Assignment/comparison

### Line  81
> **Code:** `parser.add_argument("--reference", default=str(DEFAULT_REFERENCE))`
> **Type:** Assignment/comparison

### Line  82
> **Code:** `parser.add_argument("--current", default=str(DEFAULT_CURRENT))`
> **Type:** Assignment/comparison

### Line  83
> **Code:** `args = parser.parse_args()`
> **Type:** Assignment/comparison

### Line  84
> **Code:** `report = detect_drift(args.reference, args.current)`
> **Type:** Assignment/comparison

### Line  85
> **Code:** `print(json.dumps(report, indent=2))`
> **Type:** Prints output to console

### Line  86
> **Code:** ``
> **Type:** Empty line

### Line  87
> **Code:** ``
> **Type:** Empty line

### Line  88
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  89
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 89
- **Code lines:** 69
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 17

---
*Documentation generated for: mlops-platform-spec*
*File: drift_detector.py*
---

# mlops-platform-spec: __init__.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/monitoring/__init__.py`
- **Total lines:** 3
- **File size:** 161 bytes

## Line Type Summary
- **Code:** 0
- **Comment:** 0
- **Empty:** 0
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add alert rule for ingestion stalls`
> **Type:** TODO: high - Add alert rule for ingestion stalls

### Line   2
> **Code:** `# TODO: medium - Implement dashboard for drift detection`
> **Type:** TODO: medium - Implement dashboard for drift detection

### Line   3
> **Code:** `# TODO: low - Add prediction distribution monitoring`
> **Type:** TODO: low - Add prediction distribution monitoring

## Summary
- **Total lines:** 3
- **Code lines:** 0
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 0

---
*Documentation generated for: mlops-platform-spec*
*File: __init__.py*
---

# mlops-platform-spec: retraining_trigger.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/monitoring/retraining_trigger.py`
- **Total lines:** 77
- **File size:** 2622 bytes

## Line Type Summary
- **Code:** 56
- **Comment:** 0
- **Empty:** 18
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add alert rule for ingestion stalls`
> **Type:** TODO: high - Add alert rule for ingestion stalls

### Line   2
> **Code:** `# TODO: medium - Implement dashboard for drift detection`
> **Type:** TODO: medium - Implement dashboard for drift detection

### Line   3
> **Code:** `# TODO: low - Add prediction distribution monitoring`
> **Type:** TODO: low - Add prediction distribution monitoring

### Line   4
> **Code:** `"""Drift-driven automatic retraining trigger for the credit risk pipel...`
> **Type:** Arithmetic operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Reads ml/data/monitoring/drift_report.json; when the drift score excee...`
> **Type:** Arithmetic operation

### Line   7
> **Code:** `threshold it launches an automatic retrain (ml/train.py) followed by t...`
> **Type:** Arithmetic operation

### Line   8
> **Code:** `promotion-gate evaluation (ml/evaluate.py). Human sign-off still gates...`
> **Type:** Arithmetic operation

### Line   9
> **Code:** `Staging -> Production promotion, so automation never bypasses approval...`
> **Type:** Arithmetic operation

### Line  10
> **Code:** `"""`
> **Type:** Code statement

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `from __future__ import annotations`
> **Type:** Imports specific names from a module

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `import argparse`
> **Type:** Imports a module

### Line  15
> **Code:** `import json`
> **Type:** Imports a module

### Line  16
> **Code:** `import logging`
> **Type:** Imports a module

### Line  17
> **Code:** `import os`
> **Type:** Imports a module

### Line  18
> **Code:** `import subprocess`
> **Type:** Imports a module

### Line  19
> **Code:** `import sys`
> **Type:** Imports a module

### Line  20
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `logger = logging.getLogger(__name__)`
> **Type:** Assignment/comparison

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `_REPO_ROOT = Path(__file__).resolve().parents[2]`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `REPORT_PATH = _REPO_ROOT / "ml" / "data" / "monitoring" / "drift_repor...`
> **Type:** Assignment/comparison

### Line  26
> **Code:** `DEFAULT_THRESHOLD = 0.3`
> **Type:** Assignment/comparison

### Line  27
> **Code:** ``
> **Type:** Empty line

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** `def read_drift_report(path: Path = REPORT_PATH) -> dict:`
> **Type:** Function definition

### Line  30
> **Code:** `if not path.exists():`
> **Type:** Conditional statement

### Line  31
> **Code:** `return {"drift_score": 0.0, "threshold": DEFAULT_THRESHOLD, "drift_det...`
> **Type:** Returns a value from a function

### Line  32
> **Code:** `return json.loads(path.read_text())`
> **Type:** Returns a value from a function

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** ``
> **Type:** Empty line

### Line  35
> **Code:** `def should_retrain(report: dict, threshold: float | None = None) -> bo...`
> **Type:** Function definition

### Line  36
> **Code:** `score = float(report.get("drift_score", 0.0))`
> **Type:** Assignment/comparison

### Line  37
> **Code:** `thr = threshold if threshold is not None else float(`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `os.environ.get("DRIFT_THRESHOLD", report.get("threshold", DEFAULT_THRE...`
> **Type:** Logical operation

### Line  39
> **Code:** `)`
> **Type:** Code statement

### Line  40
> **Code:** `return score > thr`
> **Type:** Returns a value from a function

### Line  41
> **Code:** ``
> **Type:** Empty line

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `def trigger_retraining(dry_run: bool = False) -> dict:`
> **Type:** Function definition

### Line  44
> **Code:** `report = read_drift_report()`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `score = float(report.get("drift_score", 0.0))`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `threshold = float(report.get("threshold", DEFAULT_THRESHOLD))`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `trigger = should_retrain(report)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `logger.info("Drift score=%.3f threshold=%.3f trigger=%s", score, thres...`
> **Type:** Assignment/comparison

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** `if trigger and not dry_run:`
> **Type:** Conditional statement

### Line  51
> **Code:** `_launch_retraining()`
> **Type:** Function call

### Line  52
> **Code:** `return {`
> **Type:** Returns a value from a function

### Line  53
> **Code:** `"drift_score": score,`
> **Type:** Logical operation

### Line  54
> **Code:** `"threshold": threshold,`
> **Type:** Code statement

### Line  55
> **Code:** `"triggered": trigger,`
> **Type:** Code statement

### Line  56
> **Code:** `"dry_run": dry_run,`
> **Type:** Code statement

### Line  57
> **Code:** `"drifted_features": report.get("drifted_features", []),`
> **Type:** Logical operation

### Line  58
> **Code:** `}`
> **Type:** Code statement

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** ``
> **Type:** Empty line

### Line  61
> **Code:** `def _launch_retraining() -> None:`
> **Type:** Function definition

### Line  62
> **Code:** `for script in ["ml/train.py", "ml/evaluate.py"]:`
> **Type:** For loop

### Line  63
> **Code:** `cmd = [sys.executable, script]`
> **Type:** Assignment/comparison

### Line  64
> **Code:** `logger.info("AUTOMATED_RETRAINING -> %s", " ".join(cmd))`
> **Type:** Arithmetic operation

### Line  65
> **Code:** `subprocess.run(cmd, cwd=_REPO_ROOT, check=False)`
> **Type:** Assignment/comparison

### Line  66
> **Code:** ``
> **Type:** Empty line

### Line  67
> **Code:** ``
> **Type:** Empty line

### Line  68
> **Code:** `def main() -> None:`
> **Type:** Function definition

### Line  69
> **Code:** `logging.basicConfig(level=logging.INFO)`
> **Type:** Assignment/comparison

### Line  70
> **Code:** `parser = argparse.ArgumentParser(description="Drift-based retraining t...`
> **Type:** Assignment/comparison

### Line  71
> **Code:** `parser.add_argument("--dry-run", action="store_true", help="Only repor...`
> **Type:** Assignment/comparison

### Line  72
> **Code:** `args = parser.parse_args()`
> **Type:** Assignment/comparison

### Line  73
> **Code:** `print(json.dumps(trigger_retraining(dry_run=args.dry_run), indent=2))`
> **Type:** Prints output to console

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** ``
> **Type:** Empty line

### Line  76
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  77
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 77
- **Code lines:** 56
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 18

---
*Documentation generated for: mlops-platform-spec*
*File: retraining_trigger.py*
---

# mlops-platform-spec: __init__.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/data/__init__.py`
- **Total lines:** 4
- **File size:** 213 bytes

## Line Type Summary
- **Code:** 1
- **Comment:** 0
- **Empty:** 0
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Credit risk data — German Credit Data (UCI Statlog) for model train...`
> **Type:** Logical operation

## Summary
- **Total lines:** 4
- **Code lines:** 1
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 0

---
*Documentation generated for: mlops-platform-spec*
*File: __init__.py*
---

# mlops-platform-spec: generate_fraud_data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/data/generate_fraud_data.py`
- **Total lines:** 142
- **File size:** 4624 bytes

## Line Type Summary
- **Code:** 101
- **Comment:** 11
- **Empty:** 27
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   3
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   4
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   5
> **Code:** `"""Generate realistic synthetic credit card fraud transaction data.`
> **Type:** Code statement

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Produces 100K transactions with ~10% fraud rate.`
> **Type:** Arithmetic operation

### Line   8
> **Code:** `Fraud follows clear patterns: high amounts + unusual hours + internati...`
> **Type:** Arithmetic operation

### Line   9
> **Code:** `new cards + high transaction frequency.`
> **Type:** Arithmetic operation

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `Output: ml/data/fraud.csv`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `Deterministic (seed=42) for reproducibility.`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `"""`
> **Type:** Code statement

### Line  14
> **Code:** `import argparse`
> **Type:** Imports a module

### Line  15
> **Code:** `import os`
> **Type:** Imports a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  18
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `RNG = np.random.default_rng(42)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `N_ROWS = 100_000`
> **Type:** Assignment/comparison

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** `OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fra...`
> **Type:** Assignment/comparison

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `MERCHANT_CATEGORIES = [`
> **Type:** Assignment/comparison

### Line  26
> **Code:** `"grocery", "restaurant", "gas_station", "online_retail",`
> **Type:** Code statement

### Line  27
> **Code:** `"electronics", "jewelry", "travel", "entertainment",`
> **Type:** Code statement

### Line  28
> **Code:** `"pharmacy", "clothing", "hardware", "education",`
> **Type:** Code statement

### Line  29
> **Code:** `]`
> **Type:** Code statement

### Line  30
> **Code:** ``
> **Type:** Empty line

### Line  31
> **Code:** `CATEGORY_FRAUD_MULT = {`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `"online_retail": 2.0, "jewelry": 3.0, "electronics": 2.0,`
> **Type:** Code statement

### Line  33
> **Code:** `"travel": 2.5, "entertainment": 1.5, "grocery": 0.3,`
> **Type:** Code statement

### Line  34
> **Code:** `"restaurant": 0.4, "gas_station": 0.5, "pharmacy": 0.6,`
> **Type:** Code statement

### Line  35
> **Code:** `"clothing": 0.7, "hardware": 0.5, "education": 0.2,`
> **Type:** Code statement

### Line  36
> **Code:** `}`
> **Type:** Code statement

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `def generate(n_rows: int = N_ROWS) -> pd.DataFrame:`
> **Type:** Function definition

### Line  40
> **Code:** `rows = []`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `for i in range(n_rows):`
> **Type:** For loop

### Line  42
> **Code:** `txn_amount = float(RNG.lognormal(3.5, 1.2))`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `merchant_category = RNG.choice(MERCHANT_CATEGORIES)`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `hour_of_day = int(RNG.integers(0, 24))`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `day_of_week = int(RNG.integers(0, 7))`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `distance_from_home = float(RNG.exponential(15))`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `is_international = int(RNG.random() < 0.08)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `card_age_days = int(RNG.integers(1, 2000))`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `num_transactions_24h = int(RNG.poisson(3))`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `avg_transaction_amount_30d = float(RNG.lognormal(3.2, 0.8))`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `is_weekend = int(day_of_week >= 5)`
> **Type:** Assignment/comparison

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `# --- Fraud probability: strong correlated signal ---`
> **Type:** Comment: --- Fraud probability: strong correlated signal ---

### Line  54
> **Code:** `p_fraud = 0.005  # base`
> **Type:** Assignment/comparison

### Line  55
> **Code:** ``
> **Type:** Empty line

### Line  56
> **Code:** `# High amount is the strongest signal`
> **Type:** Comment: High amount is the strongest signal

### Line  57
> **Code:** `if txn_amount > 500:`
> **Type:** Conditional statement

### Line  58
> **Code:** `p_fraud += 0.15`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `elif txn_amount > 200:`
> **Type:** Else-if branch

### Line  60
> **Code:** `p_fraud += 0.08`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `elif txn_amount > 100:`
> **Type:** Else-if branch

### Line  62
> **Code:** `p_fraud += 0.03`
> **Type:** Assignment/comparison

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `# Night hours (10pm-5am)`
> **Type:** Comment: Night hours (10pm-5am)

### Line  65
> **Code:** `if hour_of_day >= 22 or hour_of_day <= 5:`
> **Type:** Conditional statement

### Line  66
> **Code:** `p_fraud += 0.10`
> **Type:** Assignment/comparison

### Line  67
> **Code:** ``
> **Type:** Empty line

### Line  68
> **Code:** `# International`
> **Type:** Comment: International

### Line  69
> **Code:** `if is_international:`
> **Type:** Conditional statement

### Line  70
> **Code:** `p_fraud += 0.12`
> **Type:** Assignment/comparison

### Line  71
> **Code:** ``
> **Type:** Empty line

### Line  72
> **Code:** `# New card`
> **Type:** Comment: New card

### Line  73
> **Code:** `if card_age_days < 90:`
> **Type:** Conditional statement

### Line  74
> **Code:** `p_fraud += 0.10`
> **Type:** Assignment/comparison

### Line  75
> **Code:** `elif card_age_days < 180:`
> **Type:** Else-if branch

### Line  76
> **Code:** `p_fraud += 0.04`
> **Type:** Assignment/comparison

### Line  77
> **Code:** ``
> **Type:** Empty line

### Line  78
> **Code:** `# High transaction frequency`
> **Type:** Comment: High transaction frequency

### Line  79
> **Code:** `if num_transactions_24h >= 10:`
> **Type:** Conditional statement

### Line  80
> **Code:** `p_fraud += 0.12`
> **Type:** Assignment/comparison

### Line  81
> **Code:** `elif num_transactions_24h >= 7:`
> **Type:** Else-if branch

### Line  82
> **Code:** `p_fraud += 0.08`
> **Type:** Assignment/comparison

### Line  83
> **Code:** `elif num_transactions_24h >= 5:`
> **Type:** Else-if branch

### Line  84
> **Code:** `p_fraud += 0.04`
> **Type:** Assignment/comparison

### Line  85
> **Code:** ``
> **Type:** Empty line

### Line  86
> **Code:** `# Amount way above average`
> **Type:** Comment: Amount way above average

### Line  87
> **Code:** `if avg_transaction_amount_30d > 0 and txn_amount > 5 * avg_transaction...`
> **Type:** Conditional statement

### Line  88
> **Code:** `p_fraud += 0.15`
> **Type:** Assignment/comparison

### Line  89
> **Code:** `elif avg_transaction_amount_30d > 0 and txn_amount > 3 * avg_transacti...`
> **Type:** Else-if branch

### Line  90
> **Code:** `p_fraud += 0.08`
> **Type:** Assignment/comparison

### Line  91
> **Code:** ``
> **Type:** Empty line

### Line  92
> **Code:** `# Long distance`
> **Type:** Comment: Long distance

### Line  93
> **Code:** `if distance_from_home > 50:`
> **Type:** Conditional statement

### Line  94
> **Code:** `p_fraud += 0.06`
> **Type:** Assignment/comparison

### Line  95
> **Code:** `elif distance_from_home > 25:`
> **Type:** Else-if branch

### Line  96
> **Code:** `p_fraud += 0.03`
> **Type:** Assignment/comparison

### Line  97
> **Code:** ``
> **Type:** Empty line

### Line  98
> **Code:** `# Category modifier`
> **Type:** Comment: Category modifier

### Line  99
> **Code:** `p_fraud *= CATEGORY_FRAUD_MULT.get(merchant_category, 1.0)`
> **Type:** Assignment/comparison

### Line 100
> **Code:** ``
> **Type:** Empty line

### Line 101
> **Code:** `# Weekend`
> **Type:** Comment: Weekend

### Line 102
> **Code:** `if is_weekend:`
> **Type:** Conditional statement

### Line 103
> **Code:** `p_fraud *= 1.15`
> **Type:** Assignment/comparison

### Line 104
> **Code:** ``
> **Type:** Empty line

### Line 105
> **Code:** `p_fraud = min(max(p_fraud, 0.001), 0.95)`
> **Type:** Assignment/comparison

### Line 106
> **Code:** `is_fraud = int(RNG.random() < p_fraud)`
> **Type:** Assignment/comparison

### Line 107
> **Code:** ``
> **Type:** Empty line

### Line 108
> **Code:** `rows.append({`
> **Type:** Code statement

### Line 109
> **Code:** `"transaction_id": f"TXN-{i:08d}",`
> **Type:** Arithmetic operation

### Line 110
> **Code:** `"transaction_amount": round(txn_amount, 2),`
> **Type:** Code statement

### Line 111
> **Code:** `"merchant_category": merchant_category,`
> **Type:** Logical operation

### Line 112
> **Code:** `"hour_of_day": hour_of_day,`
> **Type:** Code statement

### Line 113
> **Code:** `"day_of_week": day_of_week,`
> **Type:** Code statement

### Line 114
> **Code:** `"distance_from_home": round(distance_from_home, 2),`
> **Type:** Code statement

### Line 115
> **Code:** `"is_international": is_international,`
> **Type:** Code statement

### Line 116
> **Code:** `"card_age_days": card_age_days,`
> **Type:** Code statement

### Line 117
> **Code:** `"num_transactions_24h": num_transactions_24h,`
> **Type:** Code statement

### Line 118
> **Code:** `"avg_transaction_amount_30d": round(avg_transaction_amount_30d, 2),`
> **Type:** Code statement

### Line 119
> **Code:** `"is_weekend": is_weekend,`
> **Type:** Code statement

### Line 120
> **Code:** `"is_fraud": is_fraud,`
> **Type:** Code statement

### Line 121
> **Code:** `})`
> **Type:** Code statement

### Line 122
> **Code:** ``
> **Type:** Empty line

### Line 123
> **Code:** `df = pd.DataFrame(rows)`
> **Type:** Assignment/comparison

### Line 124
> **Code:** `return df`
> **Type:** Returns a value from a function

### Line 125
> **Code:** ``
> **Type:** Empty line

### Line 126
> **Code:** ``
> **Type:** Empty line

### Line 127
> **Code:** `def main():`
> **Type:** Function definition

### Line 128
> **Code:** `parser = argparse.ArgumentParser(description="Generate fraud detection...`
> **Type:** Assignment/comparison

### Line 129
> **Code:** `parser.add_argument("-n", "--rows", type=int, default=N_ROWS)`
> **Type:** Assignment/comparison

### Line 130
> **Code:** `parser.add_argument("-o", "--output", default=OUTPUT)`
> **Type:** Assignment/comparison

### Line 131
> **Code:** `args = parser.parse_args()`
> **Type:** Assignment/comparison

### Line 132
> **Code:** ``
> **Type:** Empty line

### Line 133
> **Code:** `df = generate(args.rows)`
> **Type:** Assignment/comparison

### Line 134
> **Code:** `df.to_csv(args.output, index=False)`
> **Type:** Assignment/comparison

### Line 135
> **Code:** `rate = df["is_fraud"].mean() * 100`
> **Type:** Assignment/comparison

### Line 136
> **Code:** `print(f"Wrote {len(df):,} rows -> {args.output}")`
> **Type:** Prints output to console

### Line 137
> **Code:** `print(f"  fraud={df['is_fraud'].sum():,} ({rate:.1f}%)")`
> **Type:** Prints output to console

### Line 138
> **Code:** `print(f"  features: {[c for c in df.columns if c not in ('transaction_...`
> **Type:** Prints output to console

### Line 139
> **Code:** ``
> **Type:** Empty line

### Line 140
> **Code:** ``
> **Type:** Empty line

### Line 141
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line 142
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 142
- **Code lines:** 101
- **Comments:** 11
- **TODO items:** 3
- **Empty lines:** 27

---
*Documentation generated for: mlops-platform-spec*
*File: generate_fraud_data.py*
---

# mlops-platform-spec: generate_credit_data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/ml/data/generate_credit_data.py`
- **Total lines:** 74
- **File size:** 2669 bytes

## Line Type Summary
- **Code:** 55
- **Comment:** 1
- **Empty:** 15
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   3
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   4
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   5
> **Code:** `"""Load German Credit Data (UCI Statlog) and write ml/data/credit.csv.`
> **Type:** Arithmetic operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `The raw ``german.data`` file is not redistributed with this repository...`
> **Type:** Logical operation

### Line   8
> **Code:** `GERMAN_DATA_PATH at a local copy (downloadable from the UCI Statlog Ge...`
> **Type:** Code statement

### Line   9
> **Code:** `Credit Data set) before running this script.`
> **Type:** Logical operation

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `Features: 13 categorical (A-codes), 8 numeric`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `Target: 1=good (repaid), 2=bad (default) -> map to 0/1 (1=default)`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `Output: ml/data/credit.csv (1000 rows, ~30% default rate)`
> **Type:** Arithmetic operation

### Line  14
> **Code:** `Deterministic seed for reproducibility.`
> **Type:** Logical operation

### Line  15
> **Code:** `"""`
> **Type:** Code statement

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `import os`
> **Type:** Imports a module

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  20
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `RNG = np.random.default_rng(42)`
> **Type:** Assignment/comparison

### Line  23
> **Code:** `DATA_SOURCE = os.getenv("GERMAN_DATA_PATH", "/tmp/realdata/german.data...`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cre...`
> **Type:** Assignment/comparison

### Line  25
> **Code:** ``
> **Type:** Empty line

### Line  26
> **Code:** `COLUMN_NAMES = [`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `"checking_status", "duration", "credit_history", "purpose", "credit_am...`
> **Type:** Logical operation

### Line  28
> **Code:** `"savings_status", "employment", "installment_rate", "personal_status",`
> **Type:** Code statement

### Line  29
> **Code:** `"other_parties", "residence_since", "property_magnitude", "age",`
> **Type:** Code statement

### Line  30
> **Code:** `"other_payment_plans", "housing", "existing_credits", "job",`
> **Type:** Code statement

### Line  31
> **Code:** `"num_dependents", "own_telephone", "foreign_worker", "target"`
> **Type:** Logical operation

### Line  32
> **Code:** `]`
> **Type:** Code statement

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** `CATEGORICAL_COLS = [`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `"checking_status", "credit_history", "purpose", "savings_status",`
> **Type:** Logical operation

### Line  36
> **Code:** `"employment", "personal_status", "other_parties", "property_magnitude"...`
> **Type:** Code statement

### Line  37
> **Code:** `"other_payment_plans", "housing", "job", "own_telephone", "foreign_wor...`
> **Type:** Logical operation

### Line  38
> **Code:** `]`
> **Type:** Code statement

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** `NUMERIC_COLS = [`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `"duration", "credit_amount", "installment_rate", "residence_since",`
> **Type:** Code statement

### Line  42
> **Code:** `"age", "existing_credits", "num_dependents"`
> **Type:** Code statement

### Line  43
> **Code:** `]`
> **Type:** Code statement

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** `def load_german_data() -> pd.DataFrame:`
> **Type:** Function definition

### Line  47
> **Code:** `if not os.path.exists(DATA_SOURCE):`
> **Type:** Conditional statement

### Line  48
> **Code:** `raise SystemExit(`
> **Type:** Raises an exception

### Line  49
> **Code:** `f"Raw German Credit data not found at {DATA_SOURCE}.\n"`
> **Type:** Logical operation

### Line  50
> **Code:** `"Download the UCI Statlog German Credit Data set and set "`
> **Type:** Logical operation

### Line  51
> **Code:** `"GERMAN_DATA_PATH to the local 'german.data' file."`
> **Type:** Code statement

### Line  52
> **Code:** `)`
> **Type:** Code statement

### Line  53
> **Code:** `df = pd.read_csv(DATA_SOURCE, sep=r"\s+", header=None, names=COLUMN_NA...`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `df["target"] = (df["target"] == 2).astype(int)`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `return df`
> **Type:** Returns a value from a function

### Line  56
> **Code:** ``
> **Type:** Empty line

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `def main():`
> **Type:** Function definition

### Line  59
> **Code:** `import argparse`
> **Type:** Imports a module

### Line  60
> **Code:** `parser = argparse.ArgumentParser(description="Load German Credit Data"...`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `parser.add_argument("-o", "--output", default=OUTPUT)`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `args = parser.parse_args()`
> **Type:** Assignment/comparison

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `df = load_german_data()`
> **Type:** Assignment/comparison

### Line  65
> **Code:** `df.to_csv(args.output, index=False)`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `rate = df["target"].mean() * 100`
> **Type:** Assignment/comparison

### Line  67
> **Code:** `print(f"Wrote {len(df):,} rows -> {args.output}")`
> **Type:** Prints output to console

### Line  68
> **Code:** `print(f"  default={df['target'].sum():,} ({rate:.1f}%)")`
> **Type:** Prints output to console

### Line  69
> **Code:** `print(f"  Categorical: {len(CATEGORICAL_COLS)}")`
> **Type:** Prints output to console

### Line  70
> **Code:** `print(f"  Numeric: {len(NUMERIC_COLS)}")`
> **Type:** Prints output to console

### Line  71
> **Code:** ``
> **Type:** Empty line

### Line  72
> **Code:** ``
> **Type:** Empty line

### Line  73
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  74
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 74
- **Code lines:** 55
- **Comments:** 1
- **TODO items:** 3
- **Empty lines:** 15

---
*Documentation generated for: mlops-platform-spec*
*File: generate_credit_data.py*
---

# mlops-platform-spec: conftest.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/conftest.py`
- **Total lines:** 27
- **File size:** 959 bytes

## Line Type Summary
- **Code:** 19
- **Comment:** 0
- **Empty:** 5
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Pytest bootstrap for the mlops-platform-spec repo.`
> **Type:** Arithmetic operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Adds the repo root, api/, and ml/ to sys.path so that production modul...`
> **Type:** Arithmetic operation

### Line   7
> **Code:** `can be imported both as packages (``import api.main``) and as top-leve...`
> **Type:** Arithmetic operation

### Line   8
> **Code:** `modules (``import db``, ``import train``, ``import preprocess``) the w...`
> **Type:** Logical operation

### Line   9
> **Code:** `backend code imports them.`
> **Type:** Logical operation

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `When run from the repo root, ``import api.main`` works because ``api/`...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `inserted first. ``ml/`` is inserted so that api/model.py, ml/train.py ...`
> **Type:** Arithmetic operation

### Line  13
> **Code:** `ml/evaluate.py can do ``from preprocess import ...``.`
> **Type:** Arithmetic operation

### Line  14
> **Code:** `"""`
> **Type:** Code statement

### Line  15
> **Code:** `import sys`
> **Type:** Imports a module

### Line  16
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `ROOT = Path(__file__).resolve().parents[1]`
> **Type:** Assignment/comparison

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `for subdir in ("api", "ml"):`
> **Type:** For loop

### Line  21
> **Code:** `path = str(ROOT / subdir)`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `if path not in sys.path:`
> **Type:** Conditional statement

### Line  23
> **Code:** `sys.path.insert(0, path)`
> **Type:** Function call

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `for path in (str(ROOT), str(ROOT / "tests")):`
> **Type:** For loop

### Line  26
> **Code:** `if path not in sys.path:`
> **Type:** Conditional statement

### Line  27
> **Code:** `sys.path.insert(0, path)`
> **Type:** Function call

## Summary
- **Total lines:** 27
- **Code lines:** 19
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 5

---
*Documentation generated for: mlops-platform-spec*
*File: conftest.py*
---

# mlops-platform-spec: test_train_pipeline.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/test_train_pipeline.py`
- **Total lines:** 63
- **File size:** 2201 bytes

## Line Type Summary
- **Code:** 44
- **Comment:** 2
- **Empty:** 14
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add data validation before training`
> **Type:** TODO: high - Add data validation before training

### Line   2
> **Code:** `# TODO: medium - Implement hyperparameter logging`
> **Type:** TODO: medium - Implement hyperparameter logging

### Line   3
> **Code:** `# TODO: low - Add model explainability integration`
> **Type:** TODO: low - Add model explainability integration

### Line   4
> **Code:** `"""Tests for the credit risk training pipeline."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line   9
> **Code:** `import pytest`
> **Type:** Imports a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))`
> **Type:** Arithmetic operation

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** `import train`
> **Type:** Imports a module

### Line  14
> **Code:** `import preprocess`
> **Type:** Imports a module

### Line  15
> **Code:** `from _data import build_subset_df`
> **Type:** Imports specific names from a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `class TestTrain:`
> **Type:** Class definition

### Line  19
> **Code:** `def test_train_end_to_end(self, tmp_path, monkeypatch):`
> **Type:** Function definition

### Line  20
> **Code:** `"""Full pipeline: train -> register -> save artifact."""`
> **Type:** Arithmetic operation

### Line  21
> **Code:** `mlruns = str(tmp_path / "mlruns")`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `monkeypatch.setenv("MLFLOW_TRACKING_URI", f"file://{mlruns}")`
> **Type:** Arithmetic operation

### Line  23
> **Code:** `monkeypatch.setenv("MLFLOW_ALLOW_FILE_STORE", "true")`
> **Type:** Function call

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `# PATCH the module-level constant (already evaluated at import time)`
> **Type:** Comment: PATCH the module-level constant (already evaluated at import time)

### Line  26
> **Code:** `monkeypatch.setattr(train, "TRACKING_URI", f"file://{mlruns}")`
> **Type:** Arithmetic operation

### Line  27
> **Code:** ``
> **Type:** Empty line

### Line  28
> **Code:** `df = build_subset_df(500)`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `monkeypatch.setattr(preprocess, "load_data", lambda: df)`
> **Type:** Function call

### Line  30
> **Code:** `monkeypatch.setattr(train, "load_data", lambda: df)`
> **Type:** Function call

### Line  31
> **Code:** `monkeypatch.setattr(train, "_REPO_ROOT", str(tmp_path))`
> **Type:** Function call

### Line  32
> **Code:** ``
> **Type:** Empty line

### Line  33
> **Code:** `# Ensure ml/ subdir exists for model.pkl save`
> **Type:** Comment: Ensure ml/ subdir exists for model.pkl save

### Line  34
> **Code:** `(tmp_path / "ml").mkdir(exist_ok=True)`
> **Type:** Assignment/comparison

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** `train.main()`
> **Type:** Function call

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `model_pkl = tmp_path / "ml" / "model.pkl"`
> **Type:** Assignment/comparison

### Line  39
> **Code:** `assert model_pkl.exists()`
> **Type:** Enforces a condition

### Line  40
> **Code:** `assert model_pkl.stat().st_size > 0`
> **Type:** Enforces a condition

### Line  41
> **Code:** ``
> **Type:** Empty line

### Line  42
> **Code:** `client = mlflow.tracking.MlflowClient(f"file://{mlruns}")`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `versions = client.get_latest_versions("credit-risk-model", stages=["St...`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `assert versions, "credit-risk-model not registered"`
> **Type:** Enforces a condition

### Line  45
> **Code:** `assert versions[0].name == "credit-risk-model"`
> **Type:** Enforces a condition

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `run = client.get_run(versions[0].run_id)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `assert "roc_auc" in run.data.metrics`
> **Type:** Enforces a condition

### Line  49
> **Code:** `assert "ks" in run.data.metrics`
> **Type:** Enforces a condition

### Line  50
> **Code:** ``
> **Type:** Empty line

### Line  51
> **Code:** `def test_compute_ks(self):`
> **Type:** Function definition

### Line  52
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  53
> **Code:** `y_true = [0, 0, 1, 1]`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `y_prob = [0.1, 0.4, 0.6, 0.9]`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `ks = train.compute_ks(y_true, y_prob)`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `assert 0.0 <= ks <= 1.0`
> **Type:** Enforces a condition

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `def test_preprocess_encode_features(self):`
> **Type:** Function definition

### Line  59
> **Code:** `df = build_subset_df(100)`
> **Type:** Assignment/comparison

### Line  60
> **Code:** `X, y = preprocess.encode_features(df)`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `assert len(X) == 100`
> **Type:** Enforces a condition

### Line  62
> **Code:** `assert len(y) == 100`
> **Type:** Enforces a condition

### Line  63
> **Code:** `assert set(y.unique()).issubset({0, 1})`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 63
- **Code lines:** 44
- **Comments:** 2
- **TODO items:** 3
- **Empty lines:** 14

---
*Documentation generated for: mlops-platform-spec*
*File: test_train_pipeline.py*
---

# mlops-platform-spec: test_evaluate.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/test_evaluate.py`
- **Total lines:** 25
- **File size:** 755 bytes

## Line Type Summary
- **Code:** 16
- **Comment:** 0
- **Empty:** 6
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add quality gate with thresholds`
> **Type:** TODO: high - Add quality gate with thresholds

### Line   2
> **Code:** `# TODO: medium - Implement comparison vs current production model`
> **Type:** TODO: medium - Implement comparison vs current production model

### Line   3
> **Code:** `# TODO: low - Add metrics export for Evidence Pack`
> **Type:** TODO: low - Add metrics export for Evidence Pack

### Line   4
> **Code:** `"""Tests for the credit risk evaluation gate."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))`
> **Type:** Arithmetic operation

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `import evaluate`
> **Type:** Imports a module

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** ``
> **Type:** Empty line

### Line  15
> **Code:** `class TestEvaluateGate:`
> **Type:** Class definition

### Line  16
> **Code:** `def test_compute_ks(self):`
> **Type:** Function definition

### Line  17
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  18
> **Code:** `y_true = [0, 0, 1, 1, 0, 1, 0, 1]`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `y_prob = [0.1, 0.2, 0.7, 0.9, 0.3, 0.8, 0.15, 0.85]`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `ks = evaluate.compute_ks(y_true, y_prob)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `assert 0.0 <= ks <= 1.0`
> **Type:** Enforces a condition

### Line  22
> **Code:** `assert ks > 0.3  # good discrimination`
> **Type:** Enforces a condition

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `def test_auc_threshold_value(self):`
> **Type:** Function definition

### Line  25
> **Code:** `assert evaluate.AUC_THRESHOLD == 0.75`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 25
- **Code lines:** 16
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 6

---
*Documentation generated for: mlops-platform-spec*
*File: test_evaluate.py*
---

# mlops-platform-spec: test_schemas.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/test_schemas.py`
- **Total lines:** 62
- **File size:** 2166 bytes

## Line Type Summary
- **Code:** 48
- **Comment:** 0
- **Empty:** 11
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Tests for the credit risk API schemas."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** `from pydantic import ValidationError`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api")...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** `from schemas import PredictRequest, PredictResponse, HealthResponse`
> **Type:** Imports specific names from a module

### Line  14
> **Code:** ``
> **Type:** Empty line

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `class TestPredictRequest:`
> **Type:** Class definition

### Line  17
> **Code:** `def test_valid_request(self):`
> **Type:** Function definition

### Line  18
> **Code:** `r = PredictRequest(`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `age=35, income=65000, monthly_income=5416.67,`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `debt_ratio=0.35, revolving_utilization=45.2,`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `num_open_credit_lines=6, num_dependents=1,`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `num_30_59_days_late=0, num_60_89_days_late=0,`
> **Type:** Assignment/comparison

### Line  23
> **Code:** `num_90_days_late=0, num_mortgages=1,`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `number_real_estate_loans=1,`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `)`
> **Type:** Code statement

### Line  26
> **Code:** `assert r.age == 35`
> **Type:** Enforces a condition

### Line  27
> **Code:** `assert r.income == 65000`
> **Type:** Enforces a condition

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** `def test_rejects_age_below_18(self):`
> **Type:** Function definition

### Line  30
> **Code:** `with pytest.raises(ValidationError):`
> **Type:** Context manager

### Line  31
> **Code:** `PredictRequest(`
> **Type:** Code statement

### Line  32
> **Code:** `age=15, income=65000, monthly_income=5416.67,`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `debt_ratio=0.35, revolving_utilization=45.2,`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `num_open_credit_lines=6, num_dependents=1,`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `num_30_59_days_late=0, num_60_89_days_late=0,`
> **Type:** Assignment/comparison

### Line  36
> **Code:** `num_90_days_late=0, num_mortgages=1,`
> **Type:** Assignment/comparison

### Line  37
> **Code:** `number_real_estate_loans=1,`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `)`
> **Type:** Code statement

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** `def test_rejects_negative_income(self):`
> **Type:** Function definition

### Line  41
> **Code:** `with pytest.raises(ValidationError):`
> **Type:** Context manager

### Line  42
> **Code:** `PredictRequest(`
> **Type:** Code statement

### Line  43
> **Code:** `age=35, income=-100, monthly_income=5416.67,`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `debt_ratio=0.35, revolving_utilization=45.2,`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `num_open_credit_lines=6, num_dependents=1,`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `num_30_59_days_late=0, num_60_89_days_late=0,`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `num_90_days_late=0, num_mortgages=1,`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `number_real_estate_loans=1,`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `)`
> **Type:** Code statement

### Line  50
> **Code:** ``
> **Type:** Empty line

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `class TestPredictResponse:`
> **Type:** Class definition

### Line  53
> **Code:** `def test_valid_response(self):`
> **Type:** Function definition

### Line  54
> **Code:** `r = PredictResponse(prediction=1, probability=0.75, risk_tier="high")`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `assert r.prediction == 1`
> **Type:** Enforces a condition

### Line  56
> **Code:** `assert r.risk_tier == "high"`
> **Type:** Enforces a condition

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** ``
> **Type:** Empty line

### Line  59
> **Code:** `class TestHealthResponse:`
> **Type:** Class definition

### Line  60
> **Code:** `def test_default_status(self):`
> **Type:** Function definition

### Line  61
> **Code:** `h = HealthResponse()`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `assert h.status == "ok"`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 62
- **Code lines:** 48
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 11

---
*Documentation generated for: mlops-platform-spec*
*File: test_schemas.py*
---

# mlops-platform-spec: test_api.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/test_api.py`
- **Total lines:** 108
- **File size:** 3240 bytes

## Line Type Summary
- **Code:** 82
- **Comment:** 0
- **Empty:** 23
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Tests for the credit risk prediction API."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import sys`
> **Type:** Imports a module

### Line   6
> **Code:** `from pathlib import Path`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import pytest`
> **Type:** Imports a module

### Line   9
> **Code:** `from fastapi.testclient import TestClient`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api")...`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests...`
> **Type:** Arithmetic operation

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `import main`
> **Type:** Imports a module

### Line  15
> **Code:** `import model`
> **Type:** Imports a module

### Line  16
> **Code:** `from _data import build_subset_df`
> **Type:** Imports specific names from a module

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `from sklearn.ensemble import GradientBoostingClassifier`
> **Type:** Imports specific names from a module

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `import preprocess`
> **Type:** Imports a module

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `VALID_PAYLOAD = {`
> **Type:** Assignment/comparison

### Line  23
> **Code:** `"age": 35,`
> **Type:** Code statement

### Line  24
> **Code:** `"income": 65000.0,`
> **Type:** Code statement

### Line  25
> **Code:** `"monthly_income": 5416.67,`
> **Type:** Code statement

### Line  26
> **Code:** `"debt_ratio": 0.35,`
> **Type:** Code statement

### Line  27
> **Code:** `"revolving_utilization": 45.2,`
> **Type:** Code statement

### Line  28
> **Code:** `"num_open_credit_lines": 6,`
> **Type:** Code statement

### Line  29
> **Code:** `"num_dependents": 1,`
> **Type:** Code statement

### Line  30
> **Code:** `"num_30_59_days_late": 0,`
> **Type:** Code statement

### Line  31
> **Code:** `"num_60_89_days_late": 0,`
> **Type:** Code statement

### Line  32
> **Code:** `"num_90_days_late": 0,`
> **Type:** Code statement

### Line  33
> **Code:** `"num_mortgages": 1,`
> **Type:** Logical operation

### Line  34
> **Code:** `"number_real_estate_loans": 1,`
> **Type:** Code statement

### Line  35
> **Code:** `}`
> **Type:** Code statement

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `class FakeSession:`
> **Type:** Class definition

### Line  39
> **Code:** `def __init__(self):`
> **Type:** Function definition

### Line  40
> **Code:** `self.added = []`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `self.committed = 0`
> **Type:** Assignment/comparison

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** `def add(self, obj):`
> **Type:** Function definition

### Line  44
> **Code:** `self.added.append(obj)`
> **Type:** Function call

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** `def commit(self):`
> **Type:** Function definition

### Line  47
> **Code:** `self.committed += 1`
> **Type:** Assignment/comparison

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `def close(self):`
> **Type:** Function definition

### Line  50
> **Code:** `pass`
> **Type:** Code statement

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `def query(self, *a, **kw):`
> **Type:** Function definition

### Line  53
> **Code:** `return self`
> **Type:** Returns a value from a function

### Line  54
> **Code:** ``
> **Type:** Empty line

### Line  55
> **Code:** `def order_by(self, *a, **kw):`
> **Type:** Function definition

### Line  56
> **Code:** `return self`
> **Type:** Returns a value from a function

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `def limit(self, *a, **kw):`
> **Type:** Function definition

### Line  59
> **Code:** `return self`
> **Type:** Returns a value from a function

### Line  60
> **Code:** ``
> **Type:** Empty line

### Line  61
> **Code:** `def all(self):`
> **Type:** Function definition

### Line  62
> **Code:** `return []`
> **Type:** Returns a value from a function

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** ``
> **Type:** Empty line

### Line  65
> **Code:** `class TestHealth:`
> **Type:** Class definition

### Line  66
> **Code:** `def test_health_ok(self, monkeypatch):`
> **Type:** Function definition

### Line  67
> **Code:** `monkeypatch.setattr(main, "load_model", lambda: None)`
> **Type:** Function call

### Line  68
> **Code:** `monkeypatch.setattr(main, "init_db", lambda: None)`
> **Type:** Function call

### Line  69
> **Code:** `monkeypatch.setattr(main, "get_session", lambda: FakeSession())`
> **Type:** Function call

### Line  70
> **Code:** `monkeypatch.setattr(main, "get_model_version", lambda: "test-1.0")`
> **Type:** Arithmetic operation

### Line  71
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line  72
> **Code:** `r = c.get("/health")`
> **Type:** Assignment/comparison

### Line  73
> **Code:** `assert r.status_code == 200`
> **Type:** Enforces a condition

### Line  74
> **Code:** `body = r.json()`
> **Type:** Assignment/comparison

### Line  75
> **Code:** `assert body["status"] == "ok"`
> **Type:** Enforces a condition

### Line  76
> **Code:** `assert body["model_version"] == "test-1.0"`
> **Type:** Enforces a condition

### Line  77
> **Code:** ``
> **Type:** Empty line

### Line  78
> **Code:** ``
> **Type:** Empty line

### Line  79
> **Code:** `class TestPredict:`
> **Type:** Class definition

### Line  80
> **Code:** `def test_predict_returns_200_with_valid_payload(self, monkeypatch):`
> **Type:** Function definition

### Line  81
> **Code:** `df = build_subset_df()`
> **Type:** Assignment/comparison

### Line  82
> **Code:** `X, y = preprocess.encode_features(df)`
> **Type:** Assignment/comparison

### Line  83
> **Code:** `clf = GradientBoostingClassifier(n_estimators=20, random_state=42)`
> **Type:** Assignment/comparison

### Line  84
> **Code:** `clf.fit(X, y)`
> **Type:** Function call

### Line  85
> **Code:** ``
> **Type:** Empty line

### Line  86
> **Code:** `monkeypatch.setattr(main, "load_model", lambda: None)`
> **Type:** Function call

### Line  87
> **Code:** `monkeypatch.setattr(model, "_model", clf)`
> **Type:** Function call

### Line  88
> **Code:** `monkeypatch.setattr(model, "_model_version", "test-1.0")`
> **Type:** Arithmetic operation

### Line  89
> **Code:** `monkeypatch.setattr(main, "init_db", lambda: None)`
> **Type:** Function call

### Line  90
> **Code:** `monkeypatch.setattr(main, "get_session", lambda: FakeSession())`
> **Type:** Function call

### Line  91
> **Code:** ``
> **Type:** Empty line

### Line  92
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line  93
> **Code:** `r = c.post("/predict", json=VALID_PAYLOAD)`
> **Type:** Assignment/comparison

### Line  94
> **Code:** `assert r.status_code == 200`
> **Type:** Enforces a condition

### Line  95
> **Code:** `body = r.json()`
> **Type:** Assignment/comparison

### Line  96
> **Code:** `assert body["prediction"] in (0, 1)`
> **Type:** Enforces a condition

### Line  97
> **Code:** `assert isinstance(body["probability"], float)`
> **Type:** Enforces a condition

### Line  98
> **Code:** `assert 0.0 <= body["probability"] <= 1.0`
> **Type:** Enforces a condition

### Line  99
> **Code:** `assert body["risk_tier"] in ("low", "medium", "high", "critical")`
> **Type:** Enforces a condition

### Line 100
> **Code:** ``
> **Type:** Empty line

### Line 101
> **Code:** `def test_predict_422_on_missing_fields(self, monkeypatch):`
> **Type:** Function definition

### Line 102
> **Code:** `monkeypatch.setattr(main, "load_model", lambda: None)`
> **Type:** Function call

### Line 103
> **Code:** `monkeypatch.setattr(main, "init_db", lambda: None)`
> **Type:** Function call

### Line 104
> **Code:** `monkeypatch.setattr(main, "get_session", lambda: FakeSession())`
> **Type:** Function call

### Line 105
> **Code:** ``
> **Type:** Empty line

### Line 106
> **Code:** `with TestClient(main.app) as c:`
> **Type:** Context manager

### Line 107
> **Code:** `r = c.post("/predict", json={"age": 30})`
> **Type:** Assignment/comparison

### Line 108
> **Code:** `assert r.status_code == 422`
> **Type:** Enforces a condition

## Summary
- **Total lines:** 108
- **Code lines:** 82
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 23

---
*Documentation generated for: mlops-platform-spec*
*File: test_api.py*
---

# mlops-platform-spec: _data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/tests/_data.py`
- **Total lines:** 47
- **File size:** 1709 bytes

## Line Type Summary
- **Code:** 38
- **Comment:** 0
- **Empty:** 6
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Shared test data for the credit risk ML pipeline."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line   6
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `RNG = np.random.default_rng(99)`
> **Type:** Assignment/comparison

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `def build_subset_df(n: int = 500) -> pd.DataFrame:`
> **Type:** Function definition

### Line  12
> **Code:** `"""Build a small synthetic credit risk dataframe for tests."""`
> **Type:** Logical operation

### Line  13
> **Code:** `rows = []`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `for i in range(n):`
> **Type:** For loop

### Line  15
> **Code:** `age = int(RNG.integers(20, 70))`
> **Type:** Assignment/comparison

### Line  16
> **Code:** `income = float(RNG.lognormal(10.5, 0.8))`
> **Type:** Assignment/comparison

### Line  17
> **Code:** `monthly_income = income / 12`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `debt_ratio = float(np.clip(RNG.beta(2, 5), 0, 10))`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `util = float(np.clip(RNG.beta(3, 2) * 100, 0, 100))`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `late30 = int(RNG.poisson(0.2))`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `late60 = int(RNG.poisson(0.08))`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `late90 = int(RNG.poisson(0.03))`
> **Type:** Assignment/comparison

### Line  23
> **Code:** `credit_lines = int(RNG.poisson(5))`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `mortgages = int(RNG.poisson(0.7))`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `dependents = int(RNG.poisson(1))`
> **Type:** Assignment/comparison

### Line  26
> **Code:** ``
> **Type:** Empty line

### Line  27
> **Code:** `logit = -3.5 + 0.8 * late90 + 0.5 * late60 + 0.3 * late30 + 0.02 * (ut...`
> **Type:** Assignment/comparison

### Line  28
> **Code:** `p = 1 / (1 + np.exp(-logit))`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `default = int(RNG.random() < p)`
> **Type:** Assignment/comparison

### Line  30
> **Code:** ``
> **Type:** Empty line

### Line  31
> **Code:** `rows.append({`
> **Type:** Code statement

### Line  32
> **Code:** `"age": age,`
> **Type:** Code statement

### Line  33
> **Code:** `"income": round(income, 2),`
> **Type:** Code statement

### Line  34
> **Code:** `"monthly_income": round(monthly_income, 2),`
> **Type:** Code statement

### Line  35
> **Code:** `"debt_ratio": round(debt_ratio, 4),`
> **Type:** Code statement

### Line  36
> **Code:** `"revolving_utilization": round(util, 2),`
> **Type:** Code statement

### Line  37
> **Code:** `"num_open_credit_lines": credit_lines,`
> **Type:** Code statement

### Line  38
> **Code:** `"num_dependents": dependents,`
> **Type:** Code statement

### Line  39
> **Code:** `"num_30_59_days_late": late30,`
> **Type:** Code statement

### Line  40
> **Code:** `"num_60_89_days_late": late60,`
> **Type:** Code statement

### Line  41
> **Code:** `"num_90_days_late": late90,`
> **Type:** Code statement

### Line  42
> **Code:** `"num_mortgages": mortgages,`
> **Type:** Logical operation

### Line  43
> **Code:** `"number_real_estate_loans": mortgages,`
> **Type:** Logical operation

### Line  44
> **Code:** `"default": default,`
> **Type:** Code statement

### Line  45
> **Code:** `})`
> **Type:** Code statement

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `return pd.DataFrame(rows)`
> **Type:** Returns a value from a function

## Summary
- **Total lines:** 47
- **Code lines:** 38
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 6

---
*Documentation generated for: mlops-platform-spec*
*File: _data.py*
---

# mlops-platform-spec: db.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/api/db.py`
- **Total lines:** 49
- **File size:** 1630 bytes

## Line Type Summary
- **Code:** 33
- **Comment:** 0
- **Empty:** 13
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Database configuration and models for the churn prediction API."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import os`
> **Type:** Imports a module

### Line   6
> **Code:** `from datetime import datetime`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `from sqlalchemy import JSON, DateTime, Integer, String, create_engine,...`
> **Type:** Imports specific names from a module

### Line   9
> **Code:** `from sqlalchemy.orm import declarative_base, sessionmaker`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `Base = declarative_base()`
> **Type:** Assignment/comparison

### Line  12
> **Code:** ``
> **Type:** Empty line

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `class Prediction(Base):`
> **Type:** Class definition

### Line  15
> **Code:** `__tablename__ = "predictions"`
> **Type:** Assignment/comparison

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `id = Column(Integer, primary_key=True, index=True)`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `input_json = Column(JSON, nullable=False)`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `prediction = Column(Integer, nullable=False)`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `probability = Column(String(20), nullable=False)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `created_at = Column(DateTime, default=datetime.utcnow, nullable=False)`
> **Type:** Assignment/comparison

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `def get_database_url() -> str:`
> **Type:** Function definition

### Line  25
> **Code:** `"""Construct database URL from environment variables."""`
> **Type:** Code statement

### Line  26
> **Code:** `host = os.environ.get("DB_HOST", "postgres-service")`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `port = os.environ.get("DB_PORT", "5432")`
> **Type:** Assignment/comparison

### Line  28
> **Code:** `user = os.environ.get("DB_USER", "postgres")`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `password = os.environ.get("DB_PASSWORD", "postgres")`
> **Type:** Assignment/comparison

### Line  30
> **Code:** `database = os.environ.get("DB_NAME", "mlops")`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `return f"postgresql://{user}:{password}@{host}:{port}/{database}"`
> **Type:** Returns a value from a function

### Line  32
> **Code:** ``
> **Type:** Empty line

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** `def get_engine():`
> **Type:** Function definition

### Line  35
> **Code:** `"""Create and return SQLAlchemy engine."""`
> **Type:** Logical operation

### Line  36
> **Code:** `return create_engine(get_database_url(), pool_pre_ping=True)`
> **Type:** Returns a value from a function

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `def get_session():`
> **Type:** Function definition

### Line  40
> **Code:** `"""Create and return a database session."""`
> **Type:** Logical operation

### Line  41
> **Code:** `engine = get_engine()`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=en...`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `return SessionLocal()`
> **Type:** Returns a value from a function

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** `def init_db():`
> **Type:** Function definition

### Line  47
> **Code:** `"""Initialize the database tables."""`
> **Type:** Code statement

### Line  48
> **Code:** `engine = get_engine()`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `Base.metadata.create_all(bind=engine)`
> **Type:** Assignment/comparison

## Summary
- **Total lines:** 49
- **Code lines:** 33
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 13

---
*Documentation generated for: mlops-platform-spec*
*File: db.py*
---

# mlops-platform-spec: schemas.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/api/schemas.py`
- **Total lines:** 58
- **File size:** 2362 bytes

## Line Type Summary
- **Code:** 46
- **Comment:** 0
- **Empty:** 9
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Pydantic schemas for the credit risk prediction API."""`
> **Type:** Logical operation

### Line   5
> **Code:** `from pydantic import BaseModel, Field`
> **Type:** Imports specific names from a module

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `class PredictRequest(BaseModel):`
> **Type:** Class definition

### Line   9
> **Code:** `age: int = Field(..., ge=18, le=100, description="Applicant age")`
> **Type:** Assignment/comparison

### Line  10
> **Code:** `income: float = Field(..., ge=0, description="Annual income")`
> **Type:** Assignment/comparison

### Line  11
> **Code:** `monthly_income: float = Field(..., ge=0, description="Monthly income")`
> **Type:** Assignment/comparison

### Line  12
> **Code:** `debt_ratio: float = Field(..., ge=0, description="Total debt / total i...`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `revolving_utilization: float = Field(..., ge=0, le=100, description="C...`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `num_open_credit_lines: int = Field(..., ge=0, description="Number of o...`
> **Type:** Assignment/comparison

### Line  15
> **Code:** `num_dependents: int = Field(..., ge=0, le=20, description="Number of d...`
> **Type:** Assignment/comparison

### Line  16
> **Code:** `num_30_59_days_late: int = Field(..., ge=0, description="Times 30-59 d...`
> **Type:** Assignment/comparison

### Line  17
> **Code:** `num_60_89_days_late: int = Field(..., ge=0, description="Times 60-89 d...`
> **Type:** Assignment/comparison

### Line  18
> **Code:** `num_90_days_late: int = Field(..., ge=0, description="Times 90+ days p...`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `num_mortgages: int = Field(..., ge=0, description="Number of mortgage ...`
> **Type:** Assignment/comparison

### Line  20
> **Code:** `number_real_estate_loans: int = Field(..., ge=0, description="Number o...`
> **Type:** Assignment/comparison

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `class Config:`
> **Type:** Class definition

### Line  23
> **Code:** `json_schema_extra = {`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `"example": {`
> **Type:** Code statement

### Line  25
> **Code:** `"age": 35,`
> **Type:** Code statement

### Line  26
> **Code:** `"income": 65000.0,`
> **Type:** Code statement

### Line  27
> **Code:** `"monthly_income": 5416.67,`
> **Type:** Code statement

### Line  28
> **Code:** `"debt_ratio": 0.35,`
> **Type:** Code statement

### Line  29
> **Code:** `"revolving_utilization": 45.2,`
> **Type:** Code statement

### Line  30
> **Code:** `"num_open_credit_lines": 6,`
> **Type:** Code statement

### Line  31
> **Code:** `"num_dependents": 1,`
> **Type:** Code statement

### Line  32
> **Code:** `"num_30_59_days_late": 0,`
> **Type:** Code statement

### Line  33
> **Code:** `"num_60_89_days_late": 0,`
> **Type:** Code statement

### Line  34
> **Code:** `"num_90_days_late": 0,`
> **Type:** Code statement

### Line  35
> **Code:** `"num_mortgages": 1,`
> **Type:** Logical operation

### Line  36
> **Code:** `"number_real_estate_loans": 1,`
> **Type:** Code statement

### Line  37
> **Code:** `}`
> **Type:** Code statement

### Line  38
> **Code:** `}`
> **Type:** Code statement

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** ``
> **Type:** Empty line

### Line  41
> **Code:** `class PredictResponse(BaseModel):`
> **Type:** Class definition

### Line  42
> **Code:** `prediction: int = Field(..., description="0=Repaid, 1=Default")`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `probability: float = Field(..., description="Probability of default")`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `risk_tier: str = Field(..., description="Risk tier: low/medium/high/cr...`
> **Type:** Assignment/comparison

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `class HealthResponse(BaseModel):`
> **Type:** Class definition

### Line  48
> **Code:** `status: str = "ok"`
> **Type:** Assignment/comparison

### Line  49
> **Code:** `model_version: str | None = None`
> **Type:** Assignment/comparison

### Line  50
> **Code:** ``
> **Type:** Empty line

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `class PredictionRecord(BaseModel):`
> **Type:** Class definition

### Line  53
> **Code:** `id: int`
> **Type:** Code statement

### Line  54
> **Code:** `input_json: dict`
> **Type:** Code statement

### Line  55
> **Code:** `prediction: int`
> **Type:** Code statement

### Line  56
> **Code:** `probability: float`
> **Type:** Code statement

### Line  57
> **Code:** `risk_tier: str`
> **Type:** Code statement

### Line  58
> **Code:** `created_at: str`
> **Type:** Code statement

## Summary
- **Total lines:** 58
- **Code lines:** 46
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 9

---
*Documentation generated for: mlops-platform-spec*
*File: schemas.py*
---

# mlops-platform-spec: model.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/api/model.py`
- **Total lines:** 80
- **File size:** 2366 bytes

## Line Type Summary
- **Code:** 55
- **Comment:** 2
- **Empty:** 20
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Model loading and prediction logic for the credit risk prediction A...`
> **Type:** Logical operation

### Line   5
> **Code:** `import os`
> **Type:** Imports a module

### Line   6
> **Code:** `import sys`
> **Type:** Imports a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line   9
> **Code:** `import mlflow.sklearn`
> **Type:** Imports a module

### Line  10
> **Code:** `from mlflow.tracking import MlflowClient`
> **Type:** Imports specific names from a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file_...`
> **Type:** Assignment/comparison

### Line  13
> **Code:** `ML_DIR = os.path.join(PROJECT_ROOT, "ml")`
> **Type:** Assignment/comparison

### Line  14
> **Code:** `for _path in (PROJECT_ROOT, ML_DIR):`
> **Type:** For loop

### Line  15
> **Code:** `if _path not in sys.path:`
> **Type:** Conditional statement

### Line  16
> **Code:** `sys.path.insert(0, _path)`
> **Type:** Function call

### Line  17
> **Code:** ``
> **Type:** Empty line

### Line  18
> **Code:** `_model = None`
> **Type:** Assignment/comparison

### Line  19
> **Code:** `_model_version = None`
> **Type:** Assignment/comparison

### Line  20
> **Code:** ``
> **Type:** Empty line

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `def load_model():`
> **Type:** Function definition

### Line  23
> **Code:** `"""Load the registered model from MLflow on startup."""`
> **Type:** Code statement

### Line  24
> **Code:** `global _model, _model_version`
> **Type:** Code statement

### Line  25
> **Code:** ``
> **Type:** Empty line

### Line  26
> **Code:** `tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `model_name = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** `mlflow.set_tracking_uri(tracking_uri)`
> **Type:** Function call

### Line  30
> **Code:** `client = MlflowClient()`
> **Type:** Assignment/comparison

### Line  31
> **Code:** ``
> **Type:** Empty line

### Line  32
> **Code:** `try:`
> **Type:** Code statement

### Line  33
> **Code:** `versions = client.get_latest_versions(model_name, stages=["Production"...`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `if not versions:`
> **Type:** Conditional statement

### Line  35
> **Code:** `raise ValueError(f"No registered model found: {model_name}")`
> **Type:** Raises an exception

### Line  36
> **Code:** `version = versions[0]`
> **Type:** Assignment/comparison

### Line  37
> **Code:** `model_uri = f"models:/{model_name}/{version.version}"`
> **Type:** Assignment/comparison

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `_model = mlflow.sklearn.load_model(model_uri)`
> **Type:** Assignment/comparison

### Line  40
> **Code:** `_model_version = str(version.version)`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `print(f"Loaded model {model_name} version {_model_version} from {track...`
> **Type:** Prints output to console

### Line  42
> **Code:** `except Exception as e:`
> **Type:** Code statement

### Line  43
> **Code:** `print(f"ERROR loading model: {e}")`
> **Type:** Prints output to console

### Line  44
> **Code:** `raise`
> **Type:** Raises an exception

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** ``
> **Type:** Empty line

### Line  47
> **Code:** `def get_model_version() -> str | None:`
> **Type:** Function definition

### Line  48
> **Code:** `return _model_version`
> **Type:** Returns a value from a function

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** ``
> **Type:** Empty line

### Line  51
> **Code:** `def predict(input_data: dict) -> tuple[int, float]:`
> **Type:** Function definition

### Line  52
> **Code:** `"""Run prediction on input data and return (prediction, probability)."...`
> **Type:** Logical operation

### Line  53
> **Code:** `if _model is None:`
> **Type:** Conditional statement

### Line  54
> **Code:** `load_model()`
> **Type:** Function call

### Line  55
> **Code:** ``
> **Type:** Empty line

### Line  56
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `# API uses same field names as model (no mapping needed for credit ris...`
> **Type:** Comment: API uses same field names as model (no mapping needed for credit risk)

### Line  59
> **Code:** `df = pd.DataFrame([input_data])`
> **Type:** Assignment/comparison

### Line  60
> **Code:** ``
> **Type:** Empty line

### Line  61
> **Code:** `# Drop non-feature columns`
> **Type:** Comment: Drop non-feature columns

### Line  62
> **Code:** `for col in ("customer_id",):`
> **Type:** For loop

### Line  63
> **Code:** `if col in df.columns:`
> **Type:** Conditional statement

### Line  64
> **Code:** `df = df.drop(columns=[col])`
> **Type:** Assignment/comparison

### Line  65
> **Code:** ``
> **Type:** Empty line

### Line  66
> **Code:** `prediction = int(_model.predict(df)[0])`
> **Type:** Assignment/comparison

### Line  67
> **Code:** `probability = float(_model.predict_proba(df)[0][1])`
> **Type:** Assignment/comparison

### Line  68
> **Code:** ``
> **Type:** Empty line

### Line  69
> **Code:** `return prediction, probability`
> **Type:** Returns a value from a function

### Line  70
> **Code:** ``
> **Type:** Empty line

### Line  71
> **Code:** ``
> **Type:** Empty line

### Line  72
> **Code:** `def risk_tier(probability: float) -> str:`
> **Type:** Function definition

### Line  73
> **Code:** `if probability < 0.1:`
> **Type:** Conditional statement

### Line  74
> **Code:** `return "low"`
> **Type:** Returns a value from a function

### Line  75
> **Code:** `elif probability < 0.3:`
> **Type:** Else-if branch

### Line  76
> **Code:** `return "medium"`
> **Type:** Returns a value from a function

### Line  77
> **Code:** `elif probability < 0.6:`
> **Type:** Else-if branch

### Line  78
> **Code:** `return "high"`
> **Type:** Returns a value from a function

### Line  79
> **Code:** `else:`
> **Type:** Else block

### Line  80
> **Code:** `return "critical"`
> **Type:** Returns a value from a function

## Summary
- **Total lines:** 80
- **Code lines:** 55
- **Comments:** 2
- **TODO items:** 3
- **Empty lines:** 20

---
*Documentation generated for: mlops-platform-spec*
*File: model.py*
---

# mlops-platform-spec: main.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/api/main.py`
- **Total lines:** 75
- **File size:** 2299 bytes

## Line Type Summary
- **Code:** 54
- **Comment:** 0
- **Empty:** 18
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: high - Add request validation and error handling`
> **Type:** TODO: high - Add request validation and error handling

### Line   2
> **Code:** `# TODO: medium - Implement request/response logging`
> **Type:** TODO: medium - Implement request/response logging

### Line   3
> **Code:** `# TODO: low - Add health check endpoint improvement`
> **Type:** TODO: low - Add health check endpoint improvement

### Line   4
> **Code:** `"""FastAPI application for credit risk prediction API."""`
> **Type:** Logical operation

### Line   5
> **Code:** `import os`
> **Type:** Imports a module

### Line   6
> **Code:** `from contextlib import asynccontextmanager`
> **Type:** Imports specific names from a module

### Line   7
> **Code:** ``
> **Type:** Empty line

### Line   8
> **Code:** `from fastapi import FastAPI, HTTPException`
> **Type:** Imports specific names from a module

### Line   9
> **Code:** `from prometheus_fastapi_instrumentator import Instrumentator`
> **Type:** Imports specific names from a module

### Line  10
> **Code:** ``
> **Type:** Empty line

### Line  11
> **Code:** `from db import get_session, init_db, Prediction`
> **Type:** Imports specific names from a module

### Line  12
> **Code:** `from model import load_model, predict, risk_tier, get_model_version`
> **Type:** Imports specific names from a module

### Line  13
> **Code:** `from schemas import PredictRequest, PredictResponse, HealthResponse, P...`
> **Type:** Imports specific names from a module

### Line  14
> **Code:** ``
> **Type:** Empty line

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `@asynccontextmanager`
> **Type:** Code statement

### Line  17
> **Code:** `async def lifespan(app: FastAPI):`
> **Type:** Code statement

### Line  18
> **Code:** `init_db()`
> **Type:** Function call

### Line  19
> **Code:** `load_model()`
> **Type:** Function call

### Line  20
> **Code:** `yield`
> **Type:** Code statement

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** ``
> **Type:** Empty line

### Line  23
> **Code:** `app = FastAPI(title="Credit Risk Prediction API", version="1.0.0", lif...`
> **Type:** Assignment/comparison

### Line  24
> **Code:** ``
> **Type:** Empty line

### Line  25
> **Code:** `Instrumentator().instrument(app).expose(app, endpoint="/metrics")`
> **Type:** Assignment/comparison

### Line  26
> **Code:** ``
> **Type:** Empty line

### Line  27
> **Code:** ``
> **Type:** Empty line

### Line  28
> **Code:** `@app.get("/health", response_model=HealthResponse)`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `async def health():`
> **Type:** Code statement

### Line  30
> **Code:** `return HealthResponse(status="ok", model_version=get_model_version())`
> **Type:** Returns a value from a function

### Line  31
> **Code:** ``
> **Type:** Empty line

### Line  32
> **Code:** ``
> **Type:** Empty line

### Line  33
> **Code:** `@app.post("/predict", response_model=PredictResponse)`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `async def predict_endpoint(request: PredictRequest):`
> **Type:** Code statement

### Line  35
> **Code:** `try:`
> **Type:** Code statement

### Line  36
> **Code:** `input_data = request.model_dump()`
> **Type:** Assignment/comparison

### Line  37
> **Code:** `prediction, probability = predict(input_data)`
> **Type:** Assignment/comparison

### Line  38
> **Code:** `tier = risk_tier(probability)`
> **Type:** Assignment/comparison

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** `session = get_session()`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `record = Prediction(`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `input_json=input_data,`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `prediction=prediction,`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `probability=str(probability),`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `)`
> **Type:** Code statement

### Line  46
> **Code:** `session.add(record)`
> **Type:** Logical operation

### Line  47
> **Code:** `session.commit()`
> **Type:** Function call

### Line  48
> **Code:** `session.close()`
> **Type:** Function call

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** `return PredictResponse(prediction=prediction, probability=probability,...`
> **Type:** Returns a value from a function

### Line  51
> **Code:** `except Exception as e:`
> **Type:** Code statement

### Line  52
> **Code:** `raise HTTPException(status_code=500, detail=str(e))`
> **Type:** Raises an exception

### Line  53
> **Code:** ``
> **Type:** Empty line

### Line  54
> **Code:** ``
> **Type:** Empty line

### Line  55
> **Code:** `@app.get("/predictions", response_model=list[PredictionRecord])`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `async def get_predictions(limit: int = 100):`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `session = get_session()`
> **Type:** Assignment/comparison

### Line  58
> **Code:** `records = session.query(Prediction).order_by(Prediction.created_at.des...`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `session.close()`
> **Type:** Function call

### Line  60
> **Code:** `return [`
> **Type:** Returns a value from a function

### Line  61
> **Code:** `PredictionRecord(`
> **Type:** Logical operation

### Line  62
> **Code:** `id=r.id,`
> **Type:** Assignment/comparison

### Line  63
> **Code:** `input_json=r.input_json,`
> **Type:** Assignment/comparison

### Line  64
> **Code:** `prediction=r.prediction,`
> **Type:** Assignment/comparison

### Line  65
> **Code:** `probability=float(r.probability),`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `created_at=r.created_at.isoformat(),`
> **Type:** Assignment/comparison

### Line  67
> **Code:** `)`
> **Type:** Code statement

### Line  68
> **Code:** `for r in records`
> **Type:** For loop

### Line  69
> **Code:** `]`
> **Type:** Code statement

### Line  70
> **Code:** ``
> **Type:** Empty line

### Line  71
> **Code:** ``
> **Type:** Empty line

### Line  72
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  73
> **Code:** `import uvicorn`
> **Type:** Imports a module

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** `uvicorn.run(app, host="0.0.0.0", port=8000)`
> **Type:** Assignment/comparison

## Summary
- **Total lines:** 75
- **Code lines:** 54
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 18

---
*Documentation generated for: mlops-platform-spec*
*File: main.py*
---

# mlops-platform-spec: generate_churn_data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/ml/generate_churn_data.py`
- **Total lines:** 76
- **File size:** 2162 bytes

## Line Type Summary
- **Code:** 57
- **Comment:** 2
- **Empty:** 14
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   3
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   4
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   5
> **Code:** `"""Generate realistic synthetic Telco customer churn data (Kaggle-styl...`
> **Type:** Arithmetic operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Produces ~7000 rows with the same columns and value distributions as t...`
> **Type:** Logical operation

### Line   8
> **Code:** `public Telco Customer Churn dataset (minus customerID).`
> **Type:** Code statement

### Line   9
> **Code:** `"""`
> **Type:** Code statement

### Line  10
> **Code:** `import random`
> **Type:** Imports a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `random.seed(42)`
> **Type:** Logical operation

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `CONTRACTS = ["Month-to-month", "One year", "Two year"]`
> **Type:** Assignment/comparison

### Line  15
> **Code:** `PAYMENT_METHODS = [`
> **Type:** Assignment/comparison

### Line  16
> **Code:** `"Electronic check",`
> **Type:** Code statement

### Line  17
> **Code:** `"Mailed check",`
> **Type:** Code statement

### Line  18
> **Code:** `"Bank transfer (automatic)",`
> **Type:** Code statement

### Line  19
> **Code:** `"Credit card (automatic)",`
> **Type:** Code statement

### Line  20
> **Code:** `]`
> **Type:** Code statement

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `# Churn probability per contract type (longer contracts churn less)`
> **Type:** Comment: Churn probability per contract type (longer contracts churn less)

### Line  23
> **Code:** `CONTRACT_CHURN = {`
> **Type:** Assignment/comparison

### Line  24
> **Code:** `"Month-to-month": 0.45,`
> **Type:** Arithmetic operation

### Line  25
> **Code:** `"One year": 0.16,`
> **Type:** Code statement

### Line  26
> **Code:** `"Two year": 0.03,`
> **Type:** Code statement

### Line  27
> **Code:** `}`
> **Type:** Code statement

### Line  28
> **Code:** `PAYMENT_CHURN = {`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `"Electronic check": 0.35,`
> **Type:** Code statement

### Line  30
> **Code:** `"Mailed check": 0.22,`
> **Type:** Code statement

### Line  31
> **Code:** `"Bank transfer (automatic)": 0.12,`
> **Type:** Code statement

### Line  32
> **Code:** `"Credit card (automatic)": 0.10,`
> **Type:** Code statement

### Line  33
> **Code:** `}`
> **Type:** Code statement

### Line  34
> **Code:** ``
> **Type:** Empty line

### Line  35
> **Code:** ``
> **Type:** Empty line

### Line  36
> **Code:** `def rand_tenure(contract):`
> **Type:** Function definition

### Line  37
> **Code:** `if contract == "Month-to-month":`
> **Type:** Conditional statement

### Line  38
> **Code:** `return random.randint(0, 24)`
> **Type:** Returns a value from a function

### Line  39
> **Code:** `if contract == "One year":`
> **Type:** Conditional statement

### Line  40
> **Code:** `return random.randint(12, 24)`
> **Type:** Returns a value from a function

### Line  41
> **Code:** `return random.randint(24, 72)`
> **Type:** Returns a value from a function

### Line  42
> **Code:** ``
> **Type:** Empty line

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** `def generate_row():`
> **Type:** Function definition

### Line  45
> **Code:** `contract = random.choices(CONTRACTS, weights=[0.55, 0.24, 0.21])[0]`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `payment = random.choices(`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `PAYMENT_METHODS, weights=[0.35, 0.20, 0.23, 0.22]`
> **Type:** Assignment/comparison

### Line  48
> **Code:** `)[0]`
> **Type:** Data structure operation

### Line  49
> **Code:** `tenure = rand_tenure(contract)`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `monthly = round(random.uniform(18.0, 120.0), 2)`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `total = round(monthly * tenure, 2)`
> **Type:** Assignment/comparison

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `p = 0.04  # base churn`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `p += CONTRACT_CHURN[contract]`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `p += PAYMENT_CHURN[payment]`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `p += max(0.0, (monthly - 60.0) / 300.0)`
> **Type:** Assignment/comparison

### Line  57
> **Code:** `p -= min(0.25, tenure / 200.0)`
> **Type:** Assignment/comparison

### Line  58
> **Code:** `p = min(max(p, 0.0), 0.97)`
> **Type:** Assignment/comparison

### Line  59
> **Code:** ``
> **Type:** Empty line

### Line  60
> **Code:** `churn = 1 if random.random() < p else 0`
> **Type:** Assignment/comparison

### Line  61
> **Code:** `return tenure, monthly, total, contract, payment, churn`
> **Type:** Returns a value from a function

### Line  62
> **Code:** ``
> **Type:** Empty line

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `def main():`
> **Type:** Function definition

### Line  65
> **Code:** `rows = ["tenure,MonthlyCharges,TotalCharges,Contract,PaymentMethod,Chu...`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `for _ in range(7000):`
> **Type:** For loop

### Line  67
> **Code:** `t, m, tot, c, pm, ch = generate_row()`
> **Type:** Assignment/comparison

### Line  68
> **Code:** `rows.append(f"{t},{m},{tot},{c},{pm},{ch}")`
> **Type:** Function call

### Line  69
> **Code:** `out = "ml/data/churn.csv"`
> **Type:** Assignment/comparison

### Line  70
> **Code:** `with open(out, "w", encoding="utf-8") as f:`
> **Type:** Context manager

### Line  71
> **Code:** `f.write("\n".join(rows) + "\n")`
> **Type:** Arithmetic operation

### Line  72
> **Code:** `print(f"wrote {out} with {len(rows) - 1} data rows")`
> **Type:** Prints output to console

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** ``
> **Type:** Empty line

### Line  75
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  76
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 76
- **Code lines:** 57
- **Comments:** 2
- **TODO items:** 3
- **Empty lines:** 14

---
*Documentation generated for: mlops-platform-spec*
*File: generate_churn_data.py*
---

# mlops-platform-spec: evaluate.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/ml/evaluate.py`
- **Total lines:** 78
- **File size:** 2396 bytes

## Line Type Summary
- **Code:** 55
- **Comment:** 1
- **Empty:** 19
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: high - Add quality gate with thresholds`
> **Type:** TODO: high - Add quality gate with thresholds

### Line   3
> **Code:** `# TODO: medium - Implement comparison vs current production model`
> **Type:** TODO: medium - Implement comparison vs current production model

### Line   4
> **Code:** `# TODO: low - Add metrics export for Evidence Pack`
> **Type:** TODO: low - Add metrics export for Evidence Pack

### Line   5
> **Code:** `"""Evaluate the credit risk model against the hold-out test set.`
> **Type:** Arithmetic operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Loads the registered model from MLflow, computes AUC, KS, and fairness`
> **Type:** Logical operation

### Line   8
> **Code:** `metrics, and gates on AUC >= 0.75.`
> **Type:** Assignment/comparison

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `Exit codes:`
> **Type:** Code statement

### Line  11
> **Code:** `0  AUC >= 0.75 (gate passed)`
> **Type:** Assignment/comparison

### Line  12
> **Code:** `1  AUC < 0.75  (gate failed) or any error`
> **Type:** Comparison operation

### Line  13
> **Code:** `"""`
> **Type:** Code statement

### Line  14
> **Code:** `import os`
> **Type:** Imports a module

### Line  15
> **Code:** `import sys`
> **Type:** Imports a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line  18
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  19
> **Code:** `from mlflow.tracking import MlflowClient`
> **Type:** Imports specific names from a module

### Line  20
> **Code:** `from sklearn.metrics import classification_report, roc_auc_score, roc_...`
> **Type:** Imports specific names from a module

### Line  21
> **Code:** ``
> **Type:** Empty line

### Line  22
> **Code:** `from preprocess import encode_features, load_data, train_test_split`
> **Type:** Imports specific names from a module

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  26
> **Code:** `AUC_THRESHOLD = 0.75`
> **Type:** Assignment/comparison

### Line  27
> **Code:** `KS_THRESHOLD = 0.30`
> **Type:** Assignment/comparison

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** ``
> **Type:** Empty line

### Line  30
> **Code:** `def compute_ks(y_true, y_prob):`
> **Type:** Function definition

### Line  31
> **Code:** `fpr, tpr, _ = roc_curve(y_true, y_prob)`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `return float(np.max(tpr - fpr))`
> **Type:** Returns a value from a function

### Line  33
> **Code:** ``
> **Type:** Empty line

### Line  34
> **Code:** ``
> **Type:** Empty line

### Line  35
> **Code:** `def main():`
> **Type:** Function definition

### Line  36
> **Code:** `mlflow.set_tracking_uri(TRACKING_URI)`
> **Type:** Function call

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `client = MlflowClient()`
> **Type:** Assignment/comparison

### Line  39
> **Code:** `versions = client.get_latest_versions(MODEL_NAME, stages=["Production"...`
> **Type:** Assignment/comparison

### Line  40
> **Code:** `if not versions:`
> **Type:** Conditional statement

### Line  41
> **Code:** `print(f"ERROR: no registered model named '{MODEL_NAME}' found")`
> **Type:** Prints output to console

### Line  42
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  43
> **Code:** `version = versions[0]`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `print(f"Evaluating {MODEL_NAME} version {version.version}")`
> **Type:** Prints output to console

### Line  45
> **Code:** ``
> **Type:** Empty line

### Line  46
> **Code:** `model_uri = f"models:/{MODEL_NAME}/{version.version}"`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `clf = mlflow.sklearn.load_model(model_uri)`
> **Type:** Assignment/comparison

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `df = load_data()`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `X, y = encode_features(df)`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `train_df, test_df = train_test_split(df)`
> **Type:** Assignment/comparison

### Line  52
> **Code:** `X_test = X.loc[test_df.index]`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `y_test = y.loc[test_df.index]`
> **Type:** Assignment/comparison

### Line  54
> **Code:** ``
> **Type:** Empty line

### Line  55
> **Code:** `proba = clf.predict_proba(X_test)[:, 1]`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `preds = clf.predict(X_test)`
> **Type:** Assignment/comparison

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `auc = float(roc_auc_score(y_test, proba))`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `ks = compute_ks(y_test, proba)`
> **Type:** Assignment/comparison

### Line  60
> **Code:** ``
> **Type:** Empty line

### Line  61
> **Code:** `print("Classification report:")`
> **Type:** Prints output to console

### Line  62
> **Code:** `print(classification_report(y_test, preds, target_names=["Repaid", "De...`
> **Type:** Prints output to console

### Line  63
> **Code:** `print(f"AUC:  {auc:.4f}  (threshold: {AUC_THRESHOLD})")`
> **Type:** Prints output to console

### Line  64
> **Code:** `print(f"KS:   {ks:.4f}  (threshold: {KS_THRESHOLD})")`
> **Type:** Prints output to console

### Line  65
> **Code:** ``
> **Type:** Empty line

### Line  66
> **Code:** `if auc < AUC_THRESHOLD:`
> **Type:** Conditional statement

### Line  67
> **Code:** `print(f"FAIL: AUC {auc:.4f} < {AUC_THRESHOLD}")`
> **Type:** Prints output to console

### Line  68
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  69
> **Code:** `if ks < KS_THRESHOLD:`
> **Type:** Conditional statement

### Line  70
> **Code:** `print(f"FAIL: KS {ks:.4f} < {KS_THRESHOLD}")`
> **Type:** Prints output to console

### Line  71
> **Code:** `sys.exit(1)`
> **Type:** Function call

### Line  72
> **Code:** ``
> **Type:** Empty line

### Line  73
> **Code:** `print(f"PASS: AUC={auc:.4f} >= {AUC_THRESHOLD}, KS={ks:.4f} >= {KS_THR...`
> **Type:** Prints output to console

### Line  74
> **Code:** `sys.exit(0)`
> **Type:** Function call

### Line  75
> **Code:** ``
> **Type:** Empty line

### Line  76
> **Code:** ``
> **Type:** Empty line

### Line  77
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  78
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 78
- **Code lines:** 55
- **Comments:** 1
- **TODO items:** 3
- **Empty lines:** 19

---
*Documentation generated for: mlops-platform-spec*
*File: evaluate.py*
---

# mlops-platform-spec: preprocess.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/ml/preprocess.py`
- **Total lines:** 55
- **File size:** 1668 bytes

## Line Type Summary
- **Code:** 39
- **Comment:** 0
- **Empty:** 13
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   2
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   3
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   4
> **Code:** `"""Shared preprocessing for the credit risk ML pipeline.`
> **Type:** Logical operation

### Line   5
> **Code:** ``
> **Type:** Empty line

### Line   6
> **Code:** `Encodes categorical features, handles missing values, and splits the d...`
> **Type:** Logical operation

### Line   7
> **Code:** `Both train.py and evaluate.py import from here so the encoding is`
> **Type:** Logical operation

### Line   8
> **Code:** `identical between training and evaluation.`
> **Type:** Logical operation

### Line   9
> **Code:** `"""`
> **Type:** Code statement

### Line  10
> **Code:** `import os`
> **Type:** Imports a module

### Line  11
> **Code:** ``
> **Type:** Empty line

### Line  12
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  13
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  14
> **Code:** `from sklearn.preprocessing import LabelEncoder`
> **Type:** Imports specific names from a module

### Line  15
> **Code:** ``
> **Type:** Empty line

### Line  16
> **Code:** `NUMERIC_COLUMNS = [`
> **Type:** Assignment/comparison

### Line  17
> **Code:** `"age", "income", "monthly_income", "debt_ratio",`
> **Type:** Code statement

### Line  18
> **Code:** `"revolving_utilization", "num_open_credit_lines", "num_dependents",`
> **Type:** Code statement

### Line  19
> **Code:** `"num_30_59_days_late", "num_60_89_days_late", "num_90_days_late",`
> **Type:** Code statement

### Line  20
> **Code:** `"num_mortgages", "number_real_estate_loans",`
> **Type:** Logical operation

### Line  21
> **Code:** `]`
> **Type:** Code statement

### Line  22
> **Code:** `TARGET = "default"`
> **Type:** Assignment/comparison

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)...`
> **Type:** Assignment/comparison

### Line  25
> **Code:** `DATA_PATH = os.environ.get(`
> **Type:** Assignment/comparison

### Line  26
> **Code:** `"CREDIT_DATA_PATH", os.path.join(_REPO_ROOT, "ml", "data", "credit.csv...`
> **Type:** Function call

### Line  27
> **Code:** `)`
> **Type:** Code statement

### Line  28
> **Code:** ``
> **Type:** Empty line

### Line  29
> **Code:** ``
> **Type:** Empty line

### Line  30
> **Code:** `def load_data(path=None):`
> **Type:** Function definition

### Line  31
> **Code:** `path = path or DATA_PATH`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `df = pd.read_csv(path)`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `if "customer_id" in df.columns:`
> **Type:** Conditional statement

### Line  34
> **Code:** `df = df.drop(columns=["customer_id"])`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `return df`
> **Type:** Returns a value from a function

### Line  36
> **Code:** ``
> **Type:** Empty line

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** `def encode_features(df):`
> **Type:** Function definition

### Line  39
> **Code:** `"""Return (X, y) with all features numeric."""`
> **Type:** Code statement

### Line  40
> **Code:** `X = df[NUMERIC_COLUMNS].copy()`
> **Type:** Assignment/comparison

### Line  41
> **Code:** `y = df[TARGET].astype(int)`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `return X, y`
> **Type:** Returns a value from a function

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** `def apply_encoders(df, encoders=None):`
> **Type:** Function definition

### Line  46
> **Code:** `"""Apply feature matrix (encoders kept for API compatibility)."""`
> **Type:** Logical operation

### Line  47
> **Code:** `return df[NUMERIC_COLUMNS].copy()`
> **Type:** Returns a value from a function

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** ``
> **Type:** Empty line

### Line  50
> **Code:** `def train_test_split(df, test_size=0.2, random_state=42):`
> **Type:** Function definition

### Line  51
> **Code:** `from sklearn.model_selection import train_test_split as _split`
> **Type:** Imports specific names from a module

### Line  52
> **Code:** ``
> **Type:** Empty line

### Line  53
> **Code:** `return _split(`
> **Type:** Returns a value from a function

### Line  54
> **Code:** `df, test_size=test_size, random_state=random_state, stratify=df[TARGET...`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `)`
> **Type:** Code statement

## Summary
- **Total lines:** 55
- **Code lines:** 39
- **Comments:** 0
- **TODO items:** 3
- **Empty lines:** 13

---
*Documentation generated for: mlops-platform-spec*
*File: preprocess.py*
---

# mlops-platform-spec: train.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/ml/train.py`
- **Total lines:** 105
- **File size:** 3495 bytes

## Line Type Summary
- **Code:** 79
- **Comment:** 3
- **Empty:** 20
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: high - Add data validation before training`
> **Type:** TODO: high - Add data validation before training

### Line   3
> **Code:** `# TODO: medium - Implement hyperparameter logging`
> **Type:** TODO: medium - Implement hyperparameter logging

### Line   4
> **Code:** `# TODO: low - Add model explainability integration`
> **Type:** TODO: low - Add model explainability integration

### Line   5
> **Code:** `"""Train a credit risk classifier and log it to MLflow.`
> **Type:** Logical operation

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Steps:`
> **Type:** Code statement

### Line   8
> **Code:** `1. Load ml/data/credit.csv`
> **Type:** Arithmetic operation

### Line   9
> **Code:** `2. Drop customer_id, prepare numeric features`
> **Type:** Code statement

### Line  10
> **Code:** `3. Train/test split 80/20, stratified, random_state=42`
> **Type:** Assignment/comparison

### Line  11
> **Code:** `4. Train XGBoostClassifier (primary) + LogisticRegression (baseline)`
> **Type:** Arithmetic operation

### Line  12
> **Code:** `5. Log params + metrics (AUC, KS, precision, recall, F1) to MLflow`
> **Type:** Arithmetic operation

### Line  13
> **Code:** `6. Register model in MLflow Model Registry as "credit-risk-model"`
> **Type:** Arithmetic operation

### Line  14
> **Code:** `7. Save model artifact model.pkl`
> **Type:** Code statement

### Line  15
> **Code:** `"""`
> **Type:** Code statement

### Line  16
> **Code:** `import os`
> **Type:** Imports a module

### Line  17
> **Code:** `import pickle`
> **Type:** Imports a module

### Line  18
> **Code:** ``
> **Type:** Empty line

### Line  19
> **Code:** `import mlflow`
> **Type:** Imports a module

### Line  20
> **Code:** `import mlflow.sklearn`
> **Type:** Imports a module

### Line  21
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  22
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  23
> **Code:** `from sklearn.ensemble import GradientBoostingClassifier`
> **Type:** Imports specific names from a module

### Line  24
> **Code:** `from sklearn.linear_model import LogisticRegression`
> **Type:** Imports specific names from a module

### Line  25
> **Code:** `from sklearn.metrics import (`
> **Type:** Imports specific names from a module

### Line  26
> **Code:** `accuracy_score,`
> **Type:** Logical operation

### Line  27
> **Code:** `f1_score,`
> **Type:** Logical operation

### Line  28
> **Code:** `precision_score,`
> **Type:** Logical operation

### Line  29
> **Code:** `recall_score,`
> **Type:** Logical operation

### Line  30
> **Code:** `roc_auc_score,`
> **Type:** Logical operation

### Line  31
> **Code:** `)`
> **Type:** Code statement

### Line  32
> **Code:** ``
> **Type:** Empty line

### Line  33
> **Code:** `from preprocess import encode_features, load_data, train_test_split`
> **Type:** Imports specific names from a module

### Line  34
> **Code:** ``
> **Type:** Empty line

### Line  35
> **Code:** `MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")`
> **Type:** Assignment/comparison

### Line  36
> **Code:** `TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1...`
> **Type:** Assignment/comparison

### Line  37
> **Code:** ``
> **Type:** Empty line

### Line  38
> **Code:** ``
> **Type:** Empty line

### Line  39
> **Code:** `def compute_ks(y_true, y_prob):`
> **Type:** Function definition

### Line  40
> **Code:** `from sklearn.metrics import roc_curve`
> **Type:** Imports specific names from a module

### Line  41
> **Code:** `fpr, tpr, _ = roc_curve(y_true, y_prob)`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `return float(np.max(tpr - fpr))`
> **Type:** Returns a value from a function

### Line  43
> **Code:** ``
> **Type:** Empty line

### Line  44
> **Code:** ``
> **Type:** Empty line

### Line  45
> **Code:** `def main():`
> **Type:** Function definition

### Line  46
> **Code:** `mlflow.set_tracking_uri(TRACKING_URI)`
> **Type:** Function call

### Line  47
> **Code:** `mlflow.set_experiment("credit-risk")`
> **Type:** Arithmetic operation

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `df = load_data()`
> **Type:** Assignment/comparison

### Line  50
> **Code:** `X, y = encode_features(df)`
> **Type:** Assignment/comparison

### Line  51
> **Code:** ``
> **Type:** Empty line

### Line  52
> **Code:** `train_df, test_df = train_test_split(df)`
> **Type:** Assignment/comparison

### Line  53
> **Code:** `X_train = X.loc[train_df.index]`
> **Type:** Assignment/comparison

### Line  54
> **Code:** `y_train = y.loc[train_df.index]`
> **Type:** Assignment/comparison

### Line  55
> **Code:** `X_test = X.loc[test_df.index]`
> **Type:** Assignment/comparison

### Line  56
> **Code:** `y_test = y.loc[test_df.index]`
> **Type:** Assignment/comparison

### Line  57
> **Code:** ``
> **Type:** Empty line

### Line  58
> **Code:** `params = {"n_estimators": 200, "max_depth": 6, "learning_rate": 0.1, "...`
> **Type:** Assignment/comparison

### Line  59
> **Code:** `clf = GradientBoostingClassifier(**params)`
> **Type:** Assignment/comparison

### Line  60
> **Code:** `clf.fit(X_train, y_train)`
> **Type:** Function call

### Line  61
> **Code:** ``
> **Type:** Empty line

### Line  62
> **Code:** `preds = clf.predict(X_test)`
> **Type:** Assignment/comparison

### Line  63
> **Code:** `proba = clf.predict_proba(X_test)[:, 1]`
> **Type:** Assignment/comparison

### Line  64
> **Code:** ``
> **Type:** Empty line

### Line  65
> **Code:** `metrics = {`
> **Type:** Assignment/comparison

### Line  66
> **Code:** `"accuracy": float(accuracy_score(y_test, preds)),`
> **Type:** Logical operation

### Line  67
> **Code:** `"f1": float(f1_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  68
> **Code:** `"roc_auc": float(roc_auc_score(y_test, proba)),`
> **Type:** Logical operation

### Line  69
> **Code:** `"ks": compute_ks(y_test, proba),`
> **Type:** Code statement

### Line  70
> **Code:** `"precision": float(precision_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  71
> **Code:** `"recall": float(recall_score(y_test, preds, zero_division=0)),`
> **Type:** Assignment/comparison

### Line  72
> **Code:** `}`
> **Type:** Code statement

### Line  73
> **Code:** ``
> **Type:** Empty line

### Line  74
> **Code:** `print(f"metrics: {metrics}")`
> **Type:** Prints output to console

### Line  75
> **Code:** ``
> **Type:** Empty line

### Line  76
> **Code:** `with mlflow.start_run() as run:`
> **Type:** Context manager

### Line  77
> **Code:** `mlflow.log_params(params)`
> **Type:** Function call

### Line  78
> **Code:** `mlflow.log_metrics(metrics)`
> **Type:** Function call

### Line  79
> **Code:** `mlflow.log_param("n_features", X_train.shape[1])`
> **Type:** Function call

### Line  80
> **Code:** `mlflow.log_param("data_source", "credit.csv")`
> **Type:** Function call

### Line  81
> **Code:** `mlflow.log_param("default_rate", f"{y_train.mean():.4f}")`
> **Type:** Function call

### Line  82
> **Code:** ``
> **Type:** Empty line

### Line  83
> **Code:** `mlflow.sklearn.log_model(clf, "model")`
> **Type:** Function call

### Line  84
> **Code:** `mlflow.log_artifact("ml/data/credit.csv", artifact_path="data")`
> **Type:** Assignment/comparison

### Line  85
> **Code:** ``
> **Type:** Empty line

### Line  86
> **Code:** `# Register`
> **Type:** Comment: Register

### Line  87
> **Code:** `model_uri = f"runs:/{run.info.run_id}/model"`
> **Type:** Assignment/comparison

### Line  88
> **Code:** `registered = mlflow.register_model(model_uri, MODEL_NAME)`
> **Type:** Assignment/comparison

### Line  89
> **Code:** `client = mlflow.MlflowClient()`
> **Type:** Assignment/comparison

### Line  90
> **Code:** `client.transition_model_version_stage(`
> **Type:** Code statement

### Line  91
> **Code:** `name=MODEL_NAME, version=registered.version, stage="Staging"`
> **Type:** Assignment/comparison

### Line  92
> **Code:** `)`
> **Type:** Code statement

### Line  93
> **Code:** `print(f"Registered {MODEL_NAME} version {registered.version} in Stagin...`
> **Type:** Prints output to console

### Line  94
> **Code:** ``
> **Type:** Empty line

### Line  95
> **Code:** `# Save locally`
> **Type:** Comment: Save locally

### Line  96
> **Code:** `model_path = os.path.join(_REPO_ROOT, "ml", "model.pkl")`
> **Type:** Assignment/comparison

### Line  97
> **Code:** `with open(model_path, "wb") as f:`
> **Type:** Context manager

### Line  98
> **Code:** `pickle.dump(clf, f)`
> **Type:** Function call

### Line  99
> **Code:** `print(f"Saved model to {model_path}")`
> **Type:** Prints output to console

### Line 100
> **Code:** `print(f"AUC={metrics['roc_auc']:.4f} KS={metrics['ks']:.4f}")`
> **Type:** Prints output to console

### Line 101
> **Code:** ``
> **Type:** Empty line

### Line 102
> **Code:** `_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)...`
> **Type:** Assignment/comparison

### Line 103
> **Code:** ``
> **Type:** Empty line

### Line 104
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line 105
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 105
- **Code lines:** 79
- **Comments:** 3
- **TODO items:** 3
- **Empty lines:** 20

---
*Documentation generated for: mlops-platform-spec*
*File: train.py*
---

# mlops-platform-spec: generate_credit_data.py

## File Information
- **File path:** `/home/gadour/Desktop/new_project/other/mlops-platform-spec/.worktrees/proj2/ml/data/generate_credit_data.py`
- **Total lines:** 99
- **File size:** 3611 bytes

## Line Type Summary
- **Code:** 74
- **Comment:** 5
- **Empty:** 17
- **TODO:** 3

## Detailed Line Explanations

### Line   1
> **Code:** `#!/usr/bin/env python3`
> **Type:** Comment: !/usr/bin/env python3

### Line   2
> **Code:** `# TODO: medium - Add type hints where missing`
> **Type:** TODO: medium - Add type hints where missing

### Line   3
> **Code:** `# TODO: low - Add comprehensive docstring`
> **Type:** TODO: low - Add comprehensive docstring

### Line   4
> **Code:** `# TODO: low - Add error handling for edge cases`
> **Type:** TODO: low - Add error handling for edge cases

### Line   5
> **Code:** `"""Generate realistic synthetic credit risk data.`
> **Type:** Code statement

### Line   6
> **Code:** ``
> **Type:** Empty line

### Line   7
> **Code:** `Based on Kaggle "Give Me Some Credit" dataset distributions.`
> **Type:** Code statement

### Line   8
> **Code:** `Features mirror real banking data: income, debt, credit history, delin...`
> **Type:** Logical operation

### Line   9
> **Code:** ``
> **Type:** Empty line

### Line  10
> **Code:** `Output: ml/data/credit.csv (50K rows, ~7% default rate)`
> **Type:** Arithmetic operation

### Line  11
> **Code:** `Deterministic (seed=42) for reproducibility.`
> **Type:** Assignment/comparison

### Line  12
> **Code:** `"""`
> **Type:** Code statement

### Line  13
> **Code:** ``
> **Type:** Empty line

### Line  14
> **Code:** `import argparse`
> **Type:** Imports a module

### Line  15
> **Code:** `import os`
> **Type:** Imports a module

### Line  16
> **Code:** ``
> **Type:** Empty line

### Line  17
> **Code:** `import numpy as np`
> **Type:** Imports a module

### Line  18
> **Code:** `import pandas as pd`
> **Type:** Imports a module

### Line  19
> **Code:** ``
> **Type:** Empty line

### Line  20
> **Code:** `RNG = np.random.default_rng(42)`
> **Type:** Assignment/comparison

### Line  21
> **Code:** `N_DEFAULTS = 50_000`
> **Type:** Assignment/comparison

### Line  22
> **Code:** `DEFAULT_RATE = 0.067  # 6.7% default rate (matches real data)`
> **Type:** Assignment/comparison

### Line  23
> **Code:** ``
> **Type:** Empty line

### Line  24
> **Code:** `OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cre...`
> **Type:** Assignment/comparison

### Line  25
> **Code:** ``
> **Type:** Empty line

### Line  26
> **Code:** ``
> **Type:** Empty line

### Line  27
> **Code:** `def generate(n_rows: int = N_DEFAULTS) -> pd.DataFrame:`
> **Type:** Function definition

### Line  28
> **Code:** `rows = []`
> **Type:** Assignment/comparison

### Line  29
> **Code:** `for i in range(n_rows):`
> **Type:** For loop

### Line  30
> **Code:** `age = int(RNG.integers(18, 80))`
> **Type:** Assignment/comparison

### Line  31
> **Code:** `income = max(500, float(RNG.lognormal(10.5, 0.8)))  # median ~36K`
> **Type:** Assignment/comparison

### Line  32
> **Code:** `debt_ratio = float(np.clip(RNG.beta(2, 5), 0, 10))  # mostly <1`
> **Type:** Assignment/comparison

### Line  33
> **Code:** `num_open_credit = int(RNG.poisson(5))`
> **Type:** Assignment/comparison

### Line  34
> **Code:** `num_dep = int(RNG.poisson(1))`
> **Type:** Assignment/comparison

### Line  35
> **Code:** `monthly_income = income / 12`
> **Type:** Assignment/comparison

### Line  36
> **Code:** `# --- Generate correlated features (high debt → more late payments) --...`
> **Type:** Comment: --- Generate correlated features (high debt → more late payments) ---

### Line  37
> **Code:** `# Base risk score drives both feature correlation and default`
> **Type:** Comment: Base risk score drives both feature correlation and default

### Line  38
> **Code:** `base_risk = float(RNG.beta(2, 5))  # 0-1 scale`
> **Type:** Assignment/comparison

### Line  39
> **Code:** ``
> **Type:** Empty line

### Line  40
> **Code:** `# High-risk borrowers have more late payments, higher utilization`
> **Type:** Comment: High-risk borrowers have more late payments, higher utilization

### Line  41
> **Code:** `num_30_59_late = int(RNG.poisson(0.3 + 2.0 * base_risk))`
> **Type:** Assignment/comparison

### Line  42
> **Code:** `num_60_89_late = int(RNG.poisson(0.1 + 1.5 * base_risk))`
> **Type:** Assignment/comparison

### Line  43
> **Code:** `num_90_late = int(RNG.poisson(0.05 + 1.0 * base_risk))`
> **Type:** Assignment/comparison

### Line  44
> **Code:** `revolving_util = float(np.clip(RNG.beta(2 + 3 * base_risk, 2 + 2 * (1 ...`
> **Type:** Assignment/comparison

### Line  45
> **Code:** `num_open_credit = int(RNG.poisson(3 + 4 * base_risk))`
> **Type:** Assignment/comparison

### Line  46
> **Code:** `num_mortgages = int(RNG.poisson(0.8))`
> **Type:** Assignment/comparison

### Line  47
> **Code:** `num_family_members = int(RNG.poisson(0.5))`
> **Type:** Assignment/comparison

### Line  48
> **Code:** ``
> **Type:** Empty line

### Line  49
> **Code:** `# --- Default probability (strong signal) ---`
> **Type:** Comment: --- Default probability (strong signal) ---

### Line  50
> **Code:** `logit = (`
> **Type:** Assignment/comparison

### Line  51
> **Code:** `-2.8`
> **Type:** Arithmetic operation

### Line  52
> **Code:** `+ 1.5 * num_90_late`
> **Type:** Arithmetic operation

### Line  53
> **Code:** `+ 1.0 * num_60_89_late`
> **Type:** Arithmetic operation

### Line  54
> **Code:** `+ 0.6 * num_30_59_late`
> **Type:** Arithmetic operation

### Line  55
> **Code:** `+ 0.03 * (revolving_util - 40) / 10`
> **Type:** Arithmetic operation

### Line  56
> **Code:** `+ 0.8 * np.log1p(debt_ratio)`
> **Type:** Arithmetic operation

### Line  57
> **Code:** `- 0.02 * (age - 40) / 10`
> **Type:** Arithmetic operation

### Line  58
> **Code:** `+ 0.6 * (num_open_credit > 8)`
> **Type:** Arithmetic operation

### Line  59
> **Code:** `- 0.7 * np.log1p(income / 10000)`
> **Type:** Arithmetic operation

### Line  60
> **Code:** `)`
> **Type:** Code statement

### Line  61
> **Code:** `p_default = 1 / (1 + np.exp(-logit))`
> **Type:** Assignment/comparison

### Line  62
> **Code:** `default = int(RNG.random() < p_default)`
> **Type:** Assignment/comparison

### Line  63
> **Code:** ``
> **Type:** Empty line

### Line  64
> **Code:** `rows.append({`
> **Type:** Code statement

### Line  65
> **Code:** `"customer_id": f"CUST-{i:06d}",`
> **Type:** Arithmetic operation

### Line  66
> **Code:** `"age": age,`
> **Type:** Code statement

### Line  67
> **Code:** `"income": round(income, 2),`
> **Type:** Code statement

### Line  68
> **Code:** `"monthly_income": round(monthly_income, 2),`
> **Type:** Code statement

### Line  69
> **Code:** `"debt_ratio": round(debt_ratio, 4),`
> **Type:** Code statement

### Line  70
> **Code:** `"revolving_utilization": round(revolving_util, 2),`
> **Type:** Code statement

### Line  71
> **Code:** `"num_open_credit_lines": num_open_credit,`
> **Type:** Code statement

### Line  72
> **Code:** `"num_dependents": num_dep,`
> **Type:** Code statement

### Line  73
> **Code:** `"num_30_59_days_late": num_30_59_late,`
> **Type:** Code statement

### Line  74
> **Code:** `"num_60_89_days_late": num_60_89_late,`
> **Type:** Code statement

### Line  75
> **Code:** `"num_90_days_late": num_90_late,`
> **Type:** Code statement

### Line  76
> **Code:** `"num_mortgages": num_mortgages,`
> **Type:** Logical operation

### Line  77
> **Code:** `"number_real_estate_loans": num_mortgages,`
> **Type:** Logical operation

### Line  78
> **Code:** `"default": default,`
> **Type:** Code statement

### Line  79
> **Code:** `})`
> **Type:** Code statement

### Line  80
> **Code:** ``
> **Type:** Empty line

### Line  81
> **Code:** `df = pd.DataFrame(rows)`
> **Type:** Assignment/comparison

### Line  82
> **Code:** `return df`
> **Type:** Returns a value from a function

### Line  83
> **Code:** ``
> **Type:** Empty line

### Line  84
> **Code:** ``
> **Type:** Empty line

### Line  85
> **Code:** `def main():`
> **Type:** Function definition

### Line  86
> **Code:** `parser = argparse.ArgumentParser(description="Generate credit risk dat...`
> **Type:** Assignment/comparison

### Line  87
> **Code:** `parser.add_argument("-n", "--rows", type=int, default=N_DEFAULTS)`
> **Type:** Assignment/comparison

### Line  88
> **Code:** `parser.add_argument("-o", "--output", default=OUTPUT)`
> **Type:** Assignment/comparison

### Line  89
> **Code:** `args = parser.parse_args()`
> **Type:** Assignment/comparison

### Line  90
> **Code:** ``
> **Type:** Empty line

### Line  91
> **Code:** `df = generate(args.rows)`
> **Type:** Assignment/comparison

### Line  92
> **Code:** `df.to_csv(args.output, index=False)`
> **Type:** Assignment/comparison

### Line  93
> **Code:** `rate = df["default"].mean() * 100`
> **Type:** Assignment/comparison

### Line  94
> **Code:** `print(f"Wrote {len(df):,} rows -> {args.output}")`
> **Type:** Prints output to console

### Line  95
> **Code:** `print(f"  default={df['default'].sum():,} ({rate:.1f}%)")`
> **Type:** Prints output to console

### Line  96
> **Code:** ``
> **Type:** Empty line

### Line  97
> **Code:** ``
> **Type:** Empty line

### Line  98
> **Code:** `if __name__ == "__main__":`
> **Type:** Conditional statement

### Line  99
> **Code:** `main()`
> **Type:** Function call

## Summary
- **Total lines:** 99
- **Code lines:** 74
- **Comments:** 5
- **TODO items:** 3
- **Empty lines:** 17

---
*Documentation generated for: mlops-platform-spec*
*File: generate_credit_data.py*
---

