# SPEC

Requirements specifications for control logic and control law modes.

## Contents

- **[control_modes.md](control_modes.md)** - Normal Law control mode requirements
  - Pitch axis control (load factor command)
  - Roll axis control (bank angle command)
  - Yaw axis coordination
  - Envelope protection (alpha, load factor, overspeed)
  - Performance requirements
  - Requirements traceability matrix

## Purpose

This directory contains the requirements specifications for control laws, defining:

- Functional requirements (what the control law must do)
- Performance requirements (how well it must perform)
- Safety requirements (envelope protection, monitoring)
- Traceability to certification standards (CS-25, FAR Part 25)

## Control Law Modes

### Normal Law (Defined)
- Full flight envelope protection
- Load factor command (pitch)
- Bank angle command (roll)
- Automatic turn coordination (yaw)
- Status: **Implemented and tested**

### Alternate Law (Future)
- Degraded mode when sensor failures occur
- Direct relationship between stick and surface
- Reduced envelope protection

### Direct Law (Future)
- Minimal control augmentation
- Direct pilot control
- Used in multiple failure scenarios

## Requirements Format

Each requirement includes:
- **Requirement ID**: Unique identifier (e.g., REQ-FCC-011)
- **Description**: Clear statement of the requirement
- **Verification Method**: How it will be verified (analysis, test, inspection)
- **Traceability**: Parent requirements and standards
- **DAL Level**: Design Assurance Level (typically DAL-A for flight controls)

## Usage

1. Review requirements before implementing control laws
2. Create test vectors in [../TESTS/VECTORS/](../TESTS/VECTORS/) to validate each requirement
3. Maintain traceability matrix
4. Update requirements through ECR (Engineering Change Request) process

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
