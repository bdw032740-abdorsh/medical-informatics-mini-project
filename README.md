# Exploratory Analysis of Synthetic Clinical Data

**A reproducible, beginner-friendly medical informatics portfolio project**

This project demonstrates a small end-to-end workflow for exploring a **fully synthetic** clinical-style dataset with Python. It focuses on data quality checks, descriptive statistics, visualization, and reproducible outputs.

> **Important:** The dataset is artificial and contains no real patient information. This is an educational programming project, not clinical research, a validated prediction model, or a tool for medical decision-making.

## Project goals

- Generate a deterministic synthetic dataset so results can be reproduced.
- Check basic data quality and summarize key variables.
- Explore distributions and relationships using clear visualizations.
- Export analysis outputs to files that can be reviewed or reused.
- Keep the project organized, documented, and testable.

## Variables

| Variable | Description | Unit |
|---|---|---|
| `participant_id` | Artificial record identifier | — |
| `age_years` | Simulated age | years |
| `systolic_bp_mmhg` | Simulated systolic blood pressure | mmHg |
| `diastolic_bp_mmhg` | Simulated diastolic blood pressure | mmHg |
| `bmi_kg_m2` | Simulated body mass index | kg/m² |
| `fasting_glucose_mg_dl` | Simulated fasting glucose | mg/dL |
| `smoking_status` | Simulated category | category |

All values are randomly generated for demonstration and should not be interpreted as representative of any population.

## Repository structure

```text
medical-informatics-mini-project/
├── data/                         # Generated synthetic dataset
├── reports/
│   ├── figures/                  # Exported plots
│   └── summary_statistics.csv    # Exported descriptive statistics
├── src/medical_informatics/
│   ├── __init__.py
│   ├── analysis.py               # Validation and analysis functions
│   └── generate_data.py          # Reproducible synthetic data generator
├── tests/
│   └── test_analysis.py          # Basic automated tests
├── .gitignore
├── requirements.txt
└── run_analysis.py               # One-command workflow
```

## Quick start

### 1. Requirements

- Python 3.10 or newer
- pip

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the workflow

From the project root:

```bash
python run_analysis.py
```

This creates:
- `data/synthetic_clinical_data.csv`
- `reports/summary_statistics.csv`
- `reports/figures/age_distribution.png`
- `reports/figures/blood_pressure_by_age.png`
- `reports/figures/bmi_vs_glucose.png`

### 4. Run tests

```bash
python -m unittest discover -s tests -v
```

## Methods

1. **Synthetic data generation:** a fixed random seed makes the output reproducible.
2. **Data validation:** checks required columns, missing values, duplicate IDs, and impossible negative values for selected measurements.
3. **Descriptive analysis:** computes count, mean, standard deviation, median, minimum, and maximum for numeric variables.
4. **Visualization:** saves labeled plots with units and readable titles.
5. **Export:** writes machine-readable CSV files and publication-style PNG figures.

## Interpretation notes

The data are simulated for software demonstration only. Any apparent relationship between variables is an artifact of the generation process and must not be treated as evidence about real patients. The project intentionally does not make diagnoses, estimate individual risk, or recommend treatment.

## Skills demonstrated

- Python
- pandas
- NumPy
- Matplotlib
- Data validation and quality checks
- Descriptive statistics
- Reproducible analysis
- Basic automated testing
- Scientific documentation

## Possible next steps

- Add a Jupyter notebook explaining each analysis step.
- Add a real, ethically approved and properly de-identified dataset only if permissions and governance requirements are met.
- Expand tests and introduce a continuous-integration workflow.

## Author

**Abdulrahman Mohammed Rushdy**  
Medical student interested in medical informatics and scientific data analysis.
