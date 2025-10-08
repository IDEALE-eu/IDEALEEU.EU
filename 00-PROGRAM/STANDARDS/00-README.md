# STANDARDS

Comprehensive standards repository for aerospace program compliance, covering aircraft and spacecraft development, certification, and operations.

## Overview

This directory maintains the standards baseline for the IDEALEEU.EU program, including:
- Industry standards tracking and compliance
- Regulatory requirements mapping
- Standards interpretation and guidance
- Compliance matrices and checklists
- Authority position papers and regulatory guidance

## Contents

- **00-README.md** - This file
- **01-REGISTER/** - Standards register, deviations, and waivers tracking
- **02-AIRCRAFT/** - Aircraft-specific standards (ARP4754A, DO-178C, DO-254, DO-160, etc.)
- **03-SPACECRAFT/** - Spacecraft standards (ECSS series)
- **04-CROSS_CUTTING/** - Standards applicable to both domains (MBSE, safety, manufacturing)
- **05-MAPPINGS/** - Standards-to-requirements mappings, compliance matrices, checklists
- **06-INTERPRETATIONS/** - FAQs, authority guidance, obsolete references
- **07-LINKS/** - Official sources, training materials, access information

## Purpose

The STANDARDS directory serves as the single source of truth for:
1. **Compliance Baseline** - Which standards apply to which systems and why
2. **Traceability** - Links between standards, requirements, processes, and verification
3. **Configuration Control** - Version management and change tracking
4. **Certification Evidence** - Documentation required for type certification and airworthiness
5. **Knowledge Management** - Interpretations, lessons learned, and best practices

## Key Standards by Domain

### Aircraft
- **Systems Engineering**: ARP4754A (development), ARP4761 (safety assessment)
- **Software**: DO-178C (software), DO-330 (tool qualification), DO-331/332/333 (model-based development)
- **Hardware**: DO-254 (complex electronic hardware)
- **Environmental**: DO-160 (environmental conditions and test procedures)
- **Cybersecurity**: DO-326A/355/356A, EU ACSC, NIST SP 800-171, ISO/SAE 21434
- **Regulatory**: EASA CS-23/25, FAA 14 CFR Parts 21/23/25/33/35

### Spacecraft
- **Systems Engineering**: ECSS-E-ST-10 series
- **Software**: ECSS-E-ST-40, ECSS-Q-ST-80
- **Hardware/Quality**: ECSS-Q-ST-70, -60, -40
- **Structures**: ECSS-E-ST-31, -32
- **Electrical/EMC**: ECSS-E-ST-20
- **Radiation**: ECSS-Q-ST-60, -30
- **AIT/GSE**: ECSS-E-ST-10-06, ECSS-E-HB-10-2A

### Cross-Cutting
- **MBSE**: ISO/IEC/IEEE 15288, 42010, SysML v2
- **Safety**: IEC 61508, ISO 26262
- **Manufacturing**: ISO 14644, ISO 17025, AS9100
- **Data Exchange**: ISO 10303 (STEP AP242), ReqIF, OSLC, QIF

## Standards Lifecycle

```
Identify → Register → Procure → Implement → Verify → Maintain → Retire
    ↓         ↓          ↓          ↓          ↓         ↓        ↓
  Need    Approval   License    Training   Audit    Update   Archive
```

## Usage Guidelines

1. **Before Starting Design** - Review applicable standards in 02-AIRCRAFT or 03-SPACECRAFT
2. **During Development** - Use compliance matrices from 05-MAPPINGS/COMPLIANCE_MATRIX_TEMPLATES
3. **At Stage Gates** - Complete checklists from 05-MAPPINGS/CHECKLISTS (PDR, CDR, PRR)
4. **For Certification** - Reference 01-REGISTER for compliance evidence
5. **When Questions Arise** - Check 06-INTERPRETATIONS/FAQ.md and authority papers

## Standards Management Process

1. **Identification** - Engineering identifies applicable standard
2. **Registration** - Added to 01-REGISTER/STANDARDS_REGISTER.csv
3. **Procurement** - Obtained through official sources (07-LINKS/OFFICIAL_SOURCES.md)
4. **Implementation** - Mapped to requirements and processes (05-MAPPINGS/)
5. **Verification** - Compliance verified through checklists and audits
6. **Maintenance** - Monitored for updates, supersessions, and revisions

## Deviations and Waivers

Non-conformances to standards must be:
- Documented in 01-REGISTER/DEVIATIONS_WAIVERS.csv
- Justified with safety impact assessment
- Approved by appropriate authority
- Notified to certification authorities when required

## Integration with Program Processes

- **Requirements Management** - Standards flow down to system requirements
- **Design Reviews** - Standards compliance verified at PDR, CDR
- **Verification & Validation** - Test cases trace to standards requirements
- **Configuration Management** - Standards versions baselined per release
- **Quality Assurance** - Standards compliance audited regularly

## Contacts

- **Standards Manager** - Maintains register and coordinates compliance
- **Certification Lead** - Interfaces with EASA, FAA, ESA authorities
- **Domain Leads** - Ensure standards applied correctly in their areas
- **Quality Assurance** - Audits compliance and tracks findings

## References

- See 07-LINKS/OFFICIAL_SOURCES.md for standards bodies and purchase information
- See 06-INTERPRETATIONS/ for guidance on specific standards topics
- See program-level documentation in 00-PROGRAM/ for overall governance

---

**Note**: This directory is configuration-controlled. Changes to standards baseline require approval per the program's configuration management process (00-PROGRAM/CONFIG_MGMT/).
