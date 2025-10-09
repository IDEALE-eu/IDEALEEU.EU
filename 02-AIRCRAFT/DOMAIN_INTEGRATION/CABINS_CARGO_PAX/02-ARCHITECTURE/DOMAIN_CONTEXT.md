# Domain Context - CABINS_CARGO_PAX

## Purpose

This document defines the scope, boundaries, and context for the CABINS_CARGO_PAX domain integration.

## Domain Scope

The CABINS_CARGO_PAX domain encompasses all systems related to:

1. **Cabin Interior (ATA-25)**
   - Passenger seating arrangements
   - Galley equipment and installations
   - Lavatory facilities
   - Interior trims and linings
   - Overhead storage bins
   - Floor panels and coverings
   - Passenger Service Units (PSU)
   - Emergency equipment storage and deployment

2. **Cabin Systems (ATA-44)**
   - Cabin Management System (CMS)
   - In-Flight Entertainment (IFE) system
   - Cabin network infrastructure
   - Passenger connectivity (Wi-Fi, cellular)
   - Passenger power outlets (AC/DC, USB)
   - Cabin lighting control systems

3. **Cargo Systems (ATA-50)**
   - Main deck cargo handling
   - Lower deck cargo systems
   - Unit Load Devices (ULDs) and locks
   - Power Drive Units (PDUs)
   - Load sensing and monitoring
   - Cargo control electronics

## Domain Boundaries

### Within Scope

- Physical cabin interior components and furnishings
- Passenger-facing systems and interfaces
- Cargo loading and restraint systems
- Integration of cabin and cargo systems with aircraft systems
- Passenger experience optimization
- Cabin and cargo operational procedures
- Weight and balance considerations for cabin/cargo
- Interface definitions with other aircraft systems

### Outside Scope

- **ATA-21 (ECS)**: Air conditioning and pressurization systems (referenced only)
- **ATA-24 (Electrical)**: Primary power generation and distribution (interface only)
- **ATA-26 (Fire)**: Fire detection and suppression systems (interface only)
- **ATA-33 (Lighting)**: Primary aircraft lighting (interface only)
- **ATA-38 (Water/Waste)**: Water supply and waste systems (interface only)
- **ATA-42 (IMA)**: Integrated Modular Avionics platform (hosting only)
- **ATA-92 (EWIS)**: Electrical wiring (physical implementation)

### Grey Areas (Coordination Required)

1. **Cabin Lighting**
   - Cabin lighting fixtures: ATA-44 (control) + ATA-33 (power)
   - Emergency lighting: ATA-25 (equipment) + ATA-33 (system)

2. **Galley Systems**
   - Galley structure and equipment: ATA-25
   - Water supply: ATA-38 interface
   - Power distribution: ATA-24 interface

3. **Lavatory Systems**
   - Lavatory structure: ATA-25
   - Water and waste: ATA-38 interface
   - Ventilation: ATA-21 interface
   - Smoke detection: ATA-26 interface

## Domain Context Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    CABINS_CARGO_PAX DOMAIN                  │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   ATA-25    │  │   ATA-44    │  │   ATA-50    │      │
│  │ Equipment & │  │   Cabin     │  │   Cargo &   │      │
│  │ Furnishings │  │  Systems    │  │Load Systems │      │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘      │
│         │                │                │              │
│         └────────────────┴────────────────┘              │
│                          │                                │
└──────────────────────────┼────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌─────▼─────┐    ┌─────▼─────┐
    │ ATA-21  │      │  ATA-24   │    │  ATA-26   │
    │   ECS   │      │Electrical │    │   Fire    │
    └─────────┘      └───────────┘    └───────────┘
```

## Key Integration Points

### Passenger Experience Integration

1. **Seat-to-IFE Integration**
   - Physical mounting and routing
   - Power distribution
   - Data connectivity

2. **PSU-to-Cabin Systems Integration**
   - Light control
   - Attendant call
   - Air nozzle (ATA-21 interface)
   - Oxygen mask deployment (ATA-35 interface)

3. **Galley-to-Aircraft Systems**
   - Power requirements (ATA-24)
   - Water supply (ATA-38)
   - Ventilation (ATA-21)
   - Circuit protection and isolation

### Cargo Integration

1. **Cargo-to-Aircraft Structure**
   - Floor mounting and reinforcement
   - Load path analysis
   - Structural integration

2. **Cargo-to-Fire Detection**
   - Smoke detector placement (ATA-26)
   - Fire suppression coverage (ATA-26)
   - System monitoring integration

3. **Load Management Integration**
   - Weight and balance system (ATA-31)
   - Load sensing feedback
   - Center of gravity calculation

## Operational Context

### Passenger Operations

- Boarding and seating
- In-flight service (galley operations)
- Entertainment and connectivity
- Lavatory usage
- Emergency procedures
- Deplaning

### Cargo Operations

- Load planning
- Cargo loading/unloading
- ULD management
- Load verification
- Security procedures
- Hazmat handling

### Maintenance Context

- Line maintenance access
- Component replacement procedures
- Cabin reconfiguration
- IFE software updates
- Cargo system inspection
- Emergency equipment checks

## Stakeholder Context

### Internal Stakeholders

- **Flight Operations**: Cabin operational procedures, cargo loading
- **Cabin Crew**: Galley equipment, passenger services, safety equipment
- **Maintenance**: Accessibility, maintainability, troubleshooting
- **Engineering**: Design, integration, certification
- **Configuration Management**: Baseline control, change management

### External Stakeholders

- **Passengers**: Comfort, entertainment, connectivity
- **Airlines (Customers)**: Customization, branding, configuration flexibility
- **Cargo Operators**: Efficiency, capacity, compatibility
- **Regulators**: Safety, certification, compliance
- **Suppliers**: OEM equipment, integration requirements

## Performance Context

### Passenger Experience Metrics

- Seat comfort and ergonomics
- IFE availability and performance
- Connectivity bandwidth and reliability
- Galley equipment functionality
- Lavatory availability and cleanliness

### Cargo Performance Metrics

- Loading/unloading time
- Cargo capacity utilization
- ULD compatibility
- Load accuracy
- System reliability

## Design Constraints

### Physical Constraints

- Available cabin space envelope
- Cargo compartment dimensions
- Weight limitations per zone
- Center of gravity limits
- Emergency exit requirements

### Regulatory Constraints

- FAR Part 25 compliance
- EASA CS-25 compliance
- Emergency evacuation requirements
- Flammability requirements (FAR 25.853)
- Crash worthiness (FAR 25.561/562)

### Operational Constraints

- Turnaround time requirements
- Maintenance accessibility
- Reconfiguration flexibility
- Crew training complexity
- Passenger service standards

## References

- [Dependencies](./DEPENDENCIES.md)
- [Data Contracts](./DATA_CONTRACTS.md)
- [Safety Boundaries](../01-GOVERNANCE/SAFETY_BOUNDARIES.md)
- [ATA-25 Configuration](../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/)
- [ATA-44 Configuration](../../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/)
- [ATA-50 Configuration](../../../CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/)

---

**Last Updated**: 2025-01-15
