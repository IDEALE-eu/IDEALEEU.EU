# 000-GENERAL — General System Data Modules

## Purpose

This directory contains **general descriptive** Data Modules (DMs) for the 21-10 Radiators & Heat Exchangers subsystem, including system descriptions, operating principles, configurations, and overview information.

## Contents

Data Modules with Info Code **000-0xx**:
- System descriptions and overviews
- Operating principles and theory
- Configuration specifications
- System architecture documentation
- Block diagrams and functional descriptions
- Interface definitions
- Performance specifications

## Data Module Types

- **000**: General description
- **001**: Equipment/system description
- **002**: Configuration data
- **003**: Component location
- **009**: Supplementary information

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-00-00-00A-000A-A_en-US_001-00.xml
```

Where:
- `AMPEL360`: Model Identification Code
- `2110`: System Code (21 = Thermal, 10 = Radiators)
- `000A`: Info Code (General)
- `en-US`: Language code
- `001-00`: Issue and in-work

## Usage Guidelines

**DO**:
- Provide clear system descriptions
- Use ASD-STE-100 Simplified Technical English
- Include cross-references to other DMs
- Document all system configurations
- Maintain applicability statements

**DO NOT**:
- Include procedural information (use 500-series)
- Include fault isolation (use 200-series)
- Include IPD data (use 800-series)
- Duplicate information from other DMs

## Review Requirements

Before publishing:
- [ ] Technical accuracy verified
- [ ] BREX validation passed
- [ ] Illustrations linked correctly
- [ ] Cross-references validated
- [ ] Applicability defined
- [ ] Security classification assigned

## Related Directories

- **[../../brex/](../../brex/)** — BREX validation rules
- **[../../icn/](../../icn/)** — Illustrations for DMs
- **[../../pm/](../../pm/)** — Publication modules

---

**Last Updated**: 2025-10-11
