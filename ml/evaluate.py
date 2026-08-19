#!/usr/bin/env python3
"""Evaluate the credit risk model against the hold-out test set.

Loads the registered model from MLflow, computes AUC, F1, precision, recall,
and gates on AUC >= 0.75, F1 >= 0.30.

Exit codes:
  0  AUC >= 0.75 AND F1 >= 0.30 (gate passed)
  1  gate failed or any error
"""
import os
import sys

import mlflow
from mlflow.tracking import MlflowClient
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score, roc_auc_score

from preprocess import encode_features, load_data, train_test_split

MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")
TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
AUC_THRESHOLD = 0.75
F1_THRESHOLD = 0.30


def main():
    mlflow.set_tracking_uri(TRACKING_URI)

    client = MlflowClient()
    versions = client.get_latest_versions(MODEL_NAME, stages=["Production", "Staging", "None"])
    if not versions:
        print(f"ERROR: no registered model named '{MODEL_NAME}' found")
        sys.exit(1)
    version = versions[0]
    print(f"Evaluating {MODEL_NAME} version {version.version}")

    model_uri = f"models:/{MODEL_NAME}/{version.version}"
    clf = mlflow.sklearn.load_model(model_uri)

    df = load_data()
    X, y = encode_features(df)
    train_df, test_df = train_test_split(df)
    X_test = X[test_df.index]
    y_test = y[test_df.index]

    proba = clf.predict_proba(X_test)[:, 1]
    preds = clf.predict(X_test)

    auc = float(roc_auc_score(y_test, proba))
    f1 = float(f1_score(y_test, preds, zero_division=0))
    prec = float(precision_score(y_test, preds, zero_division=0))
    rec = float(recall_score(y_test, preds, zero_division=0))

    print("Classification report:")
    print(classification_report(y_test, preds, target_names=["Good", "Bad"]))
    print(f"AUC:  {auc:.4f}  (threshold: {AUC_THRESHOLD})")
    print(f"F1:   {f1:.4f}  (threshold: {F1_THRESHOLD})")
    print(f"Precision: {prec:.4f}  Recall: {rec:.4f}")

    if auc < AUC_THRESHOLD:
        print(f"FAIL: AUC {auc:.4f} < {AUC_THRESHOLD}")
        sys.exit(1)
    if f1 < F1_THRESHOLD:
        print(f"FAIL: F1 {f1:.4f} < {F1_THRESHOLD}")
        sys.exit(1)

    print(f"PASS: AUC={auc:.4f} >= {AUC_THRESHOLD}, F1={f1:.4f} >= {F1_THRESHOLD}")
    sys.exit(0)


if __name__ == "__main__":
    main()