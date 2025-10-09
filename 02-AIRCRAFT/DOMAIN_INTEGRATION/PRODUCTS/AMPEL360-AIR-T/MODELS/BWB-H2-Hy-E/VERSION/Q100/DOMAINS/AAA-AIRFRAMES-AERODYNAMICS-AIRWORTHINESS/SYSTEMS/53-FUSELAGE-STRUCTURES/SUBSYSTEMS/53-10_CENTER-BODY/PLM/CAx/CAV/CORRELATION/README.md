# CORRELATION — Test-to-Analysis Correlation

## Purpose

This directory contains correlation studies between physical test results and analytical predictions, supporting model validation, calibration, and continuous improvement.

## Directory Structure

### FEA/
Finite Element Analysis correlation studies for structural tests.

**Contents**:
- Pre-test FEA predictions
- Post-test correlation analyses
- Stress/strain field comparisons
- Deflection and stiffness correlation
- Modal analysis correlation
- Model updates and tuning

### CFD/
Computational Fluid Dynamics correlation for aerodynamic and thermal tests.

**Contents**:
- Venting flow predictions vs. test
- Thermal field predictions vs. measurements
- Pressure distribution comparisons
- Heat transfer coefficient validation

### FSI/
Fluid-Structure Interaction correlation for coupled phenomena.

**Contents**:
- Pressurization with structural deformation
- Cryogenic cooling with thermal stress
- Venting with structural vibration
- Combined thermal-structural effects

### TUNING/
Model tuning and calibration based on test data.

**Contents**:
- Material property updates
- Boundary condition refinements
- Load factor adjustments
- Damping and stiffness corrections
- Updated analysis models

## Correlation Methodology

### Pre-Test Activities
1. **Prediction Analysis** — Run analyses with best available data
2. **Uncertainty Quantification** — Identify sources of uncertainty
3. **Sensor Placement** — Optimize instrumentation for correlation
4. **Success Metrics** — Define acceptable correlation criteria

### Post-Test Activities
1. **Data Processing** — Prepare test data for comparison
2. **Model Update** — Update model with as-tested configuration
3. **Correlation Analysis** — Compare test vs. prediction
4. **Discrepancy Investigation** — Investigate significant differences
5. **Model Tuning** — Update model parameters if justified
6. **Validation Report** — Document correlation results

## Correlation Metrics

### Acceptable Correlation Criteria

**Static Structural Tests**:
- Strain: Within ±10% or ±50 microstrain (whichever is greater)
- Deflection: Within ±15%
- Load distribution: Within ±20%

**Dynamic Tests**:
- Natural frequencies: Within ±5%
- Mode shapes: MAC (Modal Assurance Criterion) > 0.9
- Damping: Within ±50% (large uncertainty expected)

**Thermal Tests**:
- Steady-state temperatures: Within ±10°C
- Transient response: Time constant within ±20%
- Heat flux: Within ±25%

### Investigation Triggers
- Any metric exceeding acceptable criteria
- Unexpected failure modes
- Sign reversal in stress/strain
- Systematic bias across all measurements

## Correlation Report Contents

1. **Objectives** — What is being correlated and why
2. **Test Summary** — Brief summary of test configuration and results
3. **Analysis Model** — Description of analytical model
4. **Comparison** — Side-by-side comparison of test vs. analysis
5. **Metrics** — Quantitative correlation metrics
6. **Discussion** — Interpretation of results, sources of difference
7. **Model Updates** — Recommended updates to analytical model
8. **Conclusions** — Assessment of model fidelity and validation status

## Correlation Database

Maintain a correlation database tracking:
- Test ID and date
- Analysis version
- Correlation metrics
- Model updates applied
- Lessons learned

**File**: `CORRELATION_DATABASE.xlsx`

## Model Update Process

Model updates based on test correlation require:
1. **Technical Justification** — Engineering rationale for update
2. **Impact Assessment** — Effect on previous analyses
3. **Approval** — Chief Engineer approval for baseline updates
4. **Documentation** — Update to model documentation
5. **Verification** — Re-run critical analyses with updated model

## References

- Test data: `../../DATA/PROCESSED/`
- Analysis models: `../../../CAE/`
- Test reports: `../../REPORTS/TEST_REPORTS/`
- Correlation reports: `../../REPORTS/CORRELATION_REPORTS/`

---

**Owner**: Analysis Team with Test Engineering support  
**Review**: Correlation review board for significant discrepancies  
**Frequency**: Post-test for each major test campaign
