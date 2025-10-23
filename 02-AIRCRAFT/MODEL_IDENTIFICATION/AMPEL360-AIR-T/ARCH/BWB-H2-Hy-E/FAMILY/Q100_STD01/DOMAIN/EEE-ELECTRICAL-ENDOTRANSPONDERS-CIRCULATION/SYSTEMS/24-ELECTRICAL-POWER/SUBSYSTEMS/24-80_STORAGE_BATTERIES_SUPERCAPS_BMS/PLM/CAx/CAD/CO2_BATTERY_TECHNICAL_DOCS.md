# CO₂ Endocircular Battery System - Technical Documentation

## Overview

The **CO₂ Endocircular Battery System** is a closed-loop energy storage solution that uses carbon dioxide (CO₂) as the working fluid. Energy is stored by maintaining CO₂ in solid (dry ice) or liquid form, and recovered through controlled phase transitions and expansion cycles.

### Key Characteristics

- **Closed System**: No CO₂ venting - mass is conserved throughout operation
- **Phase-Change Storage**: Exploits latent heat of sublimation (571 kJ/kg)
- **Multiple Cycle Options**: Sublimation, supercritical Brayton, or CAES-like pneumatic
- **Cryogenic Operation**: Storage temperatures from -80°C to +31°C (liquid/solid), or supercritical above 31.04°C
- **High Energy Density**: ~247 kWh/m³ thermal, 20-70 Wh/kg electrical (system-dependent)

## Thermodynamic Background

### CO₂ Phase Diagram

| Parameter | Value | Notes |
|-----------|-------|-------|
| Triple Point | -56.6°C, 5.185 bar | Solid/liquid/gas equilibrium |
| Critical Point | 31.04°C, 73.8 bar | Supercritical threshold |
| Sublimation (1 atm) | -78.5°C | Direct solid → gas |
| Latent Heat (sublimation) | 571 kJ/kg | Energy for phase change |
| Dry Ice Density | 1560 kg/m³ | Solid CO₂ |
| Liquid Density | 1178 kg/m³ | At 0°C, ~35 bar |

### Phase Transitions

The system exploits three main phase transitions:

1. **Sublimation** (solid → gas): Maximum latent heat, simplest operation
2. **Evaporation** (liquid → gas): Moderate latent heat, requires pressure control
3. **Supercritical transition**: Continuous properties, high efficiency potential

## System Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                   ENDOCIRCULAR CO₂ BATTERY                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐    ┌──────────┐    ┌─────────┐             │
│  │ Storage   │ -> │ Evaporator│ -> │ Expander│ -> Power   │
│  │ Tank      │    │ /Heater   │    │ /Turbine│    Output  │
│  │ (Solid/   │    └──────────┘    └─────────┘             │
│  │  Liquid)  │           ▲             │                   │
│  └───────────┘           │             ▼                   │
│       ▲                  │      ┌──────────┐               │
│       │                  └──────│Recuperator│               │
│       │                         └──────────┘               │
│       │                              │                     │
│  ┌─────────┐                         ▼                     │
│  │ Recharge│ <-  ┌──────────┐  ┌──────────┐               │
│  │ System  │ <- │Compressor│<-│  Cooler  │               │
│  │(Liquef.)│    └──────────┘  └──────────┘               │
│  └─────────┘                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Component Specifications

#### 1. Storage Tank
- **Function**: Hold CO₂ in solid, liquid, or supercritical phase
- **Materials**: Cryogenic stainless steel (316L) or aluminum alloys
- **Insulation**: Multi-layer vacuum insulation (MLI) or foam
- **Pressure rating**: 
  - Solid/liquid storage: 1-60 bar (typical 35 bar at 0°C for liquid)
  - sCO₂ loop hardware: 80-200 bar (MAWP per component)
- **Temperature range**: -90°C to +40°C

#### 2. Evaporator/Heater
- **Function**: Supply heat for sublimation/evaporation
- **Heat sources**: Waste heat, ambient, solar, or electric
- **Heat exchanger**: Shell-and-tube or plate design
- **Power**: 10-100 kW thermal (application dependent)

#### 3. Expander/Turbine
- **Function**: Convert pressure/thermal energy to mechanical work
- **Types**: Radial turbine, scroll expander, or reciprocating piston
- **Efficiency**: 70-85% typical
- **Pressure ratio**: 5:1 to 10:1
- **Power output**: 1-50 kW electrical (with generator)

#### 4. Recuperator
- **Function**: Preheat incoming CO₂ with warm exhaust
- **Effectiveness**: 80-90%
- **Type**: Counter-flow heat exchanger
- **Benefit**: +20-40% efficiency improvement

#### 5. Recharge System (Compressor + Liquefaction)
- **Function**: Return CO₂ to solid/liquid state
- **Components**: Multi-stage compressor, aftercooler, expansion valve
- **COP**: 0.8-2.0 (lower for deep cryogenic solidification, higher for liquid-only cycles)
- **Energy input**: 50-125% of electrical output (system and temperature dependent)

#### 6. Controls & Instrumentation
- **Pressure sensors**: Cryogenic-rated, ±0.5% accuracy
- **Temperature sensors**: RTD or thermocouple, -100°C to +100°C
- **Flow meters**: Mass flow or volumetric
- **Valves**: Cryogenic ball or gate valves, pneumatic actuation
- **Safety**: Relief valves, burst discs, CO₂ detectors

## Operating Cycles

### 1. Sublimation + Expander Cycle

**Best for**: Simplicity, lower capital cost, modest efficiency

**Process**:
1. Solid CO₂ stored at ~-80°C, atmospheric pressure
2. Heat added → sublimation → gas at ~10 bar
3. Gas expanded through turbine → mechanical work
4. Exhaust recirculated through recuperator
5. Compressed and cooled → returned to solid state

**Performance**:
- Thermal efficiency: 15-25%
- Electrical efficiency: 12-20%
- Round-trip efficiency: 20-35%
- Specific energy: 20-35 Wh/kg

**Advantages**:
- Simple operation
- Lower pressure requirements
- Easy storage (dry ice)

**Challenges**:
- Lower efficiency
- Solid handling complexity
- High recharge energy

### 2. Supercritical CO₂ (sCO₂) Brayton Cycle

**Best for**: High efficiency, stationary applications, heat availability

**Process**:
1. CO₂ stored above critical point (>31.04°C, >73.8 bar)
2. Heated to 350-550°C (heat source dependent)
3. Expanded through high-efficiency turbine
4. Recuperator preheats incoming fluid
5. Cooled and recompressed for storage

**Performance**:
- Thermal efficiency: 35-55%
- Electrical efficiency: 30-50%
- Round-trip efficiency: 40-60%
- Specific energy: 50-80 Wh/kg

**Advantages**:
- High efficiency (approaching gas turbines)
- Compact turbomachinery
- Good part-load performance

**Challenges**:
- High operating pressures
- Requires high-temperature heat source
- More complex control

### 3. CAES-like Pneumatic Cycle

**Best for**: Good round-trip efficiency, thermal management

**Process**:
1. CO₂ compressed and cooled → liquid storage
2. Heat stored separately during compression
3. Liquid evaporated and expanded
4. Stored heat reintroduced during expansion
5. Gas returned to liquid by cooling

**Performance**:
- Thermal efficiency: 40-50%
- Electrical efficiency: 35-45%
- Round-trip efficiency: 50-70% (with thermal storage)
- Specific energy: 40-70 Wh/kg

**Advantages**:
- Higher round-trip efficiency
- Better thermal integration
- Scalable

**Challenges**:
- Requires thermal storage
- More complex system
- Higher capital cost

## Performance Metrics

### Energy Calculations

#### Thermal Energy Stored
```
E_thermal = m_CO2 × L_sublimation
          = m_CO2 × 571 kJ/kg
          = m_CO2 × 0.1586 kWh/kg
```

Example: 100 kg CO₂ → 15.86 kWh thermal

#### Electrical Energy Recoverable
```
E_electrical = E_thermal × η_cycle × η_generator
             = E_thermal × η_overall
```

Example (15% overall efficiency): 15.86 kWh × 0.15 = 2.38 kWh electrical

#### Volumetric Energy Density
```
ρ_energy = E_thermal / V_storage
         = (m_CO2 × 0.1586 kWh/kg) / (m_CO2 / 1560 kg/m³)
         = 247.4 kWh/m³ (thermal)
```

#### Specific Energy (Gravimetric)
```
e_specific = E_electrical / m_CO2
```

Typical range: 20-70 Wh/kg (system-dependent)

### Efficiency Relationships

#### Carnot Efficiency (Theoretical Maximum)
```
η_Carnot = 1 - (T_cold / T_hot)
```

Example (80°C hot, 25°C cold):
```
η_Carnot = 1 - (298.15 K / 353.15 K) = 15.6%
```

#### Actual Cycle Efficiency
```
η_actual = η_Carnot × η_component × η_system
```

Where:
- η_component = expander, recuperator, etc.
- η_system = piping losses, controls, etc.

#### Round-Trip Efficiency
```
η_roundtrip = E_out / E_in
            = (η_discharge × E_stored) / (E_stored / COP_recharge)
            = η_discharge × COP_recharge
```

Example:
- Discharge efficiency: 15%
- Liquefaction COP: 1.5
- Round-trip: 0.15 × 1.5 = 22.5%

## Safety Considerations

### Hazards

1. **Asphyxiation**: CO₂ displaces oxygen
   - Mitigation: Ventilation, CO₂ detectors, alarms

2. **Pressure**: High-pressure storage and piping
   - Mitigation: Relief valves, burst discs, proper ratings

3. **Cryogenic**: Extreme cold temperatures
   - Mitigation: Insulation, PPE, material selection

4. **Solid Formation**: Blockage risk in piping
   - Mitigation: Keep solids in tank, P-T monitoring

### Design Limits

| Parameter | Safe Range | Notes |
|-----------|------------|-------|
| Maximum Pressure | < 200 bar | Typical high-pressure limit |
| Minimum Temperature | > -100°C | Embrittlement prevention |
| Solid Phase | Tank only | Avoid piping blockages |
| Mass Loss | < 1%/cycle | Verify closed system |

### Emergency Procedures

1. **Over-pressure**: Automatic relief valve activation
2. **Leak detection**: CO₂ sensors trigger system shutdown
3. **Loss of cooling**: Controlled pressure release or backup cooling
4. **Solid blockage**: Heat tracing, pressure/temperature monitoring

## Materials Selection

### Pressure Vessels
- **Stainless steel 316L**: Good corrosion resistance, cryogenic capable
- **Carbon steel**: Lower cost, insulated exterior
- **Aluminum alloys**: Lightweight, good for mobile applications

### Seals and Gaskets
- **Metal seals**: CF flanges for high vacuum/cryogenic
- **PTFE**: Good chemical resistance, limited cryogenic
- **PEEK**: Better cryogenic performance than PTFE
- **Avoid**: Standard elastomers (become brittle)

### Insulation
- **Vacuum**: Best performance, higher cost
- **Aerogel**: Excellent performance, flexible
- **Polyurethane foam**: Good cost/performance balance
- **Perlite**: Powder insulation for tanks

## Integration with Aircraft Systems

### Electrical Integration
- DC bus connection (270 VDC typical)
- Inverter for AC loads
- Battery management system (BMS) coordination
- Load prioritization logic

### Thermal Integration
- Waste heat capture from fuel cells/engines
- Cabin heating/cooling integration
- Recuperative heat exchange with ECS

### Weight Considerations
- Specific energy: 20-70 Wh/kg (vs. 150-250 Wh/kg Li-ion)
- Better for stationary or large-vehicle applications
- Volume often less critical than weight in aircraft

### Operational Modes

1. **Ground Power**: Pre-cooling, recharge from grid
2. **Takeoff/Climb**: Peak power supplementation
3. **Cruise**: Minimal discharge or recharge
4. **Descent**: Regenerative cooling, recharge opportunity
5. **Emergency**: Backup power for critical systems

## Maintenance and Lifecycle

### Inspection Intervals
- **Daily**: Visual inspection, leak checks
- **Monthly**: Pressure tests, instrumentation calibration
- **Annual**: Internal inspection, valve service, insulation check

### Consumables
- CO₂ makeup (minor, closed system)
- Compressor oil
- Desiccant (moisture removal)

### Expected Lifetime
- **Mechanical components**: 10-20 years
- **Pressure vessels**: 20-30 years
- **Insulation**: 15-25 years
- **Cycle life**: 5,000-10,000 cycles

## Comparison with Other Storage Technologies

| Technology | Specific Energy (Wh/kg) | Volumetric (Wh/L) | Efficiency (%) | Cost ($/kWh) | Lifetime (cycles) |
|------------|-------------------------|-------------------|----------------|--------------|-------------------|
| **CO₂ Battery** | 20-70 | 5-25 | 20-70 | 50-150 | 5k-10k |
| Li-ion | 150-250 | 250-700 | 85-95 | 100-300 | 1k-3k |
| Lead-Acid | 30-50 | 60-100 | 70-85 | 50-100 | 500-1k |
| CAES | 30-60 | 2-6 | 40-70 | 30-100 | 10k+ |
| Flywheel | 5-50 | 20-80 | 85-95 | 1000+ | 100k+ |

### Advantages of CO₂ Battery
- ✓ Non-flammable, safe chemistry
- ✓ Abundant, recyclable working fluid
- ✓ No rare materials
- ✓ Good cycle life
- ✓ Scalable from kW to MW

### Challenges
- ✗ Lower specific energy than Li-ion
- ✗ Cryogenic handling complexity
- ✗ Lower round-trip efficiency (simple cycles)
- ✗ Requires thermal management

## Future Developments

### Research Areas
1. **Advanced cycles**: Hybrid sCO₂/sublimation, multi-stage expansion
2. **Better materials**: High-strength composites, advanced insulation
3. **Higher efficiency**: Improved expanders, recuperators
4. **Integration**: Co-design with propulsion, thermal systems
5. **Control optimization**: AI/ML for cycle optimization

### Potential Improvements
- Specific energy: 80-120 Wh/kg (target)
- Round-trip efficiency: 60-80% (with advanced cycles)
- Cost reduction: $30-80/kWh (at scale)
- Lighter materials: -20-30% weight reduction

## References

### Standards
- ATA Chapter 24: Electrical Power Systems
- SAE ARP1476: Cryogenic Fluid Storage
- ASME BPVC Section VIII: Pressure Vessels
- ISO 9809: Gas cylinders - Design, construction and testing
- ISO 21013: Cryogenic vessels - Pressure-relief accessories for cryogenic service
- ISO 4126: Safety devices for protection against excessive pressure
- IEC 61508: Functional safety of electrical/electronic/programmable electronic safety-related systems
- DO-160: Environmental Conditions and Test Procedures for Airborne Equipment (aircraft applications)
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems

### Literature
- Dostal, V. (2004). "A Supercritical Carbon Dioxide Cycle for Next Generation Nuclear Reactors"
- Ahn, Y. et al. (2015). "Review of supercritical CO₂ power cycle technology"
- Zhang, X. et al. (2016). "Compressed air energy storage systems"

### Related Systems
- sCO₂ power cycles for nuclear/solar
- CO₂ heat pumps and refrigeration
- Cryogenic energy storage (LAES, LN₂)

---

**Document Version**: 1.0.0  
**Last Updated**: 2025-10-23  
**Author**: IDEALE-EU Energy Systems Team  
**Contact**: digitaltwin@idealeeu.eu
