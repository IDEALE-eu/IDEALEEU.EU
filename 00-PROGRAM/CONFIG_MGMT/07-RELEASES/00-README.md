# 07-RELEASES

Release Management structure for aircraft and spacecraft configurations.

## Overview

This directory manages all formal releases of aircraft and spacecraft configurations, ensuring complete traceability, compliance evidence, and distribution control throughout the product lifecycle.

## Directory Structure

### 01-POLICY
Release policies, versioning schemes, release types, and RASCI matrix.

### 02-WORKFLOW
Release workflow processes and emergency patch procedures.

### 03-REGISTERS
- **RELEASE_REGISTER.csv** — Master register of all releases
- **DISTRIBUTION_LOG.csv** — Distribution tracking
- **RELEASE_ICD_INDEX.csv** — Interface Control Document index per release

### 04-TEMPLATES
Standard templates for release packages, release notes, and conformity checklists.

### 05-AIRCRAFT
Aircraft-specific release packages following ARP4754A, DO-178C, DO-254, DO-160, and AS9100 standards.

### 06-SPACECRAFT
Spacecraft-specific release packages following ECSS standards and ESA production assurance requirements.

### 07-COMMON
Shared libraries and cross-domain interface components.

### 08-COMPLIANCE
Certification evidence index and audit readiness packages.

### 09-DISTRIBUTION
Internal and external distribution management with security and export classification controls.

### 10-METRICS
Release cycle time, post-release defects, and compliance coverage tracking.

### 11-ARCHIVE
Obsolete releases and retention logs.

### 12-AUTOMATION
Release pipeline automation, gates, and scripts.

## Release Process

1. **Preparation** — Verify all baseline requirements, collect artifacts
2. **Packaging** — Use templates from 04-TEMPLATES/
3. **Compliance Check** — Verify against conformity checklist
4. **CCB Approval** — Configuration Control Board signoff (see [05-CCB/](../05-CCB/))
5. **Distribution** — Controlled release per 09-DISTRIBUTION/SECURITY.md
6. **Registration** — Log in 03-REGISTERS/RELEASE_REGISTER.csv
7. **Archive** — Store complete package in 05-AIRCRAFT/ or 06-SPACECRAFT/

## Versioning

Release versions map to configuration baselines:
- **Engineering** → CDR draft baseline
- **Certification** → PRR/FRR baseline
- **Production** → ORR/EIS baseline

See [01-POLICY/VERSIONING_SCHEME.md](./01-POLICY/VERSIONING_SCHEME.md) for details.

## Compliance Requirements

Each release package must include:
- SHA256 hash verification
- Software Bill of Materials (SBOM) in CycloneDX format
- Provenance attestations (in-toto/SLSA)
- Export control classification
- CCB approval signatures
- Baseline references

## Related Documents

- **[01-CM_PLAN.md](../01-CM_PLAN.md)** — Configuration Management Plan (Section 8)
- **[04-BASELINES/](../04-BASELINES/)** — Configuration baselines
- **[05-CCB/](../05-CCB/)** — Configuration Control Board
- **[09-INTERFACES/](../09-INTERFACES/)** — Interface Control Documents

## Responsibilities

- **Configuration Manager** — Maintains release register, coordinates release process
- **Release Manager** — Prepares release packages, ensures completeness
- **CCB** — Approves releases for distribution
- **Quality Assurance** — Verifies compliance evidence and conformity
- **Security Officer** — Reviews export classification and distribution controls

## Access Control

- Release packages are configuration-controlled
- Distribution requires CCB approval
- Access logs maintained per PRO-001 Document Control
- External distribution follows 09-DISTRIBUTION/SECURITY.md

---

**Status**: This directory structure is configuration-controlled. All changes must follow the program's change control process per [01-CM_PLAN.md](../01-CM_PLAN.md).
