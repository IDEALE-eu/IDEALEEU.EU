# TRANSFORMS — Coordinate System Transformations

## Purpose

This directory contains transformation definitions, matrices, and utilities for converting between different coordinate systems used in the 53-10 Center Body.

## Contents

### DEFINITIONS/
Transformation definitions and specifications:
- Analytical transformation expressions
- Euler angle sequences
- Quaternion representations
- Rotation and translation specifications
- Transformation composition rules

### MATRICES/
Numerical transformation matrices:
- Homogeneous transformation matrices (4×4)
- Rotation matrices (3×3)
- Translation vectors
- CSV and JSON formats for tool compatibility
- Validated and version-controlled matrices

### SCRIPTS/
Automation scripts for transformation operations:
- Coordinate transformation utilities
- Batch conversion tools
- Validation and verification scripts
- CAD system integration macros
- Matrix composition and inversion tools

## Transformation Types

### Rigid Body Transformations
- Pure translations
- Pure rotations
- Combined rotation + translation
- 6-DOF transformations

### Coordinate System Conversions
- Global ↔ Station (FS/WL/BL)
- Global ↔ Local (Frame/Stringer/Panel)
- Body ↔ Wind axes
- Parent ↔ Child coordinate systems

## File Formats

### Definition Files
- `.yaml` — Human-readable transformation definitions
- `.json` — Machine-readable transformation data
- `.md` — Documentation and derivation notes

### Matrix Files
- `.csv` — Comma-separated matrix values
- `.txt` — Space-separated matrix values
- `.xml` — Structured transformation data

### Script Files
- `.py` — Python transformation utilities
- `.m` — MATLAB transformation functions
- `.vbs` — VBA macros for CAD systems

## Naming Convention

```
TRANSFORM_<from>_TO_<to>_v<version>.<ext>
```

Examples:
- `TRANSFORM_GLOBAL_TO_FS1200_v01.yaml`
- `TRANSFORM_BODY_TO_WIND_v01.csv`
- `TRANSFORM_FRAME_F12_TO_GLOBAL_v01.json`

## Transformation Validation

All transformations must be validated for:
- **Mathematical correctness**: Det(R) = 1, R·R^T = I
- **Numerical accuracy**: Precision ≤ 1e-6
- **Consistency**: Forward·Inverse = Identity
- **Physical realizability**: No scaling or shearing

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [Global Systems](../GLOBAL/README.md)
- [Local Systems](../LOCAL/README.md)
- [Validation Rules](../VALIDATION/README.md)
- [CAI Scripts](../../../../CAI/SCRIPTS/README.md)

## Usage Guidelines

### Design Phase
- Use standardized transformation utilities
- Document all coordinate system relationships
- Validate transformations before CAD application

### Analysis Phase
- Apply transformations to FEA models
- Convert load vectors between coordinate systems
- Transform results for reporting

### Manufacturing Phase
- Convert CAD coordinates to machine coordinates
- Transform inspection results to global frame
- Align tooling coordinate systems

## Standards

- **ISO 9787**: Coordinate systems and transformations
- **NASA SP-8016**: Effects of structural flexibility on spacecraft control
- **IEEE 1558**: Standard for coordinate systems and transformations

---

**Owner**: 53-10 Integration / CAE Lead  
**Tools**: Python (NumPy), MATLAB, VBA  
**Validation**: Required for all transformations  
**Update frequency**: As coordinate systems evolve
