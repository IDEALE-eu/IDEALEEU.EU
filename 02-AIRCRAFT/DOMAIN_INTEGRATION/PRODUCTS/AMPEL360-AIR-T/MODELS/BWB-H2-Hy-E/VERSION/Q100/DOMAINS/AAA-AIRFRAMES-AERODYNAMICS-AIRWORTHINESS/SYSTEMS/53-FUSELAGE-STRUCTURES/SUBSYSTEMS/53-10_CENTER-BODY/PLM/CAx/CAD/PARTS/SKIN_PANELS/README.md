# SKIN_PANELS — Fuselage Skin Panel Parts

## Purpose

This directory contains CAD part files for skin panels used in the 53-10 Center Body subsystem. Skin panels form the outer mold line (OML) and inner mold line (IML) of the fuselage, providing the pressure boundary, aerodynamic surface, and primary tension-carrying structure.

## Component Description

### Panel Types
- **OML panels**: Outer mold line (external aerodynamic surface)
- **IML panels**: Inner mold line (cabin pressure boundary)
- **Flat panels**: Simplified planar sections
- **Doubly-curved panels**: Complex compound curvature panels
- **Integrally stiffened**: Panels with integral stringers (machined or co-cured)

### Panel Zones
- **Crown**: Upper fuselage panels
- **Side**: Left and right side panels
- **Keel**: Lower fuselage panels
- **Transition**: Panels at wing-body or section junctions

## Naming Convention

```
53-10_SKIN-PANEL_<panel-id>_<location>_<version>.<ext>
```

Examples:
- `53-10_SKIN-PANEL_SP-001_OML-FWD-CROWN_v01.CATPart`
- `53-10_SKIN-PANEL_SP-025_IML-LEFT-SIDE_v02.prt`
- `53-10_SKIN-PANEL_SP-050_OML-KEEL_v01.sldprt`

## Design Considerations

### Structural Requirements
- Carry hoop stresses from cabin pressurization
- Carry axial and shear loads from fuselage bending and torsion
- Resist buckling under compression loads
- Provide smooth aerodynamic surface (OML)
- Maintain pressure boundary integrity (IML)

### Material Specifications
- **Aluminum sheet**: 2024-T3 (typical thickness 1.0-3.0 mm)
- **Thick panels**: 7075-T6 for highly loaded areas
- **Composite panels**: Carbon fiber face sheets with honeycomb or foam core
- **Hybrid**: Aluminum-lithium alloys for weight reduction

### Manufacturing Methods
- **Stretch-formed**: For single-curvature panels
- **Hydroformed**: For complex curvatures
- **Machined**: From thick plate with integral stiffeners
- **Co-cured composite**: For integrated skin-stringer panels

## File Organization

Organize skin panels by:
- OML vs. IML designation
- Fuselage zone (forward, center, aft)
- Circumferential position (crown, side, keel)
- Panel number sequence

## Cross-References

- **Panel assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Stringer attachments**: [`../STRINGERS/`](../STRINGERS/)
- **Frame interfaces**: [`../FRAMES/`](../FRAMES/)
- **Window cutouts**: [`../WINDOW_BAYS/`](../WINDOW_BAYS/)
- **Door cutouts**: [`../DOOR_SURROUNDS/`](../DOOR_SURROUNDS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Skin panel parts must meet:
- Dimensional tolerances for assembly fit
- Surface quality for aerodynamic smoothness (OML)
- Flatness/contour accuracy within specified limits
- Material thickness uniformity
- Pressure test requirements (IML)
