# EXPORTS — Neutral Format Exports

## Purpose

This directory contains neutral format exports of lightweight assembly configurations for sharing with external stakeholders, suppliers, and partners.

## Contents

### Export Formats
- **STEP**: ISO 10303 standard format (primary)
- **IGES**: Legacy 3D format for compatibility
- **JT**: Lightweight visualization format
- **STL**: Tessellated format for rapid prototyping
- **3D PDF**: Interactive 3D documents

## Naming Convention

Use the following pattern:
```
53-10_EXP_<assembly-name>_LW_<version>.<ext>
```

Examples:
- `53-10_EXP_CENTER-BODY_LW_v01.step`
- `53-10_EXP_FRAME-SECTION_LW_v02.iges`
- `53-10_EXP_SKIN-PANEL_LW_v01.jt`

## Export Standards

### STEP (ISO 10303)
- **Protocol**: AP242 (preferred) or AP214
- **Content**: Geometry, assembly structure, metadata
- **Settings**: Tessellated or B-rep geometry
- **Use case**: Primary exchange format

### IGES (Initial Graphics Exchange Specification)
- **Version**: 5.3 (minimum)
- **Content**: Surfaces and solids
- **Settings**: Trimmed surfaces, layer structure
- **Use case**: Legacy system compatibility

### JT (Jupiter Tessellation)
- **Version**: Latest (JT 9.5+)
- **Content**: Tessellated geometry, assembly tree
- **Settings**: Optimized for visualization
- **Use case**: Lightweight review and collaboration

### STL (Stereolithography)
- **Format**: Binary (preferred) or ASCII
- **Quality**: Medium tessellation (balance size/quality)
- **Units**: Millimeters
- **Use case**: 3D printing, rapid prototyping

## Export Settings

### Geometry Quality
- **High**: For manufacturing and detailed review
- **Medium**: For general collaboration (default)
- **Low**: For quick sharing and visualization

### Content Selection
- **Full assembly**: Complete structure with all components
- **Simplified**: Major components only (fasteners excluded)
- **Envelope**: Outer geometry only (internal details suppressed)

### Metadata Inclusion
- Part numbers and names
- Material specifications
- Mass properties
- Coordinate system definitions

## Export Workflow

1. **Prepare Model**
   - Apply lightweight configuration
   - Verify suppression states
   - Check for errors/warnings

2. **Configure Export**
   - Select appropriate format
   - Set quality/tessellation level
   - Include relevant metadata

3. **Execute Export**
   - Export to neutral format
   - Verify file integrity
   - Document export settings

4. **Validate Export**
   - Open in neutral viewer
   - Verify geometry accuracy
   - Check assembly structure
   - Confirm metadata

5. **Distribute**
   - Compress if needed (ZIP)
   - Share via secure channel
   - Provide accompanying documentation

## Quality Assurance

Exported files must:
- Open without errors in target system
- Preserve assembly structure and hierarchy
- Maintain geometric accuracy (±0.1 mm)
- Include required metadata
- Be within acceptable file size limits

## Use Cases

### Supplier Collaboration
- Share design intent with manufacturers
- Provide reference geometry for tooling
- Support supplier quotes and feasibility

### Design Review
- Enable stakeholder review without CAD licenses
- Support markup and commenting
- Facilitate remote collaboration

### Documentation
- Include in technical publications
- Archive for long-term preservation
- Support regulatory compliance

## File Size Guidelines

Target file sizes for lightweight exports:
- **STEP**: 50-70% of native file size
- **IGES**: 40-60% of native file size
- **JT**: 10-20% of native file size
- **STL**: 20-40% of native file size

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Part files**: [`../PARTS/`](../PARTS/)
- **Full detail exports**: [`../../EXPORTS/`](../../EXPORTS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
