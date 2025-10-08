# AUDIT_LOGS

Immutable, signed audit logs for regulatory compliance.

## Purpose

Maintain tamper-proof audit logs for FL system events to meet regulatory requirements (DO-178C, GDPR, EU AI Act).

## Contents

- **00-README.md** - This file
- (Audit logs generated automatically, stored in secure location)

## Audit Log Events

### Model Lifecycle Events

- Model training started/completed
- Model validation passed/failed
- Model deployed/rolled back
- Model archived/deleted

### Access Control Events

- User login/logout
- Role changes (privilege escalation)
- Data access (who accessed what, when)

### Security Events

- Authentication failures
- IDS/IPS alerts
- Blacklist/greylist changes

### Configuration Changes

- ECR/ECO submitted/approved
- Baseline changes
- Hyperparameter updates

## Log Format

```json
{
  "timestamp": "2024-11-15T10:30:00Z",
  "event_type": "model_deployment",
  "event_id": "evt-2024-11-15-001",
  "user": "ml-engineer@ideale.eu",
  "model_id": "FL-MODEL-PM-ENGINE-1.0.0",
  "action": "deploy",
  "target": "aircraft-hash-001",
  "result": "success",
  "signature": "sha256:a3f5b8c1d2e4f6a7..."
}
```

## Immutability

- **Append-only**: No deletions or modifications
- **Cryptographic signing**: Each log entry signed with private key
- **Verification**: Public key available for verification

## Storage

- **Primary**: Secure database (write-once-read-many)
- **Backup**: Offsite cold storage (S3 Glacier, Azure Archive)
- **Retention**: 5 years (regulatory requirement)

## Access Control

- **Read access**: Auditors, regulators, DPO, CCB
- **Write access**: Automated systems only (no manual writes)
- **Monitoring**: IDS/IPS on audit log access

## Related Documents

- **../../11-COMPLIANCE/** - Compliance frameworks (DO-178C, GDPR)
- **../../10-GOVERNANCE/ETHICS_REVIEW.md** - EU AI Act compliance
