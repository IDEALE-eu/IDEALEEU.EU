# Quick Reference: Telescope Systems Structure

## Location
```
05-TELESCOPES/DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/
```

## Complete Systems List (34 Systems)

| System | Name | Key Interfaces | Notes |
|--------|------|---------------|-------|
| 01 | INTRO | ALL | System introduction |
| 06 | DIMENSIONS_ALIGNMENTS | 51,53,55,57,70,32 | Alignment control |
| 15 | ENVIRONMENT_VIBRATION | 21,51,53,70,72,75 | Vibration isolation |
| 21 | THERMAL_CONTROL | 30,72,75,70,71,24,53,55,57 | Active thermal |
| 24 | ELECTRICAL_POWER | 71,72,73,76,78,42,31,33,92 | Power distribution |
| 26 | FIRE_SAFETY | 21,24,42,92 | Safety systems |
| 30 | ICE_DEW_PREVENTION | 21,24,53,56 | Anti-contamination |
| 31 | DATA_HANDLING | 24,42,71,32,77,99 | Data acquisition |
| 32 | POINTING_STABILIZATION | 34,24,70,76,45,21,92 | Pointing control |
| 33 | LIGHTS | 70,71,24,31 | Lighting |
| 34 | NAVIGATION_ATTITUDE | 32,42,31,24 | Navigation |
| 42 | AVIONICS_CONTROL | 31,24,32,34,71,45,70,92 | Central avionics |
| 45 | HEALTH_MONITORING | 70,71,32,24,31,42 | Health status |
| 51 | PRIMARY_STRUCTURE | 53,55,57,21,70,71,92 | Main structure |
| 52 | ACCESS_HATCHES | 53,21,24,92 | Service access |
| 53 | OPTICAL_TUBE_ASSEMBLY | 51,55,57,21,70,92 | Optical tube |
| 55 | SECONDARY_SUPPORT | 53,51,70,73,76 | Secondary mount |
| 56 | WINDOWS_DOMES | 30,53,21,24 | Protective windows |
| 57 | INSTRUMENT_BAYS | 71,70,21,24,92 | Instrument mounts |
| 66 | DEPLOYABLE_OPTICS | 57,53,55,21,24,92 | Deployable elements |
| **70** | **OPTICAL_SUBSYSTEMS** | 21,32,45,51,55,57 | **Custom optics block** |
| **71** | **INSTRUMENTS_PAYLOADS** | 24,31,70,57 | **Science instruments** |
| 72 | CRYOGENIC_COOLING | 21,24,70,71,75,92 | Cryo systems |
| 73 | FOCUS_ACTUATION | 24,70,32,42,45,92 | Focus mechanisms |
| 75 | THERMAL_RADIATORS | 21,72,24,53,57 | Passive thermal |
| 76 | MIRROR_CONTROL | 70,32,24,42,45 | Active mirrors |
| 77 | ALIGNMENT_SENSING | 70,32,31,24,45 | Metrology |
| 78 | BACKPLANE_ELECTRONICS | 71,70,24,31,42,92 | Backplane |
| 79 | LUBRICATION | 73,66,57 | Mechanisms |
| 80 | STARTUP_SEQUENCING | 42,21,24,66,72,70,71 | Initialization |
| 84 | PROPULSION | 24,21,32,34,92 | Station-keeping |
| **92** | **EWIS_HARNESS** | **ALL** | **Centralized wiring** |
| 94 | ELECTRONIC_COMPARTMENTS | 24,31,42,78,92,21 | Electronics bays |
| 99 | SCIENCE_OPERATIONS | 31,42,71,24 | Ops planning |

## Subsystems with PLM/CAx

### 70-OPTICAL_SUBSYSTEMS (8 subsystems)
```
70-10_PRIMARY_MIRROR
70-20_SECONDARY_MIRROR
70-30_TERTIARY_FLAT
70-40_CORRECTORS_LENS
70-50_FILTERS_GRISMS
70-60_DETECTOR_CRYOSTATS
70-70_WAVEFRONT_SENSORS
70-80_CALIBRATION_SOURCES
```

### 71-INSTRUMENTS_PAYLOADS (3 subsystems)
```
71-10_IMAGER
71-20_SPECTROGRAPH
71-30_CORONAGRAPH
```

## Standard Files per System

```
XX-SYSTEM_NAME/
├─ INTEGRATION_VIEW.md           # System integration overview
└─ INTERFACE_MATRIX/
   └─ XX↔OTHERS.csv              # Interface specifications
```

## Standard Files per Subsystem

```
XX-YY_SUBSYSTEM/
├─ README.md                     # Subsystem description
├─ META.json                     # Metadata (scope: "instance")
├─ PLM/
│  ├─ EBOM_LINKS.md             # Engineering BOM
│  └─ CAx/                      # Engineering artifacts
│     ├─ CAD/                   # Design
│     ├─ CAE/                   # Analysis
│     ├─ CAM/                   # Manufacturing
│     ├─ CAI/                   # Inspection
│     ├─ CAV/                   # Verification
│     ├─ CAP/                   # Planning
│     ├─ CAS/                   # Simulation
│     └─ CMP/                   # Configuration
├─ DELs/                        # Deliverables
├─ PAx/                         # Process artifacts
├─ SUPPLIERS/                   # Supplier data
├─ policy/                      # Policies
└─ tests/                       # Test artifacts
```

## Interface Matrix CSV Header

```csv
from_system,to_system,interface_type,icd_ref,signals/measures,thermal,mechanical,electrical,data_bus,harness,sw_api,safety_class,owner,status,notes
```

## Architecture Rules (Critical)

### ✅ DO
- Place PLM/CAx **ONLY** in subsystems
- Store all wiring in **92-EWIS_HARNESS**
- Keep software with host LRU
- Use interface matrices for system connections
- Follow standard CSV format

### ❌ DON'T
- Create PLM/CAx at system level
- Scatter wiring definitions across systems
- Create ad-hoc directory structures
- Skip interface documentation

## Quick Commands

### Create Structure
```bash
cd /path/to/IDEALEEU.EU
./scripts/create-telescope-systems.sh
```

### Validate Structure
```bash
cd /path/to/IDEALEEU.EU
./scripts/validate-telescope-systems.sh
```

## Common Tasks

### Add a New Subsystem to System 70
```bash
cd 05-TELESCOPES/.../SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/
mkdir -p 70-90_NEW_COMPONENT/PLM/CAx/{CAD,CAE,CAM,CAI,CAV,CAP,CAS,CMP}
# Add README.md, META.json, EBOM_LINKS.md
```

### Update Interface Matrix
```bash
# Edit the CSV file
vim 05-TELESCOPES/.../SYSTEMS/XX-SYSTEM/INTERFACE_MATRIX/XX↔OTHERS.csv
# Add row with interface details following header format
```

### Check System Interfaces
```bash
# View all interfaces for system 70
cat 05-TELESCOPES/.../SYSTEMS/70-OPTICAL_SUBSYSTEMS/INTERFACE_MATRIX/*.csv
```

## Directory Tree Example

```
SYSTEMS/
├─ 70-OPTICAL_SUBSYSTEMS/
│  ├─ INTEGRATION_VIEW.md
│  ├─ INTERFACE_MATRIX/
│  │  └─ 70↔21_32_45_51_55_57.csv
│  └─ SUBSYSTEMS/
│     ├─ 70-10_PRIMARY_MIRROR/
│     │  ├─ README.md
│     │  ├─ META.json
│     │  └─ PLM/
│     │     ├─ EBOM_LINKS.md
│     │     └─ CAx/
│     │        ├─ CAD/
│     │        ├─ CAE/
│     │        └─ ...
│     └─ 70-20_SECONDARY_MIRROR/
│        └─ ...
└─ 71-INSTRUMENTS_PAYLOADS/
   └─ ...
```

## Key Concepts

- **STA**: Space Transport Architecture (SPACE-T numbering)
- **PLM**: Product Lifecycle Management
- **CAx**: Computer-Aided X (Design, Engineering, Manufacturing, etc.)
- **EWIS**: Electrical Wiring Interconnection System
- **LRU**: Line Replaceable Unit
- **EBOM**: Engineering Bill of Materials
- **ICD**: Interface Control Document

## Support

For questions or issues:
1. Review main README: `05-TELESCOPES/00-README.md`
2. Check product README: `05-TELESCOPES/.../VERSION/V001/README.md`
3. Run validation script to identify problems
4. Refer to ECSS standards for aerospace practices
