# Validation and Management Scripts

This directory contains automation scripts for managing and validating the IDEALE-EU repository structure.

## Aircraft Validation Scripts

### validate-aircraft-systems.sh
Validates the aircraft systems-level structure for the AMPEL360-AIR-T model.

**Purpose**: Ensures all aircraft domains, ATA chapters, and systems follow the proper directory structure with required files and subdirectories.

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-aircraft-systems.sh
```

**Checks**:
- Domain directories exist and have SYSTEMS subdirectories
- Systems have INTEGRATION_VIEW.md, README.md, INTERFACE_MATRIX, and SUBSYSTEMS
- ATA naming conventions (hyphens in system names)
- System and subsystem counts

**Exit Codes**:
- `0`: Validation passed (warnings allowed)
- `1`: Validation failed with errors

### validate-aircraft-subsystems.sh
Validates the aircraft subsystems-level structure including PLM and CAx directories.

**Purpose**: Ensures subsystems have proper PLM (Product Lifecycle Management) structure with CAx tool integration directories.

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-aircraft-subsystems.sh
```

**Checks**:
- PLM directory structure
- PLM/CAx subdirectories (CAD, CAE, CAO, CAM, CAI, CAV, CAS, CMP)
- EBOM_LINKS.md files
- TRACE directories
- PLM/CAx/EBOM coverage percentages

**Exit Codes**:
- `0`: Validation passed (warnings allowed)
- `1`: Validation failed with errors

### validate-aircraft-components.sh
Validates the aircraft components-level structure (TFA - Technical Functional Architecture).

**Purpose**: Ensures components have proper configuration management structure with subproducts, subjects, and artifacts.

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-aircraft-components.sh
```

**Checks**:
- CONF/BASELINE/COMPONENTS directory structure
- Component definitions
- SUBPRODUCT and SUBJECT structures
- Artifact management capability

**Exit Codes**:
- `0`: Validation passed (warnings allowed)
- `1`: Validation failed with errors

**Note**: As of 2025-10-14, no component structure exists yet. See the [Aircraft Corrective Action Plan](../02-AIRCRAFT/CORRECTIVE_ACTION_PLAN.md) for implementation guidance.

## Spacecraft Validation Scripts

### validate-spacecraft-systems.sh
Validates the spacecraft systems structure for AMPEL360-SPACE-T.

**Purpose**: Similar to aircraft validation but for spacecraft systems with different naming conventions (underscores instead of hyphens).

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-spacecraft-systems.sh
```

## Telescope Validation Scripts

### validate-telescope-systems.sh
Validates the telescope systems structure for AMPEL360-TELESCOPE-T.

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-telescope-systems.sh
```

## General Validation Scripts

### validate-structure.sh
General repository structure validation.

**Usage**:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-structure.sh
```

## Creation Scripts

### create-domains.sh
Script to create new domain structures.

### create-probe-systems.sh
Script to create probe system structures.

### create-satellite-domains.sh
Script to create satellite domain structures.

### create-telescope-systems.sh
Script to create telescope system structures.

## Integration with CI/CD

These validation scripts can be integrated into GitHub Actions workflows for continuous validation:

```yaml
# Example .github/workflows/validate.yml
name: Structure Validation

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate-aircraft:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate Aircraft Systems
        run: ./scripts/validate-aircraft-systems.sh
      - name: Validate Aircraft Subsystems
        run: ./scripts/validate-aircraft-subsystems.sh
      - name: Validate Aircraft Components
        run: ./scripts/validate-aircraft-components.sh
```

## Troubleshooting

### Permission Denied
If you get "Permission denied" errors, make scripts executable:
```bash
chmod +x scripts/*.sh
```

### Path Issues
Always run scripts from the repository root directory:
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-aircraft-systems.sh
```

### Exit Code 1 with Warnings
Some scripts exit with code 0 even with warnings. Only errors cause exit code 1.

## Contributing

When adding new validation scripts:
1. Follow the existing naming convention: `validate-{domain}-{level}.sh`
2. Use consistent color codes (RED for errors, YELLOW for warnings, GREEN for success)
3. Include proper error counting and summary reporting
4. Handle edge cases (empty directories, missing files, etc.)
5. Use `set -euo pipefail` for robust error handling
6. Avoid `((VAR++))` which returns 0 on first increment; use `VAR=$((VAR + 1))` instead
7. Document the script in this README

## References

- [Aircraft Corrective Action Plan](../02-AIRCRAFT/CORRECTIVE_ACTION_PLAN.md)
- [ATA iSpec 2200](https://www.ata.org) - Aviation technical publication standard
- [S1000D](http://www.s1000d.org) - International technical publication specification
