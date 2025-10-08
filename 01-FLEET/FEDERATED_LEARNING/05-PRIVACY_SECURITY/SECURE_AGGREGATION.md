# SECURE_AGGREGATION

Cryptographic secure aggregation protocols for FL.

## Overview

Secure aggregation ensures server cannot see individual client updates, only aggregated result.

## Protocols

### Threshold Paillier Encryption

- **Threshold**: t = 5 (minimum clients for decryption)
- **Key size**: 2048-bit (RSA-level security)
- **Performance**: ~1 second per client update

### Multi-Party Computation (MPC)

- **Protocol**: Shamir Secret Sharing
- **Threshold**: t = 5
- **Performance**: ~5 seconds per client update

## When to Use

- **High-sensitivity models**: Medical data, PII
- **Regulatory requirement**: GDPR Art. 32 (security of processing)
- **Adversarial server**: Do not trust aggregation server

## Trade-offs

- **Pro**: Strong cryptographic privacy
- **Con**: 5-10x slower, complex key management

## Related Documents

- **DP_SGD.md** - Combine with differential privacy
- **THREAT_MODEL.md** - Threat scenarios
