# STANDARD_TO_PROCESS

Mapping of standards to internal procedures and processes.

## Aircraft Standards

### Systems Engineering

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ARP4754A | Overall | PRO-002 Systems Engineering Process | Master process document |
| ARP4754A | Section 5.1 (Planning) | PRO-002-01 Systems Engineering Plan | Planning templates |
| ARP4754A | Section 5.2 (Requirements) | PRO-002-02 Requirements Management | Requirements capture and management |
| ARP4754A | Section 5.3 (Design) | PRO-002-03 Architecture Development | Architecture definition |
| ARP4761 | Overall | PRO-003 Safety Assessment Process | Safety analysis process |
| ARP4761 | FHA | PRO-003-01 Functional Hazard Assessment | FHA procedure |
| ARP4761 | PSSA/SSA | PRO-003-02 System Safety Assessment | SSA procedure |

### Software

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| DO-178C | Overall | PRO-012 Software Development Process | Software lifecycle |
| DO-178C | Section 4 (Planning) | PRO-012-01 Software Planning | PSAC, plans |
| DO-178C | Section 5 (Development) | PRO-012-02 Software Development | Requirements, design, code |
| DO-178C | Section 6 (Verification) | PRO-012-03 Software Verification | Reviews, analysis, test |
| DO-178C | Section 7 (CM) | PRO-001 Configuration Management | Software CM |
| DO-178C | Section 8 (QA) | PRO-012-04 Software Quality Assurance | SQAP, audits |
| DO-330 | Overall | PRO-012-05 Tool Qualification | Tool qualification process |

### Hardware

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| DO-254 | Overall | PRO-015 Hardware Design Assurance | Hardware lifecycle |
| DO-254 | Section 4 (Planning) | PRO-015-01 Hardware Planning | PHAC, plans |
| DO-254 | Section 5 (Design) | PRO-015-02 Hardware Design | Requirements, conceptual, detailed |
| DO-254 | Section 6 (Verification) | PRO-015-03 Hardware Verification | Reviews, analysis, test |

### Environmental Test

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| DO-160 | Overall | PRO-020 Environmental Testing | DO-160 test execution |
| DO-160 | Section 8 (Vibration) | PRO-020-01 Vibration Testing | Vibration procedures |
| DO-160 | Section 16 (Power Input) | PRO-020-02 Power Quality Testing | Power testing |
| DO-160 | Section 20/21 (EMC) | PRO-020-03 EMC Testing | EMC procedures |

### Regulatory

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| CS-25 / Part 25 | Overall | PRO-030 Certification Management | Certification process |
| CS-25 / Part 25 | Compliance | PRO-030-01 Compliance Demonstration | Showing compliance |
| Part 21 | Production | PRO-031 Production Quality System | Part 21 POA |

## Spacecraft Standards

### Systems Engineering

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ECSS-E-ST-10C | Overall | PRO-102 Space Systems Engineering | Master SE process |
| ECSS-E-ST-10-02C | Verification | PRO-103 Verification and Validation | V&V process |
| ECSS-E-ST-10-03C | Testing | PRO-104 Testing Process | Test planning and execution |

### Software

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ECSS-E-ST-40C | Overall | PRO-112 Space Software Engineering | Software development |
| ECSS-Q-ST-80C | Product Assurance | PRO-112-01 Software Product Assurance | Software PA |

### Hardware and Quality

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ECSS-Q-ST-70C | Materials | PRO-115 Materials and Processes | Material selection, qualification |
| ECSS-Q-ST-60C | EEE Components | PRO-116 EEE Component Management | Parts selection, screening |
| ECSS-Q-ST-20C | Quality Assurance | PRO-100 Quality Management System | Overall QMS |

### AIT

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ECSS-E-ST-10-06C | AIT | PRO-120 Assembly, Integration, Test | AIT process |
| ISO 14644 | Cleanroom | PRO-121 Cleanroom Operations | Cleanroom procedures |

## Cross-Cutting Standards

### MBSE

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ISO/IEC/IEEE 15288 | Systems Engineering | PRO-002 / PRO-102 | SE processes |
| ISO/IEC/IEEE 42010 | Architecture | PRO-002-03 / PRO-102 | Architecture definition |
| SysML v2 | Modeling | PRO-200 Model-Based Engineering | MBSE approach |

### Data Exchange

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ISO 10303 AP242 | STEP | PRO-201 CAD Data Exchange | STEP file procedures |
| ReqIF | Requirements | PRO-202 Requirements Exchange | ReqIF procedures |

### Configuration Management

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| ISO 10007 | Overall | PRO-001 Configuration Management | CM process |
| EIA-649C | Overall | PRO-001 Configuration Management | CM process (alternative) |

### Safety and Security

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| IEC 61508 | Functional Safety | PRO-210 Ground System Safety | Safety for ground systems |
| ISO/IEC 27001 | Information Security | PRO-211 Information Security | ISMS |
| NIST SP 800-171 | CUI Protection | PRO-212 Data Protection | Protecting design/cert data |

### Manufacturing

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| AS9100D | Quality Management | PRO-100 Quality Management System | Overall QMS |
| ISO 14644 | Cleanrooms | PRO-121 Cleanroom Operations | Cleanroom management |
| ISO/IEC 17025 | Lab Accreditation | PRO-122 Laboratory Quality System | Test lab procedures |

### Environment and Materials

| Standard | Clause/Topic | Internal Process/Procedure | Notes |
|----------|--------------|---------------------------|-------|
| REACH | Chemicals | PRO-220 REACH Compliance | SVHC tracking |
| RoHS | Restricted Substances | PRO-221 RoHS Compliance | RoHS tracking (if applicable) |
| ISO 14001 | Environmental Management | PRO-222 Environmental Management | EMS |

## Usage

This mapping helps:
1. **New Team Members**: Understand where to find implementation of standards
2. **Auditors**: See how standards are implemented in procedures
3. **Process Updates**: When standards change, identify procedures to update
4. **Training**: Train on procedures that implement standards
5. **Gap Analysis**: Identify standards not yet implemented

## Maintenance

- **Owner**: Standards Manager
- **Review Frequency**: Annually or when standards/procedures change
- **Update Process**: Via Configuration Control Board (CCB)
- **Version Control**: Stored in PLM/PDM system

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
