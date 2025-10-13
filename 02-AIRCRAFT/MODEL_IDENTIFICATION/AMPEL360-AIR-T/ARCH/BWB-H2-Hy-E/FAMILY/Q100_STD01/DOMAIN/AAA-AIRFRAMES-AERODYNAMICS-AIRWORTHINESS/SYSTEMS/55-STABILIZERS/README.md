# 55-STABILIZERS — README

**Path:** `…/SYSTEMS/55-STABILIZERS/`

## Purpose
Define, design, and certify the **stabilizers** of the BWB aircraft, including horizontal and vertical stabilizer primary structures, leading/trailing edge panels, ribs, spars, attach fittings, access panels, anti-ice provisions, sensor brackets, and associated procedures.

## Scope
**Includes**
- Horizontal stabilizer primary structure (55-10)
- Vertical stabilizer primary structure (55-20)
- Leading/trailing edge panels and skins (55-30)
- Ribs, spars, and stringers (55-40)
- Attach fittings, fairings, and fillets (55-50)
- Access panels and inspection covers (55-60)
- Anti-ice provisions with interfaces to ATA-30 (55-70)
- Sensor brackets and EWIS provisions with interfaces to ATA-92 (55-80)
- Procedures and training (55-90)

**Excludes**
- Flight control surfaces (ATA-27)
- Actuators and hydraulic systems (ATA-29)
- Ice detection systems (handled in ATA-30)

## Key interfaces
- **24-ELECTRICAL:** power for anti-ice and sensors
- **28-FUEL:** tank interfaces and load paths
- **30-ICE-RAIN:** anti-ice systems integration
- **31-INSTRUMENTS:** sensor mounting and alignment
- **36-PNEUMATICS:** bleed air for anti-ice
- **42-IMA:** sensor data interfaces
- **53-FUSELAGE-STRUCTURES:** primary attachment points and load transfer
- **57-WINGS:** aerodynamic continuity and load distribution
- **92-EWIS:** cable routing and protection
- **93-FUEL-SYSTEM:** fuel tank integration

## Deliverables (DoD Q100)
- **CAD:** released PART/ASM, PDF/A drawings, STEP AP242
- **CAE:** load cases, correlation, margins (strength, flutter, modal)
- **CAO:** variant study and minimal Pareto set
- **CAM:** manufacturing routes and base tooling
- **CAI:** signed interface matrix
- **CAV/CAS:** verification and initial service docs
- **CMP:** UTCS traceability and linked EBOM

## Folder structure
- [`SUBSYSTEMS/55-00_STANDARDS_GENERAL/`](./SUBSYSTEMS/55-00_STANDARDS_GENERAL/)
- [`SUBSYSTEMS/55-10_HORIZONTAL_STAB_PRIMARY_STRUCTURE/`](./SUBSYSTEMS/55-10_HORIZONTAL_STAB_PRIMARY_STRUCTURE/)
- [`SUBSYSTEMS/55-20_VERTICAL_STAB_PRIMARY_STRUCTURE/`](./SUBSYSTEMS/55-20_VERTICAL_STAB_PRIMARY_STRUCTURE/)
- [`SUBSYSTEMS/55-30_LE_TE_PANELS_SKINS/`](./SUBSYSTEMS/55-30_LE_TE_PANELS_SKINS/)
- [`SUBSYSTEMS/55-40_RIBS_SPARS_STRINGERS/`](./SUBSYSTEMS/55-40_RIBS_SPARS_STRINGERS/)
- [`SUBSYSTEMS/55-50_ATTACH_FITTINGS_FAIRINGS_FILLET/`](./SUBSYSTEMS/55-50_ATTACH_FITTINGS_FAIRINGS_FILLET/)
- [`SUBSYSTEMS/55-60_ACCESS_PANELS_INSPECTION_COVERS/`](./SUBSYSTEMS/55-60_ACCESS_PANELS_INSPECTION_COVERS/)
- [`SUBSYSTEMS/55-70_ANTIICE_PROVISIONS_IF_TO_30/`](./SUBSYSTEMS/55-70_ANTIICE_PROVISIONS_IF_TO_30/)
- [`SUBSYSTEMS/55-80_SENSOR_BRACKETS_EWIS_PROVISIONS_IF_92/`](./SUBSYSTEMS/55-80_SENSOR_BRACKETS_EWIS_PROVISIONS_IF_92/)
- [`SUBSYSTEMS/55-90_PROCEDURES_TRAINING/`](./SUBSYSTEMS/55-90_PROCEDURES_TRAINING/)
- [`INTERFACE_MATRIX/`](./INTERFACE_MATRIX/) — ICDs and cross-references
- [`INTEGRATION_VIEW.md`](./INTEGRATION_VIEW.md) — System-level integration context

## Conventions
- **CAD names**  
  - Parts: `55-XX_PART_<NAME>_v##.ext`  
  - Assemblies: `55-XX_ASM_<NAME>_v##.ext`  
  - Drawings: `55-XX_DWG_<TYPE>_<NAME>_<D####>.pdf`
- **Units:** millimeters. **References:** `FS/WL/BL` and datums `A/B/C`.
- **Export:** STEP **AP242** mandatory; JT for visual reviews.

## RASCI (generic)
- **R:** 55-STABILIZERS Lead  
- **A:** Chief Airframe  
- **S:** CAD/CAE/CAO/CAM owners  
- **C:** 24, 28, 30, 31, 36, 42, 53, 57, 92, 93  
- **I:** Quality/Certification

## Links
- [SUBSYSTEMS](./SUBSYSTEMS/)  
- [INTERFACE_MATRIX](./INTERFACE_MATRIX/)  
- [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md)

