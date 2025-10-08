# SRR - System Requirements Review

This directory contains configuration baselines established at the System Requirements Review gate.

## Purpose

SRR baselines capture the approved system requirements, preliminary architecture, and stakeholder requirements at the completion of the System Requirements Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
SRR/
├─ AIRCRAFT/          (if applicable)
│  ├─ MANIFEST.json
│  ├─ MANIFEST.sha256
│  ├─ APPROVAL.md
│  ├─ SCOPE.md
│  ├─ CHANGELOG.md
│  ├─ LINKS.md
│  └─ ARTIFACTS/
└─ SPACECRAFT/        (if applicable)
   └─ … (same layout)
```

## Baseline Criteria

SRR baseline is approved when:
- System requirements specification is complete
- Stakeholder requirements are documented and traced
- Preliminary system architecture is defined
- Requirements traceability matrix is established
- All gate criteria are met per checklist: [../COMMON/CHECKLISTS/SRR_CHECKLIST.md](../COMMON/CHECKLISTS/SRR_CHECKLIST.md)

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Checklist:** [../COMMON/CHECKLISTS/SRR_CHECKLIST.md](../COMMON/CHECKLISTS/SRR_CHECKLIST.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Next Gate:** [PDR - Preliminary Design Review](../PDR/)
