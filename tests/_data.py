"""Shared test data for the credit risk ML pipeline."""
import pandas as pd
import numpy as np

RNG = np.random.default_rng(99)


def build_subset_df(n: int = 500) -> pd.DataFrame:
    """Build a small synthetic credit risk dataframe for tests."""
    rows = []
    for i in range(n):
        age = int(RNG.integers(20, 70))
        income = float(RNG.lognormal(10.5, 0.8))
        monthly_income = income / 12
        debt_ratio = float(np.clip(RNG.beta(2, 5), 0, 10))
        util = float(np.clip(RNG.beta(3, 2) * 100, 0, 100))
        late30 = int(RNG.poisson(0.2))
        late60 = int(RNG.poisson(0.08))
        late90 = int(RNG.poisson(0.03))
        credit_lines = int(RNG.poisson(5))
        mortgages = int(RNG.poisson(0.7))
        dependents = int(RNG.poisson(1))

        logit = -3.5 + 0.8 * late90 + 0.5 * late60 + 0.3 * late30 + 0.02 * (util - 50) / 10
        p = 1 / (1 + np.exp(-logit))
        default = int(RNG.random() < p)

        rows.append({
            "age": age,
            "income": round(income, 2),
            "monthly_income": round(monthly_income, 2),
            "debt_ratio": round(debt_ratio, 4),
            "revolving_utilization": round(util, 2),
            "num_open_credit_lines": credit_lines,
            "num_dependents": dependents,
            "num_30_59_days_late": late30,
            "num_60_89_days_late": late60,
            "num_90_days_late": late90,
            "num_mortgages": mortgages,
            "number_real_estate_loans": mortgages,
            "default": default,
        })

    return pd.DataFrame(rows)
