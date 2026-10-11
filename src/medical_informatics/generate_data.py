"""Generate deterministic synthetic clinical-style data for education only."""

from __future__ import annotations

import numpy as np
import pandas as pd


def generate_synthetic_data(n: int = 250, seed: int = 42) -> pd.DataFrame:
    """Return a synthetic dataset; no real patient records are used."""
    if n < 10:
        raise ValueError("n must be at least 10 to support meaningful demonstrations.")

    rng = np.random.default_rng(seed)
    age = rng.integers(18, 81, size=n)
    bmi = np.clip(rng.normal(26.0, 4.2, size=n), 16.0, 42.0)
    smoking = rng.choice(
        ["Never", "Former", "Current"],
        size=n,
        p=[0.62, 0.22, 0.16],
    )

    # These simple equations create plausible-looking synthetic values only.
    # They are not clinical models and are not fitted to patient data.
    systolic = np.clip(
        105 + 0.42 * age + 0.55 * (bmi - 25) + rng.normal(0, 11, size=n),
        85, 205
    )
    diastolic = np.clip(
        65 + 0.16 * age + 0.35 * (bmi - 25) + rng.normal(0, 7, size=n),
        45, 125
    )
    glucose = np.clip(
        82 + 0.32 * (age - 35) + 1.05 * (bmi - 25) + rng.normal(0, 13, size=n),
        55, 230
    )

    return pd.DataFrame(
        {
            "participant_id": [f"SYN-{i:04d}" for i in range(1, n + 1)],
            "age_years": age.astype(int),
            "systolic_bp_mmhg": np.round(systolic, 1),
            "diastolic_bp_mmhg": np.round(diastolic, 1),
            "bmi_kg_m2": np.round(bmi, 1),
            "fasting_glucose_mg_dl": np.round(glucose, 1),
            "smoking_status": smoking,
        }
    )
