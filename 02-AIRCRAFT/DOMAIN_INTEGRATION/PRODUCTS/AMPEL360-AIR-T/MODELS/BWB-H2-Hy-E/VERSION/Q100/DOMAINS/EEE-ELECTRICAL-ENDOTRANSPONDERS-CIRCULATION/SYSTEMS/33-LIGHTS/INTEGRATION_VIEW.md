# 33-LIGHTS — Integration View
Descripción breve del encaje funcional, dependencias y modos.

## System Overview

ATA 33 - Aircraft Lighting Systems provides all required lighting for the BWB-H2-Hy-E aircraft including:
- External navigation and anti-collision lights
- Landing, taxi, and takeoff lights
- Logo, wing, and inspection lights
- Emergency lighting and markings

## Functional Dependencies

### Power Supply
- Primary power from 24-ELECTRICAL-POWER (28VDC)
- Emergency backup from battery systems
- Ground power interface capability

### Control Interfaces
- Flight deck lighting controls (ATA 31)
- Cabin lighting controls (ATA 25)
- Auto-dimming based on ambient light sensors
- Emergency activation from fire detection (ATA 26)

### Integration Points
- Wiring harness through ATA 92 (EWIS)
- Structural mounting points (ATA 51, 53, 57)
- Environmental sealing requirements (ATA 30)

## Operating Modes

1. **Normal Operations**: All lights per flight phase requirements
2. **Emergency Mode**: Critical lights only, battery backup
3. **Ground Mode**: Reduced lighting, external power
4. **Maintenance Mode**: Full system access, test patterns

## System Architecture

- LED-based lighting throughout for efficiency
- Digital dimming and control via ARINC 429
- Distributed control units in electrical panels (ATA 39)
- Self-test and health monitoring capabilities
