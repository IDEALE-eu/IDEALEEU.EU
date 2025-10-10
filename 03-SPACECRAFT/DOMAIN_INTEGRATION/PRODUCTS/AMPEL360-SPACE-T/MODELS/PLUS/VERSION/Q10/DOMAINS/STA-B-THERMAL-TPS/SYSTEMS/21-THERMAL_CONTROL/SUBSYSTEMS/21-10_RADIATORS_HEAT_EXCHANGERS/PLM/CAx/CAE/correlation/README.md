# CORRELATION — Test-to-Model Correlation

## Purpose
Test-to-model correlation data, comparison analyses, and correlation factors for model validation.

## Contents
- Test vs model temperature comparisons
- Correlation factor derivation
- Delta analysis and uncertainty quantification
- Model validation evidence
- Uncertainty propagation studies
- Sensitivity analysis results

## File Organization
- One subdirectory per test campaign
- Include test data and model predictions
- Store correlation methodology
- Document uncertainty analysis

## Naming Convention
```
21-10-CAE_correlation_<test_id>__r<NN>__<STATUS>/
```

Example: `21-10-CAE_correlation_tvac_tb_001__r01__REL/`

## Correlation Requirements
- Overlay test and model results
- Calculate correlation factors
- Perform uncertainty quantification
- Document test-model differences
- Validate against acceptance criteria

## Correlation Package Contents
```
correlation_<test_id>/
  ├─ README.md (objectives, summary)
  ├─ test_data/ (measured temperatures, conditions)
  ├─ model_predictions/ (pre-test analysis)
  ├─ comparison/ (overlay plots, delta tables)
  ├─ correlation_factors/ (derived k, h, α, ε adjustments)
  └─ validation_report.pdf
```

## Typical Correlation Factors
- Contact conductance adjustments
- Coating property updates (α, ε)
- Material property refinements
- Model simplification uncertainties
- Boundary condition corrections

## Delta Analysis
```
Location    | Test (°C) | Model (°C) | Delta (°C) | % Error | Within Tol?
------------|-----------|------------|------------|---------|-------------
Panel 1     | +45.3     | +43.8      | -1.5       | -3.3%   | Yes
LPHX Inlet  | +18.2     | +19.1      | +0.9       | +4.9%   | Yes
```

## Validation Criteria
- Temperature delta < ±5°C (typical)
- Correlation factor < 1.5x (typical)
- 95% confidence interval coverage

## Guidelines
- Link to test procedures (CAV)
- Document test conditions and setup
- Maintain correlation factor database
- Use for model uncertainty quantification
- Update models based on correlation

---

**Last Updated**: 2025-10-10
