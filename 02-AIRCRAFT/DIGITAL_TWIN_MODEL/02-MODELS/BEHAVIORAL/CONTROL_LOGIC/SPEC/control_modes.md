# CONTROL LAW REQUIREMENTS SPECIFICATION
# ATA-27 Flight Controls - Normal Law Mode

**Document ID**: SPEC-FCC-001  
**System**: Flight Control Computer (FCC)  
**Subsystem**: Control Laws - Normal Law Mode  
**Version**: 1.0  
**Date**: 2025-01-15  
**Status**: Approved

## 1. Scope

This specification defines the requirements for the Normal Law control mode of the Flight Control Computer (FCC). Normal Law provides full flight envelope protection and optimal handling qualities during normal operations.

## 2. References

- **signals.yaml**: [../INTERFACES/signals.yaml](../INTERFACES/signals.yaml)
- **ATA-27 Configuration**: [../../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/](../../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/)
- **CS-25 / FAR Part 25**: Airworthiness standards
- **DO-178C**: Software considerations in airborne systems (DAL-A)

## 3. System Requirements

### 3.1 Control Law Architecture

**REQ-FCC-001**: The FCC shall implement a Normal Law control mode that provides:
- Pitch axis control with load factor command
- Roll axis control with bank angle command  
- Yaw axis coordination (turn coordination)
- Flight envelope protection

**Verification**: Design review, SIL/HIL testing  
**Traceability**: CS 25.143, CS 25.147  
**DAL**: A

### 3.2 Pitch Axis Control

**REQ-FCC-010**: In Normal Law, pitch control shall operate in load factor command mode.

**REQ-FCC-011**: The pitch control law shall compute elevator command as:
```
elevator_cmd = K_pitch * (n_z_cmd - n_z_actual) + K_q * q_rate + K_alpha * alpha_trim
```
Where:
- `n_z_cmd`: Commanded load factor (derived from stick input)
- `n_z_actual`: Actual load factor (from accelerometers)
- `q_rate`: Pitch rate (from rate gyros)
- `alpha_trim`: Angle of attack trim compensation

**Parameters**:
- `K_pitch`: Load factor gain (scheduled with dynamic pressure)
- `K_q`: Pitch rate damping gain
- `K_alpha`: Angle of attack compensation gain

**Verification**: Test vector validation (see [../TESTS/VECTORS/pitch_response_test.yaml](../TESTS/VECTORS/pitch_response_test.yaml))  
**Traceability**: REQ-FCC-001  
**DAL**: A

**REQ-FCC-012**: Load factor limits shall be enforced:
- Maximum positive: +2.5 g
- Maximum negative: -1.0 g

**Verification**: Corner case testing  
**Traceability**: CS 25.337  
**DAL**: A

### 3.3 Roll Axis Control

**REQ-FCC-020**: In Normal Law, roll control shall operate in bank angle command mode.

**REQ-FCC-021**: The roll control law shall compute aileron command as:
```
aileron_cmd = K_bank * (phi_cmd - phi_actual) + K_p * p_rate
```
Where:
- `phi_cmd`: Commanded bank angle (derived from stick input)
- `phi_actual`: Actual bank angle (from AHRS)
- `p_rate`: Roll rate (from rate gyros)

**Parameters**:
- `K_bank`: Bank angle gain
- `K_p`: Roll rate damping gain

**Verification**: Test vector validation  
**Traceability**: REQ-FCC-001  
**DAL**: A

**REQ-FCC-022**: Bank angle limits shall be enforced:
- Maximum bank angle: ±30 degrees (normal operations)
- Maximum bank angle: ±67 degrees (with override)

**Verification**: Limit testing  
**Traceability**: CS 25.143  
**DAL**: A

### 3.4 Yaw Axis Control

**REQ-FCC-030**: The FCC shall provide automatic turn coordination in Normal Law.

**REQ-FCC-031**: Turn coordination shall compute rudder command to null lateral acceleration:
```
rudder_cmd = K_beta * beta + K_r * r_rate + K_turn * turn_compensation
```
Where:
- `beta`: Sideslip angle
- `r_rate`: Yaw rate
- `turn_compensation`: Coordinated turn feedforward

**Verification**: Test vector validation  
**Traceability**: REQ-FCC-001  
**DAL**: A

### 3.5 Flight Envelope Protection

**REQ-FCC-040**: Normal Law shall provide automatic protection against:
- High angle of attack (alpha protection)
- Excessive load factor (g protection)  
- Overspeed (V_MO protection)
- Bank angle limits

**Verification**: Corner case testing (see [../TESTS/VECTORS/corner_cases/alpha_protection_test.yaml](../TESTS/VECTORS/corner_cases/alpha_protection_test.yaml))  
**Traceability**: CS 25.143, CS 25.1505  
**DAL**: A

**REQ-FCC-041**: Alpha protection shall activate when angle of attack exceeds:
- Warning threshold: 12 degrees
- Protection threshold: 15 degrees
- Hard limit: 18 degrees

**Action**: Automatic nose-down command to reduce angle of attack

**Verification**: Test case ALPHA-PROT-001  
**Traceability**: REQ-FCC-040  
**DAL**: A

**REQ-FCC-042**: Load factor protection shall limit commanded load factor to:
- +2.5 g maximum
- -1.0 g minimum

**Verification**: Test case LOAD-FACTOR-001  
**Traceability**: REQ-FCC-040  
**DAL**: A

### 3.6 Gain Scheduling

**REQ-FCC-050**: Control law gains shall be scheduled as a function of:
- Dynamic pressure (q)
- Mach number
- Configuration (flaps/slats position)
- Center of gravity (CG) position

**Verification**: Gain schedule validation across flight envelope  
**Traceability**: REQ-FCC-001  
**DAL**: A

**REQ-FCC-051**: Gain interpolation shall use linear interpolation between schedule points.

**Verification**: Unit test  
**Traceability**: REQ-FCC-050  
**DAL**: A

### 3.7 Mode Transitions

**REQ-FCC-060**: Normal Law shall remain active when:
- All sensors are valid (no failures)
- All FCC channels are operational
- Hydraulic systems are operational
- Air data is valid

**Verification**: Mode transition testing  
**Traceability**: System architecture  
**DAL**: A

**REQ-FCC-061**: Normal Law shall transition to Alternate Law when:
- One or more critical sensors fail
- FCC channel degradation detected
- Air data quality degraded

**Transition time**: <100 ms  
**Verification**: Failure mode testing  
**Traceability**: REQ-FCC-060  
**DAL**: A

## 4. Performance Requirements

### 4.1 Handling Qualities

**REQ-FCC-070**: Pitch response to step input:
- Time to 90% of commanded load factor: <2.0 seconds
- Overshoot: <10%
- Steady-state error: <0.1 g

**Verification**: Test case PITCH-RESP-001  
**Traceability**: CS 25.143  
**DAL**: A

**REQ-FCC-071**: Roll response to step input:
- Time to 90% of commanded bank angle: <3.0 seconds  
- Overshoot: <5%
- Steady-state error: <2 degrees

**Verification**: Test case ROLL-RESP-001  
**Traceability**: CS 25.147  
**DAL**: A

### 4.2 Stability Margins

**REQ-FCC-080**: Closed-loop stability margins shall meet:
- Gain margin: ≥6 dB
- Phase margin: ≥45 degrees

**Verification**: Frequency domain analysis  
**Traceability**: System requirements  
**DAL**: A

## 5. Monitoring and Health

**REQ-FCC-090**: The FCC shall continuously monitor:
- Control loop execution time
- Signal validity and freshness
- Cross-channel agreement
- Command reasonableness

**Verification**: Built-in test verification  
**Traceability**: System architecture  
**DAL**: A

**REQ-FCC-091**: When anomaly is detected, the FCC shall:
1. Log fault code to maintenance system
2. Annunciate to flight crew if safety-critical
3. Isolate failed channel if redundant channel available
4. Degrade control law mode if necessary

**Verification**: Fault injection testing  
**Traceability**: REQ-FCC-090  
**DAL**: A

## 6. Test Requirements

All requirements shall be verified through:

### 6.1 Software-in-the-Loop (SIL)
- Unit tests for individual functions
- Integration tests for control law assembly
- Test vectors defined in [../TESTS/VECTORS/](../TESTS/VECTORS/)

### 6.2 Hardware-in-the-Loop (HIL)
- Real-time execution on target hardware
- Actuator dynamics included
- Flight dynamics simulation

### 6.3 Flight Test
- Envelope expansion flights
- Handling qualities evaluation
- Failure mode verification

## 7. Requirements Traceability Matrix

| Requirement | Parent | Verification Method | Test Case | Status |
|-------------|--------|---------------------|-----------|--------|
| REQ-FCC-001 | CS 25.143 | Design Review, HIL | N/A | Approved |
| REQ-FCC-011 | REQ-FCC-001 | Test Vector | PITCH-RESP-001 | Approved |
| REQ-FCC-012 | CS 25.337 | Corner Case | LOAD-FACTOR-001 | Approved |
| REQ-FCC-021 | REQ-FCC-001 | Test Vector | ROLL-RESP-001 | Approved |
| REQ-FCC-022 | CS 25.143 | Limit Test | BANK-LIMIT-001 | Approved |
| REQ-FCC-031 | REQ-FCC-001 | Test Vector | YAW-COORD-001 | Approved |
| REQ-FCC-041 | REQ-FCC-040 | Corner Case | ALPHA-PROT-001 | Approved |
| REQ-FCC-042 | REQ-FCC-040 | Corner Case | LOAD-FACTOR-001 | Approved |
| REQ-FCC-051 | REQ-FCC-050 | Unit Test | GAIN-SCHED-001 | Approved |
| REQ-FCC-070 | CS 25.143 | Test Vector | PITCH-RESP-001 | Approved |
| REQ-FCC-071 | CS 25.147 | Test Vector | ROLL-RESP-001 | Approved |
| REQ-FCC-080 | System Req | Analysis | STABILITY-001 | Approved |

## 8. Compliance and Certification

- **Certification Basis**: CS-25 / FAR Part 25
- **Software Level**: DAL-A (DO-178C)
- **Hardware Level**: DAL-A (DO-254)
- **Authority**: EASA / FAA

## 9. Change History

| Version | Date | Author | Description | ECR |
|---------|------|--------|-------------|-----|
| 1.0 | 2025-01-15 | Flight Controls Engineering | Initial requirements specification | ECR-2025-001 |

---

**Approval**:
- **System Engineer**: [Signature Required]
- **Chief Engineer**: [Signature Required]  
- **Certification Authority**: [Pending]

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
