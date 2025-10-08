# Pre-Merge Validation Gates

> Location: `CONFIG_MGMT/06-CHANGES/13-AUTOMATION/GATES.md`

## Purpose

Define automated validation checks that must pass before merging changes.

## Validation Gates

### 1. Schema Validation
- ECR/ECO YAML files validate against schema
- CSV files have required columns
- JSON files are well-formed

### 2. Link Validation
- All cross-references resolve
- Baseline links are valid
- ICD references exist

### 3. Traceability Validation
- Requirements mapped to changes
- Changes mapped to baselines
- No orphaned change requests

### 4. Signature Validation
- Required approvals present
- Approval dates valid
- CCB minutes reference changes

### 5. Completeness Checks
- All required fields populated
- Supporting documentation present
- Impact assessments complete

## CI/CD Integration

See **[CI_HOOKS.md](./CI_HOOKS.md)** for CI/CD pipeline integration.
