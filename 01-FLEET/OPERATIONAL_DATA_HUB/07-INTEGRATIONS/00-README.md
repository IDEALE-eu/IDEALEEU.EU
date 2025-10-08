# INTEGRATIONS

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > INTEGRATIONS**

Integration specifications for API gateway, Digital Thread, configuration management, and regulatory reporting.

## Purpose

Defines integration points between the Operational Data Hub and external systems:
- **API Gateway**: RESTful API specifications
- **Digital Thread Hooks**: Integration with Digital Thread
- **Config Management Links**: CM/DT integration
- **Quality/QMS Feed**: NCR/CAPA integration
- **Regulatory Reporting**: Adapters for EASA, FAA, ESA reporting

## Contents

- [**00-README.md**](00-README.md) - This file
- [**API_GATEWAY_SPECS/**](API_GATEWAY_SPECS/) - REST API specifications
- [**DIGITAL_THREAD_HOOKS.md**](DIGITAL_THREAD_HOOKS.md) - Digital Thread integration
- [**CONFIG_MGMT_LINKS.md**](CONFIG_MGMT_LINKS.md) - CM/DT integration, baseline refs, schema change workflow
- [**QUALITY_QMS_FEED.md**](QUALITY_QMS_FEED.md) - → [../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/](../../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/)
- [**REGULATORY_REPORTING_ADAPTERS/**](REGULATORY_REPORTING_ADAPTERS/) - Regulatory reporting adapters

## Integration Architecture

```
┌──────────────────────────────────────────────────────┐
│           OPERATIONAL DATA HUB                       │
└───────────────────┬──────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│ Digital  │ │ Config   │ │ Quality/QMS  │
│ Thread   │ │ Mgmt     │ │ (NCR/CAPA)   │
└──────────┘ └──────────┘ └──────────────┘
        │
        ▼
┌──────────────────┐
│ Regulatory       │
│ Reporting        │
└──────────────────┘
```

## API Gateway

See [**API_GATEWAY_SPECS/**](API_GATEWAY_SPECS/)

**Endpoints**:
```
# Data Products
GET    /api/v1/data-products
GET    /api/v1/data-products/{product_id}
POST   /api/v1/data-products/{product_id}/query

# Telemetry
POST   /api/v1/telemetry/ingest
GET    /api/v1/telemetry/stream

# Anomalies
GET    /api/v1/anomalies
POST   /api/v1/anomalies/subscribe

# Metadata
GET    /api/v1/metadata/signals
GET    /api/v1/metadata/lineage

# Contracts
GET    /api/v1/contracts/{product_id}
```

**Authentication**: OAuth 2.0, API keys
**Rate Limiting**: 1000 requests/minute per client
**Versioning**: URI versioning (`/v1`, `/v2`)

## Digital Thread Integration

See [**DIGITAL_THREAD_HOOKS.md**](DIGITAL_THREAD_HOOKS.md)

**Integration Points**:
1. **Data Ingestion**: Telemetry → Digital Thread
2. **Digital Twin Feedback**: Real-world data → DT model calibration
3. **Lineage Export**: OpenLineage → Digital Thread catalog
4. **Requirements Traceability**: Telemetry → Requirements verification

**Bidirectional Flow**:
- **DT → ODH**: Configuration baselines, digital twin predictions
- **ODH → DT**: Operational data, anomalies, performance deltas

## Configuration Management Integration

See [**CONFIG_MGMT_LINKS.md**](CONFIG_MGMT_LINKS.md)

**Baseline References**:
- Telemetry linked to configuration baselines
- Schema changes tracked via ECR/ECO process
- Version control synchronized with CM system

**Schema Change Workflow**:
```
ECR (Engineering Change Request)
  → Impact Assessment
  → CCB Approval
  → ECO (Engineering Change Order)
  → Schema Update in Registry
  → Notification to Consumers
```

**References**:
- Baseline refs: `../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
- ECR/ECO process: `../../00-PROGRAM/CONFIG_MGMT/06-CHANGE_CONTROL/`

## Quality/QMS Feed

See [**QUALITY_QMS_FEED.md**](QUALITY_QMS_FEED.md)

**Integration**: Anomalies → NCR/CAPA system

**Data Flow**:
```
Anomaly Detection (ODH)
  → Severity Assessment
  → NCR Creation (if CRITICAL/HIGH)
  → CAPA Workflow
  → Resolution → ODH Update
```

**References**: [../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/](../../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/)

## Regulatory Reporting

See [**REGULATORY_REPORTING_ADAPTERS/**](REGULATORY_REPORTING_ADAPTERS/)

**Supported Authorities**:
- **EASA**: European Union Aviation Safety Agency
- **FAA**: Federal Aviation Administration (US)
- **ESA**: European Space Agency

**Report Types**:
- Safety events (mandatory reporting)
- Performance monitoring (periodic reports)
- Incident investigations (ad-hoc)

**Adapters**:
- Format conversion (ODH → regulatory format)
- Data filtering (relevant data only)
- Compliance validation

## Event-Driven Integrations

### Webhooks
```yaml
# Example webhook configuration
webhook:
  url: https://external-system.com/webhook
  events:
    - anomaly.detected
    - data_product.updated
    - schema.changed
  auth:
    type: bearer_token
    token: ${WEBHOOK_TOKEN}
  retry:
    max_attempts: 3
    backoff: exponential
```

### Message Queue (Kafka)
```yaml
# Example Kafka integration
kafka_topics:
  - name: ideale.anomalies
    consumers:
      - digital_thread_service
      - predictive_maintenance_service
  - name: ideale.telemetry
    consumers:
      - digital_twin_service
```

## Integration Monitoring

**Key Metrics**:
- API request rate (requests/second)
- API error rate (%)
- Integration latency (p50, p95, p99)
- Webhook delivery success rate (%)

**Alerts**:
- API error rate >1%
- Integration latency >5 seconds (p99)
- Webhook delivery failure >3 consecutive attempts

## Related Documents

- [**../../00-PROGRAM/DIGITAL_THREAD/**](../../../00-PROGRAM/DIGITAL_THREAD/) - Digital Thread overview
- [**../../00-PROGRAM/CONFIG_MGMT/**](../../../00-PROGRAM/CONFIG_MGMT/) - Configuration management
- [**../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/**](../../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/) - Quality management
- [**../06-ANALYTICS_CONSUMPTION/**](../06-ANALYTICS_CONSUMPTION/00-README.md) - Data consumption layer

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial integration specs       | Integration Team |
