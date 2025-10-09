# FLAT_PATTERNS — Flat Pattern Developments

## Purpose
Flat pattern developments of sheet metal parts for cutting operations.

## Contents
- Unfolded/flattened geometry of sheet metal parts
- Bend lines and bend allowances
- Material grain direction indicators
- Cut boundaries and profiles
- Hole locations and features

## File Information
Each DXF should include:
- Part number and revision
- Material specification and thickness
- Bend allowances and K-factors
- Grain direction requirements
- Dimensional tolerances

## Layer Structure
**Standard layers**:
- **CUTTING**: Outer profile for cutting
- **BENDING**: Bend lines with angles
- **HOLES**: Hole locations and sizes
- **GRAIN**: Material grain direction
- **TEXT**: Material and thickness callouts
- **DIMENSIONS**: Critical dimensions

## Export Requirements
- Scale: 1:1
- Units: Millimeters (or inches, specify clearly)
- Format: ASCII DXF, AutoCAD 2013 or 2018
- Precision: Full precision (14 decimal places)

## Manufacturing Notes
Include as text annotations:
- Material: e.g., "AL 2024-T3, 2.0 mm"
- Bend radius: e.g., "R = 3.0 mm"
- K-factor: e.g., "K = 0.33"
- Grain direction: e.g., "Grain parallel to long edge"
- Surface finish requirements

## Related Directories
- **[../SHEET_METAL/](../SHEET_METAL/)** — Formed part geometry
- **[../../NESTING/](../../NESTING/)** — Nesting layouts for material optimization
- **[../../../../CAM/NESTING/FLAT_PATTERNS/](../../../../CAM/NESTING/FLAT_PATTERNS/)** — CAM nesting data

## Validation Checklist
Before committing:
- [ ] All geometry is closed polylines
- [ ] Bend lines clearly marked
- [ ] Material thickness specified
- [ ] Grain direction indicated
- [ ] No duplicate or overlapping geometry
- [ ] Scale verified (1:1)
- [ ] File opens without errors
