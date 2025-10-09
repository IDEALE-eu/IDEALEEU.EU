# ATA-46 INFORMATION SYSTEMS - Integration View

## Overview

Information Systems integration covering data loaders (ARINC 615A), application servers, gateways, and cybersecurity appliances (DO-326A/355/356A).

## System Architecture

### Data Loading (ARINC 615A)
- Portable Data Loaders (PDL)
- Onboard Data Loader (ODL)
- Wireless data loading (if applicable)
- Software Part Number (SWPN) management

### Application Servers & Gateways
- Onboard servers for data processing
- Network gateways (ground-to-air)
- Data aggregation and routing
- Flight deck tablet interfaces

### Cybersecurity
- Firewalls and intrusion detection
- Secure data loading (digital signatures, encryption)
- Network isolation and segmentation
- Security event logging and monitoring

## Key Interfaces

### Internal Interfaces
- **46 ↔ 22**: AFCS software loading
- **46 ↔ 23**: Communication system software and connectivity security
- **46 ↔ 24**: Electrical power supply
- **46 ↔ 31**: Display software loading
- **46 ↔ 34**: Navigation database loading
- **46 ↔ 42**: IMA partition and OS loading
- **46 ↔ 44**: Cabin system software and IFE security
- **46 ↔ 45**: CMC software loading and secure data transfer
- **46 ↔ 92**: EWIS (all wiring in ATA-92)

### Data Flows
- Software packages → Data loader → LRUs
- Navigation databases → FMS (ATA-34)
- Maintenance data → Ground systems (via ATA-45)
- Cybersecurity events → Security monitoring systems

## Network Integration

### ARINC 615A Protocol
- Standard software loading protocol
- Digital signatures for software integrity
- Load verification and rollback capability

### Secure Networks
- Isolated cabin network (IFE)
- Secure avionics network (flight-critical systems)
- Firewalls and network segmentation
- Intrusion detection systems

### Wireless Data Loading
- Wi-Fi or cellular connectivity for ground loading
- Secure authentication and encryption
- Progress monitoring and error handling

## Subsystems

### ATA-46-10: DATA LOADING (ARINC 615A)
- Portable Data Loaders
- Onboard Data Loader units
- Software loading protocols
- SWPN management and versioning

### ATA-46-20: APPLICATION SERVERS & GATEWAYS
- Onboard application servers
- Network gateways (ground-to-air, cabin-to-avionics)
- Data aggregation units
- Electronic Flight Bag (EFB) interfaces

### ATA-46-30: CYBERSECURITY APPLIANCE
- Firewalls and network filters
- Intrusion Detection Systems (IDS)
- Secure data loading validation
- Security event monitoring and logging

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/SW_BASELINE/
- **Interfaces**: CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (data load procedures, network diagrams, security policies)

## Compliance

### Applicable Standards
- **ARINC 615A**: Portable Data Loader Software
- **DO-178C**: Software (data loader, cybersecurity software)
- **DO-254**: Hardware (data loaders, servers)
- **DO-160**: Environmental testing
- **DO-326A**: Airworthiness Security Process Specification
- **DO-355**: Information Security Guidance for Continuing Airworthiness
- **DO-356A**: Airworthiness Security Methods and Considerations
- **RTCA DO-355**: Cybersecurity considerations
- **ISO 27001**: Information Security Management

### Certification Considerations
- Software loading criticality (typically DAL C or D)
- Cybersecurity threat assessment
- Network isolation verification
- Secure data loading validation

## Verification Requirements

### Integration Testing
- Software loading to all LRUs
- Navigation database updates
- Cybersecurity firewall rules
- Network isolation verification

### Interface Testing
- ARINC 615A protocol compliance
- Digital signature validation
- Load verification and rollback
- Cybersecurity event detection

### Security Testing
- Penetration testing
- Vulnerability scanning
- Intrusion detection verification
- Data integrity validation

## Known Issues & Risks

### Technical Risks
- Software loading failures causing LRU unavailability
- Cybersecurity vulnerabilities in connected systems
- Navigation database loading errors
- Wireless data loading interference or interruption

### Mitigation Strategies
- Robust error handling and rollback procedures
- Multiple layers of cybersecurity defense (defense-in-depth)
- Database checksum validation
- Wired backup for wireless data loading

## Cybersecurity Integration

### Threat Model
- External threats: Ground-to-air connectivity, cabin Wi-Fi
- Internal threats: Malicious software loading, insider attacks

### Security Domains
1. **Flight-Critical Domain**: No external connectivity, highest security
2. **Airline Domain**: Limited connectivity for operations, moderate security
3. **Passenger Domain**: Public connectivity, isolated from flight-critical systems

### Security Controls
- Network segmentation and firewalls
- Strong authentication for data loading
- Digital signatures for all software
- Encryption for sensitive data
- Security event logging and monitoring

## Data Loading Workflow

### Software Loading Process
1. **Preparation**: Generate SWPN package with digital signature
2. **Transfer**: Load package to PDL or wireless transfer
3. **Validation**: Verify signature and compatibility
4. **Loading**: Transfer software to target LRU
5. **Verification**: Verify successful load and checksum
6. **Activation**: Activate new software (may require power cycle)
7. **Rollback**: Revert to previous version if issues detected

### Database Loading (Navigation, Airport, etc.)
- Similar workflow to software loading
- ARINC 424 format for navigation databases
- Effective dates and expiration management
- Automatic update alerts

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/46↔22_23_24_31_34_42_44_45_92.csv)
- [CONFIGURATION_BASE/ATA-46](../../../CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [Data Load Update Flow](../../03-INTEGRATION_VIEWS/DATA_LOAD_UPDATE_FLOW.md)
- [Data Load Plan Template](../../08-TEMPLATES/DATA_LOAD_PLAN_TEMPLATE.md)
