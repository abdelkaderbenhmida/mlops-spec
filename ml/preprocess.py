"""Shared preprocessing for the credit risk ML pipeline.

Encodes categorical features, handles missing values, and splits the data.
Both train.py and evaluate.py import from here so the encoding is
identical between training and evaluation.
"""
import os

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

NUMERIC_COLUMNS = [
    "age", "income", "monthly_income", "debt_ratio",
    "revolving_utilization", "num_open_credit_lines", "num_dependents",
    "num_30_59_days_late", "num_60_89_days_late", "num_90_days_late",
    "num_mortgages", "number_real_estate_loans",
]
TARGET = "default"

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.environ.get(
    "CREDIT_DATA_PATH", os.path.join(_REPO_ROOT, "ml", "data", "credit.csv")
)


def load_data(path=None):
    path = path or DATA_PATH
    df = pd.read_csv(path)
    if "customer_id" in df.columns:
        df = df.drop(columns=["customer_id"])
    return df


def encode_features(df):
    """Return (X, y) with all features numeric."""
    X = df[NUMERIC_COLUMNS].copy()
    y = df[TARGET].astype(int)
    return X, y


def apply_encoders(df, encoders=None):
    """Apply feature matrix (encoders kept for API compatibility)."""
    return df[NUMERIC_COLUMNS].copy()


def train_test_split(df, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split as _split

    return _split(
        df, test_size=test_size, random_state=random_state, stratify=df[TARGET]
    )
