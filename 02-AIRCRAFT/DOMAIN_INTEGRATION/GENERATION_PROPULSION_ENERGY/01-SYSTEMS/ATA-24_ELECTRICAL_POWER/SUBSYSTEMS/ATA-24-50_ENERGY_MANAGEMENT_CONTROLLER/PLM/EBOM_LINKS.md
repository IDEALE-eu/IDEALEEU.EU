# ATA-24-50 Energy Management Controller - EBOM Links

## Overview

Engineering Bill of Materials (EBOM) links for Energy Management System (EMS) components.

## Components

### Energy Management Controller (EMC)
- **Part Number**: EMC-24-5000-A
- **Description**: Primary Energy Management and Control Unit
- **PLM Reference**: PLM://PARTS/EMC-24-5000-A
- **Supplier**: Advanced Control Systems Inc.
- **Configuration Status**: Baseline Rev E
- **Software Version**: SW-EMC-4.2.1
- **DO-178C Level**: Level B
- **Installation**: Main avionics bay

### Power System Monitor Unit
- **Part Number**: PSMU-24-5010-A
- **Description**: Real-time Power Quality Monitor
- **PLM Reference**: PLM://PARTS/PSMU-24-5010-A
- **Supplier**: Advanced Control Systems Inc.
- **Configuration Status**: Baseline Rev C
- **Software Version**: SW-PSMU-2.1.0
- **Installation**: Main equipment bay

### Load Management Unit
- **Part Number**: LMU-24-5020-A
- **Description**: Automatic Load Shedding Controller
- **PLM Reference**: PLM://PARTS/LMU-24-5020-A
- **Supplier**: Control Systems Corp.
- **Configuration Status**: Baseline Rev B
- **Software Version**: SW-LMU-1.3.2
- **Installation**: Main equipment bay

## ARINC 653 Partition Mapping

If the Energy Management Controller is hosted on an IMA platform, the following partitions are defined:

### EMC Partition
- **Partition ID**: P-EMC-001
- **IMA Module**: IMA-MOD-1 (ATA-42)
- **Memory Allocation**: 4 MB
- **CPU Time Slot**: 50 ms major frame, 10 ms partition window
- **Criticality Level**: DAL B
- **Reference**: See ATA-42 IMA Configuration

### PSMU Partition
- **Partition ID**: P-PSMU-001
- **IMA Module**: IMA-MOD-1 (ATA-42)
- **Memory Allocation**: 2 MB
- **CPU Time Slot**: 50 ms major frame, 5 ms partition window
- **Criticality Level**: DAL C
- **Reference**: See ATA-42 IMA Configuration

## Software Configuration

### EMC Software Baseline
- **Software Part Number**: SW-EMC-24-5000-4.2.1
- **Certification Basis**: DO-178C Level B
- **Compiler**: GCC ARM v10.3
- **RTOS**: ARINC 653 APEX API
- **Configuration Items**:
  - Power generation control algorithms
  - Bus management logic
  - Load shedding sequences
  - Fault detection and isolation
  - Built-In Test (BIT) routines

### Software Requirements Traceability
- Requirements linked in PLM system
- Traceability to DO-178C objectives
- Test coverage reports available

## CAx Artifacts

See `PLM/CAD/`, `PLM/CAE/`, `PLM/CAO/`, `PLM/CAM/`, `PLM/CAI/`, `PLM/CAV/`, `PLM/CAP/`, `PLM/CAS/`, `PLM/CMP/` for Computer-Aided Engineering artifacts.

## Digital Thread Integration

### MBSE Model References
- SysML Model: `MBSE://EMS/EMC-24-5000`
- Requirements: `REQ://24-50/EMC-REQUIREMENTS`
- Test Cases: `TEST://24-50/EMC-TEST-SUITE`

### Digital Twin KPIs
- Power generation capacity utilization
- Load distribution efficiency
- Fault detection response time
- Bus voltage regulation accuracy

## Change History

| Date | Rev | Description | Author |
|------|-----|-------------|--------|
| 2024-01-15 | A | Initial creation | Systems Engineering |

---

**Last Updated**: 2024-01-15
