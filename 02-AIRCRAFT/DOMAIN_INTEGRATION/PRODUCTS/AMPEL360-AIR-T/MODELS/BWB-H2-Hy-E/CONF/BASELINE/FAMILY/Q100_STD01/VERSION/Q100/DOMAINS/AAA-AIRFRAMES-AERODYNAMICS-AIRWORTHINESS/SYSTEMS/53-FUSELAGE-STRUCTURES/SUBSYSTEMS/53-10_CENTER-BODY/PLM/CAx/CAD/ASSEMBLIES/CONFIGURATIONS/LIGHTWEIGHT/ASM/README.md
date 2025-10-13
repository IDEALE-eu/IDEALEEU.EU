# ASM — Assembly Files

## Purpose

This directory contains lightweight assembly files (.asm, .CATProduct, .sldasm, etc.) optimized for performance and reduced file size.

## Contents

### File Types
- **Native assembly files**: Lightweight versions of assemblies
- **Sub-assembly files**: Component assemblies with optimizations applied
- **Configuration files**: Assembly-specific settings and parameters

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-name>_LW_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_LW_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_LW_v02.asm`
- `53-10_ASM_SKIN-PANEL_LW_v01.sldasm`

## Organization

Files are organized by:
- Assembly hierarchy level (top-level, sub-assemblies)
- Component type (frames, stringers, panels)
- Version and revision

## Optimization Applied

Lightweight assemblies include:
- Suppressed non-essential features
- Simplified display representations
- Reduced tessellation quality
- Deferred sub-assembly loading

## Related Directories

- **Part files**: [`../PARTS/`](../PARTS/)
- **Suppression rules**: [`../SUPPRESSION/`](../SUPPRESSION/)
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/)
- **Documentation**: [`../DOCS/`](../DOCS/)
