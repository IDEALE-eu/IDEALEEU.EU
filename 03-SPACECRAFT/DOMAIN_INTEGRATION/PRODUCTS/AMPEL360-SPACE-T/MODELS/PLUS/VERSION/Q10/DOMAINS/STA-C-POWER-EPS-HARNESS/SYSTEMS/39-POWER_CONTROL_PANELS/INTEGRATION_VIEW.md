# 39-POWER_CONTROL_PANELS — Integration View

## System Overview

The Power Control Panels system provides centralized control, switching, and monitoring of electrical power distribution throughout the spacecraft. It includes power control units, switchgear, relays, contactors, and remote power controllers.

## Functional Description

This system integrates power switching and control equipment to manage power distribution to spacecraft subsystems. It provides commanded switching, fault detection and isolation, load management, and telemetry feedback on power distribution status.

## Key Interfaces

- **06 - Dimensions/Alignments**: Panel mounting and equipment alignment
- **15 - Environment/Vibration**: Shock and vibration protection for control equipment
- **24 - Electrical Power**: Primary power input from EPS
- **31 - Data Handling**: Command and telemetry interface for power control
- **42 - Thermal Control**: Heat dissipation from switching equipment
- **51 - Primary Structure**: Panel mounting and structural support
- **97 - Harness/EWIS**: Power distribution wiring and control signals

## Operational Modes

- **Standby**: Minimal power distribution for essential systems
- **Normal Operations**: Full power distribution to all active subsystems
- **Reconfiguration**: Dynamic power routing and load management
- **Fault Isolation**: Automatic or commanded isolation of failed circuits
- **Safe Mode**: Reduced configuration with essential services only

## Subsystems

- **39-10 Power Control Units (PCU)**: Central power control and switching units
- **39-20 Switchgear/Relays/Contactors**: Electromechanical switching devices
- **39-30 Panels/Racks/MCP**: Master control panels and equipment racks
- **39-40 Remote Power Controllers (RPC)**: Distributed power switching modules
- **39-60 Algorithms/Control**: Power control software and sequencing logic
- **39-80 Testing/Qualification**: Power control system testing procedures
