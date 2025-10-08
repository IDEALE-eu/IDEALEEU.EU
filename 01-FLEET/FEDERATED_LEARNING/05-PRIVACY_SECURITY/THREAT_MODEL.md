# THREAT_MODEL

STRIDE threat model and attack surface analysis for FL.

## Threat Categories (STRIDE)

### Spoofing

- **Threat**: Attacker impersonates legitimate client
- **Mitigation**: Mutual TLS, X.509 certificates

### Tampering

- **Threat**: Attacker modifies model updates in transit
- **Mitigation**: HTTPS/TLS 1.3, message signing

### Repudiation

- **Threat**: Client denies sending malicious update
- **Mitigation**: Immutable audit logs (see ../16-INCIDENT_RESPONSE/AUDIT_LOGS/)

### Information Disclosure

- **Threat**: Attacker infers training data from model updates
- **Mitigation**: DP-SGD, secure aggregation

### Denial of Service

- **Threat**: Attacker floods server with requests
- **Mitigation**: Rate limiting, client authentication

### Elevation of Privilege

- **Threat**: Attacker gains admin access to aggregation server
- **Mitigation**: Role-based access control, least privilege

## Attack Surface

1. **Client-server communication**: SATCOM links (encryption required)
2. **Aggregation server**: High-value target (redundancy, monitoring)
3. **Client devices**: Compromise aircraft edge device (sandboxing required)
4. **Model repository**: Tamper with stored models (integrity checks)

## Related Documents

- **../11-COMPLIANCE/AVIATION.md** - DO-326A cybersecurity
- **../16-INCIDENT_RESPONSE/RUNBOOK.md** - Incident response procedures
