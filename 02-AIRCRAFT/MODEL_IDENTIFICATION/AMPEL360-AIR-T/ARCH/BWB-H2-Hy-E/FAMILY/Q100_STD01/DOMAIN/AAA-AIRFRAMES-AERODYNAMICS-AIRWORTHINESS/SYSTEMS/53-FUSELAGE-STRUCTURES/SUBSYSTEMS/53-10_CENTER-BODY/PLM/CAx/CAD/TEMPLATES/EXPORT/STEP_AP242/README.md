# STEP_AP242 — STEP Export Templates and Settings

## Purpose

Export settings and templates for STEP AP242 (ISO 10303-242) format, the primary 3D neutral format for aerospace applications.

## STEP AP242 Overview

**Standard:** ISO 10303-242 "Managed Model Based 3D Engineering"

**Advantages:**
- Industry standard for aerospace and automotive
- Supports PMI (Product Manufacturing Information)
- Preserves assembly structure and relationships
- Includes material properties and attributes
- Better than STEP AP203 (geometry only)
- Vendor-neutral, long-term archival format

## Export Settings Template

### Recommended Settings
```
Protocol: AP242
Schema: Managed model based 3D engineering MIM LF
Application Protocol: AP242
Configuration: Design

Geometry:
  ☑ Solids (BREP representation)
  ☑ Surfaces (trimmed surfaces)
  ☑ Wireframe (curves and edges)
  ☐ Construction geometry (exclude)
  ☐ Reference geometry (exclude for clean export)

Assembly:
  ☑ Preserve assembly structure
  ☑ Include component instances
  ☑ Maintain hierarchy
  ☐ Flatten (keep hierarchical)

Attributes:
  ☑ Part properties (name, description, part number)
  ☑ Material specification
  ☑ Mass properties (mass, volume, center of gravity)
  ☑ Custom attributes (selected critical attributes)

PMI (Product Manufacturing Information):
  ☑ GD&T annotations
  ☑ Dimensions (semantic dimensions)
  ☑ Tolerances
  ☑ Surface finish callouts
  ☑ Notes and labels

Units: Millimeters (mm)
Coordinate system: Global aircraft frame (FS, BL, WL)
Precision: 0.001 mm
Validation: Enable (check for errors before export)
```

## CAD System Specific Settings

### CATIA V5/V6
**File → Save As → STEP**
- Format: STEP AP242
- Options → Assembly structure: Keep assembly
- Options → With GD&T: Yes
- Options → Export properties: Yes

### Siemens NX
**File → Export → STEP214**
- Application Protocol: AP242
- Output Type: Assembly
- PMI: Export annotations
- Options: Export attributes

### SOLIDWORKS
**File → Save As → STEP (*.step; *.stp)**
- Options → Output as: AP242
- Export as: Assembly
- Include: Annotations, Materials, Properties

### PTC Creo
**File → Save As → Save a Copy**
- Type: STEP AP242 (*.stp)
- Options → Assembly structure: Design
- Options → Export PMI: Yes

## Validation Checklist

After export, verify:
- [ ] File opens without errors in neutral viewer
- [ ] All parts/assemblies are present
- [ ] Assembly structure is preserved
- [ ] Geometry is complete (no missing faces/edges)
- [ ] Units are correct (check a known dimension)
- [ ] Materials are assigned
- [ ] PMI annotations are visible (if included)
- [ ] Part properties are populated
- [ ] File size is reasonable (not corrupted)

## Quality Control

### Visual Inspection
- Open in STEP viewer (e.g., FreeCAD, Open CASCADE)
- Check geometry integrity
- Verify assembly mates/positions
- Confirm annotations if included

### Dimensional Check
- Measure known dimensions
- Verify coordinate system origin
- Check overall bounding box

### Metadata Check
- Part numbers present
- Descriptions populated
- Materials assigned
- Mass properties calculated

## File Organization

### Naming Convention
```
<part-number>_<description>_STEP_v<version>.step
```

**Examples:**
- `53-10-001_FRAME-F01_STEP_v01.step`
- `53-10_ASM_CENTER-BODY_COMPLETE_STEP_v01.step`

### Directory Structure
```
STEP_AP242/
├── PARTS/
│   ├── 53-10-001_FRAME-F01_STEP_v01.step
│   ├── 53-10-002_FRAME-F02_STEP_v01.step
│   └── ...
├── ASSEMBLIES/
│   ├── 53-11_ASM_FRAME-SECTION_FWD_STEP_v01.step
│   ├── 53-10_ASM_CENTER-BODY_COMPLETE_STEP_v01.step
│   └── ...
└── README.md
```

## Best Practices

### For Design Reviews
- Export complete assembly with substructure
- Include PMI for critical features
- Add material specifications
- Include mass properties

### For Suppliers
- Export individual parts with tolerances
- Include PMI and GD&T
- Provide material specifications separately
- Include manufacturing notes in attributes

### For Analysis (FEA/CFD)
- Export simplified geometry (defeature if needed)
- Exclude PMI (cleaner geometry)
- Include material assignment
- Consider exporting surfaces only for CFD

### For Archive/Baseline
- Export both assemblies and individual parts
- Include all attributes and properties
- Calculate SHA-256 checksum
- Store with release documentation

## Troubleshooting

### Common Issues

**Issue:** File size too large
- **Solution:** Exclude reference/construction geometry, reduce precision if acceptable

**Issue:** Assembly structure lost
- **Solution:** Check export settings, ensure "preserve assembly" is enabled

**Issue:** PMI not visible
- **Solution:** Verify PMI export option is enabled, check receiving software PMI support

**Issue:** Materials not transferred
- **Solution:** Check material assignment in source CAD, enable attribute export

**Issue:** Dimensions/units incorrect
- **Solution:** Verify unit settings in export dialog (should be mm)

## Related Files

- Parent directory: [`../README.md`](../README.md)
- IGES export: [`../IGES/README.md`](../IGES/README.md)
- JT export: [`../JT/README.md`](../JT/README.md)
- Main exports: [`../../../EXPORTS/STEP/README.md`](../../../EXPORTS/STEP/README.md)

## References

- ISO 10303-242 standard documentation
- CAx Implementor Forum (CAx-IF) recommended practices
- LOTAR standard (Long Term Archiving and Retrieval)
- Company STEP export procedures
