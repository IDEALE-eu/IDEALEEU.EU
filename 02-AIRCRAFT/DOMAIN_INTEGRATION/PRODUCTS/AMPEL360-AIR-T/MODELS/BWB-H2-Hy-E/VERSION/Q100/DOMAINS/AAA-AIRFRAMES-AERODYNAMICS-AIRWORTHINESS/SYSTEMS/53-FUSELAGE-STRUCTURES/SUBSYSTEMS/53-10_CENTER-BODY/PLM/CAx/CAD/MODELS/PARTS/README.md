# PARTS — Individual Component Models

## Purpose

This directory contains CAD models for individual structural parts that make up the 53-10 Center Body structure. Each part is modeled as a discrete component with its own design, manufacturing, and inspection requirements.

## Organization

Parts are organized by structural category:

- **FRAMES/** — Circumferential structural frames
- **STRINGERS/** — Longitudinal stiffening members
- **SKIN_PANELS/** — Outer and inner skin panels
- **FLOORS/** — Floor panels and beams
- **BULKHEADS/** — Pressure and non-pressure bulkheads
- **INTERFACE_FITTINGS/** — Attachment fittings for system interfaces
- **MOUNTS/** — Equipment and component mounting provisions
- **TANK_SUPPORTS/** — Support structures for fuel/hydrogen tanks
- **BRACKETS_CLIPS/** — Secondary structure elements

## Naming Convention

Use the following pattern for part files:
```
53-10_<CATEGORY>_<PART-ID>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_FRAME_FR-001_FWD-PRESSURE_v01.CATPart`
- `53-10_STRINGER_STR-L-015_LEFT-UPPER_v02.prt`
- `53-10_SKIN_PANEL_SP-AFT-002_OUTER_v01.sldprt`

## File Requirements

Each part model should include:
- Full parametric design history
- Material properties defined
- Mass properties calculated
- Design parameters documented
- Manufacturing features (bend allowances, relief cuts, etc.)

## Related Documentation

- **Assembly models**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Engineering drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
- **Master geometry**: [`../MASTER/`](../MASTER/)
- **Standards**: [`../LIBRARY/`](../LIBRARY/)

## Quality Standards

All parts must:
- Follow design rules in [`../CONFIG/DESIGN_RULES/`](../CONFIG/DESIGN_RULES/)
- Use parameters from [`../CONFIG/PARAMETERS/`](../CONFIG/PARAMETERS/)
- Include metadata per [`../METADATA/`](../METADATA/) requirements
- Pass checks in [`../CHECKS/`](../CHECKS/) before release
