# 39-ELECTRICAL_PANELS — Integration View
Descripción breve del encaje funcional, dependencias y modos.

## System Overview

ATA 39 - Electrical Panels and Distribution Boxes provides centralized and distributed electrical distribution and control for the BWB-H2-Hy-E aircraft including:
- Primary Distribution Panels (PDP)
- Power Electronics Bays (PEB)
- Secondary panels and junction boxes
- Remote Power Distribution Units (RPDU)

## Functional Dependencies

### Power Input
- Primary power from 24-10 (Generation sources)
- Distribution coordination with 24-30 (Bus distribution)
- Protection devices from 24-50 (SSPC, Breakers)

### Control Interfaces
- Flight deck panel controls (ATA 31)
- System health monitoring (ATA 45)
- Thermal management interface (ATA 21, 94)
- Load management system (24-70)

### Integration Points
- Structural mounting and vibration isolation (ATA 51, 53)
- Cooling air interface (ATA 21, 94)
- Wiring harness through ATA 92 (EWIS)
- EMI/EMC shielding requirements

## Operating Modes

1. **Normal Operations**: Full distribution capability, all panels active
2. **Degraded Mode**: Reduced capacity, load shedding active
3. **Emergency Mode**: Essential systems only, emergency power
4. **Ground/Maintenance**: External power, test configurations

## System Architecture

- Distributed architecture with primary and secondary panels
- Remote Power Distribution Units (RPDUs) for zone-based distribution
- Integrated health monitoring and diagnostics
- Active thermal management with forced cooling
- Modular design for maintenance and upgrades
