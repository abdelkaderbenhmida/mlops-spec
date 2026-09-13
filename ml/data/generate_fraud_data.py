#!/usr/bin/env python3
# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Generate realistic synthetic credit card fraud transaction data.

Produces 100K transactions with ~10% fraud rate.
Fraud follows clear patterns: high amounts + unusual hours + international +
new cards + high transaction frequency.

Output: ml/data/fraud.csv
Deterministic (seed=42) for reproducibility.
"""
import argparse
import os

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
N_ROWS = 100_000

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fraud.csv")

MERCHANT_CATEGORIES = [
    "grocery", "restaurant", "gas_station", "online_retail",
    "electronics", "jewelry", "travel", "entertainment",
    "pharmacy", "clothing", "hardware", "education",
]

CATEGORY_FRAUD_MULT = {
    "online_retail": 2.0, "jewelry": 3.0, "electronics": 2.0,
    "travel": 2.5, "entertainment": 1.5, "grocery": 0.3,
    "restaurant": 0.4, "gas_station": 0.5, "pharmacy": 0.6,
    "clothing": 0.7, "hardware": 0.5, "education": 0.2,
}


def generate(n_rows: int = N_ROWS) -> pd.DataFrame:
    rows = []
    for i in range(n_rows):
        txn_amount = float(RNG.lognormal(3.5, 1.2))
        merchant_category = RNG.choice(MERCHANT_CATEGORIES)
        hour_of_day = int(RNG.integers(0, 24))
        day_of_week = int(RNG.integers(0, 7))
        distance_from_home = float(RNG.exponential(15))
        is_international = int(RNG.random() < 0.08)
        card_age_days = int(RNG.integers(1, 2000))
        num_transactions_24h = int(RNG.poisson(3))
        avg_transaction_amount_30d = float(RNG.lognormal(3.2, 0.8))
        is_weekend = int(day_of_week >= 5)

        # --- Fraud probability: strong correlated signal ---
        p_fraud = 0.005  # base

        # High amount is the strongest signal
        if txn_amount > 500:
            p_fraud += 0.15
        elif txn_amount > 200:
            p_fraud += 0.08
        elif txn_amount > 100:
            p_fraud += 0.03

        # Night hours (10pm-5am)
        if hour_of_day >= 22 or hour_of_day <= 5:
            p_fraud += 0.10

        # International
        if is_international:
            p_fraud += 0.12

        # New card
        if card_age_days < 90:
            p_fraud += 0.10
        elif card_age_days < 180:
            p_fraud += 0.04

        # High transaction frequency
        if num_transactions_24h >= 10:
            p_fraud += 0.12
        elif num_transactions_24h >= 7:
            p_fraud += 0.08
        elif num_transactions_24h >= 5:
            p_fraud += 0.04

        # Amount way above average
        if avg_transaction_amount_30d > 0 and txn_amount > 5 * avg_transaction_amount_30d:
            p_fraud += 0.15
        elif avg_transaction_amount_30d > 0 and txn_amount > 3 * avg_transaction_amount_30d:
            p_fraud += 0.08

        # Long distance
        if distance_from_home > 50:
            p_fraud += 0.06
        elif distance_from_home > 25:
            p_fraud += 0.03

        # Category modifier
        p_fraud *= CATEGORY_FRAUD_MULT.get(merchant_category, 1.0)

        # Weekend
        if is_weekend:
            p_fraud *= 1.15

        p_fraud = min(max(p_fraud, 0.001), 0.95)
        is_fraud = int(RNG.random() < p_fraud)

        rows.append({
            "transaction_id": f"TXN-{i:08d}",
            "transaction_amount": round(txn_amount, 2),
            "merchant_category": merchant_category,
            "hour_of_day": hour_of_day,
            "day_of_week": day_of_week,
            "distance_from_home": round(distance_from_home, 2),
            "is_international": is_international,
            "card_age_days": card_age_days,
            "num_transactions_24h": num_transactions_24h,
            "avg_transaction_amount_30d": round(avg_transaction_amount_30d, 2),
            "is_weekend": is_weekend,
            "is_fraud": is_fraud,
        })

    df = pd.DataFrame(rows)
    return df


def main():
    parser = argparse.ArgumentParser(description="Generate fraud detection data")
    parser.add_argument("-n", "--rows", type=int, default=N_ROWS)
    parser.add_argument("-o", "--output", default=OUTPUT)
    args = parser.parse_args()

    df = generate(args.rows)
    df.to_csv(args.output, index=False)
    rate = df["is_fraud"].mean() * 100
    print(f"Wrote {len(df):,} rows -> {args.output}")
    print(f"  fraud={df['is_fraud'].sum():,} ({rate:.1f}%)")
    print(f"  features: {[c for c in df.columns if c not in ('transaction_id', 'is_fraud')]}")


if __name__ == "__main__":
    main()
