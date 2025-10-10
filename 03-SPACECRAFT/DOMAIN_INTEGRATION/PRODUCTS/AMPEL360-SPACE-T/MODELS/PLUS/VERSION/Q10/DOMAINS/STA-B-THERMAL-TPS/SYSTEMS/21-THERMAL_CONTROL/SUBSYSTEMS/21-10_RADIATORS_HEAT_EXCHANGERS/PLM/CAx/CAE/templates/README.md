# TEMPLATES — Analysis Templates and Checklists

## Purpose
Standard templates, checklists, and best practice guides for thermal and structural analysis.

## Contents
- Case setup templates
- Analysis checklists
- Report templates
- Review checklists
- Verification matrices
- Standard operating procedures

## File Organization
- One file per template type
- Include instructions for use
- Store example/filled templates
- Maintain version control

## Naming Convention
```
21-10-CAE_template_<type>_<name>__r<NN>__<STATUS>.{docx|xlsx|md}
```

Example: `21-10-CAE_template_case_sheet_thermal_balance__r01__REL.docx`

## Template Types

### Case Sheet Template
```
Analysis Case: _______________________
Analyst: _____________________________
Date: ________________________________

Objectives:
- [ ] Define case objectives
- [ ] Identify success criteria

Configuration:
- [ ] Geometry and model version
- [ ] Material properties
- [ ] Boundary conditions

Analysis Setup:
- [ ] Solver settings
- [ ] Convergence criteria
- [ ] Mesh information

Expected Results:
- [ ] Key performance metrics
- [ ] Temperature limits
- [ ] Verification criteria
```

### Analysis Checklist
```
Pre-Analysis:
- [ ] Requirements reviewed
- [ ] Model validated
- [ ] Mesh quality verified
- [ ] Material properties verified
- [ ] Boundary conditions documented

During Analysis:
- [ ] Convergence monitored
- [ ] Results sanity checked
- [ ] Interim results reviewed

Post-Analysis:
- [ ] Results validated
- [ ] Margins calculated
- [ ] Report generated
- [ ] Peer review completed
```

### Review Checklist
```
Model Review:
- [ ] Geometry accurate
- [ ] Material properties correct
- [ ] Mesh quality acceptable
- [ ] Boundary conditions appropriate

Results Review:
- [ ] Convergence achieved
- [ ] Energy balance verified
- [ ] Results physically reasonable
- [ ] Margins adequate

Documentation Review:
- [ ] Assumptions documented
- [ ] Methodology described
- [ ] Results clearly presented
- [ ] Conclusions justified
```

## Verification Matrix Template
```
Requirement ID | Requirement | Analysis Value | Limit | Margin | Status
---------------|-------------|----------------|-------|--------|--------
THERM-001      | Panel T_max | +62.8°C        | +70°C | +7.2°C | Pass
THERM-002      | Panel T_min | -35.2°C        | -40°C | +4.8°C | Pass
```

## Guidelines
- Customize templates for specific analyses
- Maintain consistent formatting
- Update templates based on lessons learned
- Archive completed checklists with analysis
- Include instructions for template use

---

**Last Updated**: 2025-10-10
