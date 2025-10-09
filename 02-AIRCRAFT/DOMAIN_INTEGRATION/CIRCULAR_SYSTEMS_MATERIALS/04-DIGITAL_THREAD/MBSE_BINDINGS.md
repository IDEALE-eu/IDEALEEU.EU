# MBSE Bindings - Circular Systems Domain

## Overview

This document defines the bindings between the Model-Based Systems Engineering (MBSE) models and the physical folder structure for the CIRCULAR_SYSTEMS_MATERIALS domain.

## MBSE Model Location

**Primary Model**: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/)

**Model Type**: SysML v2 (Cameo Systems Modeler)

**Model Package**: `IDEALEEU::Aircraft::DomainIntegration::CircularSystemsMaterials`

## Package Structure

### Domain-Level Package
```
CircularSystemsMaterials [SysML Package]
├─ Requirements [Requirements Diagram]
│  ├─ DomainRequirements
│  └─ InterfaceRequirements
├─ Architecture [Block Definition Diagram]
│  ├─ SystemOfSystems
│  └─ IntegrationViews
├─ Behavior [Activity Diagram]
│  ├─ ThermalLoop
│  ├─ WaterLoop
│  ├─ HydrogenLoop
│  └─ MaterialCircularityLoop
└─ Verification [Parametric Diagram]
   ├─ EnergyBalance
   └─ MassBalance
```

## System-Level Bindings

### ATA-21 Air Conditioning
| MBSE Element | Type | Folder Path |
|--------------|------|-------------|
| `ATA21_ECS_System` | Block | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/) |
| `ATA21_IntegrationView` | Internal Block Diagram | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTEGRATION_VIEW.md](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTEGRATION_VIEW.md) |
| `ATA21_Pack` | Block | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-00_ENV_CONTROL_PACKS/](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-00_ENV_CONTROL_PACKS/) |
| `ATA21_TempControl` | Block | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-10_TEMPERATURE_CONTROL/](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-10_TEMPERATURE_CONTROL/) |
| `ATA21_PressControl` | Block | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-20_PRESSURIZATION_CONTROL/](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/SUBSYSTEMS/ATA-21-20_PRESSURIZATION_CONTROL/) |

### ATA-28 Fuel/H₂
| MBSE Element | Type | Folder Path |
|--------------|------|-------------|
| `ATA28_H2_System` | Block | [01-SYSTEMS/ATA-28_FUEL_H2/](../01-SYSTEMS/ATA-28_FUEL_H2/) |
| `ATA28_IntegrationView` | Internal Block Diagram | [01-SYSTEMS/ATA-28_FUEL_H2/INTEGRATION_VIEW.md](../01-SYSTEMS/ATA-28_FUEL_H2/INTEGRATION_VIEW.md) |
| `ATA28_CryoTank` | Block | [01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-00_CRYO_TANKS_VALVES/](../01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-00_CRYO_TANKS_VALVES/) |
| `ATA28_BOP_Controller` | Block | [01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-10_FUEL_MGMT_CONTROLLER/](../01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-10_FUEL_MGMT_CONTROLLER/) |
| `ATA28_ThermalHX` | Block | [01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-20_THERMAL_BALANCE_HX/](../01-SYSTEMS/ATA-28_FUEL_H2/SUBSYSTEMS/ATA-28-20_THERMAL_BALANCE_HX/) |

### ATA-38 Water/Waste
| MBSE Element | Type | Folder Path |
|--------------|------|-------------|
| `ATA38_Water_System` | Block | [01-SYSTEMS/ATA-38_WATER_WASTE/](../01-SYSTEMS/ATA-38_WATER_WASTE/) |
| `ATA38_IntegrationView` | Internal Block Diagram | [01-SYSTEMS/ATA-38_WATER_WASTE/INTEGRATION_VIEW.md](../01-SYSTEMS/ATA-38_WATER_WASTE/INTEGRATION_VIEW.md) |
| `ATA38_PotableWater` | Block | [01-SYSTEMS/ATA-38_WATER_WASTE/SUBSYSTEMS/ATA-38-00_POTABLE_WATER/](../01-SYSTEMS/ATA-38_WATER_WASTE/SUBSYSTEMS/ATA-38-00_POTABLE_WATER/) |
| `ATA38_WasteTreatment` | Block | [01-SYSTEMS/ATA-38_WATER_WASTE/SUBSYSTEMS/ATA-38-10_WASTE_TREATMENT_DISPOSAL/](../01-SYSTEMS/ATA-38_WATER_WASTE/SUBSYSTEMS/ATA-38-10_WASTE_TREATMENT_DISPOSAL/) |

### MTL-CIRCULARITY
| MBSE Element | Type | Folder Path |
|--------------|------|-------------|
| `MTL_Circularity_Domain` | Block | [01-SYSTEMS/MTL-CIRCULARITY/](../01-SYSTEMS/MTL-CIRCULARITY/) |
| `MTL_IntegrationView` | Internal Block Diagram | [01-SYSTEMS/MTL-CIRCULARITY/INTEGRATION_VIEW.md](../01-SYSTEMS/MTL-CIRCULARITY/INTEGRATION_VIEW.md) |
| `MTL_MaterialPassports` | Block | [01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-00_MATERIAL_PASSPORTS/](../01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-00_MATERIAL_PASSPORTS/) |
| `MTL_LCA_LCC` | Block | [01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-10_LCA_LCC_MODELS/](../01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-10_LCA_LCC_MODELS/) |
| `MTL_4R_Strategy` | Block | [01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-20_REUSE_REPAIR_RECYCLE/](../01-SYSTEMS/MTL-CIRCULARITY/SUBSYSTEMS/MTL-20_REUSE_REPAIR_RECYCLE/) |

## Interface Bindings

### Interface Matrix
| MBSE Element | Type | File Path |
|--------------|------|-----------|
| `InterfaceMatrix_Domain` | Table | [02-INTERFACES/INTERFACE_MATRIX.csv](../02-INTERFACES/INTERFACE_MATRIX.csv) |
| `InterfaceMatrix_ATA21` | Table | [01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTERFACE_MATRIX/21↔24_28_36_38_92.csv](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTERFACE_MATRIX/21↔24_28_36_38_92.csv) |
| `InterfaceMatrix_ATA28` | Table | [01-SYSTEMS/ATA-28_FUEL_H2/INTERFACE_MATRIX/28↔21_24_47_92.csv](../01-SYSTEMS/ATA-28_FUEL_H2/INTERFACE_MATRIX/28↔21_24_47_92.csv) |
| `InterfaceMatrix_ATA38` | Table | [01-SYSTEMS/ATA-38_WATER_WASTE/INTERFACE_MATRIX/38↔21_24_25_36_92.csv](../01-SYSTEMS/ATA-38_WATER_WASTE/INTERFACE_MATRIX/38↔21_24_25_36_92.csv) |
| `InterfaceMatrix_MTL` | Table | [01-SYSTEMS/MTL-CIRCULARITY/INTERFACE_MATRIX/MTL↔25_51_53_57_SUPPLY_CHAIN.csv](../01-SYSTEMS/MTL-CIRCULARITY/INTERFACE_MATRIX/MTL↔25_51_53_57_SUPPLY_CHAIN.csv) |

## Integration Views Bindings

| MBSE Element | Type | File Path |
|--------------|------|-----------|
| `SystemOfSystems` | Internal Block Diagram | [03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md](../03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md) |
| `EnergyMassBalance` | Parametric Diagram | [03-INTEGRATION_VIEWS/ENERGY_MASS_BALANCE.md](../03-INTEGRATION_VIEWS/ENERGY_MASS_BALANCE.md) |
| `ThermalLoop` | Activity Diagram | [03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md](../03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md#thermal-loop) |
| `WaterLoop` | Activity Diagram | [03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md](../03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md#water-loop) |
| `HydrogenLoop` | Activity Diagram | [03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md](../03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md#hydrogen-loop) |
| `MaterialCircularityLoop` | Activity Diagram | [03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md](../03-INTEGRATION_VIEWS/SYSTEM_OF_SYSTEMS.md#material-circularity-loop) |

## Requirements Traceability

### Domain Requirements
- **REQ-CSM-001**: Thermal efficiency > 80%
  - Allocated to: ATA-21, ATA-28
  - Verified by: [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/)
  
- **REQ-CSM-002**: Water reuse rate > 70%
  - Allocated to: ATA-21, ATA-38
  - Verified by: [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/)
  
- **REQ-CSM-003**: H₂ boil-off rate < 1.5% per day
  - Allocated to: ATA-21, ATA-28
  - Verified by: [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/)
  
- **REQ-CSM-004**: Material recyclability > 80% by weight
  - Allocated to: MTL-CIRCULARITY, All systems
  - Verified by: [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/)

### Interface Requirements
- Interface requirements auto-generated from SysML Interface Blocks
- Exported to: [02-INTERFACES/INTERFACE_MATRIX.csv](../02-INTERFACES/INTERFACE_MATRIX.csv)

## Model Synchronization

### Bi-directional Sync
1. **Model → Files**: Export interface matrix, requirements allocation
2. **Files → Model**: Import test results, verification data
3. **Frequency**: Weekly sync, triggered by baseline updates

### Automation
- Script: [00-PROGRAM/DIGITAL_THREAD/08-AUTOMATION/](../../../../00-PROGRAM/DIGITAL_THREAD/08-AUTOMATION/)
- CI/CD: Automated validation on commit
- Traceability: Automated traceability reports

## Verification Bindings

| MBSE Element | Type | File Path |
|--------------|------|-----------|
| `VVP_Plan` | Test Plan | [05-VERIFICATION/VVP_PLAN.md](../05-VERIFICATION/VVP_PLAN.md) |
| `TestCases_ThermalLoop` | Test Case | [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/) |
| `TestCases_WaterLoop` | Test Case | [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/) |
| `TestCases_H2Loop` | Test Case | [05-VERIFICATION/TEST_CASES/](../05-VERIFICATION/TEST_CASES/) |
| `TestResults` | Test Results | [05-VERIFICATION/RESULTS/](../05-VERIFICATION/RESULTS/) |

## Compliance Bindings

| MBSE Element | Type | File Path |
|--------------|------|-----------|
| `StandardsMap` | Requirements Matrix | [06-COMPLIANCE/STANDARDS_MAP.md](../06-COMPLIANCE/STANDARDS_MAP.md) |
| `ComplianceEvidence` | Evidence Links | [06-COMPLIANCE/EVIDENCE_LINKS.md](../06-COMPLIANCE/EVIDENCE_LINKS.md) |

## Change Management

### Model Changes
- ECR process: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- Model baselines aligned with configuration baselines
- Change log: [07-CHANGE_LOG/DOMAIN_CHANGE_LOG.csv](../07-CHANGE_LOG/DOMAIN_CHANGE_LOG.csv)

## Related Documents

- [00-PROGRAM/DIGITAL_THREAD/04-MBSE/](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/) - MBSE repository
- [TWIN_ANCHORS.md](TWIN_ANCHORS.md) - Digital twin integration
- [DATA_CONTRACTS/](DATA_CONTRACTS/) - Telemetry schemas
- [00-README.md](../00-README.md) - Domain overview
