# ALIGNMENT_REPORTS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 05-CALIBRATION_ALIGNMENT > ALIGNMENT_REPORTS**

Correlation plots, residuals, and tuned parameters with uncertainty quantification.

## Purpose

Document calibration results, model-to-test correlation, and parameter uncertainty.

## Report Structure

Each calibration report includes:
1. **Executive Summary**: Key findings, calibrated parameters, accuracy metrics
2. **Data Sources**: Test datasets used (ground, flight, HIL/SIL)
3. **Calibration Method**: Optimization algorithm, priors, convergence criteria
4. **Results**: Calibrated parameter values with confidence intervals
5. **Correlation Plots**: Predicted vs. actual (scatter plots, time-series)
6. **Residual Analysis**: Error distribution, systematic bias check
7. **Sensitivity Analysis**: Parameter impact on outputs
8. **Recommendations**: Model improvements, additional testing needs

## Example Reports

- **CALIBRATION_REPORT_AERO_2025-01-10.pdf** - Aerodynamics calibration (wind tunnel + flight test)
- **CALIBRATION_REPORT_THERMAL_2025-01-12.pdf** - Thermal models (cryo tank ground test)
- **CALIBRATION_REPORT_H2_2025-01-15.pdf** - H₂ energy system (flight test)

## Correlation Metrics

| Model | Parameter | Calibrated Value | Uncertainty (±) | R² | RMSE |
|-------|-----------|------------------|-----------------|----|----- |
| **Aerodynamics** | CD0 | 0.0185 | 0.0012 | 0.97 | 0.025 |
| **Thermal** | MLI Effectiveness | 0.94 | 0.02 | 0.93 | 1.8 K |
| **H₂ Energy** | Boil-off Rate | 1.65%/day | 0.15 | 0.89 | 0.18%/day |

## Uncertainty Quantification

- **Confidence Intervals**: 95% CI for each parameter
- **Posterior Distributions**: For Bayesian calibration (MCMC)
- **Sensitivity Indices**: Sobol indices, Morris screening

## Acceptance Criteria

Calibration accepted if:
1. **Convergence**: Optimization converged (tolerance <1e-6)
2. **Accuracy**: Validation RMSE within target (see `../CALIBRATION_PLAN.md`)
3. **Physical Plausibility**: Parameters within realistic bounds
4. **Peer Review**: Approved by calibration engineer + independent reviewer

## Related Documents

- **../CALIBRATION_PLAN.md** - Calibration methodology
- **../../13-TEMPLATES/CALIBRATION_REPORT_TEMPLATE.md** - Report template
- **../../06-VALIDATION_VERIFICATION/RESULTS/** - Validation results

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
