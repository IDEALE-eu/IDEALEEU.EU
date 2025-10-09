# SUBCOMPONENTS — Sub-Assembly Models

## Purpose

This directory contains CAD models for sub-assemblies that combine multiple individual parts into functional structural units. These are intermediate assemblies between individual parts and the final center body assembly.

## Organization

Subcomponents are organized by functional area:

- **DOOR_SURROUNDS/** — Door frame structures and reinforcements
- **WINDOW_BAYS/** — Window frame assemblies and pressure rings
- **ACCESS_PANELS/** — Access door assemblies and attach provisions

## Naming Convention

Use the following pattern for subcomponent assemblies:
```
53-10_<SUBCOMP>_<ASSY-ID>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_DOOR_SURR_DS-001_MAIN-ENTRY-FWD_v01.CATProduct`
- `53-10_WINDOW_BAY_WB-L-005_LEFT-COCKPIT_v02.asm`
- `53-10_ACCESS_PANEL_AP-AFT-012_LOWER-EQUIP_v01.sldasm`

## Content

Each subcomponent assembly should include:
- Assembly structure with part references
- Interface definitions to adjacent structure
- Fastener patterns and hardware callouts
- Clearance and tolerance stack-ups
- Installation sequence information

## Design Guidelines

Subcomponent assemblies must:
- Reference parts from [`../PARTS/`](../PARTS/)
- Follow assembly standards from [`../TEMPLATES/`](../TEMPLATES/)
- Document interfaces in [`../../CAI/INTERFACES/`](../../CAI/INTERFACES/)
- Use standard hardware from [`../LIBRARY/`](../LIBRARY/)

## Related Documentation

- **Individual parts**: [`../PARTS/`](../PARTS/)
- **Main assembly**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Interface definitions**: [`../../CAI/INTERFACES/`](../../CAI/INTERFACES/)
- **Assembly drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Checks

Before release, verify:
- [ ] All part references resolve correctly
- [ ] Interface geometry matches adjacent structure
- [ ] Fastener patterns follow design rules
- [ ] Clearances verified in [`../CHECKS/INTERFERENCE/`](../CHECKS/INTERFERENCE/)
- [ ] Mass properties calculated in [`../CHECKS/MASS_PROPERTIES/`](../CHECKS/MASS_PROPERTIES/)
