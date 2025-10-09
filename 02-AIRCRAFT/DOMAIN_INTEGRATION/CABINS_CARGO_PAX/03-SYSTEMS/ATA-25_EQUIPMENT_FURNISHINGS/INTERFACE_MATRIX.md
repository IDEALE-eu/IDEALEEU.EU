# Interface Matrix - ATA-25 Equipment & Furnishings

## Purpose

This document defines all interfaces between ATA-25 subsystems and external aircraft systems. It provides a quick reference for integration dependencies and interface specifications.

## Interface Overview Matrix

| ATA-25 Subsystem | External System | Interface Type | Criticality | ICD Reference |
|------------------|-----------------|----------------|-------------|---------------|
| Seats | ATA-51 (Structure) | Mechanical attachment | Critical | ICD-25-10-51 |
| Seats | ATA-24 (Electrical) | Power (USB, AC outlets) | Normal | ICD-25-10-24 |
| Seats | ATA-44 (IFE) | Entertainment system | Normal | ICD-25-10-44 |
| Galleys | ATA-24 (Electrical) | Power distribution | Critical | ICD-25-20-24 |
| Galleys | ATA-38 (Water/Waste) | Water supply | Normal | ICD-25-20-38 |
| Galleys | ATA-21 (ECS) | Ventilation/exhaust | Normal | ICD-25-20-21 |
| Lavatories | ATA-38 (Water/Waste) | Water/waste lines | Critical | ICD-25-30-38 |
| Lavatories | ATA-21 (ECS) | Ventilation | Normal | ICD-25-30-21 |
| Lavatories | ATA-26 (Fire) | Smoke detection | Critical | ICD-25-30-26 |
| Lavatories | ATA-24 (Electrical) | Power for lighting | Normal | ICD-25-30-24 |
| Trims/Linings | ATA-51 (Structure) | Attachment points | Normal | ICD-25-40-51 |
| Trims/Linings | ATA-33 (Lighting) | Light mounting | Normal | ICD-25-40-33 |
| Overhead Bins | ATA-51 (Structure) | Structural mounting | Critical | ICD-25-50-51 |
| Floors | ATA-51 (Structure) | Load-bearing structure | Critical | ICD-25-60-51 |
| Floors | ATA-92 (EWIS) | Wire routing channels | Normal | ICD-25-60-92 |
| PSU | ATA-24 (Electrical) | Power distribution | Normal | ICD-25-70-24 |
| PSU | ATA-21 (ECS) | Air nozzle control | Normal | ICD-25-70-21 |
| PSU | ATA-35 (Oxygen) | Oxygen mask deployment | Critical | ICD-25-70-35 |
| PSU | ATA-44 (CMS) | Call system, lighting | Normal | ICD-25-70-44 |
| Emergency Equip | ATA-26 (Fire) | Fire extinguisher integration | Critical | ICD-25-80-26 |
| Emergency Equip | ATA-35 (Oxygen) | Life vest/oxygen integration | Critical | ICD-25-80-35 |

## Interface Details

### ATA-24: Electrical Power

**Power Requirements:**
- Galley equipment: 115V AC, 400Hz, up to 20kW per galley
- Seat power outlets: 110V AC, 60Hz, 75W per seat
- USB charging: 5V DC, 2.4A per port
- PSU lighting: 28V DC
- Lavatory lighting: 28V DC

**Circuit Protection:**
- Galley circuits: Individual breakers per equipment
- Seat outlets: Circuit breaker per row
- USB ports: Electronic protection per port

**Reference:**
- [ATA-24 Configuration](../../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/)
- ICD documents in: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-24/`

---

### ATA-21: Environmental Control System (ECS)

**Ventilation Interfaces:**
- Galley exhaust: 200 CFM per galley
- Lavatory exhaust: 50 CFM per lavatory
- PSU air nozzles: Individual passenger control

**Temperature Requirements:**
- Galley area: 18-24°C
- Lavatory area: 20-25°C
- Passenger cabin: 22-24°C

**Reference:**
- [ATA-21 Configuration](../../../../CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/)
- ICD documents: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-21/`

---

### ATA-26: Fire Protection

**Detection Interfaces:**
- Lavatory smoke detectors: 1 per lavatory (required)
- Cargo area detectors: Integration with galley/equipment areas
- Alert system: Connection to cabin crew notification

**Suppression Integration:**
- Galley fire suppression: Automatic Halon/clean agent
- Portable extinguishers: Storage location in ATA-25-80

**Reference:**
- [ATA-26 Configuration](../../../../CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/)
- ICD documents: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-26/`

---

### ATA-33: Lighting

**Lighting Integration:**
- Cabin overhead lighting: Coordinated with CMS (ATA-44)
- Reading lights at seats: Individual control
- Galley lighting: Task lighting, 500 lux
- Lavatory lighting: Automatic on entry

**Emergency Lighting:**
- Floor path lighting: Part of ATA-25-60 floor panels
- Exit signs: Integrated into trims

**Reference:**
- [ATA-33 Configuration](../../../../CONFIGURATION_BASE/ATA-33_LIGHTS/)
- Control through ATA-44 CMS

---

### ATA-35: Oxygen

**Oxygen Interfaces:**
- PSU oxygen masks: Automatic deployment on cabin pressure loss
- Portable oxygen bottles: Storage in emergency equipment
- Deployment signal: From flight deck or automatic

**Requirements:**
- Mask count: 1 per passenger seat + 10% extra
- Deployment time: < 1 second
- Flow rate: 2-4 liters/minute per mask

**Reference:**
- [ATA-35 Configuration](../../../../CONFIGURATION_BASE/ATA-35_OXYGEN/)
- ICD documents: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-35/`

---

### ATA-38: Water/Waste

**Water Supply:**
- Galley hot water: 80-85°C, 2 GPM per tap
- Galley cold water: 15-20°C, 2 GPM per tap
- Lavatory water: 15-20°C, 1 GPM per faucet

**Waste System:**
- Lavatory waste: Vacuum flush system
- Grey water: From galley sinks
- Connection points: Floor-level quick disconnects

**Reference:**
- [ATA-38 Configuration](../../../../CONFIGURATION_BASE/ATA-38_WATER_WASTE/)
- ICD documents: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-38/`

---

### ATA-44: Cabin Systems

**Control Interfaces:**
- PSU attendant call: Signal to CMS
- PSU reading lights: CMS control override capability
- Galley status monitoring: Equipment status to CMS
- Seat IFE mounting: Physical and electrical integration

**Data Interfaces:**
- Occupancy sensors: Seat occupancy to CMS
- Lavatory occupancy: Status to CMS displays

**Reference:**
- [ATA-44 Cabin Systems](./ATA-44_CABIN_SYSTEMS/)
- Internal domain interface

---

### ATA-51/52: Structures

**Structural Interfaces:**
- Seat tracks: Load path to airframe
- Floor attachment: Primary structure interface
- Overhead bin mounting: Ceiling/sidewall structure
- Galley/lavatory mounting: Floor and sidewall

**Load Requirements:**
- Seats: 16g forward, 9g side, 10g vertical
- Overhead bins: 50 lb/sq ft
- Galleys: Per equipment weight + service load
- Lavatories: Per occupancy + water weight

**Reference:**
- [Airframe Integration](../../AIRFRAMES/)
- ICD documents: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-25-51/`

---

### ATA-92: EWIS (Electrical Wiring)

**Wiring Interfaces:**
- Floor cable routing: Channels in floor panels
- Sidewall routing: Behind trim panels
- PSU wiring: Ceiling-mounted harnesses
- Galley/lavatory power: Dedicated harnesses

**Note:** Physical wiring implementation is documented in ATA-92. This document defines logical interfaces only.

**Reference:**
- [ATA-92 EWIS](../../../../CONFIGURATION_BASE/ATA-92_EWIS/)

---

## Interface Change Control

All interface changes follow the process defined in:
- [Change Rules](../../../01-GOVERNANCE/CHANGE_RULES.md)
- [Interface Management](../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

Interface Change Notices (ICNs) required for:
- Changes to electrical power requirements
- Mechanical interface modifications
- New interface additions
- Interface specification changes

## Interface Verification

Verification requirements:
1. Interface Control Documents (ICDs) reviewed and approved
2. Physical fit checks during integration
3. Functional testing of all interfaces
4. Load testing for structural interfaces
5. Environmental testing per DO-160

## References

- [Domain Dependencies](../../../02-ARCHITECTURE/DEPENDENCIES.md)
- [Safety Boundaries](../../../01-GOVERNANCE/SAFETY_BOUNDARIES.md)
- [ICD Index](../../../05-LINKS/ICD_INDEX.md)

---

**Last Updated**: 2025-01-15
