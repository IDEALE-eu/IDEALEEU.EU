# Numbering Convention

> Location: `CONFIG_MGMT/06-CHANGES/01-POLICY/NUMBERING_CONVENTION.md`  
> Authority: Configuration Manager

## Purpose

Define standardized numbering schemes for change management artifacts to ensure unique identification and traceability.

## Numbering Schemes

### Engineering Change Request (ECR)

**Format:** `ECR-YYYY-####`

**Components:**
- `ECR` — Prefix (Engineering Change Request)
- `YYYY` — Four-digit year of submission
- `####` — Sequential number (0001-9999)

**Examples:**
- `ECR-2025-0001` — First ECR of 2025
- `ECR-2025-0042` — 42nd ECR of 2025
- `ECR-2026-0001` — First ECR of 2026 (counter resets)

**Assignment:**
- Assigned by Configuration Manager upon receipt
- Sequential within calendar year
- Counter resets to 0001 each January 1st
- Retired numbers not reused

**Usage:**
- All change requests, regardless of class
- Retained even if ECR is rejected
- Used in all related documentation and communication

---

### Engineering Change Order (ECO)

**Format:** `ECO-YYYY-####`

**Components:**
- `ECO` — Prefix (Engineering Change Order)
- `YYYY` — Four-digit year of ECO issuance
- `####` — Sequential number (0001-9999)

**Examples:**
- `ECO-2025-0007` — 7th ECO of 2025
- `ECO-2025-0015` — 15th ECO of 2025

**Assignment:**
- Assigned by Configuration Manager when ECR is approved
- Sequential within calendar year
- Independent sequence from ECR numbers
- Counter resets to 0001 each January 1st

**Relationship to ECR:**
- Each ECO references its source ECR
- Multiple ECOs may implement a single ECR (phased implementation)
- One ECO may consolidate multiple related ECRs

**Usage:**
- Implementation authorization
- Baseline update tracking
- Change package identification

---

### Deviation Request

**Format:** `DEV-YYYY-####`

**Components:**
- `DEV` — Prefix (Deviation)
- `YYYY` — Four-digit year of submission
- `####` — Sequential number (0001-9999)

**Examples:**
- `DEV-2025-0003` — Third deviation of 2025
- `DEV-2025-0028` — 28th deviation of 2025

**Assignment:**
- Assigned by Configuration Manager upon receipt
- Sequential within calendar year
- Counter resets to 0001 each January 1st

**Scope:**
- One-time departure from requirements
- Temporary acceptance
- Limited to specific serial numbers or lots
- Production or prototype use

**Usage:**
- Tracked in **[../07-DEVIATIONS/](../07-DEVIATIONS/)**
- May be linked to ECR/ECO if permanent fix developed
- Recorded in as-built configuration

---

### Waiver Request

**Format:** `WAIV-YYYY-####`

**Components:**
- `WAIV` — Prefix (Waiver)
- `YYYY` — Four-digit year of submission
- `####` — Sequential number (0001-9999)

**Examples:**
- `WAIV-2025-0001` — First waiver of 2025
- `WAIV-2025-0009` — Ninth waiver of 2025

**Assignment:**
- Assigned by Configuration Manager upon receipt
- Sequential within calendar year
- Counter resets to 0001 each January 1st

**Scope:**
- Permanent acceptance of non-conformance
- Engineering justification required
- May affect multiple units
- Must not compromise safety or certification

**Usage:**
- Tracked in **[../08-WAIVERS/](../08-WAIVERS/)**
- Requires CCB approval
- May require customer approval
- Recorded in baseline

---

### Change Package

**Format:** `CP-ECO-YYYY-####_vN`

**Components:**
- `CP` — Prefix (Change Package)
- `ECO-YYYY-####` — Associated ECO number
- `_vN` — Version number (v1, v2, etc.)

**Examples:**
- `CP-ECO-2025-0007_v1.zip` — Version 1 of ECO-2025-0007 package
- `CP-ECO-2025-0007_v2.zip` — Revised package (e.g., after verification failure)

**Contents:**
- ECO document (YML)
- Implementation plan
- Verification report
- Updated drawings/specifications
- Test results
- CCB approval documentation
- Traceability matrix
- As-built configuration updates

**Storage:**
- Immutable archive in **[../16-CHANGE_PACKAGES/](../16-CHANGE_PACKAGES/)**
- Retained for program life + 10 years

---

### Material Review Board (MRB) Case

**Format:** `MRB-YYYY-####`

**Components:**
- `MRB` — Prefix (Material Review Board)
- `YYYY` — Four-digit year of submission
- `####` — Sequential number (0001-9999)

**Examples:**
- `MRB-2025-0012` — 12th MRB case of 2025

**Assignment:**
- Assigned by Quality Manager or Configuration Manager
- Sequential within calendar year
- Counter resets to 0001 each January 1st

**Scope:**
- Non-conforming material disposition
- Disposition: Use-As-Is, Rework, Repair, Scrap
- Links to NCR/CAPA system

**Usage:**
- Tracked in **[../09-MRB/DECISIONS/](../09-MRB/DECISIONS/)**
- May generate ECR for permanent fix
- Linked to **[../../QUALITY_QMS/06-NCR_CAPA/](../../QUALITY_QMS/06-NCR_CAPA/)**

---

## Cross-Reference Format

When referencing multiple change artifacts:

**Format:** `TYPE1-YYYY-####, TYPE2-YYYY-####, ...`

**Examples:**
- Related ECRs: `ECR-2025-0012, ECR-2025-0015`
- ECO supersedes: `Supersedes ECO-2024-0087`
- Deviation with fix: `DEV-2025-0003 → ECR-2025-0042 → ECO-2025-0031`

---

## Numbering Registry

All assigned numbers tracked in:
- **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)** — Master register

**Fields:**
- ID (ECR/ECO/DEV/WAIV/MRB number)
- Title
- Classification (Class I/II/III)
- Status (Draft, Submitted, Approved, Rejected, Closed)
- Owner
- Submission date
- Approval date
- Related numbers

---

## Year-End Procedure

At end of calendar year (December 31):
1. Close all open number series
2. Archive year's change register
3. Reset counters to 0001 for new year
4. Update numbering registry

---

## Special Cases

### Emergency Changes
- Use standard numbering
- Mark as `EMERGENCY` in status field
- No special prefix

### Customer-Directed Changes
- Use standard numbering
- Mark as `CUSTOMER` in source field
- Reference customer change request number in notes

### Regulatory Changes
- Use standard numbering
- Mark as `REGULATORY` in source field
- Reference regulatory directive (e.g., AD, SB)

### Batch ECOs
- Single ECO may implement multiple related ECRs
- List all source ECRs in ECO documentation
- Example: `ECO-2025-0042 implements ECR-2025-0103, ECR-2025-0107, ECR-2025-0112`

---

## Number Retirement

Numbers are never reused:
- Rejected ECRs retain their number
- Cancelled ECOs retain their number
- Status field indicates final disposition
- Audit trail preserved

---

## Related Documents

- **[CHANGE_POLICY.md](./CHANGE_POLICY.md)** — Change policy overview
- **[CLASSIFICATION.md](./CLASSIFICATION.md)** — Classification criteria
- **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)** — Master change register
- **[../02-WORKFLOW/ECR_WORKFLOW.md](../02-WORKFLOW/ECR_WORKFLOW.md)** — ECR workflow
- **[../02-WORKFLOW/ECO_WORKFLOW.md](../02-WORKFLOW/ECO_WORKFLOW.md)** — ECO workflow

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
