# 400-SCHEDULED-MAINTENANCE — Scheduled Maintenance Procedures

## Purpose

This directory contains **scheduled maintenance** Data Modules (DMs) for the 21-10 Radiators & Heat Exchangers subsystem, including inspection procedures, preventive maintenance tasks, and maintenance intervals.

## Contents

Data Modules with Info Code **400-4xx**:
- Scheduled maintenance tasks
- Inspection procedures and intervals
- Preventive maintenance procedures
- Servicing requirements
- Lubrication schedules
- Cleaning procedures
- Operational checks
- Performance verification

## Data Module Types

- **400**: Scheduled maintenance introduction
- **401**: Inspection procedures
- **402**: Check procedures
- **403**: Operational test procedures
- **404**: Servicing procedures
- **405**: Cleaning procedures

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-00-00-00A-401A-A_en-US_001-00.xml
```

Where:
- `401A`: Info Code (Inspection)
- Maintenance task specific code

## Maintenance Categories

### Periodic Inspections
- Visual inspections
- Functional checks
- Leak checks
- Performance verification
- Coating integrity checks

### Servicing Tasks
- Fluid sampling and analysis
- Filter replacement
- Pressure testing
- Flow rate verification
- Temperature sensor calibration

### Cleaning Procedures
- External surface cleaning
- Contamination removal
- Pre-flight/pre-mission cleaning

## Usage Guidelines

**DO**:
- Specify maintenance intervals clearly
- Include acceptance criteria
- Document required tools and materials
- Provide safety precautions
- Cross-reference removal/installation (500-series)
- Include inspection checklists

**DO NOT**:
- Include troubleshooting (use 200-series)
- Include repair procedures (use 600-series)
- Include overhaul procedures (use 700-series)
- Mix scheduled and unscheduled maintenance

## Maintenance Intervals

Document intervals as:
- Flight hours / Mission cycles
- Calendar time
- Operational cycles
- Conditional triggers

## Review Requirements

Before publishing:
- [ ] Intervals validated by engineering
- [ ] Safety warnings included
- [ ] Tools and consumables listed
- [ ] Acceptance criteria defined
- [ ] BREX validation passed
- [ ] Technical review completed

## Related Directories

- **[../500-removal-installation/](../500-removal-installation/)** — R&I procedures
- **[../900-tools-consumables/](../900-tools-consumables/)** — Required tools
- **[../../qc/](../../qc/)** — Quality control records

---

**Last Updated**: 2025-10-11
