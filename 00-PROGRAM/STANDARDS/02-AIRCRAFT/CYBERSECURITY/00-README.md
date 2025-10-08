# CYBERSECURITY

Cybersecurity standards for aircraft systems.

## Overview

This directory contains standards for cybersecurity in civil aviation, including DO-326A, DO-355, DO-356A, EU Aviation Cybersecurity Certificate (ACSC), and related standards.

## Applicable Standards

### DO-326A - Airworthiness Security Process Specification
- **Scope**: Process for managing security aspects of aircraft systems
- **Purpose**: Integrate security into aircraft lifecycle
- **Integration**: Works with ARP4754A, DO-178C, DO-254

### DO-355 - Information Security Guidance for Continuing Airworthiness
- **Scope**: Security considerations for in-service aircraft
- **Purpose**: Maintain security posture throughout operational life
- **Topics**: Vulnerability management, security updates, incident response

### DO-356A - Airworthiness Security Methods and Considerations
- **Scope**: Methods and techniques for security analysis and development
- **Purpose**: Practical guidance for implementing DO-326A
- **Methods**: Threat modeling, security requirements, verification

### EU Aviation Cybersecurity Certificate (ACSC)
- **Authority**: EASA
- **Scope**: Cybersecurity certification for aircraft systems
- **Requirements**: Based on DO-326A/355/356A

### ISO/SAE 21434 - Road vehicles — Cybersecurity engineering
- **Applicability**: Ground systems, support equipment
- **Scope**: Cybersecurity lifecycle management
- **Integration**: Common approach with automotive industry

### NIST SP 800-171 - Protecting Controlled Unclassified Information
- **Applicability**: Design data, certification data protection
- **Scope**: Information security for non-federal systems
- **Requirements**: 110 security controls

## Security Lifecycle

```
Security Plan
    ↓
Threat Assessment → Asset Identification → Threat Analysis → Risk Assessment
    ↓
Security Requirements
    ↓
Security Development → Security Design → Implementation → Verification
    ↓
Security Validation → Penetration Testing → Vulnerability Assessment
    ↓
In-Service Security → Monitoring → Updates → Incident Response
```

## Airworthiness Security Process (ASRP)

### Key Activities
1. **Security Planning**: Define security objectives, resources, schedule
2. **Security Requirements**: Derive from threat assessment
3. **Security Development**: Design and implement security controls
4. **Security Verification**: Verify controls meet requirements
5. **Security Validation**: Validate effectiveness against threats
6. **Security Installation**: Deploy in operational environment
7. **Security Maintenance**: Update, patch, respond to incidents

## Threat Modeling

### Asset Identification
- Critical aircraft functions
- Data assets (flight plans, navigation data, certificates)
- Communication interfaces (datalink, Wi-Fi, satcom)
- Ground systems interfaces

### Threat Sources
- Opportunistic attackers
- Motivated attackers (terrorism, espionage)
- Insiders
- Supply chain compromise

### Attack Vectors
- Wireless interfaces (Wi-Fi, Bluetooth, cellular)
- Wired interfaces (USB, maintenance ports)
- Software updates and loading
- Supply chain (hardware/software trojans)

## Security Controls

### Design-Level Controls
- Secure boot and trusted execution
- Encryption (data at rest, in transit)
- Authentication and access control
- Security monitoring and logging
- Secure communication protocols
- Input validation and sanitization

### Operational Controls
- Security configuration management
- Vulnerability management
- Incident response procedures
- Security training and awareness
- Physical security

## Security Requirements

Security requirements derived from:
- Threat assessment results
- Regulatory requirements (EASA, FAA)
- Industry best practices
- Lessons learned from incidents

Requirements categorized by:
- Security level (similar to DAL)
- Asset criticality
- Threat likelihood and impact

## Security Verification

Methods include:
- **Security Testing**: Functional testing of security controls
- **Penetration Testing**: Ethical hacking to find vulnerabilities
- **Vulnerability Scanning**: Automated scanning tools
- **Code Review**: Security-focused code inspection
- **Configuration Audit**: Verify secure configuration
- **Fuzz Testing**: Invalid input testing

## Key Deliverables

1. **Security Plan** - Overall security approach and process
2. **Threat Assessment** - Assets, threats, risks
3. **Security Requirements** - Derived security requirements
4. **Security Architecture** - High-level security design
5. **Security Verification Report** - Test results, findings
6. **Security Case** - Argument for acceptable security
7. **Security Configuration Management** - Baseline and change control

## Compliance Requirements

- Aircraft systems shall follow DO-326A process
- Security requirements derived from threat assessment
- Security verification proportional to risk
- Continued airworthiness per DO-355
- EASA ACSC for applicable systems

## Integration with Other Standards

- **ARP4754A** - Security integrated into systems engineering
- **ARP4761** - Security threats considered in safety assessment
- **DO-178C** - Secure software development practices
- **DO-254** - Hardware security features
- **DO-160** - Physical security and tamper resistance

## Emerging Threats

- Connected aircraft (Internet, satcom)
- Electronic Flight Bag (EFB) security
- Wireless avionics (Bluetooth, Wi-Fi)
- Supply chain risks (hardware/software)
- AI/ML security (adversarial attacks)

## Tools and Templates

- Threat modeling templates
- Security requirements templates
- Penetration test procedures
- Incident response playbooks

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-007 (DO-326A), STD-024 (ISO 21434)
- 06-INTERPRETATIONS/AUTHORITY_POSITION_PAPERS/EASA_SIB_2020-08.md
- 07-LINKS/TRAINING_MATERIALS.md - Cybersecurity training

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
