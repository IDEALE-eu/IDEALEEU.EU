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

Sub-assemblies are organized by structural type and function:

### Primary Structure Modules
- **[FRAME_SECTIONS/](./FRAME_SECTIONS/)** — Frame section assemblies (frames with stringers and skin)
  - **FXX/** — Individual frame station assemblies (F01, F05, F10, etc.)
- **[STRINGER_BAYS/](./STRINGER_BAYS/)** — Longitudinal stringer bay assemblies
  - **LXX/** — Individual stringer runs (L01, R01, C01, etc.)
- **[SKIN_PANEL_MODULES/](./SKIN_PANEL_MODULES/)** — Skin panel assemblies with reinforcements
  - **PXX/** — Individual panel modules (P01, P15, P25, etc.)

### Secondary Structure Modules
- **[FLOOR_MODULES/](./FLOOR_MODULES/)** — Floor beam and panel assemblies
  - **BAY_XX/** — Floor modules by bay (BAY_01, BAY_05, etc.)
- **[BULKHEAD_MODULES/](./BULKHEAD_MODULES/)** — Bulkhead assemblies
  - **BH_XX/** — Individual bulkheads (BH_01, BH_05, etc.)

### Interface and Special Assemblies
- **[INTERFACE_GROUPS/](./INTERFACE_GROUPS/)** — Major interface assemblies
  - **WING_INTERFACE/** — Wing-to-body joint assemblies
  - **NOSE_INTERFACE/** — Forward section connection assemblies
  - **AFT_INTERFACE/** — Aft section connection assemblies
- **[DOOR_SURROUNDS/](./DOOR_SURROUNDS/)** — Door frame and surround assemblies
- **[WINDOW_BAYS/](./WINDOW_BAYS/)** — Window installation assemblies
- **[MOUNTING_UNITS/](./MOUNTING_UNITS/)** — Equipment mounting bracket assemblies
- **[TANK_SUPPORT_MODULES/](./TANK_SUPPORT_MODULES/)** — Fuel tank support structure assemblies

### Assembly Support
- **[FASTENER_SETS/](./FASTENER_SETS/)** — Fastener schedules and sets by assembly
- **[JIG_READY/](./JIG_READY/)** — Jig-ready assembly configurations

### Documentation and Management
- **[DOCS/](./DOCS/)** — Sub-assembly documentation
  - **[BOM/](./DOCS/BOM/)** — Bills of materials for sub-assemblies
  - **[SEQUENCE/](./DOCS/SEQUENCE/)** — Assembly sequence procedures
  - **[CHECKS/](./DOCS/CHECKS/)** — Inspection and verification procedures
- **[REVISIONS/](./REVISIONS/)** — Revision management
  - **[DRAFT/](./REVISIONS/DRAFT/)** — Work-in-progress assemblies
  - **[RELEASED/](./REVISIONS/RELEASED/)** — Released production assemblies
  - **[OBSOLETE/](./REVISIONS/OBSOLETE/)** — Superseded or retired assemblies
- **[TEMPLATES/](./TEMPLATES/)** — Reusable assembly templates and standards
- **[INDEX/](./INDEX/)** — Index files and cross-references

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
