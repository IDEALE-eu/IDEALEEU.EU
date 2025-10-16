# Product Requirements Document (PRD) - AMPEL360-AIR-T

## Document Information

| Field | Value |
|-------|-------|
| **Product Name** | AMPEL360-AIR-T (Aircraft Model) |
| **Document ID** | PRD-02-AMPEL360-AIR-T-001 |
| **Version** | 1.0 |
| **Date** | 2025-10-16 |
| **Owner** | AMPEL360-AIR-T Product Manager |
| **Status** | Draft |
| **Parent PRD** | PRD-02-AIRCRAFT-001 |

## 1. Executive Summary

AMPEL360-AIR-T is a next-generation blended wing body (BWB) aircraft with hydrogen-electric propulsion, representing a revolutionary approach to sustainable aviation. This model is part of the IDEALE-EU Aircraft product line and serves as a flagship demonstrator for advanced aerospace technologies.

## 2. Product Overview

### 2.1 Purpose and Scope
- Blended wing body configuration for optimal aerodynamic efficiency
- Hydrogen-electric hybrid propulsion system
- Digital twin integration for predictive maintenance and operations
- Target market: Commercial aviation (100-200 passenger range)
- Configuration: BWB-H2-Hy-E architecture, Q100_STD01 family

### 2.2 Product Context
- Position: Specific aircraft model within 02-AIRCRAFT product line
- Integration: Part of MODEL_IDENTIFICATION TFA structure
- Hierarchy: AMPEL360-AIR-T → ARCH/BWB-H2-Hy-E → FAMILY/Q100_STD01 → 15 Domain lines

### 2.3 Stakeholders
- Launch customer airlines
- Passengers
- EASA and FAA certification authorities
- Hydrogen infrastructure providers
- Maintenance organizations

## 3. Requirements

### 3.1 Functional Requirements

| ID | Requirement | Priority | Verification Method |
|----|-------------|----------|---------------------|
| FR-001 | Aircraft shall operate with BWB aerodynamic configuration | High | Wind tunnel, Flight test |
| FR-002 | Aircraft shall integrate hydrogen storage and fuel cells | High | Ground test, Flight test |
| FR-003 | Aircraft shall achieve 30%+ efficiency improvement | High | Performance analysis, Test |
| FR-004 | Aircraft shall operate from standard airports | High | Ground test, Compatibility study |

### 3.2 Performance Requirements

| ID | Requirement | Target Value | Acceptance Criteria |
|----|-------------|--------------|---------------------|
| PR-001 | Passenger capacity | 100-150 passengers | Configuration verified |
| PR-002 | Range | 3000-4000 km | Flight test verified |
| PR-003 | Cruise speed | Mach 0.78-0.82 | Flight test verified |
| PR-004 | Fuel efficiency improvement | >30% vs A320 | Comparative analysis |
| PR-005 | Hydrogen capacity | TBD kg | Tank design verified |

### 3.3 Interface Requirements

| ID | Interface | Type | Description |
|----|-----------|------|-------------|
| IR-001 | Airport ground power | Electrical | 400Hz, 115/200V |
| IR-002 | Hydrogen refueling | Mechanical/Fluid | LH2 or GH2 compatible |
| IR-003 | Passenger boarding | Mechanical | Standard jetway compatible |
| IR-004 | Cargo loading | Mechanical | Standard ULD compatibility |

### 3.4 Environmental Requirements

Same as parent PRD-02-AIRCRAFT-001, with specific emphasis on:
- Hydrogen system environmental qualification
- BWB-specific acoustic signature
- Thermal management for cryogenic systems

### 3.5 Safety Requirements

| ID | Requirement | Classification | Verification Method |
|----|-------------|----------------|---------------------|
| SR-001 | Hydrogen safety systems | DAL A | ARP4761, Test |
| SR-002 | BWB evacuation capability | 90 seconds | Full-scale demo |
| SR-003 | Structural integrity | CS-25 Subpart C | Static and fatigue test |

### 3.6 Regulatory & Certification Requirements

| ID | Requirement | Regulation/Standard | Compliance Method |
|----|-------------|---------------------|-------------------|
| CR-001 | Type certification | EASA CS-25 | Full certification program |
| CR-002 | Type certification | FAA Part 25 | Full certification program |
| CR-003 | Hydrogen airworthiness | Special conditions | Authority coordination |
| CR-004 | BWB configuration approval | Special conditions | Authority coordination |

## 4. Architecture and Configuration

### 4.1 BWB-H2-Hy-E Architecture
Blended Wing Body with Hydrogen-Electric Hybrid propulsion:
- Central fuselage blended with wings
- Distributed propulsion (boundary layer ingestion)
- Liquid hydrogen tanks in wing structure
- Hybrid-electric power distribution

### 4.2 Q100_STD01 Family Configuration
Standard configuration for ~100 passenger capacity:
- Passenger seating: 2-3-2 or 2-4-2 arrangement
- Cargo: Containerized cargo holds
- Range: Medium-haul missions
- Systems: Standard avionics and systems fit

### 4.3 Domain Integration (15 Domains)

The aircraft integrates 15 specialized engineering domains:

1. **AAA - Airframes, Aerodynamics, Airworthiness**: BWB structure, aerodynamics, certification
2. **AAP - Airport Adaptable Platforms**: Ground operations compatibility
3. **CCC - Cockpit, Cabin, Cargo**: Interior design and systems
4. **CQH - Cryogenics, Quantum, H2**: Hydrogen storage and management
5. **DDD - Drainage, Dehumidification, Drying**: Water management systems
6. **EDI - Electronics, Digital, Instruments**: Avionics and displays
7. **EEE - Electrical, Endotransponders, Circulation**: Electrical power systems
8. **EER - Environmental, Emissions, Remediation**: Environmental compliance
9. **IIF - Industrial, Infrastructure, Facilities**: Manufacturing and support
10. **IIS - Information, Intelligence, Systems**: Data systems and connectivity
11. **LCC - Linkages, Control, Communications**: Flight controls and comms
12. **LIB - Logistics, Inventory, Blockchain**: Supply chain and MRO
13. **MMM - Mechanical, Material, Modules**: Mechanical systems and materials
14. **OOO - OS, Ontologies, Office**: Software and data architecture
15. **PPP - Propulsion, Fuel Systems**: Hybrid-electric propulsion

Each domain contains systems following ATA chapter structure.

## 5. Key Innovations

1. **Blended Wing Body**: 15-20% drag reduction vs conventional
2. **Hydrogen-Electric Propulsion**: Zero CO₂ emissions, hybrid power
3. **Digital Twin**: Real-time monitoring and predictive maintenance
4. **Advanced Materials**: Composites and cryogenic-compatible materials
5. **Distributed Propulsion**: Boundary layer ingestion for efficiency

## 6. Verification and Validation

### 6.1 Verification Approach
- Wind tunnel testing (low-speed, transonic)
- Iron bird systems integration
- Static structural test article
- Fatigue test article
- Ground vibration test
- Flight test program (3-4 aircraft)

### 6.2 Validation Approach
- CFD validation with flight test data
- Digital twin validation with operational data
- Customer validation flights
- Certification flight tests

### 6.3 Traceability
Requirements managed in TFA structure:
- Each domain contains system-level requirements
- Systems traced to ATA chapters
- PLM/CAx artifacts linked to requirements
- Configuration baselines in CONF/BASELINE

## 7. Configuration Management

Managed through TFA (Threading Functional Architecture/Artifact):
```
AMPEL360-AIR-T/
  ARCH/
    BWB-H2-Hy-E/
      FAMILY/
        Q100_STD01/
          DOMAIN/
            [15 domain directories]
              SYSTEMS/
                [ATA chapter systems]
                  SUBSYSTEMS/
                    PLM/CAx/
                    CONF/BASELINE/
```

## 8. PLM/CAx Artifacts

Comprehensive CAx lifecycle artifacts for each domain/system:
- **CAD**: 3D models, assemblies, drawings (CATIA, NX)
- **CAE**: Structural FEA, CFD, thermal analysis
- **CAM**: Manufacturing process definitions, NC programs
- **CAO**: Design optimization data and trade studies
- **CMP**: Compliance documentation and certification artifacts
- **CAP**: Assembly and production planning

All artifacts organized by effectivity and configuration control.

## 9. Risks and Mitigation

| Risk ID | Risk Description | Probability | Impact | Mitigation Strategy |
|---------|------------------|-------------|--------|---------------------|
| R-001 | BWB certification precedent | High | High | Early FAA/EASA engagement, special conditions |
| R-002 | Hydrogen infrastructure readiness | High | Medium | Partner with airports, phased deployment |
| R-003 | Passenger acceptance (BWB cabin) | Medium | Medium | Mock-ups, customer feedback, marketing |
| R-004 | Technology integration complexity | Medium | High | Modular development, extensive testing |
| R-005 | Supply chain for hydrogen components | Medium | Medium | Multiple suppliers, technology maturation |

## 10. Success Criteria

- Type certificate from EASA and FAA
- Performance targets met (range, efficiency, capacity)
- Launch customer acceptance
- Entry into service with dispatch reliability >99%
- Digital twin operational and providing value
- 30%+ efficiency improvement demonstrated
- Hydrogen safety record maintained

## 11. References

### 11.1 Parent Documents
- PRD-02-AIRCRAFT-001: Aircraft product line PRD
- 02-AIRCRAFT/ARCHITECTURE_OVERVIEW.md
- 02-AIRCRAFT/00-README.md

### 11.2 Configuration Documents
- 02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/README.md
- TFA_IMPLEMENTATION_SUMMARY.md
- DOMAIN/README.md (domain-specific)

### 11.3 Standards and References
- EASA CS-25: Large Aeroplanes
- FAA Part 25: Airworthiness Standards
- ARP4754A: Systems development
- ATA iSpec 2200: Maintenance standards

## 12. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | TBD | | |
| Chief Engineer | TBD | | |
| Certification Manager | TBD | | |
| Safety Manager | TBD | | |

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-16 | IDEALE-EU | Initial PRD for AMPEL360-AIR-T model |
