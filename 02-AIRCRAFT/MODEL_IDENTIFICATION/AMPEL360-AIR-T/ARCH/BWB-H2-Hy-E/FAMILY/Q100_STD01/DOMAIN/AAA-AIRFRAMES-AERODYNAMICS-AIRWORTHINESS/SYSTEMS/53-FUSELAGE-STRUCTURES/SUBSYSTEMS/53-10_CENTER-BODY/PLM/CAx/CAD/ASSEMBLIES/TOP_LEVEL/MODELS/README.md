# MODELS — Component Models

## Purpose

This directory contains individual component part models that are used in the top-level assembly.

## Contents

### Component Types
- **Structural components**: Frames, stringers, skin panels
- **Interface components**: Attachment fittings, brackets
- **Standard parts**: Fasteners, bushings, inserts
- **Reference components**: Mock-ups and placeholder parts

## File Organization

Organize component models by:
- **Type**: Frame, stringer, skin, fitting, etc.
- **Zone**: Forward, center, aft sections
- **Function**: Primary structure, secondary structure, interface

## File Types

- `.CATPart` — CATIA part files
- `.prt` — NX part files
- `.sldprt` — SolidWorks part files
- `.prt` — Creo part files

## Naming Convention

```
53-10_<type>_<name>_<version>.<ext>
```

Examples:
- `53-10_FRAME_F05_v01.CATPart`
- `53-10_STRINGER_L-UPPER-01_v02.prt`
- `53-10_SKIN_SP-001_v01.sldprt`

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Top-level assemblies
- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/) — Component drawings
- **Master library**: [`../../MODELS/`](../../MODELS/) — Master component repository
