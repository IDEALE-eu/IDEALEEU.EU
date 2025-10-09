# SPACE-TELESCOPE Product Model

## Overview

This directory contains the complete systems engineering structure for a baseline space telescope following SPACE-T (STA) architecture. The structure implements a unified approach with systems, subsystems, and PLM/CAx artifacts organized according to aerospace industry best practices.

## Product Information

- **Product Family**: SPACE-TELESCOPE
- **Model**: BASELINE
- **Version**: V001
- **Architecture**: SPACE-T (STA - Space Transport Architecture)

## Directory Structure

```
VERSION/V001/
└─ SYSTEMS/
   ├─ XX-SYSTEM_NAME/
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ XX↔OTHERS.csv
   │  └─ SUBSYSTEMS/           (only for systems 70 and 71)
   │     └─ XX-YY_SUBSYS/
   │        ├─ README.md
   │        ├─ META.json
   │        ├─ PLM/
   │        │  ├─ EBOM_LINKS.md
   │        │  └─ CAx/
   │        │     ├─ CAD/  (Computer-Aided Design)
   │        │     ├─ CAE/  (Computer-Aided Engineering)
   │        │     ├─ CAM/  (Computer-Aided Manufacturing)
   │        │     ├─ CAI/  (Computer-Aided Inspection)
   │        │     ├─ CAV/  (Computer-Aided Verification)
   │        │     ├─ CAP/  (Computer-Aided Planning)
   │        │     ├─ CAS/  (Computer-Aided Simulation)
   │        │     └─ CMP/  (Configuration Management & Planning)
   │        ├─ DELs/
   │        ├─ PAx/
   │        ├─ SUPPLIERS/
   │        ├─ policy/
   │        └─ tests/
```

## Architecture Rules

### 1. PLM/CAx Location
**PLM/CAx artifacts exist ONLY in SUBSYSTEMS**, never at system or domain level.

- ✅ Allowed: `SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-10_PRIMARY_MIRROR/PLM/CAx/`
- ❌ Prohibited: `SYSTEMS/70-OPTICAL_SUBSYSTEMS/PLM/CAx/`

### 2. Software Placement
Software resides with its **host LRU (Line Replaceable Unit)**.

Example: Avionics software partitions are under `42-AVIONICS_CONTROL`.

### 3. EWIS Rule
**ALL electrical wiring** (harnesses, connectors, routing) is maintained **ONLY** in `92-EWIS_HARNESS`.

- Individual systems may reference connector types
- Actual wiring specifications, pinouts, and harness assemblies are in `92-EWIS_HARNESS`

### 4. Interface Management
Each system maintains an `INTERFACE_MATRIX/` directory with CSV files documenting interfaces with other systems.

**CSV Format:**
```csv
from_system,to_system,interface_type,icd_ref,signals/measures,thermal,mechanical,electrical,data_bus,harness,sw_api,safety_class,owner,status,notes
```

## Systems Catalog

### Structural Systems (50-57, 66)
- **51-PRIMARY_STRUCTURE** - Main telescope structure
- **52-ACCESS_HATCHES** - Service access and maintenance hatches
- **53-OPTICAL_TUBE_ASSEMBLY** - Optical tube structure
- **55-SECONDARY_SUPPORT** - Secondary mirror support structure
- **56-WINDOWS_DOMES** - Protective windows and domes
- **57-INSTRUMENT_BAYS** - Instrument mounting structure
- **66-DEPLOYABLE_OPTICS** - Deployable optical elements

### Optical Systems (70)
- **70-OPTICAL_SUBSYSTEMS** - Custom optical systems block (see below)

### Instruments (71)
- **71-INSTRUMENTS_PAYLOADS** - Science instruments (imager, spectrograph, coronagraph)

### Thermal & Environmental (15, 21, 30, 72, 75)
- **15-ENVIRONMENT_VIBRATION** - Vibration isolation and environment
- **21-THERMAL_CONTROL** - Active thermal control
- **30-ICE_DEW_PREVENTION** - Anti-contamination systems
- **72-CRYOGENIC_COOLING** - Cryogenic cooling systems
- **75-THERMAL_RADIATORS** - Passive thermal radiators

### Electrical & Power (24, 33, 78)
- **24-ELECTRICAL_POWER** - Power generation, storage, distribution
- **33-LIGHTS** - Lighting systems
- **78-BACKPLANE_ELECTRONICS** - Backplane electronics

### Data & Communications (31)
- **31-DATA_HANDLING** - Data acquisition, processing, storage

### Control & Navigation (32, 34, 42, 45)
- **32-POINTING_STABILIZATION** - Pointing and stabilization
- **34-NAVIGATION_ATTITUDE** - Navigation and attitude determination
- **42-AVIONICS_CONTROL** - Central avionics and control
- **45-HEALTH_MONITORING** - Health and status monitoring

### Actuation & Control (73, 76, 77)
- **73-FOCUS_ACTUATION** - Focus mechanism actuation
- **76-MIRROR_CONTROL** - Active mirror control
- **77-ALIGNMENT_SENSING** - Alignment sensors and metrology

### Support Systems (26, 79, 80, 84)
- **26-FIRE_SAFETY** - Fire detection and suppression
- **79-LUBRICATION** - Mechanism lubrication
- **80-STARTUP_SEQUENCING** - Startup and initialization sequences
- **84-PROPULSION** - Station-keeping propulsion (optional)

### Integration & Operations (01, 06, 92, 94, 99)
- **01-INTRO** - System introduction and overview
- **06-DIMENSIONS_ALIGNMENTS** - Dimensional control and alignments
- **92-EWIS_HARNESS** - Electrical wiring interconnection (centralized)
- **94-ELECTRONIC_COMPARTMENTS** - Electronics compartments
- **99-SCIENCE_OPERATIONS** - Science operations planning

## Custom Optical Systems Block (70-OPTICAL_SUBSYSTEMS)

System 70 is a **custom optics block** containing 8 subsystems with full PLM/CAx engineering artifacts:

### Optical Subsystems

1. **70-10_PRIMARY_MIRROR**
   - Primary mirror assembly
   - Coatings and surface treatments
   - Mounting and support interfaces

2. **70-20_SECONDARY_MIRROR**
   - Secondary mirror assembly
   - Spider/support structure interfaces

3. **70-30_TERTIARY_FLAT**
   - Tertiary flat mirror (if applicable)
   - Beam steering optics

4. **70-40_CORRECTORS_LENS**
   - Corrector optics
   - Lens assemblies
   - Anti-reflection coatings

5. **70-50_FILTERS_GRISMS**
   - Filter wheels and assemblies
   - Grism/disperser elements
   - Wavelength selection mechanisms

6. **70-60_DETECTOR_CRYOSTATS**
   - Detector assemblies
   - Cryogenic housings
   - Thermal interfaces

7. **70-70_WAVEFRONT_SENSORS**
   - Wavefront sensing optics
   - Fine guidance sensors
   - Alignment sensors

8. **70-80_CALIBRATION_SOURCES**
   - Internal calibration sources
   - Flat field illuminators
   - Wavelength calibration lamps

Each subsystem contains:
- Complete CAx artifacts (CAD, CAE, CAM, CAI, CAV, CAP, CAS, CMP)
- EBOM (Engineering Bill of Materials) links
- Subsystem-specific documentation
- Test and verification artifacts

## Instruments and Payloads (71-INSTRUMENTS_PAYLOADS)

System 71 contains 3 science instrument subsystems:

1. **71-10_IMAGER**
   - Wide-field or narrow-field imaging instrument
   - Filter mechanisms
   - Detector readout electronics

2. **71-20_SPECTROGRAPH**
   - Spectroscopic instrument
   - Dispersive elements
   - Multi-object or integral field capabilities

3. **71-30_CORONAGRAPH**
   - Coronagraphic instrument for exoplanet detection
   - Starlight suppression optics
   - Low-noise detectors

## Key Interfaces

### High-Level System Interactions

**Optical Systems (70)** interfaces with:
- 21-THERMAL_CONTROL (thermal stability)
- 32-POINTING_STABILIZATION (alignment)
- 45-HEALTH_MONITORING (performance)
- 51-PRIMARY_STRUCTURE (mechanical mounting)
- 55-SECONDARY_SUPPORT (secondary mount)
- 57-INSTRUMENT_BAYS (focal plane location)

**Instruments (71)** interfaces with:
- 24-ELECTRICAL_POWER (power supply)
- 31-DATA_HANDLING (science data)
- 70-OPTICAL_SUBSYSTEMS (optical feeds)
- 57-INSTRUMENT_BAYS (mounting)

**EWIS (92)** interfaces with:
- ALL systems (electrical interconnection)

## Scripts and Automation

### Creation Script
```bash
./scripts/create-telescope-systems.sh
```

Creates the complete telescope systems structure with:
- 34 systems following STA architecture
- Interface matrices with proper CSV headers
- Integration view templates
- Subsystems with full PLM/CAx for systems 70 and 71

### Validation Script
```bash
./scripts/validate-telescope-systems.sh
```

Validates:
- System structure completeness
- PLM/CAx only in subsystems (not at system level)
- Interface matrix CSV format
- Mandatory files (INTEGRATION_VIEW.md, META.json, etc.)
- EWIS centralization rule

## References

### Documentation
- **Architecture Rules**: `05-TELESCOPES/00-README.md`
- **Interface Control**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Standards**: `00-PROGRAM/STANDARDS/`

### Related Products
- AMPEL360-SPACE-T: Spacecraft bus reference
- Satellites (04): Orbital platform examples
- STM (09): Space station module patterns

## Compliance

This structure follows:
- **ECSS Standards** (European Cooperation for Space Standardization)
- **SPACE-T Architecture** (STA chapter sets A-M)
- **Unified Product Structure** (systems/subsystems/PLM pattern)

## Change Management

All structural changes must:
1. Maintain architecture rules (PLM in subsystems, SW with LRU, EWIS in 92)
2. Update interface matrices for affected systems
3. Pass validation script checks
4. Document in system INTEGRATION_VIEW.md files

## Version History

- **V001**: Initial baseline structure with 34 systems, optical and instrument subsystems
