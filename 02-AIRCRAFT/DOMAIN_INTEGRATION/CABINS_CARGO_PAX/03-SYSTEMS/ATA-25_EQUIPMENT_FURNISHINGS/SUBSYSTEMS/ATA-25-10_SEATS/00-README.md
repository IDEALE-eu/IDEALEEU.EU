# ATA-25-10 Seats - Subsystem

## Overview

Passenger and crew seating systems including seat structures, cushions, mechanisms, and mounting hardware.

## Scope

- Passenger seats (economy, premium economy, business, first class)
- Crew seats (flight attendant jump seats)
- Seat mechanisms (recline, tray tables, armrests)
- Seat upholstery and cushions
- In-seat power and USB integration points
- IFE screen mounting provisions

## PLM_CAX Directory Structure

### CAD/ - Computer-Aided Design
- 3D models of seat assemblies
- Individual component models
- Assembly drawings
- Installation drawings

### CAE/ - Computer-Aided Engineering
- Structural analysis (FEA)
- Crash worthiness simulations (16g)
- Dynamic analysis

### CAO/ - Computer-Aided Optimization
- Weight optimization studies
- Material selection optimization
- Ergonomics optimization

### CAM/ - Computer-Aided Manufacturing
- Manufacturing process plans
- Tooling designs
- NC programming data

### CAI/ - Computer-Aided Inspection
- Inspection plans and procedures
- CMM programs
- Quality control specifications

### CAV/ - Computer-Aided Visualization
- Renderings and visualizations
- Marketing materials
- Virtual mockups

### CAP/ - Computer-Aided Planning
- Production planning
- Assembly sequence planning
- Logistics planning

### CAS/ - Computer-Aided Simulation
- Passenger comfort simulations
- Thermal comfort analysis
- Acoustic simulations

### CMP/ - Computer-Aided Manufacturing Process
- Process simulation
- Assembly process validation
- Cycle time analysis

### METADATA/
- File metadata and properties
- Configuration IDs
- Version history
- Change tracking

## Key Interfaces

### Structural (ATA-51)
- Seat track attachment (16g forward, 9g lateral)
- Floor load distribution
- Load path to airframe

### Electrical (ATA-24)
- Power for seat controls (28V DC)
- USB charging ports (5V DC, 2.4A)
- 110V AC outlets (premium classes)

### IFE (ATA-44-20)
- Screen mounting provisions
- Screen power connections
- Screen control interface

## Design Requirements

### Regulatory
- FAR 25.561 - Emergency landing dynamic conditions
- FAR 25.562 - Emergency landing dynamic conditions
- FAR 25.853 - Compartment interiors (flammability)
- TSO-C127 - Rotorcraft, Transport Airplane, and Normal and Utility Airplane Seats

### Performance
- Service life: 40,000 flight cycles
- Flammability: Meet FAR 25.853 requirements
- Weight target: [Per configuration]
- Comfort: Ergonomic design per airline requirements

## INTERFACES.md

Detailed interface specifications are in: `./INTERFACES.md`

## TESTS/

Test procedures and results including:
- Static load testing
- Dynamic crash testing
- Flammability testing
- Durability cycling
- Environmental testing

## Configuration Reference

Baseline configuration maintained in:
- [ATA-25 Configuration Base](../../../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/)

## Suppliers

Seat supplier information managed through procurement system.

---

**Last Updated**: 2025-01-15
