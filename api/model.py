"""Model loading and prediction logic for the churn prediction API."""
import os

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient


_model = None
_model_version = None


def load_model():
    """Load the registered model from MLflow on startup."""
    global _model, _model_version

    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
    model_name = os.environ.get("MLFLOW_MODEL_NAME", "churn-model")

    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()

    try:
        versions = client.get_latest_versions(model_name, stages=["Production", "None"])
        if not versions:
            raise ValueError(f"No registered model found: {model_name}")
        version = versions[0]
        model_uri = f"models:/{model_name}/{version.version}"

        _model = mlflow.sklearn.load_model(model_uri)
        _model_version = version.version
        print(f"Loaded model {model_name} version {_model_version} from {tracking_uri}")
    except Exception as e:
        print(f"ERROR loading model: {e}")
        raise


def get_model_version() -> str | None:
    """Return the loaded model version."""
    return _model_version


def predict(input_data: dict) -> tuple[int, float]:
    """Run prediction on input data and return (prediction, probability)."""
    if _model is None:
        load_model()

    import pandas as pd
    from preprocess import apply_encoders, CATEGORICAL_COLUMNS

    # Create DataFrame with expected columns
    df = pd.DataFrame([input_data])

    # Load encoders (need to match training encoders)
    # For simplicity, we'll re-fit on training data structure
    # In production, encoders should be saved with the model
    from preprocess import load_data, encode_features

    train_df = load_data()
    _, _, encoders = encode_features(train_df)

    # Apply encoders
    X = apply_encoders(df, encoders)

    pred = _model.predict(X)[0]
    proba = _model.predict_proba(X)[0][1]

    return int(pred), float(proba)