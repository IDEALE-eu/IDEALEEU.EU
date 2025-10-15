---
layout: page
title: "TFA Domains Reference"
description: "Threading Functional Architecture - 15 canonical aerospace domains"
---

# TFA Domains Reference

Threading Functional Architecture (TFA) provides 15 canonical domains that structure aerospace lifecycle data. Each domain represents a major functional area with consistent organization across design, analysis, manufacturing, and service phases.

## Overview

TFA domains enable:
- **Consistent organization** across all aerospace programs
- **Clear ownership** and responsibility boundaries
- **Efficient search** and retrieval of artifacts
- **Traceability** throughout the lifecycle
- **Integration** with PLM, ERP, and MES systems

---

## The 15 TFA Domains

### AAA – Airframes-Aerodynamics-Airworthiness

**Purpose**: Structural design, aerodynamic performance, and certification compliance for airframes.

**Key Areas**:
- Fuselage structures (primary, secondary)
- Wing structures (spars, ribs, skins)
- Empennage (horizontal and vertical stabilizers)
- Control surfaces (ailerons, rudder, elevator)
- Landing gear interfaces
- Aerodynamic analysis (CFD, wind tunnel)
- Structural analysis (FEA, fatigue, damage tolerance)
- Airworthiness compliance (FAR/EASA Part 25)

**CAx Phases**: CAD → CAE → CAV (validation critical)

**Standards**: 
- ATA Chapters: 51-57 (Structures)
- DO-160 (Environmental conditions)
- AC 20-107B (Composite aircraft structures)

**Example Components**:
- Wing box assembly
- Fuselage frames and stringers
- Composite panels
- Joint fittings

---

### AAP – Airport-Adaptable-Platforms

**Purpose**: Ground operations, airport compatibility, and platform adaptability.

**Key Areas**:
- Ground handling equipment interfaces
- Passenger boarding systems
- Cargo loading systems
- Servicing interfaces (fuel, power, air, water)
- Towing and pushback compatibility
- Turnaround time optimization
- Multi-airport adaptability
- Remote operations capability

**CAx Phases**: CAI → CAP → CAS

**Standards**:
- ATA Chapter 12 (Servicing)
- IATA Ground Operations Manual
- Airport compatibility requirements

**Example Components**:
- Boarding door mechanisms
- Cargo door systems
- Ground power receptacles
- Fuel servicing panels

---

### CCC – Cockpit-Cabin-Cargo

**Purpose**: Flight deck, passenger cabin, and cargo compartment systems.

**Key Areas**:
- Flight deck layout and ergonomics
- Avionics displays and controls
- Passenger seating and amenities
- Cabin environmental control
- In-flight entertainment
- Cargo compartment design
- Galley and lavatory systems
- Emergency equipment

**CAx Phases**: CAD → CAI → CAS

**Standards**:
- ATA Chapters: 25 (Equipment/Furnishings), 33 (Lights), 38 (Water/Waste)
- DO-178C (Software)
- DO-254 (Hardware)
- TSO standards (avionics)

**Example Components**:
- Instrument panels
- Passenger seats
- Overhead bins
- Cargo loading systems

---

### CQH – Cryogenics-Quantum-H2

**Purpose**: Hydrogen systems, cryogenic storage, and advanced propulsion technologies.

**Key Areas**:
- Liquid hydrogen (LH2) storage (-253°C)
- Cryogenic insulation systems
- H2 fuel cell integration
- Cryogenic pumps and valves
- Boil-off management
- Safety systems (leak detection, venting)
- Quantum sensing for H2 monitoring
- Zero-emission propulsion

**CAx Phases**: CAE → CAO → CAV (safety-critical)

**Standards**:
- SAE AIR7286 (Hydrogen fuel cell systems)
- ISO/TS 19883 (Safety of hydrogen systems)
- EASA Special Conditions for hydrogen aircraft
- Cryogenic codes (ASME Section VIII)

**Example Components**:
- LH2 fuel tanks
- Vacuum-insulated piping
- Cryogenic valves
- H2 fuel cells
- Venting systems

---

### DDD – Drainage-Dehumidification-Drying

**Purpose**: Moisture management, water removal, and contamination prevention.

**Key Areas**:
- Water drainage systems
- Dehumidification equipment
- Drying processes (manufacturing, MRO)
- Condensation prevention
- Corrosion protection
- Ice and frost prevention
- Wastewater management
- Environmental control integration

**CAx Phases**: CAE → CAM → CAS

**Standards**:
- ATA Chapter 38 (Water/Waste)
- MIL-STD-810 (Environmental testing)
- Corrosion control standards

**Example Components**:
- Drain masts and tubes
- Dehumidification units
- Sealants and coatings
- Water separators

---

### EDI – Electronics-Digital-Instruments

**Purpose**: Electronic systems, digital controls, and instrumentation.

**Key Areas**:
- Avionics systems
- Flight control computers
- Engine control units (FADEC)
- Digital displays and indicators
- Sensors and transducers
- Data acquisition systems
- Communication systems
- Navigation systems

**CAx Phases**: CAD → CAE → CAV

**Standards**:
- DO-178C (Software)
- DO-254 (Hardware)
- DO-160 (Environmental)
- ARINC specifications
- MIL-STD-1553 (Data bus)

**Example Components**:
- Flight management computers
- FADEC units
- Electronic flight bags (EFB)
- Digital instruments

---

### EEE – Electrical-Endocircular-Energization

**Purpose**: Electrical power generation, distribution, and energy management.

**Key Areas**:
- Electrical power generation (generators, APU)
- Power distribution networks
- Energy storage (batteries)
- Circuit protection
- Wiring and harnesses
- Grounding and bonding
- Lightning protection
- More-electric aircraft (MEA) systems

**CAx Phases**: CAD → CAE → CAV

**Standards**:
- ATA Chapter 24 (Electrical Power)
- DO-160 (EMI/EMC)
- MIL-STD-461 (EMI requirements)
- SAE AS50881 (Wiring practices)

**Example Components**:
- Engine-driven generators
- Distribution panels
- Battery systems
- Wiring harnesses
- Lightning protection systems

---

### EER – Environmental-Emissions-Remediation

**Purpose**: Environmental impact, emissions reduction, and sustainability.

**Key Areas**:
- Emissions monitoring (NOx, CO2, particulates)
- Noise reduction systems
- Sustainable aviation fuels (SAF)
- Circular economy practices
- Environmental compliance
- Lifecycle environmental assessment
- Carbon footprint reduction
- Water and waste management

**CAx Phases**: CAE → CAO → CAS

**Standards**:
- ICAO Annex 16 (Environmental protection)
- EASA CS-34 (Engine emissions)
- ISO 14001 (Environmental management)
- Carbon offset standards

**Example Components**:
- Emissions monitoring systems
- Noise-reducing engine components
- Environmental data recorders
- Waste management systems

---

### IIF – Industrial-Infrastructure-Facilities

**Purpose**: Manufacturing facilities, tooling, and industrial equipment.

**Key Areas**:
- Factory layout and flow
- Manufacturing equipment
- Tooling and fixtures
- Material handling systems
- Quality control stations
- Clean rooms and controlled environments
- Energy systems (plant utilities)
- Facility maintenance

**CAx Phases**: CAP → CAM → CMP

**Standards**:
- ISO 9001 (Quality management)
- AS9100 (Aerospace QMS)
- Lean manufacturing principles
- 5S workplace organization

**Example Components**:
- Assembly jigs
- Autoclaves (composites)
- CNC machining centers
- Coordinate measuring machines (CMM)
- Material storage systems

---

### IIS – Information-Intelligence-Systems

**Purpose**: Information technology, data management, and intelligent systems.

**Key Areas**:
- PLM/PDM systems
- ERP integration
- MES (Manufacturing Execution Systems)
- Digital thread and digital twin
- AI/ML for predictive analytics
- Data lakes and warehouses
- Cybersecurity
- Knowledge management

**CAx Phases**: All phases (cross-cutting)

**Standards**:
- ISO 27001 (Information security)
- NIST Cybersecurity Framework
- Data exchange standards (STEP, JT, 3D PDF)
- API standards (REST, GraphQL)

**Example Components**:
- PLM servers
- Database systems
- Analytics platforms
- Cybersecurity tools

---

### LCC – Linkages-Control-Communications

**Purpose**: Mechanical linkages, control systems, and communication networks.

**Key Areas**:
- Flight control linkages
- Hydraulic systems
- Pneumatic systems
- Mechanical actuators
- Control cables and rods
- Communication systems (voice, data)
- Fly-by-wire systems
- Satellite communications

**CAx Phases**: CAD → CAE → CAV

**Standards**:
- ATA Chapters: 27 (Flight Controls), 29 (Hydraulics), 36 (Pneumatics)
- DO-178C (Software)
- MIL-STD-1553 (Data bus)
- ARINC 429 (Avionics data)

**Example Components**:
- Control surface actuators
- Hydraulic pumps and valves
- Control cables
- Communication radios

---

### LIB – Logistics-Inventory-Blockchain

**Purpose**: Supply chain management, inventory control, and blockchain traceability.

**Key Areas**:
- Supply chain visibility
- Inventory management
- Counterfeit prevention
- Blockchain-based traceability
- Serialization and tracking
- Warehouse management
- Spare parts management
- Supplier quality management

**CAx Phases**: CAP → CMP → CAS

**Standards**:
- SPEC2000 (Aviation material management)
- EPCIS (Supply chain events)
- GS1 standards (barcoding, RFID)
- ISO 28000 (Supply chain security)

**Example Components**:
- RFID tags
- Serialized components
- Blockchain nodes
- Inventory management systems

---

### MMM – Mechanical-Material-Modules

**Purpose**: Mechanical components, material specifications, and modular assemblies.

**Key Areas**:
- Material selection and specifications
- Mechanical component design
- Fasteners and hardware
- Modular assembly design
- Material testing and characterization
- Advanced materials (composites, titanium, additive manufacturing)
- Surface treatments
- Assembly processes

**CAx Phases**: CAD → CAE → CAM

**Standards**:
- AMS (Aerospace Material Specifications)
- MMPDS (Metallic Materials Properties)
- ASTM standards (material testing)
- ISO 10303 (STEP - material data)

**Example Components**:
- Machined parts
- Composite structures
- Fasteners and fittings
- Modular assemblies

---

### OOO – Operations-Optimization-Outcomes

**Purpose**: Operational excellence, performance optimization, and business outcomes.

**Key Areas**:
- Flight operations
- Maintenance operations
- Performance monitoring
- Fuel efficiency optimization
- Route optimization
- Fleet management
- Reliability analysis
- Key performance indicators (KPIs)

**CAx Phases**: CAS → CMP (feedback loop)

**Standards**:
- IATA Operational Standards
- ATA MSG-3 (Maintenance program development)
- ISO 55000 (Asset management)
- Operational safety standards

**Example Components**:
- Flight data recorders
- Health monitoring systems
- Analytics dashboards
- Optimization algorithms

---

### PPP – Propulsion-Power-Plants

**Purpose**: Propulsion systems, engines, and power generation.

**Key Areas**:
- Gas turbine engines
- Electric propulsion
- Hybrid-electric systems
- Engine controls (FADEC)
- Fuel systems
- Engine mounting and integration
- Propeller systems
- Engine health monitoring

**CAx Phases**: CAD → CAE → CAV

**Standards**:
- ATA Chapter 70-80 (Engines and related systems)
- FAR Part 33 (Airworthiness standards: Aircraft engines)
- EASA CS-E (Engine certification)
- SAE AS and ARP standards

**Example Components**:
- Turbofan engines
- Electric motors
- FADEC systems
- Fuel pumps and nozzles
- Engine mounts

---

## TFA Integration with CAx Lifecycle

Each TFA domain integrates with the 9-phase CAx lifecycle:

| Phase | Domain Integration |
|-------|-------------------|
| **CAD** | 3D models, drawings, geometric definitions |
| **CAE** | Analysis results, simulations, load cases |
| **CAI** | System integration, interface definitions |
| **CAO** | Optimization studies, trade analyses |
| **CAM** | Manufacturing plans, tooling, NC programs |
| **CAP** | Production schedules, resource planning |
| **CAV** | Test plans, verification results, validation data |
| **CMP** | Configuration management, change control |
| **CAS** | Service documentation, maintenance procedures |

---

## Using TFA Domains in Practice

### 1. Component Classification
When creating a digital passport, select the appropriate TFA domain:
```
Part: Wing Leading Edge Assembly
Domain: AAA (Airframes-Aerodynamics-Airworthiness)
ATA: 57-30 (Wing Leading Edge)
```

### 2. Directory Structure
TFA domains structure repository directories:
```
02-AIRCRAFT/
  DOMAIN_INTEGRATION/
    PRODUCTS/AMPEL360-AIR-T/
      MODELS/BWB-H2-Hy-E/
        VERSION/Q100/
          DOMAIN/
            AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/
            PPP-PROPULSION-POWER-PLANTS/
            CQH-CRYOGENICS-QUANTUM-H2/
```

### 3. Cross-Domain Integration
Many components span multiple domains. Use primary domain for classification, then link to related domains:
```
Component: Hydrogen Fuel Tank
Primary Domain: CQH (Cryogenics-Quantum-H2)
Related Domains:
  - AAA (Structural integration)
  - EEE (Electrical bonding)
  - LIB (Supply chain traceability)
```

### 4. Search and Discovery
TFA domains enable efficient search:
- Filter by domain: "Show all PPP components"
- Cross-domain queries: "Components in AAA and CQH with LH2 interfaces"
- Domain-specific experts: "Who owns CQH domain?"

---

## Domain Ownership and Responsibility

Each domain should have clear ownership:
- **Domain Lead**: Overall technical authority
- **CAx Phase Owners**: Responsible for specific lifecycle phases
- **Technical Experts**: Subject matter expertise
- **Quality Reviewers**: Verification and validation

### RACI Matrix Example (AAA Domain)

| Activity | Domain Lead | Structural Engineer | Aero Engineer | Quality |
|----------|------------|---------------------|---------------|---------|
| Design approval | A | R | C | I |
| Structural analysis | A | R | I | C |
| Aero analysis | A | C | R | I |
| Test planning | A | C | C | R |
| Certification | A | I | I | R |

**Legend**: R=Responsible, A=Accountable, C=Consulted, I=Informed

---

## Best Practices

### Domain Selection
- Choose the **most specific** domain that applies
- Use **cross-domain linking** for interfaces
- Document **domain rationale** in passport metadata

### Multi-Domain Components
For components spanning domains:
1. Select **primary domain** (most relevant)
2. Tag **secondary domains** in metadata
3. Create **interface control documents** (ICDs) linking domains
4. Maintain **traceability** across domain boundaries

### Domain Evolution
- Domains are **stable** but can evolve with industry needs
- Propose domain changes through governance process
- Maintain **backward compatibility** during transitions
- Document **domain mapping** for legacy systems

---

## Related Documentation

- [CAx Lifecycle Overview](/docs/cax-lifecycle/) - 9-phase lifecycle
- [Quick Start Guide](/docs/quick-start/) - Creating domain-specific passports
- [QS Technical Specification](/docs/technical/qs-specification/) - Evidence anchoring
- [Glossary](/docs/glossary/) - Domain-related terminology

---

*For questions about TFA domain structure, contact domain leads or [support@ideale-eu.aero](mailto:support@ideale-eu.aero)*
