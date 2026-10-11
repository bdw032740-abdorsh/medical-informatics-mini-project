"""Automated checks for the educational synthetic-data workflow."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from medical_informatics.analysis import (  # noqa: E402
    create_summary_statistics,
    validate_data,
)
from medical_informatics.generate_data import generate_synthetic_data  # noqa: E402


class SyntheticDataTests(unittest.TestCase):
    def test_generation_is_reproducible(self):
        first = generate_synthetic_data(n=25, seed=7)
        second = generate_synthetic_data(n=25, seed=7)
        self.assertTrue(first.equals(second))

    def test_expected_shape_and_unique_ids(self):
        df = generate_synthetic_data(n=30, seed=1)
        self.assertEqual(len(df), 30)
        self.assertTrue(df["participant_id"].is_unique)

    def test_generated_data_passes_validation(self):
        df = generate_synthetic_data(n=40, seed=12)
        self.assertEqual(validate_data(df), [])

    def test_summary_contains_expected_variables(self):
        df = generate_synthetic_data(n=20, seed=4)
        summary = create_summary_statistics(df)
        self.assertEqual(len(summary), 5)
        self.assertIn("mean", summary.columns)
        self.assertIn("median", summary.columns)

    def test_small_sample_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_synthetic_data(n=5)


if __name__ == "__main__":
    unittest.main()
