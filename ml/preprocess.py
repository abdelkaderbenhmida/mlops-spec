# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Shared preprocessing for the credit risk ML pipeline.

Encodes categorical features with OneHotEncoder, scales numeric features,
and splits the data. Both train.py and evaluate.py import from here so
the encoding is identical between training and evaluation.
"""
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split as _split

FEATURE_COLS = [
    "checking_status", "duration", "credit_history", "purpose", "credit_amount",
    "savings_status", "employment", "installment_rate", "personal_status",
    "other_parties", "residence_since", "property_magnitude", "age",
    "other_payment_plans", "housing", "existing_credits", "job",
    "num_dependents", "own_telephone", "foreign_worker"
]

CATEGORICAL_COLS = [
    "checking_status", "credit_history", "purpose", "savings_status",
    "employment", "personal_status", "other_parties", "property_magnitude",
    "other_payment_plans", "housing", "job", "own_telephone", "foreign_worker"
]

NUMERIC_COLS = [
    "duration", "credit_amount", "installment_rate", "residence_since",
    "age", "existing_credits", "num_dependents"
]

TARGET = "target"

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.environ.get(
    "CREDIT_DATA_PATH", os.path.join(_REPO_ROOT, "ml", "data", "credit.csv")
)

_preprocessor = None


def load_data(path=None):
    path = path or DATA_PATH
    df = pd.read_csv(path)
    return df


def _get_preprocessor():
    global _preprocessor
    if _preprocessor is None:
        _preprocessor = ColumnTransformer(
            transformers=[
                ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL_COLS),
                ("num", StandardScaler(), NUMERIC_COLS),
            ],
            remainder="drop",
            verbose_feature_names_out=False,
        )
    return _preprocessor


def encode_features(df):
    """Return (X, y) with all features encoded as numeric matrix."""
    preprocessor = _get_preprocessor()
    X = preprocessor.fit_transform(df[FEATURE_COLS])
    y = df[TARGET].astype(int).values
    return X, y


def apply_encoders(df, encoders=None):
    """Apply fitted preprocessor to new data (for API inference)."""
    preprocessor = _get_preprocessor()
    X = preprocessor.transform(df[FEATURE_COLS])
    return X


def train_test_split(df, test_size=0.2, random_state=42):
    return _split(
        df, test_size=test_size, random_state=random_state, stratify=df[TARGET]
    )


def get_feature_names():
    """Get feature names after one-hot encoding."""
    preprocessor = _get_preprocessor()
    return preprocessor.get_feature_names_out().tolist()