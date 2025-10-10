# Subsystem: 21-70_THERMAL_ALGORITHMS

## Description
Thermal control algorithms and autonomous thermal management

## PLM Structure

This subsystem contains HIL/SIL test evidence and documentation. Actual algorithm code resides in the avionics/software domain.

### Engineering BOM
- [EBOM_LINKS.md](./PLM/EBOM_LINKS.md) - Links to software baselines

### CAx Directories

- [CMP/](./PLM/CAx/CMP/) - **PRIMARY**: HIL/SIL test evidence, verification reports, algorithm validation
- Other directories (CAD, CAE, CAM, CAI, CAV, CAP, CAS) - Placeholders or empty

## Directory Structure

```
21-70_THERMAL_ALGORITHMS/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CMP/  (PRIMARY - test evidence)
      └─ (other dirs as placeholders)
```

## Note

Thermal control algorithms are software components. This subsystem focuses on:
- HIL (Hardware-in-Loop) test results
- SIL (Software-in-Loop) test results
- Algorithm verification and validation evidence
- Performance test reports

The actual algorithm source code is maintained in the avionics software domain.

## References
- [System 21 Overview](../../README.md)
- [Integration View](../../INTEGRATION_VIEW.md)
