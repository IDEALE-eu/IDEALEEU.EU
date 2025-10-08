# 04-MBSE

Model-Based Systems Engineering (MBSE) repository and requirements traceability.

## Purpose

This directory serves as the central hub for MBSE activities, including SysML models, baselines, interface definitions, and requirements allocation. It provides the authoritative source for system architecture and requirements traceability.

## Contents

- **00-README.md** - This file
- **SYSML_MODELS/** - Central SysML model repository (or links to external MBSE tools like Cameo/Capella)
- **MODEL_BASELINES/** - Symbolic links or manifests pointing to configuration baselines in CONFIG_MGMT/04-BASELINES/
- **INTERFACE_DEFINITIONS/** - Auto-generated Interface Control Documents (ICDs) from MBSE models
- **REQUIREMENTS_ALLOCATION.csv** - Requirements allocation matrix (SysML block ↔ requirement ID, ReqIF-compatible)

## MBSE Approach

### Modeling Language
- **Primary**: SysML v2.0 (Object Management Group standard)
- **Alternative**: SysML v1.x during transition period
- **Notation**: Standard SysML notation per 02-STANDARDS/STANDARDS.md

### Tooling
- **Recommended Tools**:
  - Cameo Systems Modeler (Dassault Systèmes)
  - Capella (Eclipse Foundation, open-source)
  - IBM Engineering Systems Design Rhapsody
  - PTC Windcill Modeler (integrated with PLM)

### Model Organization
- **Aircraft Models**: System architecture, domains (Airframes, Propulsion, Avionics, etc.)
- **Spacecraft Models**: Subsystems (GNC, Power/Thermal, Propulsion, etc.)
- **Shared Models**: Common interfaces, standards, reusable components

## Model Structure

### System Architecture Views

**Structural Views**
- Block Definition Diagrams (BDD): System hierarchy and composition
- Internal Block Diagrams (IBD): Internal connectivity and interfaces
- Package Diagrams: Model organization

**Behavioral Views**
- Activity Diagrams: Operational sequences and flows
- State Machine Diagrams: System modes and transitions
- Sequence Diagrams: Interactions between components
- Use Case Diagrams: System functionality and actors

**Requirement Views**
- Requirement Diagrams: Requirements hierarchy and relationships
- Requirement Tables: Tabular requirements with attributes
- Satisfaction Relationships: Requirements satisfaction by design elements

**Parametric Views**
- Parametric Diagrams: Constraints and equations
- Trade Study Models: Design space exploration

## Requirements Management

### Requirements Hierarchy
```
Level 0: Stakeholder Needs
Level 1: System Requirements
Level 2: Subsystem Requirements
Level 3: Component Requirements
Level 4: Interface Requirements
```

### Requirements Attributes
- **ID**: Unique identifier (e.g., SYS-REQ-001)
- **Text**: Requirement statement
- **Rationale**: Why the requirement exists
- **Verification Method**: Test, Analysis, Inspection, Demonstration
- **Priority**: Critical, High, Medium, Low
- **Status**: Proposed, Approved, Implemented, Verified
- **Allocation**: Allocated to which system/subsystem block

### Traceability
- **Upward Trace**: Requirement → Parent requirement
- **Downward Trace**: Requirement → Child requirements
- **Satisfaction Trace**: Requirement → Design element (SysML block)
- **Verification Trace**: Requirement → Verification procedure → Test result
- **Validation Trace**: Design element → Digital twin model

## Interface Management

### Interface Control Documents (ICDs)
- Auto-generated from SysML IBD and port definitions
- Includes: Signal types, data rates, protocols, physical connectors
- Aligned with CONFIG_MGMT/09-INTERFACES/

### Interface Types
- **Physical Interfaces**: Mechanical, electrical, thermal
- **Functional Interfaces**: Data, control, power
- **Environmental Interfaces**: Thermal, vibration, EMI/EMC

## Baselines and Configuration Management

### Model Baselines
- Baselines are established at major stage gates (PDR, CDR, etc.)
- MODEL_BASELINES/ contains manifests or symbolic links to CONFIG_MGMT/04-BASELINES/
- Baseline includes: Model version, requirements snapshot, ICD versions

### Change Management
- Model changes follow configuration control process
- Change requests linked to requirements and design elements
- Impact analysis automated via traceability

## Integration with Digital Thread

### Upstream Integration
- **Requirements Management**: Import from DOORS, Polarion, etc. via ReqIF
- **Stakeholder Input**: Use case models from stakeholder workshops

### Downstream Integration
- **CAD/CAE**: Design constraints and parameters exported to CAD tools
- **Digital Twin**: MBSE models as basis for behavioral digital twin models (05-DIGITAL_TWIN/)
- **Manufacturing**: Interface definitions used for work instructions
- **Test**: Verification procedures generated from requirements

### Continuous Synchronization
- Automated validation of requirements allocation (≥95% allocated)
- Automated generation of ICDs from model changes
- Automated traceability gap analysis

## Verification and Validation

### Model Verification (Are we building the model right?)
- Syntax checking (SysML metamodel compliance)
- Consistency checking (no orphaned requirements, complete allocations)
- Completeness checking (all system elements modeled)

### Model Validation (Are we building the right model?)
- Stakeholder reviews
- Simulation and analysis
- Correlation with digital twin predictions
- Trade study results validation

## Compliance

### Standards Compliance
- SysML v2 compliance (02-STANDARDS/STANDARDS.md)
- ReqIF compliance for requirements interchange
- ECSS-E-ST-10 compliance for spacecraft systems engineering

### Quality Metrics
- Requirements traceability coverage: Target ≥99%
- Model completeness: Target 100% of system elements modeled
- Interface definition coverage: Target 100% of interfaces documented
- Verification method defined: Target 100% of requirements

## Training and Support

### Required Training
- SysML Fundamentals (40 hours)
- Tool-specific training (Cameo/Capella, 24 hours)
- Requirements management (16 hours)
- Digital thread integration (8 hours)

### Best Practices
- Use standard SysML patterns and stereotypes
- Maintain model documentation and rationale
- Regular model reviews and peer checks
- Version control for all model artifacts

## Related Documents

- **01-STRATEGY/STRATEGY.md** - MBSE strategic approach
- **02-STANDARDS/STANDARDS.md** - SysML and ReqIF standards
- **03-ARCHITECTURE/INTEGRATION_POINTS.md** - MBSE readiness at stage gates
- **05-DIGITAL_TWIN/** - Digital twin models derived from MBSE
- **CONFIG_MGMT/** - Configuration management integration
