# DRAWINGS — 2D Engineering Drawings 

## Purpose

This directory contains 2D engineering drawings derived from CAD models for the 53_00 Structural Body subsystem.

## What to Store

### Drawing Types
- **Part drawings**: Individual component details with dimensions and tolerances
- **Assembly drawings**: Assembly views showing component relationships
- **Installation drawings**: Interface control and installation instructions
- **Detail drawings**: Enlarged views of critical features
- **Interface control drawings (ICDs)**: System boundary definitions

### Drawing Content
- **Dimensional information**: GD&T, tolerances, datums
- **Material callouts**: Material specifications and treatments
- **Surface finish**: Roughness requirements and coating specs
- **Fastener schedules**: Bolt/rivet patterns and specifications
- **Notes and standards**: Applicable specs, processes, standards

## Naming Convention

Use the following naming pattern:
```
<subsystem>_DWG_<component>_<drawing-number>_<sheet>.<ext>
```

Examples:
- `53_00_DWG_FRAME-F01_D0001_SH1.pdf`
- `53_00_DWG_SKIN-PANEL_D0025_SH1-3.pdf`
- `53_00_DWG_ASM_STRUCTURAL-BODY_D1000_SH1.pdf`

## File Formats

### Distribution Formats (Required)
- **PDF**: Primary distribution format, PDF/A-1 for archival
- **PDF/3D**: Interactive 3D PDF with embedded models

### Source Formats (Optional)
- **DXF**: AutoCAD exchange format for 2D geometry
- **DWG**: Native AutoCAD format
- **CATIA Drawing**: `.CATDrawing`
- **SolidWorks Drawing**: `.slddrw`
- **NX Drafting**: `.prt` (drawings in NX are part files)

### Export to DXF
Export 2D geometry to [`../EXPORTS/DXF/`](../EXPORTS/DXF/) for:
- Manufacturing (CNC programming)
- Laser cutting templates
- Sheet metal development
- Inspection overlays

## Drawing Standards

### Title Block Requirements
- **Drawing number**: Unique identifier
- **Revision**: Latest revision letter
- **Title**: Part/assembly description
- **Scale**: Drawing scale (or "AS NOTED")
- **Units**: Inches or millimeters
- **Date**: Release date
- **Drawn by**: Author initials/name
- **Checked by**: Checker initials/name
- **Approved by**: Engineering approval
- **Organization**: IDEALE consortium

### View Layout
- **Standard views**: Front, top, right, isometric
- **Section views**: Critical internal features
- **Detail views**: Callouts for small features (2X, 4X scale)
- **Exploded views**: Assembly sequence (for assembly drawings)

### Dimensioning
- **Geometric Dimensioning and Tolerancing (GD&T)**: Per ASME Y14.5 or ISO 1101
- **Reference datums**: A, B, C datum system
- **Critical dimensions**: Manufacturing and inspection critical dims
- **Tolerances**: Per general tolerance block or specific callouts

## Quality Requirements

### Drawing Checks
Before releasing drawings:
- [ ] All dimensions shown and toleranced
- [ ] Material callouts complete
- [ ] Surface finish specified
- [ ] GD&T applied correctly
- [ ] Title block complete
- [ ] Revision block updated
- [ ] Drawing number unique
- [ ] PDF exported at correct scale
- [ ] No model-to-drawing discrepancies

## References

### Related Directories
- **CAD models**: [`../MODELS/`](../MODELS/) and [`../ASSEMBLIES/`](../ASSEMBLIES/)
- **DXF exports**: [`../EXPORTS/DXF/`](../EXPORTS/DXF/)
- **STEP exports**: [`../EXPORTS/STEP/`](../EXPORTS/STEP/)
- **EBOM links**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)

### Applicable Standards
- **ASME Y14.5**: GD&T standard
- **ISO 1101**: Geometrical tolerancing
- **ECSS-Q-ST-70C**: Materials, mechanical parts and processes
- **AS9100**: Aerospace quality management
