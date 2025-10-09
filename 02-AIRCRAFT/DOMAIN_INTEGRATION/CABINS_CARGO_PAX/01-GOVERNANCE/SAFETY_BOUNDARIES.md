# Safety Boundaries - CABINS_CARGO_PAX Domain

## Purpose

This document defines the safety boundaries and constraints for the CABINS_CARGO_PAX domain to ensure all activities remain within acceptable safety limits.

## Safety-Critical Systems

### High Priority (Safety-Critical)

1. **Emergency Equipment (ATA-25-80)**
   - Emergency exits and slides
   - Life vests and flotation devices
   - Fire extinguishers
   - Emergency lighting

2. **Cargo Restraint Systems (ATA-50)**
   - ULD locks and restraints
   - Load sensing systems
   - Cargo fire detection integration

3. **Cabin Fire Protection**
   - Smoke detection in lavatories
   - Fire suppression systems
   - Emergency egress systems

### Medium Priority (Safety-Related)

1. **Structural Furnishings**
   - Seat attachments and strength
   - Floor structures
   - Overhead bin restraints

2. **Passenger Safety Equipment**
   - Seatbelts and restraints
   - Oxygen system integration
   - Emergency signage

3. **Cargo Load Management**
   - Weight and balance systems
   - Load distribution monitoring

## Safety Boundaries

### Design Boundaries

| System | Boundary Condition | Limit | Rationale |
|--------|-------------------|-------|-----------|
| Seats | Maximum load | 16g forward, 9g side | FAR 25.561/562 |
| Overhead Bins | Maximum load | 50 lb/sq ft | Structural limits |
| Emergency Exits | Minimum width | Per FAR 25.807 | Evacuation requirements |
| Cargo Restraints | Breaking strength | Per FAR 25.787 | Load retention |
| Galley Power | Maximum load | Per electrical system capacity | Fire risk mitigation |

### Operational Boundaries

1. **Cabin Configuration**
   - Maximum passenger capacity per emergency exits
   - Minimum aisle width requirements
   - Exit row seating restrictions

2. **Cargo Operations**
   - Maximum load per compartment
   - Load distribution limits
   - Hazardous material restrictions

3. **System Operations**
   - IFE system independent of critical systems
   - Cabin lighting backup requirements
   - Emergency power priorities

## Interface Safety Requirements

### Critical Interfaces

1. **ATA-21 (ECS)**
   - Lavatory ventilation failure modes
   - Galley exhaust requirements
   - Smoke detection integration

2. **ATA-24 (Electrical)**
   - Circuit protection and isolation
   - Emergency power distribution
   - Short circuit containment

3. **ATA-26 (Fire Protection)**
   - Cargo compartment fire detection
   - Lavatory smoke detectors
   - Fire suppression coordination

4. **ATA-38 (Water/Waste)**
   - Water system contamination prevention
   - Waste system leak containment
   - Chemical storage safety

## Failure Mode Constraints

### Unacceptable Failure Modes

1. **Structural Failure**
   - Seat detachment during crash
   - Floor panel failure
   - Overhead bin release during flight

2. **Fire Safety Degradation**
   - Disabled fire detection
   - Blocked emergency exits
   - Compromised fire suppression

3. **Cargo Safety**
   - ULD release in flight
   - Cargo fire undetected
   - Load shift beyond limits

### Acceptable with Mitigation

1. IFE system failure (no safety impact)
2. Individual seat entertainment failure
3. Non-critical lighting failure (backup available)
4. Galley equipment failure (isolated circuits)

## Safety Analysis Requirements

All changes affecting the following require Safety Assessment:

1. Structural modifications to seats, floors, or bins
2. Changes to emergency equipment or exits
3. Modifications to fire detection or suppression
4. Cargo restraint system changes
5. Weight and balance system modifications
6. Critical interface changes (power, fire, ECS)

## Compliance References

- **FAR Part 25**: Airworthiness standards for transport category airplanes
- **FAR 25.561/562**: Emergency landing dynamic conditions
- **FAR 25.787**: Cargo compartment classification
- **FAR 25.807**: Emergency exits
- **FAR 25.853**: Compartment interiors (flammability)
- **EASA CS-25**: Equivalent European standards

## Safety Review Process

1. Design Safety Review at PDR
2. Failure Modes and Effects Analysis (FMEA)
3. System Safety Assessment at CDR
4. Integration Safety Review
5. Certification Safety Review

## Contacts

- **Safety Lead**: Safety Engineering Team
- **Certification Lead**: Certification Engineering
- **Domain Safety Officer**: Cabin & Cargo Safety Engineer

---

**Last Updated**: 2025-01-15
