# CHECKS — Assembly Validation Checks

## Purpose

This directory contains validation check results and documentation for the top-level assembly.

## Check Types

### Quality Checks
- **[INTERFERENCE/](./INTERFERENCE/)** — Interference and clearance checks
- **[MASS_PROPERTIES/](./MASS_PROPERTIES/)** — Mass, CG, and inertia calculations
- **[VALIDATION/](./VALIDATION/)** — General model validation results

## Check Frequency

### During Design
- **Interference**: After each major change
- **Mass properties**: Weekly or after significant changes
- **Validation**: Before each design review

### Before Release
- [ ] All interferences resolved
- [ ] Mass properties within targets
- [ ] Model validation passed
- [ ] Documentation complete
- [ ] All checks archived

## Check Tools

### Native CAD Tools
- Assembly interference detection
- Mass properties calculator
- Model validation utilities

### Third-Party Tools
- Digital mock-up (DMU) software
- Specialized interference checkers
- Mass properties analysis tools

## Documentation

Each check should document:
- **Date**: When check was performed
- **Version**: Model version checked
- **Tool**: Software used for check
- **Results**: Pass/fail and details
- **Issues**: Problems found
- **Actions**: Corrective actions taken

## File Formats

- `.pdf` — Check reports
- `.xlsx` — Tabular results
- `.txt` / `.csv` — Data exports
- `.html` — Automated check reports

## Naming Convention

```
53-10_CHECK_<type>_<date>_<version>.<ext>
```

Examples:
- `53-10_CHECK_INTERFERENCE_2024-01-15_v01.pdf`
- `53-10_CHECK_MASS-PROPS_2024-01-15_v01.xlsx`
- `53-10_CHECK_VALIDATION_2024-01-15_v01.html`

## Quality Standards

Follow:
- **ATA iSpec 2200**: Technical documentation
- **AS9100**: Quality management
- **Company procedures**: Internal validation standards

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Source assembly models
- **Documentation**: [`../DOCS/`](../DOCS/) — Supporting documentation
