# Interface Matrix - ATA-44 Cabin Systems

## Purpose

This document defines all interfaces between ATA-44 subsystems and external aircraft systems.

## Interface Overview Matrix

| ATA-44 Subsystem | External System | Interface Type | Criticality | ICD Reference |
|------------------|-----------------|----------------|-------------|---------------|
| CMS | ATA-42 (IMA) | Hosted application | Critical | ICD-44-10-42 |
| CMS | ATA-24 (Electrical) | Power distribution | Critical | ICD-44-10-24 |
| CMS | ATA-33 (Lighting) | Lighting control | Normal | ICD-44-10-33 |
| CMS | ATA-25 (PSU) | Control signals | Normal | ICD-44-10-25 |
| IFE | ATA-42 (IMA) | Network connectivity | Normal | ICD-44-20-42 |
| IFE | ATA-24 (Electrical) | Power distribution | Critical | ICD-44-20-24 |
| IFE | ATA-25 (Seats) | Physical mounting | Normal | ICD-44-20-25 |
| Cabin Network | ATA-42 (IMA) | AFDX backbone | Critical | ICD-44-30-42 |
| Cabin Network | ATA-92 (EWIS) | Cable routing | Normal | ICD-44-30-92 |
| Connectivity | External (Satellite) | Data link | Normal | ICD-44-40-EXT |
| Connectivity | ATA-24 (Electrical) | Power for antennas | Normal | ICD-44-40-24 |
| Passenger Power | ATA-24 (Electrical) | Power distribution | Critical | ICD-44-50-24 |
| Passenger Power | ATA-25 (Seats) | Outlet installation | Normal | ICD-44-50-25 |
| Lighting Control | ATA-33 (Lighting) | Control interface | Normal | ICD-44-60-33 |
| Lighting Control | ATA-24 (Electrical) | Power distribution | Critical | ICD-44-60-24 |

## Interface Details

### ATA-24: Electrical Power

**Power Requirements:**
- CMS servers: 28V DC, 500W redundant
- IFE system: 115V AC, 400Hz, 5kW total
- Network switches: 28V DC, 200W per switch
- Connectivity equipment: 28V DC, 1kW
- Passenger USB: 5V DC via converters, 2.4A per port
- Lighting control: 28V DC, 100W

**Power Quality:**
- Voltage regulation: ±10%
- Transient protection per DO-160
- EMI filtering per DO-160

**Reference:**
- [ATA-24 Configuration](../../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/)

---

### ATA-25: Equipment & Furnishings

**PSU Control Interface:**
- Reading light control
- Attendant call signal
- Seat lighting control
- Physical mounting in PSU structure

**IFE Physical Integration:**
- Screen mounting in seat backs
- Control unit mounting in armrests
- Cable routing through seat structure

**Passenger Power Integration:**
- USB ports in seats
- AC outlets in seats (premium classes)
- Physical integration with seat design

**Reference:**
- [ATA-25 Equipment](../ATA-25_EQUIPMENT_FURNISHINGS/)

---

### ATA-33: Lighting

**CMS Lighting Control:**
- Cabin overhead lighting scenes
- Zone-based control
- Dimming control (0-100%)
- Color temperature control (2700-6500K)

**Control Signals:**
- Digital control via ARINC 664
- Discrete signals for critical functions
- Manual override capability

**Reference:**
- [ATA-33 Configuration](../../../../CONFIGURATION_BASE/ATA-33_LIGHTS/)

---

### ATA-42: Integrated Modular Avionics (IMA)

**CMS Hosting:**
- Partition allocation on IMA
- Processing resources
- Memory allocation
- I/O channels

**Network Connectivity:**
- ARINC 664 (AFDX) connections
- Guaranteed bandwidth
- Quality of Service (QoS)
- Redundancy and failover

**IFE Backend:**
- Data processing on IMA (optional)
- Content distribution
- User data management

**Reference:**
- [ATA-42 Configuration](../../../../CONFIGURATION_BASE/ATA-42_IMA/)

---

### ATA-92: EWIS

**Cable Routing:**
- Cabin network cabling
- Power distribution to cabin systems
- IFE wiring harnesses
- Antenna cables

**Note:** Physical wiring documented in ATA-92.

**Reference:**
- [ATA-92 EWIS](../../../../CONFIGURATION_BASE/ATA-92_EWIS/)

---

### External Interfaces

**Satellite Connectivity:**
- Antenna placement (fuselage mounted)
- RF requirements
- Data link specifications
- Service provider interfaces

**Ground Services:**
- Content loading interface
- Software update interface
- Maintenance interface
- Ground power compatibility

## Data Interfaces

### CMS Data Exchange
- System status monitoring
- Cabin sensor data
- Control commands
- Fault reporting

### IFE Data Flow
- Content streaming
- User session management
- Billing and usage data
- Software updates

### Connectivity Data
- Internet traffic routing
- Bandwidth management
- Authentication and security
- Usage tracking

**See:** [Data Contracts](../../../02-ARCHITECTURE/DATA_CONTRACTS.md)

## Network Architecture

### Backbone
- ARINC 664 (AFDX) for CMS critical data
- Ethernet for IFE and connectivity
- Redundant switches and paths

### Bandwidth Allocation
| System | Guaranteed | Burst |
|--------|-----------|-------|
| CMS | 10 Mbps | 20 Mbps |
| IFE Backend | 100 Mbps | 200 Mbps |
| Connectivity | 100 Mbps | 500 Mbps |
| Monitoring | 10 Mbps | 20 Mbps |

## Interface Change Control

Follow process in:
- [Change Rules](../../../01-GOVERNANCE/CHANGE_RULES.md)
- [Interface Management](../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

## Interface Verification

1. ICD review and approval
2. Bench testing of interfaces
3. Integration lab testing
4. Aircraft-level testing
5. Flight testing

## References

- [Domain Dependencies](../../../02-ARCHITECTURE/DEPENDENCIES.md)
- [Data Contracts](../../../02-ARCHITECTURE/DATA_CONTRACTS.md)
- [ICD Index](../../../05-LINKS/ICD_INDEX.md)

---

**Last Updated**: 2025-01-15
