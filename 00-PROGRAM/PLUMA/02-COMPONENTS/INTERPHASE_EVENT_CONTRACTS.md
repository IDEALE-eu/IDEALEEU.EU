# Interphase API - Event Contracts

## Overview

Interphase publishes events to Kafka topics and can push notifications to registered webhooks. Events follow a standardized schema for consistency and reliability.

## Event Schema

All events published to the `interphase.events` topic follow this schema:

```json
{
  "eventId": "8d2c8e71-1f0d-4c02-8e7d-9a2ab2a7e3b1",
  "type": "context.frozen | gate.decision | transition.started | transition.succeeded | transition.failed | validation.passed | validation.failed",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/.../bundle",
  "occurredAt": "2025-10-14T12:00:00Z",
  "evidence": [
    "utcs://.../reports/structure.json",
    "utcs://.../reports/kpis.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "user": "john.doe@ampel.aero",
    "source": "interphase-api-v1"
  }
}
```

## Event Types

### 1. context.frozen

Published when a frozen context snapshot is created.

**Example**:
```json
{
  "eventId": "8d2c8e71-1f0d-4c02-8e7d-9a2ab2a7e3b1",
  "type": "context.frozen",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/CAD/FROZEN/20251014",
  "occurredAt": "2025-10-14T12:00:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../MANIFEST.csv",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../CHECKSUM.sha256"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "user": "jane.engineer@ampel.aero",
    "artifactCount": 1247,
    "sizeBytes": 5368709120,
    "checksumAlgorithm": "sha256"
  }
}
```

### 2. gate.decision

Published when a phase gate decision (Approve/Reject/Hold) is recorded.

**Example**:
```json
{
  "eventId": "7b3d9f82-2e1c-4d03-9f8e-0c3db3c6e4c2",
  "type": "gate.decision",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "occurredAt": "2025-10-14T14:30:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/design-review-v3.pdf",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-results.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "decision": "Approve",
    "decidedBy": "ccb-179",
    "comment": "All validation checks passed. Design review completed."
  }
}
```

### 3. transition.started

Published when a phase/gate transition begins.

**Example**:
```json
{
  "eventId": "6a2e8d91-3f2d-5e14-0g9f-1d4ec4d7f5d3",
  "type": "transition.started",
  "programId": "ampel360-bwb-q100",
  "phase": "CAE",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "occurredAt": "2025-10-14T15:00:00Z",
  "metadata": {
    "tenant": "ampel-aerospace",
    "transitionId": "9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4",
    "fromPhase": "CAD",
    "fromGate": "CB",
    "toPhase": "CAE",
    "toGate": "CB",
    "user": "transition.service@ampel.aero"
  }
}
```

### 4. transition.succeeded

Published when a phase/gate transition completes successfully.

**Example**:
```json
{
  "eventId": "5b1d7c80-2e1c-4d03-9f8e-0c3db3c6e4c2",
  "type": "transition.succeeded",
  "programId": "ampel360-bwb-q100",
  "phase": "CAE",
  "gate": "CB",
  "snapshotId": "d0d2c5g1-6f1b-5c9d-0b32-7g7c1c4c6c6b",
  "occurredAt": "2025-10-14T15:05:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../CAE/MANIFEST.csv",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/transition-report.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "transitionId": "9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4",
    "fromPhase": "CAD",
    "fromGate": "CB",
    "toPhase": "CAE",
    "toGate": "CB",
    "durationSeconds": 300,
    "artifactsMigrated": 1247,
    "validationsPassed": 12
  }
}
```

### 5. transition.failed

Published when a phase/gate transition fails.

**Example**:
```json
{
  "eventId": "4a0c6b79-1d0b-3c02-8e7d-9a2ab2a7e3b1",
  "type": "transition.failed",
  "programId": "ampel360-bwb-q100",
  "phase": "CAE",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "occurredAt": "2025-10-14T15:03:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-errors.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "transitionId": "9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4",
    "fromPhase": "CAD",
    "fromGate": "CB",
    "toPhase": "CAE",
    "toGate": "CB",
    "errorCode": "validation_failed",
    "errorMessage": "Structure validation failed: 3 missing artifacts",
    "failedValidations": ["Structure"]
  }
}
```

### 6. validation.passed

Published when validation checks pass.

**Example**:
```json
{
  "eventId": "3e9b5a68-0c9a-2b01-7d6c-8a1ab1a6d2a0",
  "type": "validation.passed",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "occurredAt": "2025-10-14T11:55:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/structure-validation.json",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/links-validation.json",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/kpis-validation.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "validationId": "f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
    "validationTargets": ["Structure", "Links", "KPIs"],
    "checksPerformed": 42,
    "allChecksPassed": true
  }
}
```

### 7. validation.failed

Published when validation checks fail.

**Example**:
```json
{
  "eventId": "2d8a4b57-9b8a-1a90-6c5b-7a0aa0a5c1a9",
  "type": "validation.failed",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "occurredAt": "2025-10-14T11:50:00Z",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-errors.json"
  ],
  "metadata": {
    "tenant": "ampel-aerospace",
    "validationId": "f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
    "validationTargets": ["Structure", "Links"],
    "failedTarget": "Structure",
    "errorCount": 3,
    "errors": [
      {
        "code": "missing_artifact",
        "message": "Required artifact not found: PLM/CAx/CAD/MODELS/wing-assembly.step",
        "path": "PLM/CAx/CAD/MODELS/"
      },
      {
        "code": "invalid_checksum",
        "message": "Checksum mismatch for artifact: PLM/CAx/CAD/DOC/design-spec-v3.pdf",
        "path": "PLM/CAx/CAD/DOC/design-spec-v3.pdf"
      },
      {
        "code": "missing_metadata",
        "message": "Missing required metadata field: owner",
        "path": "PLM/CAx/CAD/META.json"
      }
    ]
  }
}
```

## Kafka Topic Configuration

### Topic: interphase.events

**Configuration**:
```yaml
topic: interphase.events
partitions: 12
replication_factor: 3
retention_ms: 2592000000  # 30 days
compression_type: snappy
min_insync_replicas: 2

partition_key: programId  # Ensures ordering per program
```

**Consumer Groups**:
- `interphase-webhooks`: Forwards events to registered webhooks
- `interphase-metrics`: Aggregates events for metrics dashboard
- `interphase-audit`: Stores events for audit trail
- `enterprise-memory`: Indexes events for historical queries

## Webhook Delivery

### Request Format

Webhooks receive POST requests with the event payload:

```http
POST /webhook/endpoint HTTP/1.1
Host: example.com
Content-Type: application/json
X-PLUMA-Event-Type: context.frozen
X-PLUMA-Event-ID: 8d2c8e71-1f0d-4c02-8e7d-9a2ab2a7e3b1
X-PLUMA-Signature: sha256=abc123...
X-PLUMA-Timestamp: 2025-10-14T12:00:01Z

{
  "eventId": "8d2c8e71-1f0d-4c02-8e7d-9a2ab2a7e3b1",
  "type": "context.frozen",
  ...
}
```

### Signature Verification

Webhooks are signed using HMAC-SHA256:

```python
import hmac
import hashlib

def verify_signature(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

### Retry Policy

- **Initial Delivery**: Immediate
- **Retry 1**: After 1 minute
- **Retry 2**: After 5 minutes
- **Retry 3**: After 15 minutes
- **Retry 4**: After 1 hour
- **Max Retries**: 4
- **Timeout**: 30 seconds per attempt
- **Success**: HTTP 2xx response
- **Failure**: HTTP 4xx, 5xx, or timeout

### Webhook Status

Webhooks that fail all retries are marked as `inactive` and must be re-registered.

## Event Filtering

Consumers can filter events by:

- **Event Type**: Subscribe to specific event types
- **Program**: Filter by program ID
- **Phase**: Filter by CAx phase
- **Gate**: Filter by MAL service gate
- **Tenant**: Multi-tenant isolation

**Example Kafka Consumer**:
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'interphase.events',
    bootstrap_servers=['kafka.interphase.ap-aero.portfolio:9092'],
    group_id='my-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    event = message.value
    
    # Filter by event type
    if event['type'] in ['context.frozen', 'gate.decision']:
        # Filter by program
        if event['programId'] == 'ampel360-bwb-q100':
            process_event(event)
```

## Event Schema Versioning

Events include a schema version for backward compatibility:

```json
{
  "schemaVersion": "1.0",
  "eventId": "...",
  "type": "...",
  ...
}
```

**Version History**:
- **1.0** (2025-10-14): Initial schema

## Monitoring & Observability

### Metrics

- **Event Publish Rate**: Events/second per type
- **Event Latency**: Time from occurrence to publish (p95, p99)
- **Webhook Delivery Rate**: Success/failure rate per endpoint
- **Consumer Lag**: Offset lag per consumer group

### Alerting

- **High Event Latency**: p99 > 5 seconds
- **Webhook Failures**: >10% failure rate over 5 minutes
- **Consumer Lag**: Lag > 10,000 messages
- **Partition Imbalance**: >20% difference between partitions

## Best Practices

1. **Idempotency**: Process events idempotently using `eventId`
2. **Ordering**: Rely on partition key (programId) for ordering guarantees
3. **Error Handling**: Implement exponential backoff for retries
4. **Monitoring**: Track consumer lag and processing latency
5. **Schema Evolution**: Plan for backward-compatible schema changes
6. **Security**: Verify webhook signatures, use TLS for Kafka

## Related Documentation

- [Interphase API Specification](./INTERPHASE_API_SPEC.yaml)
- [Interphase cURL Examples](./INTERPHASE_CURL_EXAMPLES.md)
- [Interphase Data Model](./INTERPHASE_DATA_MODEL.sql)
- [PLUMA Components](./README.md)
