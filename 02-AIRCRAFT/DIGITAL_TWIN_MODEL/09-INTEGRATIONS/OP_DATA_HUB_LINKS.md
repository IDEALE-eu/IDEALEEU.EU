# OP_DATA_HUB_LINKS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 09-INTEGRATIONS > OP_DATA_HUB_LINKS**

Telemetry ↔ twin input links to Operational Data Hub.

## Purpose

Define integration between digital twin and operational data hub for telemetry ingestion and KPI output.

## Integration Architecture

```
[Operational Data Hub] ↔ [Digital Twin]
      (01-FLEET/OPERATIONAL_DATA_HUB/)
              ↕
    Telemetry Input + KPI Output
```

## Data Flows

### Telemetry Input (ODH → Twin)

**Source**: `01-FLEET/OPERATIONAL_DATA_HUB/05-DATA_PRODUCTS/`

**Mapping**: See `../03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`

**Protocol**: 
- **Real-Time**: MQTT, Kafka (streaming)
- **Batch**: REST API (POST /telemetry)

**Format**: 
- **Time-Series**: InfluxDB line protocol, Parquet
- **Schema**: JSON Schema validation

**Example**:
```json
{
  "aircraft_id": "ACFT-001",
  "timestamp": "2025-01-15T14:32:00Z",
  "signals": [
    {"signal_id": "H2_TANK_PRES_01", "value": 245.3, "unit": "bar"},
    {"signal_id": "H2_TANK_TEMP_01", "value": 22.5, "unit": "K"},
    {"signal_id": "ENG_EGT_L", "value": 1050, "unit": "degC"}
  ]
}
```

### KPI Output (Twin → ODH)

**Destination**: `01-FLEET/OPERATIONAL_DATA_HUB/05-DATA_PRODUCTS/`

**Schema**: See `../03-INTERFACES_APIS/STREAMS/OUTPUTS/KPIs_SCHEMA.yaml`

**Protocol**: 
- **Real-Time**: WebSocket (pub/sub)
- **Batch**: REST API (POST /kpis)

**Format**: JSON

**Example**:
```json
{
  "aircraft_id": "ACFT-001",
  "timestamp": "2025-01-15T14:32:00Z",
  "health": {
    "overall_score": 92,
    "status": "healthy"
  },
  "rul": {
    "components": [
      {"component_id": "H2_VALVE_01", "rul_hours": 1250}
    ]
  },
  "alerts": [
    {
      "alert_id": "ALERT-20250115-001",
      "severity": "warning",
      "message": "H2 boil-off rate above nominal"
    }
  ]
}
```

## API Integration

### REST API

**Base URL**: `https://api.ideale-eu.org/twin/v1/`

**Endpoints**:
- `POST /telemetry` - Ingest telemetry data
- `GET /kpis/{aircraft_id}` - Retrieve KPIs
- `POST /alerts` - Push alerts to ODH

**Authentication**: OAuth2 + mTLS (see `../03-INTERFACES_APIS/TWIN_API_SPEC.yaml`)

### Message Queue (Kafka)

**Topics**:
- `ideale.telemetry` - Telemetry from aircraft (ODH → Twin)
- `ideale.kpis` - KPIs from twin (Twin → ODH)
- `ideale.alerts` - Alerts from twin (Twin → ODH)

**Consumer Group**: `digital_twin_service`

## Data Lineage

**Traceability**: OpenLineage integration (see `01-FLEET/OPERATIONAL_DATA_HUB/04-LINEAGE/`)

**Lineage Flow**:
```
[Aircraft Sensor] → [ACMS] → [ODH Ingestion] → [Twin Model] → [KPI Output] → [ODH Analytics]
```

## Quality Checks

### Data Validation (ODH → Twin)
- **Schema Validation**: JSON Schema compliance
- **Range Checks**: Sensor values within expected min/max
- **Freshness**: Data timestamp within 10 seconds (real-time)

### Output Validation (Twin → ODH)
- **Schema Validation**: KPI schema compliance
- **Completeness**: All required fields present
- **Consistency**: Cross-check with previous predictions (no sudden jumps)

## Monitoring

### Integration Health Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| **API Error Rate** | <0.1% | >1% |
| **Telemetry Latency (p99)** | <1s | >5s |
| **KPI Output Latency (p99)** | <5s | >10s |
| **Data Freshness** | <10s | >60s |

### Dashboards

- **Grafana**: Real-time metrics, latency histograms
- **Kibana**: Log analysis, error investigation

## Related Documents

- **../03-INTERFACES_APIS/** - API specifications and data schemas
- **01-FLEET/OPERATIONAL_DATA_HUB/07-INTEGRATIONS/DIGITAL_THREAD_HOOKS.md** - ODH integration points
- **01-FLEET/OPERATIONAL_DATA_HUB/04-LINEAGE/** - Data lineage tracking

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
