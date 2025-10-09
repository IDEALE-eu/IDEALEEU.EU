# ATA-21 Air Conditioning - Integration View

## Overview

The Air Conditioning system (ATA-21) provides thermal management for the aircraft cabin and equipment bays through:
- Environmental Control Packs (ECS packs)
- Temperature control systems
- Pressurization control
- Heat rejection loops

## System Architecture

### Heat Rejection Loop
- **Primary Loop**: Cabin air → heat exchangers → distribution
- **Secondary Loop**: Equipment cooling → cold plates → heat exchangers
- **Waste Heat**: Rejected to ambient through ram air or fuel heat sink

### Pack Flows
- **Fresh Air Supply**: Bleed air (ATA-36) → packs → cabin
- **Recirculation**: Cabin air → HEPA filters → mixing chamber
- **Ventilation Rate**: 15-20 CFM per occupant (FAR 25.831)

### Cabin Thermal Loads
| Load Type | Typical Value | Notes |
|-----------|---------------|-------|
| Occupant metabolic | 100 W/person | Seated, light activity |
| Solar radiation | 500-1500 W/m² | Varies by altitude, latitude |
| Equipment | 5-15 kW | Avionics, galley, lighting |
| Structural conduction | Variable | Fuselage skin temperature |

## Key Interfaces

### ATA-24 Electrical Power
- **ECS Controllers**: 28 VDC control power
- **Pack Motors**: 115 VAC 3-phase, 400 Hz
- **Fans/Pumps**: Variable frequency drives

### ATA-28 Fuel/H₂
- **Thermal Integration**: ECS heat rejection to H₂ boil-off cooling
- **Fuel Heat Sink**: Heat exchanger for high-altitude cruise
- **Boil-off Management**: Cabin heat used to pre-condition H₂

### ATA-36 Pneumatic
- **Bleed Air**: Engine bleed or APU for pack operation
- **Precooler**: Ram air or fuel for bleed air cooling
- **Pressure Regulation**: PRV for cabin pressurization

### ATA-38 Water/Waste
- **Humidity Control**: Condensate from air conditioning
- **Potable Cooling**: Chilled water for galley refrigeration
- **Waste Heat**: Water heating from equipment cooling loop

### ATA-92 EWIS
- **Control Harnesses**: Pack controllers, zone controllers
- **Sensor Wiring**: Temperature, pressure, flow sensors
- **Power Distribution**: Circuit protection, EMI filtering

## Integration with Circular Systems

### Closed-Loop Thermal Management
1. **Heat Recovery**: Waste heat from avionics used for cabin heating
2. **Condensate Reclaim**: ECS condensate routed to water treatment (ATA-38)
3. **Energy Efficiency**: Variable flow control, demand-based operation

### Material Considerations
- **Heat Exchangers**: Aluminum alloys (recyclable)
- **Ducting**: Composites with recyclable resins
- **Insulation**: Non-toxic, recyclable materials

## Subsystems

### ATA-21-00 Environmental Control Packs
- Pack assembly (heat exchangers, turbines, compressors)
- Pack controller LRU
- See [SUBSYSTEMS/ATA-21-00_ENV_CONTROL_PACKS/](SUBSYSTEMS/ATA-21-00_ENV_CONTROL_PACKS/)

### ATA-21-10 Temperature Control
- Zone temperature controllers
- Mix valves and actuators
- See [SUBSYSTEMS/ATA-21-10_TEMPERATURE_CONTROL/](SUBSYSTEMS/ATA-21-10_TEMPERATURE_CONTROL/)

### ATA-21-20 Pressurization Control
- Cabin pressure controller
- Outflow valves
- See [SUBSYSTEMS/ATA-21-20_PRESSURIZATION_CONTROL/](SUBSYSTEMS/ATA-21-20_PRESSURIZATION_CONTROL/)

## Performance Targets

| Parameter | Target | Margin |
|-----------|--------|--------|
| Cabin temperature | 22±2°C | ±5°C operating range |
| Cabin pressure | 8,000 ft equiv. @ FL410 | Max 10,000 ft |
| Fresh air flow | 20 CFM/person | Min 15 CFM/person |
| Pack efficiency | COP > 2.5 | Ground operation |

## Digital Thread Links

- **MBSE Model**: [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../../04-DIGITAL_THREAD/MBSE_BINDINGS.md)
- **Digital Twin**: [04-DIGITAL_THREAD/TWIN_ANCHORS.md](../../04-DIGITAL_THREAD/TWIN_ANCHORS.md)
- **Telemetry**: [04-DIGITAL_THREAD/DATA_CONTRACTS/](../../04-DIGITAL_THREAD/DATA_CONTRACTS/)

## Compliance

- **CS-25.831**: Ventilation requirements
- **CS-25.832**: Cabin ozone concentration
- **CS-25.841**: Pressurized cabins
- **DO-160**: Environmental testing

## References

- ATA iSpec 2200 Chapter 21
- SAE AIR1168/8: Environmental Control Systems
- [02-INTERFACES/INTERFACE_MATRIX.csv](../../02-INTERFACES/INTERFACE_MATRIX.csv)
- [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
