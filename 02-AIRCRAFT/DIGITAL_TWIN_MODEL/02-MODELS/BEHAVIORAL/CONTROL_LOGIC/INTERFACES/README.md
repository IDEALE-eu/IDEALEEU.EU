# INTERFACES

Interface Control Documents (ICD) for control logic signals and timing.

## Contents

- **[signals.yaml](signals.yaml)** - Complete signal interface definition for ATA-27 Flight Controls
  - Input signals (pilot commands, sensors, autopilot)
  - Output signals (actuator commands, status, health)
  - Internal signals (control law states)
  - Protocols (ARINC 429, ARINC 664, analog)
  - Validation and monitoring rules

- **[timing.md](timing.md)** - Timing analysis and requirements
  - Control loop timing (50 Hz)
  - End-to-end latency budgets
  - Jitter and synchronization
  - Watchdog and timeout specifications

## Purpose

This directory provides the interface specifications between the Flight Control Computer (FCC) and other aircraft systems. All signals are defined with:

- Signal identifiers and names
- Data types and units
- Valid ranges
- Sample rates and protocols
- EBOM references
- DAL level and redundancy requirements

## Related Systems

- **ATA-25**: Cockpit Controls (pilot inputs)
- **ATA-27**: Flight Controls (actuators, surfaces)
- **ATA-22**: Auto Flight (autopilot commands)
- **ATA-34**: Air Data System (airspeed, altitude, AoA)
- **ATA-42**: IMA Platform (if FCC hosted on IMA)

## Usage

When developing or modifying control laws:

1. Reference [signals.yaml](signals.yaml) for signal definitions
2. Check [timing.md](timing.md) for timing constraints
3. Ensure signal IDs match in test vectors and models
4. Validate against interface requirements before integration

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
