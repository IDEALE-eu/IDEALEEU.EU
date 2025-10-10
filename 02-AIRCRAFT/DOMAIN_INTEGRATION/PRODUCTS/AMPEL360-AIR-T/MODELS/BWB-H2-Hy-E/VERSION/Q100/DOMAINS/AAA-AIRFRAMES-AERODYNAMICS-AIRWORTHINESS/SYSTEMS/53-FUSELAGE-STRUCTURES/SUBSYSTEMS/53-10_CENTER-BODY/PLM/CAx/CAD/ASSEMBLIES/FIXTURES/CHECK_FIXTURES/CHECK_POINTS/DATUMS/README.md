# DATUMS — Datum Reference Definitions

## Purpose

This directory contains datum reference definitions and coordinate system specifications for check fixture measurements.

## Contents

### Datum Types
- **Primary datums**: Principal reference surfaces
- **Secondary datums**: Additional orientation references
- **Tertiary datums**: Final positioning references
- **Datum targets**: Point, line, area datum features

## Naming Convention

Use the following pattern:
```
DATUM_<fixture-id>_<datum-identifier>_<version>.pdf
```

Examples:
- `DATUM_FIX-CHECK-F05_DRF-ABC_v01.pdf`
- `DATUM_FIX-CHECK-WING-INT_PRIMARY-PLANE_v02.pdf`
- `DATUM_FIX-CHECK-SKIN_COORD-SYS_v01.pdf`

## Datum Reference Frame (DRF)

A complete datum reference frame consists of:
- **Datum A (Primary)**: Constrains 3 degrees of freedom
- **Datum B (Secondary)**: Constrains 2 degrees of freedom
- **Datum C (Tertiary)**: Constrains 1 degree of freedom

Together these establish a 3-2-1 coordinate system.

## Datum Definition Requirements

Each datum should specify:
- **Datum identifier**: Letter designation (A, B, C, etc.)
- **Feature type**: Plane, cylinder, point, etc.
- **Location**: Coordinates or feature reference
- **Material condition**: RFS, MMC, LMC if applicable
- **Simulators**: Physical datum features on fixture
- **Tolerance**: Datum feature tolerance

## Datum Simulator Design

Physical datum simulators should:
- Represent theoretical datum exactly
- Be machined to tight tolerances (±0.05mm)
- Be stable and repeatable
- Allow proper contact with part
- Be clearly identified and marked

## GD&T Standards

Follow:
- **ASME Y14.5**: Geometric Dimensioning and Tolerancing
- **ISO 1101**: Geometrical tolerancing
- Datum reference order matters
- Material condition applies where specified

## Related Directories

- **Check points**: [`../LOCATIONS/`](../LOCATIONS/)
- **Tolerances**: [`../TOLERANCES/`](../TOLERANCES/)
- **CAD models**: [`../../MODELS/`](../../MODELS/)
