# SOFTWARE

Software development and assurance standards for aircraft systems.

## Overview

This directory contains standards for airborne software development, including DO-178C (software), DO-330 (tool qualification), and DO-331/332/333 (model-based development supplements).

## Applicable Standards

### DO-178C - Software Considerations in Airborne Systems and Equipment Certification
- **Current Baseline**: DO-178C (replaces DO-178B)
- **Scope**: Software development for airborne systems
- **Software Levels**: A (catastrophic) through E (no safety effect)

**Key Processes**:
1. Software Planning Process
2. Software Development Process
3. Software Verification Process
4. Software Configuration Management Process
5. Software Quality Assurance Process
6. Certification Liaison Process

**Objectives by Level**:
- Level A: 71 objectives (all with independence)
- Level B: 69 objectives (some with independence)
- Level C: 62 objectives (limited independence)
- Level D: 38 objectives (no independence)
- Level E: 0 objectives (no DO-178C process required)

### DO-330 - Software Tool Qualification Considerations
- **Purpose**: Qualify tools that eliminate, reduce, or automate verification
- **Tool Qualification Levels**: TQL-1 through TQL-5
- **Criteria**:
  - Tool operational requirements
  - Software tool accomplishment summary
  - Tool qualification data

### DO-331 - Model-Based Development and Verification Supplement
- Addresses model-based development using tools like MATLAB/Simulink
- Additional objectives for model verification
- Integration with DO-178C objectives

### DO-332 - Object-Oriented Technology Supplement
- Additional considerations for OOP (C++, Ada, Java)
- Inheritance, polymorphism, dynamic dispatch
- Additional verification objectives

### DO-333 - Formal Methods Supplement
- Formal specification and verification
- Mathematical proof of correctness
- Credit for formal analysis toward DO-178C objectives

## Development Assurance Levels

Software assigned DAL based on system safety assessment (ARP4761):
- Derived from aircraft-level FHA
- PSSA allocates failure conditions to systems
- Software assigned most critical DAL of functions implemented

## Key Deliverables

1. **PSAC** - Plan for Software Aspects of Certification
2. **SDP** - Software Development Plan
3. **SVP** - Software Verification Plan
4. **SCMP** - Software Configuration Management Plan
5. **SQAP** - Software Quality Assurance Plan
6. **SRS** - Software Requirements Standards
7. **SDS** - Software Design Standards
8. **SCS** - Software Code Standards
9. **SVCP** - Software Verification Cases and Procedures
10. **SVR** - Software Verification Results
11. **SECI** - Software Configuration Index
12. **SAS** - Software Accomplishment Summary

## Tool Qualification

Tools requiring qualification per DO-330:
- **Development Tools** (TQL-5): compilers, linkers, code generators
- **Verification Tools** (TQL-1): test coverage analyzers, requirements tracers
- **Combination Tools**: static analyzers with verification credit

## Compliance Requirements

- Software development process shall comply with DO-178C
- Independence requirements met per software level
- Traceability: requirements → design → code → tests
- Configuration management of all software lifecycle data
- Quality assurance records and audits

## Integration with Other Standards

- **ARP4754A** - Systems engineering context for software development
- **DO-254** - Interface with hardware for integrated systems
- **DO-160** - Environmental testing of software/hardware integration

## Tools and Templates

- See 05-MAPPINGS/COMPLIANCE_MATRIX_TEMPLATES/DO178C_CM.csv
- Software standards documents templates
- Review and audit checklists

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-003 (DO-178C), STD-008 (DO-330), STD-009 (DO-331)
- 06-INTERPRETATIONS/AUTHORITY_POSITION_PAPERS/FAA_AC_20-115D.md
- 07-LINKS/TRAINING_MATERIALS.md - DO-178C training courses

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
