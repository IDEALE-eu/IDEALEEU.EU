# METADATA — Coordinate System Metadata

## Purpose

This directory contains metadata, conventions, and documentation standards for all coordinate systems used in the 53-10 Center Body.

## Contents

### CONVENTIONS/
Coordinate system conventions and standards:
- Naming conventions and rules
- Axis orientation standards (right-hand rule)
- Sign conventions (positive directions)
- Unit specifications and conversions
- Angular representation (degrees vs. radians)
- Handedness verification

### UNITS/
Unit system definitions and specifications:
- Length units: mm (millimeters) — primary
- Angular units: degrees (°) — documentation, radians (rad) — computation
- Tolerance specifications: ±0.01mm typical
- Unit conversion factors
- Precision and rounding rules

## Standard Conventions

### Right-Hand Rule
All coordinate systems follow the right-hand rule:
- Point fingers along +X axis
- Curl fingers toward +Y axis
- Thumb points along +Z axis

### Aircraft Body Axes (Standard)
```
+X: Forward → Aft (longitudinal)
+Y: Port → Starboard (lateral, right)
+Z: Keel → Crown (vertical, up)
```

### Aerodynamic Axes (Wind)
```
+X: Into relative wind (drag direction)
+Y: Starboard (side force direction)
+Z: Down (lift direction, negative up)
```

### Angular Measurements
- **Pitch**: Rotation about Y-axis (nose up positive)
- **Roll**: Rotation about X-axis (right wing down positive)
- **Yaw**: Rotation about Z-axis (nose right positive)

## Documentation Requirements

Each coordinate system must document:
- **Name**: Unique identifier
- **Type**: Global/Station/Local/Interface
- **Origin**: Location in parent coordinate system
- **Axes**: Orientation and alignment
- **Units**: Length and angular units
- **Parent**: Reference to parent coordinate system
- **Children**: List of dependent coordinate systems
- **Purpose**: Usage and application
- **Owner**: Responsible engineer/team
- **Version**: Revision and approval status

## File Formats

### Convention Files
- `NAMING_CONVENTIONS.yaml` — Naming rules and patterns
- `AXIS_CONVENTIONS.md` — Axis orientation standards
- `SIGN_CONVENTIONS.md` — Sign and direction standards
- `ANGULAR_CONVENTIONS.md` — Angular measurement standards

### Unit Files
- `UNITS_PRIMARY.yaml` — Primary unit definitions
- `UNITS_CONVERSION.csv` — Conversion factors
- `PRECISION_RULES.md` — Numerical precision specifications
- `TOLERANCE_STANDARDS.md` — Tolerance and accuracy requirements

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [ATA-06: Dimensions & Stations](../../../../../../../06-DIMENSIONS-STATIONS/README.md)
- [CONVENTIONS.md](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-00_GENERAL/CONVENTIONS.md)
- [Validation Rules](../VALIDATION/README.md)

## Standards Compliance

### International Standards
- **ISO 1151**: Flight dynamics coordinate systems
- **ISO 80000-3**: Space and time quantities
- **ASME Y14.5**: Dimensioning and tolerancing

### Aerospace Standards
- **ATA iSpec 2200**: Aircraft coordinate conventions
- **AIAA S-119**: Aerodynamic coordinate systems
- **MIL-STD-1374**: Coordinate systems

### Program Standards
- BWB-H2-Hy-E Q100 Configuration Management Plan
- 06-DIMENSIONS-STATIONS Master Conventions
- 53-FUSELAGE-STRUCTURES Design Standards

## Change Control

Changes to metadata and conventions require:
- Engineering review and approval
- Impact analysis on existing coordinate systems
- Update of dependent documentation
- Notification to all stakeholders
- Validation of affected transformations

---

**Owner**: 06-DIMENSIONS-STATIONS + 53-10 Integration  
**Status**: Program-wide standard  
**Criticality**: High — Foundational definitions  
**Update frequency**: Rarely; requires ECR approval
