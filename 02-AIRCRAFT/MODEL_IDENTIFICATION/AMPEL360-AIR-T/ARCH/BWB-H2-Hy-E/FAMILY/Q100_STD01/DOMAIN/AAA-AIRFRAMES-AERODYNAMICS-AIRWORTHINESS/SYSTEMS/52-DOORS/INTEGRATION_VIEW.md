# Integration View — ATA-52 Doors

## Overview
The ATA-52 Doors system encompasses all aircraft doors, hatches, and access panels, including mechanisms, seals, sensors, and control systems.

## Interfaces

### Structural Interfaces
- **53 Fuselage Structure**: Door frames, mounting provisions, load paths
- **57 Wing**: Service panels and access hatches in wing structures

### Systems Interfaces
- **21 ECS (Environmental Control)**: Pressurization sealing, leak rate management, cabin pressure coordination
- **24 Electrical**: Power supply, bonding/grounding, electrical protection
- **25 Cabin**: Emergency slides, lighting trim, interior furnishings
- **26 Fire Protection**: Fire detection and suppression interfaces
- **29 Hydraulic**: Hydraulic actuation for powered doors
- **31 Indicating/Recording**: Door status indication, EICAS messages, cockpit displays
- **33 Lighting**: Door area lighting, emergency lighting integration
- **36 Pneumatic**: Pneumatic actuation systems (if applicable)
- **42 IMA**: Discrete signals, data bus integration (ARINC-429/AFDX)
- **92 EWIS**: Wiring harnesses, connector provisions, harness keep-out zones

## Key Concerns

### Safety Critical
- **Fail-safe latching**: Multiple independent locking mechanisms
- **Indication integrity**: Positive door locked/unlocked indication
- **Egress timing**: Emergency evacuation requirements (90 seconds)
- **Safety interlocks**: Prevention of pressurized opening

### Performance Critical
- **Seal leak rate**: Must meet pressurization schedule requirements
- **Ice/contamination margins**: Operation in adverse environmental conditions
- **Actuation forces**: Manual and powered operation within limits
- **Structural margins**: Door loads and stress concentration management

### Operational
- **Maintenance access**: Ease of inspection and service
- **Weight optimization**: Balance between strength and weight
- **Reliability**: MTBF and dispatch reliability targets
- **Commonality**: Standardization of mechanisms and interfaces where practical
