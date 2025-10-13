# DATUMS — Reference Datums and Alignment Features

## Purpose

Physical reference features and datums for dimensional control, alignment, and measurement of the CENTER-BODY structure.

## Content Types

- **Primary Datums** — A-B-C datum features per ASME Y14.5
- **Tooling Datums** — Assembly and manufacturing reference features
- **Measurement Datums** — Inspection and verification reference points
- **Alignment Targets** — Optical and mechanical alignment features

## File Formats

- `.step` / `.stp` — 3D datum feature geometry
- `.dxf` / `.dwg` — 2D datum drawings
- `.csv` — Datum coordinate tables
- `.pdf` — Datum control specifications

## Naming Convention

```
DATUM_{type}_{identifier}_v{version}.{ext}
```

Examples:
- `DATUM_primary_A_v001.step`
- `DATUM_tooling_aft_bulkhead_v002.pdf`
- `DATUM_alignment_coordinates_v001.csv`

## Cross-References

- [Parent: MASTER_GEOMETRY](../README.md)
- [Coordinate Systems](../COORDINATE_SYSTEMS/README.md)
- [GD&T Schemes: TOLERANCES](../../TOLERANCES/GDNT_SCHEMES/README.md)
- [ATA-06 Dimensions & Stations](../../../../../../../06-DIMENSIONS-STATIONS/)

## Datum Hierarchy

```
Primary Structural Datums (A-B-C)
  ├─ Tooling Datums
  ├─ Measurement Datums
  └─ Interface Datums
```

## Validation Requirements

- Coordinate accuracy: ±0.1mm relative to GAF
- Datum feature repeatability per manufacturing tolerance
- CMM measurement plans for each datum
- Traceability to ATA-06 master datums

## Change Control

Critical datums require:
- Full ECO process via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Impact analysis on interfaces
- Re-certification of affected assemblies
