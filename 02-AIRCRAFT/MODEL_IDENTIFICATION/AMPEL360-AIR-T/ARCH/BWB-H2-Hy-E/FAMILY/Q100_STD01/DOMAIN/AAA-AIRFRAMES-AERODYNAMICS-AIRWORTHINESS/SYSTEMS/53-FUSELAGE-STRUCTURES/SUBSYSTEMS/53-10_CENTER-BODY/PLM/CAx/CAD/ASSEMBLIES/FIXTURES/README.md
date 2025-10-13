# FIXTURES — Assembly Fixtures and Tooling

## Purpose

This directory contains CAD models for fixtures and tooling used in assembly, testing, and inspection of the 53-10 Center Body.

## Contents

### Fixture Categories
- **[JIGS/](./JIGS/)** — Assembly jigs and positioning fixtures
- **[CHECK_FIXTURES/](./CHECK_FIXTURES/)** — Inspection and dimensional verification tooling

## Fixture Types

### Assembly Fixtures (Jigs)
- Alignment and positioning tools
- Assembly support structures
- Component holding fixtures
- Installation aids

### Check Fixtures
- Dimensional inspection tools
- Hole pattern verification
- Interface verification fixtures
- Quality control templates

## Naming Convention

Use the following pattern:
```
53-10_FIX_<fixture-type>_<purpose>_<version>.<ext>
```

Examples:
- `53-10_FIX_JIG_FRAME-ASSEMBLY_v01.CATProduct`
- `53-10_FIX_CHECK_WING-INTERFACE_v02.asm`

## Fixture Requirements

All fixtures should:
- Reference master coordinate system
- Include locating features
- Document usage procedures
- Specify calibration requirements
- Define inspection intervals

## Related Directories

- **Test assemblies**: [`../TEST/`](../TEST/)
- **Manufacturing**: [`../../../CAM/`](../../../CAM/)
- **Inspection**: [`../../../CAI/`](../../../CAI/)
