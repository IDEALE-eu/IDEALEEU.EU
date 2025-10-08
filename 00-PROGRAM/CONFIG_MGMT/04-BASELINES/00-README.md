# Baselines

Immutable snapshots at each gate. Changes after baseline require ECR→ECO and new baseline.

## Purpose

This directory maintains configuration baselines established at major program gates. Each baseline represents a frozen, approved configuration snapshot that serves as a reference point for:
- Configuration control and change management
- Requirements traceability
- Interface management
- Verification and validation activities
- Manufacturing and production releases

## Structure

Baselines are organized by gate:
- **[SRR/](./SRR/)** - System Requirements Review ([checklist](./COMMON/CHECKLISTS/SRR_CHECKLIST.md))
- **[MCR/](./MCR/)** - Mission Concept Review
- **[PDR/](./PDR/)** - Preliminary Design Review ([checklist](./COMMON/CHECKLISTS/PDR_CHECKLIST.md))
- **[CDR/](./CDR/)** - Critical Design Review ([checklist](./COMMON/CHECKLISTS/CDR_CHECKLIST.md))
- **[TRR/](./TRR/)** - Test Readiness Review ([checklist](./COMMON/CHECKLISTS/TRR_CHECKLIST.md))
- **[PRR/](./PRR/)** - Production Readiness Review ([checklist](./COMMON/CHECKLISTS/PRR_CHECKLIST.md))
- **[ORR_EIS/](./ORR_EIS/)** - Operational Readiness Review - Aircraft final pre-ops ([checklist](./COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md))
- **[FRR/](./FRR/)** - Flight Readiness Review - Spacecraft flight readiness ([checklist](./COMMON/CHECKLISTS/FRR_CHECKLIST.md))

## Contents

- **[00-README.md](./00-README.md)** - This file
- **[INDEX.csv](./INDEX.csv)** - Master registry of all baselines
- **[COMMON/](./COMMON/)** - Shared checklists and templates
  - **[CHECKLISTS/](./COMMON/CHECKLISTS/)** - Gate-specific approval checklists
  - **[TEMPLATES/](./COMMON/TEMPLATES/)** - Manifest schemas and document templates
- **[GATE]/** - Individual gate baseline folders ([see Structure](#structure))

## Baseline Structure

Each gate folder contains domain-specific baselines:

```
[GATE]/
├─ AIRCRAFT/                               # Aircraft domain baseline
│  ├─ MANIFEST.json                        # Baseline manifest
│  ├─ MANIFEST.sha256                      # Hash verification file
│  ├─ APPROVAL.md                          # CCB approval record
│  ├─ SCOPE.md                             # Baseline scope definition
│  ├─ CHANGELOG.md                         # Changes since prior baseline
│  ├─ LINKS.md                             # References to frozen artifacts
│  └─ ARTIFACTS/                           # Baseline artifacts
│     ├─ EBOM_SNAPSHOT.csv                 # Engineering BOM snapshot
│     ├─ MBOM_SNAPSHOT.csv                 # Manufacturing BOM snapshot
│     ├─ ICD_BASELINES/                    # Interface control documents
│     ├─ MBSE_EXPORT/                      # SysML/MBSE exports
│     ├─ SW_RELEASES.csv                   # Software release registry
│     ├─ TEST_PLANS.md                     # Test documentation
│     └─ EVIDENCE/                         # Compliance evidence
└─ SPACECRAFT/                             # Spacecraft domain baseline
   └─ … (same layout)
```

## Operational Rules

1. **Immutability**: Once a baseline is approved and hashed, no modifications are permitted
2. **Hash Verification**: All artifacts must be hashed and stored in `MANIFEST.sha256`
3. **Git Tagging**: Each approved baseline is tagged using format: `baseline/<GATE>/<YYYY-MM-DD>/<domain>`
4. **Change Control**: Any changes after baseline require ECR→ECO process and new baseline
5. **Domain Separation**: Maintain separate AIRCRAFT and SPACECRAFT folders (or single folder if only one domain applies)

## Baseline Process

1. **Pre-Baseline**: Complete all gate criteria, reviews, and documentation
2. **Approval**: CCB reviews and approves baseline at gate meeting
3. **Capture**: Create manifest, collect artifacts, generate hashes
4. **Tag**: Apply git tag with baseline identifier
5. **Lock**: Mark baseline as read-only, enable change control
6. **Communicate**: Notify stakeholders of baseline availability

## References

- **CCB**: [../05-CCB/](../05-CCB/)
- **Changes**: [../06-CHANGES/](../06-CHANGES/)
- **Interfaces**: [../09-INTERFACES/](../09-INTERFACES/)
- **Traceability**: [../10-TRACEABILITY/](../10-TRACEABILITY/)
- **Standards**: [../../STANDARDS/](../../STANDARDS/)
- **Digital Thread**: [../../DIGITAL_THREAD/04-MBSE/MODEL_BASELINES/](../../DIGITAL_THREAD/04-MBSE/MODEL_BASELINES/)
- **Tagging Conventions**: [../12-CI_CD_RULES/TAGGING.md](../12-CI_CD_RULES/TAGGING.md)

## Compliance

- **AS9100**: Configuration management requirements
- **ECSS-M-ST-40C**: Space configuration management
- **ARP4754A**: Aircraft systems development lifecycle
- **ISO 10007**: Configuration management guidelines

## Quick Navigation

### Gates and Checklists
| Gate | Directory | Checklist | Description |
|------|-----------|-----------|-------------|
| SRR | [SRR/](./SRR/) | [Checklist](./COMMON/CHECKLISTS/SRR_CHECKLIST.md) | System Requirements Review |
| MCR | [MCR/](./MCR/) | - | Mission Concept Review |
| PDR | [PDR/](./PDR/) | [Checklist](./COMMON/CHECKLISTS/PDR_CHECKLIST.md) | Preliminary Design Review |
| CDR | [CDR/](./CDR/) | [Checklist](./COMMON/CHECKLISTS/CDR_CHECKLIST.md) | Critical Design Review |
| TRR | [TRR/](./TRR/) | [Checklist](./COMMON/CHECKLISTS/TRR_CHECKLIST.md) | Test Readiness Review |
| PRR | [PRR/](./PRR/) | [Checklist](./COMMON/CHECKLISTS/PRR_CHECKLIST.md) | Production Readiness Review |
| ORR_EIS | [ORR_EIS/](./ORR_EIS/) | [Checklist](./COMMON/CHECKLISTS/ORR_EIS_CHECKLIST.md) | Operational Readiness (Aircraft) |
| FRR | [FRR/](./FRR/) | [Checklist](./COMMON/CHECKLISTS/FRR_CHECKLIST.md) | Flight Readiness (Spacecraft) |

### Templates and Tools
- **[Common Resources](./COMMON/)** - Shared templates and checklists
- **[Manifest Schema](./COMMON/TEMPLATES/MANIFEST.schema.json)** - JSON schema for baseline manifests
- **[Example Manifest](./COMMON/TEMPLATES/MANIFEST.example.json)** - Sample baseline manifest
- **[Approval Template](./COMMON/TEMPLATES/APPROVAL.md)** - CCB approval documentation
- **[Links Template](./COMMON/TEMPLATES/LINKS.md)** - Cross-reference template
- **[Baseline Index](./INDEX.csv)** - Master registry of all baselines
