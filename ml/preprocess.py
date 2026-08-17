"""Shared preprocessing for the churn ML pipeline.

Encodes categorical features with LabelEncoder and splits the data.
Both train.py and evaluate.py import from here so the encoding is
identical between training and evaluation.
"""
import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder

CATEGORICAL_COLUMNS = ["Contract", "PaymentMethod"]
NUMERIC_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges"]
TARGET = "Churn"

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.environ.get(
    "CHURN_DATA_PATH", os.path.join(_REPO_ROOT, "ml", "data", "churn.csv")
)


def load_data(path=None):
    path = path or DATA_PATH
    df = pd.read_csv(path)
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])
    return df


def encode_features(df):
    """Return (X, y, encoders) with categorical columns LabelEncoded."""
    X = df[CATEGORICAL_COLUMNS + NUMERIC_COLUMNS].copy()
    y = df[TARGET].astype(int)

    encoders = {}
    for col in CATEGORICAL_COLUMNS:
        enc = LabelEncoder()
        X[col] = enc.fit_transform(X[col])
        encoders[col] = enc
    return X, y, encoders


def apply_encoders(df, encoders):
    """Apply pre-fitted encoders to new data (e.g. the test set)."""
    X = df[CATEGORICAL_COLUMNS + NUMERIC_COLUMNS].copy()
    for col in CATEGORICAL_COLUMNS:
        enc = encoders[col]
        X[col] = enc.transform(X[col])
    return X


def train_test_split(df, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split as _split

    return _split(
        df, test_size=test_size, random_state=random_state, stratify=df[TARGET]
    )
