---
document_id: "PHAC-001"
title: "Plan for Hardware Aspects of Certification (PHAC)"
standard: "DO-254"
version: "1.0"
status: "Draft"
owner: "Certification Manager"
date: "2025-10-16"
confidentiality: "Internal"
---

# Plan for Hardware Aspects of Certification (PHAC)

## 1. Purpose and Scope

### 1.1 Purpose
This Plan for Hardware Aspects of Certification (PHAC) defines the hardware development processes, standards, and methods to be used to satisfy DO-254 objectives for airborne electronic hardware used in [Product Name] systems.

### 1.2 Scope
This plan applies to all airborne electronic hardware developed for [Product Name], including:
- Flight control computers and electronics
- Navigation and guidance hardware
- Communication hardware
- Power management electronics
- Sensor interfaces and signal conditioning
- Custom integrated circuits (ASIC/FPGA)

### 1.3 Hardware Design Assurance Level Assignment
Hardware components will be assigned Design Assurance Levels (DAL) based on system safety assessment per ARP4761:
- **Level A**: Catastrophic failure condition (most critical)
- **Level B**: Hazardous failure condition
- **Level C**: Major failure condition
- **Level D**: Minor failure condition
- **Level E**: No safety effect

## 2. Hardware Overview

### 2.1 System Description
[Description of the aircraft/spacecraft system and its mission]

### 2.2 Hardware Architecture
[High-level hardware architecture description]
- Processing units and controllers
- Memory and storage devices
- Input/output interfaces
- Power supplies and distribution
- Communication buses and interfaces
- Custom logic devices (FPGA, ASIC, PLD)

### 2.3 Hardware Development Environment
- Design tools (schematic capture, HDL editors)
- Simulation and analysis tools
- Synthesis and place-and-route tools
- Verification tools
- Tool qualification requirements (per Section 11)

## 3. Hardware Lifecycle

### 3.1 Hardware Planning Process
Activities:
- Hardware requirements standards definition
- Hardware design standards definition
- Hardware validation and verification standards definition
- Hardware configuration management process definition
- Hardware quality assurance process definition
- Hardware tool qualification planning
- Certification liaison process definition

Outputs:
- Plan for Hardware Aspects of Certification (PHAC) - this document
- Hardware Development Plan (HDP)
- Hardware Verification Plan (HVP)
- Hardware Configuration Management Plan (HCMP)
- Hardware Quality Assurance Plan (HQAP)

### 3.2 Hardware Design Processes

#### 3.2.1 Requirements Capture Process
Activities:
- Derived hardware requirements development
- Requirements allocation to hardware items
- Requirements validation
- Requirements traceability

Standards:
- Requirements shall be unambiguous, complete, and verifiable
- Derived requirements shall be identified and justified
- Requirements shall consider environmental conditions
- Requirements shall include failure condition effects

Outputs:
- Hardware Requirements Document (HRD)
- Hardware Requirements Data (HRD)
- Requirements traceability matrix

#### 3.2.2 Conceptual Design Process
Activities:
- Hardware architecture development
- Technology selection
- Preliminary component selection
- Design trade studies
- Design partitioning

Standards:
- Architecture shall satisfy requirements
- Design shall be analyzable for safety
- Partitioning strategy for mixed-criticality
- Interface definitions

Outputs:
- Hardware Design Description (HDD)
- Architecture diagrams
- Interface Control Documents (ICD)
- Design trade study reports

#### 3.2.3 Detailed Design Process
Activities:
- Schematic design development
- Component selection and qualification
- Circuit design and analysis
- PCB layout design
- HDL design (for FPGA/ASIC)
- Design verification

Standards:
- Design shall satisfy requirements
- Design shall be traceable to requirements
- Design shall minimize complexity
- Testability considerations
- Derating and margin analysis

Outputs:
- Detailed schematics
- Bill of Materials (BOM)
- PCB layout files
- HDL source code (VHDL/Verilog)
- Component qualification data
- Design analysis reports

#### 3.2.4 Implementation Process
Activities:
- PCB fabrication and assembly
- FPGA/ASIC synthesis and implementation
- Hardware assembly and integration
- Hardware configuration control

Standards:
- Implementation shall match design
- Manufacturing process controls
- Workmanship standards
- Assembly documentation

Outputs:
- Fabricated hardware
- As-built documentation
- Assembly procedures
- Configuration identification

### 3.3 Hardware Validation and Verification Process

#### 3.3.1 Requirements Validation
Objective: Ensure requirements are correct and complete

Methods:
- Requirements review
- Prototyping
- Analysis and simulation
- Test case development

Coverage:
- All hardware requirements reviewed and validated

#### 3.3.2 Design Verification
Objective: Verify design satisfies requirements

Methods:
- Design review
- Analysis (thermal, electrical, mechanical, timing)
- Simulation (circuit, HDL, system-level)
- Design walkthrough

Coverage:
- All requirements traced to design
- All design elements traced to requirements
- Critical timing paths analyzed
- Failure modes analyzed

#### 3.3.3 Hardware Testing
Objective: Verify hardware implementation

Test Types:
- **Functional Testing**: Verify normal operation
- **Robustness Testing**: Verify abnormal conditions
- **Environmental Testing**: Temperature, vibration, humidity, EMI/EMC
- **Margin Testing**: Verify design margins
- **Life Testing**: Reliability and endurance
- **Acceptance Testing**: Production unit verification

Test Coverage:
- 100% of requirements tested (DAL A-D)
- Boundary conditions tested
- Failure mode testing
- Integration with software and system

#### 3.3.4 Advanced Verification Methods
For complex hardware (FPGA/ASIC):
- Formal verification
- HDL code coverage analysis
- Logic equivalence checking
- Static timing analysis
- Hardware-in-the-loop (HIL) testing

Coverage Requirements by DAL:
- **Level A**: Modified Condition/Decision Coverage (MC/DC) for HDL
- **Level B**: Decision Coverage (DC) for HDL
- **Level C**: Statement Coverage for HDL
- **Level D**: Requirements-based testing only
- **Level E**: No specific coverage required

### 3.4 Hardware Configuration Management Process

#### 3.4.1 Configuration Identification
Activities:
- Hardware item identification
- Baseline establishment
- Version control
- Change identification

Outputs:
- Configuration index
- Hardware Life Cycle Environment Configuration Index (HECI)
- Problem reports and change requests

#### 3.4.2 Baselines and Traceability
Baselines:
- Hardware Requirements Baseline
- Hardware Design Baseline (schematics, BOM, HDL)
- Hardware Implementation Baseline (as-built)
- Hardware Verification Baseline (test results)

Traceability:
- Requirements to design
- Design to implementation
- Requirements to tests
- Changes to requirements

#### 3.4.3 Change Control
Process:
- Change request submission
- Impact analysis (technical and certification)
- Change approval board review
- Implementation and verification
- Regression analysis
- Configuration audit

### 3.5 Hardware Quality Assurance Process

#### 3.5.1 Process Assurance
Activities:
- Process compliance verification
- Standards compliance audits
- Process improvement

Outputs:
- HQA records
- Process compliance reports
- Audit findings and corrective actions

#### 3.5.2 Product Assurance
Activities:
- Review of hardware development outputs
- Verification independence
- Problem report review
- Component qualification review

Outputs:
- Review records
- Verification results
- Conformity review records

#### 3.5.3 Conformity Review
Objective: Verify certification compliance

Reviews:
- Hardware Accomplishment Summary (HAS) review
- Compliance checklist review
- Evidence package review

### 3.6 Certification Liaison Process

#### 3.6.1 Authority Coordination
Activities:
- PHAC submittal and approval
- Periodic status reviews
- Finding resolution
- Final certification package submittal

Schedule:
- PHAC approval: Phase C exit
- Mid-project review: Phase D
- Compliance demonstration: Phase E
- Final audit: Phase F

#### 3.6.2 Means of Compliance
Methods:
- Requirements-based testing
- Analysis (thermal, electrical, timing, safety)
- Design and implementation reviews
- Environmental testing
- Process compliance audits

## 4. Hardware Life Cycle Data

### 4.1 Planning Data
- Plan for Hardware Aspects of Certification (PHAC)
- Hardware Development Plan (HDP)
- Hardware Verification Plan (HVP)
- Hardware Configuration Management Plan (HCMP)
- Hardware Quality Assurance Plan (HQAP)

### 4.2 Development Data
- Hardware Requirements Standards
- Hardware Design Standards
- Hardware Validation and Verification Standards
- Hardware Requirements Document (HRD)
- Hardware Design Description (HDD)
- Schematics and PCB layouts
- Bill of Materials (BOM)
- HDL source code (for FPGA/ASIC)
- Component qualification data
- Assembly drawings and procedures

### 4.3 Verification Data
- Hardware Verification Procedures (HVP)
- Hardware Verification Results (HVR)
- Hardware Life Cycle Environment Configuration Index (HECI)
- Problem Reports
- Hardware Configuration Index
- Hardware Process Assurance Records
- Hardware Accomplishment Summary (HAS)

## 5. Complex Custom Hardware Devices

### 5.1 FPGA/ASIC Design Process
For programmable logic and custom ICs:
- HDL coding standards (VHDL/Verilog)
- Synthesis guidelines
- Place and route constraints
- Timing analysis requirements
- Simulation requirements
- Formal verification methods

### 5.2 HDL Code Standards
Requirements:
- Structured and modular design
- Comments and documentation
- Naming conventions
- Synchronous design practices
- Clock domain crossing management
- Reset strategy
- Testability features (scan chains, BIST)

### 5.3 Verification Methods
- HDL simulation (functional and timing)
- Code coverage analysis (statement, decision, MC/DC)
- Logic equivalence checking
- Static timing analysis
- Formal property verification
- Hardware emulation
- FPGA-in-the-loop testing

## 6. Component Management

### 6.1 Component Selection Process
Criteria:
- Performance and functional requirements
- Reliability and quality level
- Availability and lifecycle
- Environmental ratings
- Previous usage history
- Qualification status

### 6.2 Component Categories
Per DO-254:
- **Simple Components**: Behavior can be fully determined (resistors, capacitors, etc.)
- **Complex Components**: Behavior cannot be fully determined (microprocessors, PLDs, etc.)

### 6.3 Component Qualification
For complex components:
- Service history review
- Manufacturer data review
- Application-specific testing
- Failure mode analysis
- Derating analysis

### 6.4 Obsolescence Management
Process:
- Lifecycle monitoring
- Obsolescence forecasting
- Redesign planning
- Last-time-buy decisions
- Alternative component qualification

## 7. Tool Qualification

### 7.1 Tool Identification
Development and verification tools requiring qualification per DO-254 Section 11:

| Tool Name | Tool Type | Qualification Level | Rationale |
|-----------|-----------|---------------------|-----------|
| [HDL Synthesizer] | Development | TQL-1 | Generates netlist from HDL |
| [Place & Route] | Development | TQL-1 | Generates FPGA configuration |
| [Logic Equivalence] | Verification | TQL-2 | Verifies design equivalence |
| [Timing Analyzer] | Verification | TQL-2 | Verifies timing constraints |
| [Coverage Tool] | Verification | TQL-3 | HDL code coverage analysis |

### 7.2 Tool Qualification Process
For each tool requiring qualification:
1. Tool Assessment Report (TAR)
2. Tool Qualification Plan (TQP)
3. Tool Operational Requirements (TOR)
4. Tool Qualification Data (TQD)
5. Tool Qualification Summary (TQS)

Reference: [`../../TOOL_QUALIFICATION/`](../../TOOL_QUALIFICATION/)

## 8. Previously Developed Hardware (PDH)

### 8.1 Commercial Off-The-Shelf (COTS)
If COTS hardware is used:
- Service history review
- Application suitability assessment
- Environmental compatibility
- Integration testing
- Failure mode analysis

### 8.2 Reused Hardware
For hardware reused from previous projects:
- Credit for previous compliance evidence
- Gap analysis for new requirements
- Regression testing
- Change impact analysis
- Configuration compatibility

## 9. Compliance Matrix

### 9.1 DO-254 Objectives
All objectives from DO-254 Tables applicable to assigned hardware design assurance levels will be demonstrated.

Reference: [`../../COMPLIANCE_CHECKLISTS/DO_254_CHECKLIST.csv`](../../COMPLIANCE_CHECKLISTS/)

### 9.2 Evidence References
Each objective will have:
- Compliance method (Test, Analysis, Review, Inspection)
- Evidence location
- Verification status
- Authority review status

Reference: [`../../06-EVIDENCE/EVIDENCE_INDEX.csv`](../../../06-EVIDENCE/)

## 10. Hardware Accomplishment Summary (HAS)

### 10.1 Purpose
The Hardware Accomplishment Summary provides evidence that:
- Hardware life cycle processes have been completed
- Hardware complies with requirements
- All DO-254 objectives have been satisfied

### 10.2 Content
The HAS will include:
- Hardware overview and configuration
- Compliance statement by objective
- Deviations and alternative means of compliance
- Tool qualification summary
- Component qualification summary
- Problem report summary
- Hardware life cycle data index
- Schedule and status

### 10.3 Schedule
- Draft HAS: Phase E
- Final HAS: Phase F (certification submission)

## 11. Deviations and Alternative Means of Compliance

### 11.1 Process
If standard DO-254 guidance cannot be followed:
1. Document deviation rationale
2. Propose alternative means of compliance
3. Prepare Issue Paper for authority review
4. Obtain authority approval before implementation

Reference: [`../../AUTHORITY_CORRESPONDENCE/ISSUE_PAPERS/`](../../AUTHORITY_CORRESPONDENCE/ISSUE_PAPERS/)

### 11.2 Tracking
All deviations tracked in:
- PHAC (this document)
- Hardware Accomplishment Summary
- Compliance checklist

## 12. Hardware Safety Assessment

### 12.1 Safety Requirements
Hardware safety requirements derived from:
- System safety assessment (ARP4761)
- Functional Hazard Assessment (FHA)
- Fault Tree Analysis (FTA)
- Failure Modes and Effects Analysis (FMEA)

### 12.2 Hardware Safety Analysis
Activities:
- Single point failure analysis
- Common mode failure analysis
- Fault injection testing
- Sneak circuit analysis
- Worst-case analysis
- Derating analysis

## 13. Environmental Qualification

### 13.1 Environmental Testing
Required tests per RTCA DO-160:
- Temperature and altitude
- Temperature variation
- Humidity
- Operational shock and crash safety
- Vibration
- Electromagnetic interference (EMI)
- Radio frequency susceptibility (RFS)
- Induced signal susceptibility
- Magnetic effect
- Power input
- Voltage spike
- Audio frequency conducted susceptibility
- Lightning indirect effects
- Ice and freezing rain
- Fungus resistance (if applicable)

### 13.2 Test Categories
Per DO-160:
- Category A through X (based on installation location)
- Test levels based on operational environment

## 14. Schedule and Milestones

### 14.1 Key Milestones
| Milestone | Description | Phase | Target Date |
|-----------|-------------|-------|-------------|
| PHAC Approval | PHAC approved by authority | C | [Date] |
| Requirements Baseline | HRD complete and baselined | C | [Date] |
| Design Baseline | HDD complete and baselined | D | [Date] |
| Hardware Complete | All hardware fabricated | D | [Date] |
| Verification Complete | All testing complete | E | [Date] |
| HAS Complete | Hardware Accomplishment Summary | E | [Date] |
| Certification Audit | Authority final audit | F | [Date] |
| Type Certificate | TC issued | F | [Date] |

### 14.2 Reviews with Authority
- PHAC Review: Phase C
- Mid-project Review: Phase D
- Compliance Demonstration: Phase E
- Final Certification Audit: Phase F

## 15. Roles and Responsibilities

### 15.1 Organizational Structure
- **Certification Manager**: Overall certification coordination
- **Hardware Manager**: Hardware development leadership
- **Electronics Lead**: Circuit design and analysis
- **FPGA/ASIC Lead**: Complex device development
- **Quality Assurance Manager**: Process compliance oversight
- **Configuration Manager**: Baseline and change control
- **Verification Lead**: Test and analysis coordination

### 15.2 Independence Requirements
- Hardware quality assurance: Independent from development
- Hardware verification: Independent from development (DAL A-B)
- Authority liaison: Independent reporting

## 16. Standards and References

### 16.1 Applicable Documents
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware
- DO-330: Software Tool Qualification Considerations (for HDL tools)
- DO-160: Environmental Conditions and Test Procedures for Airborne Equipment
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems
- ARP4761: Guidelines and Methods for Conducting the Safety Assessment Process

### 16.2 Project Standards
- Hardware Requirements Standards: [Document reference]
- Hardware Design Standards: [Document reference]
- HDL Coding Standards: [Document reference]
- Hardware Test Standards: [Document reference]

## 17. Document Control

### 17.1 Revisions
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-16 | [Name] | Initial draft |

### 17.2 Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Certification Manager | [Name] | | |
| Hardware Manager | [Name] | | |
| Quality Assurance Manager | [Name] | | |
| Chief Engineer | [Name] | | |

### 17.3 Authority Approval
| Authority | Representative | Date | Reference |
|-----------|---------------|------|-----------|
| EASA | [Name] | | [Docket #] |
| FAA | [Name] | | [Docket #] |

---

**Document Location**: `00-PROGRAM/COMPLIANCE/03-CERTIFICATION/CERTIFICATION_PLANS/AVIATION/PHAC_DO254.md`  
**Next Review**: Phase C exit or as required for changes  
**Related Documents**: PSAC, HDP, HVP, HCMP, HQAP, HAS
