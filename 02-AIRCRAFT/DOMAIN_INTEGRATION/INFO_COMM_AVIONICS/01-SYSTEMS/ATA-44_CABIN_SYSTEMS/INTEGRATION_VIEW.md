# ATA-44 CABIN SYSTEMS - Integration View

## Overview

Cabin Systems integration focusing on Information and Communication aspects: In-Flight Entertainment (IFE), cabin connectivity, and associated systems.

**Note**: This domain only covers IFE/Connectivity aspects relevant to information and communication systems. Other cabin systems (seats, galleys, lavatories) are managed in the CABINS_CARGO_PAX domain.

## System Architecture

### In-Flight Entertainment (IFE)
- **Headend System**: Content servers, system management
- **Seat Electronics**: Seatback displays, controllers
- **Audio/Video Distribution**: Content streaming to seats
- **Moving Map**: Flight information display

### Cabin Connectivity
- **Wi-Fi System**: Passenger wireless internet
- **Cellular System**: Mobile phone connectivity (picocell)
- **Cabin Network**: Isolated network for passengers
- **Ground Connectivity**: Satellite or air-to-ground link

### Cabin Crew Systems
- **Cabin Management System**: Lighting, temperature control interfaces
- **Crew Tablets**: Electronic flight bag for cabin crew
- **PA System Integration**: Passenger announcements

## Key Interfaces

### Internal Interfaces
- **44 ↔ 23**: PA system integration, connectivity uplink
- **44 ↔ 24**: Electrical power supply
- **44 ↔ 31**: Flight information for moving map
- **44 ↔ 42**: IMA hosting for IFE applications (if applicable)
- **44 ↔ 46**: Software loading and cybersecurity
- **44 ↔ 92**: EWIS (all wiring in ATA-92)

### Data Flows
- Flight information → IFE moving map
- Passenger data → Ground (via cabin connectivity)
- Content updates → IFE headend
- Cybersecurity events → Security monitoring (ATA-46)

## Network Integration

### Cabin Network (Isolated)
- Physically separated from avionics network
- Firewall protection (ATA-46 cybersecurity)
- Passenger Wi-Fi access points
- IFE content distribution

### Avionics Interface
- One-way data flow: Avionics → Cabin (flight info only)
- No cabin network access to flight-critical systems
- Network isolation verification per DO-326A

## Subsystems

### ATA-44-10: IFE HEADEND & SEAT ELECTRONICS
- Content servers and management systems
- Seatback displays and audio systems
- Passenger control units
- Moving map displays

### ATA-44-20: CABIN Wi-Fi & CONNECTIVITY
- Wi-Fi access points
- Satellite or air-to-ground modems
- Cabin network switches and routers
- Cellular picocell (if applicable)

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/SW_BASELINE/
- **Interfaces**: CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (network topology, content distribution diagrams)

## Compliance

### Applicable Standards
- **DO-178C**: Software (IFE systems, typically DAL D or E)
- **DO-254**: Hardware (IFE controllers, displays)
- **DO-160**: Environmental testing (seat electronics)
- **DO-326A**: Cybersecurity (network isolation, passenger connectivity)
- **DO-355**: Information security for cabin systems
- **ARINC 628**: Aircraft Data Network for cabin systems
- **IEEE 802.11**: Wi-Fi standards

### Certification Considerations
- Network isolation from flight-critical systems (critical safety requirement)
- IFE software criticality (typically DAL D or E - non-safety related)
- Cybersecurity threat assessment per DO-326A
- EMI/EMC compliance for passenger connectivity

## Verification Requirements

### Integration Testing
- Network isolation verification (cabin ↔ avionics)
- IFE content distribution
- Wi-Fi performance and capacity
- Flight information display accuracy

### Interface Testing
- One-way data flow verification (avionics → cabin)
- Firewall rule validation
- Cybersecurity event detection
- PA system integration

### Cybersecurity Testing
- Penetration testing of cabin network
- Firewall bypass attempts
- Intrusion detection verification
- Passenger data protection

## Known Issues & Risks

### Technical Risks
- Network isolation breach (cabin → avionics)
- Cybersecurity vulnerabilities in passenger connectivity
- IFE system interference with avionics
- Wi-Fi performance degradation with high passenger usage

### Mitigation Strategies
- Hardware-enforced network isolation (firewalls, diodes)
- Multiple layers of cybersecurity defense
- EMI/EMC testing per DO-160
- Bandwidth management and QoS for cabin connectivity

## Cybersecurity Architecture

### Network Isolation
- **Physical Separation**: Separate network switches and cabling
- **Firewall**: One-way data flow enforcement
- **Data Diode**: Hardware-enforced one-way communication
- **Monitoring**: Intrusion detection on cabin network

### Threat Mitigation
- Passenger network completely isolated from avionics
- No passenger access to flight-critical data
- Content updates via secure data loading (ATA-46)
- Regular security patches and updates

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/44↔23_24_31_42_46_92.csv)
- [CONFIGURATION_BASE/ATA-44](../../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [ATA-46 Cybersecurity](../ATA-46_INFORMATION_SYSTEMS/SUBSYSTEMS/ATA-46-30_CYBERSECURITY_APPLIANCE/)
- [CABINS_CARGO_PAX Domain](../../CABINS_CARGO_PAX/) (for non-IFE cabin systems)
