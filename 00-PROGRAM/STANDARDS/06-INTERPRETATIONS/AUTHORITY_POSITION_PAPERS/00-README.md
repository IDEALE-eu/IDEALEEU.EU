# AUTHORITY_POSITION_PAPERS

Certification authority guidance documents and position papers.

## Overview

This directory contains guidance documents from certification authorities (EASA, FAA, ESA) that provide official interpretations and positions on standards application.

## Contents

- **00-README.md** - This file
- **EASA_SIB_2020-08.md** - EASA Safety Information Bulletin on Cybersecurity
- **FAA_AC_20-115D.md** - FAA Advisory Circular on Airborne Software (DO-178C guidance)
- **ESA_GEN_1234.md** - ESA Production Assurance Expectations (example)

## Types of Authority Documents

### EASA (European Union Aviation Safety Agency)

- **Certification Memoranda (CM)**: Technical guidance for certification
  - Example: CM-SWCEH-001 (Software and Complex Electronic Hardware)
- **Safety Information Bulletins (SIB)**: Safety-related guidance
  - Example: SIB 2020-08 (Cybersecurity)
- **Acceptable Means of Compliance (AMC)**: Methods to show compliance with regulations
- **Guidance Material (GM)**: Additional explanatory material

**Where to Find**: https://www.easa.europa.eu/

### FAA (Federal Aviation Administration)

- **Advisory Circulars (AC)**: Non-regulatory guidance
  - Example: AC 20-115D (Airborne Software)
  - Example: AC 20-152 (RTCA DO-254 recognition)
- **Policy Statements**: Official FAA positions
- **Orders**: Internal FAA guidance (sometimes made public)

**Where to Find**: https://www.faa.gov/regulations_policies/advisory_circulars/

### ESA (European Space Agency)

- **Technical Notes (TN)**: Technical guidance on ECSS application
- **Handbooks (HB)**: Detailed guidance documents (e.g., ECSS-E-HB series)
- **General Requirements**: ESA-specific requirements for missions

**Where to Find**: https://www.esa.int/ and ECSS Portal https://ecss.nl/

## Purpose of Position Papers

1. **Clarification**: Explain how to interpret and apply standards
2. **Compliance Methods**: Provide acceptable ways to demonstrate compliance
3. **Lessons Learned**: Incorporate findings from incidents and audits
4. **Policy**: State authority position on new or emerging topics
5. **Consistency**: Ensure consistent interpretation across programs

## How to Use Position Papers

### During Design
- Review applicable position papers for your domain
- Understand authority expectations
- Design to meet both standard and authority guidance
- Reference position papers in design documentation

### During Certification
- Cite position papers in compliance arguments
- Show how design aligns with authority guidance
- Discuss any deviations with authority early
- Include position papers in certification data package

### During Audits
- Have position papers available for auditors
- Demonstrate awareness of authority positions
- Show how guidance was implemented
- Explain any differences from guidance

## Key Position Papers by Topic

### Software (Aircraft)

| Document | Title | Key Points |
|----------|-------|------------|
| FAA AC 20-115D | Airborne Software | DO-178C guidance, DO-178B transition, tool qualification |
| EASA CM-SWCEH-001 | Software and Complex Electronic Hardware | Combined SW/HW guidance |

### Hardware (Aircraft)

| Document | Title | Key Points |
|----------|-------|------------|
| FAA AC 20-152 | RTCA DO-254 Recognition | DO-254 acceptable to FAA |
| EASA CM-SWCEH-001 | Software and Complex Electronic Hardware | Combined SW/HW guidance |

### Cybersecurity (Aircraft)

| Document | Title | Key Points |
|----------|-------|------------|
| EASA SIB 2020-08 | Cybersecurity | DO-326A/355/356A, risk assessment, connected aircraft |
| FAA PS-AIR-21.16-03 | Security Considerations | Aircraft security design considerations |

### Human Factors (Aircraft)

| Document | Title | Key Points |
|----------|-------|------------|
| FAA AC 25.1302-1 | Flight Deck Design | Compliance methods for 25.1302, information management |
| FAA AC 25.11 | Electronic Flight Displays | Display design guidance |

### Spacecraft (ESA/NASA)

| Document | Title | Key Points |
|----------|-------|------------|
| ECSS-E-HB-10-02A | Verification Guidelines | Detailed V&V guidance |
| ECSS-Q-HB-70-01A | Materials and Processes | Material selection guidance |
| NASA-HDBK-4002A | Mitigating In-Space Charging | ESD and charging protection |

## Maintenance

- **Review**: Quarterly check for new position papers
- **Update**: When new papers published, add to directory
- **Notification**: Inform program teams of new guidance
- **Archive**: Keep older versions for reference

## Requesting Clarification

If position paper does not address your specific situation:
1. Document your specific question
2. Consult with Certification Lead
3. Certification Lead requests clarification from authority
4. Response documented and shared with team
5. Consider whether response should be added to FAQ.md

## Example Papers in This Directory

The example papers included (EASA_SIB_2020-08, FAA_AC_20-115D, ESA_GEN_1234) are **templates/examples** showing the format and content typically found. For actual compliance, always obtain and reference the official documents from the authorities.

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/

**Contact**: Certification Lead for questions on authority position papers.
