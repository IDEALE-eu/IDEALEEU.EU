# SPACE-TELESCOPE Product Model

## Overview

This directory contains the complete systems engineering structure for a baseline space telescope following SPACE-T (STA) architecture. The structure implements a unified approach with systems, subsystems, and PLM/CAx artifacts organized according to aerospace industry best practices.

**Quick Links:**
- [Quick Reference Guide](./QUICK_REFERENCE.md) - Systems tables and common tasks
- [All Systems](./SYSTEMS/) - Browse all 34 telescope systems
- [Domain README](../../../../../00-README.md) - Telescope domain overview
- [Scripts](#scripts-and-automation) - Creation and validation scripts

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

> **Quick Navigation:** [Jump to Custom Optics Block](#custom-optical-systems-block-70-optical_subsystems) | [Jump to Instruments](#instruments-and-payloads-71-instruments_payloads) | [View Quick Reference](./QUICK_REFERENCE.md)

### Structural Systems (50-57, 66)
- **[51-PRIMARY_STRUCTURE](./SYSTEMS/51-PRIMARY_STRUCTURE/)** - Main telescope structure ([integration view](./SYSTEMS/51-PRIMARY_STRUCTURE/INTEGRATION_VIEW.md))
- **[52-ACCESS_HATCHES](./SYSTEMS/52-ACCESS_HATCHES/)** - Service access and maintenance hatches ([integration view](./SYSTEMS/52-ACCESS_HATCHES/INTEGRATION_VIEW.md))
- **[53-OPTICAL_TUBE_ASSEMBLY](./SYSTEMS/53-OPTICAL_TUBE_ASSEMBLY/)** - Optical tube structure ([integration view](./SYSTEMS/53-OPTICAL_TUBE_ASSEMBLY/INTEGRATION_VIEW.md))
- **[55-SECONDARY_SUPPORT](./SYSTEMS/55-SECONDARY_SUPPORT/)** - Secondary mirror support structure ([integration view](./SYSTEMS/55-SECONDARY_SUPPORT/INTEGRATION_VIEW.md))
- **[56-WINDOWS_DOMES](./SYSTEMS/56-WINDOWS_DOMES/)** - Protective windows and domes ([integration view](./SYSTEMS/56-WINDOWS_DOMES/INTEGRATION_VIEW.md))
- **[57-INSTRUMENT_BAYS](./SYSTEMS/57-INSTRUMENT_BAYS/)** - Instrument mounting structure ([integration view](./SYSTEMS/57-INSTRUMENT_BAYS/INTEGRATION_VIEW.md))
- **[66-DEPLOYABLE_OPTICS](./SYSTEMS/66-DEPLOYABLE_OPTICS/)** - Deployable optical elements ([integration view](./SYSTEMS/66-DEPLOYABLE_OPTICS/INTEGRATION_VIEW.md))

### Optical Systems (70)
- **[70-OPTICAL_SUBSYSTEMS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/)** - Custom optical systems block ([see detailed section below](#custom-optical-systems-block-70-optical_subsystems))

### Instruments (71)
- **[71-INSTRUMENTS_PAYLOADS](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/)** - Science instruments ([see detailed section below](#instruments-and-payloads-71-instruments_payloads))

### Thermal & Environmental (15, 21, 30, 72, 75)
- **[15-ENVIRONMENT_VIBRATION](./SYSTEMS/15-ENVIRONMENT_VIBRATION/)** - Vibration isolation and environment ([integration view](./SYSTEMS/15-ENVIRONMENT_VIBRATION/INTEGRATION_VIEW.md))
- **[21-THERMAL_CONTROL](./SYSTEMS/21-THERMAL_CONTROL/)** - Active thermal control ([integration view](./SYSTEMS/21-THERMAL_CONTROL/INTEGRATION_VIEW.md))
- **[30-ICE_DEW_PREVENTION](./SYSTEMS/30-ICE_DEW_PREVENTION/)** - Anti-contamination systems ([integration view](./SYSTEMS/30-ICE_DEW_PREVENTION/INTEGRATION_VIEW.md))
- **[72-CRYOGENIC_COOLING](./SYSTEMS/72-CRYOGENIC_COOLING/)** - Cryogenic cooling systems ([integration view](./SYSTEMS/72-CRYOGENIC_COOLING/INTEGRATION_VIEW.md))
- **[75-THERMAL_RADIATORS](./SYSTEMS/75-THERMAL_RADIATORS/)** - Passive thermal radiators ([integration view](./SYSTEMS/75-THERMAL_RADIATORS/INTEGRATION_VIEW.md))

### Electrical & Power (24, 33, 78)
- **[24-ELECTRICAL_POWER](./SYSTEMS/24-ELECTRICAL_POWER/)** - Power generation, storage, distribution ([integration view](./SYSTEMS/24-ELECTRICAL_POWER/INTEGRATION_VIEW.md))
- **[33-LIGHTS](./SYSTEMS/33-LIGHTS/)** - Lighting systems ([integration view](./SYSTEMS/33-LIGHTS/INTEGRATION_VIEW.md))
- **[78-BACKPLANE_ELECTRONICS](./SYSTEMS/78-BACKPLANE_ELECTRONICS/)** - Backplane electronics ([integration view](./SYSTEMS/78-BACKPLANE_ELECTRONICS/INTEGRATION_VIEW.md))

### Data & Communications (31)
- **[31-DATA_HANDLING](./SYSTEMS/31-DATA_HANDLING/)** - Data acquisition, processing, storage ([integration view](./SYSTEMS/31-DATA_HANDLING/INTEGRATION_VIEW.md))

### Control & Navigation (32, 34, 42, 45)
- **[32-POINTING_STABILIZATION](./SYSTEMS/32-POINTING_STABILIZATION/)** - Pointing and stabilization ([integration view](./SYSTEMS/32-POINTING_STABILIZATION/INTEGRATION_VIEW.md))
- **[34-NAVIGATION_ATTITUDE](./SYSTEMS/34-NAVIGATION_ATTITUDE/)** - Navigation and attitude determination ([integration view](./SYSTEMS/34-NAVIGATION_ATTITUDE/INTEGRATION_VIEW.md))
- **[42-AVIONICS_CONTROL](./SYSTEMS/42-AVIONICS_CONTROL/)** - Central avionics and control ([integration view](./SYSTEMS/42-AVIONICS_CONTROL/INTEGRATION_VIEW.md))
- **[45-HEALTH_MONITORING](./SYSTEMS/45-HEALTH_MONITORING/)** - Health and status monitoring ([integration view](./SYSTEMS/45-HEALTH_MONITORING/INTEGRATION_VIEW.md))

### Actuation & Control (73, 76, 77)
- **[73-FOCUS_ACTUATION](./SYSTEMS/73-FOCUS_ACTUATION/)** - Focus mechanism actuation ([integration view](./SYSTEMS/73-FOCUS_ACTUATION/INTEGRATION_VIEW.md))
- **[76-MIRROR_CONTROL](./SYSTEMS/76-MIRROR_CONTROL/)** - Active mirror control ([integration view](./SYSTEMS/76-MIRROR_CONTROL/INTEGRATION_VIEW.md))
- **[77-ALIGNMENT_SENSING](./SYSTEMS/77-ALIGNMENT_SENSING/)** - Alignment sensors and metrology ([integration view](./SYSTEMS/77-ALIGNMENT_SENSING/INTEGRATION_VIEW.md))

### Support Systems (26, 79, 80, 84)
- **[26-FIRE_SAFETY](./SYSTEMS/26-FIRE_SAFETY/)** - Fire detection and suppression ([integration view](./SYSTEMS/26-FIRE_SAFETY/INTEGRATION_VIEW.md))
- **[79-LUBRICATION](./SYSTEMS/79-LUBRICATION/)** - Mechanism lubrication ([integration view](./SYSTEMS/79-LUBRICATION/INTEGRATION_VIEW.md))
- **[80-STARTUP_SEQUENCING](./SYSTEMS/80-STARTUP_SEQUENCING/)** - Startup and initialization sequences ([integration view](./SYSTEMS/80-STARTUP_SEQUENCING/INTEGRATION_VIEW.md))
- **[84-PROPULSION](./SYSTEMS/84-PROPULSION/)** - Station-keeping propulsion (optional) ([integration view](./SYSTEMS/84-PROPULSION/INTEGRATION_VIEW.md))

### Integration & Operations (01, 06, 92, 94, 99)
- **[01-INTRO](./SYSTEMS/01-INTRO/)** - System introduction and overview ([integration view](./SYSTEMS/01-INTRO/INTEGRATION_VIEW.md))
- **[06-DIMENSIONS_ALIGNMENTS](./SYSTEMS/06-DIMENSIONS_ALIGNMENTS/)** - Dimensional control and alignments ([integration view](./SYSTEMS/06-DIMENSIONS_ALIGNMENTS/INTEGRATION_VIEW.md))
- **[92-EWIS_HARNESS](./SYSTEMS/92-EWIS_HARNESS/)** - Electrical wiring interconnection (centralized) ([integration view](./SYSTEMS/92-EWIS_HARNESS/INTEGRATION_VIEW.md))
- **[94-ELECTRONIC_COMPARTMENTS](./SYSTEMS/94-ELECTRONIC_COMPARTMENTS/)** - Electronics compartments ([integration view](./SYSTEMS/94-ELECTRONIC_COMPARTMENTS/INTEGRATION_VIEW.md))
- **[99-SCIENCE_OPERATIONS](./SYSTEMS/99-SCIENCE_OPERATIONS/)** - Science operations planning ([integration view](./SYSTEMS/99-SCIENCE_OPERATIONS/INTEGRATION_VIEW.md))

## Custom Optical Systems Block (70-OPTICAL_SUBSYSTEMS)

> **System Directory:** [SYSTEMS/70-OPTICAL_SUBSYSTEMS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/) | **[Integration View](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/INTEGRATION_VIEW.md)** | **[Interface Matrix](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/INTERFACE_MATRIX/)**

System 70 is a **custom optics block** containing 8 subsystems with full PLM/CAx engineering artifacts:

### Optical Subsystems

1. **[70-10_PRIMARY_MIRROR](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-10_PRIMARY_MIRROR/)**
   - Primary mirror assembly
   - Coatings and surface treatments
   - Mounting and support interfaces
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-10_PRIMARY_MIRROR/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-10_PRIMARY_MIRROR/PLM/CAx/)

2. **[70-20_SECONDARY_MIRROR](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-20_SECONDARY_MIRROR/)**
   - Secondary mirror assembly
   - Spider/support structure interfaces
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-20_SECONDARY_MIRROR/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-20_SECONDARY_MIRROR/PLM/CAx/)

3. **[70-30_TERTIARY_FLAT](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-30_TERTIARY_FLAT/)**
   - Tertiary flat mirror (if applicable)
   - Beam steering optics
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-30_TERTIARY_FLAT/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-30_TERTIARY_FLAT/PLM/CAx/)

4. **[70-40_CORRECTORS_LENS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-40_CORRECTORS_LENS/)**
   - Corrector optics
   - Lens assemblies
   - Anti-reflection coatings
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-40_CORRECTORS_LENS/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-40_CORRECTORS_LENS/PLM/CAx/)

5. **[70-50_FILTERS_GRISMS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-50_FILTERS_GRISMS/)**
   - Filter wheels and assemblies
   - Grism/disperser elements
   - Wavelength selection mechanisms
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-50_FILTERS_GRISMS/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-50_FILTERS_GRISMS/PLM/CAx/)

6. **[70-60_DETECTOR_CRYOSTATS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-60_DETECTOR_CRYOSTATS/)**
   - Detector assemblies
   - Cryogenic housings
   - Thermal interfaces
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-60_DETECTOR_CRYOSTATS/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-60_DETECTOR_CRYOSTATS/PLM/CAx/)

7. **[70-70_WAVEFRONT_SENSORS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-70_WAVEFRONT_SENSORS/)**
   - Wavefront sensing optics
   - Fine guidance sensors
   - Alignment sensors
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-70_WAVEFRONT_SENSORS/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-70_WAVEFRONT_SENSORS/PLM/CAx/)

8. **[70-80_CALIBRATION_SOURCES](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-80_CALIBRATION_SOURCES/)**
   - Internal calibration sources
   - Flat field illuminators
   - Wavelength calibration lamps
   - [README](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-80_CALIBRATION_SOURCES/README.md) | [PLM/CAx](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-80_CALIBRATION_SOURCES/PLM/CAx/)

Each subsystem contains:
- Complete CAx artifacts (CAD, CAE, CAM, CAI, CAV, CAP, CAS, CMP)
- EBOM (Engineering Bill of Materials) links
- Subsystem-specific documentation
- Test and verification artifacts

**Related Systems:**
- [21-THERMAL_CONTROL](./SYSTEMS/21-THERMAL_CONTROL/) - Thermal interfaces
- [32-POINTING_STABILIZATION](./SYSTEMS/32-POINTING_STABILIZATION/) - Alignment requirements
- [51-PRIMARY_STRUCTURE](./SYSTEMS/51-PRIMARY_STRUCTURE/) - Mechanical mounting

## Instruments and Payloads (71-INSTRUMENTS_PAYLOADS)

> **System Directory:** [SYSTEMS/71-INSTRUMENTS_PAYLOADS](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/) | **[Integration View](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/INTEGRATION_VIEW.md)** | **[Interface Matrix](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/INTERFACE_MATRIX/)**

System 71 contains 3 science instrument subsystems:

1. **[71-10_IMAGER](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-10_IMAGER/)**
   - Wide-field or narrow-field imaging instrument
   - Filter mechanisms
   - Detector readout electronics
   - [README](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-10_IMAGER/README.md) | [PLM/CAx](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-10_IMAGER/PLM/CAx/)

2. **[71-20_SPECTROGRAPH](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-20_SPECTROGRAPH/)**
   - Spectroscopic instrument
   - Dispersive elements
   - Multi-object or integral field capabilities
   - [README](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-20_SPECTROGRAPH/README.md) | [PLM/CAx](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-20_SPECTROGRAPH/PLM/CAx/)

3. **[71-30_CORONAGRAPH](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-30_CORONAGRAPH/)**
   - Coronagraphic instrument for exoplanet detection
   - Starlight suppression optics
   - Low-noise detectors
   - [README](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-30_CORONAGRAPH/README.md) | [PLM/CAx](./SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/71-30_CORONAGRAPH/PLM/CAx/)

**Related Systems:**
- [24-ELECTRICAL_POWER](./SYSTEMS/24-ELECTRICAL_POWER/) - Power supply
- [31-DATA_HANDLING](./SYSTEMS/31-DATA_HANDLING/) - Science data processing
- [70-OPTICAL_SUBSYSTEMS](./SYSTEMS/70-OPTICAL_SUBSYSTEMS/) - Optical feeds
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
