# DRILL_TEMPLATES — Drilling Templates

## Purpose
DXF files for drilling templates, jig plates, and hole pattern layouts.

## Contents
- Hole pattern layouts for drilling operations
- Template geometry for drill jigs
- Bushing locations for guided drilling
- Coordinate hole patterns
- Match-drilling references

## Template Types
- Fixed drill templates (jig plates)
- Coordinate drilling patterns
- Match-drill templates
- Assembly drilling layouts
- Inspection hole patterns

## Layer Structure
**Standard layers**:
- **TEMPLATE_OUTLINE**: Template boundary
- **HOLES**: Hole locations and diameters
- **BUSHINGS**: Drill bushing locations
- **REFERENCE**: Reference points and datums
- **TEXT**: Hole callouts and specifications
- **DIMENSIONS**: Coordinate dimensions

## Hole Information
Specify for each hole:
- Hole diameter
- Drilling depth (if applicable)
- Countersink/counterbore details
- Fastener type and size
- Tolerance requirements
- Drilling sequence if critical

## Coordinate System
- Establish clear datum references (A, B, C)
- Use X-Y coordinate system
- Document zero reference point
- Include coordinate tables for holes
- Specify measurement units (mm or inches)

## File Naming
```
<assembly>_DRILL-TEMPLATE_<zone>_<revision>_<date>.dxf
```

Examples:
- `53-10-FRM01_DRILL-TEMPLATE_FWD_A_20250110.dxf`
- `53-10-SKIN-PANEL_DRILL-PATTERN_CTR_B_20250110.dxf`

## Manufacturing Specifications
Include:
- Drill bit sizes
- Drilling speed and feed recommendations
- Tool reach requirements
- Access considerations
- Clamping requirements
- Chip evacuation notes

## Template Construction
For physical templates:
- Material: Typically aluminum or steel
- Thickness: Adequate for drill bushings
- Bushing specifications: Size and type
- Locating features: Pins, holes, edges
- Identification markings

## Related Directories
- **[../../../../CAM/TOOLING/](../../../../CAM/TOOLING/)** — Tooling designs
- **[../PANEL_STACKUPS/](../PANEL_STACKUPS/)** — Panel assembly drawings
- **[../../INSTALLATION/](../../INSTALLATION/)** — Installation templates

## Validation
Before use:
- [ ] All hole locations verified
- [ ] Coordinate dimensions checked
- [ ] Datum references clear
- [ ] Hole sizes correct for fasteners
- [ ] Template fits assembly correctly
- [ ] Clearances verified

## Notes
- Use for high-precision or repetitive drilling
- Coordinate with assembly process
- Consider drill tool access
- Account for material thickness stack-up
- Verify compatibility with production equipment
