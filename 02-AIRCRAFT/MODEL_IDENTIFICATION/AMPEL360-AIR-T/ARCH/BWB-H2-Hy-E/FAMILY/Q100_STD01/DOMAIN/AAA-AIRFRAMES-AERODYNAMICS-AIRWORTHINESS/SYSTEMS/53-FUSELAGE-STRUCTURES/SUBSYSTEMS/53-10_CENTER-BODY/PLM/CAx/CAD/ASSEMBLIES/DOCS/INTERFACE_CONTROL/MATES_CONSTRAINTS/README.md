# MATES_CONSTRAINTS — Assembly Mates and Constraints

## Purpose

This directory contains definitions of assembly mates, constraints, and relationships between the CENTER-BODY and interfacing components.

## Content Types

### Assembly Mate Definitions
- Coincident mates
- Concentric/coaxial mates
- Parallel and perpendicular constraints
- Distance and angle constraints
- Tangent relationships

### Constraint Specifications
- Degrees of freedom (DOF) restrictions
- Over-constrained condition analysis
- Proper constraint schemes
- Assembly sequence dependencies

## File Formats

- `.pdf` — Mate definition drawings and specifications
- `.csv` — Mate relationship tables
- `.xlsx` — Constraint analysis matrices
- `.step` — Reference geometry with mate features

## Documentation Structure

Each mate definition should include:

### Mate Identification
- Unique mate ID
- Interfacing components
- Mate type and features
- Constraint degrees of freedom

### Geometric Requirements
- Feature definitions
- Tolerance requirements
- Surface finish requirements
- Material compatibility

### Assembly Requirements
- Assembly sequence
- Tooling requirements
- Inspection methods
- Acceptance criteria

## Naming Convention

```
MATE_{component1}_TO_{component2}_{type}_v{version}.{ext}
```

Examples:
- `MATE_CB-TO-WING-CENTER_COINCIDENT_v001.pdf`
- `MATE_CB-TO-DOOR-FRAME_COAXIAL_v002.csv`
- `MATE_CB-TO-AFT-SECTION_DISTANCE_v001.xlsx`

## Mate Types

### Primary Structural Mates
- Wing-to-body integration
- Forward/aft fuselage joints
- Bulkhead connections
- Frame-to-skin attachments

### Secondary Assembly Mates
- Equipment mounting
- Door frame integration
- Window frame installation
- Access panel attachments

## Analysis Requirements

Document:
- Mate stability analysis
- Over-constraint checks
- Assembly feasibility
- Tolerance stackup effects

## Cross-References

- [Interface Control Documents](../ICD/)
- [Fasteners](../FASTENERS/)
- [Tolerances](../TOLERANCES_GDT/)
- [Assembly Sequence](../SEQUENCE/)

## Standards

- **ASME Y14.5**: Dimensioning and Tolerancing
- **ISO 10579**: Geometrical product specifications (GPS) - Dimensioning and tolerancing
- **ASD-STAN prEN 9132**: Quality management systems - Aerospace series
