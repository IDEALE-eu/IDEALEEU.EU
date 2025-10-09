# Standards Mapping

## Overview

This document maps applicable standards and regulations to the GENERATION_PROPULSION_ENERGY domain components.

## Certification Standards

### CS-25 (Certification Specifications for Large Aeroplanes)

#### Subpart E - Powerplant
- **CS-25.901**: Installation
- **CS-25.903**: Engines
- **CS-25.904**: Automatic takeoff thrust control system (ATTCS)
- **CS-25.905**: Propellers
- **CS-25.939**: Turbine engine operating characteristics
- **CS-25.943**: Negative acceleration
- **CS-25.951**: Fuel system - General
- **CS-25.981**: Fuel tank ignition prevention
- **CS-25.994**: Fuel system components

#### Subpart F - Equipment
- **CS-25.1301**: Function and installation
- **CS-25.1309**: Equipment, systems, and installations
- **CS-25.1310**: Power source capacity and distribution
- **CS-25.1331**: Instruments using a power supply
- **CS-25.1351**: General electrical system requirements
- **CS-25.1353**: Electrical equipment and installations
- **CS-25.1355**: Distribution system
- **CS-25.1357**: Circuit protective devices
- **CS-25.1431**: Electronic engine control systems

## Environmental Testing Standards

### DO-160 (Environmental Conditions and Test Procedures for Airborne Equipment)

Applicable sections for electrical/electronic equipment:
- **Section 4**: Temperature and Altitude
- **Section 5**: Temperature Variation
- **Section 6**: Humidity
- **Section 7**: Operational Shocks and Crash Safety
- **Section 8**: Vibration
- **Section 15**: Magnetic Effect
- **Section 16**: Power Input
- **Section 17**: Voltage Spike
- **Section 18**: Audio Frequency Conducted Susceptibility - Power Inputs
- **Section 19**: Induced Signal Susceptibility
- **Section 20**: Radio Frequency Susceptibility (Radiated and Conducted)
- **Section 21**: Emission of Radio Frequency Energy
- **Section 22**: Lightning Induced Transient Susceptibility
- **Section 23**: Lightning Direct Effects
- **Section 25**: Electrostatic Discharge

## Software Standards

### DO-178C (Software Considerations in Airborne Systems and Equipment Certification)

Applicable to:
- **FADEC (ATA-73)**: Design Assurance Level (DAL) A
- **Energy Management System (ATA-24)**: DAL B
- **APU Control (ATA-49)**: DAL C
- **Engine Control (ATA-76)**: DAL A/B

### DO-278A (Guidelines for Communication, Navigation, Surveillance and Air Traffic Management (CNS/ATM) Systems Software Integrity Assurance)

Applicable if CNS/ATM functions are integrated.

## Hardware Standards

### DO-254 (Design Assurance Guidance for Airborne Electronic Hardware)

Applicable to:
- **Generator Control Units (GCU)**: DAL B
- **FADEC**: DAL A
- **Power distribution units**: DAL B/C
- **Engine control units**: DAL A/B

## Interface Standards

### ARINC Standards

- **ARINC 429**: Digital Information Transfer System (DITS)
- **ARINC 664**: Aircraft Data Network, Parts 1-7 (AFDX)
- **ARINC 653**: Avionics Application Software Standard Interface (if IMA-hosted)

### Military Standards (if applicable)

- **MIL-STD-1553**: Digital Time Division Command/Response Multiplex Data Bus
- **MIL-STD-704**: Aircraft Electric Power Characteristics
- **MIL-STD-461**: Requirements for the Control of Electromagnetic Interference

## Fuel System Standards

- **CS-25 Subpart E**: Fuel system requirements
- **SAE AS5127**: Design Standard for Aircraft Fuel System Components
- **SAE AS8826**: Fuel Deoxygenation System

## EWIS Standards

- **CS-25.1701-1733**: Electrical Wiring Interconnection Systems (EWIS)
- **FAA AC 43-13-1B**: Acceptable Methods, Techniques, and Practices - Aircraft Inspection and Repair

## Quality Standards

- **AS9100**: Quality Management Systems for Aviation, Space, and Defense
- **ISO 9001**: Quality Management Systems

## Component-Specific Standards

### Generators
- **SAE AS5692**: Requirements for Generators

### Batteries
- **SAE AS6858**: Lithium-ion Battery Installation Requirements (if Li-ion used)
- **RTCA DO-311**: Minimum Operational Performance Standards for Rechargeable Lithium Battery Systems

### APU
- **CS-APU**: Certification Specifications for Auxiliary Power Units

## Compliance Matrix

| Component | Applicable Standards | Compliance Evidence Location |
|-----------|---------------------|------------------------------|
| Generators | CS-25.1351, DO-160 | `EVIDENCE_LINKS.md` |
| FADEC | CS-25.1431, DO-178C DAL-A, DO-254 | `EVIDENCE_LINKS.md` |
| Batteries | CS-25.1353, DO-160 | `EVIDENCE_LINKS.md` |
| Energy Mgmt System | CS-25.1309, DO-178C DAL-B | `EVIDENCE_LINKS.md` |
| APU | CS-APU, CS-25.1431 | `EVIDENCE_LINKS.md` |
| Engine | CS-25.901-905, CS-25.939 | `EVIDENCE_LINKS.md` |
| Wiring (EWIS) | CS-25.1701-1733 | ATA-92 Documentation |

---

**Last Updated**: 2024-01-15
