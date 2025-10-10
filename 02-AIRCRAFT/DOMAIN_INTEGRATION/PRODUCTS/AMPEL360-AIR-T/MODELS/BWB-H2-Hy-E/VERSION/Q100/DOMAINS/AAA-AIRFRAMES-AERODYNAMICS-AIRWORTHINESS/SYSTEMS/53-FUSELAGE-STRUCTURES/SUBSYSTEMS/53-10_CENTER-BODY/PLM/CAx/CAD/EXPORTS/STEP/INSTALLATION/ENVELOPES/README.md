# ENVELOPES — Spatial Envelopes and Clearances

## Purpose

This directory contains STEP files defining **spatial envelopes** that represent the maximum space occupied or required by components, equipment, and clearance zones.

## What to Store

- **Component envelopes**: Maximum bounding volumes for parts
- **Equipment clearance zones**: Space required for installation/removal
- **Maintenance envelopes**: Access space for servicing
- **Kinematic envelopes**: Movement paths for deployable components
- **Protection zones**: No-build zones around critical areas

## File Naming Convention

```
53-10_ENVELOPE_<component-name>_<envelope-type>_<revision>_<date>.step
```

Example:
```
53-10_ENVELOPE_FWD-EQUIP-BAY_MAINT_RevA_20250110.step
```

## Envelope Types

- **Maximum envelope**: Largest bounding box including tolerances
- **Clearance envelope**: Required free space around component
- **Kinematic envelope**: Full range of motion for moving parts
- **Service envelope**: Access space for maintenance
- **Installation envelope**: Space needed during installation

## Related Directories

- [**../INTERFACES/**](../INTERFACES/) — Interface definitions
- [**../../ASSEMBLIES/**](../../ASSEMBLIES/) — Assemblies within envelopes
- [**../../ZONES/**](../../ZONES/) — Zone-specific envelope management
- [**../../INDEX/**](../../INDEX/) — Envelope catalogs

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
