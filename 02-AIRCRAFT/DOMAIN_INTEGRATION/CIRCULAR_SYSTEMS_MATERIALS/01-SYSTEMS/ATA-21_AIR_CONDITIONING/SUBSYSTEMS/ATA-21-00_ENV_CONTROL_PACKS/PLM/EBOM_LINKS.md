# EBOM Links - ATA-21-00 Environmental Control Packs

## Overview

This document provides links to Engineering Bill of Materials (EBOM) entries in the PLM system for the Environmental Control Pack subsystem.

## PLM System Links

### Primary Assembly
- **Pack Assembly**: PLM-21-00-001
  - Heat Exchanger (Primary): PLM-21-00-002
  - Heat Exchanger (Secondary): PLM-21-00-003
  - Air Cycle Machine (ACM): PLM-21-00-004
  - Turbine: PLM-21-00-005
  - Compressor: PLM-21-00-006
  - Fan: PLM-21-00-007

### Controller LRU
- **Pack Controller**: PLM-21-00-100
  - Controller PCB: PLM-21-00-101
  - Power Supply: PLM-21-00-102
  - I/O Module: PLM-21-00-103
  - Software Package: PLM-21-00-104 (see CAx/CAS and CAx/CMP)

### Sensors and Actuators
- **Temperature Sensors**: PLM-21-00-200 through PLM-21-00-210
- **Pressure Sensors**: PLM-21-00-220 through PLM-21-00-230
- **Flow Control Valves**: PLM-21-00-240 through PLM-21-00-245
- **Mix Valves**: PLM-21-00-250 through PLM-21-00-255

## CAx File Organization

### CAD (Computer-Aided Design)
- 3D models of pack assembly and components
- Drawing packages for manufacturing
- Assembly instructions

### CAE (Computer-Aided Engineering)
- Thermal analysis (heat exchanger performance)
- Structural analysis (mounting loads)
- Vibration analysis (rotating components)

### CAO (Computer-Aided Optimization)
- Flow optimization for heat exchangers
- Weight optimization for structural components
- Efficiency optimization for ACM

### CAM (Computer-Aided Manufacturing)
- CNC programs for machined components
- Tooling definitions
- Manufacturing process plans

### CAI (Computer-Aided Inspection)
- CMM inspection programs
- Quality control procedures
- Acceptance test procedures

### CAV (Computer-Aided Validation)
- Environmental test procedures (DO-160)
- Qualification test plans
- Certification test reports

### CAP (Computer-Aided Project Management)
- Project schedules (Gantt charts)
- Resource allocation
- Cost tracking

### CAS (Computer-Aided Software)
- Pack controller software source code
- Software requirements specifications
- Software test cases

### CMP (Computer-Aided Maintenance Planning)
- Maintenance manuals
- Troubleshooting guides
- Spare parts lists
- Mean Time Between Removal (MTBR) data

## Traceability

### Requirements Traceability
- Requirements linked to PLM items via [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../../../../04-DIGITAL_THREAD/MBSE_BINDINGS.md)
- Each PLM item has requirement allocation in MBSE model

### Configuration Management
- EBOM changes managed through ECO process: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- Baseline controlled via configuration items (CIs)

## Related Documents

- [INTEGRATION_VIEW.md](../../INTEGRATION_VIEW.md) - System-level integration
- [02-INTERFACES/INTERFACE_MATRIX.csv](../../../../02-INTERFACES/INTERFACE_MATRIX.csv) - Interface definitions
- [05-VERIFICATION/](../../../../05-VERIFICATION/) - Test and verification artifacts
