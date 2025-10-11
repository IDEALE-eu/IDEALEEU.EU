# VERIFICATION_MATRIX — Verification Method Matrix

## Purpose

The Verification Method Matrix documents the assignment of verification methods (Analysis, Test, Inspection, Demonstration) to each requirement, providing a high-level view of the verification approach.

## Contents

This directory contains verification matrices that define:
- Which verification method(s) apply to each requirement
- Verification level (subsystem, system, spacecraft)
- Verification phase (qualification, acceptance, flight)
- Resource allocation for verification activities

## Matrix Structure

### Required Columns

| Column | Description | Example |
|--------|-------------|---------|
| Requirement ID | Subsystem requirement | 21-10-THM-RAD-010 |
| Requirement Type | Performance, Interface, Design | Performance |
| Analysis (A) | Yes/No + reference | Yes - Thermal model correlation |
| Test (T) | Yes/No + reference | Yes - TVAC steady-state |
| Inspection (I) | Yes/No + reference | Yes - Coating thickness |
| Demonstration (D) | Yes/No + reference | No |
| Verification Level | Subsystem/System/Integration | Subsystem |
| Phase | Qual/Accept/Flight | Qualification + Acceptance |
| Facility | Where performed | Thermal vacuum chamber |

## File Naming

```
21-10-CMP-VMATRIX_<scope>__r<NN>__<STATUS>.xlsx
```

Examples:
- `21-10-CMP-VMATRIX_all__r02__REL.xlsx` - All requirements
- `21-10-CMP-VMATRIX_performance__r01__RVW.xlsx` - Performance only
- `21-10-CMP-VMATRIX_qualification__r01__WIP.xlsx` - Qual phase

## Verification Method Selection

### Analysis (A)
Used when:
- Mathematical modeling can demonstrate compliance
- Physical testing is impractical or cost-prohibitive
- Heritage data supports analytical approach
- Correlation to test data is available

Examples:
- Thermal analysis (heat rejection, temperature distribution)
- Structural analysis (stress, fatigue, margins)
- Fluid flow analysis (pressure drop, flow distribution)

### Test (T)
Used when:
- Physical validation is required
- Analysis alone has insufficient confidence
- Flight environments must be simulated
- Standards mandate testing

Examples:
- TVAC (thermal vacuum)
- Vibration/shock (launch loads)
- Leak testing (fluid systems)
- Thermal cycling (coating durability)

### Inspection (I)
Used when:
- Visual or dimensional verification sufficient
- Workmanship quality must be verified
- Material properties must be confirmed
- Manufacturing compliance required

Examples:
- Coating thickness measurement
- Surface finish verification
- Dimensional inspection
- Contamination control witness

### Demonstration (D)
Used when:
- Functional operation must be shown
- Interface compatibility must be proven
- Operational procedures validated

Examples:
- Flow loop operation
- Valve actuation
- Installation/removal procedures

## Verification Philosophy

### Multiple Methods
Many requirements use combined methods:
- **A+T**: Analysis with test validation (typical for thermal)
- **T+I**: Test with inspection (quality + performance)
- **A+I**: Analysis with inspection (design validation)

### Verification by Similarity
When applicable, reference:
- Heritage hardware with similar design
- Previous qualification test results
- Industry standard data

### Verification Levels

**Subsystem Level**
- Component and assembly verification
- Unit-level thermal, structural testing

**System Level**
- Thermal control system integration
- Interface verification with other systems

**Spacecraft Level**
- End-to-end thermal balance
- Mission profile verification

## Review and Approval

1. Initial matrix created during requirements phase
2. Verification approach review at PDR
3. Update and approval at CDR
4. Verification closure at acceptance review

## Standards

- **ECSS-E-ST-10C**: Verification and validation
- **NASA-STD-7009**: Verification methodology
- **MIL-STD-1540E**: Verification requirements

## Related Documentation

- RTM: [`../rtm/`](../rtm/)
- VCRM: [`../vcrm/`](../vcrm/)
- Test plans: [`../../test_evidence/`](../../test_evidence/)
- Analysis reports: [`../../analyses/`](../../analyses/)
