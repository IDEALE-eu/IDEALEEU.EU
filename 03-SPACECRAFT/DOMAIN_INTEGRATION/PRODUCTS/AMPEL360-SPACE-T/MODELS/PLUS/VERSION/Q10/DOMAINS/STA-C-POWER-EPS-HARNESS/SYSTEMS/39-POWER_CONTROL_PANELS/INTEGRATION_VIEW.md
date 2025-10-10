# 39-POWER_CONTROL_PANELS — Integration View

## System Overview

The Power Control Panels system provides **centralized and distributed control**, **switching**, **monitoring**, and **fault isolation** for electrical power distribution across the spacecraft. It ensures reliable, commanded, and safe power delivery to all subsystems through a combination of electromechanical and solid-state switching technologies.

## Functional Description

This system integrates:
- **Power Control Units** (PCUs) for centralized command,
- **Remote Power Controllers** (RPCs) for distributed load switching,
- **Electromechanical relays/contactors** for high-reliability circuits,
- **Telemetry and health monitoring** for real-time status,
- **FDIR logic** for automatic fault response.

Power commands originate from **31-Data Handling**, are executed by **39-40_RPC** and **39-10_PCU**, and fed back via **97-Harness/EWIS**.

## Key Interfaces

| Interface To | System ID | Interface Type | Key Exchange |
|-------------|----------|----------------|--------------|
| Dimensions & Alignments | 06 | Mechanical | Panel mounting datums, equipment alignment pins |
| Environment & Vibration | 15 | Environmental | Shock/vibe qualification, acoustic survival |
| [Electrical Power](../24-ELECTRICAL_POWER/) | 24 | Power | 28V unregulated bus input; load current feedback |
| [Data Handling](../../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/31-DATA_HANDLING/) | 31 | Data/Command | Switch commands, RPC status, fault flags (SpaceWire/CAN) |
| [Thermal Control](../../STA-E-THERMAL-ENVIRONMENTAL-LIFESUPPORT/SYSTEMS/42-THERMAL_CONTROL/) | 42 | Thermal | Heat dissipation from RPCs and contactors |
| [Primary Structure](../../STA-A-STRUCTURES-MECHANISMS/SYSTEMS/51-PRIMARY_STRUCTURE/) | 51 | Structural | Panel mounting brackets, load paths for launch |
| [Harness / EWIS](../97-HARNESS_EWIS/) | 97 | Electrical | Command/status wiring, switched power outputs |

## Operational Modes

- **Standby**: Minimal power distribution for essential systems (spacecraft off-nominal)
- **Normal Operations**: Full power distribution to all active subsystems
- **Reconfiguration**: Dynamic power routing and load management (mission phase changes)
- **Fault Isolation**: Automatic or commanded isolation of failed circuits (FDIR)
- **Safe Mode**: Reduced configuration with essential services only (critical loads)

## Fault Detection, Isolation & Recovery (FDIR)

- **Overcurrent detection**: RPC trip on overload (configurable thresholds)
- **Automatic retry**: Configurable retry count (0–3) with backoff
- **Load shedding**: Priority-based load shedding on power budget violation
- **Telemetry feedback**: Real-time status to 31-Data Handling for ground monitoring

## Subsystems

- [**39-10 Power Control Units (PCU)**](./SUBSYSTEMS/39-10_POWER_CONTROL_UNITS_PCU/): Central power control and switching units
- [**39-20 Switchgear/Relays/Contactors**](./SUBSYSTEMS/39-20_SWITCHGEAR_RELAYS_CONTACTORS/): Electromechanical switching devices
- [**39-30 Panels/Racks/MCP**](./SUBSYSTEMS/39-30_PANELS_RACKS_MCP/): Master control panels and equipment racks
- [**39-40 Remote Power Controllers (RPC)**](./SUBSYSTEMS/39-40_REMOTE_POWER_CONTROLLERS_RPC/): Distributed power switching modules
- [**39-60 Algorithms/Control**](./SUBSYSTEMS/39-60_ALGORITHMS_CONTROL/): Power control software and sequencing logic
- [**39-80 Testing/Qualification**](./SUBSYSTEMS/39-80_TESTING_QUALIFICATION/): Power control system testing procedures
