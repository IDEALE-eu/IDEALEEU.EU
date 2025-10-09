# ATA-38 Water/Waste - Integration View

## Overview

The Water/Waste system (ATA-38) manages the complete water lifecycle on the aircraft:
- Potable water storage and distribution
- Wastewater collection and treatment
- Closed-loop reclamation for circular economy
- Integration with cabin systems

## System Architecture

### Water Flow Diagram
```
Potable Water Tank 
  → Distribution → Galleys/Lavatories → Usage
  → Greywater Collection → Treatment → Quality Check
  → Reclaimed Water → [Reuse Loop or Disposal]
```

### Closed-Loop Reclamation
1. **Greywater Sources**:
   - Lavatory sinks
   - Galley wastewater
   - ECS condensate (ATA-21)
2. **Treatment Process**:
   - Filtration (sediment, activated carbon)
   - UV sterilization
   - Quality monitoring (turbidity, pH, microbiology)
3. **Reclaimed Water Uses**:
   - Toilet flushing (primary)
   - Cleaning (secondary)
   - Non-potable uses (tertiary)

### Key Components

| Component | Function | Location | Capacity |
|-----------|----------|----------|----------|
| Potable Water Tank | Fresh water storage | Aft cargo bay | 150-300 L |
| Waste Tank | Wastewater/sewage | Aft cargo bay | 150-300 L |
| Water Treatment Unit | Greywater processing | Equipment bay | 50 L/hr |
| Distribution Pumps | Pressurized distribution | Tanks | 2-5 L/min |
| Quality Sensors | Water quality monitoring | Treatment unit | N/A |

## Key Interfaces

### ATA-21 ECS
- **Condensate Recovery**: ECS pack condensate routed to treatment
- **Thermal Integration**: Waste heat from ECS for water heating
- **Humidity Control**: Cabin humidity affects condensate rate

### ATA-24 Electrical Power
- **Distribution Pumps**: 28 VDC pumps for potable/waste
- **Treatment System**: 115 VAC for UV lamps, heaters
- **Control Unit**: 28 VDC for system controller
- **Sensors**: 28 VDC for flow, level, quality sensors

### ATA-25 Furnishings
- **Galleys**: Potable water supply, drain connection
- **Lavatories**: Potable supply, greywater/blackwater drains
- **Water Heaters**: Hot water for galley/lavatory

### ATA-36 Pneumatic
- **Waste System Pressurization**: Pneumatic flush system
- **Tank Venting**: Waste tank pressure relief

### ATA-92 EWIS
- **Control Harnesses**: Water controller, valve actuators
- **Sensor Wiring**: Flow, level, temperature, quality sensors
- **Power Distribution**: Circuit protection

## Water Treatment Process

### Treatment Stages
| Stage | Technology | Purpose | Efficiency |
|-------|------------|---------|------------|
| Pre-filtration | Sediment filter | Remove particles > 50 μm | 95% |
| Carbon filtration | Activated carbon | Remove organics, chlorine | 90% |
| UV sterilization | UV-C lamp (254 nm) | Kill bacteria, viruses | 99.99% |
| Post-filtration | Fine filter | Polish water, remove residuals | 98% |
| Quality monitoring | Turbidity, pH, conductivity | Ensure safety | Continuous |

### Water Quality Standards
- **Potable**: WHO drinking water standards, FAR 25.1447
- **Reclaimed**: Class B reclaimed water (EPA standards)
- **Monitoring**: Continuous turbidity, periodic microbiology

## Subsystems

### ATA-38-00 Potable Water
- Potable water tank and distribution
- Pressurization system
- Quality monitoring
- See [SUBSYSTEMS/ATA-38-00_POTABLE_WATER/](SUBSYSTEMS/ATA-38-00_POTABLE_WATER/)

### ATA-38-10 Waste Treatment/Disposal
- Waste tank and collection
- Greywater treatment unit
- Discharge/disposal system
- See [SUBSYSTEMS/ATA-38-10_WASTE_TREATMENT_DISPOSAL/](SUBSYSTEMS/ATA-38-10_WASTE_TREATMENT_DISPOSAL/)

## Performance Targets

| Parameter | Target | Margin |
|-----------|--------|--------|
| Potable water capacity | 2 L/person/hour | 150-300 L total |
| Treatment rate | 50 L/hr | Meet peak demand |
| Reclamation efficiency | > 70% | Greywater recovery |
| Water quality | Meets WHO standards | Continuous monitoring |
| System weight | < 150 kg dry | Excluding water |

## Integration with Circular Systems

### Closed-Loop Benefits
- **Water Savings**: 50-70% reduction in fresh water needed
- **Weight Reduction**: Smaller tanks, less water carried
- **Environmental**: Reduced wastewater discharge
- **Operational**: Extended range on long flights

### Material Circularity
- **Tanks**: Stainless steel or aluminum - recyclable
- **Piping**: PEX or stainless - recyclable
- **Filters**: Replaceable cartridges - partially recyclable
- **UV Lamps**: Mercury-free LEDs - recyclable electronics

### End-of-Life
- **System Decommissioning**: Drain, sanitize, dismantle
- **Component Refurbishment**: Pumps, valves, sensors - test & reuse
- **Material Recovery**: 85%+ recyclability target

## Safety and Hygiene

### Hazard Mitigation
- **Microbial Contamination**: UV sterilization, quality monitoring
- **Chemical Contamination**: Activated carbon filtration
- **Cross-Contamination**: Separate potable/reclaimed systems
- **Backflow Prevention**: Check valves, air gaps

### Maintenance
- **Filter Replacement**: Every 6 months or per indicators
- **UV Lamp Replacement**: Every 12 months or per intensity
- **Tank Sanitization**: Annual deep cleaning
- **Quality Testing**: Monthly microbiology sampling

## Digital Thread Links

- **MBSE Model**: [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../../04-DIGITAL_THREAD/MBSE_BINDINGS.md)
- **Digital Twin**: [04-DIGITAL_THREAD/TWIN_ANCHORS.md](../../04-DIGITAL_THREAD/TWIN_ANCHORS.md)
- **Telemetry**: [04-DIGITAL_THREAD/DATA_CONTRACTS/](../../04-DIGITAL_THREAD/DATA_CONTRACTS/)

## Compliance

- **FAR 25.1447**: Water systems equipment
- **EPA Guidelines**: Reclaimed water standards
- **WHO Standards**: Drinking water quality
- **DO-160**: Environmental testing
- **NSF/ANSI 55**: UV drinking water treatment

## References

- ATA iSpec 2200 Chapter 38
- SAE AIR1539: Aircraft Potable Water Systems
- [02-INTERFACES/INTERFACE_MATRIX.csv](../../02-INTERFACES/INTERFACE_MATRIX.csv)
- [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
