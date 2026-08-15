#!/usr/bin/env python3
"""Evaluate the registered churn model against the hold-out test set.

Loads the latest version of the "churn-model" registered model from MLflow,
runs predictions on the test split, prints a classification report, and
exits non-zero if accuracy < 0.75 (CI gate).

Exit codes:
  0  accuracy >= 0.75 (gate passed)
  1  accuracy < 0.75  (gate failed) or any error
"""
import os
import sys

import mlflow
from mlflow.tracking import MlflowClient
from sklearn.metrics import accuracy_score, classification_report

from preprocess import apply_encoders, encode_features, load_data, train_test_split

MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "churn-model")
TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
ACCURACY_THRESHOLD = 0.75


def main():
    mlflow.set_tracking_uri(TRACKING_URI)

    client = MlflowClient()
    versions = client.get_latest_versions(MODEL_NAME, stages=["Production", "None"])
    if not versions:
        print(f"ERROR: no registered model named '{MODEL_NAME}' found")
        sys.exit(1)
    version = versions[0]
    print(f"evaluating {MODEL_NAME} version {version.version}")

    model_uri = f"models:/{MODEL_NAME}/{version.version}"
    clf = mlflow.sklearn.load_model(model_uri)

    df = load_data()
    X_all, y_all, encoders = encode_features(df)
    train_df, test_df = train_test_split(df)

    X_test = apply_encoders(test_df, encoders)
    y_test = y_all.loc[test_df.index]

    preds = clf.predict(X_test)
    acc = float(accuracy_score(y_test, preds))

    print("Classification report:")
    print(classification_report(y_test, preds, target_names=["No churn", "Churn"]))
    print(f"Accuracy: {acc:.4f}")

    if acc < ACCURACY_THRESHOLD:
        print(f"FAIL: accuracy {acc:.4f} < {ACCURACY_THRESHOLD}")
        sys.exit(1)

    print(f"PASS: accuracy {acc:.4f} >= {ACCURACY_THRESHOLD}")
    sys.exit(0)


if __name__ == "__main__":
    main()
