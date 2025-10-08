# HARDWARE

Hardware design assurance standards for complex electronic hardware.

## Overview

This directory contains standards for complex electronic hardware design assurance, primarily DO-254.

## Applicable Standards

### DO-254 - Design Assurance Guidance for Airborne Electronic Hardware
- **Scope**: Complex electronic hardware (ASIC, FPGA, PLD, complex analog/mixed-signal)
- **Hardware Design Assurance Levels**: A (catastrophic) through E (no safety effect)
- **Lifecycle**: Requirements → Conceptual → Detailed Design → Implementation → Verification

**Key Processes**:
1. Hardware Planning Process
2. Hardware Design Process
3. Hardware Validation and Verification Process
4. Hardware Configuration Management Process
5. Hardware Process Assurance Process
6. Certification Liaison Process

**Design Assurance Levels**:
- **Level A**: Catastrophic failure conditions
- **Level B**: Hazardous/severe-major failure conditions
- **Level C**: Major failure conditions
- **Level D**: Minor failure conditions
- **Level E**: No safety effect

## Hardware Categories

### Simple Hardware
- Discrete components (resistors, capacitors, diodes)
- Established reliability data available
- DO-254 not required (use MIL-HDBK-217 or equivalent)

### Complex Hardware
- ASIC (Application-Specific Integrated Circuit)
- FPGA (Field-Programmable Gate Array)
- PLD (Programmable Logic Device)
- Complex analog/mixed-signal
- Requires DO-254 compliance

## Key Deliverables

1. **PHAC** - Plan for Hardware Aspects of Certification
2. **HDP** - Hardware Design Plan
3. **HVP** - Hardware Verification Plan
4. **HCMP** - Hardware Configuration Management Plan
5. **HPAP** - Hardware Process Assurance Plan
6. **HWRS** - Hardware Requirements Standards
7. **HDS** - Hardware Design Standards
8. **HCI** - Hardware Configuration Index
9. **HVMR** - Hardware Verification Methods and Results
10. **PSAC (HW section)** - Requirements and Test Cases
11. **HAS** - Hardware Accomplishment Summary

## Design Verification Methods

- **Requirements-Based Test**: Verify each requirement met
- **Design Reviews**: Conceptual design review, detailed design review
- **Analysis**: Timing, worst-case, thermal, EMI/EMC
- **Test**: Functional, structural, requirements coverage
- **Inspection**: Visual examination of hardware
- **Requirements Traceability**: Requirements → design → verification

## Tool Qualification

Hardware tools requiring qualification (when output not verified):
- HDL synthesis tools
- Place-and-route tools
- Code generators
- Verification tools providing coverage credit

## Compliance Requirements

- Development process shall comply with DO-254
- Independence requirements met per hardware design assurance level
- Traceability: requirements → design → verification
- Configuration management of hardware lifecycle data
- Process assurance audits and records

## Integration with Other Standards

- **ARP4754A** - Systems engineering allocates requirements to hardware
- **DO-178C** - Hardware/software interface definition and verification
- **DO-160** - Environmental qualification testing
- **DO-330** - Tool qualification for hardware development/verification tools

## Design Considerations

- **Safety monitoring**: Built-in test (BIT), watchdogs, error detection
- **Fault tolerance**: Redundancy, voting, fail-safe design
- **EMI/EMC**: Per DO-160 Section 21 (conducted), Section 20 (radiated)
- **Single Event Effects (SEE)**: For high-altitude or space-exposed hardware
- **Derating**: Component stress reduction for reliability

## Tools and Templates

- See 05-MAPPINGS/ for compliance matrices
- Hardware design standards templates
- Verification procedures templates

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-004 (DO-254)
- 06-INTERPRETATIONS/FAQ.md - Hardware-specific questions
- FAA AC 20-152 - RTCA DO-254 recognition memo
- EASA CM-SWCEH-001 - Complex electronic hardware certification

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
