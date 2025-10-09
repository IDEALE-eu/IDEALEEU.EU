# MOUNTING_UNITS — Equipment Mounting Unit Sub-Assemblies

## Purpose

This directory contains sub-assembly models for equipment mounting units within the 53-10 Center Body. Mounting units provide structural attachment points for systems, equipment, and installations throughout the fuselage.

## Mounting Unit Types

### System Installations
- **Avionics racks**: Electronic equipment mounting
- **ECS equipment**: Environmental control system components
- **Hydraulic components**: Pumps, reservoirs, and actuators
- **Electrical equipment**: Generators, transformers, and power panels
- **Pneumatic equipment**: Air conditioning and pressurization components

### Interior Installations
- **Overhead bins**: Passenger storage compartment supports
- **Galley modules**: Galley equipment mounting structure
- **Lavatory units**: Lavatory fixture support structure
- **Seat tracks**: Already covered in FLOOR_MODULES, but may include special provisions
- **Monument installations**: Class dividers, closets, and specialty areas

### Special Equipment
- **Emergency equipment**: Life raft and emergency equipment brackets
- **Fire extinguisher brackets**: Required fire suppression equipment
- **Oxygen system**: Passenger and crew oxygen system mounting
- **Communication equipment**: Antennas and communication system mounting

## Mounting Unit Components

A typical mounting unit assembly includes:
- **Mounting brackets**: Primary attachment fittings
- **Reinforcement plates**: Local structure reinforcement
- **Vibration isolators**: Damping mounts for equipment
- **Cable/pipe supports**: Routing supports near equipment
- **Access provisions**: Removable panels or covers
- **Grounding provisions**: Electrical bonding points

## Naming Convention

Use the following pattern for mounting unit assemblies:
```
53-10_ASM_MOUNT_<system>-<equipment>-<location>_v<version>.<ext>
```

Examples:
- `53-10_ASM_MOUNT_ECS-PACK-FWD_v01.CATProduct`
- `53-10_ASM_MOUNT_AVIONICS-RACK-01_v02.asm`
- `53-10_ASM_MOUNT_GALLEY-AFT-RIGHT_v01.sldasm`

## Design Considerations

### Load Analysis
- Determine equipment weight and CG
- Calculate operating loads (vibration, maneuvering)
- Design for ultimate loads (1.5x limit loads typical)
- Include crash loads (emergency landing conditions)
- Validate fatigue life for vibrating equipment

### Attachment Design
- Design for accessible fastener installation
- Include provisions for equipment removal
- Design for adjustment and shimming
- Specify torque requirements
- Include locking features for critical fasteners

### Vibration Isolation
For vibrating equipment:
- Specify isolator type and characteristics
- Design for isolator deflection and travel
- Include snubbers for overload protection
- Validate natural frequency separation
- Design for fail-safe (isolator failure) condition

## Integration Points

Mounting units interface with:
- **Frame sections**: Bracket-to-frame attachments
- **Floor modules**: Floor-mounted equipment
- **Bulkhead modules**: Bulkhead-mounted equipment
- **Skin panels**: Skin-mounted attachments (rare)
- **Systems installations**: Cable and pipe routing to/from equipment

## Load Paths

Equipment mounting loads:
- **Vertical loads**: Equipment weight (1g to 16g emergency)
- **Lateral loads**: Maneuvering and turbulence (typically 3-6g)
- **Longitudinal loads**: Braking and acceleration (9g forward emergency)
- **Vibration loads**: Cyclic loads from operating equipment
- **Thermal loads**: Thermal expansion of equipment and structure

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Floor modules**: [`../FLOOR_MODULES/`](../FLOOR_MODULES/)
- **Bulkhead modules**: [`../BULKHEAD_MODULES/`](../BULKHEAD_MODULES/)
- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Design Guidelines

### Structural Adequacy
- Design for ultimate loads per FAR/CS 25.561
- Include proper load path to primary structure
- Avoid eccentric loading where possible
- Use appropriate fastener types and sizes
- Include redundancy for critical equipment

### Accessibility
- Design for equipment installation and removal
- Provide maintenance access to fasteners
- Include provisions for cable/pipe connections
- Plan for equipment testing and adjustment
- Consider ground handling and transportation

### Standardization
- Use standard bracket designs where possible
- Maintain library of proven mounting designs
- Standardize fastener types and sizes
- Use common vibration isolators
- Document standard mounting practices

## Equipment Interface

### Physical Interface
- Define equipment footprint and envelope
- Specify mounting hole pattern
- Document electrical grounding requirements
- Include thermal interface (if required)
- Define fluid connection points (if applicable)

### Functional Interface
- Specify cable routing and support
- Define cooling air requirements
- Document drainage provisions (if required)
- Include environmental protection (moisture, dust)
- Specify maintenance access requirements

## Certification Requirements

### Structural Testing
- Static strength test to ultimate load
- Vibration testing of isolator systems
- Crash simulation for critical equipment
- Fatigue testing of high-cycle equipment
- Pull test of critical fasteners

### System Integration
- Equipment operation during flight test
- Vibration survey in aircraft
- Thermal testing under operating conditions
- EMI/EMC testing for electronic equipment
- Functional testing of installed equipment

## Metadata Requirements

Each mounting unit assembly should include:
- **Part number**: Following 53-10 numbering system
- **Description**: Equipment type and location
- **Equipment ID**: Installed equipment part number
- **Load rating**: Maximum allowable loads
- **Vibration isolation**: Isolator specifications (if used)
- **Material**: Primary materials and finishes
- **Mass properties**: Bracket weight and CG
- **Status**: Design state (draft, released, obsolete)

## Installation Planning

### Installation Sequence
- Determine when to install mounting (early or late)
- Coordinate with systems installation schedule
- Plan for access requirements during install
- Include provisions for alignment and shimming
- Document torque sequence for multi-fastener mounts

### Tooling Requirements
- Specify installation tooling (standard or custom)
- Document torque wrench requirements
- Include alignment fixtures if needed
- Plan for lifting/handling fixtures (heavy equipment)
- Provide installation procedure documentation

## Safety Considerations

Critical safety items:
- Secure attachment of life-critical equipment
- Redundant mounting for single-point failures
- Fire protection of mounting in fire zones
- Emergency equipment accessibility
- Proper electrical bonding and grounding

## Quality Assurance

Critical quality checks:
- Fastener torque verification
- Vibration isolator installation check
- Electrical bonding continuity test
- Equipment alignment and leveling
- Clearance verification to adjacent structure/systems

## Special Mounting Types

### Heavy Equipment
For equipment >100 lbs (45 kg):
- Design for lifting and handling
- Include provisions for temporary support during install
- Specify rigging points and procedures
- Validate floor/structure strength
- Document center of gravity limits

### Precision-Mounted Equipment
For equipment requiring precise alignment:
- Include alignment provisions (shims, adjusters)
- Specify alignment tolerances
- Document alignment procedure
- Include survey points for measurement
- Plan for alignment verification after installation

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design reviews and load analyses
- Document equipment or load changes
- Maintain revision history for each mounting unit
- Coordinate changes with equipment owner and systems integrator
