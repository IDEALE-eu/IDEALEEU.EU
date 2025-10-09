# Satellite Domain Integration

This directory contains the integration of satellite systems organized according to SPACE-T (STA) architecture and ECSS standards.

## Structure

```
DOMAIN_INTEGRATION/
└── PRODUCTS/
    └── <MISSION>/
        └── MODELS/
            └── <CONF>/
                └── VERSION/
                    └── <TAG>/
                        ├── README.md                    # Mission documentation
                        ├── META.json                    # Mission metadata
                        ├── domain-config.yaml           # Configuration rules
                        └── SYSTEMS/                     # All satellite systems
                            ├── 01-INTRO/
                            ├── 06-DIMENSIONS_ALIGNMENTS/
                            ├── 15-ENVIRONMENT_VIBRATION/
                            ├── 21-THERMAL_CONTROL/
                            ├── 23-COMMS_TT&C_RF_OPTICAL/
                            ├── 24-ELECTRICAL_POWER_EPS/
                            ├── 28-PROPELLANT_SYSTEMS/
                            ├── 29-PRESSURIZATION_PURGE/
                            ├── 31-DATA_HANDLING_CDH/
                            ├── 34-NAVIGATION_ATTITUDE/
                            ├── 40-DATABUS_NETWORKS/
                            ├── 42-AVIONICS_COMPUTE_FSW/
                            ├── 45-HEALTH_MONITORING_FDIR/
                            ├── 50-MECHANISMS_DEPLOYABLES/
                            ├── 51-PRIMARY_STRUCTURE/
                            ├── 57-INSTRUMENT_BAYS/
                            ├── 61-RCS_ATTITUDE_CONTROL/
                            ├── 70-OPTICAL_SUBSYSTEMS/
                            ├── 71-PAYLOADS/
                            ├── 72-PROPULSION_MAIN/
                            ├── 84-ELECTRIC_PROPULSION/
                            ├── 87-RADIATION/
                            ├── 90-SPACE_TRAFFIC_CONJUNCTION/
                            ├── 97-ELECTRICAL_HARNESS/    # STA-97 for satellites
                            └── 99-MISSION_OPERATIONS/
```

## Quick Start

### Creating Satellite Domain Structure

To generate a complete satellite domain integration structure for a new mission:

```bash
./scripts/create-satellite-domains.sh <MISSION> <CONF> <TAG>
```

**Examples:**
```bash
# Default example satellite
./scripts/create-satellite-domains.sh

# Custom mission
./scripts/create-satellite-domains.sh EARTH-OBS-1 ADVANCED V2.0

# Multiple configurations
./scripts/create-satellite-domains.sh COMSAT-X BASELINE V1.0
./scripts/create-satellite-domains.sh COMSAT-X REDUNDANT V1.0
```

This creates:
- Complete SYSTEMS/ structure with all major satellite subsystems
- **INTEGRATION_VIEW.md** for each system describing functional integration
- **INTERFACE_MATRIX/** with CSV files documenting system interconnections
- **SUBSYSTEMS/** with complete PLM/CAx structure
- Representative subsystems demonstrating the pattern

## System Organization

Each system follows the standard structure:

```
SYSTEMS/<STA-XX_NAME>/
├── INTEGRATION_VIEW.md           # System integration description
├── INTERFACE_MATRIX/              # Interface definitions
│   └── XX↔OTHERS.csv             # CSV format interface matrix
└── SUBSYSTEMS/                    # System subsystems
    └── XX-YY_SUBSYSTEM/
        ├── README.md
        ├── DELs/                  # Deliverables
        ├── PAx/                   # Package assemblies
        │   ├── ONB/              # Onboard
        │   └── OUT/              # Outputs
        ├── PLM/                   # Product Lifecycle Management
        │   ├── CAx/              # Engineering tools
        │   │   ├── CAD/          # Computer-Aided Design
        │   │   ├── CAE/          # Computer-Aided Engineering
        │   │   ├── CAO/          # Computer-Aided Optimization
        │   │   ├── CAM/          # Computer-Aided Manufacturing
        │   │   ├── CAI/          # Computer-Aided Inspection
        │   │   ├── CAV/          # Computer-Aided Validation
        │   │   ├── CAP/          # Computer-Aided Planning
        │   │   ├── CAS/          # Computer-Aided Simulation
        │   │   └── CMP/          # Computer-Aided Management/Planning
        │   └── EBOM/             # Engineering BOM
        ├── PROCUREMENT/           # Vendor management
        ├── SUPPLIERS/             # Supplier data
        ├── policy/                # Policies
        ├── tests/                 # Test data
        └── META.json              # Metadata
```

## Key Conventions

1. **STA Numbering** - Systems numbered according to SPACE-T architecture (STA)
2. **PLM/CAx only in SUBSYSTEMS** - Engineering artifacts at subsystem level only
3. **Harness in STA-97** - All electrical harness in dedicated chapter (not ATA-92)
4. **Integration focus** - Each system has INTEGRATION_VIEW.md and INTERFACE_MATRIX/
5. **ECSS compliance** - Following ECSS standards for space systems

## Major Satellite Systems

### Core Systems (Always Present)
- **21-THERMAL_CONTROL** - Thermal management (radiators, MLI, heaters)
- **23-COMMS_TT&C_RF_OPTICAL** - Communications and telemetry
- **24-ELECTRICAL_POWER_EPS** - Power generation, storage, distribution
- **31-DATA_HANDLING_CDH** - Command and data handling
- **34-NAVIGATION_ATTITUDE** - GNC sensors and systems
- **40-DATABUS_NETWORKS** - Internal data networks (SpaceWire, 1553, CAN)
- **42-AVIONICS_COMPUTE_FSW** - Flight computers and software
- **45-HEALTH_MONITORING_FDIR** - Health monitoring and FDIR
- **50-MECHANISMS_DEPLOYABLES** - Deployment mechanisms
- **51-PRIMARY_STRUCTURE** - Primary spacecraft structure
- **97-ELECTRICAL_HARNESS** - All physical harness (STA-97)

### Mission-Specific Systems (Optional)
- **57-INSTRUMENT_BAYS** - Payload accommodation
- **61-RCS_ATTITUDE_CONTROL** - Reaction control system
- **70-OPTICAL_SUBSYSTEMS** - Optical payloads (imaging missions)
- **71-PAYLOADS** - Science and mission payloads
- **72-PROPULSION_MAIN** - Main propulsion (deep space missions)
- **84-ELECTRIC_PROPULSION** - Electric propulsion (EP missions)

### Support Systems
- **01-INTRO** - Mission overview and CONOPS
- **06-DIMENSIONS_ALIGNMENTS** - Reference frames and alignments
- **15-ENVIRONMENT_VIBRATION** - Environmental specifications
- **28-PROPELLANT_SYSTEMS** - Propellant storage (if applicable)
- **29-PRESSURIZATION_PURGE** - Pressurization systems (if applicable)
- **87-RADIATION** - Radiation analysis
- **90-SPACE_TRAFFIC_CONJUNCTION** - Collision avoidance
- **99-MISSION_OPERATIONS** - Operations concept

## Interface Matrices

Interface matrices document system interconnections in CSV format:

```csv
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
24,31,power,electrical,28V_bus,80,,OBC power supply
31,23,data,digital,CCSDS,0,10Mbps,Telemetry downlink
```

**Key Fields:**
- `from_sta` / `to_sta` - System numbers (e.g., 24, 31)
- `interface_type` - Type of interface (power, data, thermal, mechanical)
- `signal_medium` - Physical medium (electrical, digital, conductive, RF)
- `protocol_spec` - Protocol or standard (e.g., 28V_bus, CCSDS, CAN)
- `power_W` - Power transfer in watts (if applicable)
- `data_rate` - Data rate (if applicable)
- `notes` - Additional information

## Integration with Configuration Management

All satellite domain structures integrate with:
- `00-PROGRAM/CONFIG_MGMT/` - Change control and baselines
- `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/` - Interface control documents
- `00-PROGRAM/DIGITAL_THREAD/04-MBSE/` - MBSE models and requirements
- `04-SATELLITES/CONFIGURATION_BASE/` - STA system configurations

## ECSS Standards Compliance

This structure supports ECSS standards:
- **ECSS-E** - Engineering standards
- **ECSS-M** - Management standards  
- **ECSS-Q** - Quality assurance standards
- **ECSS-S** - System standards

## Scripts

Located in `/scripts/`:
- `create-satellite-domains.sh` - Creates satellite domain structure for a mission

The script is idempotent and safe to run multiple times.

## Examples

See the example satellite in:
```
PRODUCTS/EXAMPLE-SAT-1/MODELS/BASELINE/VERSION/V1.0/
```

This example demonstrates:
- Complete system structure
- Interface matrices with realistic data
- Subsystem organization with PLM/CAx
- Integration views
- Proper use of STA-97 for electrical harness

## Migration from Legacy Structures

If migrating from older structures:
1. Map legacy system numbers to STA numbers
2. Consolidate all harness into STA-97 (not ATA-92)
3. Ensure PLM/CAx is only in SUBSYSTEMS
4. Create INTEGRATION_VIEW.md for each system
5. Generate INTERFACE_MATRIX CSV files
6. Update metadata files (META.json, domain-config.yaml)

## Related Documentation

- [04-SATELLITES/00-README.md](../00-README.md) - Satellite overview
- [00-PROGRAM/CONFIG_MGMT/](../../00-PROGRAM/CONFIG_MGMT/) - Configuration management
- [00-PROGRAM/DIGITAL_THREAD/04-MBSE/](../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/) - MBSE integration
- ECSS Standards: https://ecss.nl/

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-10 | IDEALE | Initial STA-aligned satellite structure |
