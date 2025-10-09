# 51-10 MATERIALS & ALLOWABLES — Structures (BWB-H2-Hy-E, Q100)

**Under System:** 51-STRUCTURES-GENERAL • **Architecture:** BWB-H2-Hy-E • **Domain:** AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS

## Purpose
Define material specifications, allowable stresses, and material property databases for all structural materials used across ATA-51–57.

## Deliverables
- Material specifications database (metallics, composites, adhesives)
- Allowables data (A-basis, B-basis) with statistical basis
- Material qualification test results
- Environmental knockdown factors
- Temperature-dependent properties

## Interfaces
- **53 Fuselage**: Material selection for fuselage structures
- **57 Wing**: Material selection for wing structures
- **54 Nacelles/Pylons**: Material selection for nacelle structures
- **51-00 General**: Feeds into ALLOWABLES_INDEX.csv
- **51-20 Manufacturing**: Material processability requirements

## PLM/CAx
- `PLM/CAx/CAE/` — Material cards and property databases
- `PLM/CAx/CAP/` — Material procurement specifications
- `PLM/CAx/CAV/` — Material qualification test data

## CM & Compliance
- Changes via ECR/ECO (CCB)
- Material changes require revalidation per test pyramid
- Traceability to material standards (AMS, ASTM, etc.)
