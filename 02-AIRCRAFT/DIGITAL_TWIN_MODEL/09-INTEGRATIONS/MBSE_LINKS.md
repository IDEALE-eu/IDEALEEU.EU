# MBSE_LINKS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 09-INTEGRATIONS > MBSE_LINKS**

SysML ↔ twin ID mapping, linking to MBSE repository.

## Purpose

Establish traceability between MBSE system models and digital twin models.

## Integration Points

### MBSE → Digital Twin

| MBSE Element | Type | Digital Twin Model | Mapping |
|--------------|------|-------------------|---------|
| **Aircraft System** | Block | Overall Twin | Root-level twin instance |
| **H₂ Fuel System** | Block | `02-MODELS/PHYSICS/ENERGY_H2/` | System-level model |
| **Propulsion** | Block | `02-MODELS/PHYSICS/PROPULSION/` | System-level model |
| **Flight Control** | Block | `02-MODELS/BEHAVIORAL/CONTROL_LOGIC/` | Behavioral model |
| **IMA Health Monitoring** | State Machine | `02-MODELS/BEHAVIORAL/STATE_MACHINES/IMA_HEALTH/` | State machine |
| **H₂ Tank** | Part | `02-MODELS/PHYSICS/ENERGY_H2/TANK_MODELS/` | Component model |

### Requirements Traceability

**MBSE Requirement → Twin Validation**:
- Each MBSE requirement (e.g., REQ-H2-001: "Tank shall maintain pressure 1-350 bar")
- Linked to twin validation test case (e.g., TC_H2_001: "Verify tank pressure model accuracy")
- See `../06-VALIDATION_VERIFICATION/TEST_CASES/`

### MBSE Repository Location

- **Primary**: `00-PROGRAM/DIGITAL_THREAD/04-MBSE/SYSML_MODELS/`
- **Baseline Links**: `00-PROGRAM/DIGITAL_THREAD/04-MBSE/MODEL_BASELINES/`

## Synchronization

### Model Structure Sync
- Twin model structure reflects MBSE system hierarchy
- Changes to MBSE architecture → update twin structure

### Parameter Sync
- MBSE design parameters → twin baseline parameters
- See `../08-SYNCHRONISATION/BASELINE_SYNC.md`

## Tools

- **MBSE Tool**: Cameo Systems Modeler, MagicDraw, or equivalent
- **SysML**: SysML 1.6 or 2.0
- **Export Format**: XMI (XML Metadata Interchange)

## Related Documents

- **../01-ARCHITECTURE/TWIN_SCOPE.md** - Twin types and use cases
- **00-PROGRAM/DIGITAL_THREAD/04-MBSE/** - MBSE repository
- **../08-SYNCHRONISATION/BASELINE_SYNC.md** - Baseline synchronization

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
