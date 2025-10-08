# CONFIG_MGMT_LINKS

Integration between Operational Data Hub and Configuration Management system.

## Purpose

Ensures operational telemetry is linked to configuration baselines and schema changes follow proper change control process.

## Baseline References

### Configuration Baseline Linkage

**Reference**: `../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/`

All telemetry data tagged with applicable configuration baselines:

```yaml
telemetry_metadata:
  platform_id: AC-H2-001
  timestamp: 2024-01-15T14:30:00Z
  configuration_baseline:
    id: BASELINE-AC-H2-001-V1.2.3
    effective_date: 2024-01-01
    components:
      - h2_propulsion_system: REV-C
      - avionics_suite: SW-2.1.0
      - flight_control_system: FCS-2.1.0
  hardware_revision: H2-TANK-REV-C
  software_version: FCS-2.1.0
```

**Benefits**:
1. **Traceability**: Link telemetry to specific hardware/software versions
2. **Root Cause Analysis**: Identify configuration-specific issues
3. **Change Impact Assessment**: Compare performance before/after changes
4. **Compliance**: Maintain audit trail for certifications

### Baseline Change Tracking

When configuration baselines change:

```
Configuration Change (CM)
  → Update Baseline in CM System
  → Notify ODH via API
  → Tag New Telemetry with New Baseline
  → Enable Before/After Comparison
```

## Schema Change Workflow

### ECR → ECO → Schema Update

**Process**:

```
Step 1: Engineering Change Request (ECR)
  ↓
Step 2: Impact Assessment
  - Which consumers affected?
  - Backward compatibility impact?
  - Migration effort required?
  ↓
Step 3: CCB Review and Approval
  ↓
Step 4: Engineering Change Order (ECO)
  ↓
Step 5: Schema Update in Registry
  ↓
Step 6: Consumer Notification (90 days for breaking changes)
  ↓
Step 7: Dual-Publish Period (if breaking change)
  ↓
Step 8: Deprecate Old Schema
  ↓
Step 9: Archive Old Schema (after 1 year)
```

**Reference**: `../../00-PROGRAM/CONFIG_MGMT/06-CHANGE_CONTROL/`

### ECR Template for Schema Changes

```markdown
# Engineering Change Request (ECR)

**ECR ID**: ECR-2024-XXXX
**Date**: 2024-01-15
**Originator**: Data Engineering Team

## Change Description
Change hydrogen tank pressure signal unit from bar to PSI.

## Rationale
Align with US aviation industry standard for pressure units.

## Impact Assessment

### Affected Schemas
- Schema: `h2_tank_pressure_fwd`
- Current Version: v1.2.0
- Proposed Version: v2.0.0 (breaking change)

### Affected Systems
- Operational Data Hub ingestion pipelines
- Digital Thread integration
- Predictive maintenance models
- Fleet operations dashboards

### Consumers Impacted
- 15 data consumers identified
- 3 ML models require retraining
- 2 dashboards require updates

### Migration Effort
- Estimated effort: 80 hours
- Timeline: 120 days (including dual-publish period)

## Proposed Implementation

1. Register new schema v2.0.0 with PSI units
2. Create new Kafka topic: `fl.acft.h2.pressure.v2`
3. Dual-publish to v1 (bar) and v2 (PSI) for 90 days
4. Migrate consumers to v2
5. Deprecate v1, archive after 1 year

## Approval

- [ ] Data Steward
- [ ] System Engineer
- [ ] CCB Chair
- [ ] Affected Stakeholders

**Approval Date**: __________
**ECO Number**: ECO-2024-XXXX (assigned after approval)
```

### Schema Change API Integration

**Notify CM System of Schema Changes**:

```bash
POST https://config-mgmt.ideale.eu/api/v1/schema-changes
Authorization: Bearer $CM_API_TOKEN
Content-Type: application/json

{
  "ecr_id": "ECR-2024-XXXX",
  "eco_id": "ECO-2024-YYYY",
  "schema_id": "h2_tank_pressure_fwd",
  "old_version": "1.2.0",
  "new_version": "2.0.0",
  "change_type": "breaking",
  "effective_date": "2024-06-01",
  "affected_consumers": [
    "predictive_maintenance_service",
    "fleet_operations_dashboard"
  ]
}
```

## Integration with Digital Thread

**Configuration Baseline → Digital Thread → ODH**:

```
Configuration Management System
  → Baseline Definition
  → Digital Thread (MBSE Model Update)
  → ODH (Telemetry Tagging)
```

**Reference**: `../../00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/INTEGRATION_POINTS.md`

## Telemetry-to-Baseline Mapping

### Automatic Tagging

ODH automatically tags telemetry with current baseline:

```python
# Example automatic baseline tagging
def tag_telemetry_with_baseline(platform_id, timestamp):
    # Query CM system for active baseline
    baseline = cm_api.get_baseline(
        platform_id=platform_id,
        effective_date=timestamp
    )
    
    return {
        "baseline_id": baseline.id,
        "baseline_version": baseline.version,
        "components": baseline.components
    }
```

### Baseline Comparison Queries

Compare telemetry across baselines:

```sql
-- Compare H2 consumption before/after baseline change
SELECT 
  baseline_id,
  AVG(h2_consumed_kg) AS avg_consumption,
  STDDEV(h2_consumed_kg) AS stddev_consumption
FROM usage_profiles
WHERE platform_id = 'AC-H2-001'
  AND date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY baseline_id;
```

## Schema Deprecation Workflow

### 90-Day Deprecation Notice

```markdown
# Schema Deprecation Notice

**Schema**: `h2_tank_pressure_fwd`
**Version**: v1.2.0
**Deprecation Date**: 2024-06-01
**Archive Date**: 2025-06-01 (1 year after deprecation)

## Reason for Deprecation
Replaced by v2.0.0 with PSI units (ECO-2024-YYYY).

## Migration Path
1. Update consumers to read from topic `fl.acft.h2.pressure.v2`
2. Convert existing data if needed: `bar_to_psi(value) = value * 14.5038`
3. Test with sample data before migration

## Support Timeline
- **Day 0-90**: Dual-publish (v1 and v2)
- **Day 90-365**: v1 read-only, v2 active
- **Day 365+**: v1 archived

## Contact
Data Engineering Team: data-engineering@ideale.eu
```

## Monitoring

**Key Metrics**:
- Baseline tagging completeness (% of telemetry with baseline)
- Schema change lead time (ECR → ECO → Implementation)
- Consumer migration success rate
- ECR approval time

**Alerts**:
- Telemetry without baseline tag
- Schema change overdue (>90 days from ECO)
- Consumer not migrated to new schema (>90 days after deprecation)

## Related Documents

- **../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/** - Configuration baselines
- **../../00-PROGRAM/CONFIG_MGMT/06-CHANGE_CONTROL/** - ECR/ECO process
- **../02-DATA_INGESTION/SCHEMA_REGISTRY/** - Schema registry
- **../../09-TEMPLATES/SCHEMA_CHANGE_RFC.md** - Schema change request template

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial CM integration          | Configuration Team |
