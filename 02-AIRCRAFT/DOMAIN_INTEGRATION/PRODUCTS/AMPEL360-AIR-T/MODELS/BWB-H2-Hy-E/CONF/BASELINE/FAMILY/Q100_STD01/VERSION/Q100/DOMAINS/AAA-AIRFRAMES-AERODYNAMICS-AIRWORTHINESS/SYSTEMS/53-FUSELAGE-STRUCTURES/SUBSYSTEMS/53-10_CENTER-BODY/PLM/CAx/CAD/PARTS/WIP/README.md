# WIP — Work in Progress

## Purpose

This directory contains CAD part files that are under active development and have not yet been released for production. Parts in WIP are subject to design changes and should not be used for manufacturing or procurement.

## Usage

### For Designers
- Store all new part designs here during development
- Iterate freely without release approval
- Collaborate with other designers on evolving concepts
- Move parts to [`../RELEASED/`](../RELEASED/) only after formal release process

### Design Status
Parts in this directory are:
- **Draft**: Initial concept or preliminary design
- **In Review**: Under design review or approval process
- **Pending ECO**: Awaiting Engineering Change Order approval

## File Organization

Organize WIP parts by:
- Component type (use subdirectories if needed)
- Designer name or work package
- Target release milestone

## Transition to Released

Before moving parts to RELEASED/:
1. Complete design review (PDR/CDR as applicable)
2. Verify all metadata is complete
3. Create engineering drawing if required
4. Obtain ECO approval
5. Export to neutral formats (STEP)
6. Update configuration management system

## Cleanup Policy

- Review WIP directory quarterly
- Archive abandoned designs to personal backup
- Delete superseded iterations after new version released
- Maintain WIP directory organization

## Naming Convention

Use standard part naming with `_WIP` suffix if needed:
```
53-10_<component>_<part-number>_<description>_WIP_<version>.<ext>
```

Example:
- `53-10_FRAME_F15_WIP_v03.CATPart`

## Cross-References

- **Released parts**: [`../RELEASED/`](../RELEASED/)
- **Obsolete parts**: [`../OBSOLETE/`](../OBSOLETE/)
- **Component directories**: See parent [`../README.md`](../README.md)
