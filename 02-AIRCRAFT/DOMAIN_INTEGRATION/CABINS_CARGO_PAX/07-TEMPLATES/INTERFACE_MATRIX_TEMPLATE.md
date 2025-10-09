# Interface Matrix Template

## Purpose

This template provides a standard format for documenting system interfaces within the CABINS_CARGO_PAX domain.

## Instructions

1. Copy this template to create a new interface matrix
2. Replace [SYSTEM_NAME] with the actual system name
3. Fill in all sections with system-specific information
4. Remove instruction sections before finalizing

---

# Interface Matrix - [SYSTEM_NAME]

## Purpose

This document defines all interfaces for [SYSTEM_NAME] within the CABINS_CARGO_PAX domain.

## Interface Overview Matrix

| Subsystem | External System | Interface Type | Criticality | ICD Reference |
|-----------|-----------------|----------------|-------------|---------------|
| [Subsystem] | [External System] | [Mechanical/Electrical/Data] | [Critical/Normal/Low] | ICD-XX-YY |
| ... | ... | ... | ... | ... |

## Interface Details

### [External System Name]

**Interface Description:**
[Describe the interface]

**Interface Type:**
- Physical: [Describe physical connections]
- Electrical: [Voltage, current, power]
- Data: [Protocol, data rate, message format]

**Requirements:**
- [List key requirements]

**Reference:**
- [Configuration base reference]
- [ICD reference]

**Do NOT duplicate:** [What not to copy from other systems]

---

### [Next External System]

[Repeat structure for each external system]

---

## Interface Change Control

All interface changes follow the process defined in:
- [Change Rules](../../../01-GOVERNANCE/CHANGE_RULES.md)
- [Interface Management](../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

## Interface Verification

1. [List verification methods]
2. [Testing approach]
3. [Acceptance criteria]

## References

- [Domain Dependencies](../../../02-ARCHITECTURE/DEPENDENCIES.md)
- [Safety Boundaries](../../../01-GOVERNANCE/SAFETY_BOUNDARIES.md)
- [ICD Index](../../../05-LINKS/ICD_INDEX.md)

---

**Last Updated**: [DATE]
