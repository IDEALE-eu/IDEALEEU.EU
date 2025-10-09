# Data Contracts - Circular Systems Domain

## Overview

This directory contains data contracts (schemas) for telemetry signals, events, and data exchange within the CIRCULAR_SYSTEMS_MATERIALS domain. Data contracts ensure consistency and compatibility across systems, digital twin, and fleet learning.

## Purpose

Data contracts define:
- **Signal Names**: Standardized telemetry signal names
- **Units**: Engineering units for all measurements
- **Sample Rates**: Expected data frequency
- **Ranges**: Valid data ranges for validation
- **EBOM References**: Links to physical components

## Contents

- **TELEMETRY_SCHEMA.yaml** - Continuous sensor signals and system parameters
- **EVENTS_SCHEMA.yaml** - Discrete events, fault codes, and maintenance tags
- **README.md** - This file

## Schema Files

### Telemetry Schema
[TELEMETRY_SCHEMA.yaml](TELEMETRY_SCHEMA.yaml) - Continuous signals for:
- ATA-21 Air Conditioning (temperatures, pressures, flows)
- ATA-28 Fuel/H₂ (tank level, boil-off rate, temperatures)
- ATA-38 Water/Waste (water levels, quality parameters, flows)
- MTL-CIRCULARITY (component usage, lifecycle data)

### Events Schema
[EVENTS_SCHEMA.yaml](EVENTS_SCHEMA.yaml) - Discrete events for:
- System state changes (startup, shutdown, mode changes)
- Fault conditions (warnings, cautions, advisories)
- Maintenance events (component replacement, inspections)
- Performance milestones (efficiency thresholds, lifecycle events)

## Data Contract Principles

1. **Single Source of Truth**: Each signal has one authoritative definition
2. **Backward Compatibility**: Schema changes maintain compatibility
3. **Validation**: All data validated against schema at ingestion
4. **Traceability**: Signals linked to EBOM, requirements, and digital twin
5. **Privacy**: No personal or proprietary data in telemetry

## Signal Naming Convention

### Format
`{SYSTEM}_{SUBSYSTEM}_{COMPONENT}_{PARAMETER}_{UNIT}`

### Examples
- `ATA21_PACK_01_INLET_TEMP_C` - Pack 1 inlet temperature in Celsius
- `ATA28_TANK_01_LEVEL_PCT` - H₂ tank 1 level in percent
- `ATA38_POTABLE_TANK_LEVEL_L` - Potable water tank level in liters
- `MTL_COMPONENT_12345_AGE_HOURS` - Component age in flight hours

## Data Quality Requirements

### Validation Rules
- **Range Check**: All signals must be within defined min/max
- **Rate Check**: Data rate must match expected sample rate ±10%
- **Missing Data**: < 5% missing data per flight
- **Outliers**: Automated outlier detection and flagging

### Quality Metrics
- **Completeness**: % of expected signals received
- **Accuracy**: % of signals within tolerance
- **Timeliness**: Average latency from sensor to storage

## Integration Points

### MBSE Model
- Signals linked to SysML model elements
- See [MBSE_BINDINGS.md](../MBSE_BINDINGS.md)

### Digital Twin
- Real-time telemetry feeds digital twin model
- See [TWIN_ANCHORS.md](../TWIN_ANCHORS.md)

### Fleet Learning
- Anonymous telemetry for federated learning
- See [01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/](../../../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/)

### PLM System
- EBOM references link signals to physical components
- See [00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/](../../../../00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/)

## Validation and Testing

### Pre-Deployment
- YAML syntax validation (yamllint)
- Schema completeness checks
- Unit consistency validation

### Runtime
- Automated data validation at ingestion
- Anomaly detection algorithms
- Quality metrics reporting to [05-VERIFICATION/RESULTS/](../../05-VERIFICATION/RESULTS/)

### Post-Flight
- Data quality reports
- Signal coverage analysis
- Digital twin model correlation

## Privacy and Security

### Data Anonymization
- No tail number or registration in telemetry
- No route or passenger information
- Timestamps in UTC only (no timezone/location inference)

### Access Control
- Role-based access to telemetry data
- ITAR/EAR compliance for controlled data
- Audit trail for all data access

## Change Management

### Schema Updates
- **Change Request**: ECR process for schema changes
- **Impact Analysis**: Assess downstream systems (digital twin, fleet learning)
- **Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Backward Compatibility**: Maintain compatibility for MINOR/PATCH changes

### Change Log
See [../../07-CHANGE_LOG/DOMAIN_CHANGE_LOG.csv](../../07-CHANGE_LOG/DOMAIN_CHANGE_LOG.csv)

## Related Documents

- [TELEMETRY_SCHEMA.yaml](TELEMETRY_SCHEMA.yaml) - Telemetry signal definitions
- [EVENTS_SCHEMA.yaml](EVENTS_SCHEMA.yaml) - Event definitions
- [MBSE_BINDINGS.md](../MBSE_BINDINGS.md) - MBSE model integration
- [TWIN_ANCHORS.md](../TWIN_ANCHORS.md) - Digital twin integration
- [01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/](../../../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/) - Fleet learning data contracts
