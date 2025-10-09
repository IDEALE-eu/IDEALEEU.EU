# ATA-24 Electrical Power - Integration View

## System Overview

The Electrical Power System provides generation, storage, distribution, and management of electrical energy for all aircraft systems.

## Architecture

### Power Generation
- **Generators/Starter-Generators (ATA-24-10)**: Primary AC power generation from engines
- **APU Generator (ATA-49)**: Ground and emergency power generation
- **Ram Air Turbine (if applicable)**: Emergency power generation

### Energy Storage
- **Batteries (ATA-24-20)**: Emergency backup power, starting power
- **Energy Storage Systems**: Advanced storage technologies (if applicable)

### Power Conversion
- **Converters/Rectifiers/Inverters (ATA-24-30)**:
  - AC to DC conversion (rectifiers)
  - DC to AC conversion (inverters)
  - DC-DC converters for voltage regulation
  - Transformer rectifier units (TRUs)

### Power Distribution
- **Distribution/Switchgear/Contactors (ATA-24-40)**:
  - AC buses (main, essential, emergency)
  - DC buses (main, essential, battery)
  - Bus tie contactors
  - Generator control units (GCUs)
  - Circuit breakers and protection

### Energy Management
- **Energy Management Controller (ATA-24-50)**:
  - Power system monitoring and control
  - Load management and shedding
  - Bus configuration control
  - Fault detection and isolation
  - Power quality monitoring
  - ARINC 653 partition hosting (if applicable)

## Key Integration Points

### Generation ↔ Storage
- Battery charging during normal operations
- Battery discharge during emergency/starting
- State of charge monitoring
- Thermal management of batteries

### Generation ↔ Distribution
- Generator output to main buses
- Paralleling of generators
- Generator protection and isolation
- Bus voltage and frequency regulation

### Storage ↔ Distribution
- Battery bus configuration
- Emergency power switching
- Battery contactor control

### Energy Management System (EMS)
- **Interfaces to All Subsystems**:
  - Generator status and control
  - Battery state monitoring
  - Bus voltage/current/frequency
  - Contactor positions
  - Load priorities

## Power Architecture Flow

```
[Generators] ──→ [GCU] ──→ [AC Main Bus] ──→ [AC Systems]
                              │
                              ├──→ [TRU] ──→ [DC Main Bus] ──→ [DC Systems]
                              │                   │
[APU Gen] ──→ [GCU] ──→ [AC Essential Bus]       │
                                                  │
[Battery] ──→ [Battery Contactor] ──→ [DC Essential Bus]
                                        │
[Emergency Gen/RAT] ──→ [Emergency Bus]
```

## Load Priorities

### Critical Loads (Priority 1)
- Flight control computers
- Engine FADEC
- Essential instruments
- Emergency lighting

### Essential Loads (Priority 2)
- Navigation systems
- Communication systems
- Essential avionics

### Non-Essential Loads (Priority 3)
- Cabin systems
- In-flight entertainment
- Galley systems

## Power Quality Requirements

- **AC Power**: 115V AC, 400Hz, 3-phase
- **DC Power**: 28V DC nominal (24-32V operating range)
- **Voltage Regulation**: ±5% steady state
- **Frequency Regulation**: ±2Hz (400Hz systems)
- **Harmonic Distortion**: <5% THD

## Fault Management

### Fault Detection
- Over/under voltage
- Over/under frequency
- Over-current
- Ground faults
- Generator failures

### Fault Isolation
- Automatic generator disconnect
- Bus isolation
- Load shedding sequences
- Emergency configuration reconfiguration

### Redundancy Strategy
- Multiple generators (N+1 redundancy)
- Multiple buses (segregated)
- Battery backup
- Emergency power sources

## Interface with Other Systems

See `INTERFACE_MATRIX/24↔28_29_36_42_45_46_92_33.csv` for detailed interface specifications.

### Key System Interfaces
- **ATA-28**: Fuel System (pump power, tank indication)
- **ATA-29**: Hydraulic System (pump power)
- **ATA-36**: Pneumatic System (compressor power)
- **ATA-42**: IMA (avionics power, data interfaces)
- **ATA-45**: Central Maintenance System (fault reporting)
- **ATA-46**: Information Systems (cockpit displays)
- **ATA-92**: EWIS (all wiring and connectors)
- **ATA-33**: Lights (interior/exterior lighting power)

## Digital Thread Integration

### MBSE Links
- SysML Block Definition Diagrams (BDD)
- Internal Block Diagrams (IBD)
- Activity Diagrams (power flow sequences)
- State Machine Diagrams (system modes)

### Digital Twin KPIs
- Total power generation capacity
- Power consumption by system
- Bus voltages and currents
- Generator load percentages
- Battery state of charge
- Power quality metrics (voltage, frequency, harmonics)

## Verification Approach

- Power system functional tests
- Load analysis verification
- Fault injection testing
- Emergency power transfer tests
- EMI/EMC testing (DO-160 Section 16)

## Compliance References

- **DO-160**: Environmental testing (Section 16: Power Input)
- **DO-178C**: Software (if EMS has embedded software)
- **DO-254**: Hardware (for electronic control units)
- **CS-25**: Subpart E (Powerplant), Subpart F (Equipment)
- **CS-25.1351**: General electrical system requirements
- **CS-25.1353**: Electrical equipment and installations

## Related Documents

- [ATA-24 Configuration Base](../../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/)
- [Subsystem Details](./SUBSYSTEMS/)
- [Interface Matrix](./INTERFACE_MATRIX/)

---

**Last Updated**: 2024-01-15
