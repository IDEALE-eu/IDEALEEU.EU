# SOFTWARE

Spacecraft software engineering and product assurance standards.

## Overview

This directory contains standards for space software development based on ECSS-E-ST-40C (software engineering) and ECSS-Q-ST-80C (software product assurance).

## Applicable Standards

### ECSS-E-ST-40C - Software Engineering
- **Scope**: Software development lifecycle for space systems
- **Coverage**: Flight software, ground software, simulation software
- **Criticality Categories**: A (critical), B (essential), C (utility), D (support)

**Software Lifecycle**:
1. Software Requirements Definition
2. Software Architecture Design
3. Software Detailed Design and Production
4. Software Transfer
5. Software Validation
6. Software Acceptance and In-Orbit Commissioning
7. Software Operations and Maintenance
8. Software Disposal

### ECSS-Q-ST-80C - Software Product Assurance
- **Scope**: Quality assurance for software development
- **Key Activities**:
  - Software product assurance planning
  - Software requirements review
  - Software design and code review
  - Software testing oversight
  - Software configuration management
  - Software quality metrics

## Software Criticality

Software assigned criticality based on failure consequences:

| Category | Description | Failure Consequence | Requirements |
|----------|-------------|---------------------|--------------|
| A | Critical | Loss of mission or spacecraft | Most stringent |
| B | Essential | Major mission degradation | High rigor |
| C | Utility | Minor mission degradation | Moderate rigor |
| D | Support | No mission impact | Basic rigor |

Requirements tailored by category (e.g., documentation, testing, independence).

## Software Architecture

### Flight Software (FSW)
- **OBSW** - On-Board Software (executes on spacecraft)
  - Real-time operating system (RTOS)
  - Application software (AOCS, TM/TC, payload)
  - Boot software and fault management
- **Firmware** - Embedded in components (power, AOCS, instruments)

### Ground Software (GSW)
- **Mission Control System (MCS)** - Monitor and control spacecraft
- **Flight Dynamics System (FDS)** - Orbit determination and control
- **Payload Data Processing** - Science data processing
- **Simulators** - Spacecraft and environment simulation for testing

## Development Process

### Requirements Phase
- Derive software requirements from system requirements
- Software Requirements Document (SRD or SWRD)
- Requirements review and approval

### Design Phase
- **Architectural Design**: High-level structure, modules, interfaces
- **Detailed Design**: Algorithms, data structures, module specifications
- Design reviews (PDR, CDR at software level)

### Implementation Phase
- Code development per coding standards
- Static analysis and code reviews
- Unit testing

### Integration and Testing
- Software integration (module by module)
- Software validation testing
- Software/hardware integration
- System-level testing

### Validation
- Functional validation (requirements coverage)
- Performance validation (timing, memory, CPU)
- Environmental validation (TVAC, EMC)

## Software Verification

### Verification Methods
- **Review**: Design and code reviews
- **Inspection**: Static analysis, code inspections
- **Analysis**: Timing analysis, worst-case execution time (WCET), memory usage
- **Test**: Unit test, integration test, validation test

### Test Coverage
- Requirements coverage (all requirements tested)
- Code coverage (statement, branch, MC/DC for critical software)
- Interface coverage (all interfaces exercised)

## Key Deliverables

1. **Software Development Plan (SDP)** - Overall approach and lifecycle
2. **Software Requirements Document (SWRD)** - Software requirements specification
3. **Software Design Document (SDD)** - Architecture and detailed design
4. **Software User Manual (SUM)** - Operating instructions
5. **Software Validation Plan (SVP)** - Test strategy and approach
6. **Software Validation Report (SVR)** - Test results and compliance
7. **Software Configuration Index (SCI)** - All software items and versions
8. **Software Product Assurance Plan (SPAP)** - QA approach
9. **Software Product Assurance Report (SPAR)** - QA findings and status

## Coding Standards

- Language-specific standards (C, C++, Ada)
- MISRA C or similar for critical software
- Coding conventions (naming, structure, documentation)
- Forbidden constructs (recursion, dynamic memory, floating point in critical code)

## Software Tools

- **Compilers/Linkers**: Qualified or validated
- **Static Analysis**: MISRA checking, complexity metrics
- **Dynamic Analysis**: Code coverage, profiling
- **Version Control**: Configuration management system
- **Requirements Management**: Traceability tools

## Flight Software Considerations

### Real-Time Constraints
- Deterministic execution
- Interrupt handling
- Task scheduling and prioritization
- Timing margins

### Resource Constraints
- Limited memory (RAM, ROM)
- Limited CPU performance
- Power consumption
- Redundancy and fault tolerance

### Fault Management
- Watchdog timers
- Error detection and correction (EDAC)
- Safe mode and recovery
- Redundancy management (cold, warm, hot spares)

## Ground Software Considerations

- Mission operations workflows
- Human-machine interface (HMI)
- Database management
- Telemetry processing and display
- Command generation and validation

## Compliance Requirements

- Software development shall follow ECSS-E-ST-40C
- Software product assurance per ECSS-Q-ST-80C
- Criticality-based tailoring with justification
- Software verification complete before delivery
- Configuration management throughout lifecycle

## Integration with Other Standards

- **ECSS-E-ST-10C** - Systems engineering context
- **ECSS-Q-ST-60C** - If implementing fault tolerance in software
- **ECSS-E-ST-20C** - Electrical interfaces to hardware

## Tools and Templates

- Software requirements templates
- Software design document templates
- Test plan and report templates
- Software product assurance plan templates

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-013 (ECSS-E-ST-40C), STD-014 (ECSS-Q-ST-80C)
- ECSS Portal: https://ecss.nl
- 05-MAPPINGS/COMPLIANCE_MATRIX_TEMPLATES/ECSS_CM.csv

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
