# QC — Quality Control & Validation Logs

## Purpose

This directory contains **quality control records, validation logs, and quality assurance documentation** for S1000D Data Modules in the 21-10 Radiators & Heat Exchangers subsystem.

## Contents

### Validation Reports
- XML schema validation results
- BREX validation reports
- Schematron check results
- Cross-reference validation
- Link integrity checks

### Quality Checks
- Technical accuracy reviews
- Content completeness checks
- Illustration quality reviews
- Language compliance (ASD-STE-100)
- Metadata verification

### Review Records
- Technical review documentation
- Editorial review records
- SME (Subject Matter Expert) sign-off
- Quality assurance approval
- Configuration control records

### Test Reports
- Transformation test results
- IETP viewer compatibility tests
- PDF rendering validation
- Cross-browser testing results

## Directory Structure

```
qc/
├── validation/             # Automated validation logs
│   ├── schema/            # XML schema validation
│   ├── brex/              # BREX rule validation
│   └── schematron/        # Schematron check results
├── reviews/               # Manual review records
│   ├── technical/         # Technical reviews
│   ├── editorial/         # Editorial reviews
│   └── qa/                # QA approvals
├── testing/               # Test results
│   ├── transformation/    # XSL transformation tests
│   └── rendering/         # Display/print tests
└── reports/               # Summary reports
    ├── weekly/            # Weekly QC summaries
    └── release/           # Release quality reports
```

## Validation Process

### 1. Automated Validation

**XML Schema Validation**
- Validates against S1000D 6.0 XSD schemas
- Checks structural correctness
- Verifies required elements
- Logs: `validation/schema/DM-{DMC}-validation.log`

**BREX Validation**
- Applies business rules from BREX DM
- Checks project-specific constraints
- Validates metadata requirements
- Logs: `validation/brex/DM-{DMC}-brex.log`

**Schematron Validation**
- Content quality checks
- Cross-reference validation
- Nomenclature compliance
- Logs: `validation/schematron/DM-{DMC}-schematron.log`

### 2. Manual Review

**Technical Review**
- Content accuracy verification
- Procedural correctness
- Technical completeness
- Safety information adequacy
- Records: `reviews/technical/DM-{DMC}-tech-review.pdf`

**Editorial Review**
- ASD-STE-100 compliance
- Grammar and style
- Consistency with other DMs
- Terminology standardization
- Records: `reviews/editorial/DM-{DMC}-edit-review.pdf`

### 3. Quality Assurance

**QA Approval**
- Final quality gate
- Release authorization
- Configuration control
- Records: `reviews/qa/DM-{DMC}-qa-approval.pdf`

## Log File Naming

```
DM-{DMC}-{check-type}-{date}.log
```

Example:
```
DM-AMPEL360-2110-00-00-00-00A-000A-A-schema-20251011.log
DM-AMPEL360-2110-00-00-00-00A-000A-A-brex-20251011.log
```

## Quality Metrics

Track and report:
- **Validation pass rate**: Percentage passing automated checks
- **First-time quality**: DMs passing all checks on first submission
- **Review cycle time**: Days from submission to approval
- **Error types**: Common validation failures
- **Revision frequency**: Number of revisions per DM

## Validation Criteria

### Must Pass (Blocking)
- ✅ XML well-formed
- ✅ Schema valid
- ✅ BREX compliant
- ✅ No broken cross-references
- ✅ All ICNs exist

### Should Pass (Non-blocking)
- ⚠️ ASD-STE-100 compliance
- ⚠️ Style consistency
- ⚠️ Naming conventions
- ⚠️ Metadata completeness

## Automated Validation Script

Example validation workflow:
```bash
#!/bin/bash
# validate_dm.sh - Validate a Data Module

DM_FILE=$1
DMC=$(basename "$DM_FILE" .xml)
DATE=$(date +%Y%m%d)

# Schema validation
xmllint --schema res/xsd/s1000d-6.0/dmodule.xsd \
        --noout "$DM_FILE" \
        2> "qc/validation/schema/${DMC}-schema-${DATE}.log"

# BREX validation
xmllint --schematron res/schematron/brex-rules.sch \
        "$DM_FILE" \
        > "qc/validation/brex/${DMC}-brex-${DATE}.log"

# Generate summary report
python scripts/generate_qc_report.py "$DM_FILE" \
       > "qc/reports/${DMC}-summary-${DATE}.txt"
```

## Review Checklist

Before QA approval:
- [ ] Schema validation passed
- [ ] BREX validation passed
- [ ] Schematron checks passed
- [ ] Technical review completed
- [ ] Editorial review completed
- [ ] All illustrations present
- [ ] Cross-references valid
- [ ] Metadata complete
- [ ] Security classification assigned
- [ ] Applicability defined

## Reporting

### Weekly QC Summary
- Total DMs validated
- Validation pass/fail rates
- Common error types
- Review cycle times
- Backlog status

### Release Quality Report
- All DMs included in release
- Validation status summary
- Outstanding issues
- Known limitations
- Release recommendation

## Issue Tracking

Log validation failures:
- **Issue ID**: Unique identifier
- **DM affected**: Data Module Code
- **Severity**: Critical/Major/Minor
- **Description**: Error description
- **Action**: Corrective action required
- **Status**: Open/In Progress/Resolved

## Related Directories

- **[../../dm/](../../dm/)** — Data Modules to validate
- **[../../brex/](../../brex/)** — BREX validation rules
- **[../../res/](../../res/)** — Validation schemas and rules

---

**Last Updated**: 2025-10-11
