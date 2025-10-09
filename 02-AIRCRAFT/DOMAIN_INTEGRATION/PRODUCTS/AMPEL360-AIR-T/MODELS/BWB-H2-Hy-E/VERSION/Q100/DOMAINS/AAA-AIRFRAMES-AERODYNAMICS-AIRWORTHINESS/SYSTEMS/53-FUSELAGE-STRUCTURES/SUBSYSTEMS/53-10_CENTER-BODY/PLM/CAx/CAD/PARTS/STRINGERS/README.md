# STRINGERS — Longitudinal Stiffener Parts

## Purpose

This directory contains CAD part files for stringers (longitudinal stiffening members) used in the 53-10 Center Body subsystem. Stringers run along the length of the fuselage to carry axial and bending loads, prevent skin buckling, and provide stiffness between frames.

## Component Description

### Stringer Types
- **Hat stringers**: Hat-shaped cross-section (most common)
- **Z-stringers**: Z-shaped profile for efficient load transfer
- **I-beam stringers**: I-section for high bending loads
- **Blade stringers**: Simple flat blade configuration
- **Integrally stiffened**: Machined from skin panel (one-piece)

### Location Designations
- **L/R**: Left/Right (looking forward)
- **Upper/Lower**: Relative to floor line
- **Keel**: Bottom centerline stringer
- **Crown**: Top centerline stringer

## Naming Convention

```
53-10_STRINGER_<stringer-id>_<location>_<version>.<ext>
```

Examples:
- `53-10_STRINGER_STR-L01_UPPER-LEFT_v01.CATPart`
- `53-10_STRINGER_STR-R02_LOWER-RIGHT_v01.prt`
- `53-10_STRINGER_STR-KEEL_CENTERLINE_v02.sldprt`

## Design Considerations

### Structural Requirements
- Carry axial loads from fuselage bending and pressurization
- Prevent skin buckling between frames
- Provide continuous load path from nose to tail
- Interface with frames at each station
- Accommodate cutouts for doors, windows, and access panels

### Material Specifications
- **Primary material**: Aluminum alloy 2024-T3 (extruded)
- **Alternative**: Aluminum 7075-T6 for high-load areas
- **Composite**: Carbon fiber for integral skin-stringer panels

### Cross-Section Optimization
- Select profile based on load magnitude and skin thickness
- Design for efficient load introduction at frame attachment points
- Consider manufacturing constraints (extrusion, forming, machining)

## File Organization

Organize stringers by:
- Left/Right side designation
- Upper/Lower fuselage position
- Stringer number/identifier
- Length or zone (forward, center, aft sections)

## Cross-References

- **Stringer assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Frame attachments**: [`../FRAMES/`](../FRAMES/)
- **Skin panel interfaces**: [`../SKIN_PANELS/`](../SKIN_PANELS/)
- **Fastener schedules**: [`../FASTENERS/`](../FASTENERS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Stringer parts must meet:
- Profile tolerances per drawing specifications
- Straightness requirements for proper alignment
- Surface finish for fatigue performance
- Material properties per applicable specifications
