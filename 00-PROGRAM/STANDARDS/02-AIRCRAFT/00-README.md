# 02-AIRCRAFT

Aircraft certification and airworthiness standards.

## Overview

This directory contains all standards applicable to aircraft development, certification, and continued airworthiness. These standards are primarily issued by SAE, RTCA, EUROCAE, EASA, and FAA, and are mandatory for type certification and airworthiness approval.

## Contents

- **00-README.md** - This file
- **SYSTEMS_ENGINEERING/** - ARP4754A (development), ARP4761 (safety assessment)
- **SOFTWARE/** - DO-178C, DO-330, DO-331/332/333 (software and model-based development)
- **HARDWARE/** - DO-254 (complex electronic hardware design assurance)
- **ENVIRONMENTAL_TEST/** - DO-160 (environmental conditions and test procedures)
- **IMA/** - DO-297 (Integrated Modular Avionics development and integration)
- **CYBERSECURITY/** - DO-326A/355/356A, EU ACSC, NIST SP 800-171, ISO/SAE 21434
- **AVIONICS_INTERFACES/** - ARINC 429/629/653/661/664 (avionics data buses and interfaces)
- **HUMAN_FACTORS/** - CS-25 Annex II, FAA AC 25.1302-1 (flight deck design)
- **REGULATORY/** - EASA CS-23/25, FAA 14 CFR Parts 21/23/25/33/35

## Certification Framework

Aircraft certification follows a structured process:

```
Type Certificate Application
    ↓
Certification Basis Establishment (CS-25, Part 25)
    ↓
Certification Plan Approval (PSCP, SCP)
    ↓
Development per ARP4754A/DO-178C/DO-254
    ↓
Compliance Demonstration
    ↓
Type Certificate Issued
```

## Key Standards Overview

### Systems Engineering (ARP4754A, ARP4761)
- **ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
  - System development lifecycle
  - Requirements management
  - V&V activities
  - Configuration management
  - Process assurance

- **ARP4761** - Guidelines and Methods for Conducting the Safety Assessment Process
  - FHA (Functional Hazard Assessment)
  - PSSA (Preliminary System Safety Assessment)
  - SSA (System Safety Assessment)
  - CCA (Common Cause Analysis)
  - FTA/FMEA methodologies

### Software (DO-178C)
- Development assurance levels: DAL A (catastrophic) through DAL E (no safety effect)
- Objectives scaled by DAL
- Requirements, design, code, test artifacts
- Configuration management, quality assurance, certification liaison
- Tool qualification per DO-330

### Hardware (DO-254)
- Complex electronic hardware (FPGA, ASIC, PLD)
- Design assurance levels A through E
- Requirements capture, conceptual design, detailed design
- Verification: analysis, test, review
- Configuration management and process assurance

### Environmental Testing (DO-160)
- Temperature, altitude, humidity
- Vibration, shock, acoustic noise
- EMI/EMC (conducted and radiated)
- Power quality, lightning, HIRF
- Category definitions by installation location

### Cybersecurity (DO-326A, DO-355, DO-356A)
- Airworthiness Security Process (ASRP)
- Security risk assessment
- Security development and verification
- Integration with ARP4754A/DO-178C/DO-254

## Applicability

These standards apply to:
- New type certification (TC)
- Supplemental type certification (STC)
- Major changes and modifications
- Continued airworthiness and service bulletins

## Development Assurance Levels (DAL)

| DAL | Failure Condition      | Probability         |
|-----|------------------------|---------------------|
| A   | Catastrophic          | < 10⁻⁹ per FH       |
| B   | Hazardous             | < 10⁻⁷ per FH       |
| C   | Major                 | < 10⁻⁵ per FH       |
| D   | Minor                 | < 10⁻³ per FH       |
| E   | No Safety Effect      | No probability req  |

## Integration with Program

- **Requirements** - Flow down from system to subsystem per ARP4754A
- **Design Reviews** - PDR/CDR verify compliance with applicable standards
- **Verification** - Test procedures per DO-160, verification per DO-178C/DO-254
- **Certification** - Evidence packages per EASA/FAA guidance
- **Production** - Continued compliance per AS9100, Part 21 Production Organization Approval

## Regulatory Authorities

- **EASA** - European Union Aviation Safety Agency
- **FAA** - Federal Aviation Administration (United States)
- **Transport Canada** - Canadian aviation authority
- **Others** - Bilateral agreements for mutual recognition

## Key Guidance Documents

- **FAA AC 20-115D** - Airborne Software guidance
- **FAA AC 20-152** - RTCA DO-254 recognition
- **EASA CM-SWCEH-001** - Complex electronic hardware certification
- **EASA SIB 2020-08** - Cybersecurity considerations

## References

- See 01-REGISTER/STANDARDS_REGISTER.csv for specific versions in use
- See 05-MAPPINGS/ for compliance matrices and requirement traceability
- See 06-INTERPRETATIONS/ for FAQs and authority position papers
- See 07-LINKS/ for official sources and training materials

---

**Note**: Compliance with these standards is mandatory for certification. Any deviations must be approved per 01-REGISTER/DEVIATIONS_WAIVERS.csv process.
