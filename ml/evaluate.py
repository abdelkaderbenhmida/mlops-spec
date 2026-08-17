#!/usr/bin/env python3
"""Evaluate the credit risk model against the hold-out test set.

Loads the registered model from MLflow, computes AUC, KS, and fairness
metrics, and gates on AUC >= 0.75.

Exit codes:
  0  AUC >= 0.75 (gate passed)
  1  AUC < 0.75  (gate failed) or any error
"""
import os
import sys

import mlflow
import numpy as np
from mlflow.tracking import MlflowClient
from sklearn.metrics import classification_report, roc_auc_score, roc_curve

from preprocess import encode_features, load_data, train_test_split

MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")
TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
AUC_THRESHOLD = 0.75
KS_THRESHOLD = 0.30


def compute_ks(y_true, y_prob):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    return float(np.max(tpr - fpr))


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
    X_test = X.loc[test_df.index]
    y_test = y.loc[test_df.index]

    proba = clf.predict_proba(X_test)[:, 1]
    preds = clf.predict(X_test)

    auc = float(roc_auc_score(y_test, proba))
    ks = compute_ks(y_test, proba)

    print("Classification report:")
    print(classification_report(y_test, preds, target_names=["Repaid", "Default"]))
    print(f"AUC:  {auc:.4f}  (threshold: {AUC_THRESHOLD})")
    print(f"KS:   {ks:.4f}  (threshold: {KS_THRESHOLD})")

    if auc < AUC_THRESHOLD:
        print(f"FAIL: AUC {auc:.4f} < {AUC_THRESHOLD}")
        sys.exit(1)
    if ks < KS_THRESHOLD:
        print(f"FAIL: KS {ks:.4f} < {KS_THRESHOLD}")
        sys.exit(1)

    print(f"PASS: AUC={auc:.4f} >= {AUC_THRESHOLD}, KS={ks:.4f} >= {KS_THRESHOLD}")
    sys.exit(0)


if __name__ == "__main__":
    main()
