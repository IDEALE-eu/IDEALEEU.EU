# FRAMES — Structural Frame Components

## Purpose

This directory contains CAD models for circumferential structural frames that form the primary load-bearing structure of the 53-10 Center Body. Frames provide shape stability, distribute loads, and support secondary structures.

## Frame Types

- **Major frames**: Primary load-carrying frames at critical stations
- **Intermediate frames**: Secondary frames between major stations
- **Pressure frames**: Frames designed for pressure loads
- **Cargo frames**: Frames with cargo support provisions
- **Bulkhead-frame interfaces**: Frames connecting to bulkheads

## Naming Convention

```
53-10_FRAME_<FRAME-ID>_<LOCATION>_<TYPE>_v<VERSION>.<ext>
```

Examples:
- `53-10_FRAME_FR-001_FWD_PRESSURE_v01.CATPart`
- `53-10_FRAME_FR-015_AFT_INTERMEDIATE_v02.prt`
- `53-10_FRAME_FR-008_CARGO-FLR_SUPPORT_v01.sldprt`

## Design Requirements

Frames must:
- Maintain fuselage cross-section shape
- Withstand circumferential (hoop) loads
- Support longitudinal loads from stringers
- Provide attachment for skin panels
- Include provisions for systems routing
- Meet damage tolerance requirements

## Material Specifications

Typical materials:
- Aluminum 7075-T6 (high-strength applications)
- Aluminum 2024-T3 (general applications)
- Titanium Ti-6Al-4V (high-temperature areas)
- Composite materials (weight-critical areas)

Material properties defined in [`../../METADATA/MATERIALS/`](../../METADATA/MATERIALS/)

## Manufacturing Methods

- Machined from plate or forging
- Built-up from channels and angles
- Composite layup (for composite frames)
- Combination fabrication

## Interface Requirements

Frames interface with:
- Stringers (Z-clips, cleats)
- Skin panels (riveted or bonded)
- Bulkheads (splice fittings)
- Floor beams (attach fittings)
- Systems brackets and mounts

## Related Documentation

- **Design rules**: [`../../CONFIG/DESIGN_RULES/`](../../CONFIG/DESIGN_RULES/)
- **Standards**: [`../../../../51-STRUCTURES-GENERAL/`](../../../../51-STRUCTURES-GENERAL/)
- **Assembly**: [`../../../ASSEMBLIES/`](../../../ASSEMBLIES/)
