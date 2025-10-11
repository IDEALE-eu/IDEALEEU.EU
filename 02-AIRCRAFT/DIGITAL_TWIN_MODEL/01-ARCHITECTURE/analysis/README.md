# analysis

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > analysis**

Analysis notebooks and scripts for digital twin performance evaluation.

## Purpose

This directory contains analysis tools for evaluating digital twin model performance, KPI validation, and energy budget analysis.

## Contents

- **[notebooks/](notebooks/)** - Jupyter notebooks for interactive analysis
  - **[kpi_sanity.ipynb](notebooks/kpi_sanity.ipynb)** - KPI validation and sanity checks
- **[scripts/](scripts/)** - Python scripts for automated analysis
  - **[energy_budget.py](scripts/energy_budget.py)** - Energy consumption and budget analysis
  - **[coverage_report.py](scripts/coverage_report.py)** - Test coverage and validation analysis

## Analysis Workflows

### KPI Validation
- Compare predicted vs. actual KPIs
- Identify drift and model degradation
- Generate performance reports

### Energy Budget Analysis
- H2 fuel consumption analysis
- Battery state of charge predictions
- Range and endurance calculations

### Coverage Analysis
- Operational envelope coverage
- Test case coverage metrics
- Validation gaps identification

## Usage

```bash
# Run KPI analysis notebook
jupyter notebook notebooks/kpi_sanity.ipynb

# Run energy budget script
python scripts/energy_budget.py --input data/flight_log.csv --output results/

# Generate coverage report
python scripts/coverage_report.py --test-dir ../validation/tests/ --output coverage.html
```

## Related Documents

- **[../validation/](../validation/)** - Validation test results
- **[../kpis/](../kpis/)** - KPI definitions and thresholds
- **[../../10-METRICS/](../../10-METRICS/)** - Performance metrics
- **[../../02-MODELS/](../../02-MODELS/)** - Model specifications

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Analytics Team | Initial analysis tools |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
