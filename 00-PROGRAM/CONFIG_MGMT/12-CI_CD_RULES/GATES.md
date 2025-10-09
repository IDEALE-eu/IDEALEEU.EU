# CI/CD Quality Gates

## Overview

This document defines the quality gates and automated checks that must pass before code and documentation can be merged into protected branches. Quality gates ensure consistency, correctness, and compliance with program standards.

## Purpose

Quality gates:
- Enforce configuration management standards
- Prevent errors from reaching protected branches
- Automate compliance checking
- Maintain baseline integrity
- Support continuous integration/deployment
- Reduce manual review burden

## Gate Levels

### Gate 1: Pre-Commit Checks
Run locally before committing

### Gate 2: Pull Request Checks
Run when PR is created or updated

### Gate 3: Pre-Merge Checks
Run before merge to protected branch

### Gate 4: Post-Merge Checks
Run after merge, trigger alerts if fail

## Gate Definitions

### Gate 1: Pre-Commit Checks

**Trigger:** Git pre-commit hook  
**Required:** Optional but recommended  
**Failure Action:** Block commit (local only)

#### Checks:
- [ ] **File size check** - No files >10MB (prevent binary commits)
- [ ] **Trailing whitespace** - Remove trailing whitespace
- [ ] **File endings** - Consistent line endings (LF)
- [ ] **Merge markers** - No unresolved merge conflicts
- [ ] **Debug statements** - No console.log, print(), TODO/FIXME in critical code
- [ ] **Secrets detection** - No API keys, passwords, credentials

**Tools:**
- pre-commit framework
- git-secrets
- detect-secrets

**Setup:**
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Gate 2: Pull Request Checks

**Trigger:** PR creation or update  
**Required:** Yes  
**Failure Action:** Block merge

#### 2.1 Markdown Linting

**Purpose:** Ensure documentation quality and consistency

**Checks:**
- [ ] Markdown syntax valid
- [ ] Headings properly structured
- [ ] Links not broken
- [ ] No trailing spaces
- [ ] Consistent list formatting
- [ ] Code blocks have language specified

**Tools:**
- markdownlint
- markdown-link-check

**Config:** `.markdownlint.json`
```json
{
  "default": true,
  "MD013": false,
  "MD033": false,
  "MD041": false
}
```

**CI Check:**
```yaml
- name: Lint Markdown
  run: |
    npm install -g markdownlint-cli
    markdownlint '**/*.md' --ignore node_modules
```

#### 2.2 File Naming Conventions

**Purpose:** Enforce consistent naming

**Checks:**
- [ ] Part numbers match format (02-PART_NUMBERING.md)
- [ ] ECR/ECO numbers match format
- [ ] File names alphanumeric with hyphens/underscores only
- [ ] No spaces in file names
- [ ] Consistent case (prefer lowercase or UPPERCASE, not Mixed)

**Custom Script:** `scripts/validate-file-names.sh`

#### 2.3 Directory Structure Validation

**Purpose:** Maintain proper organization

**Checks:**
- [ ] No orphan files (files not in proper directory)
- [ ] Required directories present
- [ ] README.md present in each major directory
- [ ] Baseline structure matches requirements
- [ ] **03-SPACECRAFT/DOMAIN_INTEGRATION** structure compliance
  - [ ] SYSTEMS directories present with ATA-XX_NAME pattern
  - [ ] Each system has INTEGRATION_VIEW.md
  - [ ] Each system has INTERFACE_MATRIX/*.csv
  - [ ] PLM artifacts only under SUBSYSTEMS/*/PLM/CAx/
  - [ ] Software with host LRU placement
  - [ ] EWIS in ATA-92 (physical wiring)

**Custom Script:** `00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/SCRIPTS/validate-structure.sh`

#### 2.4 CSV/YAML Validation

**Purpose:** Ensure data file correctness

**Checks:**
- [ ] CSV files have proper headers
- [ ] CSV data rows match header count
- [ ] YAML files valid syntax
- [ ] Required fields present
- [ ] No duplicate part numbers

**Tools:**
- csvlint
- yamllint

**CSV Validation Example:**
```bash
# Validate ITEMS.csv
csvlint 00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/ITEMS.csv
```

**YAML Validation:**
```yaml
- name: Validate YAML
  run: |
    pip install yamllint
    yamllint -c .yamllint.yml .
```

#### 2.5 Part Number Validation

**Purpose:** Ensure part numbers follow scheme

**Checks:**
- [ ] Part number format: [PROGRAM]-[CATEGORY]-[SEQUENCE]-[VARIANT]
- [ ] Program code valid (IDEALE, ACFT, SCFT, GSE, TEST)
- [ ] Category code valid (per 02-PART_NUMBERING.md)
- [ ] Sequence is 5-digit number
- [ ] No duplicate part numbers

**Custom Script:** `scripts/validate-part-numbers.py`

#### 2.6 Traceability Check

**Purpose:** Maintain requirements traceability

**Checks:**
- [ ] All items in ITEMS.csv traced to requirements (if critical)
- [ ] All ECRs referenced in changes
- [ ] No orphan requirements
- [ ] Traceability matrix complete

**Custom Script:** `scripts/check-traceability.py`

#### 2.7 Baseline Integrity

**Purpose:** Protect established baselines

**Checks:**
- [ ] No modifications to baseline directories without ECR
- [ ] Baseline changes have CCB approval reference
- [ ] Baseline branch protection not violated

**Custom Script:** `scripts/check-baseline-integrity.sh`

#### 2.8 Change Control

**Purpose:** Ensure proper change management

**Checks:**
- [ ] ECR branch references valid ECR number
- [ ] ECR exists in system
- [ ] ECR status is approved (for merge to main)
- [ ] Commit messages reference ECR/requirements

**Custom Script:** `scripts/validate-change-control.py`

### Gate 3: Pre-Merge Checks

**Trigger:** Before merge to main or develop  
**Required:** Yes  
**Failure Action:** Block merge

#### 3.1 Review Approval

**Main Branch:**
- [ ] Minimum 2 approvals
- [ ] At least 1 CCB member approval
- [ ] Configuration Manager approval

**Develop Branch:**
- [ ] Minimum 1 approval
- [ ] Code owner approval

#### 3.2 Status Checks Pass

**Required Checks:**
- [ ] All Gate 2 checks pass
- [ ] No merge conflicts
- [ ] Branch up to date with target

#### 3.3 Documentation Complete

**Checks:**
- [ ] PR description filled out
- [ ] Related issues/ECRs linked
- [ ] Checklist items completed
- [ ] Breaking changes documented (if any)

#### 3.4 Configuration Management Approval

**For Main Branch:**
- [ ] CCB meeting minutes reference
- [ ] CM approval documented
- [ ] Baseline impact assessed

### Gate 4: Post-Merge Checks

**Trigger:** After merge to main or develop  
**Required:** Monitoring only  
**Failure Action:** Alert, rollback if critical

#### 4.1 Build Verification

**Checks:**
- [ ] Documentation builds successfully
- [ ] No broken links introduced
- [ ] All referenced files exist

#### 4.2 Notification

**Actions:**
- Send merge notification to stakeholders
- Update CM database
- Trigger documentation rebuild
- Update traceability reports

## CI/CD Pipeline Configuration

### GitHub Actions Workflow

**File:** `.github/workflows/quality-gates.yml`

```yaml
name: Quality Gates

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  gate-2-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Markdown Linting
        run: |
          npm install -g markdownlint-cli
          markdownlint '**/*.md' --ignore node_modules
      
      - name: YAML Validation
        run: |
          pip install yamllint
          yamllint -c .yamllint.yml .
      
      - name: CSV Validation
        run: |
          npm install -g csvlint
          find . -name "*.csv" -exec csvlint {} \;
      
      - name: File Naming Check
        run: ./scripts/validate-file-names.sh
      
      - name: Directory Structure Check
        run: ./00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/SCRIPTS/validate-structure.sh
      
      - name: Part Number Validation
        run: python scripts/validate-part-numbers.py
      
      - name: Traceability Check
        run: python scripts/check-traceability.py
      
      - name: Baseline Integrity
        run: ./scripts/check-baseline-integrity.sh
      
      - name: Change Control Validation
        run: python scripts/validate-change-control.py
```

## Gate Overrides

### When to Override

Only in exceptional circumstances:
- Emergency hotfixes (with CCB approval)
- False positive from automated check
- Tool malfunction
- CCB authorized exception

### Override Process

1. Document reason for override
2. Obtain CCB Chair approval
3. Create waiver record
4. Apply override
5. Create follow-up action item

**Override Command:**
```bash
# Use with extreme caution
git push --no-verify origin branch-name
```

## Metrics and Monitoring

### Gate Metrics

Track and report:
- Gate success rate by type
- Average gate execution time
- Most common failures
- Override frequency and reasons
- Trends over time

### Alerts

Configure alerts for:
- Gate failures on main branch
- High failure rate on develop
- Repeated failures of same check
- Unauthorized overrides

## Tool Configuration Files

### .markdownlint.json
```json
{
  "default": true,
  "MD013": false,
  "MD033": { "allowed_elements": ["br", "table", "tr", "td", "th"] }
}
```

### .yamllint.yml
```yaml
extends: default
rules:
  line-length:
    max: 120
  indentation:
    spaces: 2
```

### .editorconfig
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
max_line_length = off
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_style = space
indent_size = 2
```

## Local Development Setup

### Prerequisites

```bash
# Install Node.js tools
npm install -g markdownlint-cli csvlint

# Install Python tools
pip install yamllint pre-commit

# Install pre-commit hooks
pre-commit install
```

### Running Checks Locally

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific check
markdownlint '**/*.md'
yamllint .
csvlint 08-ITEM_MASTER/ITEMS.csv

# Run custom validation scripts
./scripts/validate-file-names.sh
python scripts/validate-part-numbers.py
```

## Troubleshooting

### Common Issues

**Issue:** Markdown linting fails
- **Fix:** Run `markdownlint --fix` to auto-correct

**Issue:** YAML syntax error
- **Fix:** Use YAML validator to identify line

**Issue:** CSV validation fails
- **Fix:** Check header count matches data rows

**Issue:** Part number invalid
- **Fix:** Verify format matches 02-PART_NUMBERING.md

## Continuous Improvement

- Monthly review of gate effectiveness
- Quarterly update of rules and checks
- Incorporate lessons learned
- Add new checks as needed
- Remove redundant or ineffective checks

---

**Document Owner:** Configuration Management & DevOps  
**Maintained By:** DevOps Team  
**Review Frequency:** Monthly
