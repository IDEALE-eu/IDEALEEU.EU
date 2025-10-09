# MRO_LINKS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 09-INTEGRATIONS > MRO_LINKS**

Maintenance actions → twin update, twin RUL predictions → MRO planning.

## Purpose

Bidirectional integration between digital twin and MRO (Maintenance, Repair, Overhaul) system.

## Integration Architecture

```
[MRO System] ↔ [Digital Twin]
(01-FLEET/MRO_STRATEGY/)
        ↕
Maint Actions ↔ RUL Predictions
```

## Data Flows

### MRO → Twin: Maintenance Actions

**Purpose**: Update twin when maintenance actions performed (e.g., part replacement, repair)

**Source**: `01-FLEET/MRO_STRATEGY/02-PLANNING/WORK_ORDERS/`

**Data Elements**:
- **Work Order ID**: Unique identifier
- **Aircraft ID**: Which aircraft
- **ATA Chapter**: System affected (e.g., ATA-28 for H₂ fuel)
- **Component ID**: Part number (e.g., H2_VALVE_01)
- **Action Type**: Replacement, repair, inspection
- **Date**: When performed
- **Parts Used**: New part serial numbers

**Impact on Twin**:
1. **Reset RUL**: If component replaced, reset RUL counter to zero
2. **Update Configuration**: Update as-maintained config (see `../04-VERSIONING_CONFIG/SERIALIZED_INSTANCES/`)
3. **Recalibrate**: If major change (e.g., engine swap), trigger recalibration

**Example**:
```json
{
  "work_order_id": "WO-2025-0123",
  "aircraft_id": "ACFT-001",
  "date": "2025-01-15",
  "actions": [
    {
      "ata_chapter": "ATA-28",
      "component_id": "H2_VALVE_01",
      "action_type": "replacement",
      "old_part_sn": "VAL-12345",
      "new_part_sn": "VAL-67890",
      "twin_update_required": true
    }
  ]
}
```

### Twin → MRO: RUL Predictions

**Purpose**: Provide predictive maintenance recommendations to MRO planners

**Destination**: `01-FLEET/MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/`

**Data Elements**:
- **Aircraft ID**: Which aircraft
- **Component ID**: Part predicted to fail
- **RUL (Hours)**: Remaining useful life in flight hours
- **RUL (Cycles)**: Remaining useful life in flight cycles
- **Confidence**: Prediction confidence (0-1)
- **Recommendation**: Immediate, planned, or monitor
- **Criticality**: Safety level (A/B/C/D)

**Example**:
```json
{
  "aircraft_id": "ACFT-001",
  "timestamp": "2025-01-15T14:32:00Z",
  "rul_predictions": [
    {
      "component_id": "H2_VALVE_01",
      "rul_hours": 1250,
      "rul_cycles": 800,
      "confidence": 0.85,
      "recommendation": "planned",
      "criticality": "B"
    },
    {
      "component_id": "ENG_L_BEARING_03",
      "rul_hours": 150,
      "rul_cycles": 100,
      "confidence": 0.78,
      "recommendation": "immediate",
      "criticality": "A"
    }
  ]
}
```

## Integration Mechanisms

### API Integration

**REST API** (see `../03-INTERFACES_APIS/TWIN_API_SPEC.yaml`):
- `POST /maintenance/actions` - MRO system pushes maintenance actions to twin
- `GET /rul/{aircraft_id}` - MRO system retrieves RUL predictions from twin

### Event-Driven Integration

**Message Queue** (Kafka):
- **Topic**: `ideale.maintenance.actions` (MRO → Twin)
- **Topic**: `ideale.rul.predictions` (Twin → MRO)

### Batch Integration

**Scheduled Sync**:
- **Frequency**: Daily (02:00 UTC)
- **Format**: CSV or JSON files
- **Transport**: SFTP or S3 bucket

## MRO System Integration

### Work Order Management

**MRO Tool**: SAP PM, Maximo, or equivalent

**Integration Points**:
1. **Work Order Creation**: MRO creates work order → twin notified (planned maintenance)
2. **Work Order Completion**: MRO closes work order → twin updated (as-maintained config)
3. **RUL Alert**: Twin predicts failure → MRO creates preventive work order

### Predictive Maintenance Workflow

```
1. [Twin Detects Anomaly] → RUL prediction triggered
2. [RUL < Threshold] → Alert generated (e.g., RUL <200 hours)
3. [Alert → MRO System] → Preventive maintenance work order created
4. [MRO Plans Maintenance] → Schedule aircraft downtime
5. [Maintenance Performed] → Work order completed
6. [Maintenance Action → Twin] → Twin configuration updated
7. [RUL Reset] → Component RUL counter reset to zero
```

## Data Validation

### Maintenance Action Validation
- **Component ID**: Verify component exists in twin (see ATA mapping)
- **Action Type**: Valid action (replacement, repair, inspection)
- **Date**: Maintenance date not in future

### RUL Prediction Validation
- **Confidence Threshold**: Only send predictions with confidence >0.7
- **Negative RUL**: Flag as "IMMEDIATE" if RUL <0 (overdue)
- **Consistency**: Compare with previous predictions (no sudden jumps)

## Monitoring

### Integration Health

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| **API Error Rate** | <0.1% | >1% |
| **Maintenance Action Latency** | <1 hour | >24 hours |
| **RUL Prediction Latency** | <5 minutes | >1 hour |

### MRO Effectiveness

| Metric | Target | Description |
|--------|--------|-------------|
| **Preventive Maintenance Rate** | >80% | % of failures caught by RUL predictions |
| **False Positive Rate** | <20% | % of RUL alerts that were not actual failures |
| **Avoided Failures** | Maximize | Count of failures avoided by predictive maintenance |

## Related Documents

- **../01-ARCHITECTURE/TWIN_SCOPE.md** - Predictive maintenance use cases (UC-PRED-001)
- **../03-INTERFACES_APIS/STREAMS/OUTPUTS/KPIs_SCHEMA.yaml** - RUL output schema
- **01-FLEET/MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/TWIN_INTEGRATION.md** - MRO-side integration
- **ATA_MAPPING.md** - Model ↔ ATA chapter mapping

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
