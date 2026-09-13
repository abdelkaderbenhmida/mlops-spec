# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Model loading and prediction logic for the credit risk prediction API."""
import os
import sys

import mlflow
import mlflow.xgboost
from mlflow.tracking import MlflowClient

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_DIR = os.path.join(PROJECT_ROOT, "ml")
for _path in (PROJECT_ROOT, ML_DIR):
    if _path not in sys.path:
        sys.path.insert(0, _path)

from preprocess import apply_encoders  # noqa: E402

_model = None
_model_version = None


def load_model():
    """Load the registered model from MLflow on startup."""
    global _model, _model_version

    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://localhost:5000")
    model_name = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")

    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()

    try:
        versions = client.get_latest_versions(model_name, stages=["Production", "Staging", "None"])
        if not versions:
            raise ValueError(f"No registered model found: {model_name}")
        version = versions[0]
        model_uri = f"models:/{model_name}/{version.version}"

        _model = mlflow.xgboost.load_model(model_uri)
        _model_version = str(version.version)
        print(f"Loaded model {model_name} version {_model_version} from {tracking_uri}")
    except Exception as e:
        print(f"ERROR loading model: {e}")
        raise


def get_model_version() -> str | None:
    return _model_version


def predict(input_data: dict) -> tuple[int, float]:
    """Run prediction on input data and return (prediction, probability)."""
    if _model is None:
        load_model()

    import pandas as pd

    df = pd.DataFrame([input_data])
    X = apply_encoders(df)

    prediction = int(_model.predict(X)[0])
    probability = float(_model.predict_proba(X)[0][1])

    return prediction, probability


def risk_tier(probability: float) -> str:
    if probability < 0.1:
        return "low"
    elif probability < 0.3:
        return "medium"
    elif probability < 0.6:
        return "high"
    else:
        return "critical"