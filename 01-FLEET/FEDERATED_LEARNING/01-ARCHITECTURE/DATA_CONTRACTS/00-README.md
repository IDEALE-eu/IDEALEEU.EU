# DATA_CONTRACTS

Data schemas and contracts for federated learning telemetry and labels.

## Purpose

This directory defines standardized data contracts for telemetry signals, event labels, and model inputs/outputs. Data contracts ensure consistency across aircraft, ground stations, and simulation rigs, enabling reliable model training and inference.

## Contents

- [**00-README.md**](00-README.md) - This file
- **TELEMETRY_SCHEMA.yaml** - Signal names, units, sample rates, ranges
- **LABELS_EVENTS_SCHEMA.yaml** - Fault codes, maintenance tags, event definitions

## Data Contract Principles

### Design Goals
1. **Alignment with EBOM** - Signal names match Engineering Bill of Materials identifiers
2. **Traceability** - Links to requirements, NCRs, and system specifications
3. **Versioning** - Semantic versioning for schema changes (v1.2.0)
4. **Backward compatibility** - Graceful handling of schema evolution
5. **Privacy by design** - No PII, pseudonymisation enforced

### Schema Governance
- **Owner**: AI/ML Team (Data Engineering)
- **Approver**: Configuration Control Board (CCB)
- **Review Cycle**: Quarterly or upon significant system changes
- **Change Process**: ECR (Engineering Change Request) required for breaking changes

## Schema Structure

### Telemetry Schema (TELEMETRY_SCHEMA.yaml)

Defines continuous sensor signals and system parameters:

```yaml
signals:
  - name: airspeed_indicated
    unit: knots
    sample_rate: 10 Hz
    range: [0, 350]
    ebom_ref: ATA-34-12-001
    description: Indicated airspeed from pitot-static system
```

### Labels Schema (LABELS_EVENTS_SCHEMA.yaml)

Defines discrete events, fault codes, and maintenance tags:

```yaml
events:
  - name: engine_oil_pressure_low
    code: ENG-001
    severity: warning
    ncr_link: NCR-2024-123
    description: Engine oil pressure below threshold
```

## Data Quality Requirements

### Completeness
- **Missing data**: Max 5% missing values per signal per flight
- **Interpolation**: Linear interpolation for gaps < 10 seconds
- **Imputation**: No imputation for gaps > 10 seconds (mark as missing)

### Accuracy
- **Sensor calibration**: Annual calibration records required
- **Outlier detection**: 3-sigma rule or IQR method
- **Validation**: Cross-check with redundant sensors (if available)

### Timeliness
- **Latency**: Telemetry timestamps within ±1 second of UTC
- **Synchronization**: GPS time sync required for all clients
- **Staleness**: Data older than 30 days flagged for retention review

## Privacy and Security

### Pseudonymisation
- **Aircraft ID**: `sha256(tail_number + salt)` - no clear-text tail numbers
- **Flight ID**: `sha256(flight_number + date + salt)`
- **Crew ID**: Not collected (no PII)

### Data Minimization
- Only signals relevant to FL use cases are collected
- Retention policy: 90 days for raw telemetry, 2 years for aggregated metrics

### Consent and Rights
- GDPR Art. 6(1)(f) - Legitimate interest (safety, maintenance optimization)
- Right to erasure: Clients can opt-out; gradients deleted within 30 days

## Integration Points

### Upstream Sources
- [**02-AIRCRAFT/DOMAIN_INTEGRATION/INFO_COMM_AVIONICS/**](02-AIRCRAFT/DOMAIN_INTEGRATION/INFO_COMM_AVIONICS/) -  Avionics data buses
- [**01-FLEET/OPERATIONAL_DATA_HUB/**](01-FLEET/OPERATIONAL_DATA_HUB/) -  Fleet telemetry aggregation
- [**00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/**](00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/) -  EBOM references

### Downstream Consumers
- [**03-CLIENTS/**](03-CLIENTS/) -  Client-side data ingestion and preprocessing
- [**04-ALGORITHMS/**](04-ALGORITHMS/) -  Feature engineering and model training
- [**06-MODELS/DATASETS_INDEX.md**](06-MODELS/DATASETS_INDEX.md) - Dataset provenance tracking

## Validation and Testing

### Schema Validation
- **Syntax**: YAML linting (yamllint)
- **Semantics**: Unit consistency, range checks
- **Compatibility**: Backward compatibility tests

### Data Validation
- **Pre-flight**: Schema compliance checks before aircraft deployment
- **Runtime**: Validation at data ingestion (client-side)
- **Post-flight**: Quality metrics reported to 12-METRICS/

## Related Documents

- [**FL_TOPOLOGY.md**](FL_TOPOLOGY.md) - Communication patterns for data transmission
- [**CLIENT_TYPES.md**](CLIENT_TYPES.md) - Client-specific data access permissions
- [**06-MODELS/DATASETS_INDEX.md**](06-MODELS/DATASETS_INDEX.md) - Dataset provenance and lineage
- [**11-COMPLIANCE/PRIVACY.md**](11-COMPLIANCE/PRIVACY.md) - GDPR compliance for telemetry data

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|-----------------|
| 1.0     | 2024-Q4 | Initial schema definitions       | AI/ML Data Team |
