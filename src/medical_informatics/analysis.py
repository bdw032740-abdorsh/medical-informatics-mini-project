"""Validation, summary statistics, and visualizations for synthetic data."""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

REQUIRED_COLUMNS = {
    "participant_id",
    "age_years",
    "systolic_bp_mmhg",
    "diastolic_bp_mmhg",
    "bmi_kg_m2",
    "fasting_glucose_mg_dl",
    "smoking_status",
}
NUMERIC_COLUMNS = [
    "age_years",
    "systolic_bp_mmhg",
    "diastolic_bp_mmhg",
    "bmi_kg_m2",
    "fasting_glucose_mg_dl",
]


def validate_data(df: pd.DataFrame) -> list[str]:
    """Return a list of validation issues; an empty list means checks passed."""
    issues: list[str] = []
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        issues.append(f"Missing required columns: {', '.join(sorted(missing_columns))}")
        return issues

    if df["participant_id"].isna().any():
        issues.append("Participant IDs contain missing values.")
    if df["participant_id"].duplicated().any():
        issues.append("Participant IDs are not unique.")
    if df[list(REQUIRED_COLUMNS)].isna().any().any():
        issues.append("One or more required fields contain missing values.")

    for col in NUMERIC_COLUMNS:
        if (pd.to_numeric(df[col], errors="coerce").isna()).any():
            issues.append(f"{col} contains non-numeric values.")

    if (df["age_years"] < 0).any():
        issues.append("Age contains negative values.")
    if (df["bmi_kg_m2"] <= 0).any():
        issues.append("BMI contains zero or negative values.")
    if (df["systolic_bp_mmhg"] <= 0).any() or (df["diastolic_bp_mmhg"] <= 0).any():
        issues.append("Blood pressure contains zero or negative values.")
    if (df["fasting_glucose_mg_dl"] <= 0).any():
        issues.append("Glucose contains zero or negative values.")

    return issues


def create_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Create a concise descriptive-statistics table for numeric columns."""
    return (
        df[NUMERIC_COLUMNS]
        .describe()
        .T[["count", "mean", "std", "50%", "min", "max"]]
        .rename(columns={"50%": "median"})
        .round(2)
        .rename_axis("variable")
        .reset_index()
    )


def create_figures(df: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """Save three figures and return their paths."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []

    plots = [
        (
            "age_distribution.png",
            lambda ax: ax.hist(df["age_years"], bins=14, edgecolor="black"),
            "Age distribution (synthetic data)",
            "Age (years)",
            "Number of records",
        ),
        (
            "blood_pressure_by_age.png",
            lambda ax: ax.scatter(
                df["age_years"], df["systolic_bp_mmhg"], alpha=0.75
            ),
            "Age and systolic blood pressure (synthetic data)",
            "Age (years)",
            "Systolic blood pressure (mmHg)",
        ),
        (
            "bmi_vs_glucose.png",
            lambda ax: ax.scatter(
                df["bmi_kg_m2"], df["fasting_glucose_mg_dl"], alpha=0.75
            ),
            "BMI and fasting glucose (synthetic data)",
            "BMI (kg/m²)",
            "Fasting glucose (mg/dL)",
        ),
    ]

    for filename, draw, title, xlabel, ylabel in plots:
        fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
        draw(ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
        target = output_path / filename
        fig.savefig(target, dpi=180, bbox_inches="tight")
        plt.close(fig)
        saved.append(target)

    return saved
