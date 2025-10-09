# ATA-49 APU - Integration View

## System Overview

The Auxiliary Power Unit (APU) provides independent electrical power and pneumatic (bleed air) generation when main engines are not operating, typically for ground operations and emergency backup power.

## Architecture

### APU Core (ATA-49-10)
- Gas turbine engine (small turbine)
- Compressor section
- Combustion chamber
- Turbine section
- Exhaust system

### APU Starter (ATA-49-20)
- Electric or pneumatic starter
- Starting motor/turbine
- Engagement mechanism
- Starting control

### APU Control (ATA-49-30)
- Electronic Control Unit (ECU)
- Start/stop sequencing
- Speed/load governing
- Protection and monitoring
- Fault management

## Key Integration Points

### APU ↔ Electrical Power (ATA-24)
- APU generator output to AC buses
- Starting power from main batteries
- APU generator paralleling capability
- Emergency power configuration

### APU ↔ Fuel System (ATA-28)
- Dedicated APU fuel feed
- Fuel valve control
- Fuel flow monitoring
- Fuel system isolation

### APU ↔ Bleed Air (ATA-29/75)
- Pneumatic bleed output
- Air conditioning supply
- Engine starting air supply
- Cabin pressurization

### APU ↔ Indicating (ATA-36)
- APU operating parameters
- EGT (Exhaust Gas Temperature)
- N1/N2 speeds
- Oil pressure and temperature

### APU ↔ EWIS (ATA-92)
- All electrical wiring
- Sensor harnesses
- Control wiring

## Operational Modes

### Ground Operation
- Primary power source on ground
- Air conditioning during ground ops
- Main engine starting capability

### In-Flight Emergency
- Emergency electrical power
- Emergency pneumatic supply
- Altitude limitations apply

## Performance Parameters

- **Electrical Output**: 90 kVA (typical)
- **Pneumatic Output**: 40 lb/min (typical)
- **Operating Altitude**: 0-35,000 ft (typical)
- **Start Time**: 60 seconds (typical)
- **EGT Limit**: 760°C (typical)

## Interface Matrix

See `INTERFACE_MATRIX/49↔24_28_29_36_92.csv` for detailed interface specifications.

## Subsystems

- [ATA-49-10 APU Core](./SUBSYSTEMS/ATA-49-10_APU_CORE/)
- [ATA-49-20 APU Starter](./SUBSYSTEMS/ATA-49-20_APU_STARTER/)
- [ATA-49-30 APU Control](./SUBSYSTEMS/ATA-49-30_APU_CONTROL/)

## Digital Thread Integration

### MBSE Links
- APU system model
- Operational state machines
- Performance envelopes

### Digital Twin KPIs
- APU run hours
- Start cycles
- EGT trends
- Fuel consumption
- Availability metrics

## Compliance References

- **CS-APU**: APU certification specifications
- **CS-25.1431**: Electronic Engine Control Systems (applicable to APU ECU)
- **DO-160**: Environmental testing
- **DO-178C**: Software (APU ECU)
- **DO-254**: Hardware (APU ECU)

## Related Documents

- [ATA-49 Configuration Base](../../../../CONFIGURATION_BASE/ATA-49_APU/)
- [Subsystem Details](./SUBSYSTEMS/)

---

**Last Updated**: 2024-01-15
