# ELECTRICAL_EMC

Electrical and electromagnetic compatibility standards for spacecraft.

## Overview

This directory contains ECSS standards for electrical engineering and electromagnetic compatibility (EMC) in space systems.

## Applicable Standards

### ECSS-E-ST-20C - Electrical and Electronic Engineering
- **Scope**: Electrical design, interfaces, and power systems
- **Coverage**: Power generation, distribution, grounding, ESD protection
- **Key Topics**:
  - Electrical power system design
  - Power budgets and margins
  - Electrical interface specifications
  - Grounding and bonding
  - Electrostatic discharge (ESD) protection
  - Electrical parts selection and derating

### ECSS-E-ST-20-07C - Electromagnetic Compatibility
- **Scope**: EMC requirements and verification
- **Coverage**: Emissions and susceptibility (conducted and radiated)
- **Key Topics**:
  - EMC requirements specification
  - EMC design guidelines
  - EMC analysis and modeling
  - EMC testing

### ECSS-E-ST-20-08C - Photovoltaic Assemblies and Components
- **Scope**: Solar array design and qualification
- **Coverage**: Solar cells, panels, deployment mechanisms
- **Key Topics**:
  - Solar cell selection and characterization
  - Solar array design (electrical, thermal, structural)
  - End-of-life (EOL) performance prediction
  - Radiation degradation

## Electrical Power System

### Power Generation
- **Solar Arrays**: Photovoltaic panels, deployment mechanisms
- **Batteries**: Energy storage (Li-ion most common)
- **Other**: Fuel cells, nuclear (RTG) for deep space

### Power Distribution
- **Power Bus**: Regulated (28V common) or unregulated
- **Power Converters**: DC/DC converters for various voltage levels
- **Power Switching**: Relays, solid-state switches
- **Fusing and Protection**: Overcurrent protection, short-circuit protection

### Power Budget
- **Generation**: Solar array output (beginning-of-life BOL, end-of-life EOL)
- **Storage**: Battery capacity and depth-of-discharge (DOD)
- **Consumption**: All loads by mode (launch, eclipse, nominal, peak)
- **Margin**: Typically 20-30% at EOL

### Power System Modes
- **Launch Mode**: Batteries only, minimal power
- **Eclipse Mode**: Batteries supply all power
- **Sunlight Mode**: Solar arrays charge batteries and supply loads
- **Peak Mode**: Maximum power demand (e.g., payload operations, thrusting)
- **Safe Mode**: Minimum power, survival mode

## Grounding and Bonding

### Grounding Philosophy
- **Single-Point Ground (SPG)**: All grounds connect at one point
- **Multi-Point Ground (MPG)**: Grounds connect at multiple points
- **Hybrid**: Combination based on frequency (SPG at low freq, MPG at high freq)

### Bonding
- **Electrical Bonding**: Low-impedance connections between metallic parts
- **Grounding Straps**: Flexible conductors for bonding
- **Bonding Resistance**: Typically < 2.5 mΩ between bonded surfaces
- **Purpose**: EMC, ESD protection, fault current return path

## Electromagnetic Compatibility (EMC)

### EMC Requirements
- **Emissions**: Limits on conducted and radiated electromagnetic emissions
- **Susceptibility**: Equipment must operate in presence of EM fields
- **Margins**: Typically 6 dB for emissions, 6 dB for susceptibility

### EMC Design Guidelines
- **Filtering**: Power line filters, signal filters
- **Shielding**: Conductive enclosures, shielded cables
- **Grounding**: Proper grounding to minimize ground loops
- **Cable Routing**: Separation of power and signal cables
- **Layout**: PCB layout for EMC (ground planes, trace routing)

### EMC Analysis
- **Emissions Modeling**: Predict radiated and conducted emissions
- **Susceptibility Analysis**: Assess vulnerability to external fields
- **Coupling Analysis**: Crosstalk between cables, systems

### EMC Testing
- **Conducted Emissions (CE)**: Measure emissions on power and signal lines
- **Radiated Emissions (RE)**: Measure emissions from equipment in anechoic chamber
- **Conducted Susceptibility (CS)**: Inject disturbances on cables
- **Radiated Susceptibility (RS)**: Expose equipment to EM fields
- **Frequency Range**: Typically 10 kHz to 18 GHz or higher

## Electrostatic Discharge (ESD)

### ESD Threats
- **Handling**: Personnel handling during AIT
- **Launch/Ascent**: Triboelectric charging
- **Space Environment**: Spacecraft charging from plasma

### ESD Protection
- **Design**: Discharge paths, bleed resistors, protection diodes
- **Procedures**: Grounding, wrist straps, conductive mats
- **Materials**: Conductive or dissipative materials
- **Testing**: ESD immunity testing per ECSS or IEC 61000-4-2

## Solar Arrays

### Solar Cell Technologies
- **Silicon**: Heritage, moderate efficiency (~18%)
- **Multi-Junction**: GaAs, GaInP/GaAs/Ge, high efficiency (~30%)
- **Thin-Film**: CdTe, CIGS, flexible, lower efficiency

### Solar Array Design
- **Sizing**: Power generation vs. area, mass, cost
- **Configuration**: Body-mounted or deployable
- **Orientation**: Sun-tracking or fixed
- **Temperature**: High temperature degrades performance
- **Radiation**: Performance degrades over mission life

### Degradation
- **Radiation**: Displacement damage from protons, electrons
- **UV Exposure**: Cover glass protects cells
- **Thermal Cycling**: Fatigue of solder joints, connections
- **Micrometeoroid/Debris**: Physical damage

### End-of-Life (EOL) Performance
- BOL power × (1 - annual degradation)^mission_years
- Typically 2-3% per year in LEO, less in GEO or deep space

## Electrical Interfaces

### Interface Types
- **Power Interfaces**: Voltage levels, current limits, inrush, ripple
- **Data Interfaces**: Protocols (RS-422, SpaceWire, CAN, MIL-STD-1553)
- **Analog Interfaces**: Voltage/current signals, sensor interfaces
- **Discrete Interfaces**: On/off commands, status signals

### Interface Control
- **Interface Control Document (ICD)**: Define all electrical interfaces
- **Connector Specifications**: Pin assignments, mating, contact resistance
- **Cable Specifications**: Gauge, shielding, length

## Key Deliverables

1. **Electrical Power System Design** - Architecture, components, sizing
2. **Power Budget** - Generation, storage, consumption by mode
3. **Electrical Schematic Diagrams** - All electrical interconnections
4. **Grounding and Bonding Plan** - Grounding philosophy and implementation
5. **EMC Control Plan** - EMC requirements, design, analysis, testing
6. **EMC Test Plan and Report** - CE, RE, CS, RS testing
7. **Solar Array Design and Analysis** - Sizing, performance, EOL prediction
8. **ESD Control Plan** - Design and procedures for ESD protection
9. **Interface Control Documents (ICDs)** - All electrical interfaces

## Compliance Requirements

- Electrical design per ECSS-E-ST-20C
- EMC per ECSS-E-ST-20-07C
- Solar arrays per ECSS-E-ST-20-08C
- Power margins verified
- EMC testing demonstrates compliance

## Integration with Other Standards

- **ECSS-E-ST-10C** - Systems engineering defines electrical requirements
- **ECSS-Q-ST-60C** - EEE component selection for electrical systems
- **ECSS-E-ST-31C** - Thermal design for solar arrays and power electronics

## Tools and Templates

- Power budget spreadsheets
- EMC analysis tools (FEKO, CST)
- Solar array performance calculators
- EMC test procedures

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-017 (ECSS-E-ST-20C)
- ECSS Portal: https://ecss.nl
- IEC 61000 series (EMC standards)

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
