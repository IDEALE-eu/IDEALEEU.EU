# DATA_SECURITY_COMPLIANCE

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > DATA_SECURITY_COMPLIANCE**

Security, access control, encryption, and regulatory compliance for operational data.

## Purpose

Ensures operational data is:
- **Classified** appropriately
- **Access-controlled** per RBAC/ABAC policies
- **Encrypted** at rest and in transit
- **Audited** comprehensively
- **Compliant** with GDPR, ITAR/EAR regulations

## Contents

- [**00-README.md**](00-README.md) - This file
- [**CLASSIFICATION_SCHEMA.md**](CLASSIFICATION_SCHEMA.md) - Data classification levels
- [**ACCESS_CONTROL_MATRIX.yaml**](ACCESS_CONTROL_MATRIX.yaml) - RBAC/ABAC rules (PR-reviewed)
- [**ENCRYPTION_STANDARD.md**](ENCRYPTION_STANDARD.md) - Encryption algorithms and key management
- [**AUDIT_LOG_REQUIREMENTS.md**](AUDIT_LOG_REQUIREMENTS.md) - Audit trail specifications
- [**PII_HANDLING.md**](PII_HANDLING.md) - GDPR compliance, anonymization, consent
- [**ITAR_EAR_CLASSIFICATION.md**](ITAR_EAR_CLASSIFICATION.md) - Export control classification

## Security Architecture

```
┌─────────────────────────────────────────────────────┐
│              DATA CLASSIFICATION                    │
│  Public | Internal | Confidential | Restricted      │
└───────────────────┬─────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│ ACCESS CONTROL   │    │  ENCRYPTION      │
│                  │    │                  │
│ - RBAC/ABAC      │    │ - At-rest: AES256│
│ - MFA Required   │    │ - In-transit: TLS│
│ - Role Approval  │    │ - Key Rotation   │
└──────────────────┘    └──────────────────┘
        │                       │
        └───────────┬───────────┘
                    ▼
        ┌───────────────────────┐
        │   AUDIT LOGGING       │
        │   - Who accessed      │
        │   - What data         │
        │   - When              │
        │   - From where        │
        └───────────────────────┘
```

## Data Classification

See [**CLASSIFICATION_SCHEMA.md**](CLASSIFICATION_SCHEMA.md)

### Classification Levels

| Level | Description | Examples | Access |
|-------|-------------|----------|--------|
| **Public** | Publicly releasable | Aggregated fleet statistics | All users |
| **Internal** | Internal use only | Operational telemetry | Employees |
| **Confidential** | Business-sensitive | Performance benchmarks | Need-to-know |
| **Restricted** | Highly sensitive | H2 system design data, export-controlled | CCB approval required |

### Classification Marking
All datasets tagged with classification level:
```yaml
dataset: h2_performance_metrics
classification: CONFIDENTIAL
export_control: EAR99
retention: 5 years
```

## Access Control

See [**ACCESS_CONTROL_MATRIX.yaml**](ACCESS_CONTROL_MATRIX.yaml)

### Role-Based Access Control (RBAC)

**Roles**:
- **Data Viewer**: Read-only access to non-confidential data
- **Data Analyst**: Read access to confidential data, write to curated datasets
- **Data Engineer**: Full access to ingestion pipelines, raw vault
- **Data Steward**: Metadata management, schema approval
- **Security Administrator**: Access control management, audit review

### Attribute-Based Access Control (ABAC)

**Attributes**:
- User clearance level (Public, Internal, Confidential, Restricted)
- Data classification level
- Export control classification (None, EAR99, ITAR)
- Purpose of access (operations, ML training, compliance)

**Policy Example**:
```yaml
rule: confidential_data_access
condition: |
  (user.clearance >= data.classification) AND
  (user.export_clearance covers data.export_control) AND
  (user.mfa_enabled == true)
action: ALLOW
```

## Encryption

See [**ENCRYPTION_STANDARD.md**](ENCRYPTION_STANDARD.md)

### At-Rest Encryption
- **Algorithm**: AES-256-GCM
- **Key Management**: AWS KMS or Azure Key Vault
- **Key Rotation**: Automatic quarterly rotation

### In-Transit Encryption
- **Protocol**: TLS 1.3
- **Cipher Suites**: ECDHE-RSA-AES256-GCM-SHA384 (minimum)
- **Certificate Management**: Let's Encrypt or internal CA

## Audit Logging

See [**AUDIT_LOG_REQUIREMENTS.md**](AUDIT_LOG_REQUIREMENTS.md)

**Logged Events**:
- Data access (read, write, delete)
- Schema changes
- Access control changes
- Export/download operations
- Authentication events (login, logout, failed attempts)

**Log Retention**: 7 years (regulatory requirement)

**Log Format** (JSON):
```json
{
  "timestamp": "2024-01-15T14:30:00Z",
  "user": "jane.doe@ideale.eu",
  "action": "READ",
  "resource": "s3://ideale-raw-vault/dt=2024-01-15/platform=AC-H2-001/",
  "classification": "CONFIDENTIAL",
  "result": "SUCCESS",
  "ip_address": "10.0.1.42",
  "user_agent": "Python/3.9 boto3/1.20.0"
}
```

## PII Handling (GDPR Compliance)

See [**PII_HANDLING.md**](PII_HANDLING.md)

### PII Identification
**Personally Identifiable Information** in operational data:
- Pilot names
- Crew IDs
- Passenger manifests (if any)
- Maintenance technician IDs

### Pseudonymization
All PII pseudonymized at ingestion:
```python
# Example
pilot_id = "PILOT-001"  # Original: "John Smith"
crew_id = "CREW-042"    # Original: "Jane Doe"
```

### Right to Erasure
Process for GDPR erasure requests:
1. Receive erasure request
2. Identify pseudonym mapping
3. Delete mapping (data becomes anonymized)
4. Retain anonymized telemetry per retention policy

## Export Control (ITAR/EAR)

See [**ITAR_EAR_CLASSIFICATION.md**](ITAR_EAR_CLASSIFICATION.md)

### Classification Criteria

| Classification | Description | Access Restrictions |
|----------------|-------------|---------------------|
| **ITAR** | US Munitions List | US persons only, export license required |
| **EAR (CCL)** | Commerce Control List | Export restrictions to certain countries |
| **EAR99** | Not subject to EAR | Minimal restrictions |
| **None** | Not export-controlled | No restrictions |

### Screening Process
1. Identify export-controlled data (H2 system design, propulsion)
2. Classify per ITAR/EAR
3. Tag datasets with export control classification
4. Enforce access control (ABAC)
5. Audit all exports

## Security Monitoring

**Key Metrics**:
- Failed authentication attempts
- Unauthorized access attempts
- Data exfiltration (large downloads)
- Access control violations
- Encryption key rotation status

**Alerts**:
- Failed login >5 attempts (potential brute force)
- Access to RESTRICTED data without approval
- Encryption key rotation overdue
- Audit log gap detected

## Compliance Certifications

**Target Certifications**:
- ISO 27001 (Information Security)
- SOC 2 Type II (Security, Availability, Confidentiality)
- GDPR (Data Protection)
- ITAR (Export Control)

## Related Documents

- [**../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/**](../../../00-PROGRAM/QUALITY_QMS/06-NCR_CAPA/) - Quality management
- [**../../00-PROGRAM/CONFIG_MGMT/**](../../../00-PROGRAM/CONFIG_MGMT/) - Configuration control
- [**../03-DATA_STORAGE/RETENTION_POLICY.md**](../03-DATA_STORAGE/RETENTION_POLICY.md) - Data retention
- [**../08-METRICS_AND_MONITORING/**](../08-METRICS_AND_MONITORING/00-README.md) - Security metrics

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial security documentation  | Security Team |
