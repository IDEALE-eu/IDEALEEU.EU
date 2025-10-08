# TRR - Test Readiness Review

This directory contains configuration baselines established at the Test Readiness Review gate.

## Purpose

TRR baselines capture the test configuration, test procedures, and as-built configuration at the completion of the Test Readiness Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
TRR/
├─ AIRCRAFT/          (if applicable)
│  ├─ MANIFEST.json
│  ├─ MANIFEST.sha256
│  ├─ APPROVAL.md
│  ├─ SCOPE.md
│  ├─ CHANGELOG.md
│  ├─ LINKS.md
│  └─ ARTIFACTS/
│     ├─ EBOM_SNAPSHOT.csv
│     ├─ SW_RELEASES.csv
│     ├─ TEST_PLANS.md
│     └─ EVIDENCE/
└─ SPACECRAFT/        (if applicable)
   └─ … (same layout)
```

## Baseline Criteria

TRR baseline is approved when:
- Test articles are built and inspected
- Test procedures are approved
- Test equipment is calibrated and ready
- Test facilities are prepared
- Safety review is complete
- Test personnel are trained
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/TRR_CHECKLIST.md](../COMMON/CHECKLISTS/TRR_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/TRR_CHECKLIST.md](../COMMON/CHECKLISTS/TRR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [CDR - Critical Design Review](../CDR/)
- **Next Gate:** [PRR - Production Readiness Review](../PRR/)
