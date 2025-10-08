# METRICS_AND_MONITORING

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > METRICS_AND_MONITORING**

Monitoring dashboards, metrics, and operational health tracking for the Operational Data Hub.

## Purpose

Provides visibility into:
- **Data Quality**: Completeness, accuracy, timeliness
- **Pipeline Health**: Ingestion, processing, delivery performance
- **Consumer Usage**: Active consumers, query patterns, SLA compliance

## Contents

- [**00-README.md**](00-README.md) - This file
- [**DATA_QUALITY_DASHBOARD.md**](DATA_QUALITY_DASHBOARD.md) - Data quality metrics and visualizations
- [**PIPELINE_HEALTH.csv**](PIPELINE_HEALTH.csv) - Pipeline performance tracking
- [**CONSUMER_USAGE_LOG.csv**](CONSUMER_USAGE_LOG.csv) - Consumer activity logs

## Key Metrics

### Data Quality Metrics

**Completeness**:
- % of expected signals received
- Missing data rate per signal
- Gap detection (time periods with no data)

**Accuracy**:
- Validation pass rate
- Out-of-range values detected
- Sensor drift detected

**Timeliness**:
- End-to-end latency (source → availability)
- Data freshness (time since last update)
- SLA compliance rate

**Consistency**:
- Cross-field validation failures
- Duplicate detection rate
- Schema compliance rate

### Pipeline Health Metrics

**Ingestion**:
- Messages ingested per second
- Ingestion error rate
- Schema validation failure rate

**Processing**:
- Processing latency (p50, p95, p99)
- Backlog size (messages waiting)
- Worker utilization

**Storage**:
- Storage capacity used
- Write throughput (MB/s)
- Partition count

### Consumer Usage Metrics

**Adoption**:
- Active consumers (daily, weekly, monthly)
- New consumers onboarded
- Data products accessed

**Performance**:
- Query latency (p50, p95, p99)
- Query success rate
- API error rate

**SLA Compliance**:
- SLA compliance rate per data product
- SLA violations count
- Downtime incidents

## Dashboards

### 1. Data Quality Dashboard

See [**DATA_QUALITY_DASHBOARD.md**](DATA_QUALITY_DASHBOARD.md)

**Visualizations**:
- Time-series: Data completeness over time
- Heatmap: Quality scores by signal and platform
- Bar chart: Top 10 signals with quality issues
- Gauge: Overall data quality score (0-100)

**Refresh**: Real-time (1-minute intervals)

---

### 2. Pipeline Health Dashboard

**Visualizations**:
- Time-series: Ingestion rate (messages/sec)
- Line chart: Processing latency (p50, p95, p99)
- Bar chart: Error rate by pipeline stage
- Table: Pipeline status (green/yellow/red)

**Refresh**: Real-time (30-second intervals)

---

### 3. Consumer Usage Dashboard

**Visualizations**:
- Bar chart: Active consumers by data product
- Pie chart: Query distribution by consumer
- Time-series: Query latency trends
- Table: SLA compliance by data product

**Refresh**: Hourly

## Alerting Rules

### Critical Alerts (Immediate Notification)

| Alert | Condition | Action |
|-------|-----------|--------|
| Pipeline Down | No data ingested for >5 minutes | Page on-call engineer |
| Data Quality Failure | Quality score <80% for >10 minutes | Notify data steward |
| SLA Violation | Latency >2x SLA target | Notify data owner |
| Storage Capacity | >90% capacity used | Notify infrastructure team |

### Warning Alerts (Notification within 15 minutes)

| Alert | Condition | Action |
|-------|-----------|--------|
| High Error Rate | Error rate >1% for >15 minutes | Notify data engineer |
| Schema Mismatch | Schema validation failure >1% | Notify schema owner |
| Consumer Error | Consumer error rate >5% | Notify consumer owner |

### Informational Alerts (Daily Summary)

| Alert | Condition | Action |
|-------|-----------|--------|
| Low Usage | No queries for >7 days | Consider deprecation |
| High Backlog | Backlog >10k messages | Review processing capacity |
| Anomaly Rate | Anomaly rate >10% | Review anomaly detectors |

## Monitoring Stack

**Components**:
- **Metrics Collection**: Prometheus
- **Visualization**: Grafana
- **Alerting**: Alertmanager
- **Log Aggregation**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger (distributed tracing)

**Architecture**:
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Data Pipelines  │────▶│ Prometheus      │────▶│ Grafana         │
│ (Metrics Export)│     │ (Metrics Store) │     │ (Dashboards)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                │
                                ▼
                        ┌─────────────────┐
                        │ Alertmanager    │
                        │ (Alert Routing) │
                        └─────────────────┘
```

## Service Level Indicators (SLIs)

### Data Freshness SLI
```
SLI = (data_available_within_SLA / total_data_points) * 100%
Target: >99.5%
```

### Query Latency SLI
```
SLI = (queries_completed_within_SLA / total_queries) * 100%
Target: >99% of queries <5 seconds (p99)
```

### Availability SLI
```
SLI = (uptime_seconds / total_seconds) * 100%
Target: >99.9% uptime
```

## Operational Runbooks

### Runbook: Pipeline Down

**Symptoms**: No data ingested for >5 minutes

**Diagnosis**:
1. Check pipeline status dashboard
2. Review recent error logs
3. Check upstream data sources (are they sending data?)
4. Verify Kafka/MQTT broker health

**Resolution**:
1. Restart failed pipeline component
2. If broker issue, failover to backup
3. Monitor for recovery
4. Post-mortem after resolution

---

### Runbook: Data Quality Degradation

**Symptoms**: Quality score <80% for >10 minutes

**Diagnosis**:
1. Identify affected signals (quality dashboard)
2. Check validation failure logs
3. Review recent schema changes
4. Check sensor health (anomaly dashboard)

**Resolution**:
1. If schema issue: rollback or fix schema
2. If sensor issue: alert platform operations
3. If validation rule issue: adjust rules
4. Document root cause in incident log

## Related Documents

- [**../02-DATA_INGESTION/**](../02-DATA_INGESTION/00-README.md) - Ingestion pipeline configuration
- [**../03-DATA_STORAGE/**](../03-DATA_STORAGE/00-README.md) - Storage metrics
- [**../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/**](../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/) - SLA definitions
- [**../07-INTEGRATIONS/**](../07-INTEGRATIONS/00-README.md) - Integration monitoring

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial monitoring setup        | Operations Team |
