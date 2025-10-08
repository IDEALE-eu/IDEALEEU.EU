# 05-PRIVACY_SECURITY

Privacy-preserving techniques and security policies for federated learning.

## Purpose

This directory defines privacy-preserving mechanisms (differential privacy, secure aggregation, homomorphic encryption) and security policies (threat model, pseudonymisation) for FL.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**DP_SGD.md**](DP_SGD.md) - Differential Privacy via DP-SGD ((ε, δ) budgets, accountant logs)
- [**SECURE_AGGREGATION.md**](SECURE_AGGREGATION.md) - Threshold Paillier, MPC
- [**HOMOMORPHIC_ENCRYPTION.md**](HOMOMORPHIC_ENCRYPTION.md) - Optional for high-sensitivity models
- [**PSEUDONYMISATION.md**](PSEUDONYMISATION.md) - GDPR-compliant client IDs (no tail numbers in clear)
- [**THREAT_MODEL.md**](THREAT_MODEL.md) - STRIDE analysis, attack surface map

## Privacy-Security Trade-offs

- **High privacy**: DP-SGD + Secure Aggregation (slower, less accurate)
- **Moderate privacy**: DP-SGD only (faster, good accuracy)
- **Low privacy**: Pseudonymisation only (fastest, regulatory minimum)

## Related Documents

- [**../04-ALGORITHMS/**](../04-ALGORITHMS/) -  Integration with FL algorithms
- [**../11-COMPLIANCE/PRIVACY.md**](../11-COMPLIANCE/PRIVACY.md) - GDPR compliance
- [**../16-INCIDENT_RESPONSE/**](../16-INCIDENT_RESPONSE/) -  Security incident handling
