# SHEET_METAL — Sheet Metal Parts

## Purpose
DXF files for sheet metal parts including bending and forming details.

## Contents
- Sheet metal part profiles
- Bend lines and bend angles
- Forming features (flanges, hems, etc.)
- Relief notches and cutouts
- Hole patterns

## Part Types
- Brackets and fittings
- Covers and panels
- Stiffeners and doublers
- Clips and angles
- Formed channels

## Layer Structure
**Standard layers**:
- **CUTTING**: Outer cutting profile
- **BENDING**: Bend lines with angles
- **HOLES**: Hole locations, diameters
- **FORMING**: Forming features (emboss, dimple)
- **TEXT**: Manufacturing notes
- **DIMENSIONS**: Critical dimensions

## Bend Information
Specify for each bend:
- Bend angle (e.g., 90°, 135°)
- Bend radius (inside radius)
- Bend direction (up/down)
- Bend sequence if critical
- K-factor or bend allowance

## Manufacturing Specifications
Include as annotations:
- Material: Grade and temper (e.g., AL 2024-T3)
- Thickness: Sheet thickness in mm or inches
- Bend radius: Inside bend radius
- Tolerances: Dimensional and angular tolerances
- Surface treatment: Anodize, paint, etc.

## File Naming
```
<part-number>_<description>_<thickness>_<revision>_<date>.dxf
```

Examples:
- `53-10-BRK01_BRACKET-FWD_2MM_A_20250110.dxf`
- `53-10-STF20_STIFFENER_1.5MM_B_20250110.dxf`

## Related Directories
- **[../FLAT_PATTERNS/](../FLAT_PATTERNS/)** — Flat pattern developments
- **[../../NESTING/](../../NESTING/)** — Material nesting layouts
- **[../../../../CAM/NC_PROGRAMS/](../../../../CAM/NC_PROGRAMS/)** — NC programs for cutting/bending

## Quality Requirements
- All contours must be closed
- Bend lines properly annotated
- Material callout clearly specified
- No overlapping geometry
- Proper layer organization
