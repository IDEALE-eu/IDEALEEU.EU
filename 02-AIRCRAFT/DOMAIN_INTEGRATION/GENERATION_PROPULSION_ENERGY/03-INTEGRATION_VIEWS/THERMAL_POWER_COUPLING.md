# Thermal-Power Coupling Integration

## Overview

This document describes the thermal-power coupling relationships between propulsion, energy generation, and aircraft systems, including heat generation, dissipation, and management.

## Thermal Sources and Sinks

### Heat Generation Sources

#### Engine Core (ATA-72)
- **Combustion Heat**: Primary thermal energy source (1200-1800°C)
- **Compression Heat**: Air heated through compression work
- **Friction Heat**: Bearings, seals, mechanical components
- **Exhaust Heat**: High-temperature exhaust gases (500-700°C)

#### Oil System (ATA-79)
- **Bearing Friction**: Heat generated in engine bearings
- **Gearbox Losses**: Accessory gearbox heat
- **Pump Work**: Hydraulic energy conversion to heat

#### Electrical Systems (ATA-24)
- **Generator Losses**: I²R losses in windings, eddy current losses
- **Power Electronics**: TRU, inverter, converter losses
- **Bus Bar Heating**: Resistive losses in distribution

#### Bleed Air (ATA-75)
- **High-Pressure Bleed**: 250-450°C from HP compressor
- **Low-Pressure Bleed**: 150-250°C from LP compressor
- **Compression Work**: Temperature rise through compression

### Heat Sinks and Cooling

#### Fuel Cooling (ATA-28)
- **Oil-Fuel Heat Exchanger**: Engine oil cooled by fuel
- **Hydraulic-Fuel Heat Exchanger**: Hydraulic oil cooled by fuel
- **IDG Oil Cooling**: Generator oil cooled by fuel (if applicable)
- **Fuel Temperature Rise**: 20-40°C typical

#### Air Cooling
- **Ram Air**: Ambient air for heat exchangers
- **Fan Air**: Bypass air used for nacelle cooling
- **Bleed Air Cooling**: Pre-cooler for ECS air

#### Liquid Cooling (if applicable)
- **Coolant Loops**: Dedicated cooling systems
- **Cold Plates**: Electronics cooling

## Thermal Coupling Interfaces

### Bleed Air ↔ Oil Cooling (ATA-75 ↔ ATA-79)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Engine Oil  │──────►│ Oil-Air HX   │◄──────│  Bleed Air   │
│  (Hot: 140°C)│       │              │       │ (Cool side)  │
└──────────────┘       └──────────────┘       └──────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │ Cooled Oil   │
                       │ (110°C)      │
                       └──────────────┘
```

**Coupling Parameters**:
- Oil inlet temperature: 130-150°C
- Oil outlet temperature: 100-120°C
- Bleed air temperature: 200-300°C (precooled)
- Heat transfer rate: 50-100 kW

### Fuel Cooling ↔ Oil/Hydraulic (ATA-28 ↔ ATA-79/29)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Engine Oil  │──────►│ Fuel-Oil HX  │◄──────│     Fuel     │
│  (Hot: 140°C)│       │              │       │  (Cool: 20°C)│
└──────────────┘       └──────────────┘       └──────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │  Warm Fuel   │
                       │  (60°C)      │
                       └──────────────┘
```

**Coupling Parameters**:
- Oil inlet temperature: 130-150°C
- Oil outlet temperature: 100-120°C
- Fuel inlet temperature: -40 to +40°C (ambient dependent)
- Fuel outlet temperature: 40-80°C
- Heat transfer rate: 100-200 kW

**Fuel Temperature Limits**:
- Maximum: 90°C (prevents fuel system issues)
- Minimum: -40°C (fuel freezing point dependent on type)

### Bleed Air ↔ ECS (ATA-75 ↔ ATA-21)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  HP Bleed    │──────►│ Precooler    │◄──────│   Fan Air    │
│  (Hot: 400°C)│       │              │       │  (Ambient)   │
└──────────────┘       └──────────────┘       └──────────────┘
        │                      │
        │                      ▼
        │              ┌──────────────┐
        └─────────────►│     ACM      │
                       │ (Air Cycle   │
                       │  Machine)    │
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │  Cabin Air   │
                       │  (20-25°C)   │
                       └──────────────┘
```

**Coupling Parameters**:
- Bleed air inlet: 200-450°C, 30-60 psi
- Precooled air: 150-200°C
- Final cabin supply: 10-30°C
- Heat removed: 200-400 kW (depending on aircraft size and conditions)

### Exhaust Thermal Management (ATA-78 ↔ ATA-21)

**Hot Exhaust Interfaces**:
- Exhaust nozzle temperatures: 500-700°C
- Thrust reverser actuation: High-temperature environment
- Nacelle cooling: Prevent structural damage
- APU exhaust: Tail cone thermal protection

**Cooling Methods**:
- Insulation blankets
- Cooling air flow
- Heat shields
- Thermal barriers

## Power-Thermal Interaction

### Generator Cooling (ATA-24)

**Cooling Requirements**:
- Generator operating temperature: 150-200°C
- Oil cooling for integrated drive generators (IDG)
- Fan cooling for direct-drive generators
- Heat dissipation: 5-10 kW per generator

**Cooling Methods**:
1. **Oil Cooling**: IDG oil cooled via fuel-oil heat exchanger
2. **Air Cooling**: Ram air or fan air for generator cooling
3. **Combined**: Oil for rotor, air for stator

### Power Electronics Cooling (ATA-24)

**Components Requiring Cooling**:
- TRUs (Transformer Rectifier Units)
- Static Inverters
- DC-DC Converters
- Energy Management Controller

**Heat Dissipation**:
- TRU: 2-5 kW heat (5-10% losses)
- Inverter: 1-3 kW heat (5-8% losses)
- DC-DC Converters: 0.5-2 kW heat (5-10% losses)

**Cooling Methods**:
- Cold plates with liquid cooling
- Forced air cooling
- Natural convection (low-power units)

### APU Thermal Management (ATA-49)

**APU Heat Generation**:
- Core temperature: 600-800°C
- Oil temperature: 100-130°C
- Exhaust temperature: 400-600°C
- Compartment heat: Requires cooling/ventilation

**Cooling Systems**:
- APU oil cooler (fuel-cooled or air-cooled)
- Compartment ventilation
- Exhaust duct insulation
- Fire detection/suppression

## Thermal Protection and Limits

### Component Temperature Limits

| Component | Operating Range | Maximum Limit | Critical Action |
|-----------|----------------|---------------|-----------------|
| Engine Oil | 80-150°C | 165°C | Engine shutdown if exceeded |
| Fuel | -40 to 80°C | 90°C | Reduce heat load, monitor |
| Generator | 120-180°C | 200°C | Generator trip offline |
| TRU | 50-100°C | 120°C | Load shedding, fault isolation |
| Bleed Air (delivered) | 180-220°C | 260°C | Bleed valve closure |
| APU Oil | 80-130°C | 150°C | APU shutdown |
| Hydraulic Fluid | 40-90°C | 120°C | System degradation warning |

### Thermal Monitoring

**Sensors and Indication**:
- Oil temperature sensors (ATA-79)
- Fuel temperature sensors (ATA-28)
- Bleed air temperature sensors (ATA-75)
- EGT sensors (ATA-77)
- Generator temperature sensors (ATA-24)
- APU compartment temperature (ATA-49)

**Cockpit Indications**:
- EICAS cautions/warnings for over-temperature
- System synoptic pages showing temperatures
- Trend monitoring for predictive maintenance

## Thermal Efficiency Optimization

### Waste Heat Recovery (Future Consideration)

**Potential Applications**:
- Cabin heating from bleed air or exhaust
- Fuel pre-heating in cold conditions
- Battery thermal management
- De-icing systems

### Heat Load Reduction Strategies

**Operational**:
- Reduce electrical load (shed non-essential systems)
- Reduce bleed air extraction (use electric ECS if available)
- Optimize generator loading
- APU usage minimization

**Design**:
- More efficient power electronics (reduced losses)
- Better insulation (reduced heat transfer)
- Improved heat exchangers (better efficiency)
- Electric systems replacing bleed air systems (more electric aircraft)

## System Integration Scenarios

### High-Power, High-Temperature Scenario
**Conditions**: Takeoff on hot day, full systems operating

**Thermal Challenges**:
- Maximum bleed air extraction (anti-ice + ECS)
- Maximum electrical load
- High ambient temperature (reduces cooling effectiveness)
- Engine at maximum power (high heat generation)

**Management**:
- Fuel cooling absorbs oil and hydraulic heat
- Bleed air precooler uses maximum fan air
- Generator loading balanced
- APU may supplement for ground ops

### Cold Start Scenario
**Conditions**: Engine start in cold environment

**Thermal Challenges**:
- Cold fuel (high viscosity)
- Cold oil (high viscosity)
- Engine thermal shock
- Battery capacity reduced in cold

**Management**:
- Fuel and oil heaters (if equipped)
- Extended warm-up period
- APU provides warm bleed air for engine start
- Pre-heating systems activated

## Digital Twin Integration

### Thermal Model KPIs
- Component temperatures (real-time)
- Heat exchanger effectiveness
- Cooling system efficiency
- Thermal margin to limits
- Predicted component life (temperature-dependent)

### Predictive Maintenance
- Oil cooler fouling detection
- Heat exchanger degradation
- Insulation breakdown
- Bearing wear (temperature-based)

## Related Documents

- [Energy Flow Integration](./ENERGY_FLOW.md)
- [Propulsion Chain Integration](./PROPULSION_CHAIN.md)
- [ATA-79 Oil System](../01-SYSTEMS/ATA-79_OIL/INTEGRATION_VIEW.md)
- [ATA-75 Bleed Air](../01-SYSTEMS/ATA-75_BLEED_AIR/INTEGRATION_VIEW.md)

---

**Last Updated**: 2024-01-15
