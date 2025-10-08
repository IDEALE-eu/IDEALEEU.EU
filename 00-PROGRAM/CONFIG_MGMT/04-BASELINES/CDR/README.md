# CDR - Critical Design Review

This directory contains configuration baselines established at the Critical Design Review gate.

## Purpose

CDR baselines capture the final detailed design, manufacturing plans, and complete verification approach at the completion of the Critical Design Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
CDR/
├─ AIRCRAFT/          (if applicable)
│  ├─ MANIFEST.json
│  ├─ MANIFEST.sha256
│  ├─ APPROVAL.md
│  ├─ SCOPE.md
│  ├─ CHANGELOG.md
│  ├─ LINKS.md
│  └─ ARTIFACTS/
│     ├─ EBOM_SNAPSHOT.csv
│     ├─ MBOM_SNAPSHOT.csv
│     ├─ ICD_BASELINES/
│     ├─ MBSE_EXPORT/
│     ├─ SW_RELEASES.csv
│     ├─ TEST_PLANS.md
│     └─ EVIDENCE/
└─ SPACECRAFT/        (if applicable)
   └─ … (same layout)
```

## Baseline Criteria

CDR baseline is approved when:
- Detailed design is complete for all subsystems
- All design analyses are complete and approved
- Manufacturing plans are established
- Test procedures are complete
- Final EBOM and MBOM are approved
- All TBDs/TBRs are resolved
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/CDR_CHECKLIST.md](../COMMON/CHECKLISTS/CDR_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/CDR_CHECKLIST.md](../COMMON/CHECKLISTS/CDR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [PDR - Preliminary Design Review](../PDR/)
- **Next Gate:** [TRR - Test Readiness Review](../TRR/)
