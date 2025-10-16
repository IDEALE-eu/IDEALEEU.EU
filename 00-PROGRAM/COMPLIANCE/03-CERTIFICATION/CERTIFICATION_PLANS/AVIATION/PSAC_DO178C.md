---
document_id: "PSAC-001"
title: "Plan for Software Aspects of Certification (PSAC)"
standard: "DO-178C"
version: "1.0"
status: "Draft"
owner: "Certification Manager"
date: "2025-10-16"
confidentiality: "Internal"
---

# Plan for Software Aspects of Certification (PSAC)

## 1. Purpose and Scope

### 1.1 Purpose
This Plan for Software Aspects of Certification (PSAC) defines the software development processes, standards, and methods to be used to satisfy DO-178C objectives for airborne software used in [Product Name] systems.

### 1.2 Scope
This plan applies to all airborne software developed for [Product Name], including:
- Flight control software
- Navigation and guidance software
- Mission management software
- Health monitoring software
- Communication and data link software

### 1.3 Software Level Assignment
Software components will be assigned Design Assurance Levels (DAL) based on system safety assessment per ARP4761:
- **Level A**: Catastrophic failure condition (most critical)
- **Level B**: Hazardous failure condition
- **Level C**: Major failure condition
- **Level D**: Minor failure condition
- **Level E**: No safety effect

## 2. Software Overview

### 2.1 System Description
[Description of the aircraft/spacecraft system and its mission]

### 2.2 Software Architecture
[High-level software architecture description]
- Operating system and platform
- Application software components
- Interfaces to hardware and other systems
- Software configuration items (SCI)

### 2.3 Software Development Environment
- Development platforms and tools
- Host and target hardware
- Compilers and code generators
- Tool qualification requirements (per Section 12)

## 3. Software Lifecycle

### 3.1 Software Planning Process
Activities:
- Software requirements standards definition
- Software design standards definition
- Software code standards definition
- Software integration process definition
- Software verification process definition
- Software configuration management process definition
- Software quality assurance process definition
- Certification liaison process definition

Outputs:
- Plan for Software Aspects of Certification (PSAC) - this document
- Software Development Plan (SDP)
- Software Verification Plan (SVP)
- Software Configuration Management Plan (SCMP)
- Software Quality Assurance Plan (SQAP)

### 3.2 Software Development Processes

#### 3.2.1 Requirements Process
Activities:
- High-level requirements development
- Derived requirements development
- Requirements validation
- Requirements traceability

Standards:
- Requirements shall be unambiguous, verifiable, and traceable
- Derived requirements shall be identified and justified
- Requirements shall be compatible with target hardware

Outputs:
- Software Requirements Specification (SRS)
- Software Requirements Data (SRD)
- Requirements traceability matrix

#### 3.2.2 Design Process
Activities:
- Software architecture development
- Low-level requirements development
- Design implementation
- Design verification

Standards:
- Design shall satisfy requirements
- Design shall be traceable to requirements
- Design shall be verifiable

Outputs:
- Software Design Description (SDD)
- Interface Control Documents (ICD)
- Design traceability matrix

#### 3.2.3 Coding Process
Activities:
- Source code development
- Code standards compliance
- Code review and analysis

Standards:
- Code shall satisfy design
- Code shall be traceable to design
- Coding standards per [Coding Standards Document]
- Comments and documentation requirements

Outputs:
- Source Code
- Code review records
- Code analysis reports

### 3.3 Software Verification Process

#### 3.3.1 Requirements-Based Testing
Objective: Verify software requirements implementation

Methods:
- Requirements-based test cases
- Normal range testing
- Robustness testing
- Equivalence partitioning

Coverage:
- 100% of high-level requirements (DAL A-D)
- 100% of low-level requirements (DAL A-C)

#### 3.3.2 Structural Coverage Analysis
Objective: Verify completeness of requirements-based testing

Coverage Requirements by DAL:
- **Level A**: Modified Condition/Decision Coverage (MC/DC)
- **Level B**: Decision Coverage (DC)
- **Level C**: Statement Coverage
- **Level D**: Statement Coverage (with other methods)
- **Level E**: No structural coverage required

Tools:
- Coverage analysis tool (requires qualification per Section 12)

#### 3.3.3 Software/Hardware Integration Testing
Objective: Verify software operation in target environment

Activities:
- Hardware/software interface testing
- Timing and performance verification
- Resource utilization verification
- Failure mode testing

Environment:
- Target hardware or representative simulator
- Integrated test bench
- Hardware-in-the-loop (HIL) testing

### 3.4 Software Configuration Management Process

#### 3.4.1 Configuration Identification
Activities:
- Baseline establishment
- Version identification
- Change identification

Outputs:
- Configuration index
- Software Life Cycle Environment Configuration Index (SECI)
- Problem reports and change requests

#### 3.4.2 Baseline and Traceability
Baselines:
- Software Requirements Baseline
- Software Design Baseline
- Source Code Baseline
- Executable Object Code Baseline

Traceability:
- Requirements to design
- Design to code
- Code to executable
- Requirements to tests

#### 3.4.3 Software Change Control
Process:
- Change request submission
- Impact analysis
- Change approval
- Implementation and verification
- Regression analysis

Tools:
- Configuration management tool
- Version control system
- Change tracking system

### 3.5 Software Quality Assurance Process

#### 3.5.1 Process Assurance
Activities:
- Process compliance verification
- Process improvement
- Standards compliance audits

Outputs:
- SQA records
- Process compliance reports
- Audit findings and corrective actions

#### 3.5.2 Product Assurance
Activities:
- Review of software development outputs
- Verification independence
- Problem report review

Outputs:
- Review records
- Verification results
- Conformity review records

#### 3.5.3 Conformity Review
Objective: Verify certification compliance

Reviews:
- Software Accomplishment Summary (SAS) review
- Compliance checklist review
- Evidence package review

### 3.6 Certification Liaison Process

#### 3.6.1 Authority Coordination
Activities:
- PSAC submittal and approval
- Periodic status reviews
- Finding resolution
- Final certification package submittal

Schedule:
- PSAC approval: Phase C exit
- Mid-project review: Phase D
- Compliance demonstration: Phase E
- Final audit: Phase F

#### 3.6.2 Means of Compliance
Methods:
- Requirements-based testing
- Structural coverage analysis
- Design and code reviews
- Analysis and simulation
- Process compliance audits

## 4. Software Life Cycle Data

### 4.1 Planning Data
- Plan for Software Aspects of Certification (PSAC)
- Software Development Plan (SDP)
- Software Verification Plan (SVP)
- Software Configuration Management Plan (SCMP)
- Software Quality Assurance Plan (SQAP)

### 4.2 Development Data
- Software Requirements Standards
- Software Design Standards
- Software Code Standards
- Software Requirements Data (SRD)
- Software Design Description (SDD)
- Source Code
- Executable Object Code

### 4.3 Verification Data
- Software Verification Cases and Procedures (SVCP)
- Software Verification Results (SVR)
- Software Life Cycle Environment Configuration Index (SECI)
- Problem Reports
- Software Configuration Index
- Software Process Assurance Records
- Software Accomplishment Summary (SAS)

### 4.4 Control Categories
Data classified as:
- **Control Category 1 (CC1)**: Affects airborne software without review
- **Control Category 2 (CC2)**: Affects airborne software but with review

Tool outputs that generate CC1 data must be qualified.

## 5. Tool Qualification

### 5.1 Tool Identification
Development and verification tools requiring qualification per DO-178C Section 12:

| Tool Name | Tool Type | Qualification Level | Rationale |
|-----------|-----------|---------------------|-----------|
| [Compiler] | Development | TQL-1 | Generates executable code |
| [Code Generator] | Development | TQL-1 | Auto-generates source code |
| [Coverage Analyzer] | Verification | TQL-2 | Determines test coverage |
| [Static Analyzer] | Verification | TQL-3 | Detects code anomalies |

### 5.2 Tool Qualification Process
For each tool requiring qualification:
1. Tool Assessment Report (TAR)
2. Tool Qualification Plan (TQP)
3. Tool Operational Requirements (TOR)
4. Tool Qualification Data (TQD)
5. Tool Qualification Summary (TQS)

Reference: [`../../TOOL_QUALIFICATION/`](../../TOOL_QUALIFICATION/)

## 6. Previously Developed Software (PDS)

### 6.1 Commercial Off-The-Shelf (COTS)
If COTS software is used:
- Service history review
- Operational environment compatibility
- Error reports and anomaly analysis
- Integration testing

### 6.2 Reused Software
For software reused from previous projects:
- Credit for previous compliance evidence
- Gap analysis for new requirements
- Regression testing
- Change impact analysis

## 7. Compliance Matrix

### 7.1 DO-178C Objectives
All objectives from DO-178C Tables A-1 through A-10 applicable to assigned software levels will be demonstrated.

Reference: [`../../COMPLIANCE_CHECKLISTS/DO_178C_CHECKLIST.csv`](../../COMPLIANCE_CHECKLISTS/)

### 7.2 Evidence References
Each objective will have:
- Compliance method (Test, Analysis, Review, Inspection)
- Evidence location
- Verification status
- Authority review status

Reference: [`../../06-EVIDENCE/EVIDENCE_INDEX.csv`](../../../06-EVIDENCE/)

## 8. Software Accomplishment Summary (SAS)

### 8.1 Purpose
The Software Accomplishment Summary provides evidence that:
- Software life cycle processes have been completed
- Software complies with requirements
- All DO-178C objectives have been satisfied

### 8.2 Content
The SAS will include:
- Software overview and configuration
- Compliance statement by objective
- Deviations and alternative means of compliance
- Tool qualification summary
- Problem report summary
- Software life cycle data index
- Schedule and status

### 8.3 Schedule
- Draft SAS: Phase E
- Final SAS: Phase F (certification submission)

## 9. Deviations and Alternative Means of Compliance

### 9.1 Process
If standard DO-178C guidance cannot be followed:
1. Document deviation rationale
2. Propose alternative means of compliance
3. Prepare Issue Paper for authority review
4. Obtain authority approval before implementation

Reference: [`../../AUTHORITY_CORRESPONDENCE/ISSUE_PAPERS/`](../../AUTHORITY_CORRESPONDENCE/ISSUE_PAPERS/)

### 9.2 Tracking
All deviations tracked in:
- PSAC (this document)
- Software Accomplishment Summary
- Compliance checklist

## 10. Software Safety Assessment

### 10.1 Safety Requirements
Software safety requirements derived from:
- System safety assessment (ARP4761)
- Functional Hazard Assessment (FHA)
- Fault Tree Analysis (FTA)
- Failure Modes and Effects Analysis (FMEA)

Reference: System Safety Assessment documents

### 10.2 Partitioning and Protection
For mixed-criticality systems:
- Spatial partitioning (memory protection)
- Temporal partitioning (time slicing)
- Interference protection mechanisms
- Partition testing and verification

## 11. Configuration Management

### 11.1 Software Configuration Items (SCI)
Each SCI includes:
- Unique identifier
- Version number
- Baseline designation
- Change history

### 11.2 Baselines
- Software Requirements Baseline: Phase C exit
- Software Design Baseline: Phase D mid-point
- Source Code Baseline: Phase D exit
- Executable Code Baseline: Phase E (for certification)

### 11.3 Release Process
Software releases for certification:
1. Baseline freeze
2. Regression testing
3. Configuration audit
4. Release authorization
5. Archive and retention

## 12. Schedule and Milestones

### 12.1 Key Milestones
| Milestone | Description | Phase | Target Date |
|-----------|-------------|-------|-------------|
| PSAC Approval | PSAC approved by authority | C | [Date] |
| Requirements Baseline | SRS complete and baselined | C | [Date] |
| Design Baseline | SDD complete and baselined | D | [Date] |
| Code Complete | All source code complete | D | [Date] |
| Verification Complete | All testing complete | E | [Date] |
| SAS Complete | Software Accomplishment Summary | E | [Date] |
| Certification Audit | Authority final audit | F | [Date] |
| Type Certificate | TC issued | F | [Date] |

### 12.2 Reviews with Authority
- PSAC Review: Phase C
- Mid-project Review: Phase D
- Compliance Demonstration: Phase E
- Final Certification Audit: Phase F

## 13. Roles and Responsibilities

### 13.1 Organizational Structure
- **Certification Manager**: Overall certification coordination
- **Software Manager**: Software development leadership
- **Quality Assurance Manager**: Process compliance oversight
- **Configuration Manager**: Baseline and change control
- **Verification Lead**: Test and analysis coordination

### 13.2 Independence Requirements
- Software quality assurance: Independent from development
- Software verification: Independent from development (DAL A-B)
- Authority liaison: Independent reporting

## 14. Standards and References

### 14.1 Applicable Documents
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- DO-330: Software Tool Qualification Considerations
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems
- ARP4761: Guidelines and Methods for Conducting the Safety Assessment Process

### 14.2 Project Standards
- Software Requirements Standards: [Document reference]
- Software Design Standards: [Document reference]
- Software Code Standards: [Document reference]
- Software Test Standards: [Document reference]

## 15. Document Control

### 15.1 Revisions
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-16 | [Name] | Initial draft |

### 15.2 Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Certification Manager | [Name] | | |
| Software Manager | [Name] | | |
| Quality Assurance Manager | [Name] | | |
| Chief Engineer | [Name] | | |

### 15.3 Authority Approval
| Authority | Representative | Date | Reference |
|-----------|---------------|------|-----------|
| EASA | [Name] | | [Docket #] |
| FAA | [Name] | | [Docket #] |

---

**Document Location**: `00-PROGRAM/COMPLIANCE/03-CERTIFICATION/CERTIFICATION_PLANS/AVIATION/PSAC_DO178C.md`  
**Next Review**: Phase C exit or as required for changes  
**Related Documents**: PHAC, SDP, SVP, SCMP, SQAP, SAS
