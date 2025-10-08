# PDR - Preliminary Design Review

This directory contains configuration baselines established at the Preliminary Design Review gate.

## Purpose

PDR baselines capture the preliminary design, interface definitions, and requirements allocation at the completion of the Preliminary Design Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
PDR/
├─ AIRCRAFT/          (if applicable)
│  ├─ MANIFEST.json
│  ├─ MANIFEST.sha256
│  ├─ APPROVAL.md
│  ├─ SCOPE.md
│  ├─ CHANGELOG.md
│  ├─ LINKS.md
│  └─ ARTIFACTS/
│     ├─ EBOM_SNAPSHOT.csv
│     ├─ ICD_BASELINES/
│     ├─ MBSE_EXPORT/
│     └─ ...
└─ SPACECRAFT/        (if applicable)
   └─ … (same layout)
```

## Baseline Criteria

PDR baseline is approved when:
- Preliminary design is complete for all subsystems
- Interface Control Documents are established
- Requirements are allocated to design elements
- Design analysis is complete
- Make/buy decisions are documented
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/PDR_CHECKLIST.md](../COMMON/CHECKLISTS/PDR_CHECKLIST.md)

## References

- **Checklist:** [../COMMON/CHECKLISTS/PDR_CHECKLIST.md](../COMMON/CHECKLISTS/PDR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
- **Index:** [../INDEX.csv](../INDEX.csv)
