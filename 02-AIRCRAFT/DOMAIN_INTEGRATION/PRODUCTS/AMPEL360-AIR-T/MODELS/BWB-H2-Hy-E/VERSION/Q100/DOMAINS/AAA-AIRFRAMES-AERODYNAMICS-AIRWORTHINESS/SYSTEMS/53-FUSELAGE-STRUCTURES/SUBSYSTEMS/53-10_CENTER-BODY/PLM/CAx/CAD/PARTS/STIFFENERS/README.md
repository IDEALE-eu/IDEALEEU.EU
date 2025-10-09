# STIFFENERS — Local Stiffening Element Parts

## Purpose

This directory contains CAD part files for stiffeners and local reinforcement elements used in the 53-10 Center Body subsystem. Stiffeners provide local stiffness to prevent buckling, reduce panel vibration, and distribute concentrated loads.

## Component Description

### Stiffener Types
- **Skin stiffeners**: Prevent skin panel buckling between stringers
- **Web stiffeners**: Reinforce thin webs against shear buckling
- **Flange stiffeners**: Prevent flange local buckling
- **Angle stiffeners**: L-section or Z-section local reinforcements
- **Hat stiffeners**: Hat-section stiffening members

### Applications
- Between stringers on large skin panels
- In frame webs and bulkhead webs
- Around cutouts and openings
- At load introduction points
- In door and window surrounds

## Naming Convention

```
53-10_STIFFENER_<identifier>_<location>_<version>.<ext>
```

Examples:
- `53-10_STIFFENER_STF-001_SKIN-PANEL-SP05_v01.CATPart`
- `53-10_STIFFENER_STF-025_BULKHEAD-BH03_v02.prt`
- `53-10_STIFFENER_STF-050_FRAME-WEB-F10_v01.sldprt`

## Design Considerations

### Structural Requirements
- Prevent local buckling under compression loads
- Increase panel stiffness and natural frequency
- Distribute point loads over larger area
- Minimize weight while achieving stiffness goals

### Material Specifications
- **Aluminum angles**: 2024-T3 or 6061-T6 extruded angles
- **Sheet metal formed**: 2024-T3 formed hat or Z sections
- **Machined**: From plate for complex profiles
- **Bonded**: Adhesively bonded for reduced weight

### Attachment Methods
- **Riveted**: Most common for removable/repairable structure
- **Bonded**: For composite or weight-optimized designs
- **Welded**: For aluminum or titanium continuous structures
- **Combination**: Bonded and riveted for durability

## Design Guidelines

### Stiffener Spacing
- Space to prevent panel buckling under design loads
- Consider panel thickness and material properties
- Account for boundary conditions at edges

### Cross-Section Selection
- L-section: Simple and lightweight
- Z-section: More stiffness, good for edge reinforcement
- Hat-section: Maximum stiffness for weight
- T-section: For heavy loads

## Cross-References

- **Skin panels**: [`../SKIN_PANELS/`](../SKIN_PANELS/)
- **Frames**: [`../FRAMES/`](../FRAMES/)
- **Bulkheads**: [`../BULKHEADS/`](../BULKHEADS/)
- **Door surrounds**: [`../DOOR_SURROUNDS/`](../DOOR_SURROUNDS/)
- **Fasteners**: [`../FASTENERS/`](../FASTENERS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Stiffeners must meet:
- Dimensional tolerances for proper fit and alignment
- Material properties per specifications
- Surface finish for fatigue resistance (if applicable)
- Attachment requirements (rivet spacing, adhesive coverage)
