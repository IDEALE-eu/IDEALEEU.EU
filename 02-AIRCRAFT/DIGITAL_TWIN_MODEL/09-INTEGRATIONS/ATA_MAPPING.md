# ATA_MAPPING

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 09-INTEGRATIONS > ATA_MAPPING**

**Critical**: Model ↔ ATA chapter, fidelity, owner (CSV format).

## Purpose

Map digital twin models to ATA (Air Transport Association) chapters for traceability and configuration management.

## CSV Format

See `ATA_MAPPING.csv` for the full mapping table.

| Column | Description |
|--------|-------------|
| **ata_chapter** | ATA chapter (e.g., "ATA-28") |
| **ata_section** | ATA section (e.g., "28-21 H2 Tank") |
| **model_id** | Twin model identifier |
| **model_path** | Path to model file |
| **fidelity_level** | Model fidelity (L1-L5) |
| **owner** | Responsible engineer/team |
| **criticality** | Safety level (A/B/C/D) |
| **status** | Development status (dev/validated/production) |

## Example Mapping

```csv
ata_chapter,ata_section,model_id,model_path,fidelity_level,owner,criticality,status
ATA-21,21-00 Air Conditioning,THERMAL_CABIN_V1.0,02-MODELS/PHYSICS/THERMAL/CABIN/,L3,Thermal Team,C,validated
ATA-27,27-10 Flight Controls,CONTROL_LOGIC_AUTOPILOT_V1.0,02-MODELS/BEHAVIORAL/CONTROL_LOGIC/AUTOPILOT/,L5,FCS Team,A,production
ATA-28,28-21 H2 Tank,H2_ENERGY_TANK_BOP_V1.0,02-MODELS/PHYSICS/ENERGY_H2/TANK_MODELS/,L4,H2 Team,B,production
ATA-28,28-22 H2 Leak Detection,ANOMALY_DETECTOR_H2_LEAK_V1.2.3,02-MODELS/DATA_DRIVEN/ANOMALY_DETECTORS/,L5,Data Science Team,A,production
ATA-51,51-00 Structures,STRUCT_FEM_REDUCED_V1.0,02-MODELS/PHYSICS/STRUCTURES/FEM_MODELS/,L3,Structures Team,B,validated
ATA-53,53-00 Fuselage,STRUCT_FUSELAGE_FATIGUE_V1.0,02-MODELS/PHYSICS/STRUCTURES/FATIGUE/,L4,Structures Team,B,validated
ATA-55,55-00 Stabilizers,AERO_STABILIZER_V1.0,02-MODELS/PHYSICS/AERODYNAMICS/,L4,Aero Team,B,validated
ATA-57,57-00 Wings,AERO_WING_CFD_SURROGATE_V1.2,02-MODELS/PHYSICS/AERODYNAMICS/CFD_SURROGATES/,L4,Aero Team,B,production
ATA-70,70-00 Engine,PROPULSION_ENGINE_PERF_V1.0,02-MODELS/PHYSICS/PROPULSION/ENGINE_MODELS/,L5,Propulsion Team,B,production
ATA-76,76-00 Engine Controls,CONTROL_LOGIC_EMS_V1.0,02-MODELS/BEHAVIORAL/CONTROL_LOGIC/EMS/,L5,Propulsion Team,B,production
```

## ATA Chapter Coverage

### Primary ATA Chapters Covered

- **ATA-21**: Air Conditioning (thermal models)
- **ATA-22**: Auto Flight (autopilot, FMS)
- **ATA-27**: Flight Controls (control surfaces, FCS)
- **ATA-28**: Fuel (H₂ fuel system)
- **ATA-36**: Pneumatic (bleed air, pressurization)
- **ATA-42**: Integrated Modular Avionics (IMA health)
- **ATA-51**: Structures (general)
- **ATA-53**: Fuselage
- **ATA-55**: Stabilizers
- **ATA-57**: Wings
- **ATA-70**: Engine (general)
- **ATA-71-79**: Engine systems (fuel, ignition, exhaust, oil, etc.)
- **ATA-76**: Engine Controls (FADEC, EMS)
- **ATA-80**: Starting

### Secondary ATA Chapters (Planned)

- **ATA-24**: Electrical Power
- **ATA-30**: Ice & Rain Protection
- **ATA-49**: Auxiliary Power Unit (APU)

## Usage

### For Configuration Management
- Link twin models to aircraft configuration items (CIs)
- Track model status and ownership

### For Maintenance
- Link predictive maintenance models to ATA chapters
- Integrate with MRO system (see `MRO_LINKS.md`)

### For Certification
- Map models to certification requirements (e.g., CS-25, FAR-25)
- Evidence traceability (see `../06-VALIDATION_VERIFICATION/CERT_EVIDENCE_LINKS.md`)

## Related Documents

- **../../CONFIGURATION_BASE/** - Aircraft ATA configuration
- **MRO_LINKS.md** - MRO integration
- **../04-VERSIONING_CONFIG/MODEL_MANIFEST.yaml** - Model manifest

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
