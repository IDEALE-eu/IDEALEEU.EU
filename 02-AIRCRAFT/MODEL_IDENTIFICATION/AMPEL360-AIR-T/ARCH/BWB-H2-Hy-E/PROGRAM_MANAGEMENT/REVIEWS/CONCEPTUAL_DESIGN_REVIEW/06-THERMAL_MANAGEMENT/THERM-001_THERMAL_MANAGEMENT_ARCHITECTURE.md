# THERM-001: Thermal Management Architecture
## BWB-H2-HY-E-THERMAL-CRYO-001

**Deliverable ID**: THERM-001  
**Deliverable Type**: System Architecture  
**Version**: 1.0 (Template)  
**Date**: 2025-10-24  
**Status**: Draft Template  
**Owner**: Thermal Lead  
**UTCS**: TBD

---

## 1. Introduction

### 1.1 Purpose
Define the integrated thermal management architecture for the BWB-H2-Hy-E aircraft, addressing cryogenic hydrogen storage, propulsion system cooling, and aircraft-level thermal balance.

### 1.2 Scope
- System-level thermal integration
- Heat loads inventory
- Heat sinks inventory
- Thermal management strategy per flight phase
- Coolant selection and circulation paths

---

## 2. System-Level Thermal Integration Diagram

```
[System Thermal Architecture Diagram - TBD]

              ┌─────────────────────────────────────┐
              │   Aircraft Thermal Management      │
              └─────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    ┌────▼────┐        ┌─────▼──────┐      ┌─────▼──────┐
    │Cryogenic│        │ Propulsion │      │  Aircraft  │
    │  H2     │        │  Cooling   │      │  Systems   │
    │ Thermal │        │            │      │            │
    └─────────┘        └────────────┘      └────────────┘
```

### 2.1 Thermal Subsystems
1. **Cryogenic Hydrogen Thermal Management** (See THERM-002)
   - Tank insulation
   - Boil-off management
   - Pre-cooling systems

2. **Propulsion System Cooling** (See THERM-003)
   - Fuel cell cooling
   - Electric motor cooling
   - Power electronics cooling

3. **Aircraft Systems Thermal Management** (See THERM-004)
   - Environmental Control System (ECS)
   - Avionics cooling
   - Cabin thermal management

---

## 3. Heat Loads Inventory

### 3.1 Propulsion Heat Sources

| Component | Heat Load (kW) | Operating Temp (°C) | Cooling Method |
|-----------|----------------|---------------------|----------------|
| Fuel cells | [X] | [X] | Liquid coolant |
| Electric motors | [X] | [X] | Liquid coolant |
| Power electronics | [X] | [X] | Liquid/Air |
| Batteries | [X] | [X] | Liquid coolant |
| **Total Propulsion** | **[X]** | | |

### 3.2 Aircraft System Heat Sources

| System | Heat Load (kW) | Operating Temp (°C) | Cooling Method |
|--------|----------------|---------------------|----------------|
| Avionics | [X] | [X] | Air cooling |
| ECS compressor | [X] | [X] | Air cooling |
| Hydraulics (if used) | [X] | [X] | Oil cooling |
| Cabin heat load | [X] | [X] | ECS |
| Solar gain | [X] | | ECS |
| **Total Aircraft** | **[X]** | | |

### 3.3 Total Heat Rejection Requirements

| Flight Phase | Total Heat Load (kW) | Peak Load (kW) |
|--------------|----------------------|----------------|
| Ground | [X] | [X] |
| Taxi | [X] | [X] |
| Takeoff | [X] | [X] |
| Climb | [X] | [X] |
| Cruise | [X] | [X] |
| Descent | [X] | [X] |
| Approach/Landing | [X] | [X] |

---

## 4. Heat Sinks Inventory

### 4.1 Available Heat Sinks

| Heat Sink | Capacity (kW) | Availability | Temperature (°C) |
|-----------|---------------|--------------|------------------|
| Ram air | [X] | Flight only | Ambient - ISA |
| Cryogenic H2 | [X] | Continuous | -253°C → ambient |
| Cabin air | [X] | Continuous | 20-25°C |
| Fuel (H2) heat capacity | [X] | Continuous | -253°C → FC inlet |

### 4.2 Heat Sink Utilization Strategy
[Describe priority and usage of each heat sink]

#### Primary Heat Sinks by Flight Phase
| Phase | Primary Heat Sink | Secondary |
|-------|-------------------|-----------|
| Ground | Ram air (APU) / Ground cart | - |
| Taxi | Cryogenic H2 precooling | Cabin air |
| Takeoff | Ram air + H2 precooling | - |
| Climb | Ram air + H2 precooling | - |
| Cruise | Ram air + H2 precooling | - |
| Descent | Ram air | H2 precooling |
| Landing | Ram air + H2 precooling | - |

---

## 5. Thermal Management Strategy Per Flight Phase

### 5.1 Ground Operations
**Challenges**: 
- No ram air cooling
- High ambient temperatures possible
- Limited H2 precooling capacity

**Strategy**:
- Ground support air conditioning
- Minimize heat-generating systems
- Pre-cool H2 system before flight

### 5.2 Takeoff and Climb
**Challenges**:
- Maximum heat loads from propulsion
- High power electronics heat
- Limited ram air (low speed)

**Strategy**:
- Maximize H2 precooling utilization
- Thermal mass buffering
- Ram air cooling ramp-up

### 5.3 Cruise
**Challenges**:
- Sustained heat loads
- Long duration
- Optimal efficiency required

**Strategy**:
- Efficient ram air cooling
- H2 precooling for high-temperature loads
- Waste heat recovery for cabin heating
- Thermal equilibrium management

### 5.4 Descent
**Challenges**:
- Reduced heat loads
- Decreasing ram air
- Potential for regenerative heating

**Strategy**:
- Reduce cooling flow rates
- Manage thermal transients
- Maintain component temperatures within limits

---

## 6. Coolant Selection and Circulation Paths

### 6.1 Coolant Types

#### Primary Coolants
1. **Propulsion Liquid Coolant**
   - Type: [Glycol/Water mix / PAO / Specialized]
   - Operating range: [X]°C to [X]°C
   - Flow rate: [X] L/min

2. **Gaseous Hydrogen** (for precooling)
   - Temperature: -253°C → [X]°C
   - Flow rate: [X] kg/hr (from boil-off)

3. **Ram Air**
   - Temperature: Ambient
   - Flow rate: Variable with airspeed

### 6.2 Cooling Loops

#### Loop 1: High-Temperature Propulsion Loop
- **Components cooled**: Fuel cells, power electronics
- **Coolant**: [Type]
- **Temp range**: [X]°C to [X]°C
- **Heat exchanger**: Ram air heat exchanger

#### Loop 2: Medium-Temperature Motor Loop
- **Components cooled**: Electric motors
- **Coolant**: [Type]
- **Temp range**: [X]°C to [X]°C
- **Heat exchanger**: Ram air heat exchanger

#### Loop 3: Battery Thermal Management Loop
- **Components cooled**: Battery packs
- **Coolant**: [Type]
- **Temp range**: [X]°C to [X]°C
- **Control**: Heating and cooling capability

#### Loop 4: Cryogenic Pre-Cooling Loop
- **Heat source**: H2 boil-off gas
- **Usage**: Pre-cooling for high-temp loops
- **Benefit**: Reduces ram air heat exchanger size

---

## 7. Heat Exchanger Network

### 7.1 Primary Heat Exchangers

| HX ID | Type | Capacity (kW) | Coolant 1 | Coolant 2 | Location |
|-------|------|---------------|-----------|-----------|----------|
| HX-01 | Liquid-Air | [X] | Propulsion coolant | Ram air | Wing leading edge |
| HX-02 | Liquid-Air | [X] | Motor coolant | Ram air | Aft fuselage |
| HX-03 | Gas-Liquid | [X] | H2 boil-off | Propulsion coolant | Near H2 tanks |
| HX-04 | Liquid-Liquid | [X] | Battery coolant | Propulsion coolant | Battery bay |

### 7.2 Heat Exchanger Sizing Methodology
[Describe approach to sizing heat exchangers]

---

## 8. Thermal Energy Balance

### 8.1 Energy Balance by Flight Phase

| Phase | Heat Generated (kW) | Heat Rejected (kW) | Thermal Mass Storage (kJ) |
|-------|---------------------|--------------------|---------------------------|
| Taxi | [X] | [X] | [X] |
| Takeoff | [X] | [X] | [X] |
| Climb | [X] | [X] | [X] |
| Cruise | [X] | [X] | 0 (equilibrium) |
| Descent | [X] | [X] | [X] (recovery) |

### 8.2 Thermal Mass Buffering
- Use thermal capacitance of coolant and structures
- Allow temporary temperature excursions during transients
- Ensure temperatures return to nominal during cruise

---

## 9. Waste Heat Recovery Opportunities

### 9.1 Cabin Heating
- **Source**: Fuel cell waste heat
- **Capacity**: [X] kW available
- **Usage**: Cabin heating in cold weather
- **Benefit**: Reduced ECS heating load

### 9.2 Ice Protection
- **Source**: Propulsion waste heat
- **Capacity**: [X] kW available
- **Usage**: Wing and empennage anti-ice/de-ice
- **Benefit**: Eliminates bleed air requirement

### 9.3 Pre-Flight Conditioning
- **Source**: Stored thermal energy
- **Usage**: Pre-warm systems before flight
- **Benefit**: Improved cold-start reliability

---

## 10. Integration with Aircraft Systems

### 10.1 Environmental Control System (ECS)
- Interface with thermal management system
- Cabin air conditioning and heating
- Humidity control
- Ventilation

### 10.2 Hydrogen System
- Heat input to cryogenic tanks (see THERM-002)
- Boil-off gas utilization for cooling
- Tank thermal stratification management

### 10.3 Electrical System
- Battery thermal management critical for safety
- Power electronics cooling for efficiency
- Thermal runaway prevention

---

## 11. Thermal Control System

### 11.1 Active Controls
- Coolant pump speed control
- Valve position control for flow distribution
- Fan speed control for ram air augmentation
- Thermal management system computer (TMSC)

### 11.2 Sensors and Instrumentation
- Temperature sensors at key locations
- Flow sensors in coolant loops
- Pressure sensors
- Thermal imaging for diagnostics

### 11.3 Control Logic
- Feedback control for temperature regulation
- Predictive control based on flight phase
- Fault detection and isolation
- Degraded mode operation

---

## 12. Failure Modes and Mitigations

| Failure Mode | Impact | Mitigation | Dispatch Impact |
|--------------|--------|------------|-----------------|
| HX blockage | Reduced cooling | Redundant paths, monitoring | Go with caution |
| Pump failure | Loop shutdown | Redundant pumps | Go with limitations |
| Coolant leak | Loss of cooling | Leak detection, isolation | No-Go |
| Control system fault | Improper cooling | Manual mode, redundancy | Go with limitations |

---

## 13. Thermal Analysis Tools and Methods

### 13.1 Analysis Approach
- Computational Fluid Dynamics (CFD)
- Finite Element Analysis (FEA) for conduction
- Lumped parameter thermal models
- Transient thermal analysis

### 13.2 Validation Plan
- Component-level thermal testing
- System-level thermal testing
- Flight test validation

---

## 14. Mass and Volume Estimates

### 14.1 Thermal System Mass Breakdown
| Component | Mass (kg) |
|-----------|-----------|
| Heat exchangers | [X] |
| Coolant (filled) | [X] |
| Pumps | [X] |
| Plumbing and valves | [X] |
| Insulation | [X] |
| Controls and sensors | [X] |
| **Total** | **[X]** |

---

## 15. Open Issues and TBDs

1. [TBD: Final heat exchanger sizing]
2. [TBD: Coolant fluid final selection]
3. [TBD: Control system architecture details]

---

## 16. Next Steps

1. Detailed thermal modeling and simulation
2. Component selection and procurement
3. Thermal test rig design
4. Integration with propulsion and H2 systems
5. Safety analysis for thermal hazards

---

## References

- **Cryogenic Thermal**: [THERM-002_CRYOGENIC_THERMAL_ANALYSIS.md](./THERM-002_CRYOGENIC_THERMAL_ANALYSIS.md)
- **Propulsion Cooling**: [THERM-003_PROPULSION_COOLING_DESIGN.md](./THERM-003_PROPULSION_COOLING_DESIGN.md)
- **Aircraft Integration**: [THERM-004_AIRCRAFT_THERMAL_INTEGRATION.md](./THERM-004_AIRCRAFT_THERMAL_INTEGRATION.md)
- **Propulsion System**: [../04-PROPULSION/PROP-001_PROPULSION_SYSTEM_ARCHITECTURE_DOCUMENT.md](../04-PROPULSION/PROP-001_PROPULSION_SYSTEM_ARCHITECTURE_DOCUMENT.md)
- **H2 Storage**: [../05-HYDROGEN_STORAGE/H2-001_CRYOGENIC_TANK_PRELIMINARY_DESIGN.md](../05-HYDROGEN_STORAGE/H2-001_CRYOGENIC_TANK_PRELIMINARY_DESIGN.md)

---

**Document Control**  
**Classification**: Internal/Technical  
**Distribution**: Engineering, Thermal Team, Integration  
**Change Control**: Via ECR/ECO process
