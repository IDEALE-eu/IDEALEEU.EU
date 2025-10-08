# DATA_STORAGE

Storage architecture for raw data, curated datasets, and metadata management.

## Purpose

Defines storage layers, data organization, metadata management, and retention policies for operational telemetry.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**RAW_DATA_VAULT/**](RAW_DATA_VAULT/) - Immutable raw telemetry storage
- [**CURATED_DATASETS/**](CURATED_DATASETS/) - Processed and quality-assured datasets
- [**METADATA_REGISTRY/**](METADATA_REGISTRY/) - Data catalog, lineage, quality rules
  - **00-README.md** - Metadata registry overview
  - **DATA_DICTIONARY.csv** - Complete signal catalog
  - **LINEAGE_GRAPH/** - Data lineage and provenance
  - **DQ_RULESETS.yaml** - Data quality rules
  - **OPENLINEAGE_EXPORT.md** - OpenLineage integration
- [**RETENTION_POLICY.md**](RETENTION_POLICY.md) - Data retention rules
- [**PARTITIONING_STRATEGY.md**](PARTITIONING_STRATEGY.md) - Data partitioning scheme
- [**UNITS_NORMALIZATION.md**](UNITS_NORMALIZATION.md) - SI units and exceptions

## Storage Architecture

```
┌──────────────────────────────────────────────────────┐
│                 INGESTION LAYER                      │
└────────────────────┬─────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
┌─────────────────┐    ┌─────────────────┐
│  RAW DATA VAULT │    │  METADATA       │
│  (Immutable)    │◄───│  REGISTRY       │
│                 │    │  (Catalog)      │
│ - Parquet/Avro  │    │                 │
│ - Partitioned   │    │ - Lineage       │
│ - Compressed    │    │ - Quality       │
└────────┬────────┘    └─────────────────┘
         │
         │ ETL/Processing
         │
         ▼
┌─────────────────┐
│ CURATED         │
│ DATASETS        │
│                 │
│ - Aggregated    │
│ - Validated     │
│ - Feature Eng   │
└────────┬────────┘
         │
         │ Data Products
         │
         ▼
┌─────────────────┐
│ CONSUMPTION     │
│ LAYER           │
└─────────────────┘
```

## Raw Data Vault

**Purpose**: Immutable storage of ingested telemetry.

**Characteristics**:
- **Append-Only**: No updates or deletes (except legal requirements)
- **Compressed**: LZ4 or Snappy compression
- **Partitioned**: By date, platform, system (see PARTITIONING_STRATEGY.md)
- **Format**: Parquet or Avro (columnar, schema-embedded)

**Example Path**:
```
s3://ideale-raw-vault/
├─ dt=2024-01-15/
│  ├─ platform=AC-H2-001/
│  │  ├─ system=h2/
│  │  │  └─ data.parquet
│  │  ├─ system=engine/
│  │  │  └─ data.parquet
│  ├─ platform=SC-LEO-005/
│  │  ├─ system=power/
│  │  │  └─ data.parquet
```

**Retention**: Permanent (or per RETENTION_POLICY.md)

## Curated Datasets

**Purpose**: Processed datasets ready for analytics and ML.

**Characteristics**:
- **Quality-Assured**: Passed data quality checks
- **Aggregated**: Time-series aggregations (e.g., 1-minute averages)
- **Feature-Engineered**: Derived features for ML models
- **Documented**: Metadata and lineage tracked

**Example Path**:
```
s3://ideale-curated/
├─ usage_profiles/
│  ├─ daily_summaries/
│  │  └─ dt=2024-01-15/
│  │     └─ data.parquet
├─ anomaly_events/
│  ├─ critical/
│  │  └─ dt=2024-01-15/
│  │     └─ data.parquet
```

**Retention**: Per dataset retention policy

## Metadata Registry

See [**METADATA_REGISTRY/00-README.md**](METADATA_REGISTRY/00-README.md) for complete specification.

**Components**:
- **Data Dictionary**: Signal catalog with EBOM references
- **Lineage Graph**: Data flow from source to consumption
- **Quality Rulesets**: Completeness, range, consistency rules
- **OpenLineage Export**: Standardized lineage format

## Partitioning Strategy

See [**PARTITIONING_STRATEGY.md**](PARTITIONING_STRATEGY.md) for complete specification.

**Partitioning Scheme**:
```
dt=YYYY-MM-DD / platform={platform_id} / system={system_code}
```

**Benefits**:
- Efficient time-range queries
- Parallel processing
- Targeted data retention
- Cost optimization

## Units Normalization

See [**UNITS_NORMALIZATION.md**](UNITS_NORMALIZATION.md) for complete specification.

**Standard**: SI units by default
**Exceptions**: Documented per signal (e.g., altitude in feet for aviation)

## Data Quality Management

**Quality Dimensions**:
1. **Completeness**: <5% missing values per signal
2. **Accuracy**: Sensor calibration, cross-validation
3. **Consistency**: Cross-field validation
4. **Timeliness**: Timestamp synchronization (±1 second)
5. **Validity**: Range checks, enumeration validation

**Quality Tracking**:
- Quality scores per dataset
- Quality trend monitoring
- Automated quality reports

## Retention Policy

See [**RETENTION_POLICY.md**](RETENTION_POLICY.md) for complete specification.

**Retention Classes**:
- **Permanent**: Safety events, anomalies, certifiable data
- **Long-Term (5+ years)**: Performance trends, reliability data
- **Medium-Term (1-5 years)**: Operational telemetry
- **Short-Term (<1 year)**: Verbose logs, raw diagnostics

## Data Lifecycle

```
┌─────────────┐  Ingestion   ┌─────────────┐  Curation   ┌─────────────┐
│ Telemetry   │─────────────▶│ Raw Vault   │────────────▶│ Curated     │
│ Sources     │              │ (Day 0)     │             │ Datasets    │
└─────────────┘              └─────────────┘             └─────────────┘
                                    │                            │
                                    │                            │
                             Archive (Year 1)            Archive (Year 5)
                                    │                            │
                                    ▼                            ▼
                             ┌─────────────┐            ┌─────────────┐
                             │ Cold        │            │ Cold        │
                             │ Storage     │            │ Storage     │
                             └─────────────┘            └─────────────┘
```

## Performance Considerations

**Query Performance**:
- Partitioning reduces scan size
- Columnar format optimizes column-specific queries
- Compression reduces I/O

**Storage Costs**:
- Hot storage (first 30 days): SSD/S3 Standard
- Warm storage (30-365 days): S3 Infrequent Access
- Cold storage (1+ years): S3 Glacier

## Security and Access Control

**Encryption**:
- At-rest: AES-256
- In-transit: TLS 1.3

**Access Control**:
- RBAC: Role-based access per dataset
- ABAC: Attribute-based (data classification, clearance level)
- Audit logging: All access logged

See [**04-DATA_SECURITY_COMPLIANCE/**](../04-DATA_SECURITY_COMPLIANCE/) for details.

## Related Documents

- **../../02-DATA_INGESTION/** - Data ingestion pipelines
- **../../04-DATA_SECURITY_COMPLIANCE/** - Security and compliance
- **../../05-DATA_PRODUCTS/** - Data product definitions
- **../../09-TEMPLATES/RETENTION_SCHEDULE_TEMPLATE.csv** - Retention schedule template

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial storage architecture    | Data Engineering Team |
