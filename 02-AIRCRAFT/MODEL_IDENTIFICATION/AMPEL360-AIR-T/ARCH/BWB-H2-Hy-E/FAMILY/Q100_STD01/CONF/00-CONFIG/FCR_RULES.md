<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# Functional Compliance Rules (FCR) - Q100_STD01

## Purpose

This document defines the **Functional Compliance Rules** that govern changes to the Q100_STD01 configuration baseline. These rules are enforced through CI/CD pipelines and manual CCB review.

---

## Core FCR Rules

### FCR-001: QS State Integrity
**Rule**: Any PR that modifies files under `CONF/` must include an update to `00-CONFIG/QS_STATE.yaml`.

**Enforcement**: CI check via `.ci/fcr_enforcer.py`

**Rationale**: Maintains quantum state traceability and ensures configuration changes are reflected in the QS anchor.

**Exception Process**: CCB waiver required for non-functional documentation changes.

---

### FCR-002: UTCS Manifest Consistency
**Rule**: All configuration changes must update the `hash_tree` field in `UTCS.MANIFEST.yaml`.

**Enforcement**: CI check via `.ci/fcr_enforcer.py`

**Rationale**: Ensures cryptographic integrity of the configuration baseline.

---

### FCR-003: Baseline Tagging
**Rule**: Every release tag must have a corresponding entry in `02-RELEASE_TAGS/BASELINES.csv` with:
- TAG name
- QS_ANCHOR version
- TREE_HASH (SHA-256)
- FCR_NOTE (compliance summary)

**Enforcement**: Manual CCB verification + CI check

**Rationale**: Enables auditability and rollback capability.

---

### FCR-004: TFA Domain Labeling
**Rule**: All domain-specific artifacts must include a domain tag in their header:
```yaml
# Example for geometry files
tfa_domain: AAA
ata_chapter: "51"
```

**Enforcement**: CI check via `.ci/path_validator.py`

**Rationale**: Maintains domain separation and enables automated cross-domain integration checks.

---

### FCR-005: Schema Compliance
**Rule**: Data files under `geometry/`, `weights/`, `performance/`, and `propulsion/` must validate against their respective `SCHEMA_*.yaml` files.

**Enforcement**: CI check using JSON Schema validators

**Rationale**: Ensures data consistency and prevents unit mismatch errors.

---

### FCR-006: Traceability Completeness
**Rule**: Every requirement in `03-TRACEABILITY/UTCS_THREADS.csv` must have:
- SOURCE (requirement document)
- EVIDENCE_URI (test result or analysis)
- QS_ANCHOR (version)

**Enforcement**: CI check + quarterly CCB audit

**Rationale**: Regulatory compliance (EASA, Clean Aviation) and certification readiness.

---

### FCR-007: ICD Versioning
**Rule**: Interface Control Documents listed in `04-ICD_LINKS/ICD_INDEX.md` must:
- Have a valid VERSION field
- Specify an OWNER
- Define a VERIFICATION_METHOD

**Enforcement**: Manual review during CCB

**Rationale**: Prevents interface mismatches and integration failures.

---

### FCR-008: Link Integrity
**Rule**: All relative links in markdown files must resolve to existing files or directories.

**Enforcement**: CI check via `.ci/linkcheck.yml`

**Rationale**: Prevents documentation drift and broken navigation.

---

### FCR-009: Evidence Reproducibility
**Rule**: All computational evidence in `03-TRACEABILITY/EVIDENCE/` must include:
- Checksums (`checksums.sha256`)
- Reproduction steps (`REPRO_STEPS.md`)
- Software versions used

**Enforcement**: Manual verification during audits

**Rationale**: Scientific reproducibility and regulatory acceptance.

---

### FCR-010: MAL-EEM Policy Adherence
**Rule**: Any AI/ML component must comply with `00-CONFIG/MAL-EEM_POLICY.md` regarding:
- Bias mitigation
- Fairness metrics
- Explainability requirements

**Enforcement**: Design review + CCB approval

**Rationale**: Ethical AI deployment and safety assurance.

---

## Enforcement Hierarchy

1. **CI Blocking**: FCR-001, FCR-002, FCR-004, FCR-005, FCR-008 (automated)
2. **CCB Review**: FCR-003, FCR-006, FCR-007 (meeting approval)
3. **Audit**: FCR-009, FCR-010 (quarterly/milestone-based)

---

## Change Process

To modify these rules:
1. File an ECR under `00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/INBOX/`
2. Present to CCB with impact analysis
3. Update this document + CI scripts in same PR
4. Notify all domain stewards

---

**Version**: 1.0  
**Effective Date**: 2025-10-15  
**Owner**: Configuration Management Team  
**Next Review**: 2026-01-15
