"""Shared synthetic churn data builder for the QA suite.

Mirrors the schema of ml/data/churn.csv (see mlops-platform-spec.md) so
train/evaluate tests run fast on a small in-memory frame instead of the
full 7k-row CSV, without depending on the CSV being present at test time.

The Churn label has learnable signal (low tenure + high monthly charges push
toward churn) so a trained Random Forest beats the 0.70 accuracy gate on the
hold-out split deterministically.
"""
import numpy as np
import pandas as pd

CONTRACTS = ["Month-to-month", "One year", "Two year"]
PAYMENTS = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)",
]


def build_subset_df(n=120, seed=42):
    """Deterministic synthetic churn frame with both target classes present."""
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(n):
        tenure = int(rng.integers(0, 73))
        monthly = round(float(rng.uniform(18.0, 119.0)), 2)
        score = (1.0 - tenure / 72.0) * 0.6 + (monthly / 119.0) * 0.4
        churn = 1 if score > 0.52 + float(rng.uniform(-0.18, 0.18)) else 0
        rows.append(
            {
                "tenure": tenure,
                "MonthlyCharges": monthly,
                "TotalCharges": round(float(rng.uniform(0.0, 9000.0)), 2),
                "Contract": str(rng.choice(CONTRACTS)),
                "PaymentMethod": str(rng.choice(PAYMENTS)),
                "Churn": int(churn),
            }
        )
    df = pd.DataFrame(rows)
    # Guarantee both classes appear.
    df.loc[0, "Churn"] = 0
    df.loc[1, "Churn"] = 1
    return df
