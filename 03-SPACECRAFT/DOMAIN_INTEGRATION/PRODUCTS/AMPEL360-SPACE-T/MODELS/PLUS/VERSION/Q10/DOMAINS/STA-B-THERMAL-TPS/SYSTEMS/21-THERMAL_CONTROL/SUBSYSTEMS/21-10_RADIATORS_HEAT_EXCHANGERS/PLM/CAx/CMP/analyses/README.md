# ANALYSES — Engineering Analysis Documentation

## Purpose

This directory contains summary reports and references to detailed engineering analyses performed to verify design requirements and demonstrate compliance for the 21-10 RADIATORS_HEAT_EXCHANGERS subsystem.

## Contents

### Subdirectories

- [**thermal/**](./thermal/) - Thermal budgets, margins, correlation summaries
- [**structural/**](./structural/) - Stress, flatness, stiffness reports
- [**reliability/**](./reliability/) - FMEA/FTA, MTBF, criticality analyses
- [**safety/**](./safety/) - Hazard analysis, FMEA, single-point failures

## Analysis Philosophy

### Analysis vs. Test
- Analysis used for design verification and optimization
- Test used for validation of analytical predictions
- Correlation between analysis and test required
- Analysis models maintained in CAE directory

### Analysis Hierarchy
1. **Preliminary Analysis**: Concept and trade studies
2. **Detailed Analysis**: Design verification
3. **Correlation Analysis**: Test-to-analysis comparison
4. **As-Built Analysis**: Final configuration verification

## File Naming

```
21-10-CMP-ANAL_<discipline>_<topic>__r<NN>__<STATUS>.pdf
```

Examples:
- `21-10-CMP-ANAL_thermal_radiator-sizing__r03__REL.pdf`
- `21-10-CMP-ANAL_structural_margin-summary__r02__RVW.pdf`
- `21-10-CMP-ANAL_reliability_FMEA__r01__REL.xlsx`

## Analysis Content

### Required Sections

1. **Executive Summary**
   - Analysis objectives
   - Key results
   - Compliance status

2. **Analysis Approach**
   - Methods and tools
   - Assumptions and limitations
   - Model description (reference to CAE)

3. **Results**
   - Detailed findings
   - Margin calculations
   - Comparison to requirements

4. **Correlation** (if applicable)
   - Test data comparison
   - Model validation
   - Uncertainty quantification

5. **Conclusions**
   - Compliance statement
   - Recommendations
   - Open items

## Margin Philosophy

### Design Margins
- **Thermal**: Temperature margins (min/max)
- **Structural**: Stress margins (yield, ultimate)
- **Performance**: Heat rejection margin

### Margin Calculation
```
Margin = (Allowable - Predicted) / Predicted × 100%
```

Positive margin indicates compliance.

### Minimum Margins
- **Thermal**: ±10°C operating margin
- **Structural**: Factor of safety per NASA-STD-5001
- **Reliability**: Per mission requirements

## Analysis Tools

### Thermal
- ESATAN-TMS, Thermal Desktop
- Detailed models in [`CAE/thermal/`](../../CAE/thermal/)

### Structural
- NASTRAN, ANSYS, Abaqus
- FE models in [`CAE/structural/`](../../CAE/structural/)

### Reliability
- Relex, Windchill Quality Solutions
- FMEA worksheets

## Correlation to Test

Each analysis shall be correlated to test where applicable:
- Pre-test predictions documented
- Post-test comparison performed
- Model updated based on test results
- Correlation report generated

## Configuration Control

- Analysis reports baselined at CDR
- Updates via ECN process
- Version control through PLM
- Audit trail maintained

## Standards

- **NASA-STD-7009**: Standard for models and simulations
- **ECSS-E-ST-32C**: Structural general requirements
- **ECSS-E-ST-31C**: Thermal control

## Related Documentation

- Detailed models: [`../../CAE/`](../../CAE/)
- Test correlation: [`../test_evidence/`](../test_evidence/)
- Requirements: [`../requirements/`](../requirements/)
