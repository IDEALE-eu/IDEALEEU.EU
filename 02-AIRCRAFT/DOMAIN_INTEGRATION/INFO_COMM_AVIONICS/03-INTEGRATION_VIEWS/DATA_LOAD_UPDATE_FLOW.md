# DATA LOAD & UPDATE FLOW

Software part numbers (SWPNs), secure data loading, digital signatures, and cryptographic keys.

## Overview

This document describes the process for loading software and databases to avionics Line Replaceable Units (LRUs) using ARINC 615A protocol, including security measures (digital signatures, encryption) per DO-326A.

## Data Loading Architecture

### Loading Methods

#### 1. Portable Data Loader (PDL)
- **Type**: Handheld device or laptop
- **Interface**: Wired connection to aircraft data loading port
- **Use Case**: Software updates on the ground
- **Bandwidth**: 10-100 Mbps

#### 2. Onboard Data Loader (ODL)
- **Type**: Permanently installed loader
- **Interface**: Integrated with avionics network
- **Use Case**: In-flight database updates (limited)
- **Bandwidth**: 100 Mbps (AFDX)

#### 3. Wireless Data Loading
- **Type**: Wi-Fi or cellular connection
- **Interface**: Secure wireless link
- **Use Case**: Ground operations (not in-flight)
- **Bandwidth**: 1-10 Mbps (variable)

## ARINC 615A Protocol

### Protocol Layers
1. **Physical Layer**: Ethernet (typically)
2. **Network Layer**: IP
3. **Transport Layer**: TCP
4. **Application Layer**: ARINC 615A

### Load Session Workflow

```
1. Initiate Load Session
   ↓
2. Authenticate Loader
   ↓
3. Verify Software Compatibility
   ↓
4. Verify Digital Signature
   ↓
5. Transfer Software Package
   ↓
6. Verify Checksum
   ↓
7. Activate Software (or schedule activation)
   ↓
8. Verify Successful Load
   ↓
9. Close Load Session
```

## Software Part Number (SWPN) Management

### SWPN Structure
```
SWPN Format: XXXXX-YYY-ZZZ-AA
  XXXXX = System identifier (e.g., FMS, AFCS)
  YYY   = Major version
  ZZZ   = Minor version
  AA    = Build number
```

### SWPN Database
- Master SWPN database in CONFIG_MGMT/08-ITEM_MASTER/
- Each SWPN linked to:
  - Certification status (approved, test, obsolete)
  - Compatible hardware part numbers
  - Prerequisites (other software that must be loaded first)
  - Supersession information

### Version Control
- All SWPNs version-controlled in CONFIG_MGMT
- Change history tracked via ECR/ECO process
- Baselines identified by SWPN sets

## Security and Digital Signatures

### Digital Signature Process

#### 1. Software Package Creation
```
1. Compile/build software
2. Generate package file (e.g., ZIP, TAR)
3. Compute cryptographic hash (SHA-256)
4. Sign hash with private key (RSA 2048-bit or higher)
5. Attach signature to package
```

#### 2. Signature Verification (on aircraft)
```
1. Receive software package
2. Extract signature
3. Compute hash of received package
4. Verify signature with public key
5. Compare computed hash with signed hash
6. Accept package if match, reject if mismatch
```

### Cryptographic Keys

#### Key Types
- **Private Key**: Held securely by software publisher (OEM)
- **Public Key**: Embedded in target LRU (non-extractable)
- **Key Algorithm**: RSA 2048-bit minimum (or ECDSA P-256)

#### Key Management
- Public keys provisioned during LRU manufacturing
- Private keys stored in Hardware Security Module (HSM)
- Key expiration and rotation per security policy
- Certificate chain for trust validation

### Encryption (for sensitive data)
- **Algorithm**: AES-256
- **Mode**: GCM (Galois/Counter Mode)
- **Key Exchange**: TLS 1.2 or higher for session establishment

## Data Loading by System

### FMS Navigation Database (ATA-34)
- **Format**: ARINC 424 (navigation database standard)
- **Update Cycle**: 28 days (AIRAC cycle)
- **Size**: 50-200 MB
- **Loading Time**: 5-15 minutes
- **Criticality**: DAL C (must have current database)

### IMA Software (ATA-42)
- **Components**: IMA OS, partition images
- **Size**: 100-500 MB
- **Loading Time**: 15-30 minutes
- **Criticality**: DAL A (IMA OS), varies by partition
- **Special Procedure**: Requires aircraft power cycle for activation

### AFCS Software (ATA-22)
- **Components**: Control laws, mode logic
- **Size**: 10-50 MB
- **Loading Time**: 5-10 minutes
- **Criticality**: DAL B or C
- **Special Procedure**: Requires flight control check after load

### Communication Software (ATA-23)
- **Components**: ACARS, CPDLC, radio firmware
- **Size**: 10-30 MB
- **Loading Time**: 5-10 minutes
- **Criticality**: DAL C or D

### Display Software (ATA-31)
- **Components**: Display symbology, rendering engine
- **Size**: 50-150 MB
- **Loading Time**: 10-20 minutes
- **Criticality**: DAL B or C

## Load Verification

### Automatic Verification
- Checksum verification (CRC-32 or SHA-256)
- SWPN compatibility check
- Digital signature validation
- Post-load Built-In Test (BIT)

### Manual Verification
- Display software version on EICAS/ECAM
- Compare with intended SWPN
- Perform functional checks per maintenance manual

### Rollback Procedure
- If load fails verification, automatically rollback to previous version
- Previous version stored in LRU non-volatile memory
- Manual rollback available via PDL

## Compliance and Certification

### DO-326A Cybersecurity
- Software loading is a security-critical function
- Digital signatures mandatory for all flight-critical software
- Secure boot process verifies software integrity

### DO-178C Software
- Data loading software (PDL, ODL) certified to DAL C or D
- Target LRU software loader certified per LRU criticality

### ARINC 615A Compliance
- Protocol conformance testing
- Interoperability testing with multiple loader types

## Data Loading Procedures

### Pre-Load Checklist
1. Verify aircraft on ground (not in flight)
2. Verify electrical power available
3. Verify loader has correct SWPN package
4. Verify digital signature of package
5. Record current software versions

### Load Execution
1. Connect loader to aircraft
2. Initiate load session
3. Monitor progress on loader display
4. Verify successful completion
5. Perform post-load BIT

### Post-Load Checklist
1. Verify new software version on display
2. Perform functional checks
3. Update aircraft logbook
4. Update configuration database (CONFIG_MGMT)

## Known Issues & Risks

### Technical Risks
- Load interruption (power loss, cable disconnect)
- Incompatible software versions
- Corrupted load files
- Cybersecurity vulnerabilities

### Mitigation Strategies
- Automatic rollback on load failure
- Pre-load compatibility checks
- Redundant load files (backup copies)
- Regular security audits and penetration testing

## Related Documents

- [ATA-46 Information Systems](../01-SYSTEMS/ATA-46_INFORMATION_SYSTEMS/INTEGRATION_VIEW.md)
- [Data Load Plan Template](../08-TEMPLATES/DATA_LOAD_PLAN_TEMPLATE.md)
- [CONFIG_MGMT Software Baseline](../../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)
- [Cybersecurity Policy](../06-COMPLIANCE/STANDARDS_MAP.md)

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial data loading architecture |
