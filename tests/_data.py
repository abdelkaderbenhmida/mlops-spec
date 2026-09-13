# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Shared test data for the credit risk ML pipeline (German Credit Data)."""
import pandas as pd
import numpy as np

RNG = np.random.default_rng(99)

CHECKING_STATUS = ["A11", "A12", "A13", "A14"]
CREDIT_HISTORY = ["A30", "A31", "A32", "A33", "A34"]
PURPOSE = ["A40", "A41", "A42", "A43", "A44", "A45", "A46", "A47", "A48", "A49", "A410"]
SAVINGS_STATUS = ["A61", "A62", "A63", "A64", "A65"]
EMPLOYMENT = ["A71", "A72", "A73", "A74", "A75"]
PERSONAL_STATUS = ["A91", "A92", "A93", "A94", "A95"]
OTHER_PARTIES = ["A101", "A102", "A103"]
PROPERTY_MAGNITUDE = ["A121", "A122", "A123", "A124"]
OTHER_PAYMENT_PLANS = ["A141", "A142", "A143"]
HOUSING = ["A151", "A152", "A153"]
JOB = ["A171", "A172", "A173", "A174"]
OWN_TELEPHONE = ["A191", "A192"]
FOREIGN_WORKER = ["A201", "A202"]


def build_subset_df(n: int = 500) -> pd.DataFrame:
    """Build a small synthetic German Credit Data dataframe for tests."""
    rows = []
    for _ in range(n):
        age = int(RNG.integers(18, 76))
        duration = int(RNG.integers(1, 73))
        credit_amount = int(RNG.integers(250, 20001))
        checking_status = RNG.choice(CHECKING_STATUS)
        credit_history = RNG.choice(CREDIT_HISTORY)
        savings_status = RNG.choice(SAVINGS_STATUS)
        purpose = RNG.choice(PURPOSE)

        logit = (
            -1.8
            + 1.2 * (credit_history == "A34")
            + 0.7 * (credit_history == "A33")
            + 0.6 * (checking_status in ("A11", "A12"))
            - 0.5 * (savings_status in ("A64", "A65"))
            + 0.02 * (duration - 36) / 10
            - 0.03 * (age - 40) / 10
            - 0.2 * np.log1p(credit_amount / 1000)
        )
        p_default = 1 / (1 + np.exp(-logit))
        target = int(RNG.random() < p_default)

        rows.append({
            "checking_status": checking_status,
            "duration": duration,
            "credit_history": credit_history,
            "purpose": purpose,
            "credit_amount": credit_amount,
            "savings_status": savings_status,
            "employment": RNG.choice(EMPLOYMENT),
            "installment_rate": int(RNG.integers(1, 5)),
            "personal_status": RNG.choice(PERSONAL_STATUS),
            "other_parties": RNG.choice(OTHER_PARTIES),
            "residence_since": int(RNG.integers(1, 5)),
            "property_magnitude": RNG.choice(PROPERTY_MAGNITUDE),
            "age": age,
            "other_payment_plans": RNG.choice(OTHER_PAYMENT_PLANS),
            "housing": RNG.choice(HOUSING),
            "existing_credits": int(RNG.integers(1, 5)),
            "job": RNG.choice(JOB),
            "num_dependents": int(RNG.integers(1, 3)),
            "own_telephone": RNG.choice(OWN_TELEPHONE),
            "foreign_worker": RNG.choice(FOREIGN_WORKER),
            "target": target,
        })

    return pd.DataFrame(rows)