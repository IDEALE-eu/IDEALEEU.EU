# PPP-PROPELLERS-PROPELLENTS-PROPULSION Domain

**Architecture:** BWB-H2-Hy-E • **Family:** Q100_STD01

## Purpose

This domain manages propellers, propellents, propulsion systems, and aircraft fuel systems. It encompasses all aspects of aircraft propulsion from fuel storage and distribution to engine systems and propeller operations.

## Structure

- `SYSTEMS/` - Contains ATA chapters and their systems
  - Each system follows the TFA structure with PLM/CAx and CONF/BASELINE hierarchies

## ATA Chapters

This domain covers the following ATA chapters:
- **ATA-28** - Fuel System (including H₂)
- **ATA-49** - APU (Auxiliary Power Unit)
- **ATA-61** - Propellers/Propulsors
- **ATA-70** - Powerplant Practices
- **ATA-71** - Power Plant
- **ATA-72** - Engine
- **ATA-73** - Engine Fuel & Control
- **ATA-74** - Ignition
- **ATA-75** - Engine Bleed Air
- **ATA-76** - Engine Controls
- **ATA-77** - Engine Indicating
- **ATA-78** - Exhaust
- **ATA-79** - Oil (Lubrication)
- **ATA-80** - Starting

## Integration

This domain integrates with:
- MEC-MECHANICAL-SYSTEMS-MODULES (mechanical systems)
- EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION (power distribution)
- LCC-LINKAGES-CONTROL-COMMUNICATIONS (control systems)

## Rules

- Follow TFA structure for all artifacts
- Maintain traceability through metadata files
- Use make commands for structure management

> Owner: DomainBoard-PPP • Status: InWork • Year: 2025
