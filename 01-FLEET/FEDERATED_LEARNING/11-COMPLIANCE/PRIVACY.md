# PRIVACY

GDPR compliance: Art. 5, retention, DPO consultation.

## GDPR Principles (Art. 5)

### 1. Lawfulness, Fairness, Transparency

- **Legal basis**: Art. 6(1)(f) - Legitimate interest (safety, predictive maintenance)
- **Transparency**: Model cards, privacy notices

### 2. Purpose Limitation

- **Purpose**: Federated learning for predictive maintenance and anomaly detection
- **No secondary use**: Data not used for other purposes without consent

### 3. Data Minimization

- **Signals**: Only FL-relevant telemetry (see ../../01-ARCHITECTURE/DATA_CONTRACTS/)
- **No PII**: No crew names, passenger data, personal identifiers

### 4. Accuracy

- **Data quality**: Sensor calibration, validation (see ../../01-ARCHITECTURE/DATA_CONTRACTS/)
- **Error correction**: Anomaly detection, outlier removal

### 5. Storage Limitation

- **Retention**: 90 days (raw telemetry), 2 years (aggregated metrics)
- **Deletion**: Automated deletion after retention period

### 6. Integrity and Confidentiality

- **Encryption**: TLS 1.3, DP-SGD (see ../../05-PRIVACY_SECURITY/)
- **Access control**: Role-based, least privilege

## Data Subject Rights

### Right to Erasure (Art. 17)

- **Aircraft operators**: Can opt-out of FL (gradients deleted within 30 days)
- **Limitation**: Safety data retained per regulatory requirements (e.g., 5 years for maintenance records)

### Right to Data Portability (Art. 20)

- **Not applicable**: Aggregated FL gradients are not personal data

## DPO Consultation

- **Trigger**: New FL use case, high-risk processing
- **DPO Contact**: dpo@ideale.eu
- **Timeline**: 2 weeks for review

## Related Documents

- [**../../05-PRIVACY_SECURITY/PSEUDONYMISATION.md**](../../05-PRIVACY_SECURITY/PSEUDONYMISATION.md) - Pseudonymisation policy
- [**../../05-PRIVACY_SECURITY/DP_SGD.md**](../../05-PRIVACY_SECURITY/DP_SGD.md) - Differential privacy
- [**../../06-MODELS/DATASETS_INDEX.md**](../../06-MODELS/DATASETS_INDEX.md) - Dataset provenance
