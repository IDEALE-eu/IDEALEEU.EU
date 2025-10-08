# DATA_INGESTION

Data ingestion pipelines, validation rules, and schema management for operational telemetry.

## Purpose

This directory defines how operational data flows from aircraft and spacecraft into the Operational Data Hub, including:

- Real-time streaming pipelines for live telemetry
- Batch upload processes for historical data
- Schema registration and versioning
- Data validation and quality checks
- Anomaly detection at ingestion

## Contents

- [**00-README.md**](00-README.md) - This file
- [**INGESTION_PIPELINES/**](INGESTION_PIPELINES/) - Real-time and batch ingestion
  - **REAL_TIME_STREAM/** - Kafka/MQTT streaming configuration
  - **BATCH_UPLOAD/** - S3/SFTP batch upload processes
- [**DATA_VALIDATION_RULES.md**](DATA_VALIDATION_RULES.md) - Validation rules at ingestion
- [**ANOMALY_DETECTION_AT_INGEST.md**](ANOMALY_DETECTION_AT_INGEST.md) - Anomaly detection before storage
- [**SCHEMA_REGISTRY/**](SCHEMA_REGISTRY/) - Schema versioning and compatibility
  - **00-README.md** - Schema registry overview
  - **TELEMETRY_SCHEMA_VERSIONING.md** - SemVer lifecycle and states
  - **COMPATIBILITY_POLICY.md** - BACKWARD | FORWARD | FULL

## Ingestion Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────┐
│ Telemetry       │────▶│ Schema           │────▶│ Validation &   │
│ Sources         │     │ Validation       │     │ Quality Checks │
└─────────────────┘     └──────────────────┘     └────────────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌────────────────┐
│ Metadata        │◀────│ Anomaly          │◀────│ Routing        │
│ Registry        │     │ Detection        │     │ & Partitioning │
└─────────────────┘     └──────────────────┘     └────────────────┘
                                                           │
                                                           ▼
                                                   ┌────────────────┐
                                                   │ Raw Data Vault │
                                                   └────────────────┘
```

## Ingestion Pipelines

### Real-Time Stream Processing

**Use Cases:**
- In-flight telemetry from aircraft
- Live spacecraft telemetry via ground stations
- Real-time health monitoring and alerts

**Technology Stack:**
- **Message Bus**: Apache Kafka, MQTT (for constrained networks)
- **Stream Processing**: Apache Flink, Kafka Streams
- **Serialization**: Avro, Protobuf (with schema registry)

**Pipeline Stages:**
1. **Deserialize** - Parse message using registered schema
2. **Validate** - Check ranges, completeness, freshness
3. **Enrich** - Add metadata (platform ID, timestamp, version)
4. **Detect Anomalies** - Apply statistical and ML-based detectors
5. **Route** - Partition by date, platform, system
6. **Store** - Write to raw vault and forward to consumers

**Performance Requirements:**
- **Latency**: <5 seconds end-to-end (p99)
- **Throughput**: 100k messages/second per topic
- **Reliability**: At-least-once delivery guarantee

### Batch Upload Processing

**Use Cases:**
- Historical FDR/QAR data from maintenance downloads
- Post-mission spacecraft data dumps
- Bulk data migrations

**Technology Stack:**
- **Transfer**: S3, SFTP, REST API
- **Processing**: Apache Spark, Pandas (Python)
- **Validation**: Great Expectations, custom rules

**Pipeline Stages:**
1. **Upload** - Secure file transfer to staging area
2. **Validate** - Schema check, file integrity (checksum)
3. **Parse** - Convert to standardized format (Parquet, Avro)
4. **Quality Check** - Completeness, range, consistency
5. **Partition** - Organize by date, platform, system
6. **Catalog** - Register in Metadata Registry
7. **Archive** - Move to raw vault, delete staging files

**Performance Requirements:**
- **Processing Time**: <1 hour for 10 GB batch
- **Data Quality**: >99% pass rate on validation rules
- **Retry Logic**: 3 retries with exponential backoff

## Data Validation Rules

See [**DATA_VALIDATION_RULES.md**](DATA_VALIDATION_RULES.md) for complete specification.

**Categories:**
- **Structural**: Schema compliance, required fields, data types
- **Range**: Min/max values, allowed enumerations
- **Consistency**: Cross-field validation (e.g., altitude vs. pressure)
- **Completeness**: Missing data thresholds (<5% per signal)
- **Freshness**: Timestamp within expected window

**Failure Handling:**
- **Critical Failures**: Reject message, alert operators
- **Warning Failures**: Accept with quality flag, log for review
- **Informational**: Accept, log for analysis

## Anomaly Detection at Ingest

See [**ANOMALY_DETECTION_AT_INGEST.md**](ANOMALY_DETECTION_AT_INGEST.md) for complete specification.

**Methods:**
- **Statistical**: 3-sigma, IQR, moving average
- **ML-Based**: Isolation Forest, Autoencoder
- **Domain-Specific**: Physics-based checks (e.g., energy balance)

**Actions:**
- **Anomaly Detected**: Flag message, forward to anomaly queue
- **Severe Anomaly**: Trigger alert to flight operations/mission control
- **No Anomaly**: Continue normal processing

## Schema Registry

See [**SCHEMA_REGISTRY/00-README.md**](SCHEMA_REGISTRY/00-README.md) for complete specification.

**Key Features:**
- **Versioning**: Semantic versioning (major.minor.patch)
- **Compatibility**: BACKWARD (default), FORWARD, FULL, NONE
- **Lifecycle States**: DRAFT → ACTIVE → DEPRECATED → ARCHIVED
- **Change Control**: ECR required for breaking changes

**Schema Evolution Example:**
```
v1.0.0 (ACTIVE)       - Initial schema
v1.1.0 (ACTIVE)       - Add optional field (backward compatible)
v2.0.0 (ACTIVE)       - Remove field (breaking change, requires ECR)
v1.1.0 (DEPRECATED)   - Mark old version as deprecated (90-day notice)
v1.1.0 (ARCHIVED)     - Archive after deprecation period
```

## Integration Points

### Upstream
- **01-DATA_SOURCES/** - Telemetry source definitions
- **00-PROGRAM/CONFIG_MGMT/04-BASELINES/** - System configuration baselines

### Downstream
- **03-DATA_STORAGE/RAW_DATA_VAULT/** - Ingested data storage
- **03-DATA_STORAGE/METADATA_REGISTRY/** - Data catalog and lineage
- **08-METRICS_AND_MONITORING/PIPELINE_HEALTH.csv** - Pipeline monitoring

## Monitoring and Alerting

**Key Metrics:**
- Message throughput (messages/second)
- Validation failure rate (%)
- Anomaly detection rate (%)
- End-to-end latency (p50, p95, p99)
- Schema registry hit rate (%)

**Alerts:**
- Pipeline down >5 minutes
- Validation failure rate >5%
- Anomaly rate >10% (may indicate sensor fault)
- Schema mismatch >1% (indicates schema drift)

## Related Documents

- **../../00-PROGRAM/DIGITAL_THREAD/07-INTEGRATIONS/FLEET_DATA_INGEST/** - API specifications
- **../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/** - ML data contracts
- **../../09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json** - Schema template

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial ingestion documentation | Data Engineering Team |
