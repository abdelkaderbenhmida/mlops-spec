#!/usr/bin/env python3
"""Train a credit risk classifier and log it to MLflow.

Steps:
  1. Load ml/data/credit.csv (German Credit Data)
  2. Encode categorical features with OneHotEncoder, scale numeric with StandardScaler
  3. Train/test split 80/20, stratified, random_state=42
  4. Train GradientBoostingClassifier
  5. Log params + metrics (AUC, F1, precision, recall) to MLflow
  6. Register model in MLflow Model Registry as "credit-risk-model"
  7. Save model artifact model.pkl
"""
import os
import pickle

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from preprocess import encode_features, load_data, train_test_split

MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "credit-risk-model")
TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment("credit-risk")

    df = load_data()
    X, y = encode_features(df)

    train_df, test_df = train_test_split(df)
    X_train = X[train_df.index]
    y_train = y[train_df.index]
    X_test = X[test_df.index]
    y_test = y[test_df.index]

    params = {
        "n_estimators": 300,
        "max_depth": 6,
        "learning_rate": 0.05,
        "subsample": 0.8,
        "min_samples_split": 5,
        "min_samples_leaf": 2,
        "random_state": 42,
    }
    clf = GradientBoostingClassifier(**params)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    proba = clf.predict_proba(X_test)[:, 1]

    metrics = {
        "f1": float(f1_score(y_test, preds, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, proba)),
        "precision": float(precision_score(y_test, preds, zero_division=0)),
        "recall": float(recall_score(y_test, preds, zero_division=0)),
    }

    print(f"metrics: {metrics}")

    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_param("n_features", X_train.shape[1])
        mlflow.log_param("data_source", "german.data (UCI Statlog)")
        mlflow.log_param("default_rate", f"{y_train.mean():.4f}")

        mlflow.sklearn.log_model(clf, "model")
        mlflow.log_artifact("ml/data/credit.csv", artifact_path="data")

        model_uri = f"runs:/{run.info.run_id}/model"
        registered = mlflow.register_model(model_uri, MODEL_NAME)
        client = mlflow.MlflowClient()
        client.transition_model_version_stage(
            name=MODEL_NAME, version=registered.version, stage="Staging"
        )
        print(f"Registered {MODEL_NAME} version {registered.version} in Staging")

    model_path = os.path.join(_REPO_ROOT, "ml", "model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
    print(f"Saved model to {model_path}")
    print(f"AUC={metrics['roc_auc']:.4f} F1={metrics['f1']:.4f}")


if __name__ == "__main__":
    main()