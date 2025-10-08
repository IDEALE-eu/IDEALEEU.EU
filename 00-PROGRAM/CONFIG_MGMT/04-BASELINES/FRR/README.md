# FRR - Flight Readiness Review

This directory contains configuration baselines established at the Flight Readiness Review gate (Spacecraft).

## Purpose

FRR baselines capture the final spacecraft configuration ready for flight, including complete testing, launch readiness, and mission operations readiness.

## Domain

**Note:** FRR is specific to the **SPACECRAFT** domain for flight readiness.

## Contents

Each baseline under this directory follows the structure:

```
FRR/
└─ SPACECRAFT/
   ├─ MANIFEST.json
   ├─ MANIFEST.sha256
   ├─ APPROVAL.md
   ├─ SCOPE.md
   ├─ CHANGELOG.md
   ├─ LINKS.md
   └─ ARTIFACTS/
      ├─ EBOM_SNAPSHOT.csv
      ├─ MBOM_SNAPSHOT.csv
      ├─ SW_RELEASES.csv
      ├─ TEST_PLANS.md
      └─ EVIDENCE/
```

## Baseline Criteria

FRR baseline is approved when:
- Spacecraft is fully integrated and tested
- All qualification and acceptance testing is complete
- Flight configuration is frozen
- Ground systems are operational
- Flight operations team is trained
- Launch vehicle interface is verified
- Mission readiness is confirmed
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/FRR_CHECKLIST.md](../COMMON/CHECKLISTS/FRR_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/FRR_CHECKLIST.md](../COMMON/CHECKLISTS/FRR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [PRR - Production Readiness Review](../PRR/)
- **Related Gate:** [ORR_EIS - Operational Readiness Review (Aircraft)](../ORR_EIS/)
