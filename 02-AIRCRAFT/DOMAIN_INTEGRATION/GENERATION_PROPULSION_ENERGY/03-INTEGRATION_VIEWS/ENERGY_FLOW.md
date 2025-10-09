# Energy Flow Integration View

## Overview

This document describes the complete energy flow architecture for the GENERATION_PROPULSION_ENERGY domain, including AC/DC power generation, distribution, priorities, and load-shedding strategies.

## Power Generation Architecture

### Primary Generation
- **Main Engine Generators**: 2× 90 kVA AC generators (400Hz, 115V 3-phase)
- **APU Generator**: 1× 90 kVA AC generator (ground and emergency operations)
- **Emergency Generator/RAT**: Emergency power source (if applicable)

### Secondary Generation (Power Conversion)
- **Transformer Rectifier Units (TRUs)**: AC to DC conversion (28V DC)
- **Static Inverters**: DC to AC conversion (emergency AC power)
- **DC-DC Converters**: Voltage regulation (5V, 12V from 28V)

### Energy Storage
- **Main Batteries**: 2× 24V 40Ah NiCd batteries
- **APU Battery**: 1× 24V 20Ah NiCd battery
- **Emergency battery backup**: Critical system support

## Power Distribution Architecture

### AC Power Distribution

```
                    ┌─────────────────┐
                    │  GEN 1 (90kVA)  │
                    └────────┬─────────┘
                             │
                        ┌────▼────┐
                        │  GCU 1  │
                        └────┬────┘
                             │
      ┌──────────────────────┼──────────────────────┐
      │                      │                      │
┌─────▼──────┐        ┌──────▼──────┐       ┌──────▼──────┐
│ AC Main    │◄───────┤ Bus Tie     │───────►│ AC Main    │
│ Bus 1      │        │ Contactor   │        │ Bus 2      │
└─────┬──────┘        └─────────────┘        └──────┬─────┘
      │                                              │
      │                                              │
┌─────▼──────┐                              ┌───────▼─────┐
│ AC Essen.  │                              │  GEN 2      │
│ Bus 1      │                              │  (90kVA)    │
└────────────┘                              └─────────────┘

         ┌───────────────┐
         │  APU GEN      │
         │  (90kVA)      │
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │ AC Essential  │
         │ Bus (Ground)  │
         └───────────────┘
```

### DC Power Distribution

```
┌──────────┐         ┌──────────┐
│  TRU 1   │         │  TRU 2   │
│ (200A)   │         │ (200A)   │
└────┬─────┘         └─────┬────┘
     │                     │
┌────▼─────────────────────▼────┐
│      DC Main Bus (28V)        │
└────┬──────────────────────┬───┘
     │                      │
┌────▼────────┐      ┌──────▼───────┐
│ DC Essen.   │      │ Battery Bus  │
│ Bus         │      │              │
└─────────────┘      └──────┬───────┘
                            │
                     ┌──────▼───────┐
                     │  Batteries   │
                     │  (2× 40Ah)   │
                     └──────────────┘
```

## Load Priorities and Shedding

### Priority 1 - Critical Loads (Never Shed)
- **Flight Control Computers**: Primary and standby channels
- **Engine FADEC**: Full Authority Digital Engine Control
- **Essential Flight Instruments**: Attitude, airspeed, altitude
- **Emergency Lighting**: Exit path illumination
- **Fire Detection/Suppression**: Safety-critical systems

**Total Load**: ~15 kVA

### Priority 2 - Essential Loads (Shed Only in Emergency)
- **Navigation Systems**: IRS, GPS, VOR/ILS
- **Communication Systems**: VHF, HF radios (minimum 1 system)
- **Essential Avionics**: FMS, EICAS (basic mode)
- **Anti-ice Systems**: Wing and engine anti-ice
- **Fuel Pumps**: Minimum required for operation

**Total Load**: ~25 kVA

### Priority 3 - Normal Loads (Shed When Required)
- **Hydraulic Pumps**: Non-critical pumps
- **Environmental Control**: Full ECS capacity
- **Full Avionics Suite**: All displays and systems
- **Cabin Systems**: Cabin lighting, IFE prep
- **Galley Power**: Reduced capability

**Total Load**: ~30 kVA

### Priority 4 - Non-Essential Loads (First to Shed)
- **In-Flight Entertainment**: Passenger entertainment systems
- **Galley Systems**: Full galley capability
- **Comfort Systems**: Cabin comfort features
- **Non-essential Lighting**: Cabin mood lighting
- **Auxiliary Equipment**: Non-critical equipment

**Total Load**: ~40 kVA

## Load Shedding Sequences

### Automatic Load Shedding Triggers
1. **Single Generator Failure**: Shed Priority 4 loads
2. **Total Generator Failure with Battery**: Shed Priority 3 & 4, essential only
3. **Low Battery Voltage**: Progressive shedding Priority 4 → 3 → 2
4. **Generator Overload**: Shed lowest priority until within limits

### Manual Load Shedding
- Pilot can manually shed non-essential loads via cockpit controls
- Load shed status displayed on EICAS

## Bus Configuration Modes

### Normal Mode (All Generators Online)
- Each generator powers its own bus
- Bus tie contactor open (isolated buses)
- Full system capacity available

### Parallel Mode (Generators Paralleled)
- Bus tie contactor closed
- Generators share load equally
- Used for load balancing or maintenance

### Single Generator Mode
- One generator failed or offline
- Remaining generator(s) power all buses
- Automatic load shedding activated

### Emergency Mode (Battery Only)
- All generators failed
- Batteries supply DC essential bus
- Static inverter supplies AC essential bus
- Only Priority 1 loads powered

### Ground Mode (APU Only)
- APU generator powers essential buses
- Main generators offline
- Limited power capacity

## Power Quality Requirements

### AC Power Specifications
- **Voltage**: 115V ±5% (109-121V)
- **Frequency**: 400Hz ±2% (392-408Hz)
- **Waveform**: Sine wave, <5% THD
- **Phase Balance**: ±10% between phases
- **Transient Response**: <200ms recovery to ±10%

### DC Power Specifications
- **Voltage**: 28V DC nominal (24-32V operating range)
- **Ripple**: <2% peak-to-peak
- **Transient Response**: <100ms recovery to ±5%
- **Load Regulation**: ±2% from no-load to full-load

## Energy Management System (EMS) Functions

### Monitoring
- Bus voltages and currents
- Generator loads and power factors
- Battery state of charge
- Power quality metrics

### Control
- Generator control and paralleling
- Bus configuration (tie contactor control)
- Load shedding sequencing
- Battery charging control

### Protection
- Over/under voltage protection
- Over-current protection
- Ground fault detection
- Arc fault detection (if applicable)

### Optimization
- Load balancing between generators
- Generator run-time equalization
- Battery charging optimization
- Fuel efficiency optimization

## Digital Twin Integration

### Real-Time KPIs
- Total power generation (kVA)
- Power consumption by system (kW)
- Generator efficiency (%)
- Battery SOC (%)
- System efficiency (%)

### Predictive Analytics
- Remaining generator capacity
- Battery health trending
- Power system degradation
- Maintenance predictions

## Related Documents

- [Propulsion Chain Integration](./PROPULSION_CHAIN.md)
- [Thermal-Power Coupling](./THERMAL_POWER_COUPLING.md)
- [ATA-24 Integration View](../01-SYSTEMS/ATA-24_ELECTRICAL_POWER/INTEGRATION_VIEW.md)
- [Domain Interface Matrix](../02-INTERFACES/INTERFACE_MATRIX.csv)

---

**Last Updated**: 2024-01-15
