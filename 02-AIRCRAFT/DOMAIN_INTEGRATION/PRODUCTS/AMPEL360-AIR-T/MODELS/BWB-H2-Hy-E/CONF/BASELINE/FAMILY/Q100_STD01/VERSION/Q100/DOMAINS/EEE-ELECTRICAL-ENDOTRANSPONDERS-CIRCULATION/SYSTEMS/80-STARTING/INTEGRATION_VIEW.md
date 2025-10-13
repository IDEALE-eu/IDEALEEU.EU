# 80-STARTING — Integration View
Descripción breve del encaje funcional, dependencias y modos.

## System Overview

ATA 80 - Engine Starting provides all electrical and control systems required for starting the propulsion system of the BWB-H2-Hy-E aircraft including:
- Starter-Generator units (PMSM-based)
- Start Power Electronics (SPCU)
- Start sequence control and interfaces

## Functional Dependencies

### Power Supply
- High-voltage DC power from 24-ELECTRICAL-POWER (typically 270VDC)
- Emergency start capability from battery systems
- Ground power start capability

### Control Interfaces
- Engine control system (ATA 73 - FADEC)
- Propulsion system control (ATA 76)
- Flight deck start controls (ATA 31)
- Health monitoring (ATA 45)

### Integration Points
- Mechanical interface to engine/propulsion (ATA 71, 72)
- Fuel cell system coordination (ATA 28 H₂ systems)
- Wiring harness through ATA 92 (EWIS)
- Thermal management during start (ATA 21)

## Operating Modes

1. **Ground Start**: External power or APU-assisted start
2. **Air Start**: In-flight engine restart capability
3. **Cross-bleed Start**: Start using operating engine
4. **Emergency Start**: Battery-only start sequence
5. **Generator Mode**: After start, unit operates as generator

## System Architecture

- **Starter-Generators (SG)**: Permanent Magnet Synchronous Motor (PMSM) based units
- **Start Power Control Unit (SPCU)**: High-power electronics for start sequence
- **Sequence Control**: Coordinated start logic with FADEC and fuel cell systems
- **Health Monitoring**: Temperature, speed, current monitoring during start
- **Safety Interlocks**: Ground safety, fuel flow, ignition coordination

## Special Considerations for H₂ Propulsion

- Coordination with fuel cell stack warmup
- H₂ flow management during start
- Thermal management of cryogenic H₂ systems
- Safety interlocks for H₂ systems
