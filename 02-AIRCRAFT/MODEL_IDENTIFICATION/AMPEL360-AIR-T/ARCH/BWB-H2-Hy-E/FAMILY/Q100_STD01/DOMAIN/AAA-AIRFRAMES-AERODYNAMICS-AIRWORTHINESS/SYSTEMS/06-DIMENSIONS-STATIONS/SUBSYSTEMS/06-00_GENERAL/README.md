# 06-00 GENERAL — Dimensions & Stations (BWB-H2-Hy-E, Q100)

**Purpose**  
Root node for Chapter 06 that defines the common contract: units, axis systems, sign conventions, grid granularity (FS/WL/BL/WS), nomenclature, tolerances, and master artifacts.

## Scope
- Units and numerical precision (mm, deg; rounding).
- Definition of the **Global Aircraft Frame (GAF)** and local frames.
- Conventions for **FS / WL / BL / WS** (origin, step, sign).
- Naming rules (STA, FR, WS, ZONE).
- Templates for master datasets and CI validation.

## Deliverables (this subsystem)
- `CONVENTIONS.md` — Units, signs, names, examples.
- `STATIONING_MASTER.csv` — Recommended indices and steps by domain.
- `NAMING_RULES.yaml` — Rules and regex for validators.
- `TOLERANCES_GDT.md` — Global reference tolerances.
- `VALIDATION_RULES.json` — Rules consumed by `validate-structure.sh`.

## Interfaces (consumers of 06 contract)
- **53 Fuselage**, **57 Wing**, **32 Landing Gear**, **25 Cabin**, **34 Navigation / 31 Indicating**, **92 EWIS**.  
See `../../INTERFACE_MATRIX/06↔53_57_32_25_34_92.csv`.

## Acceptance
- All derived datasets (06-10…06-90) must validate against `VALIDATION_RULES.json`.
- CAD↔CSV coherence (error ≤ 1e-6) and SHA-256 signatures in baselines.

## PLM/CAx (reference artifacts)
- `PLM/CAx/CAD/coords_master_skeleton.*` (guide solids/curves).
- `PLM/EBOM_LINKS.md` (no physical material; document references).

## Governance & CM
- Changes after CDR via **ECR/ECO** (CCB).  
- Baselines in `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`; ICDs in `09-INTERFACES/`.
