# DATA_EXCHANGE

Data exchange and interoperability standards.

## Overview

This directory contains standards for exchanging data between organizations, systems, and tools throughout the product lifecycle.

## Applicable Standards

### ISO 10303 (STEP) - Standard for the Exchange of Product Model Data
- **Scope**: Neutral format for CAD/CAE/CAM data exchange
- **AP242**: Managed model-based 3D engineering (current standard for aerospace)
- **Benefits**: Vendor-neutral, preserves design intent, long-term archival

**Application Protocols**:
- **AP203**: Configuration controlled 3D design (legacy, being replaced by AP242)
- **AP214**: Automotive design (cars)
- **AP242**: Managed model-based 3D engineering (aerospace, defense)

### ReqIF - Requirements Interchange Format
- **Scope**: Exchange requirements between tools (DOORS, Jama, Polarion, etc.)
- **Format**: XML-based
- **Benefits**: Preserve traceability, links, attributes
- **Use Cases**: Supplier requirements handoff, tool migration, collaboration

### OSLC - Open Services for Lifecycle Collaboration
- **Scope**: Web services for tool integration
- **Domains**: Requirements, change management, quality, architecture
- **Benefits**: Real-time integration, avoid data duplication
- **Protocols**: RESTful APIs, RDF, linked data

### QIF - Quality Information Framework
- **Scope**: Exchange inspection and quality data
- **Format**: XML-based
- **Benefits**: Automated quality workflows, first article inspection (FAI)
- **Use Cases**: CMM measurement results, inspection reports, manufacturing quality

## STEP AP242

### Capabilities
- 3D geometry (solids, surfaces, wireframe)
- Product structure (assemblies, parts)
- Product and manufacturing information (PMI)
  - Geometric dimensioning and tolerancing (GD&T)
  - Material specifications
  - Surface finish
- Configuration management
- Design history and parametrics

### Workflow
1. **Export**: CAD tool exports STEP AP242 file
2. **Validate**: Check file for completeness and correctness
3. **Exchange**: Send file to partner/supplier
4. **Import**: Partner imports into their CAD system
5. **Verify**: Check geometry and PMI preserved

### Validation
- STEP file analyzer tools (CAx-IF, etc.)
- Check for missing entities, errors
- Visual inspection of imported geometry

## ReqIF

### Structure
- **ReqIF Core**: Specification objects, attributes, datatypes
- **ReqIF Links**: Relationships between requirements
- **ReqIF Exchange**: Packaging for exchange

### Use Cases
- **Supplier Handoff**: Send requirements to suppliers in neutral format
- **Tool Migration**: Move data between requirements tools
- **Multi-Party Collaboration**: Share requirements across organizations

### Workflow
1. **Export**: Export requirements from tool A as ReqIF
2. **Validate**: Check ReqIF file for completeness
3. **Exchange**: Send ReqIF file to partner
4. **Import**: Partner imports into tool B
5. **Map**: Map attributes and links between tools

## OSLC

### Architecture
- **Resources**: Requirements, defects, test cases represented as web resources
- **Services**: Create, read, update, delete (CRUD) operations via HTTP
- **Linking**: Hyperlinks between resources (e.g., requirement → test case)

### Benefits
- Real-time integration (no batch file exchange)
- Avoid data duplication (single source of truth)
- Tool-agnostic (any tool supporting OSLC can integrate)

### Example Integrations
- DOORS ↔ Polarion (requirements sync)
- Jira ↔ DOORS (defect tracking to requirements)
- Cameo ↔ DOORS (model elements to requirements)
- Jenkins ↔ Jama (build status to requirements)

## Data Exchange Best Practices

### Governance
- Define data ownership and responsibility
- Establish exchange frequency (real-time, daily, weekly)
- Version control exchanged data
- Audit trail of exchanges

### Quality
- Validate data before exchange
- Check for completeness and correctness
- Maintain traceability through exchange
- Handle errors and exceptions gracefully

### Security
- Encrypt sensitive data
- Access control (who can send/receive)
- Audit logging
- Compliance with export control (ITAR, EAR)

### Interoperability
- Agree on standards and versions
- Document mappings between systems
- Test exchanges before production use
- Maintain compatibility with legacy systems

## PLM/PDM Integration

### Data Types
- **CAD Models**: STEP AP242 for 3D geometry
- **Requirements**: ReqIF for requirements data
- **Documents**: PDF/A for long-term archival
- **Metadata**: Dublin Core, ISO 15836

### PLM Systems
- Siemens Teamcenter
- Dassault Systèmes 3DEXPERIENCE
- PTC Windchill
- SAP PLM
- Aras Innovator

### Integration Patterns
- **File-Based**: Export/import files (STEP, ReqIF)
- **API-Based**: RESTful APIs, SOAP, OSLC
- **Database-Level**: Direct database access (not recommended)

## Key Deliverables

1. **Data Exchange Specification** - Formats, frequency, protocols
2. **STEP AP242 Files** - 3D CAD models and PMI
3. **ReqIF Files** - Requirements data
4. **OSLC Services** - API endpoints and documentation
5. **QIF Files** - Inspection and quality data
6. **Data Mapping Documents** - Field mappings between systems
7. **Validation Reports** - Data quality checks

## Compliance Requirements

- Data exchange per agreed standards (STEP, ReqIF, OSLC)
- Data quality verified before exchange
- Traceability maintained through exchanges
- Security and export control compliance
- Archival in neutral formats for long-term access

## Integration with Other Standards

- **ISO/IEC/IEEE 15288** - Data exchange supports lifecycle processes
- **ISO 10007 / EIA-649C** - Configuration management of exchanged data
- **AS9100** - Quality requirements for data exchange

## Tools and Software

- **STEP Tools**: CAx-IF, Jotne EDM Model Checker
- **ReqIF Tools**: ReqIF Studio, Visure Requirements
- **OSLC Tools**: Eclipse Lyo, OSLC adapters
- **Validation**: STEP file analyzers, ReqIF validators

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-022 (ISO 10303-242)
- ISO 10303-242 standard (purchase from ISO)
- ReqIF specification: https://www.omg.org/spec/ReqIF/
- OSLC: https://open-services.net/
- QIF: https://qifstandards.org/

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
