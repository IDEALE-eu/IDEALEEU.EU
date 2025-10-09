# SUB_ASSEMBLIES — Sub-Assembly Models

## Purpose

This directory contains sub-assembly models that combine multiple components into intermediate structural assemblies for the 53-10 Center Body.

## Contents

### Sub-Assembly Types
- **Frame sections**: Frame + stringer + skin panel assemblies
- **Structural zones**: Forward, center, and aft center body sections
- **Component groups**: Related parts assembled together
- **Panel assemblies**: Skin panel with stringers and frames

## Example Sub-Assembly

```
53-10_ASM_FRAME-SECTION_F05
├── Frame F05
├── Stringers (4x)
├── Skin panels (2x)
└── Fasteners (clips, rivets)
```

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-type>_<identifier>_<version>.<ext>
```

Examples:
- `53-10_ASM_FRAME-SECTION_F01-F05_v01.CATProduct`
- `53-10_ASM_SKIN-PANEL_SP-001_v02.asm`
- `53-10_ASM_STRINGER-GROUP_L-UPPER_v01.sldasm`

## Organization

Organize sub-assemblies by:
- **Zone**: Forward, center, aft sections
- **Component type**: Frames, stringers, skin panels
- **Assembly level**: Detail vs. intermediate sub-assemblies

## Assembly Guidelines

Sub-assemblies should:
- Be reusable in top-level assemblies
- Have well-defined interfaces
- Include complete fastener schedules
- Document assembly sequence
- Maintain individual BOM

## Related Directories

- **Top-level**: [`../TOP_LEVEL/`](../TOP_LEVEL/)
- **Component models**: [`../../MODELS/`](../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
