# Wiring and Schematics Data Modules (DMC: W)

## Purpose

This directory contains **Wiring and Schematics Data Modules** for the AMPEL360 AIR-T 53-10 Center Body subsystem. These DMs provide electrical wiring diagrams, schematics, connector pinouts, and signal routing information.

## InfoCode Range

**900-999**: Wiring diagrams and electrical schematics
- **900A**: General wiring diagram
- **901A**: Power distribution diagram
- **902A**: Signal wiring diagram
- **903A**: Ground/bonding diagram
- **910A**: Connector pinout diagram
- **920A**: Electrical schematic
- **930A**: Cable assembly drawing
- **940A**: Harness routing diagram

## DMC Naming Pattern

```
DMC-AMP360-AAA-53-10-<XX>-00A-<InfoCode><Var>-W_en-US_<Issue>-<InWork>.xml
```

Where:
- `<XX>` = Disassembly code (00=general, 10-99=specific areas/systems)
- `<InfoCode>` = 900-999 for wiring/schematics
- `<Var>` = A-Z variant (usually A)
- `<Issue>` = 001, 002, 003...
- `<InWork>` = 00 (released) or 01-99 (draft)

## Examples

### General Center Body Wiring
```
DMC-AMP360-AAA-53-10-00-00A-900A-W_en-US_001-00.xml
```
- Complete wiring overview for Center Body
- InfoCode 900A: General wiring diagram

### Forward Bulkhead Wiring
```
DMC-AMP360-AAA-53-10-10-00A-900A-W_en-US_001-00.xml
```
- Wiring specific to forward bulkhead area
- Disassembly code 10: Forward bulkhead

### Center Body Power Distribution
```
DMC-AMP360-AAA-53-10-00-00A-901A-W_en-US_001-00.xml
```
- Power distribution within Center Body
- InfoCode 901A: Power distribution diagram

### Connector Pinouts
```
DMC-AMP360-AAA-53-10-00-00A-910A-W_en-US_001-00.xml
```
- Connector pinout diagrams for Center Body
- InfoCode 910A: Connector pinout diagram

## Content Types

### Wiring Diagrams
- Overall wiring layout
- Wire routing and paths
- Connector locations
- Junction boxes and splices
- Wire identification
- Color codes
- Gauge/size information

### Electrical Schematics
- Circuit diagrams
- Component symbols
- Signal flow
- Voltage levels
- Current ratings
- Protective devices (fuses, circuit breakers)

### Connector Pinouts
- Pin assignments
- Signal names
- Wire colors
- Connector type/part number
- Mating connector information
- Shielding and grounding

### Cable Assemblies
- Cable construction
- Connector types
- Wire specifications
- Length and routing
- Testing requirements

## Wiring Standards

### Wire Identification (ARINC 622)
```
<SystemCode>-<WireNumber>-<Segment>-<Gauge>
```

Example: `53-1234-A-20`
- System: 53 (Fuselage)
- Wire: 1234
- Segment: A
- Gauge: 20 AWG

### Wire Color Codes
Follow standard aviation color codes:
- **BK**: Black (ground/common)
- **RD**: Red (power/hot)
- **BL**: Blue (signal)
- **YL**: Yellow (caution/warning)
- **GN**: Green (normal/safe)
- **WT**: White (return/neutral)
- **OR**: Orange (data/communication)
- **BR**: Brown (supplementary)

### Wire Gauge Standards
- **20 AWG**: Signal wires (2-3A)
- **18 AWG**: Light power (5-7A)
- **16 AWG**: Medium power (10-13A)
- **14 AWG**: Heavy power (17-23A)
- **12 AWG**: Very heavy power (25-35A)

## Illustration Types

### Wiring Diagram Symbols (ICN)
```
ICN-53-10-WIRE-<SeqNum>-A.svg
```

### Schematic Symbols (ICN)
```
ICN-53-10-SCHM-<SeqNum>-A.svg
```

### Standard Symbols
- Connectors (various pin counts)
- Splices and junctions
- Grounds and bonds
- Circuit breakers and fuses
- Relays and switches
- Diodes and resistors
- Power sources

## Integration with ATA-92 EWIS

### Cross-References
Wiring DMs should reference:
- **ATA-92 EWIS** baseline data
- Harness assemblies
- Wire specifications
- Zone definitions
- Routing paths
- Grounding requirements

### EWIS Compliance
- Proper separation from hydraulic/fuel lines
- Adequate support (clamps, ties)
- Proper bend radius
- Chafe protection
- Environmental protection
- Maintenance access

## Connector Information

### Connector Pinout Tables

| Pin | Signal Name | Wire Color | Wire Gauge | From/To | Notes |
|-----|-------------|------------|------------|---------|-------|
| A1  | 28V DC PWR  | RD         | 18 AWG     | CB-12   | Main power |
| A2  | GND         | BK         | 18 AWG     | Ground  | Chassis ground |
| B1  | DATA+       | OR/WT      | 22 AWG     | LRU-A   | CAN bus high |
| B2  | DATA-       | OR/BK      | 22 AWG     | LRU-A   | CAN bus low |

### Connector Standards
- **MIL-DTL-38999**: Environmental circular connectors
- **MIL-DTL-26482**: General purpose connectors
- **ARINC 600/700**: Avionics rack connectors
- **D-sub**: Data and signal connectors

## Signal Types

### Power
- Primary DC power (28V DC)
- AC power (115V/400Hz)
- Ground returns
- Circuit protection

### Data/Communication
- ARINC 429 (aviation data bus)
- MIL-STD-1553 (military data bus)
- CAN bus (Controller Area Network)
- Ethernet (avionics)
- Discrete signals

### Sensor/Analog
- Temperature sensors (RTD, thermocouple)
- Pressure sensors (4-20mA)
- Position sensors (LVDT)
- Analog signals (0-5V, 0-10V)

## Testing Requirements

### Continuity Testing
- Point-to-point continuity
- Resistance measurements
- Proper terminations

### Insulation Resistance
- Megohm testing (IR test)
- Minimum 10 MΩ at 500V DC

### High-Potential Testing
- Hi-pot test per specification
- Verify dielectric strength

### Functional Testing
- Signal integrity
- Power distribution
- Communication protocols
- End-to-end verification

## Quality Checklist

- [ ] DMC follows naming convention
- [ ] Metadata complete and correct
- [ ] UTCS anchors included
- [ ] Wire identification follows ARINC 622
- [ ] Color codes consistent and accurate
- [ ] Gauge/current ratings verified
- [ ] Connector pinouts accurate
- [ ] Schematic symbols standard
- [ ] Illustrations clear and legible
- [ ] Cross-references to ATA-92 validated
- [ ] EWIS compliance verified
- [ ] Testing requirements specified
- [ ] Technical accuracy verified
- [ ] BREX validation passed
- [ ] Electrical engineering review
- [ ] QA approval obtained

## Safety Considerations

### Warnings
- **High voltage hazards**
- **Arc flash protection**
- **Proper grounding required**
- **Lockout/tagout procedures**

### Cautions
- **ESD sensitive components**
- **Proper wire dress and routing**
- **Connector damage prevention**
- **Wire chafing hazards**

## Maintenance Support

Wiring DMs support:
- **Troubleshooting** - Signal tracing
- **Repair** - Wire replacement procedures
- **Modification** - Circuit changes
- **Inspection** - Visual and electrical checks
- **Testing** - Functional verification

## Validation

```bash
# Validate single wiring DM
python ../../../VALIDATION/BREX/validate_brex.py DMC-*-W_*.xml

# Validate all wiring DMs
python ../../../VALIDATION/BREX/validate_brex.py .
```

## Related Resources

- **ATA-92 EWIS**: `/02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/`
- **Wire Specifications**: `ATA-92/PARAMS/WIRE_GAUGE_SPECS.csv`
- **Harness Assemblies**: `ATA-92/BASELINE/HARNESS_ASSEMBLIES.xml`
- **Zone Definitions**: `ATA-92/PARAMS/ZONE_DEFINITIONS.csv`
- **Grounding Specs**: `ATA-92/PARAMS/GROUNDING_SPECS.csv`
- **Style Guide**: `../../../GUIDES/StyleGuide.md`
- **Conventions**: `../../../GUIDES/Conventions.md`
- **BREX Rules**: `../../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`

## Updates and Revisions

Update wiring DMs when:
- New circuits added
- Wiring modifications
- Connector changes
- Harness rerouting
- System upgrades
- Engineering changes

## Certification Compliance

Wiring documentation must support:
- **Part 25** certification (aircraft)
- **EWIS requirements** (ATA-92)
- **EMI/EMC compliance**
- **Lightning protection**
- **Fire safety standards**
