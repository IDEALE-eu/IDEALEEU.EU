# DATA_SOURCES

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > DATA_SOURCES**

Definitions and specifications for operational data sources from aircraft and spacecraft fleets.

## Purpose

This directory documents all telemetry sources feeding into the Operational Data Hub, including signal definitions, sampling rates, data formats, and connectivity requirements.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**AIRCRAFT_TELEMETRY/**](AIRCRAFT_TELEMETRY/) - Aircraft-specific data sources
  - **FLIGHT_DATA_RECORDER/** - FDR/QAR data streams
  - **H2_SYSTEMS_MONITORING/** - Hydrogen propulsion system telemetry
  - **AVIONICS_HEALTH/** - Avionics system status and diagnostics
  - **CABIN_ENVIRONMENT/** - Cabin pressure, temperature, air quality
- [**SPACECRAFT_TELEMETRY/**](SPACECRAFT_TELEMETRY/) - Spacecraft-specific data sources
  - **ORBITAL_STATE/** - Position, velocity, attitude telemetry
  - **POWER_THERMAL/** - Power generation, battery, thermal control
  - **PROPULSION_HEALTH/** - Thruster performance and consumables
  - **PAYLOAD_OPERATIONS/** - Payload instrument data
  - **RADIATION_ENVIRONMENT/** - Radiation dose monitoring

## Source Registration Process

### 1. Identify Data Source
- System name and identifier (EBOM reference)
- Data type (telemetry, events, logs)
- Owner/responsible team

### 2. Define Schema
- Signal names (aligned with EBOM)
- Data types (float32, int16, bool, string)
- Units (SI by default, exceptions documented)
- Sample rates and expected throughput
- Value ranges and validity checks

### 3. Document Connectivity
- Physical interface (ARINC, CAN, Ethernet, satellite link)
- Protocol (MQTT, Kafka, SFTP, REST API)
- Latency requirements
- Reliability/redundancy

### 4. Register in Schema Registry
- Submit schema to [../../02-DATA_INGESTION/SCHEMA_REGISTRY/](../02-DATA_INGESTION/SCHEMA_REGISTRY/00-README.md)
- Assign semantic version (v1.0.0)
- Define compatibility policy (BACKWARD, FORWARD, FULL)

### 5. Implement Ingestion Pipeline
- Configure pipeline in [../../02-DATA_INGESTION/INGESTION_PIPELINES/](../02-DATA_INGESTION/INGESTION_PIPELINES/)
- Apply data validation rules
- Enable anomaly detection

## Data Source Categorization

### By Update Frequency
- **High-Rate (>1 Hz)**: Flight control surfaces, engine parameters, attitude sensors
- **Medium-Rate (0.1-1 Hz)**: Environmental sensors, health monitoring
- **Low-Rate (<0.1 Hz)**: Housekeeping, maintenance events, mission milestones

### By Criticality
- **Safety-Critical**: Flight control feedback, propulsion health
- **Mission-Critical**: Navigation, power systems, thermal control
- **Operational**: Performance monitoring, efficiency metrics
- **Diagnostic**: Detailed logs, debug traces

### By Data Retention
- **Permanent**: Safety events, anomalies, certifiable data
- **Long-Term (5+ years)**: Performance trends, reliability data
- **Medium-Term (1-5 years)**: Operational telemetry, training data
- **Short-Term (<1 year)**: Verbose logs, raw diagnostics

## Quality Requirements

### Completeness
- **Target**: >95% data availability per source
- **Missing Data Handling**: Flag as missing, no synthetic imputation at source
- **Gap Detection**: Automated alerts for >10-second gaps in critical signals

### Accuracy
- **Sensor Calibration**: Annual calibration required for all sensors
- **Cross-Validation**: Redundant sensors cross-checked for consistency
- **Outlier Detection**: 3-sigma or IQR method applied at ingestion

### Timeliness
- **Timestamp Synchronization**: GPS/UTC time required (±1 second tolerance)
- **Latency**: <5 seconds for real-time streams, <24 hours for batch
- **Staleness Alerts**: Data older than expected refresh period flagged

## Integration with EBOM

All signal names must reference Engineering Bill of Materials (EBOM) identifiers:

```yaml
signal:
  name: h2_tank_pressure_fwd
  ebom_ref: ATA-28-42-001  # Fuel system, hydrogen tank, forward
  description: Forward hydrogen tank pressure sensor
  unit: bar
  range: [0, 350]
  sample_rate: 1 Hz
```

## Related Documents

- [**../../02-DATA_INGESTION/SCHEMA_REGISTRY/**](../02-DATA_INGESTION/SCHEMA_REGISTRY/00-README.md) - Schema registration and versioning
- [**../../03-DATA_STORAGE/METADATA_REGISTRY/DATA_DICTIONARY.csv**](../03-DATA_STORAGE/METADATA_REGISTRY/DATA_DICTIONARY.csv) - Complete signal catalog
- [**../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/**](../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/) - System configuration baselines
- [**../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/**](../../FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/) - ML data contracts

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial data source documentation | Data Engineering Team |
