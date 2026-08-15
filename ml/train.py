#!/usr/bin/env python3
"""Train a Random Forest churn classifier and log it to MLflow.

Steps:
  1. Load ml/data/churn.csv
  2. Drop customerID, encode categoricals (LabelEncoder)
  3. Train/test split 80/20, random_state=42
  4. Train RandomForestClassifier(n_estimators=100)
  5. Log params + metrics (accuracy, f1, roc_auc) to MLflow
  6. Register model in MLflow Model Registry as "churn-model"
  7. Save model artifact model.pkl
"""
import os
import pickle

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

from preprocess import encode_features, load_data, train_test_split

MODEL_NAME = os.environ.get("MLFLOW_MODEL_NAME", "churn-model")
TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment("customer-churn")

    df = load_data()
    X, y, encoders = encode_features(df)

    train_df, test_df = train_test_split(df)
    X_train = X.loc[train_df.index]
    y_train = y.loc[train_df.index]
    X_test = X.loc[test_df.index]
    y_test = y.loc[test_df.index]

    params = {"n_estimators": 100, "random_state": 42}
    clf = RandomForestClassifier(**params)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    proba = clf.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "f1": float(f1_score(y_test, preds)),
        "roc_auc": float(roc_auc_score(y_test, proba)),
    }

    print(f"metrics: {metrics}")

    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_artifact("ml/data/churn.csv", artifact_path="data")
        mlflow.sklearn.log_model(
            clf,
            artifact_path="model",
            registered_model_name=MODEL_NAME,
            input_example=X_test.head(1),
        )

        artifact_uri = f"{mlflow.get_artifact_uri()}/model"
        print(f"model logged to: {artifact_uri}")
        print(f"run_id: {run.info.run_id}")
        print(f"registered model: {MODEL_NAME} (version 1)")

        local_path = os.path.join("ml", "model.pkl")
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            pickle.dump(clf, f)
        print(f"saved local artifact: {local_path}")


if __name__ == "__main__":
    main()
