# EXPORTS — Neutral Format Exports for Simplified Models

## Purpose

This directory contains neutral format exports of simplified assembly configurations for data exchange, archival, and cross-platform interoperability.

## Overview

Neutral format exports of simplified models enable:
- **Lightweight distribution**: Smaller files for easier sharing
- **Visualization**: Views without CAD licenses
- **Long-term archival**: Format stability for data preservation
- **Cross-platform use**: Readable across different CAD systems
- **Design reviews**: Distributed review without native tools

## Supported Formats

### STEP (ISO 10303-242)
**Best for**: 3D geometry exchange, archival
- Simplified geometry with structure
- External interfaces preserved
- Mass properties included
- PMI included where applicable

### JT (ISO 14306)
**Best for**: Lightweight visualization, design reviews
- Optimized for large assembly performance
- Multiple LOD representations
- Embedded view states
- Ideal for presentations

### IGES (Initial Graphics Exchange)
**Best for**: Legacy system compatibility
- Surface and solid geometry
- Compatible with older CAD/CAM systems
- Use when STEP not supported

### STL (Stereolithography)
**Best for**: Visualization, 3D printing (mockups)
- Tessellated geometry only
- No assembly structure
- Very lightweight
- Use for visual mockups only

### 3D PDF
**Best for**: Document distribution, reviews
- Embedded 3D models
- Multiple views included
- Measurement tools available
- Annotations and markup

## Directory Structure

```
EXPORTS/
├── STEP/          # ISO 10303-242 exports
├── JT/            # ISO 14306 exports
├── IGES/          # Legacy 3D format
├── STL/           # Tessellated geometry
├── PDF/           # 3D PDF documents
└── README.md      # This file
```

## Naming Convention

Use consistent naming across all export formats:
```
53-10_ASM_<name>_SIMP_LOD<level>_<version>_<date>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMP_LOD1_v01_20250110.step`
- `53-10_ASM_FRAME-SECTION_SIMP_LOD2_v02_20250115.jt`
- `53-10_ASM_WING-ATTACH_SIMP_LOD3_v01_20250120.iges`

## Export Settings

### STEP (AP242) Settings
- **Protocol**: AP242 (3rd edition preferred)
- **Assembly structure**: Maintain hierarchy
- **Geometry**: Solid bodies
- **Attributes**: Include mass properties
- **PMI**: Include if present in simplified model
- **Units**: Millimeters

### JT Export Settings
- **Version**: Latest JT version
- **Geometry**: Tessellated with LOD
- **Structure**: Assembly hierarchy
- **Views**: Embed saved view states
- **Attributes**: Part names, mass properties
- **Optimization**: Optimize for visualization

### IGES Export Settings
- **Version**: IGES 5.3
- **Geometry**: Surfaces and solids
- **Trimmed surfaces**: Yes
- **Assembly**: Single file preferred
- **Units**: Millimeters

### STL Export Settings
- **Format**: Binary STL (more compact)
- **Resolution**: Medium (appropriate for visualization)
- **Units**: Millimeters
- **Coordinate system**: Match CAD model

### 3D PDF Settings
- **3D format**: U3D or PRC
- **Views**: Include multiple view states
- **Interactivity**: Enable rotation, zoom
- **Measurements**: Enable measurement tools
- **Annotations**: Include key dimensions

## Export Workflow

### 1. Model Preparation
- Verify simplified model is complete
- Check for geometric errors
- Validate mass properties
- Document simplification level

### 2. Export Process
- Use CAD system export function
- Select appropriate format
- Configure export settings
- Include metadata in file properties

### 3. Validation
- Open exported file in neutral viewer
- Verify geometry integrity
- Check assembly structure (if applicable)
- Validate file size reduction

### 4. Documentation
- Name file per convention
- Update metadata
- Document export date and settings
- Cross-reference to source model

## Use Cases by Format

### Design Reviews (JT or 3D PDF)
- Export to JT for CAD viewers
- Export to 3D PDF for general distribution
- Include saved view states
- Embed presentation views

### Manufacturing (STEP)
- Export to STEP AP242
- Include external interfaces
- Preserve dimensional accuracy
- Document simplification level

### Analysis (STEP or STL)
- Export to STEP for FEA preprocessing
- Export to STL for basic mesh generation
- Note: Simplified geometry may not be suitable for detailed analysis

### Visualization (JT or STL)
- Export to JT for lightweight viewing
- Export to STL for 3D rendering/mockups
- Optimize for display performance

### Archival (STEP)
- Export to STEP AP242
- Include complete metadata
- Document simplification applied
- Reference detailed baseline

## Quality Requirements

### Export Validation Checklist
Before distributing exported files:
- [ ] File opens without errors in neutral viewer
- [ ] Geometry matches simplified source
- [ ] Assembly structure preserved (if applicable)
- [ ] External interfaces correct
- [ ] File size appropriate for LOD level
- [ ] Naming convention followed
- [ ] Metadata complete
- [ ] Documentation updated

### Geometry Checks
- **Completeness**: All intended geometry present
- **Accuracy**: Within tolerance of source
- **Interfaces**: External interfaces unchanged
- **Units**: Correct units (mm)
- **Orientation**: Proper coordinate system

## Performance Targets

### File Size Reduction
- **LOD1**: 90-95% reduction vs. detailed model
- **LOD2**: 70-85% reduction vs. detailed model
- **LOD3**: 40-60% reduction vs. detailed model

### Load Time Improvement
- **LOD1-2**: Load in < 5 seconds
- **LOD3**: Load in < 10 seconds
- Target: 50-80% faster than detailed model

## Version Control

### File Management
- Commit all exports to Git
- Use Git LFS for files > 10 MB
- Tag with model version
- Maintain export history

### Synchronization
- Re-export when simplified model changes
- Update metadata with each export
- Cross-reference to source model version
- Document export settings used

## Documentation Requirements

For each export, document:
- **Source model**: Simplified assembly version
- **Export date**: When exported
- **Export settings**: Settings used
- **CAD system**: Tool and version
- **File size**: Before and after
- **Validation**: Quality checks performed

## Related Directories

- **Source models**: [`../ASM/`](../ASM/) — Simplified assemblies
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/) — Views for export
- **Documentation**: [`../DOCS/`](../DOCS/) — Export documentation
- **Detailed exports**: [`../../../EXPORTS/`](../../../EXPORTS/) — Full detail exports

## Tools and Viewers

### STEP Viewers
- CAx-IF Viewer (free)
- Jotne EDM Model Checker
- FreeCAD (open source)

### JT Viewers
- JT2Go (free from Siemens)
- Teamcenter Visualization

### 3D PDF Viewers
- Adobe Acrobat Reader (free)
- Web browsers (limited support)

### STL Viewers
- MeshLab (open source)
- 3D Builder (Windows)
- Various online viewers
