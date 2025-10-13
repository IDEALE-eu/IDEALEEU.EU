# CHECK_POINTS — Inspection Check Points

## Purpose

This directory contains definitions of inspection check points, datum references, and tolerance specifications for check fixture operations.

## Contents

### Subdirectories
- **[DATUMS/](./DATUMS/)** — Datum reference definitions
- **[LOCATIONS/](./LOCATIONS/)** — Check point locations
- **[TOLERANCES/](./TOLERANCES/)** — Tolerance specifications

## Check Point Definition

A check point defines:
- **Location**: X, Y, Z coordinates or feature reference
- **Feature type**: Hole, surface, edge, etc.
- **Measurement method**: CMM, gauge, visual
- **Tolerance**: Allowable deviation
- **Datum reference**: Coordinate system reference
- **Inspection frequency**: First article, periodic, 100%

## Check Point Categories

### Critical Characteristics
- Affect fit, form, or function
- Interface features
- Structural load paths
- 100% inspection required
- Tighter tolerances

### Major Characteristics
- Important for assembly
- May affect performance
- Sample inspection acceptable
- Standard tolerances

### Minor Characteristics
- Non-critical dimensions
- Minimal impact on function
- Reduced inspection frequency
- Relaxed tolerances

## Inspection Planning

### Check Point Selection
- Based on design requirements
- Critical dimensions identified
- GD&T callouts included
- Interface features prioritized
- Historical issues considered

### Documentation
- Check point list
- Measurement methods
- Acceptance criteria
- Sampling plan
- Traceability to drawings

## Related Directories

- **CMM programs**: [`../CMM/PROGRAMS/`](../CMM/PROGRAMS/)
- **Laser tracker targets**: [`../LASER_TRACKER/TARGETS/`](../LASER_TRACKER/TARGETS/)
- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/)
