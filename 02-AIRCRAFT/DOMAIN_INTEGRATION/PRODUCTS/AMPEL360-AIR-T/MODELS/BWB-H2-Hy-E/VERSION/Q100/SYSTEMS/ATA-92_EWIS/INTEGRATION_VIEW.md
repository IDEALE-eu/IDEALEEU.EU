# ATA-92 EWIS — Integration View

## Functional Overview
Electrical Wiring Interconnection System for BWB H₂ hybrid-electric aircraft. Manages all electrical wiring, harnesses, and interconnections across systems.

## Key Dependencies
All ATA chapters rely on ATA-92 for:
- Power distribution wiring
- Signal and data bus wiring
- Sensor and actuator connections
- Grounding and bonding
- EMI/EMC protection

## Critical Interfaces
- **ATA-21**: Thermal management sensors and controls
- **ATA-24**: Power distribution buses and feeders
- **ATA-28**: H₂ system sensors and safety interlocks
- **ATA-42**: IMA data buses and power
- **ATA-71**: Propulsion system power and control
- **ATA-73**: FADEC control and monitoring

## Design Principles
- SW colocated with host LRU (software in 42/73)
- Separation of power and signal wiring
- Redundancy for critical systems
- H₂ safety zone segregation
- EMI/EMC compliance

## Integration Points
EWIS is referenced by all systems but does not contain software or application logic.
