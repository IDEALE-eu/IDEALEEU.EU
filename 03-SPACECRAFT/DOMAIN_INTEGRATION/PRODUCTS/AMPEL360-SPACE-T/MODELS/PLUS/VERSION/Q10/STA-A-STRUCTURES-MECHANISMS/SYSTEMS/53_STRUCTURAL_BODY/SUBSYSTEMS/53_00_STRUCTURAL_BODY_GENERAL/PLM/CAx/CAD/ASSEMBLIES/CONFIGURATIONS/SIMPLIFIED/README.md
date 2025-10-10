# SIMPLIFIED — Simplified Assembly Configurations

## Purpose

This directory contains simplified assembly configurations with reduced geometric complexity for design reviews, analysis, and performance optimization of spacecraft structural body designs.

## Contents

### Simplified Model Types
- **Envelope models**: Simplified bounding geometry
- **Schematic representations**: Functional layouts without full detail
- **Analysis-ready models**: Pre-simplified for FEA/CFD
- **Review models**: Appropriate detail level for stakeholder reviews

## Simplification Techniques

### Geometry Reduction
- Remove small features (fillets, chamfers)
- Replace complex shapes with simple primitives
- Merge multiple parts into single bodies
- Simplify curved surfaces to faceted approximations

### Part Suppression
- Hide fasteners and small hardware
- Suppress internal details
- Remove cosmetic features
- Hide non-critical components

### Assembly Simplification
- Replace sub-assemblies with single parts
- Use simplified component representations
- Reduce part count
- Consolidate similar parts

## Naming Convention

Use the following pattern:
```
53_00_ASM_<assembly-name>_SIMP_<version>.<ext>
```

Examples:
- `53_00_ASM_STRUCTURAL-BODY_SIMP_v01.CATProduct`
- `53_00_ASM_FRAME-SECTION_SIMP_v02.asm`
- `53_00_ASM_INTERFACE_SIMP_v01.sldasm`

## Use Cases

### Analysis Preparation
- Pre-simplified for FEA meshing
- Reduced complexity for CFD
- Appropriate detail for thermal analysis
- Optimized for load case studies

### Design Reviews
- Focus on critical features
- Reduce visual clutter
- Faster model loading
- Better presentation clarity

### Integration Studies
- System-level fit checks
- Interface verification
- Mass property estimates
- Envelope validation

## Simplification Guidelines

### Preserve
- Overall dimensions and envelope
- Critical interfaces and mounting points
- Mass properties (within ±10%)
- Coordinate system alignment
- Major structural features

### Remove/Simplify
- Fillets and rounds < 5mm
- Chamfers < 2mm
- Fasteners and small hardware
- Surface textures and finishes
- Cosmetic details

## Quality Assurance

Simplified models must:
- Maintain external interfaces exactly
- Preserve overall dimensions
- Document simplifications applied
- Validate mass properties
- Verify interference clearances

## Related Directories

- **Lightweight models**: [`../LIGHTWEIGHT/`](../LIGHTWEIGHT/)
- **Full assemblies**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **Analysis models**: [`../../../../CAE/`](../../../../CAE/)
