# Cyber Security Boundaries

## Overview

This document defines cyber security zones, conduits, and cryptographic anchors for the aircraft network per DO-326A airworthiness security requirements.

## Security Architecture

### Defense-in-Depth Strategy
1. **Physical Security** - Locked equipment bays, tamper-evident seals
2. **Network Segmentation** - Zones isolated by firewalls/conduits
3. **Cryptographic Protection** - Encryption and authentication
4. **Access Control** - Role-based access for maintenance/configuration
5. **Monitoring & Logging** - Intrusion detection and audit trails

## Security Zones

### Zone 1: Flight-Critical Domain (DAL A)
**Systems**: Flight Control System, Air Data System, Engine Control
**Trust Level**: Highest - No external connectivity
**Protection**: 
- Physical isolation from all external networks
- AFDX network with no routing to other zones
- Read-only configuration, write-protected memory
- No wireless interfaces permitted
**Access**: Authorized maintenance only via wired connection with MFA

**Systems in Zone 1**:
- FCC-1, FCC-2 (Flight Control Computers)
- ACE-1, ACE-2 (Actuator Control Electronics)
- ADC-1, ADC-2 (Air Data Computers)
- FADEC-1, FADEC-2 (Full Authority Digital Engine Control)
- ENG-ECU-1, ENG-ECU-2 (Engine Electronic Control Units)
- FIRE-DET-1, FIRE-SUPP-1 (Fire Detection and Suppression)
- BRAKE-CTRL-1 (Brake Control)

### Zone 2: Safety-Critical Domain (DAL B)
**Systems**: Navigation, Pressurization, Landing Gear, Oxygen
**Trust Level**: High - Limited external data with validation
**Protection**:
- Separate AFDX VLANs from Zone 1
- Data validation at all zone boundaries
- Controlled conduit to Zone 1 (one-way data flow)
- GNSS receiver inputs subject to spoofing detection
**Access**: Authorized maintenance with MFA and audit logging

**Systems in Zone 2**:
- FMS-1 (Flight Management System)
- GPS-1, GPS-2 (GNSS Receivers)
- IRS-1, IRS-2 (Inertial Reference Systems)
- PRESS-CTRL-1 (Pressurization Control)
- LG-CTRL-1 (Landing Gear Control)
- OXY-CTRL-1 (Oxygen System Control)

### Zone 3: Aircraft Systems Domain (DAL C/D)
**Systems**: Fuel Management, Hydraulics, Lighting, Displays
**Trust Level**: Medium - Monitored connectivity
**Protection**:
- Separate network segment
- Firewall between Zone 3 and Zone 2
- Intrusion detection system (IDS)
- Rate limiting and anomaly detection
**Access**: Authorized personnel with authentication

**Systems in Zone 3**:
- DISPLAY-1, DISPLAY-2 (Cockpit Displays)
- HYD-CTRL-1 (Hydraulic Control)
- FUEL-MGMT-1 (Fuel Management)
- LIGHT-CTRL-1 (Lighting Control)
- CABIN-CTRL-1 (Cabin Management)

### Zone 4: Passenger & Crew Connectivity (Non-Safety)
**Systems**: Passenger WiFi, Crew Tablets, IFE (In-Flight Entertainment)
**Trust Level**: Low - Untrusted
**Protection**:
- Completely isolated from Zones 1, 2, 3
- Separate physical network (no shared switches with aircraft systems)
- Firewall with default-deny policy
- Deep packet inspection (DPI)
- No routing to aircraft operational systems
**Access**: Guest access for passengers, authenticated for crew

**Systems in Zone 4**:
- WiFi Access Points
- IFE servers
- Crew tablets (read-only aircraft data via secure gateway)

### Zone 5: Maintenance & Ground Interface
**Systems**: Ground data loader, wireless maintenance access
**Trust Level**: Controlled - Authenticated and logged
**Protection**:
- Active only on ground (weight-on-wheels interlock)
- Multi-factor authentication required
- All activities logged and audited
- Session timeouts (15 minutes)
- Cryptographic authentication of maintenance devices
**Access**: Authorized maintenance personnel only

**Systems in Zone 5**:
- Ground Data Loader port
- Wireless Maintenance Access Point (ground only)
- Aircraft Condition Monitoring System (ACMS) gateway

## Security Conduits

### Conduit 1-2: Flight Critical ↔ Safety Critical
- **Direction**: Bidirectional with strict filtering
- **Protection**: Hardware-enforced data diode for critical data flow
- **Data Flow Examples**: 
  - Zone 2 → Zone 1: Validated GNSS position, IRS attitude
  - Zone 1 → Zone 2: Flight mode status for display
- **Validation**: All data validated against expected ranges and CRC checked
- **Monitoring**: All traffic logged, anomalies trigger alerts

### Conduit 2-3: Safety Critical ↔ Aircraft Systems
- **Direction**: Bidirectional with firewall
- **Protection**: Stateful firewall, rate limiting
- **Data Flow Examples**:
  - Zone 2 → Zone 3: Nav data for displays
  - Zone 3 → Zone 2: Hydraulic pressure status
- **Validation**: Protocol inspection, whitelist-only traffic
- **Monitoring**: IDS active, alerts on suspicious patterns

### Conduit 3-5: Aircraft Systems ↔ Maintenance (Ground Only)
- **Direction**: Bidirectional, ground-active only
- **Protection**: Weight-on-wheels interlock, authentication gateway
- **Data Flow Examples**:
  - Zone 5 → Zone 3: Software updates, configuration changes
  - Zone 3 → Zone 5: Fault logs, diagnostic data
- **Validation**: Cryptographic signing of all updates, version control
- **Monitoring**: Full session recording, compliance audit trail

### Conduit Isolation: Zone 4 ↔ Aircraft Systems
- **Direction**: NONE - Complete isolation
- **Protection**: No physical or logical connection
- **Exception**: Crew tablets may receive READ-ONLY data (e.g., flight plan, weather) via secure one-way gateway with air-gap
- **Validation**: Any data to crew devices must pass through security gateway with deep inspection
- **Monitoring**: Any attempted connection from Zone 4 to aircraft systems triggers security alert

## Cryptographic Anchors

### Hardware Root of Trust
- **Platform**: Trusted Platform Module (TPM 2.0) or equivalent in each critical LRU
- **Functions**: Secure boot, key storage, cryptographic operations
- **Key Management**: Keys provisioned during manufacturing, never extractable

### Secure Boot
- **Zone 1 & 2 LRUs**: Mandatory secure boot with hardware root of trust
- **Boot Chain**: ROM → Bootloader → OS → Application (each stage verified)
- **Failure Mode**: LRU refuses to boot if signature verification fails, crew alerted

### Cryptographic Algorithms
- **Encryption**: AES-256-GCM for data at rest and in transit (where required)
- **Authentication**: HMAC-SHA-256 for message authentication
- **Digital Signatures**: RSA-3072 or ECDSA P-384 for software signing
- **Key Exchange**: ECDH P-384 for session key establishment (maintenance interfaces)

### Certificate Management
- **PKI**: Internal PKI for aircraft systems
- **Certificate Validity**: 2 years for LRU certificates, 10 years for CA
- **Revocation**: CRL distributed via ground maintenance interface
- **Updates**: Certificates updated during scheduled maintenance

## Intrusion Detection & Monitoring

### Network Monitoring
- **Placement**: Monitoring taps on conduits between zones
- **Detection**: Anomaly detection (ML-based), signature-based rules
- **Alerts**: Real-time alerts to cockpit (critical), maintenance log (non-critical)
- **Logging**: All network traffic metadata logged (not payload for privacy)

### Log Management
- **Collection**: Centralized logging from all zones (except Zone 4)
- **Retention**: 90 days in aircraft non-volatile memory, 7 years on ground
- **Protection**: Logs cryptographically signed and tamper-evident
- **Analysis**: Automated analysis for security events, manual review quarterly

### Security Alerts
- **Critical**: Unauthorized access attempt to Zone 1/2, cockpit alert
- **High**: Anomaly detected in conduit traffic, maintenance alert
- **Medium**: Failed authentication attempt, logged for review
- **Low**: Routine events, logged for audit

## Physical Security

### Equipment Bay Access
- **Locking**: Keyed locks on all equipment bays
- **Tamper Detection**: Tamper-evident seals on critical LRU covers
- **Access Log**: Maintenance log records all bay openings

### Connectors
- **Critical Systems**: Unique connectors prevent mis-wiring
- **Maintenance Ports**: Covered and secured when not in use
- **Key Management**: Physical keys controlled via maintenance security process

## Maintenance Security

### Authenticated Access
- **Credentials**: Smart card + PIN or biometric
- **Roles**: Read-only, Operator, Maintainer, Administrator
- **Principle of Least Privilege**: Users granted minimum necessary access

### Configuration Changes
- **Approval**: All configuration changes require CCB approval (ECR/ECO process)
- **Verification**: Cryptographic signature verification before accepting changes
- **Rollback**: Ability to rollback to last known good configuration

### Software Updates
- **Source Verification**: All software packages cryptographically signed
- **Version Control**: Version management per 06-SOFTWARE_INTEGRATION/BUILD_BASELINES.md
- **Testing**: Updates tested on ground before installation on operational aircraft

## Compliance & Audit

### DO-326A Requirements
- **Threat Identification**: Documented in [08-SAFETY_SECURITY/CYBER_THREATS.md](../../08-SAFETY_SECURITY/CYBER_THREATS.md)
- **Risk Assessment**: Threat log with likelihood and impact per DO-326A
- **Security Controls**: Defense-in-depth as documented herein
- **Assurance**: Security development assurance per DO-326A process

### Audit Trail
- **Access Logs**: All Zone 1/2/3 access logged with timestamp, user, action
- **Configuration Changes**: Full audit trail of all changes (who, what, when, why)
- **Security Events**: All security alerts logged with context
- **Review**: Quarterly security audit, annual penetration testing

## References

- **DO-326A**: Airworthiness Security Process Specification
- **DO-356A**: Airworthiness Security Methods and Considerations
- **[08-SAFETY_SECURITY/CYBER_THREATS.md](../../08-SAFETY_SECURITY/CYBER_THREATS.md)** - Threat analysis
- **[08-SAFETY_SECURITY/SAFETY_CYBER_CROSSWALK.csv](../../08-SAFETY_SECURITY/SAFETY_CYBER_CROSSWALK.csv)** - Safety/security integration

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Cyber Security Team | Initial cyber boundaries per DO-326A |
