#!/usr/bin/env python3
"""Generate realistic synthetic credit risk data.

Based on Kaggle "Give Me Some Credit" dataset distributions.
Features mirror real banking data: income, debt, credit history, delinquency.

Output: ml/data/credit.csv (50K rows, ~7% default rate)
Deterministic (seed=42) for reproducibility.
"""

import argparse
import os

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
N_DEFAULTS = 50_000
DEFAULT_RATE = 0.067  # 6.7% default rate (matches real data)

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credit.csv")


def generate(n_rows: int = N_DEFAULTS) -> pd.DataFrame:
    rows = []
    for i in range(n_rows):
        age = int(RNG.integers(18, 80))
        income = max(500, float(RNG.lognormal(10.5, 0.8)))  # median ~36K
        debt_ratio = float(np.clip(RNG.beta(2, 5), 0, 10))  # mostly <1
        num_open_credit = int(RNG.poisson(5))
        num_dep = int(RNG.poisson(1))
        monthly_income = income / 12
        # --- Generate correlated features (high debt → more late payments) ---
        # Base risk score drives both feature correlation and default
        base_risk = float(RNG.beta(2, 5))  # 0-1 scale

        # High-risk borrowers have more late payments, higher utilization
        num_30_59_late = int(RNG.poisson(0.3 + 2.0 * base_risk))
        num_60_89_late = int(RNG.poisson(0.1 + 1.5 * base_risk))
        num_90_late = int(RNG.poisson(0.05 + 1.0 * base_risk))
        revolving_util = float(np.clip(RNG.beta(2 + 3 * base_risk, 2 + 2 * (1 - base_risk)) * 100, 0, 100))
        num_open_credit = int(RNG.poisson(3 + 4 * base_risk))
        num_mortgages = int(RNG.poisson(0.8))
        num_family_members = int(RNG.poisson(0.5))

        # --- Default probability (strong signal) ---
        logit = (
            -2.8
            + 1.5 * num_90_late
            + 1.0 * num_60_89_late
            + 0.6 * num_30_59_late
            + 0.03 * (revolving_util - 40) / 10
            + 0.8 * np.log1p(debt_ratio)
            - 0.02 * (age - 40) / 10
            + 0.6 * (num_open_credit > 8)
            - 0.7 * np.log1p(income / 10000)
        )
        p_default = 1 / (1 + np.exp(-logit))
        default = int(RNG.random() < p_default)

        rows.append({
            "customer_id": f"CUST-{i:06d}",
            "age": age,
            "income": round(income, 2),
            "monthly_income": round(monthly_income, 2),
            "debt_ratio": round(debt_ratio, 4),
            "revolving_utilization": round(revolving_util, 2),
            "num_open_credit_lines": num_open_credit,
            "num_dependents": num_dep,
            "num_30_59_days_late": num_30_59_late,
            "num_60_89_days_late": num_60_89_late,
            "num_90_days_late": num_90_late,
            "num_mortgages": num_mortgages,
            "number_real_estate_loans": num_mortgages,
            "default": default,
        })

    df = pd.DataFrame(rows)
    return df


def main():
    parser = argparse.ArgumentParser(description="Generate credit risk data")
    parser.add_argument("-n", "--rows", type=int, default=N_DEFAULTS)
    parser.add_argument("-o", "--output", default=OUTPUT)
    args = parser.parse_args()

    df = generate(args.rows)
    df.to_csv(args.output, index=False)
    rate = df["default"].mean() * 100
    print(f"Wrote {len(df):,} rows -> {args.output}")
    print(f"  default={df['default'].sum():,} ({rate:.1f}%)")


if __name__ == "__main__":
    main()
