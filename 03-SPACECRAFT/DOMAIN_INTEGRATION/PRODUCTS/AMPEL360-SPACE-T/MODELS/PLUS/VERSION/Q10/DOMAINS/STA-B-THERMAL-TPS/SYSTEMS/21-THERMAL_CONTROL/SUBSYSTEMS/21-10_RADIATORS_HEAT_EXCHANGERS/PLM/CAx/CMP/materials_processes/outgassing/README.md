# OUTGASSING — Outgassing Test Data

## Purpose

This directory contains outgassing test data per ASTM E595 for all materials used in the radiator subsystem, ensuring compliance with CVCM and TML limits.

## Contents

- ASTM E595 test reports for each material
- CVCM (Collected Volatile Condensable Material) data
- TML (Total Mass Loss) data
- WVR (Water Vapor Regained) data
- Material qualification certificates
- Supplier data sheets with outgassing properties

### Acceptance Criteria

- CVCM ≤ 0.1%
- TML ≤ 1.0%
- Per ECSS-Q-ST-70-02C or NASA-STD-6016

### Documentation

Each material requires:
1. Material specification or data sheet
2. ASTM E595 test report
3. Lot/batch traceability
4. Approval for flight use

## File Naming

```
21-10-CMP-MATPROC_OUTGASSING_<topic>__r<NN>__<STATUS>.<ext>
```

## Standards

- **ECSS-Q-ST-70C**: Materials, mechanical parts, processes
- **NASA-STD-6016**: Standard materials and processes requirements
- **ASTM E595**: Outgassing test
- **NASA-STD-8739**: Workmanship standards (welding, bonding)

## Related Documentation

- Parent directory: [`../README.md`](../README.md) if not parent else None
- Requirements: [`../requirements/`](../requirements/)
- Certificates: [`../certificates/`](../certificates/)
