# TOLERANCES_GDT — Tolerances and Geometric Dimensioning

## Purpose

This directory contains tolerance specifications and Geometric Dimensioning and Tolerancing (GD&T) requirements for interface control.

## Content Types

### Tolerance Specifications
- Dimensional tolerances
- Geometric tolerances
- Position tolerances
- Form tolerances (flatness, straightness, circularity)
- Orientation tolerances (perpendicularity, parallelism, angularity)
- Profile tolerances
- Runout tolerances

### Tolerance Analysis
- Tolerance stackup studies
- Worst-case analysis
- Statistical tolerance analysis (RSS)
- Assembly variation analysis
- Monte Carlo simulations

### GD&T Callouts
- Feature control frames
- Datum reference frames
- Material condition modifiers (MMC, LMC, RFS)
- Composite tolerancing
- Projected tolerance zones

## File Formats

- `.pdf` — GD&T drawings and specifications
- `.xlsx` — Tolerance stackup calculations
- `.csv` — Tolerance tables
- `.json` — Machine-readable tolerance data

## Documentation Structure

### Tolerance Drawings
- Fully dimensioned drawings with GD&T
- Datum feature identification
- Feature control frames
- Material condition callouts

### Stackup Analysis
- Dimension chains
- Contributing tolerances
- Accumulated variation
- Critical characteristics
- Assembly compensation methods

## Naming Convention

```
TOL_{feature}_{type}_v{version}.{ext}
```

Examples:
- `TOL_WING-ATTACH_STACKUP_v001.xlsx`
- `TOL_BULKHEAD_FLATNESS_v002.pdf`
- `TOL_DOOR-FRAME_POSITION_v001.pdf`

## Tolerance Classes

### Critical Interfaces
- Tight tolerances for primary load paths
- Close fit requirements
- Sealing surface tolerances
- Aerodynamic surface tolerances

### Standard Interfaces
- Normal machining tolerances
- Standard fit classes
- Commercial tolerances

### Non-Critical Features
- Liberal tolerances
- As-cast or as-formed tolerances

## GD&T Symbols and Applications

### Form Controls
- **⏤** Straightness
- **○** Flatness
- **○** Circularity
- **⌭** Cylindricity

### Orientation Controls
- **⊥** Perpendicularity
- **∥** Parallelism
- **∠** Angularity

### Location Controls
- **⊕** Position
- **⌖** Concentricity/Coaxiality
- **⌯** Symmetry

### Profile Controls
- **⌓** Profile of a line
- **⌒** Profile of a surface

### Runout Controls
- **↗** Circular runout
- **↗↗** Total runout

## Material Condition Modifiers

- **Ⓜ** Maximum Material Condition (MMC)
- **Ⓛ** Least Material Condition (LMC)
- **Ⓢ** Regardless of Feature Size (RFS)

## Tolerance Stackup Methods

### Worst-Case Analysis
- Sum of maximum tolerances
- Conservative approach
- Guarantees assembly

### Statistical Analysis (RSS)
- Root Sum Square method
- Probability-based
- Realistic approach

### Monte Carlo Simulation
- Computer-based analysis
- Handles complex geometries
- Statistical distribution modeling

## Cross-References

- [Datums and Coordinates](../DATUMS_COORDS/)
- [Interface Control Documents](../ICD/)
- [Clearances](../CLEARANCES/)
- [Mates and Constraints](../MATES_CONSTRAINTS/)

## Standards

- **ASME Y14.5-2018**: Dimensioning and Tolerancing
- **ISO 1101**: Geometrical tolerancing
- **ISO 2768**: General tolerances
- **ISO 5458**: Positional tolerancing
- **AIA NAS 3000**: Aerospace tolerance standards
