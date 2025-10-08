# AVIATION

Aviation compliance: DO-178C, DO-326A/355/356A cybersecurity.

## DO-178C Software Certification

### Scope

FL client software on aircraft edge devices:

- **DAL (Design Assurance Level)**: Level C (Major)
- **Rationale**: FL models are advisory; no direct actuation on flight-critical systems
- **Exclusion**: Ground stations, sim rigs (non-certified environments)

### DO-178C Objectives

1. **Software Planning**: Plan for Software Aspects of Certification (PSAC)
2. **Software Development**: Requirements, design, code, integration
3. **Software Verification**: Reviews, analysis, testing
4. **Configuration Management**: Version control, baseline management
5. **Quality Assurance**: Audits, compliance records

### Evidence

- **Requirements**: Linked in ../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/
- **Test cases**: Linked in ../../08-VALIDATION_VVP/TEST_PLANS.md
- **Traceability**: Requirements ↔ Design ↔ Code ↔ Tests

## DO-326A Cybersecurity

### Threat Model

- See ../../05-PRIVACY_SECURITY/THREAT_MODEL.md

### Security Controls

- Mutual TLS authentication
- ARINC 653 sandboxing (see ../../03-CLIENTS/AIRCRAFT_EDGE/SANDBOXING.md)
- Intrusion detection, audit logs

## DO-355/356A Connectivity Security

- **Scope**: LEO/GEO satellite links (SATCOM)
- **Controls**: TLS 1.3, certificate validation, rate limiting

## Related Documents

- **../../08-VALIDATION_VVP/CERT_EVIDENCE_LINKS.md** - Certification evidence
- **../../05-PRIVACY_SECURITY/THREAT_MODEL.md** - Cybersecurity threat model
- **../../03-CLIENTS/AIRCRAFT_EDGE/SANDBOXING.md** - ARINC 653 partitioning
