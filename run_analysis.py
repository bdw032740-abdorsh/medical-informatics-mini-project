"""Run the complete synthetic-data analysis workflow from the repository root."""

from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from medical_informatics.analysis import (  # noqa: E402
    create_figures,
    create_summary_statistics,
    validate_data,
)
from medical_informatics.generate_data import generate_synthetic_data  # noqa: E402


def main() -> int:
    data_dir = ROOT / "data"
    report_dir = ROOT / "reports"
    figures_dir = report_dir / "figures"
    data_dir.mkdir(exist_ok=True)
    report_dir.mkdir(exist_ok=True)

    data = generate_synthetic_data(n=250, seed=42)
    issues = validate_data(data)
    if issues:
        print("Data validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    data_path = data_dir / "synthetic_clinical_data.csv"
    summary_path = report_dir / "summary_statistics.csv"
    data.to_csv(data_path, index=False)
    summary = create_summary_statistics(data)
    summary.to_csv(summary_path, index=False)
    figures = create_figures(data, figures_dir)

    print("Analysis completed successfully.")
    print(f"Records analyzed: {len(data)}")
    print(f"Dataset: {data_path.relative_to(ROOT)}")
    print(f"Summary statistics: {summary_path.relative_to(ROOT)}")
    print("Figures:")
    for figure in figures:
        print(f"- {figure.relative_to(ROOT)}")
    print("\nDescriptive statistics:")
    print(summary.to_string(index=False))
    print("\nReminder: all records are synthetic and must not be used for clinical decisions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
