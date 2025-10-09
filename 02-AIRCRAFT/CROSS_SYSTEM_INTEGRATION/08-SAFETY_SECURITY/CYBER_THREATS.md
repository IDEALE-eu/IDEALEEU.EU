# Cyber Threats (DO-326A)

## Overview

Threat log per DO-326A Airworthiness Security Process Specification.

## Threat Categories

### External Threats
1. **Passenger WiFi → Avionics**: Unauthorized access attempt from Zone 4
   - **Likelihood**: Remote
   - **Impact**: Catastrophic (if successful)
   - **Mitigation**: Complete network isolation, physical barriers
   - **Status**: Mitigated

2. **GNSS Spoofing**: False position/time injection
   - **Likelihood**: Occasional
   - **Impact**: Hazardous
   - **Mitigation**: Multi-constellation cross-check, signal quality monitoring
   - **Status**: Mitigated

3. **HIRF/EMI**: Electromagnetic interference
   - **Likelihood**: Probable (near airports, radar sites)
   - **Impact**: Major
   - **Mitigation**: HIRF protection per CS-25.1317, EMC per DO-160G
   - **Status**: Mitigated

### Insider Threats
4. **Malicious Maintenance**: Unauthorized software/config changes
   - **Likelihood**: Remote
   - **Impact**: Catastrophic
   - **Mitigation**: Cryptographic signing, MFA, audit logging
   - **Status**: Mitigated

5. **Supply Chain**: Compromised component
   - **Likelihood**: Extremely Remote
   - **Impact**: Catastrophic
   - **Mitigation**: Supplier vetting, secure boot, tamper detection
   - **Status**: Mitigated

## Threat Assessment Matrix

| Threat ID | Threat | Likelihood | Impact | Risk Level | Mitigation | Status |
|-----------|--------|------------|--------|------------|------------|--------|
| THR-001 | Passenger WiFi intrusion | Remote | Catastrophic | High | Zone isolation | Mitigated |
| THR-002 | GNSS spoofing | Occasional | Hazardous | Medium | Multi-constellation | Mitigated |
| THR-003 | HIRF upset | Probable | Major | Medium | HIRF protection | Mitigated |
| THR-004 | Malicious maintenance | Remote | Catastrophic | High | Crypto + MFA | Mitigated |
| THR-005 | Supply chain attack | Extremely Remote | Catastrophic | Medium | Secure boot | Mitigated |

## References
- **DO-326A**: Airworthiness Security Process Specification
- **DO-356A**: Airworthiness Security Methods and Considerations
- **[02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md](../../02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md)** - Security zones
- **[SAFETY_CYBER_CROSSWALK.csv](./SAFETY_CYBER_CROSSWALK.csv)** - Safety/security integration
