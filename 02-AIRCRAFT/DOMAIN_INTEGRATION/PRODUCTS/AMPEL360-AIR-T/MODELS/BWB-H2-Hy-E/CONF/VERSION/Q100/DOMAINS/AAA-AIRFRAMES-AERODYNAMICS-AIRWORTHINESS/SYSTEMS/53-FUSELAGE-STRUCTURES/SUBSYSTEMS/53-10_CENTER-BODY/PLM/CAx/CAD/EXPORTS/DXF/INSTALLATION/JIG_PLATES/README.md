# JIG_PLATES — Installation Jig Plates

## Purpose
DXF files for physical jig plates and fixtures used during installation and assembly.

## Contents
- Jig plate geometry and profiles
- Locating feature locations (pins, holes)
- Mounting hole patterns
- Reference surfaces and datums
- Clamping points
- Support structures

## Jig Plate Types
- **Location jigs**: Position parts accurately
- **Clamping jigs**: Hold parts during assembly
- **Welding/bonding jigs**: Support during joining
- **Alignment jigs**: Ensure correct alignment
- **Transport jigs**: Support during handling

## Layer Structure
**Standard layers**:
- **JIG_OUTLINE**: Jig plate boundary
- **LOCATORS**: Locating pins, holes, edges
- **MOUNTING**: Mounting holes and interfaces
- **REFERENCE**: Datum references
- **CLAMPS**: Clamping point locations
- **TEXT**: Jig identification and notes
- **DIMENSIONS**: Manufacturing dimensions

## Jig Plate Information
Specify:
- Material: Aluminum, steel, composite
- Thickness: Plate thickness
- Surface finish: As-machined, anodized, etc.
- Hardness requirements: If applicable
- Weight: For handling considerations
- Locating features: Pin sizes, hole tolerances

## Locating Features
Document:
- **Locating pins**: Diameter, length, tolerance
- **Locating holes**: Diameter, depth, tolerance
- **Reference edges**: Machining tolerances
- **Datums**: Primary, secondary, tertiary
- **Tolerance stack-up**: Critical dimensions

## File Naming
```
<assembly>_JIG-PLATE_<description>_<revision>_<date>.dxf
```

Examples:
- `53-10_JIG-PLATE_FRAME-FWD_A_20250110.dxf`
- `53-10_JIG-PLATE_PANEL-BONDING_B_20250110.dxf`
- `53-10_JIG-PLATE_ASSEMBLY-LOC_A_20250110.dxf`

## Manufacturing Specifications
Include:
- Material specification and thickness
- Machining tolerances
- Surface finish requirements
- Heat treatment (if required)
- Locating feature tolerances (typically ±0.05 mm)
- Edge break and deburring requirements

## Related Directories
- **[../../../../CAM/TOOLING/FIXTURES_JIGS/](../../../../CAM/TOOLING/FIXTURES_JIGS/)** — 3D tooling models
- **[../OVERLAYS/](../OVERLAYS/)** — Installation overlays
- **[../../ASSEMBLIES/DRILL_TEMPLATES/](../../ASSEMBLIES/DRILL_TEMPLATES/)** — Drill templates

## Usage Considerations
- Design for easy part loading/unloading
- Minimize obstruction to access
- Consider operator ergonomics
- Allow for inspection access
- Plan for maintenance and cleaning
- Include identification markings

## Validation
Before fabrication:
- [ ] Locating features verified against assembly
- [ ] Clearances checked for part and tools
- [ ] Material and thickness appropriate
- [ ] Tolerances achievable and appropriate
- [ ] Mounting interfaces compatible
- [ ] Handling features included

## Maintenance
- Store jigs in designated location
- Inspect locating features regularly
- Clean after use
- Document any damage or wear
- Calibrate periodically if required
