# DO-326A Hardening

## Overview

Security hardening measures per DO-326A Airworthiness Security Process.

## Security Zones

Per [02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md](../../02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md):
- Zone 1: Flight-Critical (isolated)
- Zone 2: Safety-Critical (controlled conduits)
- Zone 3: Aircraft Systems (monitored)
- Zone 4: Passenger/Crew (untrusted, isolated)
- Zone 5: Maintenance (ground-only, authenticated)

## Cryptographic Protection

- **Secure Boot**: Hardware root of trust (TPM 2.0) for DAL A/B systems
- **Encryption**: AES-256-GCM for sensitive data
- **Signing**: RSA-3072 for software updates
- **Authentication**: MFA for maintenance access

## SBOM (Software Bill of Materials)

Software Bill of Materials maintained per system:
- Open-source components tracked
- License compliance verified
- Vulnerability scanning (CVE database)
- Update tracking for security patches

**Location**: [06-SOFTWARE_INTEGRATION/BUILD_BASELINES.md](../../06-SOFTWARE_INTEGRATION/BUILD_BASELINES.md)

## Threat Mitigation

All threats documented in [08-SAFETY_SECURITY/CYBER_THREATS.md](../../08-SAFETY_SECURITY/CYBER_THREATS.md) with mitigations.

## Compliance Evidence

- DO-326A threat log
- Security risk assessment
- Penetration test results
- Security review minutes

## References

- **DO-326A**: Airworthiness Security Process Specification
- **DO-356A**: Airworthiness Security Methods and Considerations
- **[08-SAFETY_SECURITY/](../../08-SAFETY_SECURITY/)** - Security documentation
