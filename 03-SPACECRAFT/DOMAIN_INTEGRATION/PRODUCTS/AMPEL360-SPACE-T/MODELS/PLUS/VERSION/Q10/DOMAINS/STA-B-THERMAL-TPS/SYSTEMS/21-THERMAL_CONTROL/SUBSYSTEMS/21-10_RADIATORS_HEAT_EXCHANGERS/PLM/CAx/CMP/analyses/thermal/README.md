# THERMAL — Thermal Analysis Documentation

## Purpose

This directory contains thermal analysis reports including radiator sizing, heat rejection budgets, temperature predictions, and correlation to TVAC test data.

## Contents

This directory includes:
- Radiator sizing calculations and heat rejection budgets
- Temperature distribution analyses
- Thermal margin assessments
- TVAC test correlation reports
- Steady-state and transient thermal analyses
- Thermal interface conductance analyses

### Analysis Types

**Steady-State Analysis**
- Operating mode thermal balance
- Component temperature predictions
- Heat rejection sizing

**Transient Analysis**
- Temperature evolution during orbit
- Worst-case hot/cold scenarios
- Thermal cycling effects

**Correlation Analysis**
- Pre-test predictions vs. test data
- Model calibration and validation
- Uncertainty quantification

## File Naming

```
21-10-CMP-ANAL_thermal_<topic>__r<NN>__<STATUS>.<ext>
```

Examples:
- PDF reports for narratives and summaries
- Excel files for tabulated data
- Reference detailed models in [`../../../CAE/`](../../../CAE/)

## Documentation Requirements

Each analysis report shall include:
1. Objective and scope
2. Analysis method and assumptions
3. Model description (reference to CAE)
4. Results and margins
5. Conclusions and recommendations

## Verification

- Analysis results verified by independent review
- Correlation to test data when applicable
- Model validation documented
- Margins assessed against requirements

## Standards

- **NASA-STD-7009**: Standard for models and simulations
- **ECSS-E-ST-10C**: System engineering general requirements
- Discipline-specific standards as applicable

## Related Documentation

- Parent directory: [`../README.md`](../README.md)
- Detailed models: [`../../../CAE/`](../../../CAE/)
- Test evidence: [`../../test_evidence/`](../../test_evidence/)
- Requirements: [`../../requirements/`](../../requirements/)
