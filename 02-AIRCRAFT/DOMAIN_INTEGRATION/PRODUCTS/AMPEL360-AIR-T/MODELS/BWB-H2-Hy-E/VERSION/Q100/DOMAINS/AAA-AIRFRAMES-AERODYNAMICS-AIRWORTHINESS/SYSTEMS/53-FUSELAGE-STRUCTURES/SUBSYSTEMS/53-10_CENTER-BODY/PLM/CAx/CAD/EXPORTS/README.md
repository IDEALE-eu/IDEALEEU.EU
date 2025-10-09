# EXPORTS — Neutral Format CAD Exports

## Purpose

This directory contains neutral format exports of CAD models for long-term archival, data exchange with partners, and cross-platform interoperability.

## Overview

Neutral formats enable:
- **Vendor independence**: Files readable across different CAD systems
- **Long-term archival**: Format stability for decades of data preservation
- **Supply chain collaboration**: Exchange with partners using different tools
- **Manufacturing handoff**: Provide to suppliers without native CAD tools
- **Regulatory compliance**: Archival per aerospace regulations (e.g., FAA, EASA)

## Supported Formats

This directory contains exports in four industry-standard neutral formats:

### STEP (ISO 10303-242)
**Directory**: [`./STEP/`](./STEP/)
- **Best for**: 3D geometry, assemblies, PMI (GD&T)
- **Use cases**: Primary exchange format for aerospace
- **Details**: See [`./STEP/README.md`](./STEP/README.md)

### IGES (Initial Graphics Exchange Specification)
**Directory**: [`./IGES/`](./IGES/)
- **Best for**: 3D surfaces and wireframe
- **Use cases**: Legacy systems, CAM systems
- **Details**: See [`./IGES/README.md`](./IGES/README.md)

### JT (ISO 14306)
**Directory**: [`./JT/`](./JT/)
- **Best for**: Lightweight visualization, large assemblies
- **Use cases**: Design reviews, PLM integration
- **Details**: See [`./JT/README.md`](./JT/README.md)

### DXF (Drawing Exchange Format)
**Directory**: [`./DXF/`](./DXF/)
- **Best for**: 2D drawings, manufacturing documentation
- **Use cases**: CNC programming, sheet metal, laser cutting
- **Details**: See [`./DXF/README.md`](./DXF/README.md)

## Export Workflow

### 1. Model Preparation
- Verify model is complete and error-free
- Check for missing surfaces, gaps, or invalid geometry
- Ensure units are correct (mm or inches)
- Validate material properties
- Clean up construction geometry

### 2. Export Process
- Use CAD system's native export function
- Select appropriate neutral format
- Configure export options per format standards
- Include PMI/GD&T where supported (STEP AP242)
- Export assembly structure for assemblies

### 3. Validation
- Open exported file in neutral viewer or CAD system
- Verify geometry integrity
- Check assembly structure (if applicable)
- Validate PMI preservation (STEP AP242)
- Confirm file size is reasonable

### 4. Documentation
- Name files per naming convention
- Update metadata (part number, revision)
- Document export date and CAD system version
- Reference native source file

## Naming Convention

Use consistent naming across all export formats:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.<ext>
```

Examples:
- `53-10_FRAME-F01_PN-12345_RevB_20250110.step`
- `53-10_ASM_CENTER-BODY_PN-10000_RevA_20250110.jt`
- `53-10_SKIN-PANEL_PN-12346_RevA_20250110.igs`

## Directory Structure

```
EXPORTS/
├── STEP/          # Primary 3D exchange format
│   └── README.md
├── IGES/          # Legacy 3D format
│   └── README.md
├── JT/            # Lightweight visualization
│   └── README.md
└── DXF/           # 2D drawings and profiles
    └── README.md
```

## Export Requirements by File Type

### For Parts
Export each part to:
- **STEP**: Always (primary format)
- **IGES**: If required by partner/supplier
- **JT**: For visualization and large assembly performance
- **DXF**: 2D profiles if needed for sheet metal/machining

### For Assemblies
Export assemblies to:
- **STEP**: Complete assembly with structure
- **JT**: For lightweight reviews
- **IGES**: Only if specifically requested
- **DXF**: Not applicable (assemblies are 3D)

### For Drawings
Export 2D drawings to:
- **PDF**: Primary distribution format (see [`../DRAWINGS/`](../DRAWINGS/))
- **DXF**: 2D geometry for manufacturing

## Version Control

### File Management
- Commit all neutral format exports to Git
- Use Git LFS for files > 10 MB
- Tag major releases with version numbers
- Maintain export history for audit trail

### Synchronization
- Keep exports synchronized with native CAD files
- Re-export when native models are updated
- Document export date and CAD version
- Cross-reference native source files

## Quality Standards

### Export Validation Checklist
Before committing exported files:
- [ ] File opens in neutral viewer without errors
- [ ] Geometry matches source model
- [ ] Assembly structure preserved (if applicable)
- [ ] Units are correct
- [ ] PMI/GD&T transferred (STEP only)
- [ ] File size is reasonable (< 100 MB for parts)
- [ ] Naming convention followed
- [ ] Metadata complete

### Geometry Checks
- **Completeness**: All surfaces and solids present
- **Accuracy**: Within tolerance of native model
- **Topology**: No gaps, overlaps, or invalid edges
- **Units**: Millimeters or inches as specified
- **Orientation**: Proper coordinate system alignment

## Use Cases

### Design Review
- Export to **JT** for lightweight visualization
- Share with stakeholders without CAD licenses
- Enable markup and commenting
- Reduce file sizes for email/web distribution

### Manufacturing
- Export to **STEP** for CNC programming
- Provide **DXF** for 2D profiles and sheet metal
- Include **IGES** if supplier requires
- Ensure tolerance and PMI are transferred

### Supply Chain
- Distribute **STEP AP242** with PMI to suppliers
- Include material specifications in metadata
- Provide installation drawings as **PDF + DXF**
- Support supplier questions with neutral formats

### Archival
- Store **STEP AP242** for long-term preservation
- Follow ISO 10303 standard for data longevity
- Include metadata and documentation
- Verify readability every 5 years

## Best Practices

### Export Settings
- **STEP**: Use AP242 with PMI, assembly structure, and attributes
- **IGES**: Version 5.3, surfaces and solids, trimmed surfaces
- **JT**: Latest JT version, tessellated geometry, assembly structure
- **DXF**: 2D geometry, appropriate units, layer structure preserved

### Data Exchange
- Always provide **STEP AP242** as primary format
- Include **PDF drawings** with 3D exports
- Provide **material specifications** separately
- Document **design intent** in accompanying notes

### File Organization
- Group by component type (frames, skins, etc.)
- Maintain consistent naming across formats
- Cross-reference between formats
- Document export parameters used

## References

### Standards Documentation
- **ISO 10303-242**: STEP AP242 specification
- **ISO 14306**: JT format specification
- **IGES 5.3**: IGES format specification
- **DXF Reference**: AutoCAD DXF format guide

### Related Directories
- **Native models**: [`../MODELS/`](../MODELS/) and [`../ASSEMBLIES/`](../ASSEMBLIES/)
- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **Data exchange standards**: [`/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`](/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/)

### Tools
- **STEP viewers**: CAx-IF viewer, Jotne EDM Model Checker
- **JT viewers**: JT2Go (free from Siemens)
- **IGES viewers**: Various CAD systems
- **DXF viewers**: AutoCAD, DraftSight, LibreCAD

## Compliance

### Regulatory Requirements
- **FAA 14 CFR Part 21**: Type certificate data retention
- **EASA Part 21**: Design organization requirements
- **AS9100**: Quality management for aerospace
- **ITAR/EAR**: Export control compliance (if applicable)

### Retention Policy
- Retain neutral formats for **life of aircraft + 10 years**
- Archive per configuration management procedures
- Maintain traceability to native source files
- Document all format conversions and validations
