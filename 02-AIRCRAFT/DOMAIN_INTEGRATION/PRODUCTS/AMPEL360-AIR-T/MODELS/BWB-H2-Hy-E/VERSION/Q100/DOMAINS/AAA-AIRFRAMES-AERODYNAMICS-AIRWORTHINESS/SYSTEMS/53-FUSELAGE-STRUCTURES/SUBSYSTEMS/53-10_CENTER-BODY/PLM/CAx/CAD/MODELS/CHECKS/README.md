# CHECKS — Model Validation and Quality Checks

## Purpose

This directory contains quality check results, validation reports, and verification data for 53-10 Center Body CAD models. Regular checks ensure model quality, accuracy, and compliance with design requirements.

## Organization

Check results are organized by check type:

- **INTERFERENCE/** — Interference and clearance check results
- **MASS_PROPERTIES/** — Mass, center of gravity, and inertia calculations

## Naming Convention

Use the following pattern for check result files:
```
53-10_CHECK_<TYPE>_<MODEL-ID>_<DATE>_v<VERSION>.<ext>
```

Examples:
- `53-10_CHECK_INTERFERENCE_ASSY-001_20240115_v01.pdf`
- `53-10_CHECK_MASS_PROPS_FRAME-FR001_20240120_v01.csv`
- `53-10_CHECK_CLEARANCE_DOOR-SURR_20240125_v02.html`

## INTERFERENCE Directory

Contains interference check results including:
- **Global interference**: Full assembly clash detection
- **Local clearances**: Minimum gap measurements
- **Dynamic clearances**: Movement envelope checks
- **Assembly clearances**: Installation path verification
- **Tool access**: Maintenance accessibility checks

Check outputs:
- Interference reports (PDF, HTML)
- Clearance matrices (CSV, Excel)
- Visual highlights (screenshots, animations)
- Resolution tracking (issue logs)

## MASS_PROPERTIES Directory

Contains mass property calculations including:
- **Component mass**: Individual part weights
- **Assembly mass**: Subassembly and total weights
- **Center of gravity**: CG location in defined coordinate systems
- **Moments of inertia**: Ixx, Iyy, Izz, Ixy, Ixz, Iyz
- **Mass tracking**: Weight vs. allocation

Calculation outputs:
- Mass property reports (PDF)
- Mass property tables (CSV, Excel)
- CG travel envelopes
- Weight tracking dashboards
- Material breakdown summaries

## Check Frequency

Run checks:
- **Before release**: All models must pass checks before release
- **After major changes**: Re-check after significant design updates
- **Weekly**: Routine checks on active design work
- **On demand**: Ad-hoc checks for specific investigations

## Check Criteria

### Interference Checks
Pass criteria:
- Zero hard interferences between components
- Minimum clearances per design rules met
- Assembly path clearances verified
- Tool access provisions confirmed

### Mass Properties
Accuracy requirements:
- Part mass within ±0.5% of actual
- Assembly mass rollup verified
- CG location within ±5mm
- Material densities from approved specifications

## Automation

Where possible, automate checks:
- Batch interference checking
- Automated mass property extraction
- Scheduled check runs
- Automated report generation
- Issue tracking integration

## Issue Resolution

When checks fail:
1. Document the issue with screenshots/data
2. Create issue tracker entry
3. Assign to responsible designer
4. Implement corrective action
5. Re-run check to verify resolution
6. Update model metadata

## Related Documentation

- **Design rules**: [`../CONFIG/DESIGN_RULES/`](../CONFIG/DESIGN_RULES/)
- **Quality standards**: [`../../../../../../../../00-PROGRAM/QUALITY/`](../../../../../../../../00-PROGRAM/QUALITY/)
- **Models**: [`../PARTS/`](../PARTS/) and [`../SUBCOMPONENTS/`](../SUBCOMPONENTS/)
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)

## Tools

Common tools used:
- CAD native interference detection
- CATIA Clash Detection
- NX Check-Mate
- SolidWorks Interference Detection
- Third-party validation tools

## Reporting

Check results should:
- Be dated and versioned
- Include model configuration
- Show pass/fail status clearly
- Provide actionable details for failures
- Be archived for traceability
