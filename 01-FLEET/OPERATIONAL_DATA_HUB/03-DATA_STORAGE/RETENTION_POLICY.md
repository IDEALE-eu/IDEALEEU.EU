# RETENTION_POLICY

Data retention rules for operational telemetry.

## Purpose

Defines how long different types of data are retained, archived, and eventually deleted.

## Retention Classes

### Permanent Retention
**Retention Period**: Indefinite

**Data Types**:
- Safety-critical events (engine failures, system faults)
- Regulatory-required data (certifiable events)
- Anomalies and incidents (for trend analysis)
- Baseline configurations (system snapshots)

**Storage**:
- Hot (0-90 days): S3 Standard
- Cold (90+ days): S3 Glacier Deep Archive

**Deletion**: Only upon legal requirement (GDPR right to erasure, etc.)

---

### Long-Term Retention (5+ years)
**Retention Period**: 5-10 years

**Data Types**:
- Performance trends (efficiency, fuel consumption)
- Reliability data (MTBF, failure rates)
- Maintenance history (CAPA, NCRs)
- Training datasets for ML models

**Storage**:
- Hot (0-30 days): S3 Standard
- Warm (30-365 days): S3 Infrequent Access
- Cold (365+ days): S3 Glacier

**Deletion**: Automatic after retention period

---

### Medium-Term Retention (1-5 years)
**Retention Period**: 1-5 years (configurable per signal)

**Data Types**:
- Operational telemetry (all sensors)
- Flight/mission logs
- Environmental data
- System health metrics

**Storage**:
- Hot (0-30 days): S3 Standard
- Warm (30-180 days): S3 Infrequent Access
- Cold (180+ days): S3 Glacier

**Deletion**: Automatic after retention period

---

### Short-Term Retention (<1 year)
**Retention Period**: 30-365 days

**Data Types**:
- Verbose diagnostic logs
- Raw unprocessed data (post-curation)
- Temporary intermediate datasets
- Debug traces

**Storage**:
- Hot (0-30 days): S3 Standard
- Delete after 30-365 days

**Deletion**: Automatic after retention period

---

## Retention Schedule by Data Category

| Data Category | Retention Period | Storage Transition | Justification |
|---------------|------------------|-------------------|---------------|
| **Safety Events** | Permanent | Hot → Cold (90 days) | Regulatory, audit trail |
| **Flight Data (Raw)** | 5 years | Hot → Warm → Cold | Industry standard (FAA Part 121) |
| **Engine Performance** | 10 years | Hot → Warm → Cold | Reliability analysis, warranty |
| **H2 System Telemetry** | 5 years | Hot → Warm → Cold | New technology, long-term monitoring |
| **Cabin Environment** | 1 year | Hot → Warm → Delete | Operational, low criticality |
| **Debug Logs** | 90 days | Hot → Delete | Troubleshooting only |
| **Spacecraft Telemetry** | 10 years | Hot → Warm → Cold | Mission lifetime + analysis |
| **Anomaly Reports** | Permanent | Hot → Cold (90 days) | Trend analysis, ML training |

## Retention Workflow

```
┌─────────────┐  Ingestion  ┌─────────────┐  30 days   ┌─────────────┐
│ Raw Data    │────────────▶│ Hot Storage │───────────▶│ Warm        │
│             │             │ (S3 Std)    │            │ Storage     │
└─────────────┘             └─────────────┘            └─────────────┘
                                                               │
                                                        180 days
                                                               │
                                                               ▼
                                                        ┌─────────────┐
                                                        │ Cold        │
                                                        │ Storage     │
                                                        │ (Glacier)   │
                                                        └─────────────┘
                                                               │
                                                      Retention Period
                                                               │
                                                               ▼
                                                        ┌─────────────┐
                                                        │ Delete      │
                                                        │ (or keep if │
                                                        │ Permanent)  │
                                                        └─────────────┘
```

## Legal and Regulatory Requirements

### GDPR (General Data Protection Regulation)
- **Right to Erasure**: PII must be deletable upon request
- **Purpose Limitation**: Retain only for specified purposes
- **Storage Minimization**: Delete when no longer needed

**Implementation**:
- PII anonymized at ingestion (see ../04-DATA_SECURITY_COMPLIANCE/PII_HANDLING.md)
- Pseudonymized data retained per retention policy
- Erasure request triggers deletion of pseudonym mapping

### ITAR/EAR Export Control
- **Export-Controlled Data**: Special retention rules
- **Access Logging**: Audit trail retained permanently
- **Deletion**: Requires approval from export control officer

### Aviation Regulations (EASA, FAA)
- **Flight Data**: Minimum 5 years (FAA Part 121.344)
- **Maintenance Records**: 10 years
- **Safety Events**: Permanent

## Retention Policy Exceptions

### Exception Request Process
1. Submit retention exception request with justification
2. Data steward review
3. CCB approval (for >5 year extensions)
4. Document exception in retention schedule

### Common Exceptions
- **Extended ML Training Period**: 10 years for new models
- **Ongoing Investigation**: Retain until investigation closed
- **Legal Hold**: Retain until litigation resolved

## Automated Retention Management

### Lifecycle Policies
```yaml
# Example S3 lifecycle policy
rules:
  - id: operational_telemetry
    prefix: raw-vault/dt=
    transitions:
      - days: 30
        storage_class: STANDARD_IA  # Infrequent Access
      - days: 180
        storage_class: GLACIER
    expiration:
      days: 1825  # 5 years
  
  - id: safety_events
    prefix: curated/safety_events/
    transitions:
      - days: 90
        storage_class: GLACIER_DEEP_ARCHIVE
    # No expiration (permanent)
```

### Monitoring
- Daily report: Data volumes by retention class
- Monthly review: Retention policy compliance
- Alerts: Failed deletions, storage quota exceeded

## Restoration from Cold Storage

**Process**:
1. Submit restoration request with time range and reason
2. Data steward approval
3. Restore from Glacier (3-12 hours)
4. Temporary hot storage (7 days)
5. Automatic re-archive after 7 days

**Cost**:
- Restoration fee: $0.01/GB
- Data transfer: Standard egress charges

## Compliance Audits

**Audit Frequency**: Annually

**Audit Checks**:
- Retention periods correctly applied
- Expired data deleted on schedule
- Exceptions properly documented
- PII handling compliant with GDPR

## Related Documents

- **../04-DATA_SECURITY_COMPLIANCE/AUDIT_LOG_REQUIREMENTS.md** - Audit logging
- **../04-DATA_SECURITY_COMPLIANCE/PII_HANDLING.md** - GDPR compliance
- **../../09-TEMPLATES/RETENTION_SCHEDULE_TEMPLATE.csv** - Template for custom schedules

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial retention policy        | Data Engineering Team |
