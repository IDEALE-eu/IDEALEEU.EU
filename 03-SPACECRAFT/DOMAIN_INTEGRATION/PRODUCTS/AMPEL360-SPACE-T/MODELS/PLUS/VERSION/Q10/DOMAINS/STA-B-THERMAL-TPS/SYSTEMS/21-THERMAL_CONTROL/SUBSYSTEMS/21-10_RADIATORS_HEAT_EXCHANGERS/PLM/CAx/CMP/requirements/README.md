# REQUIREMENTS — Requirement Traceability & Verification

## Purpose

This directory contains all requirement traceability and verification documentation for the 21-10 RADIATORS_HEAT_EXCHANGERS subsystem, ensuring complete traceability from system requirements through verification and validation.

## Contents

### Subdirectories

- [**rtm/**](./rtm/) - Requirement Traceability Matrix
- [**vcrm/**](./vcrm/) - Verification Cross-Reference Matrix  
- [**verification_matrix/**](./verification_matrix/) - Verification Method Matrix (A/T/I/D)

## Requirement Flow

```
System Requirements (SSRD)
    ↓
Subsystem Requirements (21-10-THM-XXX)
    ↓
Derived Requirements (design/process)
    ↓
Verification Methods (A/T/I/D)
    ↓
Evidence (CAE/CAV/CAI/CAP)
```

## Naming Convention

Use the following pattern:
```
21-10-CMP-REQ_<artifact>__r<NN>__<STATUS>.<ext>
```

Examples:
- `21-10-CMP-REQ-RTM-master__r03__REL.xlsx`
- `21-10-CMP-REQ-VCRM-thermal__r02__RVW.xlsx`
- `21-10-CMP-REQ-VMATRIX-all__r01__WIP.xlsx`

## Verification Methods

- **A (Analysis)**: Engineering analysis, modeling, simulation
- **T (Test)**: Physical testing (TVAC, vibration, thermal, leak)
- **I (Inspection)**: Visual, dimensional, NDT inspection
- **D (Demonstration)**: Functional demonstration, operation

## Traceability Requirements

Each requirement shall include:
- Unique requirement ID
- Parent requirement reference
- Verification method(s)
- Verification status
- Evidence location
- NCR/waiver linkage (if applicable)

## Status Values

- **WIP**: Work in Progress
- **RVW**: Under Review
- **REL**: Released/Approved

## Standards Compliance

Follow:
- **ECSS-E-ST-10C**: Space project management - System engineering
- **ECSS-M-ST-10C**: Project planning and implementation
- **NASA-STD-7009**: Standard for models and simulations
- **ISO/IEC 15288**: Systems and software engineering

## Related Directories

- Requirements baseline: [`../../../EBOM_LINKS.md`](../../../EBOM_LINKS.md)
- Verification evidence: [`../test_evidence/`](../test_evidence/)
- Analysis evidence: [`../analyses/`](../analyses/)
- Standards compliance: [`../standards/`](../standards/)
