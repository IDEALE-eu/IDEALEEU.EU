# ORR_EIS - Operational Readiness Review / Entry Into Service

This directory contains configuration baselines established at the Operational Readiness Review / Entry Into Service gate (Aircraft).

## Purpose

ORR_EIS baselines capture the final aircraft configuration ready for operational service, including certification compliance, operational procedures, and support infrastructure.

## Domain

**Note:** ORR_EIS is specific to the **AIRCRAFT** domain for final pre-operations readiness.

## Contents

Each baseline under this directory follows the structure:

```
ORR_EIS/
└─ AIRCRAFT/
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

ORR_EIS baseline is approved when:
- Type certification is obtained (EASA/FAA)
- Flight manual is approved
- Maintenance program is approved
- Flight crew training is complete
- Support infrastructure is ready
- Operational procedures are approved
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md](../COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md](../COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [PRR - Production Readiness Review](../PRR/)
- **Related Gate:** [FRR - Flight Readiness Review (Spacecraft)](../FRR/)
