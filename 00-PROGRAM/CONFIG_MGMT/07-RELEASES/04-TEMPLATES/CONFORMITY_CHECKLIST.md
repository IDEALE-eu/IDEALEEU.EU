# Release Conformity Checklist

**Release ID:** [REL-ACFT-x.y.z or REL-SC-x.y.z]  
**Version:** [x.y.z]  
**Release Type:** [Engineering / Certification / Production / Operational / Emergency]  
**Date:** [YYYY-MM-DD]  
**Reviewer:** [Name]

---

## Purpose

This checklist ensures all mandatory requirements for a release are met before CCB approval and distribution. All items marked as "Required" must be checked "Yes" for the release to proceed.

**Instructions:**
1. Review each item
2. Mark Yes/No/N/A
3. Provide notes or evidence location for each item
4. Ensure all "Required" items are "Yes"
5. Obtain approvals at end

---

## 1. Release Package Structure

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 1.1 | Release directory created per naming convention | Yes | [ ] Yes [ ] No | Path: |
| 1.2 | RELEASE_NOTES.md present and complete | Yes | [ ] Yes [ ] No | Reviewed by: |
| 1.3 | MANIFEST.yaml present and complete | Yes | [ ] Yes [ ] No | Verified: |
| 1.4 | EFFECTIVITY.csv present with serial number mapping | Conditional* | [ ] Yes [ ] No [ ] N/A | *Required for Production+ |
| 1.5 | All subdirectories created per structure | Yes | [ ] Yes [ ] No | Verified: |

---

## 2. Bill of Materials

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 2.1 | EBOM/ directory populated | Yes | [ ] Yes [ ] No | Item count: |
| 2.2 | EBOM items match baseline | Yes | [ ] Yes [ ] No | Baseline ref: |
| 2.3 | MBOM/ directory populated | Conditional* | [ ] Yes [ ] No [ ] N/A | *Required for Production+ |
| 2.4 | MBOM items traceable to EBOM | Conditional* | [ ] Yes [ ] No [ ] N/A | *Required for Production+ |
| 2.5 | All part numbers properly formatted per 02-PART_NUMBERING.md | Yes | [ ] Yes [ ] No | Spot check: |

---

## 3. Software Bill of Materials (SBOM)

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 3.1 | SBOM/ directory exists | Yes | [ ] Yes [ ] No | Path: |
| 3.2 | sbom.json file in CycloneDX format | Yes | [ ] Yes [ ] No | Format verified: |
| 3.3 | SBOM includes all software components | Yes | [ ] Yes [ ] No | Component count: |
| 3.4 | SBOM includes all third-party libraries | Yes | [ ] Yes [ ] No | Library count: |
| 3.5 | License information complete for all components | Yes | [ ] Yes [ ] No | Reviewed by Legal: |
| 3.6 | SBOM signed with authorized key | Yes | [ ] Yes [ ] No | Signature file: sbom.json.sig |
| 3.7 | Vulnerability scan performed and documented | Yes | [ ] Yes [ ] No | Scan date: / Tool: |
| 3.8 | Critical vulnerabilities resolved or waived | Yes | [ ] Yes [ ] No | Critical count: 0 |

---

## 4. Compliance Evidence

### 4.1 Aircraft Compliance (if applicable)

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 4.1.1 | DO-178C software lifecycle data complete | Conditional* | [ ] Yes [ ] No [ ] N/A | *If software | DAL: |
| 4.1.2 | DO-254 hardware lifecycle data complete | Conditional* | [ ] Yes [ ] No [ ] N/A | *If complex electronics | DAL: |
| 4.1.3 | DO-160 environmental qualification evidence | Conditional* | [ ] Yes [ ] No [ ] N/A | *If applicable | Category: |
| 4.1.4 | AS9100 quality system evidence | Yes | [ ] Yes [ ] No | Audit date: |
| 4.1.5 | ARP4754A system development records | Yes | [ ] Yes [ ] No | Compliance matrix: |
| 4.1.6 | ARP4761 safety assessment complete | Yes | [ ] Yes [ ] No | Hazard analysis: |

### 4.2 Spacecraft Compliance (if applicable)

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 4.2.1 | ECSS-Q-ST-80 software standards compliance | Conditional* | [ ] Yes [ ] No [ ] N/A | *If software | Category: |
| 4.2.2 | ECSS-Q-ST-70 materials and processes evidence | Yes | [ ] Yes [ ] No | Materials qualified: |
| 4.2.3 | Radiation test results | Conditional* | [ ] Yes [ ] No [ ] N/A | *If radiation environment | TID/SEE: |
| 4.2.4 | ESA production assurance evidence | Yes | [ ] Yes [ ] No | PA level: |
| 4.2.5 | PSS-05-0 software engineering compliance | Conditional* | [ ] Yes [ ] No [ ] N/A | *If software |

### 4.3 Common Compliance

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 4.3.1 | Compliance matrices present for all applicable standards | Yes | [ ] Yes [ ] No | Count: / Coverage: |
| 4.3.2 | All compliance evidence traceable to requirements | Yes | [ ] Yes [ ] No | Traceability %: |
| 4.3.3 | Compliance evidence ≥99% complete | Yes | [ ] Yes [ ] No | Actual: |
| 4.3.4 | All findings from authorities closed or waived | Yes | [ ] Yes [ ] No | Open findings: |
| 4.3.5 | Deviations and waivers documented and approved | Conditional* | [ ] Yes [ ] No [ ] N/A | *If any exist | Count: |

---

## 5. Interface Control Documents (ICDs)

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 5.1 | All ICDs identified for this configuration | Yes | [ ] Yes [ ] No | ICD count: |
| 5.2 | ICDs frozen at baseline revision | Yes | [ ] Yes [ ] No | All at baseline rev: |
| 5.3 | ICD copies stored in INTERFACES/ICDs/ | Yes | [ ] Yes [ ] No | Verified: |
| 5.4 | RELEASE_ICD_INDEX.csv updated | Yes | [ ] Yes [ ] No | Entries: |
| 5.5 | Backward compatibility documented | Yes | [ ] Yes [ ] No | Compatible: Y/N |

---

## 6. Verification and Validation

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 6.1 | All verification activities per baseline complete | Yes | [ ] Yes [ ] No | Baseline gate: |
| 6.2 | Test traceability matrix complete (req→test→result) | Yes | [ ] Yes [ ] No | Coverage %: |
| 6.3 | Unit tests executed with passing results | Yes | [ ] Yes [ ] No | Pass rate: |
| 6.4 | Integration tests executed with passing results | Yes | [ ] Yes [ ] No | Pass rate: |
| 6.5 | System tests executed with passing results | Yes | [ ] Yes [ ] No | Pass rate: |
| 6.6 | Regression tests executed with passing results | Yes | [ ] Yes [ ] No | Pass rate: |
| 6.7 | Test coverage ≥95% for critical software | Conditional* | [ ] Yes [ ] No [ ] N/A | *If software | Actual: |
| 6.8 | All critical defects resolved | Yes | [ ] Yes [ ] No | Critical count: 0 |
| 6.9 | Validation against operational scenarios complete | Conditional* | [ ] Yes [ ] No [ ] N/A | *For Operational+ |

---

## 7. Safety and Security

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 7.1 | Safety case complete | Yes | [ ] Yes [ ] No | Reviewed by: |
| 7.2 | All hazards mitigated to acceptable level | Yes | [ ] Yes [ ] No | Residual risk: |
| 7.3 | FMEA/FMECA complete | Yes | [ ] Yes [ ] No | Critical items: |
| 7.4 | Security vulnerability assessment performed | Yes | [ ] Yes [ ] No | Assessment date: |
| 7.5 | Penetration testing complete (if applicable) | Conditional* | [ ] Yes [ ] No [ ] N/A | *For networked systems |
| 7.6 | Security patches up to date | Yes | [ ] Yes [ ] No | Patch date: |

---

## 8. Cryptographic Verification

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 8.1 | SHA256 hashes calculated for all files | Yes | [ ] Yes [ ] No | File count: |
| 8.2 | SHA256SUMS.txt file created | Yes | [ ] Yes [ ] No | Verified: |
| 8.3 | SHA256SUMS.txt signed | Yes | [ ] Yes [ ] No | Signature file: |
| 8.4 | Hash verification instructions provided | Yes | [ ] Yes [ ] No | In README: |
| 8.5 | Distribution package hash calculated | Yes | [ ] Yes [ ] No | SHA256: |

---

## 9. Provenance and Attestations

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 9.1 | PROVENANCE/ directory exists | Yes | [ ] Yes [ ] No | Path: |
| 9.2 | Build attestation (in-toto/SLSA) present | Yes | [ ] Yes [ ] No | Format: |
| 9.3 | Materials attestation present | Yes | [ ] Yes [ ] No | Source traceable: |
| 9.4 | Review attestation present | Yes | [ ] Yes [ ] No | Code review: 100% |
| 9.5 | Attestations signed with authorized keys | Yes | [ ] Yes [ ] No | Keys verified: |
| 9.6 | Source control commit/tag documented | Yes | [ ] Yes [ ] No | Commit SHA: |

---

## 10. Export Control

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 10.1 | Export classification review performed | Yes | [ ] Yes [ ] No | Reviewed by: |
| 10.2 | ECCN determined (if applicable) | Conditional* | [ ] Yes [ ] No [ ] N/A | *If export-controlled | ECCN: |
| 10.3 | USML check performed | Yes | [ ] Yes [ ] No | On USML: Y/N |
| 10.4 | Dual-use determination documented | Yes | [ ] Yes [ ] No | Dual-use: Y/N |
| 10.5 | EXPORT_CLASSIFICATION.md complete | Yes | [ ] Yes [ ] No | Reviewer: / Date: |
| 10.6 | Legal review obtained (if required) | Conditional* | [ ] Yes [ ] No [ ] N/A | *If export issues | Attorney: |

---

## 11. Approvals and Signoff

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 11.1 | CCB approval obtained | Yes | [ ] Yes [ ] No | Date: / Decision: |
| 11.2 | CCB approval documented in SIGNOFF/ | Yes | [ ] Yes [ ] No | File: CCB_APPROVAL.pdf |
| 11.3 | CCB members' signatures collected | Yes | [ ] Yes [ ] No | Signature count: |
| 11.4 | Engineering Manager approval | Yes | [ ] Yes [ ] No | Date: |
| 11.5 | Quality Manager approval | Yes | [ ] Yes [ ] No | Date: |
| 11.6 | Safety Manager approval | Yes | [ ] Yes [ ] No | Date: |
| 11.7 | Security Officer approval | Yes | [ ] Yes [ ] No | Date: |
| 11.8 | Certification authority approval (if required) | Conditional* | [ ] Yes [ ] No [ ] N/A | *For Certification+ | Authority: / Date: |

---

## 12. Baseline and Traceability

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 12.1 | Baseline gate identified | Yes | [ ] Yes [ ] No | Gate: |
| 12.2 | Baseline reference documented | Yes | [ ] Yes [ ] No | Baseline ID: |
| 12.3 | BASELINE_REF/ symlink or documentation exists | Yes | [ ] Yes [ ] No | Target: |
| 12.4 | All changes since previous release documented | Yes | [ ] Yes [ ] No | ECR/ECO count: |
| 12.5 | Configuration items properly identified | Yes | [ ] Yes [ ] No | CI count: |
| 12.6 | Traceability to requirements verified | Yes | [ ] Yes [ ] No | Traceability %: |

---

## 13. Distribution Package

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 13.1 | DISTRIBUTION/ directory exists | Yes | [ ] Yes [ ] No | Path: |
| 13.2 | Distribution package created (ZIP/TAR) | Yes | [ ] Yes [ ] No | File: / Size: |
| 13.3 | README with extraction instructions included | Yes | [ ] Yes [ ] No | Reviewed: |
| 13.4 | Package integrity tested (extract and verify) | Yes | [ ] Yes [ ] No | Test date: |
| 13.5 | Distribution package SHA256 calculated | Yes | [ ] Yes [ ] No | SHA256: |
| 13.6 | Distribution list identified and approved | Yes | [ ] Yes [ ] No | Recipient count: |

---

## 14. Rollback Kit

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 14.1 | ROLLBACK_KIT/ directory exists | Yes | [ ] Yes [ ] No | Path: |
| 14.2 | rollback_procedure.md present and complete | Yes | [ ] Yes [ ] No | Reviewed by: |
| 14.3 | Rollback procedure tested | Yes | [ ] Yes [ ] No | Test date: / Result: |
| 14.4 | Rollback scripts included (if applicable) | Conditional* | [ ] Yes [ ] No [ ] N/A | *If automated |
| 14.5 | Previous version artifacts included (if needed) | Conditional* | [ ] Yes [ ] No [ ] N/A | *If required |
| 14.6 | Rollback verification procedure documented | Yes | [ ] Yes [ ] No | Verified: |

---

## 15. Release Register

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 15.1 | RELEASE_REGISTER.csv updated | Yes | [ ] Yes [ ] No | Entry verified: |
| 15.2 | All required fields populated | Yes | [ ] Yes [ ] No | Fields complete: |
| 15.3 | DISTRIBUTION_LOG.csv ready for entries | Yes | [ ] Yes [ ] No | Verified: |
| 15.4 | RELEASE_ICD_INDEX.csv updated | Yes | [ ] Yes [ ] No | Entries: |

---

## 16. Documentation

| # | Item | Required | Status | Evidence/Notes |
|---|------|----------|--------|----------------|
| 16.1 | Release notes complete per template | Yes | [ ] Yes [ ] No | Reviewed by: |
| 16.2 | Installation instructions clear and complete | Yes | [ ] Yes [ ] No | Reviewed by: |
| 16.3 | Known issues and limitations documented | Yes | [ ] Yes [ ] No | Issue count: |
| 16.4 | Compatibility information documented | Yes | [ ] Yes [ ] No | Backward compatible: Y/N |
| 16.5 | Contact information for support provided | Yes | [ ] Yes [ ] No | Verified: |

---

## Summary

### Statistics

- **Total Items:** [Count]
- **Required Items:** [Count]
- **Items Checked "Yes":** [Count]
- **Items Checked "No":** [Count]
- **Items N/A:** [Count]
- **Conformity Rate:** [Percentage] = (Yes / Required) × 100%

### Readiness Assessment

**Release is ready for CCB approval and distribution:**
- [ ] **YES** — All required items checked "Yes", conformity ≥100%
- [ ] **NO** — Issues must be resolved before proceeding

### Issues to Resolve

[List any items checked "No" that must be addressed]

1. Item #: Issue description
2. Item #: Issue description

---

## Approvals

### Checklist Reviewer

**Name:** ________________________  
**Role:** Release Manager  
**Date:** ________________________  
**Signature:** ________________________

### Quality Assurance Verification

**Name:** ________________________  
**Role:** QA Lead  
**Date:** ________________________  
**Signature:** ________________________

### Configuration Manager Approval

**Name:** ________________________  
**Role:** Configuration Manager  
**Date:** ________________________  
**Signature:** ________________________

---

## Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md)
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md)
- [RELEASE_PACKAGE_MANIFEST.yaml](./RELEASE_PACKAGE_MANIFEST.yaml)
- [RELEASE_NOTES_TEMPLATE.md](./RELEASE_NOTES_TEMPLATE.md)

---

**Notes:**

* "Conditional" items are required only when the stated condition applies
* All "Required" items must be "Yes" for release approval
* Document any N/A justifications in the Evidence/Notes column
* Attach supporting evidence as needed

---

**Revision History**

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial checklist | Configuration Manager |
