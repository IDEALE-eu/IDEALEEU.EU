# SUB_ASSEMBLIES — Component Sub-Assemblies

## Purpose

JT files for sub-assemblies of the center body structure. These represent major sections or systems within the complete assembly.

## What to Store

- Frame section assemblies
- Skin panel assemblies
- Stringer sections
- Interface assemblies
- Major structural sections

## Typical Sub-Assemblies

- **Frame sections**: Multiple frames with stringers and skin
- **Zone assemblies**: Forward, center, aft sections
- **System assemblies**: Floor structures, cargo sections
- **Interface assemblies**: Wing attach, door frames

## Usage

Use sub-assemblies for:
- Section-level design reviews
- Work package definition
- Supplier coordination
- Manufacturing planning
- Detailed integration studies

## File Characteristics

- **Complexity**: Moderate (10-100 components)
- **File size**: Medium (1-20 MB)
- **Component count**: Manageable subset
- **Hierarchy depth**: 2-4 levels typically

## Related Directories

- [`../TOP_LEVEL/`](../TOP_LEVEL/) — Complete assembly
- [`../../PARTS/`](../../PARTS/) — Individual components
- [`../../ZONES/`](../../ZONES/) — Zone-based organization
- [`../`](../) — ASSEMBLIES directory
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Define logical sub-assembly boundaries
- Maintain consistent naming conventions
- Use for work breakdown structure alignment
- Coordinate with manufacturing sequences
- Include relevant fasteners and details
