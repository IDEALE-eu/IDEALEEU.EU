# Interface Matrix Mapping to ICDs

## Overview

This document maps the interface matrix entries to their corresponding Interface Control Documents (ICDs) managed in the CONFIG_MGMT repository.

## Purpose

- Provide human-readable index of all system interfaces
- Link local interface matrix to program-level ICD repository
- Track ICD approval status and versions
- Support configuration baseline management

## ICD Repository Structure

All ICDs are maintained in:
```
00-PROGRAM/CONFIG_MGMT/09-INTERFACES/
├─ ICD_INDEX.md           # Master ICD catalog
├─ ICD-XXXX.md            # Individual ICD documents
└─ ARCHIVE/               # Superseded ICDs
```

## Critical Interfaces

### Flight Control Interfaces (DAL A)
- **ICD-0003**: Avionics ↔ Flight Control System (AFDX)
  - Version: 1.2 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0003.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0003.md)
  - Used by: FC-001 (Primary Flight Control - Pitch)
  
- **ICD-0015**: Flight Control ↔ Actuator Control Electronics (AFDX)
  - Version: 1.1 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0015.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0015.md)
  - Used by: FC-001 (Primary Flight Control - Pitch)

### Propulsion Interfaces (DAL A)
- **ICD-0001**: Aircraft ↔ Propulsion System
  - Version: 1.0 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0001.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0001.md)
  - Used by: FC-003 (Engine Thrust Control)

- **ICD-0006**: Engine ECU ↔ FADEC (CAN Bus)
  - Version: 1.0 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0006.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0006.md)
  - Used by: FC-003 (Engine Thrust Control)

- **ICD-0031**: Throttle Lever ↔ FADEC
  - Version: 1.0 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0031.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0031.md)
  - Used by: FC-003 (Engine Thrust Control)

- **ICD-0032**: FADEC ↔ Engine ECU (CAN Bus)
  - Version: 1.1 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0032.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0032.md)
  - Used by: FC-003 (Engine Thrust Control)

### Power System Interfaces (DAL A)
- **ICD-0004**: Power Generation ↔ Power Distribution
  - Version: 1.0 (Draft)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0004.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0004.md)
  - Used by: FC-005 (Electrical Power Distribution)

### Navigation Interfaces (DAL B)
- **ICD-0021**: GPS Receiver ↔ FMS (ARINC 429)
  - Version: 1.2 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0021.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0021.md)
  - Used by: FC-002 (Navigation Solution)

- **ICD-0022**: Inertial Reference ↔ FMS (AFDX)
  - Version: 1.1 (Approved)
  - Path: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0022.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0022.md)
  - Used by: FC-002 (Navigation Solution)

## ICD Status Dashboard

### By Criticality
- **Critical**: 10 ICDs (8 Approved, 2 Draft)
- **High**: 9 ICDs (5 Approved, 4 Draft)
- **Medium**: 5 ICDs (2 Approved, 3 Draft)
- **Low**: 2 ICDs (1 Approved, 1 Draft)

### Approval Status
- **Approved**: 16 ICDs (61%)
- **Draft**: 10 ICDs (39%)
- **Superseded**: 0 ICDs

## ICD Change Control

Changes to ICDs follow the program change management process:

1. **ECR Submission**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
2. **Impact Analysis**: Assess affected functional chains and systems
3. **CCB Review**: Configuration Control Board approval
4. **Baseline Update**: Update configuration baseline
5. **Notification**: Notify affected parties via RASCI

## Traceability

### Requirements to ICDs
Requirements traceability maintained in:
- [00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv)

### Functional Chains to ICDs
See: [../FUNCTIONAL_CHAINS/CHAINS.yaml](../FUNCTIONAL_CHAINS/CHAINS.yaml)

### ICDs to Test Procedures
See: [../../07-INTEGRATION_TEST/TRACEABILITY.csv](../../07-INTEGRATION_TEST/TRACEABILITY.csv)

## MBSE Integration

ICDs are auto-generated from SysML models:
- Model Location: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/SYSML_MODELS/](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/)
- Generated ICDs: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/)
- Generation Scripts: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/README.md](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/README.md)

## References

- **ARP4754A** - Section 5.3, Interface Management
- **[00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md)** - Master ICD catalog
- **[INTERFACE_MATRIX.csv](./INTERFACE_MATRIX.csv)** - Interface matrix data

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Interface Management Team | Initial ICD mapping |
