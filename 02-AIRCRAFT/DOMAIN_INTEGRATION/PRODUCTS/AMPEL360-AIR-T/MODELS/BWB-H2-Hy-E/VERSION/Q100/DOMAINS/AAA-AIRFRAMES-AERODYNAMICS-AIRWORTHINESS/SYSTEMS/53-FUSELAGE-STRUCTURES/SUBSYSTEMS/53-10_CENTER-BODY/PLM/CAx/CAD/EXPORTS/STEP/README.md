# STEP — ISO 10303 (AP242) Exports

## Purpose

This directory contains STEP (Standard for the Exchange of Product Model Data) file exports following the ISO 10303-242 Application Protocol (AP242) for managed model-based 3D engineering.

## Overview

**STEP AP242** is the primary neutral format for aerospace CAD data exchange:
- **Vendor-neutral**: Readable by all major CAD systems
- **Comprehensive**: Geometry + PMI + assembly structure + metadata
- **Long-term archival**: Designed for decades of data preservation
- **Industry standard**: Mandated by aerospace OEMs and regulatory agencies

## What to Store

### Part Files
- **Solid models**: 3D parametric parts exported as B-rep solids
- **Surface models**: Complex surfaces, lofts, and class-A surfaces
- **Geometry types**: Solids, surfaces, wireframe, curves
- **PMI data**: Geometric Dimensioning and Tolerancing (GD&T)
- **Attributes**: Material, mass, properties, metadata

### Assembly Files
- **Product structure**: Hierarchical assembly tree
- **Instances**: Part occurrences with placement transformations
- **Assembly features**: Holes, cuts across multiple parts
- **Configuration**: Variants and options
- **Metadata**: BOM data, effectivity, attributes

### Capabilities Included in AP242
- ✅ 3D geometry (solids, surfaces, wireframe)
- ✅ Product structure (assemblies, sub-assemblies)
- ✅ PMI (Product and Manufacturing Information)
- ✅ GD&T (Geometric Dimensioning and Tolerancing)
- ✅ Material specifications
- ✅ Surface finish requirements
- ✅ Configuration management data
- ✅ Design history and parametrics (if exported)
- ✅ Annotations and notes

## File Format

### File Extension
- `.step` or `.stp` (both acceptable)
- Use lowercase for consistency: `.step`

### File Structure
STEP files are human-readable ASCII text:
```
ISO-10303-21;
HEADER;
FILE_DESCRIPTION(...);
FILE_NAME(...);
FILE_SCHEMA(...);
ENDSEC;
DATA;
#1=PRODUCT(...);
#2=PRODUCT_DEFINITION(...);
...
ENDSEC;
END-ISO-10303-21;
```

## Naming Convention

Use the following naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.step
```

Examples:
- `53-10_FRAME-F01_PN-12345_RevB_20250110.step`
- `53-10_ASM_CENTER-BODY_PN-10000_RevA_20250110.step`
- `53-10_SKIN-PANEL_PN-12346_RevA_20250110.step`

## Export Settings

### Recommended Export Options
When exporting from CAD systems, configure:

**Geometry**:
- ☑ Solid bodies and surfaces
- ☑ B-rep (boundary representation)
- ☑ Trimmed surfaces
- ☑ Exact geometry (not tessellated)
- ☑ All visible layers/bodies

**PMI (Product and Manufacturing Information)**:
- ☑ Dimensions
- ☑ Tolerances
- ☑ GD&T (datums, feature control frames)
- ☑ Surface finish symbols
- ☑ Notes and annotations

**Assembly Structure** (for assemblies):
- ☑ Product structure hierarchy
- ☑ Part instances with transformations
- ☑ Component names and IDs
- ☑ Assembly constraints (optional)

**Attributes**:
- ☑ Part number
- ☑ Revision/version
- ☑ Material
- ☑ Mass properties
- ☑ Author and date
- ☑ Custom properties

**Protocol**:
- **Application Protocol**: AP242
- **Schema**: managed_model_based_3d_engineering_ed2_mim_lf (or latest)

### CAD System-Specific Settings

#### CATIA V5/V6
- File → Export → STEP
- Format: `AP242`
- Options: Check "Export PMI", "Assembly structure", "Attributes"

#### Siemens NX
- File → Export → STEP
- Application Protocol: `AP242`
- Options: "Export PMI", "Product structure", "Attributes"

#### SolidWorks
- File → Save As → STEP
- Options → Output as: `STEP AP242`
- Include: Geometry + PMI

#### Creo (PTC)
- File → Save a Copy → STEP
- Configuration: AP242
- Include: Geometry, annotations, assembly structure

## Validation

### Opening and Checking STEP Files
Use STEP validation tools:
- **CAx-IF Recommended Practices**: Industry validation guidelines
- **Jotne EDM Model Checker**: Commercial STEP validator
- **STEP File Analyzer**: Free tool from NIST
- **CAD system import**: Test import into different CAD system

### Validation Checklist
Before committing STEP files:
- [ ] File opens without errors in STEP viewer
- [ ] All geometry imported correctly
- [ ] Assembly structure preserved (if assembly)
- [ ] PMI/GD&T visible and complete
- [ ] Material properties present
- [ ] Units are correct (mm or inches)
- [ ] File size reasonable (< 100 MB for parts, < 1 GB for assemblies)
- [ ] Metadata complete (part number, revision, etc.)

### Geometry Checks
- **Completeness**: All surfaces and solids present
- **Accuracy**: Within 0.001 mm of source model
- **Topology**: No invalid edges, gaps, or self-intersecting surfaces
- **Orientation**: Coordinate system aligned with aircraft reference frame

### PMI Checks
- **Datums**: All datums defined and visible
- **GD&T**: Feature control frames complete
- **Dimensions**: Critical dimensions present
- **Notes**: Important manufacturing notes included
- **Surface finish**: Roughness symbols present

## Use Cases

### Primary Exchange Format
STEP AP242 is the **primary format** for:
- Design data exchange with partners
- Supply chain distribution to manufacturers
- Regulatory submissions (FAA, EASA)
- Long-term data archival
- Cross-platform collaboration

### Manufacturing Handoff
Provide to suppliers:
- STEP files with geometry + PMI
- PDF drawings as reference
- Material specifications
- Quality requirements

### Analysis and Simulation
- Import into FEA tools (Nastran, Abaqus, Ansys)
- Import into CFD tools (Fluent, Star-CCM+)
- Mesh generation from STEP geometry
- Geometry simplification for analysis

### Documentation
- Include in technical data packages (TDP)
- Archive with engineering drawings
- Submit with type certificate applications
- Maintain for configuration control

## Best Practices

### Export Quality
- Start from clean, validated CAD models
- Remove construction geometry before export
- Simplify very complex surfaces if needed
- Include PMI for all critical features
- Test export in neutral viewer before distribution

### Metadata
Include comprehensive metadata:
- **Part number**: Unique identifier
- **Revision**: Current revision letter/number
- **Material**: Material specification code
- **Mass**: Calculated mass in kg
- **Author**: Designer/engineer name
- **Date**: Export date
- **Source file**: Native CAD filename
- **CAD system**: Tool and version used

### File Organization
- Group by component type (frames, skins, etc.)
- Use consistent naming convention
- Maintain version history
- Cross-reference to native source files

### Version Control
- Commit STEP files to Git repository
- Use Git LFS for large files (> 10 MB)
- Tag releases with version identifiers
- Document major geometry changes in commit messages

## File Size Considerations

### Typical File Sizes
- **Simple parts**: 100 KB - 5 MB
- **Complex parts**: 5 MB - 50 MB
- **Sub-assemblies**: 10 MB - 100 MB
- **Large assemblies**: 100 MB - 1 GB+

### Reducing File Size
If STEP files are too large:
- Remove unnecessary details (fillets, chamfers)
- Simplify complex surfaces
- Export sub-assemblies separately
- Use JT format for visualization instead
- Compress with ZIP before distribution (not for Git)

## Standards and References

### ISO Standards
- **ISO 10303-242**: Application Protocol 242 (AP242)
- **ISO 10303-21**: Clear text encoding (STEP-File)
- **ISO 10303-238**: Integrated CNC (STEP-NC)

### Industry Guidelines
- **CAx-IF Recommended Practices**: Implementation guidelines
- **PDES Inc.**: Standards development organization
- **LOTAR**: Long-Term Archiving and Retrieval standards

### Aerospace Standards
- **AS9100**: Quality management
- **ATA iSpec 2200**: Technical publications
- **FAA AC 21-45**: Digital data approval
- **EASA Part 21**: Design organization requirements

## Troubleshooting

### Common Issues

**Missing PMI**:
- Verify PMI export option enabled
- Check CAD system supports AP242 PMI
- Confirm annotations are in model (not drawing-only)

**Assembly Structure Lost**:
- Export as assembly, not individual parts
- Enable "Product structure" option
- Use AP242 (not AP203 or AP214)

**Large File Size**:
- Simplify geometry if possible
- Export sub-assemblies separately
- Consider JT for visualization
- Check for duplicate geometry

**Import Errors**:
- Validate with STEP checker tool
- Test in multiple CAD systems
- Check for non-manifold geometry in source
- Ensure units are consistent

## Related Directories

- **Source models**: [`../../MODELS/`](../../MODELS/) and [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Other formats**: [`../IGES/`](../IGES/), [`../JT/`](../JT/), [`../DXF/`](../DXF/)
- **Drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
- **Standards**: [`/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`](/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/)

## Tools and Software

### STEP Viewers (Free)
- **CAx-IF Viewer**: Basic STEP viewer
- **FreeCAD**: Open-source CAD with STEP import
- **STP Viewer**: Lightweight STEP viewer

### STEP Validators (Commercial)
- **Jotne EDM Model Checker**: Comprehensive validator
- **Theorem Solutions**: CADverter with validation
- **TransMagic**: Multi-format translator and validator

### CAD Systems with STEP Support
- CATIA V5/V6 (Dassault Systèmes)
- Siemens NX
- SolidWorks
- Creo (PTC)
- Inventor (Autodesk)
- Solid Edge (Siemens)

## Compliance and Archival

### Regulatory Compliance
STEP AP242 files satisfy:
- FAA type certificate data requirements
- EASA design organization data retention
- AS9100 quality documentation
- ITAR technical data (with proper controls)

### Archival Duration
Retain STEP files for:
- **Minimum**: Life of aircraft type certificate
- **Recommended**: Life + 10 years
- **Long-term**: Permanent archival for historical aircraft

### Verification
Periodically (every 5 years):
- Verify files still readable
- Test import into current CAD systems
- Regenerate if format versions deprecated
- Document validation results
