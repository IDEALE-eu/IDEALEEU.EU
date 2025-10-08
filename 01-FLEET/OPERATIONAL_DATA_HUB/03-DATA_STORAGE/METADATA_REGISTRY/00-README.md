# METADATA_REGISTRY

Central catalog for data dictionary, lineage tracking, and quality rules.

## Purpose

Provides comprehensive metadata management for all operational data:
- **Data Dictionary**: Complete catalog of signals with EBOM references
- **Lineage Graph**: Track data flow from source to consumption
- **Quality Rulesets**: Automated data quality validation
- **OpenLineage Export**: Standardized lineage format for external tools

## Contents

- [**00-README.md**](00-README.md) - This file
- [**DATA_DICTIONARY.csv**](DATA_DICTIONARY.csv) - Complete signal catalog
- [**LINEAGE_GRAPH/**](LINEAGE_GRAPH/) - Data lineage tracking
- [**DQ_RULESETS.yaml**](DQ_RULESETS.yaml) - Data quality rules (completeness, range, consistency)
- [**OPENLINEAGE_EXPORT.md**](OPENLINEAGE_EXPORT.md) - OpenLineage integration spec

## Data Dictionary

See [**DATA_DICTIONARY.csv**](DATA_DICTIONARY.csv)

**Schema**:
```csv
signal_id, signal_name, description, unit, data_type, sample_rate, ebom_ref, system, platform_type, owner, status
```

**Example Entry**:
```csv
h2_pressure_fwd, Forward H2 Tank Pressure, Hydrogen tank pressure sensor forward, bar, double, 1 Hz, ATA-28-42-001, h2, aircraft, H2 Propulsion Team, ACTIVE
```

**Usage**:
- Browse available signals
- Find EBOM references
- Identify signal owners
- Check signal status (ACTIVE, DEPRECATED, ARCHIVED)

## Lineage Graph

See [**LINEAGE_GRAPH/**](LINEAGE_GRAPH/)

**Tracks**:
- Data sources (sensors, systems)
- Ingestion pipelines
- Transformations (ETL, feature engineering)
- Curated datasets
- Data products
- Consumers (ML models, dashboards, reports)

**Format**: OpenLineage-compatible JSON

**Example**:
```json
{
  "source": "sensor://AC-H2-001/h2_tank_pressure_fwd",
  "pipeline": "ingestion://real_time_stream/h2_telemetry",
  "transformation": "validation://range_check",
  "destination": "dataset://raw_vault/h2_telemetry",
  "downstream": [
    "dataset://curated/h2_performance",
    "model://predictive_maintenance/h2_fault_detection"
  ]
}
```

## Data Quality Rulesets

See [**DQ_RULESETS.yaml**](DQ_RULESETS.yaml)

**Quality Dimensions**:
1. **Completeness**: Missing data thresholds
2. **Accuracy**: Range checks, cross-validation
3. **Consistency**: Cross-field validation
4. **Timeliness**: Timestamp synchronization
5. **Validity**: Enumeration checks, format validation

**Example Ruleset**:
```yaml
signal: h2_tank_pressure_fwd
rules:
  completeness:
    max_missing_rate: 0.05  # 5%
    window: 1_hour
  accuracy:
    range: [0, 350]  # bar
    cross_validation:
      signal: h2_tank_temp_fwd
      correlation: positive
  timeliness:
    max_latency: 5  # seconds
    timestamp_sync: GPS
```

## OpenLineage Export

See [**OPENLINEAGE_EXPORT.md**](OPENLINEAGE_EXPORT.md)

**Purpose**: Export lineage metadata in OpenLineage standard format for integration with:
- Apache Airflow
- Marquez (lineage UI)
- Amundsen (data discovery)
- DataHub (metadata platform)

**Export Frequency**: Real-time (on pipeline execution) or batch (daily)

## Integration with Schema Registry

**Synchronization**:
- Schema Registry → Metadata Registry (on schema registration)
- Signal definitions automatically added to DATA_DICTIONARY.csv
- Schema versions tracked in lineage graph

## Metadata API

**Query Examples**:
```bash
# Find signals by system
GET /api/metadata/signals?system=h2

# Get signal lineage
GET /api/metadata/lineage?signal=h2_tank_pressure_fwd

# Search by EBOM reference
GET /api/metadata/signals?ebom=ATA-28-42-001

# Get quality metrics
GET /api/metadata/quality?signal=h2_tank_pressure_fwd&date=2024-01-15
```

## Metadata Governance

### Update Process
1. Schema changes trigger automatic metadata update
2. Manual updates require PR + data steward approval
3. Quality rules versioned in Git

### Roles
- **Data Steward**: Metadata curator, quality enforcer
- **System Owner**: Responsible for system-specific metadata
- **Data Consumer**: Read-only access, can request metadata updates

## Monitoring

**Key Metrics**:
- Metadata coverage (signals with complete metadata)
- Lineage completeness (all data flows documented)
- Quality rule coverage (signals with quality rules)
- Metadata staleness (last update timestamp)

**Alerts**:
- New signal without metadata
- Quality rule failure rate >5%
- Lineage gap detected (missing transformation)

## Related Documents

- **../../02-DATA_INGESTION/SCHEMA_REGISTRY/** - Schema definitions
- **../../02-DATA_INGESTION/DATA_VALIDATION_RULES.md** - Validation rules
- **../PARTITIONING_STRATEGY.md** - Data organization
- **../../00-PROGRAM/DIGITAL_THREAD/** - Digital Thread integration

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial metadata registry       | Data Engineering Team |
