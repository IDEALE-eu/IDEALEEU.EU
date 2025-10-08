# 06-INTERPRETATIONS

Standards interpretations, FAQs, authority position papers, and obsolete references.

## Overview

This directory provides guidance on interpreting and applying standards, including frequently asked questions, authority position papers, and handling of obsolete standards.

## Contents

- **00-README.md** - This file
- **FAQ.md** - Frequently asked questions about standards application
- **OBSOLETE_REFERENCES.md** - How to handle legacy/obsolete standards
- **AUTHORITY_POSITION_PAPERS/** - Certification authority guidance documents

## Purpose

Standards can be complex and subject to interpretation. This directory provides:
1. **Clarification**: Answers to common questions
2. **Authority Guidance**: Official interpretations from EASA, FAA, ESA
3. **Best Practices**: Lessons learned from previous programs
4. **Legacy Handling**: How to deal with obsolete standards
5. **Common Pitfalls**: Mistakes to avoid

## FAQ.md

Frequently Asked Questions covering:
- General standards questions
- Aircraft-specific (ARP4754A, DO-178C, DO-254, DO-160)
- Spacecraft-specific (ECSS)
- Cross-cutting (MBSE, data exchange, configuration management)
- Certification and compliance

## AUTHORITY_POSITION_PAPERS/

Official guidance from certification authorities:
- **EASA**: Special Bulletins (SIB), Certification Memoranda (CM)
- **FAA**: Advisory Circulars (AC), Policy Statements
- **ESA**: Technical Notes (TN), Handbooks

### Example Papers Included
- **EASA_SIB_2020-08.md** - Cybersecurity considerations
- **FAA_AC_20-115D.md** - Airborne software guidance (DO-178C)
- **ESA_GEN_1234.md** - Production assurance expectations

## OBSOLETE_REFERENCES.md

Guidance for handling obsolete standards:
- DO-178B (replaced by DO-178C)
- MIL-STD-1553 (still in use, but not for new designs typically)
- PSS standards (replaced by ECSS)
- How to transition from old to new standards
- Grandfathering and equivalency

## Usage

### For Engineers
- Check FAQ before asking standards questions
- Review authority papers relevant to your design
- Consult when applying a standard to a novel situation

### For Certification
- Reference authority papers in compliance arguments
- Ensure interpretations align with authority expectations
- Document deviations from standard interpretation

### For Quality/Audits
- Use FAQs to train team on standards
- Reference authority papers during audits
- Ensure consistent interpretation across program

## Maintenance

- **Owner**: Standards Manager and Certification Lead
- **Updates**: When new authority papers published or new FAQs identified
- **Review**: Annually or when standards updated
- **Version Control**: Documents stored in PLM/PDM

## Contributing

If you have a standards question:
1. Check FAQ first
2. If not answered, consult Standards Manager
3. If useful to others, add to FAQ (via CCB approval)

If you find authority guidance:
1. Submit to Standards Manager
2. Standards Manager reviews and adds to AUTHORITY_POSITION_PAPERS/
3. Notify relevant teams of new guidance

## Integration with Other Directories

- **01-REGISTER/**: Standards being interpreted
- **02-AIRCRAFT/, 03-SPACECRAFT/**: Domain-specific interpretations
- **05-MAPPINGS/**: Interpretations affect compliance approach

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
