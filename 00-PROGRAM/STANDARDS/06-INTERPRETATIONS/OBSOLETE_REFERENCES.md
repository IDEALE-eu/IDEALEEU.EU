# OBSOLETE_REFERENCES

Handling legacy and obsolete standards.

## Overview

This document provides guidance on handling standards that have been superseded or are no longer current. This is important for:
- Legacy systems in service
- Reuse of certified components
- Understanding historical designs
- Transition to new standards

## Obsolete Standards by Domain

### Aircraft

| Obsolete Standard | Current Replacement | Notes |
|-------------------|---------------------|-------|
| DO-178B | DO-178C | Software - released 2011 |
| DO-178A | DO-178C | Software - very old, pre-1992 |
| DO-254 (no letter) | DO-254 (current) | Hardware - minor updates over time |
| ARP4754 | ARP4754A | Systems Engineering - Rev A released 2010 |
| DO-160 (older revisions) | DO-160G | Environmental Test - regularly updated |
| MIL-HDBK-217 | Not directly replaced | Reliability prediction - no longer maintained, but still referenced |

### Spacecraft

| Obsolete Standard | Current Replacement | Notes |
|-------------------|---------------------|-------|
| PSS series (ESA) | ECSS series | Complete replacement, PSS phased out ~2000-2010 |
| ECSS-E-10A/B | ECSS-E-ST-10C | Revision updates (A, B, C) |
| NASA-STD-8719.xx (old) | NPR 8715.3 series | NASA transitioned from standards to procedural requirements |

### Cross-Cutting

| Obsolete Standard | Current Replacement | Notes |
|-------------------|---------------------|-------|
| MIL-STD-1553 | Not replaced | Still in use for some applications, but less common for new designs |
| ISO 9001:2008 | ISO 9001:2015 | Quality Management System |
| AS9100C | AS9100D | Aerospace QMS |
| ISO 14001:2004 | ISO 14001:2015 | Environmental Management |

## Handling Obsolete Standards

### Scenario 1: Existing Certified Product

**Situation**: You have an aircraft component certified to DO-178B and want to make a change.

**Approach**:
1. **Grandfathering**: Existing certification remains valid under DO-178B
2. **Minor Changes**: May continue under DO-178B with authority agreement
3. **Major Changes**: May require upgrade to DO-178C (authority decision)
4. **Documentation**: Document in PSAC what standard version used and rationale

**Reference**: FAA AC 20-115D provides guidance on DO-178B to DO-178C transition

### Scenario 2: Reusing Certified Component

**Situation**: You want to reuse a DO-178B certified software module in a new DO-178C program.

**Approach**:
1. **Separate Certification**: Module can remain DO-178B certified
2. **Interface Verification**: Verify integration per DO-178C
3. **Credit**: Take credit for existing certification evidence
4. **Documentation**: PSAC explains reuse approach and existing certification basis

**Key Point**: Don't need to re-certify to new standard unless making significant changes.

### Scenario 3: New Design Using Obsolete Standard

**Situation**: New design, but team wants to use DO-178B because they have experience and tools.

**Approach**:
1. **Not Recommended**: Authorities expect current standards for new designs
2. **Authority Approval Required**: Must justify to EASA/FAA
3. **Likely Response**: "Use DO-178C for new designs"
4. **Transition**: Invest in training and tools for current standard

**Key Point**: Use current standards for new designs unless strong justification.

### Scenario 4: Historical Reference

**Situation**: Legacy document references DO-178A, need to understand what it meant.

**Approach**:
1. **Obtain Copy**: Find archived copy of DO-178A (SAE archives, libraries)
2. **Understand Context**: What was state-of-practice at that time?
3. **Map to Current**: How does DO-178A objective map to DO-178C?
4. **Document**: Capture understanding for future reference

### Scenario 5: PSS to ECSS Transition (Spacecraft)

**Situation**: Legacy spacecraft design used PSS standards, new mission uses ECSS.

**Approach**:
1. **Mapping**: ESA provides PSS-to-ECSS mapping documents
2. **Equivalency**: Most PSS requirements have ECSS equivalents
3. **Updates**: ECSS incorporates lessons learned from PSS era
4. **Fresh Start**: New designs should use ECSS, not PSS

**Reference**: ECSS website has PSS-to-ECSS mapping documents

## Equivalency and Mapping

### DO-178B to DO-178C

DO-178C is backward compatible with DO-178B, with additions:
- **Main Document**: ~95% same as DO-178B
- **Supplements**: DO-331 (model-based), DO-332 (OOP), DO-333 (formal methods)
- **Objectives**: Similar, some clarified or added
- **Tool Qualification**: DO-330 replaces DO-178B Section 12

**Transition Tips**:
- DO-178B evidence generally acceptable for DO-178C
- DO-178C has clarifications that improve understanding
- Supplements apply only if using those technologies

### ARP4754 to ARP4754A

ARP4754A is revision of ARP4754:
- **Structure**: Similar, improved organization
- **Clarifications**: Safety assessment process clarified
- **Integration**: Better integration with DO-178C, DO-254, DO-160
- **New Content**: Expanded guidance on complex systems

**Transition Tips**:
- ARP4754 programs can transition to ARP4754A
- Differences are evolutionary, not revolutionary
- ARP4754A is clearer and more complete

## Obtaining Obsolete Standards

### Sources
- **SAE**: Archives of older standards (may require special request)
- **RTCA/EUROCAE**: Older revisions available for purchase
- **Libraries**: University or technical libraries may have copies
- **Company Archives**: Your organization may have copies from past programs
- **ESA/NASA**: Some older standards available in archives

### Caution
- Obsolete standards are for reference only
- Do not use for new designs without justification
- Ensure team understands current standards

## Regulatory Guidance

### EASA
- **Certification Memoranda**: Guidance on transition between standards
- **Position**: Generally expect current standards for new type certificates
- **Grandfathering**: Existing certificates remain valid
- **Changes**: Major changes may trigger update to current standards

### FAA
- **Advisory Circulars**: Provide transition guidance (e.g., AC 20-115D for DO-178B/C)
- **Position**: Similar to EASA, prefer current standards for new designs
- **Delegation**: DERs may have authority to approve use of older standards for minor changes

### ESA
- **ECSS Adoption**: Phased out PSS in favor of ECSS
- **Legacy**: PSS-certified missions remain valid
- **New Missions**: Use ECSS

## Best Practices

1. **Use Current Standards**: For new designs, always use the current version of standards
2. **Document Basis**: Clearly document which standard version used and why
3. **Authority Agreement**: Get authority agreement early for any non-standard approaches
4. **Transition Planning**: Plan transition to new standards (training, tools, processes)
5. **Archives**: Maintain archives of older standards for reference
6. **Knowledge Transfer**: Capture knowledge from legacy programs before team disperses

## Common Questions

**Q: Can I use DO-178B for a new design?**
A: Not recommended. Authorities expect DO-178C for new designs. Requires strong justification and authority approval.

**Q: Do I need to upgrade existing DO-178B software to DO-178C?**
A: No, unless making major changes. Existing certification remains valid.

**Q: What if my supplier only knows DO-178B?**
A: They need to transition to DO-178C. DO-178C training widely available. Differences are manageable.

**Q: Is DO-178B more or less rigorous than DO-178C?**
A: Very similar rigor. DO-178C clarifies some areas and adds technology supplements, but core objectives are nearly identical.

**Q: Can I mix DO-178B and DO-178C in the same program?**
A: Yes, with authority agreement. Document approach clearly in PSAC. Typical: reuse DO-178B components, new development DO-178C.

---

**Maintenance**: Update this document when standards superseded or new transition guidance published.

**Contact**: Standards Manager for questions on obsolete standards.
