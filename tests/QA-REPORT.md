# QA Report — mlops-platform-spec

Bugs / issues found while writing and running the QA suite against the
parallel backend worktree (`agent/backend-agent`). Severity: `HIGH` =
breaks acceptance criteria or availability; `MED` = robustness/perf;
`LOW` = style/cleanliness.

## HIGH

### H1. Hardcoded DB credential in `api/db.py`
- **File:** `api/db.py:22-28` (`get_database_url`)
- **Issue:** default `DB_PASSWORD="postgres"` hardcodes a credential. Violates the acceptance criterion *"Zero hardcoded credentials anywhere in the repo"*.
- **Repro:** `get_database_url()` with no env vars → `postgresql://postgres:postgres@postgres-service:5432/mlops`.
- **Fix:** require credentials via env (raise if unset) or read from a K8s Secret-mounted env file. Never ship a default password.

### H2. `/predict` fails when PostgreSQL is down even though the model works
- **File:** `api/main.py:38-48`
- **Issue:** DB write (`session.commit()`) runs inside the request path; any DB error bubbles up as HTTP 500, so a Postgres outage takes down prediction entirely.
- **Fix:** decouple persistence from prediction (write async, or catch DB errors and still return the prediction), or fail with a clear 503.

### H4. `POST /predict` always 500s: snake_case fields never mapped to CSV column names
- **File:** `api/model.py:52-53` + `ml/preprocess.py:12-14`
- **Issue:** the API schema (and the spec's request body) uses snake_case (`monthly_charges`, `total_charges`), but `preprocess.CATEGORICAL_COLUMNS/NUMERIC_COLUMNS` expect the CSV's PascalCase (`MonthlyCharges`, `TotalCharges`). `model.predict` builds `pd.DataFrame([input_data])` and hands it straight to `apply_encoders`, which does `df[["Contract","PaymentMethod","tenure","MonthlyCharges","TotalCharges"]]` → `KeyError` on every request.
- **Repro:** a **valid** spec payload (`tenure`, `monthly_charges`, `total_charges`, `contract`, `payment_method`) → HTTP 500, so the acceptance criterion *"POST /predict returns a valid prediction"* fails 100% of the time.
- **Fix:** map API fields to model/preprocess column names in `model.predict` (e.g. `{"tenure":"tenure","monthly_charges":"MonthlyCharges","total_charges":"TotalCharges","contract":"Contract","payment_method":"PaymentMethod"}`) or have `apply_encoders` accept both.
- **Test:** `tests/test_api.py::TestPredict::test_real_predict_path` is marked `xfail` until this is fixed.

### H3. Unknown categorical value returns 500 instead of 422
- **File:** `api/model.py:59-63` + `api/schemas.py:5-10`
- **Issue:** `contract`/`payment_method` are free-form strings. `LabelEncoder.transform` raises `ValueError` for out-of-vocabulary input; the endpoint catches it and returns 500.
- **Repro:** `POST /predict` with `"contract": "Zero-year platinum"` → 500.
- **Fix:** constrain the schema to the training vocabulary (enum/Literal) so invalid input is rejected with 422 at validation time. Test locks this in: `tests/test_api.py::TestPredict::test_out_of_vocab_category_rejected`.

## MED

### M1. Encoders re-fit on every prediction request
- **File:** `api/model.py:57-62`
- **Issue:** every `/predict` re-reads the full CSV and re-fits two `LabelEncoder`s. Slow, wasteful, and if the training CSV ever changes the API silently re-encodes with different mappings than the served model was trained on.
- **Fix:** persist the fitted encoders alongside the model artifact and load them with the model.

### M2. Relative paths in `ml/train.py`
- **File:** `ml/train.py:59,72`
- **Issue:** `mlflow.log_artifact("ml/data/churn.csv")` and `os.path.join("ml", "model.pkl")` depend on the process CWD being the repo root. Breaks when run from Jenkins workspace or any other directory.
- **Fix:** resolve paths relative to the script location (`Path(__file__).resolve().parent`).

### M3. `roc_auc_score` can crash on a single-class test split
- **File:** `ml/train.py:51`
- **Issue:** `roc_auc_score` raises `ValueError` if the test split has only one class. Unlikely with stratified split on the full CSV, but a small/balanced-enough dataset can hit it and kill the whole pipeline.
- **Fix:** guard with a fallback (report `roc_auc=None` when a class is missing).

### M4. Duplicate full-data encode in `ml/evaluate.py`
- **File:** `ml/evaluate.py:41`
- **Issue:** `encode_features(df)` re-fits encoders on all data on every evaluation; only the test-split subset is needed.
- **Fix:** encode once from `train_test_split` output (the fitted encoders only need the training split), or reuse saved encoders.

### M5. Absolute imports break `import api.main` from repo root
- **File:** `api/main.py:8-11` (`from db import ...`, `from model import ...`, `from schemas import ...`)
- **Issue:** the API modules are only importable when `api/` (and `ml/` for `api/model.py`) are on `sys.path`. Any tooling that does `import api.main` from the repo root fails. Jenkins-style `pytest` runs need a path bootstrap.
- **Fix:** use package-relative imports (`from . import db`) or make `api/` a proper package. The QA suite works around this via `tests/conftest.py`.

## LOW

### L1. Deprecated pydantic v2 `Config` class
- **File:** `api/schemas.py:12-21`
- **Issue:** `class Config: json_schema_extra = {...}` is the pydantic v1 style; v2 prefers `model_config = ConfigDict(json_schema_extra=...)`. Works today but warns on newer pydantic.

### L2. `/predictions` has no error handling
- **File:** `api/main.py:51-65`
- **Issue:** DB outage on `GET /predictions` → unhandled 500. A 503 with a clear message is friendlier.

### L3. MLflow model-registry `stages` API is deprecated
- **File:** `api/model.py:24`, `ml/evaluate.py:30`
- **Issue:** `MlflowClient.get_latest_versions(..., stages=["Production","None"])` warns as deprecated since MLflow 2.9 (stages being removed in a future major). Fine on the pinned 2.10.0; will break on MLflow 4.x.
- **Fix:** use `mlflow.registered_model.endpoints` / `get_latest_versions` without stages, or alias-based deployment.

## Verified-passing behavior (no bug)

- Train pipeline: 80/20 split (`random_state=42`, stratified), `RandomForestClassifier(n_estimators=300, max_depth=10, random_state=42)`, MLflow params/metrics logging, model registration as `churn-model`, `model.pkl` artifact — all covered by `tests/test_train_pipeline.py`.
- Accuracy gate: `ml/evaluate.py` exits 1 below 0.70, 0 at/above — covered by `tests/test_evaluate.py`.
