# Telemetry Topics

Diagnostic events are published to MQTT topics for real-time monitoring by the FL orchestrator.

## Topic Structure

```
fl/diagnostics/{aircraft_id}/{event_type}
```

## Topics

### 1. Diagnostic Reports

**Topic**: `fl/diagnostics/{aircraft_id}/report`

**Description**: Full diagnostic report containing health, network, storage, security, and training checks.

**Publish Frequency**: Every 60 seconds (configurable via timer)

**QoS**: 1 (at least once delivery)

**Retention**: 24 hours

**Payload**: JSON conforming to `diag_report.schema.json`

**Example**:
```
Topic: fl/diagnostics/AC-H2-001/report
Payload: See examples/diag_event.json
```

### 2. Critical Alerts

**Topic**: `fl/diagnostics/{aircraft_id}/alert/critical`

**Description**: Critical alerts requiring immediate action (e.g., storage full, network down, security violation)

**Publish Frequency**: On event (triggered by alert rules)

**QoS**: 2 (exactly once delivery)

**Retention**: 7 days

**Payload**: JSON conforming to `envelope.schema.json` with alert details

**Example**:
```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "event_type": "diagnostic.alert",
  "timestamp": "2025-10-11T19:00:00Z",
  "source": {
    "agent_id": "aircraft-edge-001",
    "aircraft_id": "AC-H2-001"
  },
  "payload": {
    "severity": "critical",
    "rule_name": "storage_critical",
    "message": "Storage at 92% - training suspended",
    "metric": "storage.disk_usage_percent",
    "value": 92
  },
  "routing": {
    "topic": "fl/diagnostics/AC-H2-001/alert/critical",
    "priority": "critical"
  }
}
```

### 3. Warning Alerts

**Topic**: `fl/diagnostics/{aircraft_id}/alert/warning`

**Description**: Warning alerts for degraded conditions (e.g., high latency, memory pressure)

**Publish Frequency**: On event (triggered by alert rules)

**QoS**: 1 (at least once delivery)

**Retention**: 3 days

### 4. Heartbeat

**Topic**: `fl/diagnostics/{aircraft_id}/heartbeat`

**Description**: Lightweight heartbeat to confirm agent is running

**Publish Frequency**: Every 5 minutes

**QoS**: 0 (at most once delivery)

**Retention**: 1 hour

**Payload**:
```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "event_type": "diagnostic.heartbeat",
  "timestamp": "2025-10-11T19:05:00Z",
  "source": {
    "agent_id": "aircraft-edge-001",
    "aircraft_id": "AC-H2-001"
  },
  "payload": {
    "status": "healthy",
    "uptime_seconds": 3600
  }
}
```

## Topic Subscriptions

### FL Orchestrator

The FL orchestrator subscribes to:
- `fl/diagnostics/+/report` - All diagnostic reports
- `fl/diagnostics/+/alert/critical` - All critical alerts

Use this data for:
- Real-time fleet health dashboard
- Client selection for training rounds
- Automatic exclusion of unhealthy clients

### System Health Monitor

The system health monitor subscribes to:
- `fl/diagnostics/+/alert/#` - All alerts
- `fl/diagnostics/+/heartbeat` - Heartbeat monitoring

Use this data for:
- Alerting and incident response
- Historical trend analysis
- Capacity planning

## Message Format

All messages use the envelope format defined in `envelope.schema.json`:

```json
{
  "event_id": "uuid",
  "event_type": "diagnostic.report|diagnostic.alert|diagnostic.heartbeat",
  "timestamp": "ISO 8601",
  "source": {
    "agent_id": "string",
    "aircraft_id": "AC-H2-XXX",
    "hostname": "string",
    "location": {
      "latitude": -90 to 90,
      "longitude": -180 to 180,
      "altitude_ft": number
    }
  },
  "payload": {},
  "metadata": {
    "schema_version": "1.0.0",
    "compression": "none|gzip|lz4"
  },
  "routing": {
    "topic": "string",
    "priority": "low|normal|high|critical"
  }
}
```

## Related Documents

- [**../SCHEMAS/diag_report.schema.json**](../SCHEMAS/diag_report.schema.json) - Diagnostic report schema
- [**../SCHEMAS/envelope.schema.json**](../SCHEMAS/envelope.schema.json) - Event envelope schema
- [**../../02-ORCHESTRATION/SCHEDULER.md**](../../02-ORCHESTRATION/SCHEDULER.md) - Training scheduler
- [**../../12-METRICS/KPI_DEFINITIONS.md**](../../12-METRICS/KPI_DEFINITIONS.md) - Metric definitions
