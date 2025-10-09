# ASSEMBLY — Assembly Templates

## Purpose

This directory contains assembly templates with pre-configured skeleton structures, reference geometry, and standard constraints for the 53-10 Center Body assemblies.

## Contents

### Assembly Template Types
- **Top-level assemblies**: Complete center body assemblies
- **Sub-assemblies**: Frame sections, skin panel assemblies
- **Detail assemblies**: Interface assemblies, installation assemblies

## Template Files

Standard assembly templates should include:
- Master reference geometry (FS, BL, WL stations)
- Skeleton structure (layout curves and surfaces)
- Standard coordinate systems
- Constraint definitions and mate types
- Level of detail (LOD) configurations
- Bill of Materials (BOM) structure template
- Standard components (fasteners, bushings, hardware)

## Naming Convention

```
ASM_<assembly-level>_<description>_<variant>.<ext>
```

Examples:
- `ASM_TopLevel_CenterBody_Complete.CATProduct`
- `ASM_SubAssy_FrameSection_F01-F05.asm`
- `ASM_Detail_WingInterface.sldasm`
- `ASM_Section_SkinPanel_SP-001.asm`

## Usage Guidelines

### Starting a New Assembly
1. Select appropriate assembly template based on assembly level
2. Save as new file with proper naming convention (see `../NAMING_CONVENTIONS/`)
3. Insert reference geometry (skeleton) as needed
4. Add components using standard mates/constraints
5. Maintain product structure conventions per `../BOM/`
6. Document assembly intent in properties

### Assembly Organization
- **By assembly level**: Top-level, sub-assembly, detail
- **By zone**: Forward, center, aft sections
- **By system interface**: Wing interface, door interface, floor interface

### Best Practices
- Always use skeleton/master model approach
- Maintain reference geometry throughout assembly hierarchy
- Use standard constraint types consistently
- Document assembly sequence and critical constraints
- Set up appropriate display states/LODs for large assemblies

## Related Directories

- **BOM**: [`../BOM/`](../BOM/) — Bill of Materials structure
- **Parameters**: [`../PARAMETERS/`](../PARAMETERS/) — Assembly parameter standards
- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Assembly metadata fields
- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — File naming rules

## References

- Main templates documentation: [`../README.md`](../README.md)
- Assembly best practices: [`../../ASSEMBLIES/README.md`](../../ASSEMBLIES/README.md)
- Interface requirements: [`../../../../INTERFACE_MATRIX/`](../../../../INTERFACE_MATRIX/)
- Product structure standards: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
