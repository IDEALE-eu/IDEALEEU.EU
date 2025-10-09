# Propulsion Chain Integration

## Overview

This document describes the complete propulsion chain from fuel/air/ignition inputs through thrust/torque output, including all control loops and system integration.

## Propulsion Chain Flow

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   Fuel   │────►│   Air    │────►│ Ignition │────►│  Thrust  │
│  System  │     │  Intake  │     │  System  │     │  Output  │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │
     │           ┌────▼────────────────▼────┐          │
     └──────────►│  Engine Control (FADEC)  │◄─────────┘
                 └─────────┬─────────────────┘
                           │
                    ┌──────▼───────┐
                    │ Pilot Input  │
                    │ (Thrust Lever)│
                    └──────────────┘
```

## Fuel System Chain (ATA-28 → ATA-73 → ATA-72)

### Fuel Flow Path
1. **Aircraft Fuel Tanks (ATA-28)**
   - Main wing tanks
   - Center tank (if applicable)
   - Fuel quantity measurement

2. **Fuel Pumps (ATA-28)**
   - Primary and backup pumps
   - Pressure regulation
   - Flow control

3. **Fuel Control (ATA-73)**
   - FADEC fuel metering valve
   - Flow rate control
   - Fuel shutoff valve

4. **Engine Fuel Nozzles (ATA-72)**
   - Fuel atomization
   - Combustion chamber injection

### Control Loop
- **Input**: Thrust lever position, engine parameters
- **Processing**: FADEC computes required fuel flow
- **Output**: Fuel metering valve position
- **Feedback**: Actual fuel flow, N1/N2 speeds, EGT

## Air System Chain (ATA-72 → ATA-75 → Aircraft Systems)

### Airflow Path
1. **Engine Inlet (ATA-72)**
   - Air intake
   - Inlet guide vanes (if variable)

2. **Compressor Stages (ATA-72)**
   - Low-pressure compressor (fan)
   - High-pressure compressor
   - Pressure and temperature rise

3. **Combustion Chamber (ATA-72)**
   - Fuel-air mixing
   - Combustion process
   - Energy release

4. **Turbine Stages (ATA-72)**
   - High-pressure turbine (drives HP compressor)
   - Low-pressure turbine (drives fan)
   - Energy extraction

5. **Bleed Air Extraction (ATA-75)**
   - High-pressure bleed (from HP compressor)
   - Low-pressure bleed (from LP compressor or fan)
   - Pressure regulation

### Bleed Air Distribution
- **Environmental Control (ATA-21)**: Cabin pressurization and temperature
- **Anti-Ice (ATA-30)**: Wing and engine anti-ice
- **Hydraulic System (ATA-29)**: Reservoir pressurization
- **Engine Starting (ATA-80)**: Cross-bleed starting
- **Water/Waste (ATA-38)**: Potable water pressurization (if applicable)

## Ignition System Chain (ATA-74 → ATA-72)

### Ignition Sequence
1. **Start Command (ATA-76)**
   - Pilot initiates start sequence
   - Start control logic validation

2. **Ignition Activation (ATA-74)**
   - Exciter energizes
   - High-voltage generation (20-25 kV)
   - Spark at igniter plugs

3. **Engine Light-Off (ATA-72)**
   - Fuel ignition in combustion chamber
   - Self-sustaining combustion achieved
   - Acceleration to idle speed

4. **Continuous Ignition (if required)**
   - Heavy rain, ice, or severe turbulence
   - Automatic or manual activation

### Control Loop
- **Input**: Start switch, N1/N2 speeds, EGT
- **Processing**: Start logic in FADEC or start controller
- **Output**: Ignition on/off commands
- **Feedback**: Light-off detection, stable idle confirmation

## Engine Control Chain (ATA-76 → ATA-73 → ATA-72)

### Thrust Control Loop
1. **Pilot Input (ATA-76)**
   - Thrust lever position
   - Auto-throttle commands (if equipped)

2. **Control Processing (ATA-73 FADEC)**
   - Thrust lever resolver position (TLA)
   - Engine operating mode (start, idle, cruise, takeoff)
   - Environmental conditions (altitude, temperature)
   - Engine limits (N1, N2, EGT, fuel flow)

3. **Actuation (ATA-76 → ATA-73)**
   - Fuel metering valve position
   - Variable geometry actuation (if applicable)
   - Bleed valve control

4. **Engine Response (ATA-72)**
   - N1/N2 acceleration/deceleration
   - Thrust output change
   - Temperature and pressure changes

### Feedback Signals (ATA-77)
- **N1 Speed**: Low-pressure rotor (fan) speed
- **N2 Speed**: High-pressure rotor speed
- **EGT**: Exhaust gas temperature
- **Fuel Flow**: Actual fuel consumption
- **Oil Pressure/Temperature**: Lubrication system health
- **Vibration**: Engine health monitoring

## Engine Starting Chain (ATA-80 → ATA-72)

### Start Sequence
1. **Pre-Start Checks**
   - Fuel available
   - Oil pressure adequate
   - Ignition armed
   - Start valve ready

2. **Starter Engagement (ATA-80)**
   - Starter motor energized (electric or pneumatic)
   - Engine cranking to light-off speed
   - Typical: 10-15% N2

3. **Fuel Introduction (ATA-73)**
   - FADEC opens fuel valve
   - Fuel flow begins

4. **Ignition (ATA-74)**
   - Igniters spark
   - Light-off occurs

5. **Acceleration to Idle**
   - Starter continues until self-sustaining
   - Typical: 50-60% N2
   - Starter disengages

6. **Idle Stabilization**
   - Engine at stable idle
   - All parameters normal
   - Start sequence complete

## Thrust Output and Propulsion Performance

### Thrust Generation
- **Bypass Air (ATA-72-20)**: Fan thrust (80-85% of total thrust in high-bypass engines)
- **Core Exhaust (ATA-72-10 + ATA-78)**: Hot gas thrust (15-20% of total thrust)
- **Thrust Reversers (ATA-78)**: Reverse thrust for deceleration

### Performance Parameters
- **Thrust Settings**:
  - Maximum Takeoff: 100% N1
  - Maximum Continuous: 95% N1
  - Maximum Climb: 90% N1
  - Cruise: 80-85% N1
  - Approach: 50-60% N1
  - Idle: 20-30% N1

### Operating Limits
- **N1 Limit**: Fan overspeed protection
- **N2 Limit**: Core overspeed protection
- **EGT Limit**: Turbine temperature limit
- **Fuel Flow Limit**: Maximum fuel delivery rate

## Fault Management and Redundancy

### Critical Failures
- **Fuel System Failure**: Engine shutdown, APU or battery power
- **Ignition Failure**: Continuous ignition mode, manual relight
- **Control System Failure**: Reversion to backup control mode
- **Sensor Failure**: Redundant sensor voting, degraded mode

### Engine-Out Operations
- **Single-Engine Failure**: Asymmetric thrust, rudder compensation
- **Dual-Engine Failure (if applicable)**: Emergency power (RAT, batteries)
- **APU Auto-Start**: Emergency electrical and pneumatic power

## Integration with Other Systems

### Electrical Power (ATA-24)
- Generators driven by engine accessory gearbox
- Electrical load affects fuel consumption
- Generator failure affects overall power availability

### Hydraulic Power (ATA-29)
- Engine-driven pumps (EDP)
- Hydraulic load affects engine power requirement
- Pump failure may require bleed air backup

### Oil System (ATA-79)
- Engine-driven oil pump
- Oil cooling via fuel or air
- Oil health affects engine reliability

## Digital Twin Integration

### Real-Time Monitoring
- Engine thrust output (lbf or kN)
- Fuel consumption rate (lb/hr or kg/hr)
- Specific fuel consumption (SFC)
- Engine health parameters
- Performance degradation

### Predictive Analytics
- Remaining engine life
- Maintenance due dates
- Performance deterioration trends
- Optimal operating points

## Related Documents

- [Energy Flow Integration](./ENERGY_FLOW.md)
- [Thermal-Power Coupling](./THERMAL_POWER_COUPLING.md)
- [ATA-72 Engine Integration View](../01-SYSTEMS/ATA-72_ENGINE/INTEGRATION_VIEW.md)
- [ATA-73 FADEC Integration View](../01-SYSTEMS/ATA-73_ENGINE_FUEL_CONTROL/INTEGRATION_VIEW.md)

---

**Last Updated**: 2024-01-15
