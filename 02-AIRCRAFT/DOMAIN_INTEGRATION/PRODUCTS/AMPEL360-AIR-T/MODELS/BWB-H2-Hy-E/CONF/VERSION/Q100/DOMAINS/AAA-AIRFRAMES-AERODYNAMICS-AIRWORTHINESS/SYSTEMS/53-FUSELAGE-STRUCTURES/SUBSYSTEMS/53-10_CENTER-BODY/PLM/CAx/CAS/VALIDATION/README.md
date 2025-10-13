# VALIDATION — S1000D Validation Infrastructure

## Purpose

This directory contains validation tools, schemas, and reports for ensuring AMPEL360 AIR-T S1000D Data Modules comply with:
- XML Schema (XSD) validation
- Schematron business rules
- BREX (Business Rules Exchange) validation
- Link and reference checking

## Directory Structure

```
VALIDATION/
├── README.md           # This file
├── XSD/                # XML Schema definitions
├── Schematron/         # Schematron validation rules
├── BREX/               # BREX validation scripts and reports
│   └── validate_brex.py
└── Reports/            # Validation reports and logs
```

## Validation Pipeline

Data Modules must pass through this validation pipeline before release:

```
1. XSD Validation (Schema)
   ↓
2. Schematron Validation (Business Rules)
   ↓
3. BREX Validation (120 AMPEL360 Rules)
   ↓
4. Link Checking (Internal/External References)
   ↓
5. DMRL Gating (Requirements Check)
   ↓
6. QA Review
   ↓
7. Publication
```

## XSD Validation

### S1000D Issue 6.0 Schemas

XML Schema validation ensures structural correctness according to S1000D Issue 6.0 specification.

**Schemas required:**
- Data Module schema
- Publication Module schema
- DMRL schema
- ACT schema
- BREX schema

**Download schemas from:**
- http://www.s1000d.org/

**Validation command:**
```bash
xmllint --noout --schema s1000d_6-0.xsd DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```

## Schematron Validation

Schematron rules enforce business logic and content constraints beyond XSD.

**Example rules:**
- Enforce sequential step numbering
- Validate cross-references
- Check for required metadata
- Enforce naming conventions

**Validation command:**
```bash
schematron validate --schematron rules.sch --input DM.xml
```

## BREX Validation

### Overview

The **BREX validator** checks Data Modules against **120 AMPEL360-specific rules** defined in:
```
DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml
```

See [`../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv`](../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv) for complete rule listing.

### Rule Categories

1. **IDS & Metadata (001-020)**: Core metadata requirements
2. **DMC & Ownership (021-030)**: Data Module Code standards
3. **Language & Localization (031-040)**: Language and style
4. **Security & QA (041-050)**: Security and quality assurance
5. **Applicability & ACT (051-060)**: Applicability rules
6. **Procedural Structure (061-075)**: Procedural content
7. **Fault Isolation (076-085)**: Fault isolation procedures
8. **Illustrations & Graphics (086-095)**: Graphics requirements
9. **IPD & Logistics (096-105)**: Illustrated Parts Data
10. **References & Linking (106-110)**: Cross-references
11. **Controlled Language & Domain Safety (111-120)**: ASD-STE-100 and safety

### Severity Levels

- **ERROR**: Blocking issue; DM cannot be released
- **WARN**: Advisory issue; should be addressed but not blocking

### Usage

**Validate single Data Module:**
```bash
python BREX/validate_brex.py ../CSDB/DMs/Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```

**Validate directory:**
```bash
python BREX/validate_brex.py ../CSDB/DMs/Procedural/
```

**With BREX file:**
```bash
python BREX/validate_brex.py --brex ../CSDB/BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml ../CSDB/DMs/
```

### Output Example

```
Validating: DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
  ✓ PASS: All BREX rules passed

Validating: DMC-AMP360-AAA-53-10-10-00A-310A-P_en-US_001-00.xml
  [ERROR] [AMP360-BREX-119] UTCS anchor required in IDS/extension.
  [WARN] [AMP360-BREX-008] DM should contain <originator>.

======================================================================
VALIDATION SUMMARY
======================================================================
Files validated: 2
Total errors:    1
Total warnings:  1

✗ VALIDATION FAILED (1 blocking error(s))
```

### Exit Codes

- `0`: Validation passed (no errors)
- `1`: Validation failed (one or more errors)

## Link Checking

Validates internal and external references:
- Internal references (`internalRefId`)
- External references (`xlink:href`)
- Cross-DM references (`dmRef`)
- ICN references

**Command:**
```bash
python tools/check_links.py ../CSDB/DMs/
```

## DMRL Gating

Verifies that all required Data Modules exist and are up-to-date:
- Check against DMRL
- Verify issue numbers
- Ensure required DMs present

**Command:**
```bash
python tools/check_dmrl.py ../CSDB/DMRL/DMRL_53-10.xml ../CSDB/DMs/
```

## UTCS Validation

Validates UTCS (Universal Traceability and Configuration System) anchors:
- Presence (BREX-119)
- Format validation
- Uniqueness checking
- Mirror to central registry

**Command:**
```bash
python tools/validate_utcs.py ../CSDB/DMs/
```

**Format:**
```
UTCS-<ModelIdent>-<SysDiff>-<SysCode>-<SubSysCode>-DMC-<SeqNum>
```

**Example:**
```xml
<extension>
  <utcs id="UTCS-AMP360-AAA-53-10-DMC-001"/>
</extension>
```

## CI/CD Integration

### GitHub Actions Workflow

```yaml
name: Validate S1000D Content

on:
  pull_request:
    paths:
      - '**/CAS/CSDB/**/*.xml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install dependencies
        run: |
          pip install lxml
          sudo apt-get install -y libxml2-utils
      
      - name: XSD Validation
        run: |
          xmllint --noout --schema schemas/s1000d_6-0.xsd CSDB/DMs/**/*.xml
      
      - name: BREX Validation
        run: |
          python VALIDATION/BREX/validate_brex.py CSDB/DMs/
      
      - name: Link Checking
        run: |
          python tools/check_links.py CSDB/DMs/
      
      - name: UTCS Validation
        run: |
          python tools/validate_utcs.py CSDB/DMs/
```

### Pre-commit Hooks

Install pre-commit hooks to validate before committing:

```bash
# .git/hooks/pre-commit
#!/bin/bash
echo "Running BREX validation..."
python VALIDATION/BREX/validate_brex.py CSDB/DMs/
if [ $? -ne 0 ]; then
    echo "BREX validation failed. Commit aborted."
    exit 1
fi
```

## Validation Reports

Reports are saved to `Reports/` directory:

```
Reports/
├── validation-2025-10-10-001.log
├── brex-errors-2025-10-10.csv
├── link-check-2025-10-10.html
└── utcs-audit-2025-10-10.json
```

### Report Formats

- **Log files**: Text log of validation run
- **CSV files**: Tabular error/warning reports
- **HTML files**: Interactive reports with charts
- **JSON files**: Machine-readable audit trails

## Best Practices

### Pre-validation Checklist

Before running validation:
- [ ] File named according to DMC convention
- [ ] XML well-formed (no syntax errors)
- [ ] All required metadata present
- [ ] UTCS anchor included
- [ ] Security classification set
- [ ] QA fields completed

### Fixing Common Errors

#### Missing UTCS Anchor (BREX-119)
**Error:**
```
[AMP360-BREX-119] [ERROR] UTCS anchor required in IDS/extension.
```

**Fix:**
```xml
<dmIdent>
  <!-- dmCode, language, issueInfo -->
  <extension>
    <utcs id="UTCS-AMP360-AAA-53-10-DMC-001"/>
  </extension>
</dmIdent>
```

#### Wrong Model Identifier (BREX-021)
**Error:**
```
[AMP360-BREX-021] [ERROR] @modelIdentCode must be AMP360.
```

**Fix:**
```xml
<dmCode modelIdentCode="AMP360" .../>
```

#### Safety in Notes (BREX-039)
**Error:**
```
[AMP360-BREX-039] [ERROR] Do not put safety messages inside <note>.
```

**Fix:** Move `<warning>` or `<caution>` outside of `<note>` element.

## Tools and Dependencies

### Required Python Packages
```bash
pip install lxml jsonschema
```

### Required System Tools
```bash
sudo apt-get install libxml2-utils  # xmllint
```

### Optional Tools
- Oxygen XML Editor (commercial, includes BREX/Schematron support)
- Arbortext Editor (commercial S1000D authoring tool)

## Support

For validation issues:
- **BREX Rules**: validation@ampel360.eu
- **Schema Issues**: tech-pubs@ampel360.eu
- **Tool Support**: automation@ampel360.eu

## Related Documentation

- **BREX Rules Index**: [`../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv`](../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv)
- **Style Guide**: [`../GUIDES/StyleGuide.md`](../GUIDES/StyleGuide.md)
- **Language Guide**: [`../GUIDES/Language.md`](../GUIDES/Language.md)
- **Conventions**: [`../GUIDES/Conventions.md`](../GUIDES/Conventions.md)

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-10  
**Owner**: Technical Publications Office  
**Review Cycle**: With S1000D updates
