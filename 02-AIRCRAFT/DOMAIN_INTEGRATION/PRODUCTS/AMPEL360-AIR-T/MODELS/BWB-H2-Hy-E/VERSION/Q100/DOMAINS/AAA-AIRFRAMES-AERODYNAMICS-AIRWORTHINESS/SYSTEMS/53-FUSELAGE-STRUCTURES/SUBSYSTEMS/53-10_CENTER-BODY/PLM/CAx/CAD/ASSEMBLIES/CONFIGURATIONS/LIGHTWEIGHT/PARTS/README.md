# PARTS — Component Part Files

## Purpose

This directory contains lightweight part files that are used within the lightweight assembly configurations.

## Contents

### Part Types
- **Simplified geometry**: Parts with reduced feature complexity
- **Display representations**: Lightweight visualization models
- **Reference parts**: Envelope and interface parts

## Naming Convention

Use the following pattern:
```
53-10_PRT_<part-name>_LW_<version>.<ext>
```

Examples:
- `53-10_PRT_FRAME-F05_LW_v01.CATPart`
- `53-10_PRT_STRINGER-S12_LW_v02.prt`
- `53-10_PRT_SKIN-PANEL-SP01_LW_v01.sldprt`

## Optimization Techniques

Parts are optimized through:
- **Feature suppression**: Non-visible or non-essential features removed
- **Simplified geometry**: Reduced detail on small features (fillets, chamfers)
- **Reduced precision**: Lower tessellation for curved surfaces
- **Lightweight bodies**: Graphics-only representations

## Quality Requirements

Lightweight parts must maintain:
- External interface geometry accuracy
- Overall dimensions (±0.1 mm)
- Mass properties (±5%)
- Coordinate system alignment

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Full detail parts**: [`../../MODELS/`](../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
