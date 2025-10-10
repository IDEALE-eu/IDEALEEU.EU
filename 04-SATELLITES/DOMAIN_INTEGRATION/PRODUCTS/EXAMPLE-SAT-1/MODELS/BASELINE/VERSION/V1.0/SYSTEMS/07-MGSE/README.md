# 07-MGSE — Mechanical Ground Support Equipment

**Optional system. Include only if required by mission.**  
**Flight status:** Non-flight. Ground use only.

## Purpose
Enable safe handling, integration, transport, and test of EXAMPLE-SAT-1 during AIT. Includes cradles, lift fixtures, alignment tools, and cleanroom handling aids.

## Integration status
- Non-flight system used only in ground operations.
- Excluded from flight mass, power, and thermal budgets.
- Interface-critical for mechanical and alignment boundaries.

## Key interfaces
- **51-PRIMARY_STRUCTURE:** Load paths, interface plates, alignment pins.
- **50-MECHANISMS_DEPLOYABLES:** Stowage and deployment verification fixtures.
- **16-EGSE:** Coordination during integrated tests.
- **ICDs:** Managed centrally at `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/` (e.g., `ICD-MGSE-51-01`).

> Interface matrix for this system: `INTERFACE_MATRIX/07↔51_50_16.csv`.

## Design and compliance
- ECSS-E-HB-32-23A (MGSE design handbook).
- Materials: non-magnetic, low-outgassing (ECSS-Q-ST-70-02C).
- Cleanliness: ISO Class 8 or better.
- Traceability: All MGSE items tracked in `00-PROGRAM/CONFIG_MGMT/05-CONFIGURATION/`.

## Artifacts rule
No PLM/CAx content in this folder. Per IDEALE rule, PLM/CAx resides only in **flight** `SUBSYSTEMS/`.

## Verification
- Structural FEM (static, dynamic).
- Modal survey during AIT.
- Alignment repeatability checks (< 50 µm).
- Witnessed dry-runs with flight hardware.

## Ownership
- AIT Lead Engineering.
- Changes via ECR/ECO in `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`.
