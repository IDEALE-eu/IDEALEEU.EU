# PRR - Production Readiness Review

This directory contains configuration baselines established at the Production Readiness Review gate.

## Purpose

PRR baselines capture the production-ready configuration, manufacturing processes, and quality control procedures at the completion of the Production Readiness Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
PRR/
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
│     ├─ SW_RELEASES.csv
│     ├─ TEST_PLANS.md
│     └─ EVIDENCE/
└─ SPACECRAFT/        (if applicable)
   └─ … (same layout)
```

## Baseline Criteria

PRR baseline is approved when:
- Production processes are validated
- Tooling is complete and qualified
- Supply chain is established
- Quality control procedures are implemented
- First article inspection is complete
- Manufacturing personnel are trained
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/PRR_CHECKLIST.md](../COMMON/CHECKLISTS/PRR_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/PRR_CHECKLIST.md](../COMMON/CHECKLISTS/PRR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [TRR - Test Readiness Review](../TRR/)
- **Next Gates:** 
  - [ORR_EIS - Operational Readiness Review (Aircraft)](../ORR_EIS/)
  - [FRR - Flight Readiness Review (Spacecraft)](../FRR/)
