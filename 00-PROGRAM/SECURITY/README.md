# SECURITY

Security policies, threat models, SBOM/VEX, and incident response for AMPEL360.

## Purpose

Manage security risks, cryptographic keys, vulnerability tracking, and incident response across all program artifacts.

## Contents

- **Risk Models** - Threat modeling and risk assessments per LRU/SW unit
- **Key Management** - Custody, rotation, and HSM procedures
- **SBOM/VEX** - Software Bill of Materials and Vulnerability Exploitability eXchange
- **Incident Response** - Runbooks, communications, and evidence capture
- **Attestations** - Security certifications and compliance evidence

## Key Principles

- Threat model required for all software and electronics
- SBOM required for all software; VEX for known vulnerabilities
- Cryptographic keys managed with custody chain and rotation schedules
- HSM (Hardware Security Module) usage when available
- Incident response with defined escalation paths and evidence preservation

## Related Documents

- Governance: [`../GOVERNANCE/README.md`](../GOVERNANCE/README.md)
- Compliance: [`../COMPLIANCE/`](../COMPLIANCE/)
- Quality: [`../QUALITY_QMS/`](../QUALITY_QMS/)
