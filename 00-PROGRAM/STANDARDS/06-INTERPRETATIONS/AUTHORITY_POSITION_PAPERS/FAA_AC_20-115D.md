# FAA AC 20-115D - Airborne Software Development Assurance

**EXAMPLE DOCUMENT - For reference format only. Obtain official document from FAA.**

## Advisory Circular - Airborne Software Development Assurance

**Document**: AC 20-115D  
**Date**: 2023  
**Authority**: FAA (Federal Aviation Administration)  
**Status**: Current

## Purpose

This Advisory Circular (AC) provides guidance on using RTCA DO-178C "Software Considerations in Airborne Systems and Equipment Certification" for showing compliance with 14 CFR Part 25, Section 25.1309 and other applicable regulations.

## Scope

Applicable to:
- Type Certificate (TC) applicants
- Supplemental Type Certificate (STC) applicants
- Software-intensive systems on transport category aircraft
- Part 21 Design Organization Approvals (DOA)

## Key Guidance

### 1. DO-178C Acceptance

- **FAA Position**: DO-178C is acceptable means of compliance for airborne software
- **Applicability**: Software Levels A through D (Level E not subject to DO-178C)
- **Supplements**: DO-331 (model-based), DO-332 (OOP), DO-333 (formal methods) also acceptable

### 2. Software Level Assignment

Software level determined by failure condition severity:
- **Level A**: Catastrophic failure condition
- **Level B**: Hazardous/Severe-Major failure condition
- **Level C**: Major failure condition
- **Level D**: Minor failure condition
- **Level E**: No safety effect

Assigned through system safety assessment per ARP4761.

### 3. Plan for Software Aspects of Certification (PSAC)

- **Submittal**: PSAC to FAA early (Phase B/C, before CDR)
- **Content**: Software development plan, verification plan, configuration management plan, quality assurance plan, certification liaison process
- **Approval**: FAA Aircraft Certification Office (ACO) reviews and approves PSAC
- **Updates**: PSAC updated if significant changes to approach

### 4. Software Accomplishment Summary (SAS)

- **Submittal**: After software development complete
- **Content**: Summary of compliance with DO-178C objectives, reference to lifecycle data
- **Review**: FAA reviews SAS and supporting data
- **Approval**: FAA approval required before software can be installed on type-certificated aircraft

### 5. DO-178B to DO-178C Transition

**Existing Software (DO-178B certified)**:
- Can remain under DO-178B (grandfathering)
- Minor changes can continue under DO-178B with justification
- Major changes may require transition to DO-178C (FAA decision)

**New Software**:
- Should use DO-178C for new type certificates
- DO-178B may be acceptable for minor STCs with justification

**Reuse**:
- DO-178B certified software can be reused in DO-178C program
- Interface verified per DO-178C, but module remains DO-178B
- Credit taken for existing certification evidence

### 6. Tool Qualification (DO-330)

**Tools Requiring Qualification**:
- Tools that eliminate, reduce, or automate verification activities
- Based on Tool Qualification Level (TQL 1-5)
- TQL determined by tool function and software level

**FAA Expectations**:
- Tool qualification data submitted with software data
- Alternatively, tool qualification data approved separately

### 7. Previously Developed Software (PDS)

- **Definition**: Software from prior project, COTS, open source
- **Approach**: Assess PDS against DO-178C objectives
- **Credit**: Take credit for existing evidence where available
- **Gaps**: Identify gaps and generate additional evidence

### 8. Software Configuration Index (SCI)

- **Purpose**: Identify all software lifecycle data
- **Content**: Documents, plans, standards, code, test cases, etc.
- **Submittal**: SCI provided to FAA with SAS
- **Format**: Typically a list or database of configuration items

### 9. Independence

DO-178C requires independence for certain activities (review, verification):
- **Level A**: Most independence required
- **Level B**: Moderate independence
- **Level C**: Limited independence
- **Level D**: Minimal independence

FAA expects independence requirements met and documented.

### 10. Deviations and Alternative Methods

If proposing deviations from DO-178C or alternative methods:
- Document in PSAC
- Provide justification
- Obtain FAA approval before implementation
- Show equivalent level of safety

## Certification Process

1. **Pre-Application**: Discuss software approach with FAA
2. **PSAC Submittal**: Submit PSAC for FAA review
3. **Software Development**: Develop software per approved PSAC
4. **SAS Submittal**: Submit SAS and supporting data
5. **FAA Review**: FAA reviews data, may conduct audits
6. **Approval**: FAA approves software for installation
7. **Type Certificate**: Software approved as part of TC/STC

## FAA Involvement

- **ACO (Aircraft Certification Office)**: Primary FAA contact
- **DER (Designated Engineering Representative)**: May review on behalf of FAA
- **Audits**: FAA or DER may audit software development process
- **Testing**: FAA may witness software testing

## References

- **FAA Website**: https://www.faa.gov/
- **Official AC 20-115D**: Download from https://www.faa.gov/regulations_policies/advisory_circulars/
- **DO-178C**: Available from RTCA/EUROCAE
- **Related ACs**: AC 20-152 (DO-254), AC 20-170 (Integrated Modular Avionics)

---

**Note**: This is an **example format**. For actual compliance, obtain the official FAA AC 20-115D from https://www.faa.gov/regulations_policies/advisory_circulars/
