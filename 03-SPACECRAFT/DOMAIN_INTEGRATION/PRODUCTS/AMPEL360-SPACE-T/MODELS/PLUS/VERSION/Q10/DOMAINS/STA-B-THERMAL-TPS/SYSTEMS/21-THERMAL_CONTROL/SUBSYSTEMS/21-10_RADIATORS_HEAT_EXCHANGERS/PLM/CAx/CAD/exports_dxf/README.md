# EXPORTS_DXF — DXF Format Exports (Flat Patterns)

## Purpose

This directory contains DXF (Drawing Exchange Format) exports of flat patterns for sheet metal parts, facesheet blanks, and other 2D geometry used in the fabrication of 21-10 radiators and heat exchangers.

## DXF Format

### Standard
- **AutoCAD DXF**: Industry-standard 2D CAD exchange format
- **Version**: R14/2000 or later (for maximum compatibility)
- **ASCII format**: Preferred for human readability and version control

### Use Cases
- **Sheet metal fabrication**: Flat patterns for laser cutting, waterjet, punch press
- **Facesheet blanks**: 2D outlines for aluminum facesheets
- **Gasket cutting**: Templates for TIM and gasket materials
- **Drilling patterns**: Hole locations for CNC drilling
- **Inspection templates**: 2D layouts for CMM programming

## Content

### What to Export
- **Flat patterns**: Unfolded sheet metal parts with bend lines
- **Blank outlines**: 2D contours of flat parts before forming
- **Hole patterns**: Drilling templates with precise hole locations
- **Cutting paths**: Laser/waterjet cutting paths
- **Inspection layouts**: 2D geometry for CMM and inspection

### What NOT to Export
- 3D geometry (use STEP format in `../exports_step/`)
- Complete assembly drawings (use PDF in `../drawings/`)
- Construction geometry and reference lines (unless needed for manufacturing)

## Naming Convention

```
21-10_DXF_<type>_<description>__r<NN>__<status>.dxf
```

Examples:
- `21-10_DXF_FACESHEET_BLANK_TOP__r02__REL.dxf`
- `21-10_DXF_MANIFOLD_FLAT-PATTERN__r01__REL.dxf`
- `21-10_DXF_DRILLING_MOUNT-HOLES__r03__REL.dxf`
- `21-10_DXF_GASKET_TIM-PAD__r01__RVW.dxf`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released

## Export Requirements

### When to Export
- **Mandatory**: Sheet metal parts at REL status requiring flat pattern manufacturing
- **Mandatory**: Parts with complex 2D profiles requiring CNC cutting
- **Optional**: Inspection templates and drilling patterns as needed
- **Not required**: Solid parts without flat pattern representation

### Units and Precision
- **Units**: Millimeters (mm) - must be clearly defined in DXF header
- **Decimal places**: Minimum 3 decimal places (0.001 mm precision)
- **Origin**: Align to convenient manufacturing origin (typically lower-left corner)

## Layer Organization

### Standard Layers
- **0 (Default)**: Main geometry outline
- **OUTLINE**: Part outline / cutting path
- **HOLES**: Hole centers and diameters
- **BEND_LINES**: Bend lines for sheet metal (dashed)
- **DIMENSIONS**: Reference dimensions (if included)
- **TEXT**: Part number, material, thickness notes
- **CONSTRUCTION**: Construction geometry (hidden or separate)

### Layer Properties
- Use consistent line types (continuous, dashed, center)
- Set appropriate line weights (0.25mm for outline, 0.13mm for details)
- Use color coding if helpful for manufacturing process

## Content Requirements

### Flat Pattern Data
- [ ] Complete outer profile (closed polyline)
- [ ] All holes with correct diameters and positions
- [ ] Bend lines clearly marked (for sheet metal)
- [ ] Material thickness noted
- [ ] Bend radii specified (if applicable)
- [ ] Grain direction indicated (if critical)
- [ ] Reference edges/datums identified

### Annotation (Minimal)
- Part number in text layer
- Material specification
- Thickness (for sheet metal)
- Revision level
- Scale (typically 1:1 for manufacturing)

### Geometry Quality
- [ ] All polylines closed where appropriate
- [ ] No duplicate or overlapping geometry
- [ ] Consistent units throughout file
- [ ] Origin at logical manufacturing reference
- [ ] Geometry simplified (no construction curves unless needed)

## Export Settings

### Recommended Settings
- **Format**: ASCII DXF (not binary)
- **Version**: AutoCAD R14/2000 or later
- **Units**: Millimeters (set explicitly)
- **Precision**: 0.001 mm (3 decimal places minimum)
- **Layers**: Organize by feature type
- **Line types**: Use standard AutoCAD line types
- **Text**: Use standard AutoCAD fonts (avoid custom fonts)

### Geometry Simplification
- Remove construction geometry unless needed for manufacturing
- Convert splines to polylines if acceptable (maintain tolerance < 0.01 mm)
- Remove hidden or internal features not needed for fabrication
- Simplify complex profiles where possible without losing critical features

## Quality Checks

### Pre-Export Validation
- [ ] CAD flat pattern is correct and complete
- [ ] All holes and features present
- [ ] Dimensions and tolerances verified against drawing
- [ ] Bend lines and bend allowances calculated correctly
- [ ] Material thickness set correctly

### Post-Export Validation
- [ ] DXF file opens in target CAM software without errors
- [ ] Units are millimeters (verify scale)
- [ ] All geometry on correct layers
- [ ] Hole diameters correct
- [ ] Part outline closed and continuous
- [ ] No extraneous or duplicate geometry
- [ ] File size reasonable (< 10 MB typical for 2D)

### Validation Tools
- CAD system DXF preview
- AutoCAD or compatible viewer (DraftSight, LibreCAD)
- CAM software import test
- Geometry comparison with source CAD model

## Manufacturing Integration

### CNC Cutting
- Provide closed polylines for cutting paths
- Specify kerf compensation requirements (if any)
- Indicate part orientation and nesting allowances
- Document lead-in/lead-out requirements

### CNC Drilling
- Hole centers as points or small circles
- Hole diameters as attributes or on separate layer
- Through-holes vs. countersunk/counterbored indicated
- Thread callouts documented

### Sheet Metal Forming
- Bend lines clearly marked with line type
- Bend direction indicated (up or down)
- Bend radius and K-factor documented
- Bend sequence documented (if critical)

## Traceability

### Source Documentation
- Link to 3D CAD part model
- Reference to part drawing in `../drawings/`
- Material and thickness specification
- Reference to manufacturing process plan (CAP/CAM)

### EBOM Integration
- DXF files referenced in EBOM_LINKS.md for applicable parts
- Part numbers match EBOM structure
- Revision control synchronized with 3D model

## Revision Control

### File Versioning
- DXF revision must match CAD model and drawing revision
- Update DXF whenever flat pattern geometry changes
- Document changes in revision notes
- Archive superseded versions

### Change Management
- Coordinate changes with manufacturing
- Verify updated DXF produces acceptable parts
- Update CAM programs if DXF changes significantly

## File Organization

### Structure
```
exports_dxf/
├─ 21-10_DXF_FACESHEET_BLANK_TOP__r02__REL.dxf
├─ 21-10_DXF_FACESHEET_BLANK_BOTTOM__r02__REL.dxf
├─ 21-10_DXF_MANIFOLD_FLAT-PATTERN__r01__REL.dxf
├─ 21-10_DXF_DRILLING_MOUNT-HOLES__r03__REL.dxf
└─ ...
```

### Archival
- Keep only current REL revision in main directory
- Archive superseded versions per configuration management plan
- Maintain traceability to source 3D model and drawings

## Related Directories

- **Parts**: [`../parts/`](../parts/) - Source 3D part models
- **Drawings**: [`../drawings/`](../drawings/) - Corresponding manufacturing drawings
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - 3D neutral format exports
- **CAM**: [`../../CAM/`](../../CAM/) - CNC programs using DXF files
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - Engineering BOM links

## Standards References

- **ISO 10303-21**: STEP exchange file format (for comparison)
- **ISO 128**: Technical drawings - General principles of presentation
- **ASME Y14.5**: Dimensioning and tolerancing
- **DXF Reference**: AutoCAD DXF format documentation

---

**Last Updated**: 2025-10-10
