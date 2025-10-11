# IIS — Information Intelligence Systems

## Overview

The IIS (Information Intelligence Systems) domain encompasses all information management, data processing, analytics, and training systems for the AMPEL360-AIR-T BWB-H2-Hy-E aircraft. This domain manages the digital infrastructure, data flows, cybersecurity, performance analytics, and operational procedures.

## Systems in This Domain

### 46 — INFORMATION SYSTEMS
Primary information technology systems including networking, data management, cybersecurity, and digital twin capabilities.

**Subsystems:**
- 46-00 Standards & General
- 46-10 Ground IT Gateways & APIs
- 46-20 Data Bus UTCS Broker
- 46-30 Health Analytics & PDM
- 46-40 Cybersecurity IDAM & SIEM
- 46-50 OTA Software Content Management
- 46-60 Data Lake & Warehouse
- 46-70 Event Logging & Telemetry
- 46-80 Digital Twin (OPTIMO-DT)

**Key Interfaces:** See [INTERFACE_MATRIX/46-INFORMATION-SYSTEMS↔OTROS.csv](./46-INFORMATION-SYSTEMS/INTERFACE_MATRIX/)

### 91 — CHARTS & PERFORMANCE
Aircraft performance models, flight planning charts, and regulatory reporting systems.

**Subsystems:**
- 91-00 Standards & General
- 91-10 Aircraft Performance Models
- 91-20 Flight Planning Charts
- 91-30 Performance Export Interfaces
- 91-40 Audit Reports & Regulatory Compliance

### IIS-90 — PROCEDURES & TRAINING
Standard operating procedures and training modules for aircraft systems.

**Subsystems:**
- 90-01 SOPs & Checklists
- 90-02 CBT Training Modules

## Domain-Level Interfaces

The IIS domain interfaces with multiple ATA chapters across the aircraft:

- **23** Communications
- **24** Electrical Power
- **31** Instruments
- **34** Navigation
- **42** Integrated Modular Avionics
- **44** Cabin Systems
- **45** Central Maintenance System
- **46** Information Systems (internal)
- **71** Powerplant
- **72** Engine
- **92** EWIS (Electrical Wiring Interconnection System)
- **93** Ground Support & Service Equipment
- **94** Training

**Interface Matrix:** [IIS↔23_24_31_34_42_44_45_46_71_72_92_93_94.csv](./INTERFACE_MATRIX/IIS↔23_24_31_34_42_44_45_46_71_72_92_93_94.csv)

## Architecture

```
IIS-INFORMATION-INTELLIGENCE-SYSTEMS/
├─ SYSTEMS/
│  ├─ README.md (this file)
│  ├─ INTERFACE_MATRIX/
│  │  └─ IIS↔23_24_31_34_42_44_45_46_71_72_92_93_94.csv
│  ├─ 46-INFORMATION-SYSTEMS/
│  │  ├─ README.md
│  │  ├─ INTEGRATION_VIEW.md
│  │  ├─ INTERFACE_MATRIX/
│  │  └─ SUBSYSTEMS/
│  │     └─ 46-XX_NAME/
│  │        ├─ README.md
│  │        └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
│  ├─ 91-CHARTS_PERFORMANCE/
│  │  ├─ README.md
│  │  ├─ INTERFACE_MATRIX/
│  │  └─ SUBSYSTEMS/
│  │     └─ 91-XX_NAME/
│  │        ├─ README.md
│  │        └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
│  └─ IIS-90_PROCEDURES_TRAINING/
│     ├─ README.md
│     └─ SUBSYSTEMS/
│        └─ 90-XX_NAME/
│           ├─ README.md
│           └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
```

## PLM Structure

All engineering artifacts reside in subsystem-level `PLM/CAx/` directories:

- **CAD** — Computer-Aided Design (3D models, drawings)
- **CAE** — Computer-Aided Engineering (FEA, CFD)
- **CAO** — Computer-Aided Optimization (topology, sizing)
- **CAI** — Computer-Aided Installation (assembly procedures)
- **CAM** — Computer-Aided Manufacturing (toolpaths, NC programs)
- **CAV** — Computer-Aided Validation (test plans, results)
- **CAP** — Computer-Aided Planning (schedules, resources)
- **CAS** — Computer-Aided Simulation (system simulation)
- **CMP** — Composite Materials Processing (layup, curing)

## Key Principles

1. **No PLM at System Level:** PLM/CAx directories exist only in SUBSYSTEMS
2. **Interface Matrices:** Each system maintains interface definitions with other ATA chapters
3. **Integration Views:** Each system provides integration documentation
4. **Traceability:** All artifacts link to requirements via EBOM_LINKS.md
5. **Validation:** Structure validated via CI/CD scripts

## Related Documentation

- Domain README: `../README.md`
- Domain Config: `../domain-config.yaml`
- Q100 Architecture: `../../README.md`
- Interface Management: `../../04-ICD_LINKS/`
