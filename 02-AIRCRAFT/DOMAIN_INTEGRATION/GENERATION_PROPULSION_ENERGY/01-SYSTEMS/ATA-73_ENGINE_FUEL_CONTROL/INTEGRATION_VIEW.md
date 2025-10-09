# ATA-73 Engine Fuel Control - Integration View

## System Overview

Full Authority Digital Engine Control (FADEC) system managing fuel flow and engine operation.

## Architecture

### FADEC (ATA-73-10)
- Electronic Control Unit (ECU)
- Dual-channel redundant control
- Software-based control laws
- Engine parameter monitoring

### Pumps and Meters (ATA-73-20)
- Engine-driven fuel pump
- Flow meters
- Pressure sensors

### Valves and Actuation (ATA-73-30)
- Fuel metering valve
- Shutoff valves
- Actuators

## Key Integration Points

- **ATA-72**: Engine (fuel metering, speed sensing)
- **ATA-28**: Fuel system (fuel supply)
- **ATA-24**: Electrical power
- **ATA-76**: Engine controls (thrust lever position)
- **ATA-77**: Indication (fuel flow, pressure)
- **ATA-42**: Avionics (data bus)
- **ATA-92**: EWIS

## Interface Matrix

See `INTERFACE_MATRIX/73↔28_24_76_77_42_92.csv`

## Subsystems

- [ATA-73-10 FADEC](./SUBSYSTEMS/ATA-73-10_FADEC/)
- [ATA-73-20 Pumps/Meters](./SUBSYSTEMS/ATA-73-20_PUMPS_METERS/)
- [ATA-73-30 Valves/Actuation](./SUBSYSTEMS/ATA-73-30_VALVES_ACTUATION/)

---

**Last Updated**: 2024-01-15
