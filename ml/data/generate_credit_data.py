#!/usr/bin/env python3
"""Load German Credit Data (UCI Statlog) from /tmp/realdata/german.data.

Features: 13 categorical (A-codes), 8 numeric
Target: 1=good (repaid), 2=bad (default) -> map to 0/1 (1=default)
Output: ml/data/credit.csv (1000 rows, ~30% default rate)
Deterministic seed for reproducibility.
"""

import os

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
DATA_SOURCE = "/tmp/realdata/german.data"
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credit.csv")

COLUMN_NAMES = [
    "checking_status", "duration", "credit_history", "purpose", "credit_amount",
    "savings_status", "employment", "installment_rate", "personal_status",
    "other_parties", "residence_since", "property_magnitude", "age",
    "other_payment_plans", "housing", "existing_credits", "job",
    "num_dependents", "own_telephone", "foreign_worker", "target"
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


def load_german_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_SOURCE, sep=r"\s+", header=None, names=COLUMN_NAMES)
    df["target"] = (df["target"] == 2).astype(int)
    return df


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Load German Credit Data")
    parser.add_argument("-o", "--output", default=OUTPUT)
    args = parser.parse_args()

    df = load_german_data()
    df.to_csv(args.output, index=False)
    rate = df["target"].mean() * 100
    print(f"Wrote {len(df):,} rows -> {args.output}")
    print(f"  default={df['target'].sum():,} ({rate:.1f}%)")
    print(f"  Categorical: {len(CATEGORICAL_COLS)}")
    print(f"  Numeric: {len(NUMERIC_COLS)}")


if __name__ == "__main__":
    main()