# INTERFACES — Component Interface Definitions

## Purpose

This directory contains STEP files defining **interface geometries and mating surfaces** between the center body (53-10) and adjacent systems.

## What to Store

- **Mounting interfaces**: Attachment points and bolt patterns
- **Mating surfaces**: Interface geometry between systems
- **Clearance envelopes**: Space claims at interfaces
- **Connector locations**: Electrical, hydraulic, and pneumatic connections
- **Interface control documents (ICD) geometry**: Reference models from ICDs

## File Naming Convention

```
53-10_INTERFACE_<adjacent-system>_<interface-id>_<revision>_<date>.step
```

Example:
```
53-10_INTERFACE_21-AIR-COND_IFC-001_RevA_20250110.step
```

## Interface Management

- Coordinate with system integration team
- Reference ICDs in `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- Align with [**../ENVELOPES/**](../ENVELOPES/) for space management
- Cross-reference with adjacent system directories

## Related Directories

- [**../ENVELOPES/**](../ENVELOPES/) — Spatial envelopes and clearances
- [**../../ASSEMBLIES/TOP_LEVEL/**](../../ASSEMBLIES/TOP_LEVEL/) — Complete assemblies showing interfaces
- [**../../ZONES/**](../../ZONES/) — Zone-specific interfaces
- [**../../INDEX/**](../../INDEX/) — Interface catalogs

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- ICD repository: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
