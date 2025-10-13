# EXPORT — CAD Export Standards and Settings

## Purpose

Standardized export settings, file formats, and procedures for sharing CAD data from the 53-10 Center Body design work.

## Directory Structure

```
EXPORT/
├── STEP_AP242/      # Primary 3D neutral format
├── IGES/            # Legacy 3D format
├── DXF/             # 2D drawings and profiles
├── JT/              # Lightweight visualization
└── README.md        # This file
```

## Export Formats Overview

### STEP (ISO 10303-242)
- **Primary format** for 3D geometry exchange
- Includes PMI (Product Manufacturing Information)
- Preserves assembly structure
- Contains attributes and metadata
- Industry-standard for aerospace

### IGES (Initial Graphics Exchange Specification)
- **Legacy format** for 3D geometry
- Widely supported (older CAD systems)
- Less robust than STEP
- Use only when specifically requested

### DXF (Drawing Exchange Format)
- **2D format** for drawings and profiles
- Good for sheet metal flat patterns
- Compatible with manufacturing systems
- Use for NC programming, laser cutting

### JT (ISO 14306)
- **Lightweight format** for visualization
- Fast loading of large assemblies
- Suitable for design reviews
- Integration with digital mockup tools

## Export Use Cases

### For Suppliers/Partners
**Primary:**
- STEP AP242 (3D models with PMI)
- PDF drawings (2D documentation)
- Material specifications (separate document)

**Optional:**
- JT (for visualization/review)
- IGES (if supplier requires legacy format)

### For Manufacturing
**Internal:**
- Native CAD files (CATIA, NX, etc.)
- STEP AP242 (for CAM systems)
- DXF (2D profiles for sheet metal)

**External:**
- STEP AP242 (with tolerances)
- PDF drawings
- DXF (2D for NC programming)

### For Analysis Teams
**FEA/CFD:**
- STEP (for geometry import)
- IGES (if STEP not supported)
- Simplified geometry (defeature for mesh)

**Visualization:**
- JT (lightweight review)
- STEP (detailed geometry)

### For Configuration Management
**Baseline/Release:**
- Native CAD files (master data)
- STEP AP242 (neutral archive format)
- PDF drawings (non-editable documentation)
- SHA-256 checksums (data integrity)

## Export Settings by Format

### STEP AP242 Export Settings

**General Settings:**
- Protocol: AP242
- Schema: Managed model based 3D engineering
- Assembly structure: Preserve hierarchy
- Configuration: Current configuration only

**Geometry Settings:**
- Solids: Yes
- Surfaces: Yes
- Wireframe: Yes
- Reference geometry: Optional (exclude for cleaner file)
- Construction geometry: Exclude

**Attributes:**
- Part properties: Include
- Material: Include
- Mass properties: Include
- Custom attributes: Include critical attributes only

**PMI (Product Manufacturing Information):**
- GD&T annotations: Include
- Dimensions: Include (if semantic)
- Notes: Include
- Tolerance definitions: Include

**File Options:**
- Units: Millimeters (mm)
- Precision: 0.001 mm
- Validation: Enable (check for errors)

### IGES Export Settings

**Version:** 5.3 (most compatible)

**Geometry:**
- Surfaces: Trimmed surfaces
- Solids: BREP solids (type 186)
- Wireframe: Include curves
- Assembly: Single file or multiple files

**Options:**
- Units: Millimeters (mm)
- Precision: 0.001 mm
- Trim surfaces: Yes
- Convert to NURBS: Yes

**Limitations:**
- No PMI support
- Limited attribute support
- May lose assembly structure

### DXF Export Settings

**Version:** AutoCAD 2018 or later

**Content:**
- 2D geometry only
- Dimensions (if applicable)
- Layer structure preserved
- Text and annotations

**Options:**
- Units: Millimeters (mm)
- Precision: 0.01 mm
- Explode dimensions: No (keep associative if possible)
- Export to model space

**Use Cases:**
- Flat patterns for sheet metal
- 2D profiles for machining
- Drawing views for documentation

### JT Export Settings

**Version:** JT 10.5 or later

**Geometry:**
- Tessellation: High quality
- Wireframe: Include edges
- PMI: Include if available
- Assembly structure: Preserve

**Options:**
- Units: Millimeters (mm)
- Level of Detail (LOD): Medium to High
- Compression: Enable for file size reduction
- Attributes: Include basic properties

**Use Cases:**
- Lightweight design reviews
- Digital mockup
- Visualization in non-CAD tools

## Export Naming Convention

### File Naming Template
```
<part-number>_<description>_<format>_<version>.<ext>
```

**Examples:**
- `53-10-001_FRAME-F01_STEP_v01.step`
- `53-10-001_FRAME-F01_IGES_v01.igs`
- `53-10-001_FRAME-F01_DXF_v01.dxf`
- `53-10_ASM_CENTER-BODY_JT_v01.jt`

### Directory Organization
```
EXPORT/
├── STEP_AP242/
│   ├── 53-10-001_FRAME-F01_STEP_v01.step
│   ├── 53-10-002_FRAME-F02_STEP_v01.step
│   └── 53-10_ASM_CENTER-BODY_STEP_v01.step
├── IGES/
│   ├── 53-10-001_FRAME-F01_IGES_v01.igs
│   └── ...
├── DXF/
│   ├── 53-10-001_FRAME-F01_FLAT-PATTERN_DXF_v01.dxf
│   └── ...
└── JT/
    ├── 53-10_ASM_CENTER-BODY_JT_v01.jt
    └── ...
```

## Export Validation

### Quality Checks
After export, verify:
- File size is reasonable (not corrupted)
- Geometry is complete (no missing surfaces)
- Assembly structure is preserved (if applicable)
- Units are correct (millimeters)
- Attributes are included (if required)

### Import Test
- Import exported file into receiving CAD system
- Check for errors or warnings
- Verify geometry integrity
- Confirm dimensions (spot check)

### Automation
See [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) for:
- `export_batch_step.py` — Batch export to STEP
- `export_batch_iges.py` — Batch export to IGES
- `validate_exports.py` — Validate exported files
- `generate_export_report.py` — Export summary report

## Export Documentation

### Export Package Contents
When delivering CAD data, include:
1. **Exported files** (STEP, PDF, etc.)
2. **Readme file** describing contents
3. **Material specifications** (separate document)
4. **Assembly instructions** (if applicable)
5. **Change log** (if revised)
6. **Checksums** (SHA-256) for file integrity

### Export Metadata
Document in README.txt:
- Export date and time
- Source CAD system and version
- Export settings used
- Units and coordinate system
- Known limitations or issues
- Contact information

## Related Directories

- **Part Templates**: [`../PART/`](../PART/)
- **Assembly Templates**: [`../ASSEMBLY/`](../ASSEMBLY/)
- **STEP Export**: [`./STEP_AP242/`](./STEP_AP242/)
- **IGES Export**: [`./IGES/`](./IGES/)
- **DXF Export**: [`./DXF/`](./DXF/)
- **JT Export**: [`./JT/`](./JT/)
- **Scripts/Macros**: [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/)

## References

- Main exports documentation: [`../../EXPORTS/README.md`](../../EXPORTS/README.md)
- STEP AP242 standard: ISO 10303-242
- IGES standard: IGES 5.3
- JT standard: ISO 14306
- Company data exchange procedures
