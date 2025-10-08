# MBSE

Model-Based Systems Engineering standards.

## Overview

Model-Based Systems Engineering (MBSE) is a formalized approach to systems engineering using models as the primary artifact. This directory contains standards for MBSE practices applicable to both aircraft and spacecraft.

## Applicable Standards

### ISO/IEC/IEEE 15288:2023 - Systems and Software Engineering - System Life Cycle Processes
- **Scope**: Comprehensive lifecycle processes for systems
- **Coverage**: Technical processes, technical management, organizational processes
- **Key Processes**:
  - Stakeholder needs and requirements definition
  - System requirements definition
  - Architecture definition
  - Design definition
  - System analysis
  - Implementation, integration, verification, validation

### ISO/IEC/IEEE 42010:2022 - Systems and Software Engineering - Architecture Description
- **Scope**: Frameworks for architecture description
- **Concepts**: Stakeholders, concerns, viewpoints, views, models
- **Architecture Description Language (ADL)**: SysML, AADL, UML

### SysML v2 - Systems Modeling Language version 2
- **Scope**: General-purpose modeling language for systems engineering
- **Notation**: Graphical and textual syntax
- **Diagram Types**: Requirements, structure, behavior, parametrics
- **Tool Support**: Cameo, Capella, others

### UAF/NAF - Unified/NATO Architecture Frameworks
- **Scope**: Enterprise and system-of-systems architectures
- **Views**: Strategic, operational, services, systems, standards
- **Use Cases**: Defense, aerospace, complex systems

## MBSE Benefits

- **Single Source of Truth**: Model replaces documents as primary artifact
- **Consistency**: Automated consistency checking
- **Traceability**: Requirements to design to verification
- **Communication**: Visual models improve stakeholder understanding
- **Analysis**: Simulation, trade studies, verification
- **Reuse**: Modular architectures, standard libraries

## MBSE Practices

### Requirements Modeling
- Capture functional and non-functional requirements
- Allocate requirements to subsystems and components
- Trace requirements through design and verification
- Derive lower-level requirements from system requirements

### Architecture Modeling
- Define system architecture (logical, physical)
- Decompose system into subsystems and components
- Define interfaces between elements
- Allocate functions to components

### Behavior Modeling
- Model system behavior (state machines, activity diagrams, sequence diagrams)
- Simulate nominal and off-nominal scenarios
- Verify timing and performance
- Analyze fault propagation

### Parametric Modeling
- Define constraints and equations
- Link parameters across system
- Perform trade studies and optimization
- Verify budgets (mass, power, data, etc.)

## SysML Diagram Types

### Requirements Diagram
- Capture requirements and their relationships
- Derive, satisfy, verify, refine relationships

### Block Definition Diagram (BDD)
- Define system structure (blocks, components)
- Composition, aggregation, generalization

### Internal Block Diagram (IBD)
- Define internal structure and interfaces
- Ports, connectors, flows

### Activity Diagram
- Model behavior and workflows
- Control flow, data flow, swimlanes

### Sequence Diagram
- Model interactions between components
- Messages, lifelines, timing

### State Machine Diagram
- Model state-based behavior
- States, transitions, events, guards

### Parametric Diagram
- Model equations and constraints
- Constraint blocks, bindings

## MBSE Tools

- **Cameo Systems Modeler** (No Magic / Dassault Systèmes)
- **Capella** (Thales, open-source)
- **IBM Engineering Systems Design Rhapsody**
- **PTC Integrity Modeler** (formerly Artisan Studio)
- **Sparx Enterprise Architect**

## Integration with Other Standards

### Aircraft (ARP4754A)
- MBSE supports system development per ARP4754A
- Requirements allocation, architecture definition, V&V planning
- Interface with DO-178C (software) and DO-254 (hardware)

### Spacecraft (ECSS-E-ST-10C)
- MBSE supports system engineering per ECSS
- Interfaces, budgets, verification control documents (VCD)
- Integration with ECSS software and hardware standards

## Key Deliverables

1. **Systems Model** - Complete SysML or equivalent model
2. **Requirements Database** - All requirements captured in model
3. **Architecture Views** - Logical and physical architectures
4. **Behavior Models** - State machines, activities, sequences
5. **Parametric Models** - Budgets, constraints, trade studies
6. **Interface Specifications** - All interfaces defined in model
7. **Traceability Matrix** - Requirements to design to verification

## Best Practices

- Start with simple models, grow incrementally
- Establish model structure and conventions early
- Use reference architectures and libraries
- Automate document generation from model
- Version control model in PLM/PDM
- Train team in MBSE and tool usage
- Integrate with requirements management and PLM systems

## Common Pitfalls

- Over-modeling (too much detail too early)
- Inconsistent naming conventions
- Poor model structure (hard to navigate)
- Model not maintained (diverges from reality)
- Tool focus instead of method focus
- Lack of stakeholder buy-in

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-019 (ISO 15288), STD-020 (ISO 42010)
- INCOSE Systems Engineering Handbook
- SysML v2 specification: https://www.omg.org/spec/SysML/
- 07-LINKS/TRAINING_MATERIALS.md - MBSE training courses

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
