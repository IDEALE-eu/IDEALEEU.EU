# Interface Control Document (ICD) Index

## Purpose

Index of Interface Control Documents (ICDs) for Q100 version systems. ICDs specify the interfaces between different systems and domains.

## ICD Location

All ICDs are maintained centrally in:
```
00-PROGRAM/CONFIG_MGMT/09-INTERFACES/
```

**Relative path from Q100:**
```
../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/
```

## Interface Matrix by System

Each system maintains an `INTERFACE_MATRIX/` directory with CSV files listing interfaces to other systems.

### AAA — Airframes, Aerodynamics, Airworthiness

#### ATA 06 — Dimensions & Stations
**Matrix:** `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-06-24: Dimensions ↔ Electrical Power (coordinate reference)
- ICD-Q100-06-25: Dimensions ↔ Equipment/Furnishings (cabin layout)
- ICD-Q100-06-53: Dimensions ↔ Fuselage (structural datums)
- ICD-Q100-06-57: Dimensions ↔ Wings (wing stations)
- ICD-Q100-06-92: Dimensions ↔ Aircraft General (overall dimensions)

#### ATA 51 — Structures General
**Matrix:** `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/51-STRUCTURES-GENERAL/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-51-52: Structures ↔ Doors (door frame interfaces)
- ICD-Q100-51-53: Structures ↔ Fuselage (primary structure)
- ICD-Q100-51-57: Structures ↔ Wings (wing-body integration)
- ICD-Q100-51-24: Structures ↔ Electrical (grounding, bonding)
- ICD-Q100-51-25: Structures ↔ Equipment/Furnishings (mounting)
- ICD-Q100-51-92: Structures ↔ Aircraft General (structural criteria)

#### ATA 52 — Doors
**Matrix:** `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/52-DOORS/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-52-53: Doors ↔ Fuselage (door opening, sealing)
- ICD-Q100-52-24: Doors ↔ Electrical (door control, lighting)
- ICD-Q100-52-25: Doors ↔ Equipment/Furnishings (interior finish)
- ICD-Q100-52-29: Doors ↔ Hydraulic (door actuators)
- ICD-Q100-52-36: Doors ↔ Pneumatic (door seals)
- ICD-Q100-52-92: Doors ↔ Aircraft General (emergency egress)

### EEE — Electrical, Endotransponders, Circulation

#### ATA 24 — Electrical Power
**Matrix:** `EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/24-ELECTRICAL-POWER/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-24-28: Electrical ↔ Fuel (fuel cell power generation)
- ICD-Q100-24-29: Electrical ↔ Hydraulic (electric hydraulic pumps)
- ICD-Q100-24-36: Electrical ↔ Pneumatic (electric air compressors)
- ICD-Q100-24-42: Electrical ↔ IMA (avionics power distribution)
- ICD-Q100-24-45: Electrical ↔ Maintenance System (BITE power)
- ICD-Q100-24-46: Electrical ↔ Information Systems (data power)
- ICD-Q100-24-92: Electrical ↔ Aircraft General (grounding)
- ICD-Q100-24-33: Electrical ↔ Lights (lighting power)
- ICD-Q100-24-71: Electrical ↔ Power Plant (motor drive power)

### EDI — Electronics, Digital, Instruments

#### ATA 34 — Navigation & Avionics
**Matrix:** `EDI-ELECTRONICS-DIGITAL-INSTRUMENTS/SYSTEMS/34-NAVIGATION-AVIONICS/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-34-22: Navigation ↔ Auto Flight (flight director)
- ICD-Q100-34-24: Navigation ↔ Electrical (avionics power)
- ICD-Q100-34-31: Navigation ↔ Displays (navigation displays)
- ICD-Q100-34-42: Navigation ↔ IMA (data integration)
- ICD-Q100-34-45: Navigation ↔ Maintenance (navigation health monitoring)
- ICD-Q100-34-92: Navigation ↔ Aircraft General (navigation requirements)

### MEC — Mechanical Systems & Modules

#### ATA 32 — Landing Gear Systems
**Matrix:** `MEC-MECHANICAL-SYSTEMS-MODULES/SYSTEMS/32-LANDING-GEAR-SYSTEMS/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-32-27: Landing Gear ↔ Flight Controls (steering, braking)
- ICD-Q100-32-29: Landing Gear ↔ Hydraulic (gear actuation, brakes)
- ICD-Q100-32-24: Landing Gear ↔ Electrical (position indicators)
- ICD-Q100-32-92: Landing Gear ↔ Aircraft General (ground handling)

### PPP — Propulsion & Fuel Systems

#### ATA 71 — Power Plant
**Matrix:** `PPP-PROPULSION-FUEL-SYSTEMS/SYSTEMS/71-POWER-PLANT/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-71-24: Power Plant ↔ Electrical (motor power, control)
- ICD-Q100-71-28: Power Plant ↔ Fuel (H₂ fuel supply to fuel cells)
- ICD-Q100-71-29: Power Plant ↔ Hydraulic (accessory drives)
- ICD-Q100-71-36: Power Plant ↔ Pneumatic (cooling air)
- ICD-Q100-71-75: Power Plant ↔ Air Conditioning (waste heat recovery)
- ICD-Q100-71-92: Power Plant ↔ Aircraft General (thrust, noise)

### CCC — Cockpit, Cabin, Cargo

#### ATA 25 — Equipment & Furnishings
**Matrix:** `CCC-COCKPIT-CABIN-CARGO/SYSTEMS/25-EQUIPMENT-FURNISHINGS/INTERFACE_MATRIX/`  
**Key Interfaces:**
- ICD-Q100-25-21: Equipment ↔ Environmental Control (cabin comfort)
- ICD-Q100-25-38: Equipment ↔ Water/Waste (galley, lavatory)
- ICD-Q100-25-24: Equipment ↔ Electrical (cabin power, IFE)
- ICD-Q100-25-33: Equipment ↔ Lights (cabin lighting)
- ICD-Q100-25-50: Equipment ↔ Cargo (cargo restraints)
- ICD-Q100-25-92: Equipment ↔ Aircraft General (interior config)

## ICD Document Structure

Each ICD follows this structure:
```
ICD-Q100-XX-YY/
├── ICD_SPECIFICATION.md       # Interface specification
├── REQUIREMENTS.md             # Interface requirements
├── VERIFICATION_MATRIX.md      # Verification criteria
├── DRAWINGS/                   # Interface drawings
└── CHANGE_LOG.md               # ICD revision history
```

## ICD Naming Convention

Format: `ICD-{VERSION}-{ATA1}-{ATA2}`

Examples:
- `ICD-Q100-24-71` — Electrical ↔ Power Plant interface
- `ICD-Q100-51-53` — Structures ↔ Fuselage interface

## ICD Status Tracking

| ICD ID | Title | Rev | Status | Last Updated |
|--------|-------|-----|--------|--------------|
| ICD-Q100-24-71 | Electrical ↔ Power Plant | A | Released | 2025-03-15 |
| ICD-Q100-24-28 | Electrical ↔ Fuel | A | Released | 2025-03-10 |
| ICD-Q100-51-53 | Structures ↔ Fuselage | A | Released | 2025-03-01 |
| ICD-Q100-32-29 | Landing Gear ↔ Hydraulic | A | Released | 2025-03-05 |
| ICD-Q100-34-42 | Navigation ↔ IMA | A | Released | 2025-03-12 |
| ICD-Q100-52-53 | Doors ↔ Fuselage | A | Released | 2025-02-28 |
| ICD-Q100-25-21 | Equipment ↔ ECS | A | Released | 2025-03-08 |

## Using ICDs

### For System Engineers
1. Identify your system's interfaces from the INTERFACE_MATRIX/
2. Locate the corresponding ICD in `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
3. Review interface requirements and specifications
4. Ensure compliance during design and verification

### For Integration Engineers
1. Use ICDs to validate interface compatibility
2. Coordinate interface testing per ICD verification matrices
3. Report interface issues via change process
4. Update ICDs when interfaces evolve

### For Configuration Management
1. Control ICD versions alongside configuration baselines
2. Ensure ICD changes go through CCB approval
3. Maintain traceability between ICDs and requirements
4. Include ICD status in baseline reviews

## Change Control

ICD changes require:
1. Interface Change Notice (ICN)
2. Impact assessment on both systems
3. CCB approval
4. Coordinated implementation
5. Verification testing

## References

- **ICD Repository:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Interface Process:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md#interface-control`
- **Change Process:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/`

## Document Control

- **Version:** 1.0.0
- **Last Updated:** 2025-03-31
- **Owner:** Systems Integration Team
- **Review Cycle:** With each baseline release or ICD change

---

For detailed interface specifications, navigate to:
`../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
