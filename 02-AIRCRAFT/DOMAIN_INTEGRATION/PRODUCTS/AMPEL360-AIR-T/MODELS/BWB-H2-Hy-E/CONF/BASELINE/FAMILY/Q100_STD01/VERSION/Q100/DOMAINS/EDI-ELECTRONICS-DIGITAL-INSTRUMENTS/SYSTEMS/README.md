# EDI — ELECTRONICS, DIGITAL INSTRUMENTS — SYSTEMS

## Overview

The EDI domain encompasses all electronic, digital, and instrumentation systems for the aircraft. This includes avionics systems, integrated modular avionics (IMA), navigation, engine indicating, flight deck displays, and electronics equipment compartments.

## Systems Architecture

### System Organization

All systems follow the unified convention:
- System-level: `INTEGRATION_VIEW.md` + `INTERFACE_MATRIX/`
- Subsystem-level: `PLM/CAx/` with all 9 subdirectories (CAD, CAE, CAO, CAI, CAM, CAV, CAP, CAS, CMP)

### ATA Chapter Mapping

| System | ATA Chapter | Description |
|--------|-------------|-------------|
| 31-INDICATING_RECORDING | ATA 31 | Indicating, recording, and alerting systems |
| 34-NAVIGATION | ATA 34 | Navigation systems and avionics |
| 40-AVIONICS_STD_GENERAL | ATA 40 | Avionics standards and templates |
| 42-INTEGRATED_MODULAR_AVIONICS | ATA 42 | IMA, core processing, and networks |
| 77-ENGINE_INDICATING | ATA 77 | Engine indicating and crew alerting |
| 94-EE_COMPARTMENTS | ATA 94 | Electronics and equipment compartments |

## System Details

### 31 — INDICATING & RECORDING

**Subsystems:**
- 31-00: Standards & General
- 31-10: Flight Deck Displays (PFD, ND, EICAS/ECAM)
- 31-20: Alerting, Caution & Warning (Master Caution/Warning)
- 31-30: Recorders (FDR, CVR)
- 31-40: Data Acquisition & Bussing
- 31-50: ACMS & Maintenance Logging Interfaces

**Key Interfaces:** ATA 24, 34, 39, 42, 44, 45, 71, 72, 92, 93, 94

### 34 — NAVIGATION

**Subsystems:**
- 34-00: Standards & General
- 34-10: Air Data (ADC, Pitot-Static)
- 34-20: AHRS/IRS (Inertial Reference)
- 34-30: Radio Navigation (VOR, ILS, DME)
- 34-40: GNSS (GPS, Galileo)
- 34-50: Radar Altimeter
- 34-60: Surveillance (TCAS, ADS-B)
- 34-70: Terrain Awareness (EGPWS/GPWS)

**Key Interfaces:** ATA 22, 24, 31, 42, 45, 92

### 40 — AVIONICS STANDARDS & GENERAL (Template)

**Subsystems:**
- 40-00: Standards & Templates

**Purpose:** Cross-system standards, templates, and requirements applicable to all EDI systems.

**Key Interfaces:** All EDI systems

### 42 — INTEGRATED MODULAR AVIONICS

**Subsystems:**
- 42-00: Standards & General (ARINC 653, DO-297)
- 42-10: Core Processors (CMC, CPM)
- 42-20: Network (AFDX/TSN Switching)
- 42-30: Time Sync (PTP, IRIG-B)
- 42-40: ARINC 653 Partitions & Services
- 42-50: SW Loaders & Config Management
- 42-60: Security, Crypto & Hardening

**Key Interfaces:** ATA 24, 31, 34, 45, 92, 93

### 77 — ENGINE INDICATING

**Subsystems:**
- 77-00: Standards & General
- 77-10: EIU Interfaces & Data Gateway
- 77-20: Engine Sensors (N1, N2, EGT, Fuel Flow)
- 77-30: Display Integration (EICAS/ECAM)
- 77-40: FADEC Data Interface (with ATA 73)

**Key Interfaces:** ATA 24, 31, 42, 73, 92

### 94 — ELECTRONICS & EQUIPMENT COMPARTMENTS

**Subsystems:**
- 94-00: Standards & General
- 94-10: Racks (ARINC 600 Installation)
- 94-20: Cooling, Airflow & Heat Management
- 94-30: EMI/EMC Shielding & Gaskets
- 94-40: Access Panels & HUMS Monitoring
- 94-50: Fire Detect/Suppress Interface (with ATA 26)

**Key Interfaces:** ATA 21, 24, 26, 31, 42, 92

## Architecture Rules

### PLM/CAx Location
- **PLM/CAx directories ONLY exist at SUBSYSTEM level**
- Systems contain `INTEGRATION_VIEW.md` and `INTERFACE_MATRIX/`
- Domain level contains configuration and standards

### Interface Management
- Each system has an `INTERFACE_MATRIX/` directory
- CSV files define system-to-system interfaces
- Format: `XX-SYSTEM↔YY_ZZ_...csv` showing all interfacing systems

### Naming Convention
- Systems: `{ID}-{NAME}` (e.g., `34-NAVIGATION`)
- Subsystems: `{SYSTEM_ID}-{SUB_ID}_{NAME}` (e.g., `34-20_AHRS_IRS_INERTIAL`)
- Use underscores for multi-word names within components
- Use hyphens to separate ID from name

### CAx Directory Structure
Every subsystem contains:
```
PLM/
├─ EBOM_LINKS.md
└─ CAx/
   ├─ CAD/  (Computer-Aided Design)
   ├─ CAE/  (Computer-Aided Engineering)
   ├─ CAO/  (Computer-Aided Optimization)
   ├─ CAM/  (Computer-Aided Manufacturing)
   ├─ CAI/  (Computer-Aided Inspection)
   ├─ CAV/  (Computer-Aided Verification)
   ├─ CAP/  (Computer-Aided Planning)
   ├─ CAS/  (Computer-Aided Simulation)
   └─ CMP/  (Computer-Aided Materials/Processing)
```

## Integration Notes

### ICDs (Interface Control Documents)
- Reference: `../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- All interface definitions coordinated at program level

### EWIS (Electrical Wiring Interconnection System)
- Physical connectivity managed in **ATA 92**
- Only references from interface matrices

### Software Management
- Software versions tracked with host LRU
- Examples:
  - FADEC software in ATA 73
  - ARINC 653 partitions in ATA 42
  - IMA applications in ATA 42

### Configuration Management
- Engineering BOMs in `SUBSYSTEMS/*/PLM/EBOM_LINKS.md`
- Interface definitions in `INTERFACE_MATRIX/*.csv`
- CAx artifacts in `SUBSYSTEMS/*/PLM/CAx/*`

## Working with EDI Systems

### For System Engineers
1. Review [INTEGRATION_VIEW.md](./SYSTEM/INTEGRATION_VIEW.md) for system scope
2. Check [INTERFACE_MATRIX/](./SYSTEM/INTERFACE_MATRIX/) for cross-system interfaces
3. Navigate to specific subsystems in [SUBSYSTEMS/](./SYSTEM/SUBSYSTEMS/)

### For Subsystem Engineers
1. Access subsystem directory under `SYSTEMS/{SYSTEM}/SUBSYSTEMS/`
2. Review subsystem README for specific requirements
3. Place engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### For PLM/Configuration Management
- All engineering artifacts reside in subsystem-level `PLM/CAx/` directories
- BOM links tracked in `PLM/EBOM_LINKS.md`
- Interface definitions in system-level `INTERFACE_MATRIX/` CSVs
- No PLM artifacts at system or domain level (validation enforced)

## Navigation

- [⬆️ Back to EDI Domain](../)
- [📋 Domain README](../README.md)
- [🔗 ICD Index](../../04-ICD_LINKS/ICD_INDEX.md)

---

**Status**: Structure complete - Ready for engineering artifact population

**Version**: Q100  
**Product**: AMPEL360-AIR-T  
**Model**: BWB-H2-Hy-E
