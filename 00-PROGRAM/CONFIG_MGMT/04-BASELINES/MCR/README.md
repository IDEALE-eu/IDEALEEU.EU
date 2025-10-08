# MCR - Mission Concept Review

This directory contains configuration baselines established at the Mission Concept Review gate.

## Purpose

MCR baselines capture the mission concept, preliminary requirements, and feasibility analysis at the completion of the Mission Concept Review milestone.

## Contents

Each baseline under this directory follows the structure:

```
MCR/
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

MCR baseline is approved when:
- Mission concept is defined and documented
- Preliminary mission requirements are established
- Feasibility studies are complete
- Mission architecture alternatives are evaluated
- Stakeholder needs are captured

## References

- **Main Baselines:** [../00-README.md](../00-README.md)
- **Templates:** [../COMMON/TEMPLATES/](../COMMON/TEMPLATES/)
  - [MANIFEST.schema.json](../COMMON/TEMPLATES/MANIFEST.schema.json)
  - [MANIFEST.example.json](../COMMON/TEMPLATES/MANIFEST.example.json)
  - [APPROVAL.md](../COMMON/TEMPLATES/APPROVAL.md)
  - [LINKS.md](../COMMON/TEMPLATES/LINKS.md)
- **Index:** [../INDEX.csv](../INDEX.csv)
- **Previous Gate:** [SRR - System Requirements Review](../SRR/)
- **Next Gate:** [PDR - Preliminary Design Review](../PDR/)
