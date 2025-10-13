# 51-00 GENERAL — Structures (BWB-H2-Hy-E, Q100)

**Purpose**  
Define the common contract for structural practices across ATA-51–57: units, allowables sources, design margins, joint categories, repair philosophy, corrosion protection, and verification methods.

## Scope
- Material systems & references (metallics, composites, adhesives)
- Global structural margins policy (UL/LL, FoS, DF, knockdowns)
- Joint taxonomy (riveted/bolted/bonded/co-bonded/bolted-bonded)
- Damage tolerance & inspection intervals (DT/NDI strategy)
- Repair standard practices and approval levels
- Corrosion/aging protection (primers, sealants, CPC)
- Test pyramid (coupon → element → subcomp → full-scale)

## Core Deliverables
- `MARGINS_POLICY.md`  — factors, combinations, load cases
- `ALLOWABLES_INDEX.csv` — source (A/B-basis), version, spec
- `JOINT_CATEGORIES.yaml` — design rules & validation checks
- `DT_NDI_STRATEGY.md` — detectable damage, intervals, methods
- `REPAIR_PHILOSOPHY.md` — SRM rules, limits of authority
- `PROTECTION_SCHEME.md` — corrosion/thermal/environmental
- `TEST_PYRAMID_PLAN.md` — trace to verification evidence

## Interfaces
- **53 Fuselage**, **57 Wing**, **54 Nacelles/Pylons**, **32 Landing Gear**, **25 Cabin**, **24 Electrical (bonding/grounding)**, **92 EWIS**.  
See `../../INTERFACE_MATRIX/51↔53_57_54_32_25_24_92.csv`.

## Acceptance
- All 51-x subsystems conform to `MARGINS_POLICY.md`.
- Allowables referenced in designs exist in `ALLOWABLES_INDEX.csv` with A/B-basis.
- Joints pass rule checks from `JOINT_CATEGORIES.yaml`.
- DT/NDI intervals justified and linked to hazards in CM/QMS.

## PLM/CAx (reference)
- `PLM/CAx/CAE/allowables_curves.*` (material cards)
- `PLM/CAx/CAD/joint_typologies.*` (parametric exemplars)
- `PLM/EBOM_LINKS.md` (non-material refs only)

## CM & Compliance
- Changes via ECR/ECO (CCB). Baselines: `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`.
- Evidence links to releases: `.../07-RELEASES/*/COMPLIANCE/`.
