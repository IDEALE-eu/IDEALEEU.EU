# CONTROL_LOGIC

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/BEHAVIORAL > CONTROL_LOGIC**

Control system models for autopilot, autothrottle, and engine control with complete development lifecycle support.

## Purpose

This directory contains behavioral models, interfaces, specifications, and test artifacts for aircraft control logic systems. It provides a structured framework for:

- **Interface Control**: Signal definitions and timing requirements
- **Requirements Management**: Control law specifications and modes
- **Model Development**: Simulink/Modelica/FMU control models
- **Parameter Management**: Gains, schedules, and tuning data
- **Simulation**: Test harnesses and scenarios
- **Verification**: Test vectors, SIL/HIL testing, and evidence

## Directory Structure

```
CONTROL_LOGIC/
├─ INTERFACES/          # ICD, signals.yaml, timing.md
│  ├─ signals.yaml      # Signal interface definitions (I/O, protocols, timing)
│  └─ timing.md         # Timing analysis and requirements
│
├─ SPEC/                # Requirements, modes, limits
│  └─ control_modes.md  # Control law requirements (Normal Law example)
│
├─ MODELS/              # Control law models
│  ├─ *.slx             # Simulink models (not included in this example)
│  ├─ *.mo              # Modelica models (not included in this example)
│  └─ *.fmu             # Functional Mock-up Units (not included in this example)
│
├─ PARAMS/              # Tuning parameters and gain schedules
│  ├─ gains.yaml        # Control law gains and schedules
│  └─ schedules.csv     # Additional lookup tables (not included)
│
├─ SIM/                 # Simulation environment
│  ├─ harness/          # Test harnesses for SIL/HIL
│  └─ scenarios/        # Simulation scenarios
│
├─ TESTS/               # Test artifacts
│  ├─ VECTORS/          # Test cases and corner cases
│  │  ├─ cases/         # Nominal test vectors
│  │  │  └─ pitch_response_test.yaml
│  │  └─ corner_cases/  # Edge case and limit testing
│  │     └─ alpha_protection_test.yaml
│  ├─ SIL/              # Software-in-the-Loop tests
│  │  ├─ unit/          # Unit tests
│  │  └─ integration/   # Integration tests
│  └─ HIL/              # Hardware-in-the-Loop tests
│
├─ EVIDENCE/            # Verification evidence
│  ├─ coverage/         # Code coverage reports
│  └─ test_reports/     # Test execution results
│
└─ README.md            # This file
```

## Example: ATA-27 Flight Controls Integration

This directory provides a complete example for **ATA-27 Flight Controls** system integration, demonstrating how control logic interfaces with the flight control system.

### Signal Interface Example

The [signals.yaml](INTERFACES/signals.yaml) file defines the complete interface control document (ICD) for the Flight Control Computer (FCC):

- **Input signals**: Pilot commands, air data, autopilot commands, position feedback
- **Output signals**: Surface commands, status, health monitoring
- **Internal signals**: Control law intermediate variables
- **Protocols**: ARINC 429, ARINC 664, analog 4-20mA
- **Safety**: DAL-A requirements, redundancy, validation

**Related Configuration**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/](../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/)

### Timing Requirements

The [timing.md](INTERFACES/timing.md) document provides detailed timing analysis:

- Control loop timing (50 Hz, 20 ms period)
- End-to-end latency budgets (<60 ms requirement)
- Watchdog and timeout specifications
- Timing verification results

### Requirements Specification

The [control_modes.md](SPEC/control_modes.md) document defines requirements for Normal Law control mode:

- **REQ-FCC-011**: Pitch control law (load factor command mode)
- **REQ-FCC-021**: Roll control law (bank angle command mode)
- **REQ-FCC-031**: Yaw coordination
- **REQ-FCC-041**: Angle of attack protection
- **REQ-FCC-042**: Load factor protection

All requirements are traceable to CS-25/FAR Part 25 airworthiness standards.

### Test Vector Example

The [pitch_response_test.yaml](TESTS/VECTORS/cases/pitch_response_test.yaml) demonstrates validation of REQ-FCC-070:

**Test Case**: PITCH-RESP-001  
**Validates**: Pitch response to step input
- Rise time < 2.0 seconds
- Overshoot < 10%
- Steady-state error < 0.1 g

### Corner Case Example

The [alpha_protection_test.yaml](TESTS/VECTORS/corner_cases/alpha_protection_test.yaml) validates envelope protection:

**Test Case**: ALPHA-PROT-001  
**Validates**: REQ-FCC-041 (Angle of attack protection)
- Protection activates at 15° AoA
- Maximum AoA never exceeds 18° (hard limit)
- Activation time < 50 ms

This test simulates an aggressive pilot input approaching stall conditions to verify that the automatic protection system prevents loss of control.

### Control Parameters

The [gains.yaml](PARAMS/gains.yaml) file contains control law tuning parameters:

- **Pitch axis**: Load factor gains, pitch rate damping, AoA compensation
- **Roll axis**: Bank angle gains, roll rate damping
- **Yaw axis**: Sideslip coordination, turn coordination
- **Gain scheduling**: Varies with dynamic pressure, CG position, configuration
- **Envelope protection**: Alpha protection, load factor limits, overspeed protection

All parameters are flight-tested and certified to DO-178C (DAL-A).

## Use Case: Creating a Test Vector

To create a new test vector for validating a requirement:

1. **Identify the requirement** in [SPEC/control_modes.md](SPEC/control_modes.md)
   - Example: REQ-FCC-070 (pitch response performance)

2. **Define test inputs** based on [signals.yaml](INTERFACES/signals.yaml)
   - Use signal IDs (e.g., FCC_IN_001 for pilot_stick_pitch_cmd)
   - Specify time-based input profiles

3. **Define expected outputs** with acceptance criteria
   - Reference output signal IDs (e.g., FCC_OUT_001 for elevator_cmd_left)
   - Specify performance metrics (rise time, overshoot, steady-state error)

4. **Create test vector YAML** in [TESTS/VECTORS/cases/](TESTS/VECTORS/cases/)
   - See [pitch_response_test.yaml](TESTS/VECTORS/cases/pitch_response_test.yaml) as template
   - Include traceability to requirements and signals

5. **Execute in SIL/HIL environment**
   - Use test harness from [SIM/harness/](SIM/harness/)
   - Log results to [EVIDENCE/test_results/](EVIDENCE/)

6. **Generate test report**
   - Document pass/fail for each acceptance criterion
   - Archive in [EVIDENCE/test_reports/](EVIDENCE/test_reports/)

## ATA Chapter Links

This control logic framework supports multiple ATA chapters:

- **ATA-22** - Auto Flight (autopilot control laws)
- **ATA-27** - Flight Controls (primary example in this implementation)
- **ATA-76** - Engine Controls (thrust management)

### ATA-27 Flight Controls Integration

The control logic in this directory directly interfaces with the ATA-27 Flight Controls system configuration:

**Configuration Baseline**: [02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/](../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/)

**Key Interfaces**:
- **ICD**: Signal interfaces defined in [signals.yaml](INTERFACES/signals.yaml) complement ATA-27 ICD/
- **Parameters**: Control gains in [gains.yaml](PARAMS/gains.yaml) align with ATA-27 PARAMS/
- **Verification**: Test vectors provide evidence for ATA-27 VERIFICATION/

**Safety Considerations**:
- **DAL-A**: All control laws certified to DO-178C (DAL-A)
- **Redundancy**: Triple-modular redundancy with voting
- **Envelope Protection**: Automatic protection against stall, overspeed, excessive load factor
- **Fault Tolerance**: Graceful degradation to Alternate Law or Direct Law

## Model Formats

- **Simulink** (`.slx`): Control diagrams and simulations
- **Modelica** (`.mo`): Object-oriented physical modeling
- **FMU** (`.fmu`): Functional Mock-up Units for co-simulation
- **C/C++**: Generated code for real-time execution

## Fidelity Level

- **Level 5 (Real-Time)**: Control loop execution at 10-50 Hz
- **Hardware-in-the-Loop**: Real-time execution on target FCC hardware
- **Flight Dynamics Integration**: Full 6-DOF non-linear aircraft model

## Validation Requirements

### Software-in-the-Loop (SIL)
- Unit tests for individual control functions
- Integration tests for complete control laws
- Requirements-based test coverage >100% (including corner cases)

### Hardware-in-the-Loop (HIL)
- Real-time execution on target hardware
- Actuator dynamics and hydraulic systems included
- Timing verification and latency measurement

### Certification Evidence
- **DO-178C** (DAL-A): Software requirements, design, testing
- **DO-254** (DAL-A): Hardware timing and logic verification
- **ARP-4754A**: System-level safety assessment
- **CS-25 / FAR Part 25**: Airworthiness compliance

## Standards and Compliance

- **DO-178C**: Software Considerations in Airborne Systems (DAL-A)
- **DO-254**: Design Assurance Guidance for Airborne Electronic Hardware (DAL-A)
- **ARP-4754A**: Guidelines for Development of Civil Aircraft and Systems
- **CS-25 / FAR Part 25**: Airworthiness Standards for Transport Category Airplanes
- **DO-160**: Environmental Conditions and Test Procedures for Airborne Equipment

## Related Documents

- [ATA-27 Flight Controls Configuration](../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/)
- [Configuration Management](../../../../../00-PROGRAM/CONFIG_MGMT/)
- [Interface Control Documents](../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

## Contacts

- **System Owner**: Flight Controls Engineering
- **Model Development**: Digital Twin Team
- **Certification**: Compliance & Certification Team
- **Configuration Owner**: Configuration Management

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`  
**Last Updated**: 2025-01-15  
**Version**: 1.0
