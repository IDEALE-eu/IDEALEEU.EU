# Release Policy

**Document Number:** CM-POL-RELEASE  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

This policy establishes the governance framework for releasing aircraft and spacecraft configurations, ensuring controlled distribution of verified and validated products with full traceability and compliance evidence.

## 2. Scope

Applies to all formal releases of:
- Aircraft configurations and subsystems
- Spacecraft configurations and subsystems
- Software and firmware
- Ground support equipment
- Manufacturing data packages
- Certification evidence packages

## 3. Release Authority

### 3.1 Configuration Control Board (CCB)

The CCB has final authority to approve all releases. CCB composition and procedures are defined in [05-CCB/](../../05-CCB/).

### 3.2 Release Manager

The Release Manager, appointed by the Configuration Manager, is responsible for:
- Preparing release packages
- Coordinating compliance verification
- Managing distribution
- Maintaining release registers

### 3.3 Domain Authorities

Domain-specific authorities must approve releases for their areas:
- **Chief Engineer** — Technical adequacy
- **Quality Manager** — Compliance evidence
- **Safety Manager** — Safety case completeness
- **Security Officer** — Export classification

## 4. Release Criteria

### 4.1 Mandatory Prerequisites

Before CCB review, all releases must have:

1. **Baseline Reference** — Linked to approved configuration baseline (PDR/CDR/PRR/FRR/ORR)
2. **Verification Complete** — All verification activities closed per baseline gate criteria
3. **Compliance Evidence** — Full certification evidence package assembled
4. **Traceability** — Requirements-to-test-to-acceptance traceability complete
5. **Quality Approval** — QA verification of conformance
6. **SBOM** — Software Bill of Materials in CycloneDX format
7. **Provenance** — Build and review attestations (in-toto/SLSA)
8. **Hash Verification** — SHA256 hashes for all distributed artifacts
9. **ICD Freeze** — All interface control documents at baseline revision
10. **Export Classification** — ECCN/USML determination documented

### 4.2 Release Package Contents

Each release package must contain:
- Release notes
- Manifest (YAML format)
- EBOM (Engineering Bill of Materials)
- MBOM (Manufacturing Bill of Materials)
- SBOM (Software Bill of Materials, CycloneDX)
- Compliance evidence (DO-178C, DO-254, DO-160, AS9100, ECSS as applicable)
- Interface Control Documents (frozen versions)
- CCB signoff documentation
- Distribution package with SHA256SUMS.txt
- Rollback kit and procedures
- Baseline reference (symlink or documented)
- Provenance attestations

### 4.3 Conformity Checklist

All releases must complete the conformity checklist in [04-TEMPLATES/CONFORMITY_CHECKLIST.md](../04-TEMPLATES/CONFORMITY_CHECKLIST.md).

## 5. Release Approval Process

1. **Preparation** — Release Manager assembles package per templates
2. **Self-Check** — Release Manager verifies conformity checklist
3. **Domain Review** — Domain authorities review and approve their sections
4. **QA Verification** — Quality Assurance verifies compliance evidence
5. **CCB Submission** — Complete package submitted to CCB
6. **CCB Review** — CCB evaluates readiness and approves/rejects/defers
7. **Distribution** — Upon approval, Release Manager controls distribution
8. **Registration** — Release logged in RELEASE_REGISTER.csv with metadata

## 6. Release Types

See [RELEASE_TYPES.md](./RELEASE_TYPES.md) for detailed definitions:
- Engineering Release
- Certification Release
- Production Release
- Operational Release
- Emergency Patch

## 7. Version Control

See [VERSIONING_SCHEME.md](./VERSIONING_SCHEME.md) for version numbering rules aligned with baseline gates.

## 8. Distribution Control

### 8.1 Internal Distribution

- Limited to authorized program personnel
- Access logged per [09-DISTRIBUTION/INTERNAL/](../09-DISTRIBUTION/INTERNAL/)
- No export restrictions

### 8.2 External Distribution

- Requires CCB approval and export classification review
- Distribution logged in DISTRIBUTION_LOG.csv
- Security requirements per [09-DISTRIBUTION/SECURITY.md](../09-DISTRIBUTION/SECURITY.md)
- Export classification per [09-DISTRIBUTION/EXPORT_CLASSIFICATION.md](../09-DISTRIBUTION/EXPORT_CLASSIFICATION.md)

## 9. Change Management

### 9.1 Changes to Released Configurations

All changes to released configurations follow ECR/ECO process per [01-CM_PLAN.md](../../01-CM_PLAN.md) Section 4.2.

### 9.2 Emergency Patches

Emergency patches follow expedited process defined in [02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md).

## 10. Audit and Compliance

### 10.1 Release Audits

- Pre-release conformity verification by QA
- Post-release effectiveness review after 3 months
- Annual audit of release process compliance

### 10.2 Metrics

Tracked metrics per [10-METRICS/](../10-METRICS/):
- Release cycle time (baseline to distribution)
- Defects found post-release
- Compliance coverage percentage
- Rollback frequency

## 11. Retention

### 11.1 Active Releases

Active releases retained in [05-AIRCRAFT/](../05-AIRCRAFT/) or [06-SPACECRAFT/](../06-SPACECRAFT/) directories.

### 11.2 Obsolete Releases

Obsolete releases moved to [11-ARCHIVE/OBSOLETE_RELEASES/](../11-ARCHIVE/OBSOLETE_RELEASES/) per retention schedule documented in RETENTION_LOG.csv.

### 11.3 Retention Period

- **Engineering Releases** — 5 years after superseded
- **Certification Releases** — Life of type certificate + 10 years
- **Production Releases** — Life of serial number + 15 years
- **Operational Releases** — End of service + 20 years

## 12. Roles and Responsibilities (RASCI)

See [RASCI.md](./RASCI.md) for detailed RASCI matrix.

## 13. Training

All personnel involved in release activities must complete training on:
- Release policy and procedures
- Conformity checklist requirements
- Distribution controls and export classification
- SBOM and provenance generation

## 14. Continuous Improvement

Release process reviewed quarterly during Configuration Management reviews. Lessons learned captured and process improvements implemented per [01-CM_PLAN.md](../../01-CM_PLAN.md) Section 12.

## 15. Related Documents

- [01-CM_PLAN.md](../../01-CM_PLAN.md) — Configuration Management Plan
- [RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md) — Standard release workflow
- [VERSIONING_SCHEME.md](./VERSIONING_SCHEME.md) — Version numbering scheme
- [RELEASE_TYPES.md](./RELEASE_TYPES.md) — Release type definitions
- [RASCI.md](./RASCI.md) — Roles and responsibilities

## 16. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Configuration Manager | TBD | | |
| Quality Manager | TBD | | |
| Program Manager | TBD | | |

## 17. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Configuration Manager |
