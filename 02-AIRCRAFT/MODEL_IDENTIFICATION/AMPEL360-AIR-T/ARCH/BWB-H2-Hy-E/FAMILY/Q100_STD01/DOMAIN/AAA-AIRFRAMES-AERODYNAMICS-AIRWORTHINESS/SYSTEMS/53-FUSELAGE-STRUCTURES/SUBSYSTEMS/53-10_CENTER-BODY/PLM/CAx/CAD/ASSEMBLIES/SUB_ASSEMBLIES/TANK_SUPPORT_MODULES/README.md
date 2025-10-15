# TANK_SUPPORT_MODULES — Fuel Tank Support Sub-Assemblies

## Purpose

This directory contains sub-assembly models for fuel tank support structures within the 53-10 Center Body. These assemblies provide structural support, load distribution, and interface provisions for integral or bladder fuel tanks in the fuselage.

## Tank Support Types

### Center Wing Box Tanks
- **Carry-through tank**: Center section fuel storage
- **Surge tanks**: Fuel expansion and vent collection
- **Collector tanks**: Fuel pump supply tanks

### Fuselage Integral Tanks
- **Belly tanks**: Lower fuselage auxiliary fuel tanks
- **Tail cone tanks**: Aft auxiliary fuel or trim tanks
- **Tip tanks**: Horizontal stabilizer or wing tip tanks

### Bladder Tank Supports
- **Bladder cradles**: Support structure for flexible bladder tanks
- **Retention frames**: Peripheral support and retention
- **Anti-slosh baffles**: Internal tank baffles and structure

## Tank Support Components

A typical tank support assembly includes:
- **Tank support beams**: Primary load-bearing structure
- **Tank bulkheads**: Tank-forming or tank-sealing bulkheads
- **Attach fittings**: Connection to primary fuselage structure
- **Access provisions**: Panels for tank inspection and maintenance
- **Sump structure**: Low point for fuel drainage
- **Vent provisions**: Tank venting and pressure relief
- **Baffle supports**: Internal structure for anti-slosh baffles

## Naming Convention

Use the following pattern for tank support assemblies:
```
53-10_ASM_TANK-SUPPORT_<tank-location>_v<version>.<ext>
```

Examples:
- `53-10_ASM_TANK-SUPPORT_CENTER-WING_v01.CATProduct`
- `53-10_ASM_TANK-SUPPORT_BELLY-TANK-01_v02.asm`
- `53-10_ASM_TANK-SUPPORT_TAIL-TRIM_v01.sldasm`

## Design Considerations

### Structural Design
- Design for fuel weight (full and empty conditions)
- Include maneuvering and crash loads on fuel mass
- Design for thermal expansion of fuel and structure
- Include provisions for tank pressure/vacuum
- Validate fatigue life under fuel sloshing

### Tank Interface
- Define tank attachment points and methods
- Specify sealing provisions (integral tanks)
- Include drain and sump provisions
- Design for tank inspection and cleaning access
- Provide for fuel quantity probes and sensors

### Load Cases
- **Static loads**: Fuel weight at maximum capacity
- **Inertia loads**: Maneuvering accelerations (6g up, 3g down, 4g lateral)
- **Crash loads**: Emergency landing conditions (16g forward, 9g up)
- **Sloshing loads**: Dynamic fuel motion during flight
- **Thermal loads**: Fuel temperature variations

## Integral Tank Sealing

For integral fuel tanks (wet tanks):
- **Sealant application**: Faying surfaces and fasteners
- **Sealant type**: Fuel-resistant polysulfide or other approved
- **Joint design**: Lap joints with proper edge distance
- **Fastener sealing**: Wet installation of fasteners
- **Leak testing**: Pressure or vacuum leak test procedures

## Integration Points

Tank support modules interface with:
- **Frame sections**: Tank boundary frames
- **Floor modules**: Tank upper surface (floor structure)
- **Skin panels**: Tank lower surface (belly skin)
- **Bulkhead modules**: Tank end bulkheads
- **Fuel system (ATA-28)**: Pumps, lines, valves, and sensors
- **Vent system**: Tank venting and pressure control

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Floor modules**: [`../FLOOR_MODULES/`](../FLOOR_MODULES/)
- **Bulkhead modules**: [`../BULKHEAD_MODULES/`](../BULKHEAD_MODULES/)
- **Skin panel modules**: [`../SKIN_PANEL_MODULES/`](../SKIN_PANEL_MODULES/)
- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Design Guidelines

### Tank Capacity
- Calculate tank volume and fuel capacity
- Account for unusable fuel (sump and lines)
- Include fuel expansion allowance (2-3%)
- Document fuel quantity indication system
- Validate CG travel with fuel burn-off

### Baffles and Anti-Slosh
- Design baffles to limit fuel sloshing
- Ensure adequate openings for fuel flow
- Design for structural loads from fuel impact
- Include access for baffle installation
- Validate effectiveness through analysis or testing

### Crashworthiness
- Design for crash loads per FAR 25.561
- Include provisions to prevent fuel spillage
- Design for separation of fuel and ignition sources
- Include fire protection in post-crash scenario
- Document emergency fuel dump provisions (if applicable)

## Fuel System Integration

### Fuel System Components
- **Boost pumps**: In-tank fuel pumps
- **Scavenge pumps**: Transfer pumps for auxiliary tanks
- **Fuel quantity probes**: Capacitance or ultrasonic sensors
- **Vent system**: Overboard vents and NACA inlets
- **Drain valves**: Sump drains for maintenance

### Installation Provisions
- Mounting points for pumps and sensors
- Electrical bonding for all components
- Access for component removal and replacement
- Wire/tube routing supports
- Lightning protection and grounding

## Certification Requirements

### Structural Testing
- Static load test to ultimate (full tank at limit load factor)
- Crash test for fuel containment
- Fatigue test for design life
- Sloshing test or analysis validation
- Thermal cycling test

### Fuel System Testing
- Leak test at operating pressure and vacuum
- Functional test of fuel system
- Fuel flow and transfer testing
- Vent system capacity testing
- Lightning protection testing

### Fire Safety
- Demonstrate post-crash fire safety
- Validate fuel system fire protection
- Test fire detection and suppression (if installed)
- Document compliance with FAR 25.863 (flammable fluid systems)

## Metadata Requirements

Each tank support assembly should include:
- **Part number**: Following 53-10 numbering system
- **Description**: Tank location and type
- **Tank capacity**: Usable and total capacity (gallons or liters)
- **Tank material**: Integral (sealed structure) or bladder
- **Design pressure**: Maximum tank pressure (psi)
- **Material**: Primary materials and sealants
- **Mass properties**: Dry weight and CG
- **Full weight**: Weight with full fuel load
- **Status**: Design state (draft, released, obsolete)

## Manufacturing Considerations

### Integral Tank Construction
- Apply sealant to all faying surfaces
- Wet-install all fasteners in tank
- Cure sealant per manufacturer specifications
- Leak test after assembly
- Document leak test results

### Bladder Tank Installation
- Install bladder support cradle first
- Install anti-chafing material
- Install bladder and secure retention
- Connect fuel lines and vents
- Perform functional test

## Maintenance Considerations

Design for maintainability:
- Tank inspection access (entry if required)
- Component replacement access
- Sump drainage for water removal
- Fuel sampling provisions
- Leak detection and repair access

## Special Considerations

### Fuel Type Compatibility
- Design for specified fuel type (Jet-A, Jet-A1, etc.)
- Material compatibility with fuel and additives
- Seal material selection for fuel resistance
- Document fuel specifications

### Lightning Protection
- Provide adequate electrical bonding
- Include lightning strike protection
- Design for fuel vapor ignition prevention
- Document grounding and bonding verification

## Quality Assurance

Critical quality checks:
- Sealant application completeness (integral tanks)
- Leak test at specified pressure
- Electrical bonding continuity
- Component installation and torque verification
- Tank capacity verification (if possible)
- Documentation of all repairs or rework

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design reviews and leak tests
- Document capacity or configuration changes
- Maintain revision history for each tank support
- Coordinate changes with ATA-28 fuel system owner
