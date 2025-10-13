# ASM — Simplified Assembly Files

## Purpose

This directory contains simplified assembly model files with reduced detail for design reviews, presentations, and preliminary analysis.

## Contents

### Assembly Model Files
Store native CAD assembly files for simplified configurations:
- **CATIA**: `.CATProduct` files
- **NX**: `.prt` assembly files
- **SolidWorks**: `.sldasm` files
- **Creo**: `.asm` files

### Simplified Assembly Types
- **LOD1**: Envelope only (outer boundary)
- **LOD2**: Major components simplified
- **LOD3**: Moderate detail for review
- **LOD4**: Full detail (reference only)

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-name>_SIMP_LOD<level>_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMP_LOD1_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_SIMP_LOD2_v02.asm`
- `53-10_ASM_WING-ATTACH_SIMP_LOD3_v01.sldasm`

## File Organization

Organize files by:
- Level of detail (LOD1-LOD4)
- Assembly type (complete, section, zone)
- Version number

## Assembly Requirements

Simplified assemblies should:
- Maintain external interfaces
- Preserve overall dimensions
- Reference baseline detailed assembly
- Document simplifications applied
- Include metadata in file properties

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design review versions
- Document configuration changes
- Maintain traceability to detailed models

## Related Directories

- **Parts**: [`../PARTS/`](../PARTS/) — Simplified component parts
- **Documentation**: [`../DOCS/`](../DOCS/) — Assembly documentation
- **Exports**: [`../EXPORTS/`](../EXPORTS/) — Neutral format exports
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/) — Saved display configurations
