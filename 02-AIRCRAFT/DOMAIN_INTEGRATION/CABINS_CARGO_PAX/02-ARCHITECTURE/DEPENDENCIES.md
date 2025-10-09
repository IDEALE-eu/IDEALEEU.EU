# Dependencies - CABINS_CARGO_PAX Domain

## Purpose

This document defines external dependencies and references for the CABINS_CARGO_PAX domain. It provides pointers to other ATA chapters WITHOUT copying their content.

## External ATA Chapter Dependencies

### ATA-21: Air Conditioning

**Referenced for:**
- Lavatory ventilation requirements
- Galley exhaust specifications
- Cabin temperature control interfaces
- Air distribution to passenger areas

**Interface Points:**
- Air nozzle control at PSU
- Galley ventilation ducts
- Lavatory exhaust fans
- Temperature sensor locations

**Configuration Reference:**
- [ATA-21 Configuration](../../../CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/)
- [ATA-21 Interface Specs](../../../CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/ICD/)

**Do NOT duplicate:** ECS design, ducting details, control logic

---

### ATA-24: Electrical Power

**Referenced for:**
- Cabin system power requirements
- Galley power distribution (115V AC, 28V DC)
- IFE system power budgets
- Passenger power outlets (AC/DC, USB)
- Cargo system electrical loads

**Interface Points:**
- Power distribution panels for galleys
- IFE power supply units
- USB charging ports
- Cargo PDU power feeds
- Emergency power priorities

**Configuration Reference:**
- [ATA-24 Configuration](../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/)
- [ATA-24 Load Analysis](../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/PARAMS/)

**Do NOT duplicate:** Electrical system design, generator specs, distribution logic

---

### ATA-26: Fire Protection

**Referenced for:**
- Cargo compartment fire detection coverage
- Lavatory smoke detectors
- Galley fire suppression
- Emergency equipment fire protection

**Interface Points:**
- Smoke detector mounting locations (cargo, lavatories)
- Fire suppression system activation
- Alarm indication to cabin crew
- System status monitoring

**Configuration Reference:**
- [ATA-26 Configuration](../../../CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/)
- [ATA-26 Detection Zones](../../../CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/BASELINE/)

**Do NOT duplicate:** Fire detection algorithms, suppression system design

---

### ATA-31: Indicating/Recording Systems

**Referenced for:**
- Weight and balance data integration
- Cargo load sensing data
- System status indication
- Maintenance data recording

**Interface Points:**
- Load cell data from cargo systems
- Weight and balance calculations
- System health monitoring
- Fault recording and reporting

**Configuration Reference:**
- [ATA-31 Configuration](../../../CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/)

**Do NOT duplicate:** Data recording architecture, indication system design

---

### ATA-33: Lights

**Referenced for:**
- Cabin lighting control
- Emergency lighting coordination
- Reading lights at seats
- Galley and lavatory lighting

**Interface Points:**
- Cabin lighting control from CMS
- Emergency lighting activation
- Individual reading light switches
- Lighting power distribution

**Configuration Reference:**
- [ATA-33 Configuration](../../../CONFIGURATION_BASE/ATA-33_LIGHTS/)

**Do NOT duplicate:** Lighting hardware design, power distribution details

---

### ATA-35: Oxygen

**Referenced for:**
- Passenger oxygen mask deployment (PSU integration)
- Lavatory oxygen mask (if applicable)
- Emergency oxygen system coordination

**Interface Points:**
- PSU oxygen mask deployment mechanism
- Deployment signal from cabin crew
- System pressure monitoring

**Configuration Reference:**
- [ATA-35 Configuration](../../../CONFIGURATION_BASE/ATA-35_OXYGEN/)

**Do NOT duplicate:** Oxygen generation/storage, pressure regulation

---

### ATA-38: Water/Waste

**Referenced for:**
- Galley water supply connections
- Lavatory water supply and drainage
- Waste system integration
- Potable water quality

**Interface Points:**
- Water supply valves and connections (galleys, lavatories)
- Grey water drainage
- Waste tank connections
- Water heater interfaces (if in galleys)

**Configuration Reference:**
- [ATA-38 Configuration](../../../CONFIGURATION_BASE/ATA-38_WATER_WASTE/)

**Do NOT duplicate:** Water system design, waste tank specifications

---

### ATA-42: Integrated Modular Avionics (IMA)

**Referenced for:**
- CMS hosted on IMA platform
- IFE system connectivity
- Cabin system data processing
- Network infrastructure

**Interface Points:**
- IMA cabinet hosting for cabin applications
- ARINC 664 (AFDX) network connections
- Data processing for cabin systems
- Software integration requirements

**Configuration Reference:**
- [ATA-42 Configuration](../../../CONFIGURATION_BASE/ATA-42_IMA/)

**Do NOT duplicate:** IMA architecture, partitioning, resource allocation

---

### ATA-92: Electrical Wiring Interconnection System (EWIS)

**Referenced for:**
- Physical wiring implementation
- Wire routing through cabin
- Connector specifications
- Grounding and shielding

**Interface Points:**
- All electrical connections for cabin systems
- IFE wiring harnesses
- Power distribution wiring
- Sensor and control wiring

**Configuration Reference:**
- [ATA-92 Configuration](../../../CONFIGURATION_BASE/ATA-92_EWIS/)

**Do NOT duplicate:** Wiring diagrams, cable specifications, routing details

---

## Internal Dependencies

### Between ATA Chapters within Domain

1. **ATA-25 → ATA-44**
   - PSU structure (ATA-25) hosts lighting and call controls (ATA-44)
   - Seat structure (ATA-25) supports IFE screens and controls (ATA-44)
   - Floor panels (ATA-25) provide routing for cabin network (ATA-44)

2. **ATA-25 → ATA-50**
   - Floor structure (ATA-25) supports cargo handling equipment (ATA-50)
   - Load path integration between furnishings and cargo systems

3. **ATA-44 → ATA-50**
   - Cargo control interfaces with CMS (ATA-44) for monitoring
   - Network infrastructure (ATA-44) supports cargo system data

## Configuration Management Dependencies

### References to CONFIGURATION_BASE

All baseline configuration data resides in:
- `02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/`
- `02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/`
- `02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/`

This domain integration references but does NOT duplicate:
- Component specifications
- Hardware configurations
- Software baselines
- Verification data
- Parameter definitions

### Interface Control Documents (ICDs)

All formal interfaces are managed through:
- `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

System-specific ICD references:
- `CONFIGURATION_BASE/[ATA-XX]/ICD/` for each system

## Supplier Dependencies

### Major Equipment Suppliers

**Note:** Specific supplier information maintained in procurement/supply chain systems.

1. **Seating Suppliers** (ATA-25-10)
   - Seat design specifications
   - Interface requirements
   - Installation data

2. **Galley Equipment** (ATA-25-20)
   - Equipment specifications
   - Power and water requirements
   - Service procedures

3. **IFE Providers** (ATA-44-20)
   - System architecture
   - Content management
   - Network requirements

4. **Cargo Systems** (ATA-50)
   - ULD specifications
   - PDU specifications
   - Control system interfaces

## Software Dependencies

### Operating Systems and Platforms

- CMS software hosted on IMA (ATA-42)
- IFE system software (supplier-specific)
- Cargo management software
- Network management software

### Data Dependencies

- Flight operations data (weight, balance, passenger count)
- Maintenance data (system health, fault logs)
- Content data (IFE movies, maps, etc.)
- Configuration data (seat maps, cargo loading)

## Certification Dependencies

### Regulatory Compliance

- FAR Part 25 (Transport Category Airplanes)
- EASA CS-25 (Certification Specifications)
- TSO certifications for components
- DO-160 (Environmental Conditions)
- DO-178C (Software) for cabin systems software
- DO-254 (Hardware) for cabin systems hardware

### Certification Artifacts

Referenced from:
- `CONFIGURATION_BASE/[ATA-XX]/VERIFICATION/`

## Maintenance Dependencies

### Maintenance Planning

- Access requirements through other systems
- Scheduled maintenance coordination
- Component replacement procedures
- Software update procedures

### Maintenance Support

- Ground Support Equipment (GSE) requirements
- Special tooling requirements
- Test equipment specifications
- Maintenance training materials

## Reference Documents

- [Domain Context](./DOMAIN_CONTEXT.md)
- [Data Contracts](./DATA_CONTRACTS.md)
- [Interface Management Process](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [Configuration Rules](../../../CONFIGURATION_BASE/00-COMMON/RULES.md)

## Dependency Management

### Change Impact Analysis

When changes occur in dependent systems:
1. Review interface specifications
2. Assess impact on cabin/cargo systems
3. Update interface documentation
4. Coordinate with affected system owners
5. Update this dependencies document

### Version Control

Dependencies are version-controlled:
- Document references include baseline/version
- Interface specifications include revision dates
- Configuration references include configuration IDs

---

**Last Updated**: 2025-01-15
