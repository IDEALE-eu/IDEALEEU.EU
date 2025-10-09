# Software Build Baselines

## Overview

This document links to software baselines maintained in the Configuration Base structure, organized by ATA chapter.

## Baseline Strategy

Software baselines are maintained per ATA chapter in the Configuration Base structure:
```
02-AIRCRAFT/CONFIGURATION_BASE/ATA-XX/SOFTWARE/
├─ BASELINE_YYYY-MM-DD/
│  ├─ MANIFEST.yaml
│  ├─ SOURCE_CODE/
│  ├─ BINARIES/
│  ├─ VERIFICATION_RESULTS/
│  └─ DO178C_ARTIFACTS/
```

## Current Baselines by ATA Chapter

### ATA-27: Flight Controls
**Path**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-27/SOFTWARE/](../../../CONFIGURATION_BASE/)
**Baseline**: BASELINE_2024-09-15
**Components**:
- FCC-1 Primary Control Law (v2.5.1, DAL A)
- FCC-2 Backup Control Law (v2.5.1, DAL A)
- ACE-1 Actuator Control (v1.8.3, DAL A)
- ACE-2 Actuator Control (v1.8.3, DAL A)

### ATA-34: Navigation
**Path**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-34/SOFTWARE/](../../../CONFIGURATION_BASE/)
**Baseline**: BASELINE_2024-09-10
**Components**:
- FMS-1 Navigation Solution (v3.2.0, DAL B)
- GPS-1 Receiver Firmware (v1.5.2, DAL B)
- IRS-1 IMU Processing (v2.1.4, DAL B)
- ADC-1 Air Data Processing (v1.9.1, DAL A)

### ATA-72: Engine (Propulsion)
**Path**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-72/SOFTWARE/](../../../CONFIGURATION_BASE/)
**Baseline**: BASELINE_2024-09-20
**Components**:
- FADEC-1 Engine Control (v4.1.2, DAL A)
- FADEC-2 Engine Control (v4.1.2, DAL A)
- ENG-ECU-1 Engine Monitoring (v2.3.1, DAL A)
- ENG-ECU-2 Engine Monitoring (v2.3.1, DAL A)

### ATA-31: Indicating/Recording Systems
**Path**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-31/SOFTWARE/](../../../CONFIGURATION_BASE/)
**Baseline**: BASELINE_2024-09-05
**Components**:
- DISPLAY-1 Graphics Driver (v1.7.0, DAL C)
- DISPLAY-2 Graphics Driver (v1.7.0, DAL C)
- Flight Data Recorder (v2.0.5, DAL D)

### ATA-42: Integrated Modular Avionics (IMA)
**Path**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-42/SOFTWARE/](../../../CONFIGURATION_BASE/)
**Baseline**: BASELINE_2024-10-01
**Components**:
- IMA OS Core (v5.2.0, DAL A)
- ARINC 653 Hypervisor (v3.1.1, DAL A)
- System Health Monitor (v1.4.2, DAL B)
- Configuration Manager (v1.2.0, DAL D)

## Integration Baseline

### Current Integration Baseline: IBL-2024-Q3
**Date**: 2024-09-25
**Contents**:
- All ATA chapter baselines listed above
- Integration test results
- Configuration management artifacts
- Release notes

**Path**: [09-CONFIG_BASELINES_HANDOFF/INTEGRATION_BASELINES/IBL-2024-Q3/](../../09-CONFIG_BASELINES_HANDOFF/INTEGRATION_BASELINES/)

## Software Version Control

### Repository Structure
```
git-repo/
├─ ata-27-flight-controls/
├─ ata-34-navigation/
├─ ata-72-engine/
├─ ata-31-displays/
├─ ata-42-ima/
└─ integration/
```

### Branching Strategy
- **main**: Approved baselines only
- **develop**: Integration branch
- **feature/XXX**: Feature development
- **release/YYYY-QX**: Release candidates

### Tagging Convention
- **Format**: `ATA-XX_vMAJOR.MINOR.PATCH_BASELINE-DATE`
- **Example**: `ATA-27_v2.5.1_BASELINE-2024-09-15`

## Build Process

### Continuous Integration
- **Trigger**: Commit to develop branch
- **Steps**:
  1. Compile source code
  2. Run unit tests
  3. Run static analysis (MISRA, Coverity)
  4. Package binaries
  5. Generate traceability reports
- **Artifacts**: Stored in CI server, linked from baseline manifest

### Baseline Creation
- **Trigger**: CCB approval of release candidate
- **Steps**:
  1. Tag release in version control
  2. Build from tagged source (reproducible build)
  3. Run full verification suite (unit, integration, system tests)
  4. Generate DO-178C artifacts (source code, object code, verification results)
  5. Package baseline with manifest
  6. Sign baseline with cryptographic signature
  7. Archive in Configuration Base

## DO-178C Artifacts

Each software baseline includes DO-178C artifacts per DAL:

### DAL A Software
- Software Requirements Standards
- Software Design Standards
- Software Code Standards
- Software Requirements Data
- Software Design Description
- Source Code
- Executable Object Code
- Software Verification Cases and Procedures
- Software Verification Results
- Software Life Cycle Environment Configuration Index
- Software Configuration Index
- Software Accomplishment Summary

### DAL B/C/D Software
- Subset of DAL A artifacts per DO-178C Table A-1

## Traceability

### Requirements to Code
- Maintained in [00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv)
- Automated traceability checks in CI pipeline

### Code to Test
- Unit test traceability per source file
- Integration test traceability per functional chain
- See [07-INTEGRATION_TEST/TRACEABILITY.csv](../../07-INTEGRATION_TEST/TRACEABILITY.csv)

## Change Control

### Software Changes
All software changes follow ECR/ECO process:
1. **ECR Submission**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
2. **Impact Analysis**: Assess affected baselines, re-verification needs
3. **CCB Approval**: Configuration Control Board review
4. **Implementation**: Develop, test, verify
5. **Baseline Update**: Create new baseline with change incorporated

## Compliance

- **DO-178C**: Software development and verification per DAL
- **DO-330**: Software tool qualification (compilers, static analyzers)
- **ARP4754A**: Software safety assessment
- **AS9100**: Quality management system

## References

- **[02-AIRCRAFT/CONFIGURATION_BASE/](../../../CONFIGURATION_BASE/)** - ATA-specific baselines
- **[09-CONFIG_BASELINES_HANDOFF/](../../09-CONFIG_BASELINES_HANDOFF/)** - Integration baselines
- **[15-AUTOMATION/CI_PIPELINE.md](../../15-AUTOMATION/CI_PIPELINE.md)** - CI/CD pipeline

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | SW Integration Team | Initial build baselines document |
