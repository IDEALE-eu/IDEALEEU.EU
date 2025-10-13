# MODELS — Installation Assembly Models

## Purpose

This directory contains CAD models specific to installation assemblies, showing how the 53-10 Center Body integrates with adjacent systems during installation.

## Content Types

- **Installation assembly models** — Complete installation configurations
- **Interface assemblies** — Mating part envelopes and connection points
- **Positioning assemblies** — Alignment and positioning configurations
- **Temporary support assemblies** — Installation support structures

## File Formats

- `.CATPart` / `.CATProduct` — CATIA V5 native files
- `.sldprt` / `.sldasm` — SolidWorks native files
- `.asm` / `.prt` — Other CAD formats
- `.step` / `.stp` — Neutral exchange format

## Naming Convention

```
53-10_INSTALL_<interface>_<description>_v<version>.<ext>
```

Examples:
- `53-10_INSTALL_WING-ATTACH_MAIN-JOINT_v001.CATProduct`
- `53-10_INSTALL_DOOR-FRAME-52-10_CUTOUT_v002.sldasm`
- `53-10_INSTALL_AFT-BULKHEAD_INTERFACE_v001.step`

## Model Requirements

Installation models should:
- Show complete mating geometry
- Include clearance envelopes
- Document interface datums
- Specify tolerance requirements
- Include temporary supports where needed

## Cross-References

- [Parent: Installation Root](../README.md)
- [Installation Drawings](../DRAWINGS/README.md)
- [Fastener Specifications](../FASTENERS/README.md)
- [Clearances](../CLEARANCES/README.md)

## Version Control

- Track model revisions in filename
- Document changes in model metadata
- Link to associated ECO/ECR numbers
- Maintain released version history

## Related Documentation

- Interface Control Documents (ICDs)
- Installation procedures
- Assembly sequences
- Tooling requirements
