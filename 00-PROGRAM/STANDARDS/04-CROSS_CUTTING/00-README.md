# 04-CROSS_CUTTING

Standards applicable to both aircraft and spacecraft domains.

## Overview

This directory contains standards that apply across both aircraft and spacecraft programs, covering model-based systems engineering, data exchange, digital twins, safety/security, manufacturing, and environmental/materials standards.

## Contents

- **00-README.md** - This file
- **MBSE/** - Model-Based Systems Engineering (ISO/IEC/IEEE 15288, 42010, SysML v2)
- **DATA_EXCHANGE/** - Data exchange standards (ISO 10303 STEP AP242, ReqIF, OSLC, QIF)
- **CONFIG_MGMT/** - Configuration management (ISO 10007, EIA-649C)
- **DIGITAL_TWIN/** - Digital twin standards (ISO 23247, NIST Digital Twin Framework)
- **SAFETY_SECURITY/** - Safety and security for ground systems (IEC 61508, ISO 21434)
- **MANUFACTURING/** - Manufacturing quality standards (ISO 14644, ISO 17025, ISO 45001)
- **ENVIRONMENT_MATERIALS/** - Environmental compliance and materials (REACH, RoHS, ASTM aerospace specs)

## Cross-Domain Applicability

These standards apply to:
- **Aircraft**: Civil aviation development and manufacturing
- **Spacecraft**: Space systems development and operations
- **Ground Systems**: Support equipment, facilities, tools
- **Supply Chain**: Suppliers, subcontractors, partners

## Key Standards Overview

### Model-Based Systems Engineering
- **ISO/IEC/IEEE 15288**: Systems and software engineering - System life cycle processes
- **ISO/IEC/IEEE 42010**: Systems and software engineering - Architecture description
- **SysML v2**: Systems Modeling Language version 2
- **UAF/NAF**: Unified/NATO Architecture Frameworks

### Data Exchange
- **ISO 10303 (STEP)**: Industrial automation systems - Product data representation
  - **AP242**: Managed model-based 3D engineering
- **ReqIF**: Requirements Interchange Format
- **OSLC**: Open Services for Lifecycle Collaboration
- **QIF**: Quality Information Framework

### Configuration Management
- **ISO 10007**: Quality management - Guidelines for configuration management
- **EIA-649C**: National Consensus Standard for Configuration Management
- **CMII**: Configuration Management II best practices

### Digital Twin
- **ISO 23247**: Automation systems and integration - Digital twin framework
- **NIST Digital Twin Framework**: Manufacturing digital twins
- **AIAA Digital Twin Standards**: Aerospace-specific guidance

### Safety and Security
- **IEC 61508**: Functional safety of electrical/electronic/programmable electronic systems
- **ISO 26262**: Road vehicles - Functional safety (applicable to ground systems)
- **ISO 21434**: Road vehicles - Cybersecurity engineering
- **ISO/IEC 27001**: Information security management systems

### Manufacturing
- **ISO 14644**: Cleanrooms and associated controlled environments
- **ISO 17025**: General requirements for testing and calibration laboratories
- **ISO 45001**: Occupational health and safety management systems
- **AS9100**: Quality management systems for aviation, space, and defense

### Environment and Materials
- **REACH**: Registration, Evaluation, Authorization and Restriction of Chemicals (EU)
- **RoHS**: Restriction of Hazardous Substances (EU)
- **ASTM Standards**: Material specifications for aerospace applications
- **ISO 14001**: Environmental management systems

## Integration with Domain-Specific Standards

### Aircraft Integration
- MBSE supports ARP4754A systems engineering
- Data exchange for CAD/PDM/PLM integration
- Configuration management per Part 21 production approval
- Manufacturing per AS9100 and aviation-specific requirements

### Spacecraft Integration
- MBSE supports ECSS-E-ST-10C systems engineering
- Data exchange for spacecraft design and AIT
- Configuration management per ECSS-Q-ST-20C
- Manufacturing per ISO 14644 cleanroom requirements

## Shared Tools and Technologies

- **PLM/PDM Systems**: Siemens Teamcenter, Dassault 3DEXPERIENCE, PTC Windchill
- **MBSE Tools**: Cameo Systems Modeler, Capella, IBM Rhapsody
- **Requirements Management**: DOORS, Jama, Polarion
- **CAD Systems**: CATIA, NX, SolidWorks, Creo
- **Simulation**: ANSYS, COMSOL, MATLAB/Simulink

## Benefits of Cross-Cutting Standards

1. **Consistency**: Common approach across aircraft and spacecraft
2. **Reuse**: Tools, processes, training applicable to both domains
3. **Interoperability**: Seamless data exchange between systems and suppliers
4. **Efficiency**: Avoid duplication of standards and processes
5. **Quality**: Leveraged best practices from both aviation and space industries

## Key Deliverables

Common across aircraft and spacecraft:
1. **Systems Model** - SysML or equivalent MBSE model
2. **Configuration Baseline** - Controlled product definition
3. **Data Exchange Protocols** - STEP files, ReqIF, OSLC interfaces
4. **Digital Twin** - Virtual representation of physical system
5. **Safety Cases** - Functional safety arguments and evidence
6. **Manufacturing Quality Plans** - AS9100 / ISO 9001 compliance
7. **Environmental Compliance** - REACH, RoHS declarations

## Compliance Requirements

- Systems engineering per ISO/IEC/IEEE 15288
- Configuration management per ISO 10007 or EIA-649C
- Data exchange formats per agreed standards (STEP, ReqIF, etc.)
- Manufacturing per AS9100 (aviation) or ISO 9001 (space)
- Environmental compliance per REACH, RoHS, ISO 14001

## Program-Level Integration

- **00-PROGRAM/DIGITAL_THREAD/** - Cross-cutting standards enable digital thread
- **00-PROGRAM/CONFIG_MGMT/** - Configuration management implementation
- **00-PROGRAM/QUALITY_QMS/** - Quality management system based on AS9100
- **00-PROGRAM/SUPPLY_CHAIN/** - Supplier compliance with cross-cutting standards

## Tools and Templates

- MBSE model templates (SysML)
- Configuration management procedures
- Data exchange specifications
- Digital twin architectures
- Quality management system documents

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - Cross-cutting standards (STD-019 through STD-024)
- 05-MAPPINGS/ - Mappings between standards and requirements
- 07-LINKS/OFFICIAL_SOURCES.md - Where to obtain standards

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
