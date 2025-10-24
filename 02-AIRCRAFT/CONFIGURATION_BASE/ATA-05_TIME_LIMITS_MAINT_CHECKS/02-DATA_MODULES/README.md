# 02-DATA_MODULES

## Purpose
Source Data Modules (DMCs) defining individual maintenance requirements and procedures.

## Overview
This directory contains the canonical S1000D Data Modules that define all maintenance requirements, intervals, and procedures for time-limited tasks and periodic checks under ATA Chapter 05.

## Data Module Structure
Each Data Module follows S1000D Issue 5.0 structure with:
- **DMC (Data Module Code)**: Unique identifier per S1000D schema
- **DMTitle**: Descriptive title of the maintenance requirement
- **Info Code**: Type of information (procedural, descriptive, fault isolation)
- **Issue Date**: Publication date and version
- **Applicability**: Aircraft models, serial number ranges, effectivity

## Content Types
### Procedural Data Modules
- Step-by-step maintenance procedures
- Inspection criteria and acceptance standards
- Calibration and test procedures
- Rigging and adjustment instructions

### Descriptive Data Modules
- Component identification and location
- System descriptions relevant to maintenance
- Servicing specifications
- Troubleshooting decision trees

### Scheduled Maintenance
- Calendar-based interval definitions
- Flight-hour-based interval definitions
- Cycle-based interval definitions
- Condition-based monitoring thresholds

## S1000D Compliance
- **Data Module Identification**: DMC-{Model}-{System}-{SubSystem}-{Type}-{Variant}-{Item}
- **XML Schema**: S1000D Issue 5.0 compliant XML
- **Common Source Database (CSDB)**: Integrated with publication pipeline
- **Technical Publications**: Export to PDF, HTML, IETP formats

## Integration
- **AAMMPP**: Maintenance planning and scheduling system
- **CMP**: Configuration Management Program
- **Digital Twin**: Maintenance event correlation
- **ESG Tracking**: Environmental impact per procedure

## Versioning
All Data Modules follow configuration control:
- Version tracked in DMC issue number
- Changes require ECN approval
- Baseline references in `03-IDENTIFICATION/`

## Compliance References
- **S1000D Issue 5.0**: International specification for technical publications
- **ASD S1000D**: Aerospace and Defence Industries Association of Europe
- **MSG-3**: Maintenance Steering Group logic (where applicable)

## Status
Active — Baseline 1.0

## Contacts
- **Owner**: Technical Publications / CMP
- **Approver**: CMP Lead — ATA-05
- **Reviews**: CCB quarterly

---
**Last Updated**: 2025-10-24
