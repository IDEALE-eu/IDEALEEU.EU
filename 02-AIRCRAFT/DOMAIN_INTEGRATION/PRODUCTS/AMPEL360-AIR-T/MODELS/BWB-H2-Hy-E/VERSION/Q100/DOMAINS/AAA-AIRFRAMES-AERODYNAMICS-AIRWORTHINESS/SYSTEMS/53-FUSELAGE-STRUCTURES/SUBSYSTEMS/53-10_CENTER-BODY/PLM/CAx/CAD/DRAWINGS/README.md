# DRAWINGS — 2D Engineering Drawings

## Purpose

This directory contains 2D engineering drawings derived from CAD models for the 53-10 Center Body subsystem.

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
- `53-10_DWG_FRAME-F01_D0001_SH1.pdf`
- `53-10_DWG_SKIN-PANEL_D0025_SH1-3.pdf`
- `53-10_DWG_ASM_CENTER-BODY_D1000_SH1.pdf`

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
Export 2D geometry to `../EXPORTS/DXF/` for:
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
- **Company**: IDEALE consortium

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

## Drawing Types Detail

### Part Drawings
- Show all manufacturing features
- Include material specification
- Define surface finish requirements
- Specify heat treatment processes
- Note critical dimensions and tolerances
- Reference applicable standards

### Assembly Drawings
- Show assembled configuration
- Include BOM with item balloons
- Define assembly sequence notes
- Specify fastener types and torque
- Show interface connections
- Note critical assembly dimensions

### Installation Drawings
- Define interface datums and dimensions
- Show mating part requirements
- Include installation sequence
- Specify tooling requirements
- Note clearance and access requirements
- Define installation torque specs

## Organization

Group drawings by:
- **Component type**: Frames, stringers, skins, etc.
- **Drawing type**: Part, assembly, installation, detail
- **Zone/station**: Forward, center, aft sections

## Version Control

### Drawing Revisions
- **Revision letters**: A, B, C, ... (no I, O, Q)
- **Revision blocks**: Track changes with date, description, approver
- **ECN/ECO**: Engineering Change Notice/Order references
- **Release states**: Draft, Released, Obsolete

### Git Workflow
- Commit PDF versions for all drawings
- Include source files (DXF, DWG) if size permits
- Use Git LFS for large drawing files (> 10 MB)
- Tag releases with version/configuration identifiers

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

### Review Process
- **Self-check**: Designer verifies completeness
- **Peer review**: Another engineer checks technical content
- **Checker approval**: Senior engineer or checker signs off
- **Engineering approval**: Chief engineer or designee approves
- **Configuration control**: Drawing entered into PDM/PLM system

## References

### Related Directories
- **CAD models**: `../MODELS/` and `../ASSEMBLIES/`
- **DXF exports**: `../EXPORTS/DXF/`
- **STEP exports**: `../EXPORTS/STEP/`
- **EBOM links**: `../../EBOM_LINKS.md`

### Applicable Standards
- **ASME Y14.5**: GD&T standard
- **ISO 1101**: Geometrical tolerancing (European)
- **ATA iSpec 2200**: Technical publications
- **AS9100**: Aerospace quality management
- **General tolerances**: `../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`

## Best Practices

### Drawing Creation
1. Start from 3D CAD model views
2. Apply appropriate scale for clarity
3. Add dimensions progressively (location, size, form)
4. Apply GD&T to critical features
5. Add notes for processes and materials
6. Complete title block
7. Export to PDF/A for distribution

### Drawing Maintenance
- Update drawings when models change
- Track revision history in revision block
- Archive superseded revisions
- Maintain drawing-model associativity
- Validate after model changes

### Manufacturing Handoff
- Provide complete drawing packages
- Include all referenced standards
- Supply neutral formats (DXF for 2D, STEP for 3D)
- Coordinate with manufacturing engineering
- Support supplier questions and RFIs
