# TORQUE_SPECS — Torque Specifications and Installation Requirements

## Purpose

This directory contains torque specifications, installation procedures, and quality requirements for all fasteners at interfaces.

## Content Types

### Torque Specifications
- Fastener torque values
- Torque ranges (min-max)
- Dry vs. lubricated torque
- Special torque requirements
- Re-torque requirements

### Installation Procedures
- Tightening sequences
- Torque patterns
- Tool specifications
- Verification methods
- Quality checkpoints

### Documentation
- Torque tables by fastener type
- Installation work instructions
- Inspection criteria
- Non-conformance procedures

## File Formats

- `.pdf` — Torque specification documents
- `.csv` — Torque tables
- `.xlsx` — Detailed torque matrices
- `.dwg` — Torque sequence diagrams

## Torque Specification Data

### Basic Torque Information
```csv
fastener_id,part_number,size,material,thread,torque_min,torque_max,units,lubrication,notes
FTN-001,NAS1303-6,1/4-28,A286,UNF,60,70,in-lb,Dry,Wing attach primary
FTN-002,NAS1352N6-8,3/8-24,A286,UNF,120,140,in-lb,Dry,Bulkhead critical
```

### Torque Parameters
- Fastener size and thread
- Material and coating
- Lubrication condition
- Torque value and tolerance
- Tightening method
- Verification requirement

## Torque Categories

### Critical Fasteners
- Primary structure
- Safety-critical joints
- Pressure vessel attachments
- Engine mounts
- Flight control attachments

### Standard Fasteners
- Secondary structure
- Non-critical attachments
- Access panels
- Equipment mounting

### Special Fasteners
- Locking fasteners
- Interference fit bolts
- Pre-tensioned bolts
- Torque-to-yield fasteners

## Torque Methods

### Manual Torque Wrench
- Calibrated torque wrench required
- Operator certification
- Three attempts maximum
- Verification required

### Automatic Torque Tools
- Computer-controlled tools
- Angle and torque monitoring
- Automatic documentation
- Statistical process control

### Torque-Angle Method
- Initial torque to specified value
- Additional rotation by angle
- Used for yielding fasteners
- Plastic region tightening

## Tightening Sequences

### Uniform Distribution
- Star pattern for circular patterns
- Cross pattern for rectangular patterns
- Inside-out or outside-in progression
- Multiple passes with increasing torque

### Critical Joint Sequences
1. First pass: 30% of final torque
2. Second pass: 60% of final torque
3. Final pass: 100% of final torque
4. Verification pass

## Naming Convention

```
TRQ_{interface}_{fastener_type}_v{version}.{ext}
```

Examples:
- `TRQ_WING-ATTACH_BOLTS_v001.csv`
- `TRQ_BULKHEAD_INSTALLATION-SEQ_v002.pdf`
- `TRQ_DOOR-FRAME_RIVETS_v001.xlsx`

## Factors Affecting Torque

### Lubrication
- **Dry torque**: No lubricant applied
- **Lubricated**: Specified lubricant used
- Torque reduction: 20-30% typical for lubrication

### Thread Condition
- New threads
- Re-used fasteners
- Thread damage
- Thread wear

### Environmental Conditions
- Temperature effects
- Humidity effects
- Contamination

### Material Considerations
- Aluminum vs. steel
- Composite interfaces
- Coating effects
- Corrosion protection

## Torque Verification

### Measurement Methods
- Break-away torque check
- Angle monitoring
- Ultrasonic measurement
- Strain gauge measurement

### Acceptance Criteria
- Within specified torque range
- No visual damage
- Proper seating
- Correct angle (if applicable)

### Documentation
- Torque value recorded
- Operator identification
- Tool calibration status
- Date and time

## Quality Control

### Pre-Installation
- Tool calibration verification
- Fastener inspection
- Surface preparation check
- Thread lubrication verification

### During Installation
- Torque monitoring
- Sequence verification
- Visual inspection
- Anomaly reporting

### Post-Installation
- Final torque verification
- Lock wire installation (if required)
- Safety wire verification
- Final inspection

## Special Considerations

### Composite Structures
- Lower torque to prevent crushing
- Use of torque-limiter tools
- Bearing plates or washers
- Monitoring for creep

### Aluminum Structures
- Torque sequence important
- Avoid over-torque (stripping)
- Thread protection
- Corrosion prevention

### Critical Joints
- 100% verification
- Multiple inspectors
- Photo documentation
- Traceability records

## Re-Torque Requirements

### Initial Assembly
- Allow settling period
- Re-torque after first flight (if specified)
- Document re-torque values

### Maintenance
- Periodic re-torque intervals
- After vibration exposure
- Following disassembly
- Per maintenance manual

## Cross-References

- [Fasteners](../FASTENERS/)
- [Hole Patterns](../HOLE_PATTERNS/)
- [Sealants and Gaskets](../SEALANTS_GASKETS/)
- [Interface Control Documents](../ICD/)

## Standards

- **ASME B18.2.1**: Square and hex bolts and screws
- **NASM 33540**: Hole preparation for aerospace fasteners
- **MIL-STD-1312**: Fastener test methods
- **SAE J429**: Mechanical and material requirements for fasteners
- **ISO 898**: Mechanical properties of fasteners
