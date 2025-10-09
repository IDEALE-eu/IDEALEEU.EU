# CYBERSECURITY

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 07-RUNTIME_DEPLOYMENT > CYBERSECURITY**

DO-326A/355/356A compliance: Secure boot, model signing, input validation.

## Purpose

Define cybersecurity controls for digital twin runtime to protect against threats.

## Compliance Standards

- **DO-326A**: Airworthiness Security Process Specification
- **DO-355**: Information Security Guidance for Continuing Airworthiness
- **DO-356A**: Airworthiness Security Methods and Considerations
- **ISO/IEC 27001**: Information Security Management
- **NIST SP 800-53**: Security and Privacy Controls

## Threat Model

### Threats
1. **Model Tampering**: Malicious modification of model files (adversarial attack)
2. **Data Poisoning**: Corrupted telemetry data injected to mislead twin
3. **Unauthorized Access**: Unauthorized users accessing twin API
4. **Denial of Service (DoS)**: Overload twin runtime, prevent legitimate use
5. **Eavesdropping**: Interception of telemetry or predictions
6. **Supply Chain Attack**: Compromised models from untrusted sources

### Assets to Protect
- Model files (ONNX, pickle, etc.)
- Telemetry data (sensor streams)
- Predictions and KPIs (outputs)
- API credentials (OAuth2 tokens, mTLS certificates)
- Configuration data (as-built, as-maintained)

## Security Controls

### 1. Secure Boot (Edge Runtime)

**Objective**: Ensure only authorized software runs on aircraft IMA.

**Implementation**:
- **TPM (Trusted Platform Module)**: Store cryptographic keys, verify boot chain
- **Signed Bootloader**: Verify bootloader signature before execution
- **Measured Boot**: Measure each component hash, store in TPM
- **Attestation**: Remote attestation to verify integrity before data exchange

**Compliance**: DO-326A Section 3.2 (Platform Security)

### 2. Model Signing

**Objective**: Prevent tampered or untrusted models from being loaded.

**Implementation**:
- **GPG Signing**: All production models signed with GPG key
- **Public Key Distribution**: Public key stored in secure location (HSM - Hardware Security Module)
- **Verification on Load**: Runtime verifies signature before loading model
- **SLSA Framework**: Supply-chain Levels for Software Artifacts (SLSA Level 3+)

**Example**:
```bash
# Sign model
gpg --sign --armor anomaly_detector_v1.2.3.onnx

# Verify signature
gpg --verify anomaly_detector_v1.2.3.onnx.asc
```

**Compliance**: DO-356A Section 4.3 (Software Integrity)

### 3. Input Validation

**Objective**: Prevent injection attacks via telemetry or API inputs.

**Implementation**:
- **Schema Validation**: All telemetry validated against schema (see `../../03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`)
- **Range Checks**: Sensor values within expected min/max
- **Rate Limiting**: API requests limited (100 req/min per client)
- **SQL Injection Prevention**: Parameterized queries, no dynamic SQL
- **XSS Prevention**: Sanitize all user inputs (web UI)

**Compliance**: DO-356A Section 4.4 (Input Validation)

### 4. Encryption

#### At Rest
- **AES-256**: Encrypt all persistent storage (models, data, configs)
- **Key Management**: Keys stored in HSM, rotated annually

#### In Transit
- **TLS 1.3**: All network communication (API, telemetry)
- **mTLS**: Mutual TLS for inter-service communication
- **IPsec VPN**: Secure aircraft-to-ground datalink

**Compliance**: DO-355 Section 5.2 (Cryptography)

### 5. Authentication and Authorization

#### Authentication
- **OAuth2 + OIDC**: User authentication for API access
- **Certificate-Based**: mTLS certificates for services, aircraft
- **Multi-Factor Authentication (MFA)**: Required for administrative access

#### Authorization
- **Role-Based Access Control (RBAC)**: 
  - **Operator**: Read-only access to KPIs, alerts
  - **Engineer**: Read/write access to models, what-if scenarios
  - **Admin**: Full access, including model deployment
- **Least Privilege**: Users granted minimum necessary permissions
- **Audit Logging**: All access attempts logged (successful + failed)

**Compliance**: DO-326A Section 3.3 (Access Control)

### 6. Anomaly Detection (Cybersecurity)

**Objective**: Detect malicious activity or data poisoning.

**Implementation**:
- **Intrusion Detection System (IDS)**: Monitor API traffic for anomalous patterns
- **Telemetry Anomaly Detection**: Flag telemetry data inconsistent with physics
  - Example: Sudden 100°C jump in temperature (likely sensor fault or spoofing)
- **Rate Limiting**: Excessive API requests → temporary IP ban
- **Behavioral Analysis**: Detect unusual user activity (e.g., mass model download)

**Compliance**: DO-355 Section 6.1 (Monitoring)

### 7. Secure Development Lifecycle

**Objective**: Embed security in development process.

**Practices**:
- **Threat Modeling**: Identify threats early (see Threat Model above)
- **Secure Coding Standards**: MISRA-C, CERT C Coding Standard
- **Static Analysis**: Automated SAST (Static Application Security Testing) in CI/CD
- **Penetration Testing**: Annual pen test by independent security firm
- **Vulnerability Scanning**: Weekly scans of dependencies (OWASP Dependency-Check)
- **Security Training**: Annual training for all developers

**Compliance**: DO-326A Section 2 (Security Lifecycle)

### 8. Incident Response

**Objective**: Respond quickly to security incidents.

**Plan**:
1. **Detection**: Automated alerts (IDS, SIEM)
2. **Containment**: Isolate affected systems, revoke credentials
3. **Eradication**: Remove malware, patch vulnerabilities
4. **Recovery**: Restore from known-good backups
5. **Post-Incident**: Root cause analysis, lessons learned

**Compliance**: DO-355 Section 7 (Incident Management)

## Security Testing

### Penetration Testing
- **Frequency**: Annual, plus after major releases
- **Scope**: API gateway, edge runtime, model registry
- **Provider**: Independent third-party security firm

### Vulnerability Scanning
- **Frequency**: Weekly (automated)
- **Tools**: OWASP ZAP, Nessus, Dependency-Check
- **Remediation SLA**: Critical (7 days), High (30 days), Medium (90 days)

### Security Audits
- **Frequency**: Annual (internal), every 3 years (external)
- **Standards**: ISO 27001, DO-326A compliance

## Key Management

### Cryptographic Keys
- **Generation**: HSM-generated, 256-bit entropy
- **Storage**: HSM (Hardware Security Module) or Azure Key Vault
- **Rotation**: Annually, or after suspected compromise
- **Backup**: Encrypted backup in secure offline storage

### Certificates
- **mTLS Certificates**: 2048-bit RSA or 256-bit ECDSA, 1-year validity
- **Root CA**: Offline, air-gapped storage
- **Intermediate CA**: Online, for certificate issuance

## Compliance Matrix

| Requirement | Standard | Control | Implementation |
|-------------|----------|---------|----------------|
| Platform Security | DO-326A 3.2 | Secure Boot | TPM, measured boot |
| Software Integrity | DO-356A 4.3 | Model Signing | GPG, SLSA Level 3 |
| Input Validation | DO-356A 4.4 | Schema Validation | JSON Schema, range checks |
| Cryptography | DO-355 5.2 | Encryption | AES-256, TLS 1.3, mTLS |
| Access Control | DO-326A 3.3 | RBAC | OAuth2, mTLS, audit logs |
| Monitoring | DO-355 6.1 | IDS | Anomaly detection, SIEM |
| Incident Mgmt | DO-355 7 | Incident Response | Runbook, post-incident review |

## Related Documents

- **SAFETY_GUARDS.md** - Safety guardrails and interlocks
- **../../03-INTERFACES_APIS/TWIN_API_SPEC.yaml** - API security (OAuth2, rate limiting)
- **00-PROGRAM/STANDARDS/02-AIRCRAFT/CYBERSECURITY/** - Aircraft cybersecurity standards

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
