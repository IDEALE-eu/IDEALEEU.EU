# REFERENCES — Master Reference Models and Baseline Geometry

## Purpose

Master reference geometry models that define the official dimensional baseline for the CENTER-BODY subsystem.

## Content Types

- **Master CAD Models** — Baseline geometry definitions
- **Control Surfaces** — Theoretical mold lines and OML/IML definitions
- **Envelope Models** — Space claim and interference check models
- **Reference Skeletons** — Simplified geometry for layout and integration

## File Formats

- `.step` / `.stp` — Neutral CAD format (primary)
- `.jt` — Lightweight visualization
- `.iges` — Legacy interchange format
- `.pdf` — 2D reference drawings

## Naming Convention

```
REF_{component}_{type}_v{version}_{date}.{ext}
```

Examples:
- `REF_centerbody_envelope_v003_20240115.step`
- `REF_centerbody_OML_baseline_v001_20240101.step`
- `REF_centerbody_skeleton_v002_20240110.jt`

## File Organization

```
REFERENCES/
├─ baseline/          # Released baseline models
├─ working/           # In-progress reference updates
├─ archives/          # Previous baselines
└─ validation/        # Comparison and validation reports
```

## Cross-References

- [Parent: MASTER_GEOMETRY](../README.md)
- [Interface Definitions](../../INTERFACES/)
- [ATA-06 Master Geometry](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-00_GENERAL/)
- [System-Level Integration](../../../../INTEGRATION_VIEW.md)

## Version Control

Baseline models follow strict versioning:
- **v001-v099**: Pre-release iterations
- **v100+**: Released baselines
- Date stamps in YYYYMMDD format

## Usage Guidelines

- Always reference the latest **released** baseline
- Working models must not be used for interface definitions
- Archive previous baselines when releasing new versions
- Include validation reports comparing versions

## Validation Requirements

Reference models must:
- Pass geometric validation (closed volumes, no gaps)
- Align with ATA-06 coordinate system within ±0.01mm
- Include metadata (units, author, approval status)
- Be validated against interface envelopes

## Change Control

Reference model updates require:
- Formal ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- [PDR/CDR approval](../../REVIEWS/) for major changes
- Interface impact analysis
- Notification to all dependent systems
