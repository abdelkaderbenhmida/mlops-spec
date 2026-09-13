#!/usr/bin/env python3
# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Generate realistic synthetic Telco customer churn data (Kaggle-style).

Produces ~7000 rows with the same columns and value distributions as the
public Telco Customer Churn dataset (minus customerID).
"""
import random

random.seed(42)

CONTRACTS = ["Month-to-month", "One year", "Two year"]
PAYMENT_METHODS = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)",
]

# Churn probability per contract type (longer contracts churn less)
CONTRACT_CHURN = {
    "Month-to-month": 0.45,
    "One year": 0.16,
    "Two year": 0.03,
}
PAYMENT_CHURN = {
    "Electronic check": 0.35,
    "Mailed check": 0.22,
    "Bank transfer (automatic)": 0.12,
    "Credit card (automatic)": 0.10,
}


def rand_tenure(contract):
    if contract == "Month-to-month":
        return random.randint(0, 24)
    if contract == "One year":
        return random.randint(12, 24)
    return random.randint(24, 72)


def generate_row():
    contract = random.choices(CONTRACTS, weights=[0.55, 0.24, 0.21])[0]
    payment = random.choices(
        PAYMENT_METHODS, weights=[0.35, 0.20, 0.23, 0.22]
    )[0]
    tenure = rand_tenure(contract)
    monthly = round(random.uniform(18.0, 120.0), 2)
    total = round(monthly * tenure, 2)

    p = 0.04  # base churn
    p += CONTRACT_CHURN[contract]
    p += PAYMENT_CHURN[payment]
    p += max(0.0, (monthly - 60.0) / 300.0)
    p -= min(0.25, tenure / 200.0)
    p = min(max(p, 0.0), 0.97)

    churn = 1 if random.random() < p else 0
    return tenure, monthly, total, contract, payment, churn


def main():
    rows = ["tenure,MonthlyCharges,TotalCharges,Contract,PaymentMethod,Churn"]
    for _ in range(7000):
        t, m, tot, c, pm, ch = generate_row()
        rows.append(f"{t},{m},{tot},{c},{pm},{ch}")
    out = "ml/data/churn.csv"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")
    print(f"wrote {out} with {len(rows) - 1} data rows")


if __name__ == "__main__":
    main()
