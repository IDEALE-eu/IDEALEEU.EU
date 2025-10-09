# CALIBRATION REPORT TEMPLATE

**Report ID**: [e.g., CALIB-2025-001]

**Model**: [e.g., Thermal Cryo Tank Model]

**Model ID**: [e.g., THERMAL_CRYO_TANK_V1.1]

**Date**: [e.g., 2025-01-15]

**Author**: [e.g., Thermal Team, John Doe]

---

## Executive Summary

[Brief summary of calibration objectives, data used, results, and recommendations]

---

## Objectives

[What parameters were calibrated and why?]

---

## Data Sources

### Test Datasets

| Dataset | Type | Date | Test Points | Description |
|---------|------|------|-------------|-------------|
| [e.g., GT_H2_TANK_2024] | Ground Test | 2024-12-10 | 50 | Cryo tank thermal tests |
| [e.g., FT_H2_2024_Q4] | Flight Test | 2024-Q4 | 30 flights | In-flight boil-off data |

---

## Calibration Method

[Description of calibration algorithm, e.g., least-squares, Bayesian inference, parameter sweep]

---

## Parameters Calibrated

| Parameter | Prior Value | Calibrated Value | Uncertainty (±) | Unit |
|-----------|-------------|------------------|-----------------|------|
| [e.g., MLI Effectiveness] | 0.95 | 0.94 | 0.02 | (dimensionless) |
| [e.g., Heat Leak Rate] | 2.0 | 1.85 | 0.15 | W |
| [e.g., Boil-off Coefficient] | 1.5 | 1.65 | 0.10 | %/day |

---

## Results

### Correlation Plots

[Include scatter plots: Predicted vs. Actual]

### Residual Analysis

[Histogram of residuals, Q-Q plot]

### Correlation Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **RMSE** | [e.g., 1.5 K] | <2 K | ✅ Pass |
| **MAE** | [e.g., 1.2 K] | <1.5 K | ✅ Pass |
| **R²** | [e.g., 0.93] | >0.90 | ✅ Pass |
| **Bias** | [e.g., -0.3 K] | <0.5 K | ✅ Pass |

---

## Sensitivity Analysis

[How sensitive are outputs to parameter changes?]

---

## Validation

[Validation on hold-out test set, not used in calibration]

---

## Recommendations

[Any model improvements, additional testing needs, or parameter constraints]

---

## Approval

- **Calibration Engineer**: [Name, Signature, Date]
- **Independent Reviewer**: [Name, Signature, Date]

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
