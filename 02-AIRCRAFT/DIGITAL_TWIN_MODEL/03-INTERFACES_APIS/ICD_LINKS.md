# ICD_LINKS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 03-INTERFACES_APIS > ICD_LINKS**

Pointers to Interface Control Documents (ICDs) in configuration management.

## Purpose

Links digital twin interfaces to formal ICDs managed in configuration management.

## ICD References

### Digital Thread ICDs

| ICD ID | Title | Location | Version |
|--------|-------|----------|---------|
| **ICD-DT-001** | Digital Twin ↔ Operational Data Hub | `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-DT-001.md` | 1.2 |
| **ICD-DT-002** | Digital Twin ↔ MRO System | `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-DT-002.md` | 1.0 |
| **ICD-DT-003** | Digital Twin ↔ MBSE Repository | `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-DT-003.md` | 1.1 |
| **ICD-DT-004** | Digital Twin API (External) | `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-DT-004.md` | 1.0 |

### Aircraft System ICDs

| ICD ID | Title | Location | Version |
|--------|-------|----------|---------|
| **ICD-ATA-28-01** | H₂ Fuel System ↔ Digital Twin | `02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-INTERFACES/ICD-ATA-28-01.md` | 1.0 |
| **ICD-ATA-70-01** | Propulsion ↔ Digital Twin | `02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-INTERFACES/ICD-ATA-70-01.md` | 1.0 |
| **ICD-ATA-42-01** | IMA ↔ Digital Twin Edge Runtime | `02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-INTERFACES/ICD-ATA-42-01.md` | 1.0 |

## Interface Types

### Data Interfaces
- **Telemetry Ingestion**: Real-time sensor data (see `STREAMS/INPUTS/TELEMETRY_MAP.csv`)
- **KPI Output**: Health, RUL, energy metrics (see `STREAMS/OUTPUTS/KPIs_SCHEMA.yaml`)
- **Configuration Sync**: As-built/as-maintained configuration from CM

### Control Interfaces
- **API Gateway**: REST/gRPC endpoints (see `TWIN_API_SPEC.yaml`)
- **Model Deployment**: CI/CD pipeline for model updates
- **Alert Notification**: WebSocket pub/sub for anomalies

### Management Interfaces
- **Model Registry**: Version control, signing, deployment
- **Metrics Export**: Model health, prediction quality to monitoring systems

## Change Management

All ICD changes must follow the CCB (Configuration Control Board) process:
1. Propose change via CR (Change Request)
2. Impact analysis (affected systems, interfaces, tests)
3. CCB review and approval
4. Update ICD version
5. Notify all stakeholders

See `00-PROGRAM/CONFIG_MGMT/06-CHANGES/` for CR process.

## Related Documents

- **TWIN_API_SPEC.yaml** - Digital twin API specification
- **../09-INTEGRATIONS/** - Integration points with other systems
- **00-PROGRAM/CONFIG_MGMT/09-INTERFACES/** - Master ICD repository

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
