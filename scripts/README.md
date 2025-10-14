# Validation Scripts

This directory contains validation scripts for verifying the structural integrity and compliance of various system architectures in the IDEALE repository.

---

## Aircraft Validation Scripts

### validate-aircraft-systems.sh

Validates domain and system-level structure for aircraft systems following TFA (Threading Functional Architecture) rules.

**Validates:**
- Domain existence and structure (15 domains)
- System-level mandatory files (INTEGRATION_VIEW.md, INTERFACE_MATRIX/, SUBSYSTEMS/)
- Domain-level metadata (META.json, domain-config.yaml, README.md)
- Prohibition of PLM/CAx at domain level
- System counts and completeness

**Usage:**
```bash
./scripts/validate-aircraft-systems.sh
```

**Exit Codes:**
- 0: Validation passed (or warnings only)
- 1: Validation failed with errors

**Output:** Color-coded with errors (red), warnings (yellow), success (green), and info (blue)

---

### validate-aircraft-subsystems.sh

Validates subsystem-level structure across all aircraft domains.

**Validates:**
- Subsystem mandatory files (README.md, META.json, inherit.json)
- PLM directory structure
- PLM/CAx directory with all 9 subdirectories (CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP)
- PLM/EBOM_LINKS.md presence
- META.json scope field validation

**Usage:**
```bash
./scripts/validate-aircraft-subsystems.sh
```

**Exit Codes:**
- 0: Validation passed (or warnings only)
- 1: Validation failed with errors

**Metrics Provided:**
- Total subsystems count
- Subsystems with complete PLM structure
- Subsystems with complete CAx structure
- Coverage percentages

---

### validate-aircraft-components.sh

Validates component-level CAx structure and identifies pilot systems.

**Validates:**
- PLM/CAx directory completeness (all 9 subdirectories)
- CAx README.md presence
- Individual CAx subdirectory counts
- Pilot system identification

**Usage:**
```bash
./scripts/validate-aircraft-components.sh
```

**Exit Codes:**
- 0: Validation passed (or warnings only)
- 1: Validation failed with errors

**Special Features:**
- Identifies and reports pilot systems (systems with complete CAx structures)
- Provides completion percentage
- Breaks down CAx subdirectory statistics

---

## Spacecraft Validation Scripts

### validate-spacecraft-systems.sh

Validates spacecraft systems structure for AMPEL360-SPACE-T architecture.

**Validates:**
- SYSTEMS directory existence
- System structure (INTEGRATION_VIEW.md, INTERFACE_MATRIX/, SUBSYSTEMS/)
- Subsystem PLM/CAx structure
- Naming conventions (underscores vs hyphens)
- EBOM_LINKS.md presence

**Usage:**
```bash
./scripts/validate-spacecraft-systems.sh
```

---

## Telescope Validation Scripts

### validate-telescope-systems.sh

Validates telescope systems structure following STA chapters.

**Validates:**
- SYSTEMS directory with STA chapter structure
- System-level files and directories
- EWIS special rules (centralized wiring location)
- Subsystem PLM/CAx structure
- INTERFACE_MATRIX CSV files

**Usage:**
```bash
./scripts/validate-telescope-systems.sh
```

---

## General Structure Validation

### validate-structure.sh

Validates domain integration structure for aircraft TFA architecture.

**Validates:**
- Domain-level structure and policies
- System-level mandatory elements
- Subsystem PLM/CAx structure
- Prohibition of PLM/CAx at domain level
- domain-config.yaml validation rules

**Usage:**
```bash
./scripts/validate-structure.sh
```

---

## Common Validation Rules

All validation scripts follow these common patterns:

### Color Coding

- **Red (✗)**: Errors - critical issues that must be fixed
- **Yellow (⚠)**: Warnings - should be addressed but not blocking
- **Green (✓)**: Success - validation passed
- **Blue (ℹ)**: Info - informational messages

### Exit Codes

- **0**: Validation passed successfully (no errors, warnings allowed)
- **1**: Validation failed (errors found)

### Output Format

Each script provides:
1. Initial validation context
2. Progressive validation steps with real-time feedback
3. Summary statistics
4. Final validation summary with error and warning counts

---

## Integration with CI/CD

These scripts are designed for CI/CD pipeline integration:

### GitLab CI Example

```yaml
aircraft-validation:
  stage: validate
  script:
    - chmod +x scripts/validate-aircraft-*.sh
    - ./scripts/validate-aircraft-systems.sh
    - ./scripts/validate-aircraft-subsystems.sh
    - ./scripts/validate-aircraft-components.sh
  artifacts:
    when: always
    paths:
      - "*.txt"
  allow_failure: false
```

### GitHub Actions Example

```yaml
name: Validate Aircraft Structure
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Aircraft Validations
        run: |
          chmod +x scripts/validate-aircraft-*.sh
          ./scripts/validate-aircraft-systems.sh
          ./scripts/validate-aircraft-subsystems.sh
          ./scripts/validate-aircraft-components.sh
```

---

## Validation Reports

Validation results are documented in domain-specific validation reports:

- **Aircraft:** `02-AIRCRAFT/VALIDATION_REPORT.md`
- **Spacecraft:** (To be created)
- **Telescopes:** (To be created)

---

## Requirements

### System Dependencies

- Bash 4.0 or higher
- `find` command
- `jq` (optional, for JSON validation)
- `grep` command

### File System

Scripts assume execution from repository root:
```bash
cd /path/to/repository
./scripts/validate-*.sh
```

---

## Script Development Guidelines

When creating new validation scripts:

1. **Use consistent error/warning/success functions**
   ```bash
   error() {
     echo -e "${RED}✗ ERROR:${NC} $1"
     ERRORS=$((ERRORS + 1))
   }
   ```

2. **Provide comprehensive summary**
   - Count errors and warnings separately
   - Show statistics for validated elements
   - Use clear exit codes

3. **Enable CI/CD integration**
   - Non-interactive execution
   - Predictable exit codes
   - Machine-parseable output option

4. **Document thoroughly**
   - Script header with description
   - Usage examples
   - Exit code meanings

---

## Troubleshooting

### Script Won't Execute

```bash
chmod +x scripts/validate-*.sh
```

### jq Not Found Warnings

Install jq for enhanced JSON validation:
```bash
# Ubuntu/Debian
apt-get install jq

# macOS
brew install jq

# Or continue without jq (warnings will be shown but not fatal)
```

### Permission Denied

Ensure you have read permissions on all directories being validated.

---

## Contributing

When adding new validation scripts:

1. Follow the existing naming convention: `validate-<domain>-<level>.sh`
2. Update this README with script documentation
3. Add corresponding validation report template
4. Test with CI/CD pipeline before merging
5. Include example output in documentation

---

## See Also

- [Aircraft Validation Report](../02-AIRCRAFT/VALIDATION_REPORT.md)
- [TFA Quick Reference](../02-AIRCRAFT/MODEL_IDENTIFICATION/TFA_QUICK_REFERENCE.md)
- [Automation Guide](../02-AIRCRAFT/MODEL_IDENTIFICATION/AUTOMATION_README.md)
- [Digital Thread Validation](../00-PROGRAM/DIGITAL_THREAD/08-AUTOMATION/VALIDATION_SCRIPTS/README.md)

---

**Last Updated:** 2025-10-14  
**Maintained By:** IDEALE Repository Team
