# ATA-72 Engine - Integration View

## System Overview

Main propulsion engine system including core engine and fan/propulsor assembly.

## Architecture

### Core Engine (ATA-72-10)
- Compressor stages
- Combustion chamber
- Turbine stages
- Engine case and mounts

### Fan or Propulsor (ATA-72-20)
- Fan assembly
- Fan case
- Inlet cowl
- Thrust generation

## Key Integration Points

- **ATA-73**: Fuel control (FADEC)
- **ATA-74**: Ignition system
- **ATA-75**: Bleed air extraction
- **ATA-76**: Engine controls
- **ATA-77**: Engine indicating sensors
- **ATA-28**: Fuel supply
- **ATA-24**: Electrical power (starter, ignition)
- **ATA-29**: Hydraulic pump drive
- **ATA-36**: Pneumatic interfaces
- **ATA-92**: EWIS

## Performance Parameters

- **Thrust**: Per engine specification
- **N1/N2 Speeds**: Operating ranges defined
- **EGT Limits**: Maximum temperature limits
- **Fuel Flow**: Operating envelope

## Interface Matrix

See `INTERFACE_MATRIX/72↔73_74_75_76_77_28_24_29_36_92.csv`

## Subsystems

- [ATA-72-10 Core Engine](./SUBSYSTEMS/ATA-72-10_CORE_ENGINE/)
- [ATA-72-20 Fan/Propulsor](./SUBSYSTEMS/ATA-72-20_FAN_OR_PROPULSOR/)

---

**Last Updated**: 2024-01-15
