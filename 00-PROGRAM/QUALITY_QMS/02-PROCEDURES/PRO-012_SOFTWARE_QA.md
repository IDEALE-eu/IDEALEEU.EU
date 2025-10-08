# PRO-012: Software Quality Assurance (DO-178C)

**Procedure Number:** PRO-012  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Chief Engineer (Aircraft)

## 1. Purpose

Establish software development and quality assurance requirements for airborne and spacecraft software per DO-178C and ECSS-Q-ST-80C.

## 2. Scope

Applies to:
- Flight control software
- Avionics software
- Mission-critical spacecraft software
- Ground support software for safety-critical systems

## 3. Design Assurance Level (DAL)

Per ARP4754A/DO-178C:
- **DAL A:** Catastrophic failure condition
- **DAL B:** Hazardous failure condition
- **DAL C:** Major failure condition
- **DAL D:** Minor failure condition
- **DAL E:** No safety effect

DAL determines rigor of software development and verification activities.

## 4. Software Lifecycle

### 4.1 Planning Process
- Software Development Plan (SDP)
- Software Verification Plan (SVP)
- Software Configuration Management Plan (SCMP)
- Software Quality Assurance Plan (SQAP)
- Tool Qualification Plans (if required)

### 4.2 Development Process
- High-level requirements
- Low-level requirements
- Software architecture
- Source code implementation
- Integration

### 4.3 Verification Process
- Requirements-based testing
- Structural coverage analysis
- Traceability analysis
- Review of verification results

### 4.4 Configuration Management
- Baseline identification
- Change control
- Version control
- Problem reporting

### 4.5 Quality Assurance
- Process assurance
- Product assurance
- Conformity review

### 4.6 Certification Liaison
- Interface with certification authorities
- Compliance demonstration
- Software Accomplishment Summary (SAS)

## 5. Software Requirements

### 5.1 High-Level Requirements (HLR)
- Derived from system requirements
- Define what software shall do
- Traceable to system requirements
- Verifiable
- Reviewed and approved

### 5.2 Low-Level Requirements (LLR)
- Derived from HLR and architecture
- Detailed design-level requirements
- Traceable to HLR
- Implementable in source code
- Verifiable

### 5.3 Requirements Standards
- Unambiguous
- Consistent
- Complete
- Traceable
- Verifiable

## 6. Software Verification

### 6.1 Reviews
- Requirements reviews
- Design reviews
- Code reviews
- Verification results reviews

### 6.2 Analysis
- Traceability analysis (bidirectional)
- Worst-case execution time (WCET)
- Resource usage analysis
- Stack analysis

### 6.3 Testing

**Requirements-Based Testing:**
- Test cases for all requirements
- Normal range
- Boundary values
- Robustness (off-nominal, error conditions)

**Structural Coverage (DAL-dependent):**
- **DAL A:** MC/DC (Modified Condition/Decision Coverage)
- **DAL B:** Decision Coverage
- **DAL C:** Statement Coverage
- **DAL D:** Statement Coverage (reduced)
- **DAL E:** No specific coverage required

**Test Environment:**
- Target hardware testing (preferred)
- Validated simulator acceptable
- Integration testing
- Hardware/software integration testing

## 7. Software Configuration Management

**Elements:**
- Version control system (Git, SVN, etc.)
- Configuration identification
- Baseline management
- Change control (linked to PRO-003)
- Archive and retrieval
- Tool control

**Baselines:**
- Requirements baseline
- Design baseline
- Code baseline
- Verification baseline

## 8. Software Quality Assurance

**Activities:**
- Process compliance audits
- Product evaluations
- Independence from development
- Conformity review
- Records review

**Independence:**
- SQA independent from development
- May be organizational or project-level
- DAL A requires strong independence

## 9. Tool Qualification

**Tools Requiring Qualification:**
- Compilers (unless verified outputs)
- Code generators
- Static analyzers (used for compliance evidence)
- Test coverage tools

**Qualification Criteria:**
- Tool Operational Requirements (TOR)
- Tool Qualification Plan
- Tool Qualification Data
- Tool Accomplishment Summary

## 10. ECSS Software Requirements

For spacecraft software per ECSS-Q-ST-80C:
- Software requirements definition
- Software architectural design
- Software detailed design
- Software unit implementation and testing
- Software integration and testing
- Software verification and validation
- Software configuration management
- Software quality assurance

**Criticality Categories:**
- Category A: Critical
- Category B: Essential
- Category C: Non-essential

## 11. Records

- Software plans (SDP, SVP, SCMP, SQAP)
- Requirements specifications
- Design descriptions
- Source code (controlled)
- Verification procedures and results
- Test reports and coverage analysis
- Problem reports and change records
- Traceability matrices
- Configuration management records
- Software Accomplishment Summary (SAS)

**Retention:** Life of aircraft/spacecraft + 10 years

## 12. Related Documents

- DO-178C (Software Considerations in Airborne Systems)
- ARP4754A (Aircraft Development)
- ECSS-Q-ST-80C (Software Product Assurance)
- PRO-003_CHANGE_CONTROL
- Section 02-AIRCRAFT/DOMAIN_INTEGRATION/INFO_COMM_AVIONICS/
- Section 03-SPACECRAFT/SOFTWARE/

## 13. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Chief Engineer (Aircraft) |
