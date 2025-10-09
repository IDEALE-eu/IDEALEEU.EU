# MBSE Bindings

## Overview

This document maps Model-Based Systems Engineering (MBSE) elements to physical implementation in the GENERATION_PROPULSION_ENERGY domain.

## SysML Model Structure

### Domain-Level Model
- **Model Location**: `MBSE://DOMAINS/GENERATION_PROPULSION_ENERGY/`
- **Tool**: Cameo Systems Modeler (or equivalent)
- **Version Control**: Linked to Git repository

### Model Organization

```
GENERATION_PROPULSION_ENERGY (Package)
├─ Requirements (Package)
│  ├─ Functional Requirements
│  ├─ Performance Requirements
│  ├─ Interface Requirements
│  └─ Safety Requirements
├─ Structure (Package)
│  ├─ System BDD (Block Definition Diagrams)
│  ├─ System IBD (Internal Block Diagrams)
│  └─ Component Hierarchy
├─ Behavior (Package)
│  ├─ Activity Diagrams (Power flow, fuel flow)
│  ├─ State Machines (System modes)
│  └─ Sequence Diagrams (Start sequence, shutdown)
└─ Analysis (Package)
   ├─ Parametric Diagrams (Power budget, thermal analysis)
   └─ Trade Studies
```

## SysML to Physical Mapping

### Block Definition Diagrams (BDD)

| SysML Block | Physical Location | PLM Reference |
|-------------|------------------|---------------|
| `ElectricalPowerSystem` | `01-SYSTEMS/ATA-24_ELECTRICAL_POWER/` | PLM://SYSTEMS/ATA-24 |
| `Generator` | `01-SYSTEMS/ATA-24_ELECTRICAL_POWER/SUBSYSTEMS/ATA-24-10_GENERATORS_STARTER-GENS/` | PLM://PARTS/GEN-24-1000-A |
| `Battery` | `01-SYSTEMS/ATA-24_ELECTRICAL_POWER/SUBSYSTEMS/ATA-24-20_BATTERIES_ENERGY_STORAGE/` | PLM://PARTS/BAT-24-2000-A |
| `EnergyManagementController` | `01-SYSTEMS/ATA-24_ELECTRICAL_POWER/SUBSYSTEMS/ATA-24-50_ENERGY_MANAGEMENT_CONTROLLER/` | PLM://PARTS/EMC-24-5000-A |
| `APU_System` | `01-SYSTEMS/ATA-49_APU/` | PLM://SYSTEMS/ATA-49 |
| `APU_Core` | `01-SYSTEMS/ATA-49_APU/SUBSYSTEMS/ATA-49-10_APU_CORE/` | PLM://PARTS/APU-49-1000-A |
| `Engine` | `01-SYSTEMS/ATA-72_ENGINE/` | PLM://SYSTEMS/ATA-72 |
| `FADEC` | `01-SYSTEMS/ATA-73_ENGINE_FUEL_CONTROL/SUBSYSTEMS/ATA-73-10_FADEC/` | PLM://PARTS/FADEC-73-1000-A |
| `IgnitionSystem` | `01-SYSTEMS/ATA-74_IGNITION/` | PLM://SYSTEMS/ATA-74 |
| `BleedAirSystem` | `01-SYSTEMS/ATA-75_BLEED_AIR/` | PLM://SYSTEMS/ATA-75 |
| `EngineControls` | `01-SYSTEMS/ATA-76_ENGINE_CONTROLS/` | PLM://SYSTEMS/ATA-76 |
| `EngineIndication` | `01-SYSTEMS/ATA-77_ENGINE_INDICATING/` | PLM://SYSTEMS/ATA-77 |
| `ExhaustSystem` | `01-SYSTEMS/ATA-78_EXHAUST/` | PLM://SYSTEMS/ATA-78 |
| `OilSystem` | `01-SYSTEMS/ATA-79_OIL/` | PLM://SYSTEMS/ATA-79 |
| `StartingSystem` | `01-SYSTEMS/ATA-80_STARTING/` | PLM://SYSTEMS/ATA-80 |

### Interface Definitions

| SysML Interface | ICD Reference | Physical Documentation |
|-----------------|---------------|------------------------|
| `ElectricalPowerInterface` | ICD-24-XX-POWER | `02-INTERFACES/ICD_LINKS.md` |
| `ARINC429_Interface` | ICD-XX-XX-ARINC429 | `02-INTERFACES/ICD_LINKS.md` |
| `ARINC664_Interface` | ICD-XX-XX-AFDX | `02-INTERFACES/ICD_LINKS.md` |
| `FuelInterface` | ICD-28-73-FUEL | `02-INTERFACES/ICD_LINKS.md` |
| `BleedAirInterface` | ICD-75-XX-BLEED | `02-INTERFACES/ICD_LINKS.md` |
| `MechanicalInterface` | ICD-72-XX-MECH | `02-INTERFACES/ICD_LINKS.md` |

### Requirements Traceability

| Requirement ID | SysML Requirement | Implementation | Verification |
|----------------|------------------|----------------|--------------|
| REQ-GPE-001 | Total electrical power generation ≥180 kVA | ATA-24 Generators | `05-VERIFICATION/TEST_CASES/TC-GPE-001` |
| REQ-GPE-002 | Emergency power available ≥30 min | ATA-24 Batteries | `05-VERIFICATION/TEST_CASES/TC-GPE-002` |
| REQ-GPE-003 | Engine thrust per specification | ATA-72 Engine | `05-VERIFICATION/TEST_CASES/TC-GPE-003` |
| REQ-GPE-004 | FADEC response time <50ms | ATA-73 FADEC | `05-VERIFICATION/TEST_CASES/TC-GPE-004` |
| REQ-GPE-005 | Bleed air temperature <260°C | ATA-75 Bleed System | `05-VERIFICATION/TEST_CASES/TC-GPE-005` |

## Activity Diagrams

### Energy Flow Activity
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/EnergyFlow_Activity`
- **Documentation**: `03-INTEGRATION_VIEWS/ENERGY_FLOW.md`

### Propulsion Chain Activity
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/PropulsionChain_Activity`
- **Documentation**: `03-INTEGRATION_VIEWS/PROPULSION_CHAIN.md`

### Engine Start Sequence
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/EngineStart_Sequence`
- **Documentation**: `01-SYSTEMS/ATA-80_STARTING/`

## State Machines

### Power System States
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/PowerSystem_StateMachine`
- **States**: Normal, Single Generator, Emergency, Ground
- **Documentation**: `01-SYSTEMS/ATA-24_ELECTRICAL_POWER/INTEGRATION_VIEW.md`

### Engine Operating States
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/Engine_StateMachine`
- **States**: Shutdown, Starting, Idle, Operating, Shutdown Sequence
- **Documentation**: `01-SYSTEMS/ATA-72_ENGINE/INTEGRATION_VIEW.md`

### APU States
- **SysML Model**: `MBSE://DOMAINS/GPE/Behavior/APU_StateMachine`
- **States**: Off, Starting, Running, Cooling Down, Fault
- **Documentation**: `01-SYSTEMS/ATA-49_APU/INTEGRATION_VIEW.md`

## Parametric Diagrams

### Power Budget Analysis
- **SysML Model**: `MBSE://DOMAINS/GPE/Analysis/PowerBudget_Parametric`
- **Constraints**: Power generation ≥ Power consumption + Margin
- **Template**: `08-TEMPLATES/POWER_BUDGET_TEMPLATE.xlsx`

### Thermal Analysis
- **SysML Model**: `MBSE://DOMAINS/GPE/Analysis/ThermalAnalysis_Parametric`
- **Documentation**: `03-INTEGRATION_VIEWS/THERMAL_POWER_COUPLING.md`

## Model Updates and Synchronization

### Change Process
1. Requirements change triggers model update
2. SysML model updated and reviewed
3. Physical documentation updated to match
4. Verification cases updated
5. Digital twin models synchronized

### Version Control
- SysML models: Teamwork Cloud (or equivalent)
- Documentation: Git repository
- Synchronization: Automated where possible, manual review required

## Tool Integration

### MBSE Tool
- **Primary**: Cameo Systems Modeler
- **Model Repository**: Teamwork Cloud
- **Export Formats**: XMI, HTML reports, diagrams (PNG/SVG)

### PLM Integration
- **PLM System**: (Specify system name)
- **Integration**: SysML blocks linked to PLM part numbers
- **Synchronization**: Bi-directional for part numbers and configurations

### Requirements Management
- **Tool**: DOORS, Jama, or integrated in SysML tool
- **Traceability**: Requirements ↔ Design ↔ Test ↔ Code (for software)

## Related Documents

- [Digital Twin Anchors](./TWIN_ANCHORS.md)
- [Data Contracts](./DATA_CONTRACTS/)
- [Verification Plan](../05-VERIFICATION/VVP_PLAN.md)

---

**Last Updated**: 2024-01-15
