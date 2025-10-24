# VALIDATION — Validation and Verification

## Purpose

This directory contains validation and verification (V&V) documentation and results for CAE simulations.

## Directory Structure

```
VALIDATION/
├─ README.md                    # This file
├─ validation_plan.md           # Overall V&V strategy
└─ correlation_reports/         # Validation reports comparing to experiments
   ├─ 2025-10-23_tank_validation.md
   └─ templates/
      └─ validation_report_template.md
```

## Validation vs. Verification

### Verification
**Definition**: Are we solving the equations correctly?

**Activities**:
- Code verification (method of manufactured solutions)
- Mesh convergence studies
- Time step sensitivity
- Comparison with analytical solutions

### Validation
**Definition**: Are we solving the right equations?

**Activities**:
- Comparison with experimental data
- Physics model assessment
- Uncertainty quantification
- Domain of applicability

## Validation Hierarchy

### Level 1: Unit Tests
- Single physics phenomena
- Simple geometries
- Analytical solutions available
- Example: Laminar pipe flow

### Level 2: Benchmark Tests
- Combined physics
- Standard test cases
- Community validation data
- Example: NACA 0012 airfoil

### Level 3: Subsystem Tests
- Representative geometry
- Operating conditions
- Experimental data
- Example: Heat exchanger

### Level 4: System Tests
- Full system
- Integrated physics
- Flight/operational data
- Example: Full aircraft

## Validation Plan

See `validation_plan.md` for the complete validation strategy including:
- Phenomena identification and ranking
- Required experiments
- Validation metrics
- Schedule and milestones

## Validation Reports

Each validation activity should produce a report documenting:
- Objective and scope
- Experimental setup and data
- Simulation setup
- Comparison methodology
- Results and correlation metrics
- Uncertainty analysis
- Conclusions and recommendations

### Report Template
Use `correlation_reports/templates/validation_report_template.md`

## Correlation Metrics

### Quantitative Metrics
- **R²**: Coefficient of determination (> 0.95 good)
- **RMSE**: Root mean square error (< 10% of range)
- **MAPE**: Mean absolute percentage error (< 15%)
- **Bias**: Systematic offset (< 5%)

### Qualitative Assessment
- Trend agreement (increasing/decreasing)
- Peak locations
- Flow features
- Stability characteristics

## Uncertainty Quantification

Document uncertainties in:

### Input Uncertainties
- Geometry tolerances
- Material properties
- Boundary conditions
- Operating conditions

### Numerical Uncertainties
- Discretization error
- Iterative convergence
- Round-off error

### Model Uncertainties
- Turbulence models
- Transition prediction
- Multiphase models
- Chemistry models

## Validation Database

Maintain database of validation cases:
- Case identifier
- Physics phenomena
- Validation level
- Experimental data source
- Correlation metrics
- Simulation setup
- Status and approval

## Best Practices

1. **Early Planning**: Plan validation before building models
2. **Independent Review**: Have validation reviewed by uninvolved party
3. **Documentation**: Document all assumptions and limitations
4. **Uncertainty**: Always quantify uncertainties
5. **Iteration**: Validation is iterative process
6. **Applicability**: Define domain of applicability

## Experimental Data Quality

Required for validation data:
- [ ] Measurement uncertainty documented
- [ ] Calibration current
- [ ] Test conditions documented
- [ ] Raw data available
- [ ] Repeatability demonstrated
- [ ] Traceability to standards

## Model Improvement

When validation shows deficiencies:
1. Understand root cause
2. Consider physics model improvements
3. Refine mesh if needed
4. Re-validate
5. Document changes and impact

## Certification Support

For certification activities:
- Use highest validation level practical
- Independent review required
- Full uncertainty analysis
- Conservative assumptions
- Document limitations

## References

- AIAA Guide for V&V of CFD Simulations (G-077)
- ASME V&V Standards (V&V 10, V&V 20)
- NASA Standard for Models and Simulations (NASA-STD-7009)

---

**Last Updated:** 2025-10-23
