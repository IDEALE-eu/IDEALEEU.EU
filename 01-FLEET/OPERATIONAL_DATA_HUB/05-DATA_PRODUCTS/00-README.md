# DATA_PRODUCTS

Curated data products derived from operational telemetry for analytics and ML consumption.

## Purpose

Provides value-added datasets ready for downstream consumers:
- **Usage Profiles**: Flight/mission performance summaries
- **Anomaly Reports**: Detected anomalies with context
- **Reliability Datasets**: MTBF, failure rates, degradation trends
- **Benchmarking Packs**: Cross-platform performance comparisons

## Contents

- [**00-README.md**](00-README.md) - This file
- [**USAGE_PROFILES/**](USAGE_PROFILES/) - Aggregated performance summaries
- [**ANOMALY_REPORTS/**](ANOMALY_REPORTS/) - Anomaly detection outputs → ../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/
- [**RELIABILITY_DATASETS/**](RELIABILITY_DATASETS/) - Reliability metrics and trends
- [**BENCHMARKING_PACKS/**](BENCHMARKING_PACKS/) - Fleet-wide performance comparisons

## Data Product Principles

### 1. Well-Documented
- Clear description and purpose
- Metadata (lineage, quality, freshness)
- Schema and data contract
- Usage examples

### 2. Quality-Assured
- Passed data quality checks
- Known limitations documented
- Quality metrics published

### 3. Versioned
- Semantic versioning (major.minor.patch)
- Backward compatibility policy
- Deprecation notices

### 4. Accessible
- Discoverable in data catalog
- Standard formats (Parquet, CSV, JSON)
- API or file-based access

## Data Product Catalog

### Usage Profiles

**Description**: Aggregated flight/mission performance summaries

**Use Cases**:
- Fleet performance monitoring
- Fuel efficiency analysis
- Mission success metrics

**Schema**:
```yaml
fields:
  - date: date
  - platform_id: string
  - flight_hours: float
  - fuel_consumed_kg: float
  - avg_altitude_m: float
  - max_airspeed_ms: float
  - h2_consumption_kg: float
  - efficiency_score: float (0-100)
```

**Refresh**: Daily

**Retention**: 5 years

---

### Anomaly Reports

**Description**: Detected anomalies with context and severity

**Use Cases**:
- Predictive maintenance (→ ../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/)
- Fault diagnosis
- ML model training

**Schema**:
```yaml
fields:
  - timestamp: timestamp
  - platform_id: string
  - signal_name: string
  - anomaly_type: string (out_of_range, drift, spike, stuck_sensor)
  - severity: string (LOW, MEDIUM, HIGH, CRITICAL)
  - confidence: float (0-1)
  - value: float
  - expected_range: array[float]
  - context: struct (recent_trend, related_signals)
```

**Refresh**: Real-time

**Retention**: Permanent

---

### Reliability Datasets

**Description**: Reliability metrics and degradation trends

**Use Cases**:
- RUL (Remaining Useful Life) estimation
- Warranty analysis
- Design feedback

**Schema**:
```yaml
fields:
  - component_id: string
  - mtbf_hours: float (Mean Time Between Failures)
  - failure_rate: float (failures per 1000 hours)
  - degradation_trend: string (stable, gradual, rapid)
  - last_maintenance: date
  - predicted_failure_date: date
```

**Refresh**: Weekly

**Retention**: 10 years

---

### Benchmarking Packs

**Description**: Cross-platform performance comparisons

**Use Cases**:
- Fleet optimization
- Variant comparison
- Best practice identification

**Schema**:
```yaml
fields:
  - platform_group: string (aircraft_type, spacecraft_mission)
  - metric_name: string
  - p50_value: float (median)
  - p95_value: float (95th percentile)
  - best_performer: string (platform_id)
  - worst_performer: string (platform_id)
```

**Refresh**: Monthly

**Retention**: 5 years

## Data Product Lifecycle

```
┌─────────────┐  Define   ┌─────────────┐  Build   ┌─────────────┐
│ Use Case    │──────────▶│ Data        │─────────▶│ ETL         │
│ Identified  │           │ Contract    │          │ Pipeline    │
└─────────────┘           └─────────────┘          └─────────────┘
                                                            │
                                                            ▼
┌─────────────┐  Publish  ┌─────────────┐  Validate ┌─────────────┐
│ Consumers   │◀──────────│ Data        │◀──────────│ Quality     │
│             │           │ Product     │           │ Check       │
└─────────────┘           └─────────────┘           └─────────────┘
```

### 1. Define Data Product
- Identify consumer use case
- Define data contract (schema, SLA, quality)
- Document purpose and limitations

### 2. Build ETL Pipeline
- Extract from raw vault
- Transform (aggregate, join, feature engineer)
- Load to curated datasets

### 3. Validate Quality
- Run quality checks
- Compute quality metrics
- Document known issues

### 4. Publish Data Product
- Register in data catalog
- Publish schema and contract
- Notify consumers

## Data Contracts

Each data product has a data contract:

```yaml
# Example: usage_profiles_contract.yaml
product: usage_profiles
version: 1.2.0
owner: Data Engineering Team
consumers:
  - Fleet Operations
  - ML Team
  - Design Engineering

sla:
  refresh_frequency: daily
  latency: < 24 hours
  availability: 99.5%

quality_guarantees:
  completeness: > 99%
  accuracy: sensor_calibration_certified
  timeliness: within_24h

schema:
  format: parquet
  location: s3://ideale-curated/usage_profiles/
  fields: [...]  # See schema above

backward_compatibility: FULL
deprecation_notice: 90 days minimum
```

## Integration with Downstream Systems

### Predictive Maintenance
- Anomaly reports forwarded to `../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/`
- RUL models trained on reliability datasets

### Federated Learning
- Training datasets exported to `../FEDERATED_LEARNING/`
- Privacy-preserving aggregation

### Digital Twin
- Real-world data used for model calibration
- Anomalies used for parameter tuning

### Design Engineering
- Performance benchmarks inform next-gen design
- Failure modes feed into FMEA

## Monitoring

**Key Metrics**:
- Data product freshness (time since last update)
- Quality scores (completeness, accuracy)
- Consumer adoption (active users)
- Query performance (p95 latency)

**Alerts**:
- Data product stale (>24 hours overdue)
- Quality score below SLA
- No consumers for >90 days (candidate for deprecation)

## Related Documents

- **../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/** - Per-product data contracts
- **../03-DATA_STORAGE/CURATED_DATASETS/** - Storage layer
- **../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/** - Maintenance integration
- **../../FEDERATED_LEARNING/** - ML integration

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial data products catalog   | Data Engineering Team |
