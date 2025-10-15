# Traceability Links

[← Back to UTCS](../README.md) | [↑ Up to CMP](../../README.md)

Formal traceability links between requirements, design, and verification.

## Purpose

Establish bidirectional:
- Requirements traceability
- Verification traceability
- Interface traceability
- Change impact traceability

## Traceability Matrix

```csv
Requirement ID,Design Element,Analysis,Test,Verification Status
REQ-53-001,Drawing-001,STRESS-001,TEST-001,Verified
REQ-53-002,Drawing-002,FEA-002,TEST-002,In Progress
```

## Traceability Types

### Vertical Traceability
- System → Subsystem → Component
- Requirements decomposition
- Verification roll-up

### Horizontal Traceability
- Requirements → Design
- Design → Analysis
- Analysis → Test
- Test → Certification

## Traceability Tools

- Requirements management system
- PLM system
- Test management system
- Traceability database

## Related

- [Thread Maps](../THREAD_MAPS/)
- [Requirements](../../GOVERNANCE/REVIEWS/SRR/)
- [Verification](../../GOVERNANCE/REVIEWS/FRR/)
- [Configuration Management](../../../../../../../../../../00-CONFIG/RULES.md)
