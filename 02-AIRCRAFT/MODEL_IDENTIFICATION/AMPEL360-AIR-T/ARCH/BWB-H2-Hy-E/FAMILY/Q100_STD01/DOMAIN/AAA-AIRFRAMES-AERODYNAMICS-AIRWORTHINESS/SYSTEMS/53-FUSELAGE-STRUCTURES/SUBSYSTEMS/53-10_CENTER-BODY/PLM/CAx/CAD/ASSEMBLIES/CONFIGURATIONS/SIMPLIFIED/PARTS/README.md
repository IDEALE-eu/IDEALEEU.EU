# PARTS — Simplified Component Parts

## Purpose

This directory contains simplified component part models that are used in simplified assembly configurations.

## Contents

### Simplified Part Types
- **Envelope parts**: Outer boundary representations
- **Proxy parts**: Simplified placeholders for complex components
- **Reduced detail parts**: Parts with features removed or simplified
- **Reference parts**: Boundary and interface representations

## Simplification Methods

### Geometry Reduction
- Remove internal features (fillets, chamfers, small holes)
- Combine multiple features into single bodies
- Replace complex surfaces with simple approximations
- Remove non-visible internal components

### Feature Suppression
- Suppress non-critical features
- Remove fastener details
- Simplify surface finishes
- Eliminate construction geometry

### Mass Properties
- Maintain accurate mass and center of gravity
- Preserve moment of inertia if required
- Document simplifications in part properties

## Naming Convention

Use the following pattern:
```
53-10_PRT_<part-name>_SIMP_LOD<level>_<version>.<ext>
```

Examples:
- `53-10_PRT_FRAME-F01_SIMP_LOD1_v01.CATPart`
- `53-10_PRT_SKIN-PANEL_SIMP_LOD2_v02.prt`
- `53-10_PRT_STRINGER_SIMP_LOD3_v01.sldprt`

## File Formats

### Native CAD Formats
- **CATIA**: `.CATPart`
- **NX**: `.prt`
- **SolidWorks**: `.sldprt`
- **Creo**: `.prt`

## Organization

Organize parts by:
- Component type (frames, stringers, skins, etc.)
- Level of detail (LOD1-LOD4)
- Version number

## Part Requirements

Simplified parts must:
- Maintain external interfaces unchanged
- Preserve mounting points and datums
- Reference detailed baseline part
- Document simplification level
- Include appropriate metadata

## Metadata

Each simplified part should include:
- **Part number**: Reference to detailed part
- **Simplification level**: LOD1-LOD4
- **Mass**: Actual or representative mass
- **Material**: Material specification
- **Baseline reference**: Link to detailed model
- **Limitations**: Usage restrictions

## Version Control

- Commit all part files to Git
- Use Git LFS for large files (> 10 MB)
- Tag major simplification revisions
- Maintain traceability to detailed parts

## Quality Requirements

Simplified parts must:
- Be validated for intended use
- Maintain dimensional accuracy for interfaces
- Document any deviations from baseline
- Pass geometry validation checks

## Related Directories

- **Assemblies**: [`../ASM/`](../ASM/) — Simplified assembly models
- **Documentation**: [`../DOCS/`](../DOCS/) — Part documentation
- **Exports**: [`../EXPORTS/`](../EXPORTS/) — Neutral format exports
- **Detailed parts**: [`../../../MODELS/`](../../../MODELS/) — Baseline detailed parts
