# GENERATION_PROPULSION_ENERGY Domain Integration

## Scope

This domain covers the integration of all aircraft power generation, propulsion, and energy systems, including:

- **ATA-24**: Electrical Power Generation, Storage, and Distribution
- **ATA-49**: Auxiliary Power Unit (APU)
- **ATA-71**: Powerplant General
- **ATA-72**: Engine Core and Propulsor
- **ATA-73**: Engine Fuel Control (FADEC)
- **ATA-74**: Ignition Systems
- **ATA-75**: Bleed Air
- **ATA-76**: Engine Controls
- **ATA-77**: Engine Indicating
- **ATA-78**: Exhaust and Thrust Reversers
- **ATA-79**: Oil Systems
- **ATA-80**: Starting Systems

## RASCI Matrix

| Activity | Responsible | Accountable | Supportive | Consulted | Informed |
|----------|-------------|-------------|------------|-----------|----------|
| System Design | Propulsion Engineering | Chief Engineer | PLM Team | Safety, Cert | Program Mgmt |
| Interface Definition | Systems Integration | Chief Engineer | Suppliers | ATA Owners | Config Mgmt |
| PLM Artifact Management | PLM Team | Config Mgmt | Engineering | - | All Stakeholders |
| Verification Planning | V&V Lead | Chief Engineer | Test Team | Cert Authority | Program Mgmt |
| Compliance Evidence | Compliance Lead | Chief Engineer | Engineering | Cert Authority | Program Mgmt |

## Rules and Guidelines

### Software and LRU Integration

**Rule 1**: Software-bearing LRUs (Line Replaceable Units) are documented with their software configurations in this domain structure.
- FADEC controllers (ATA-73)
- Energy Management Systems (ATA-24)
- Engine control units (ATA-76)
- APU controllers (ATA-49)

**Rule 2**: Each LRU with embedded software shall have:
- Hardware configuration in `PLM/EBOM_LINKS.md`
- Software baseline reference
- Interface specifications

### EWIS (Electrical Wiring Interconnection System)

**Rule 3**: Physical wiring is documented ONLY in **ATA-92_EWIS** per EWIS rules.

**Rule 4**: This domain documents:
- Logical interfaces between systems
- Power requirements and distribution architecture
- Signal interfaces and protocols
- Interface Control Documents (ICDs)

**Rule 5**: Cross-references to ATA-92 are made via Interface Matrices.

### PLM Integration

**Rule 6**: Each subsystem includes a `PLM/` directory containing:
- `EBOM_LINKS.md` - Links to Engineering Bill of Materials in PLM system
- `CAx/` subdirectories for Computer-Aided Engineering artifacts:
  - `CAD/` - Computer-Aided Design models
  - `CAE/` - Computer-Aided Engineering analysis
  - `CAO/` - Computer-Aided Optimization
  - `CAM/` - Computer-Aided Manufacturing
  - `CAI/` - Computer-Aided Inspection
  - `CAV/` - Computer-Aided Verification
  - `CAP/` - Computer-Aided Planning
  - `CAS/` - Computer-Aided Simulation
  - `CMP/` - Computer-Aided Manufacturing Process

**Rule 7**: EBOM_LINKS.md shall contain:
- Part numbers and descriptions
- PLM system references
- Supplier information
- Configuration status

### ARINC 653 Partitions

**Rule 8**: If Energy Management Systems (ATA-24-50) host ARINC 653 partitions, partition mappings are documented in the subsystem's PLM directory with cross-references to ATA-42 (IMA configuration).

### Integration Views

**Rule 9**: System-level integration views are maintained in `03-INTEGRATION_VIEWS/` to show:
- Energy flow diagrams (AC/DC buses, priorities)
- Propulsion chain integration (fuel/air/ignition → thrust)
- Thermal-power coupling interfaces

### Interface Management

**Rule 10**: All inter-system interfaces are documented in:
- System-level Interface Matrices (in each ATA system directory)
- Domain-level Interface Matrix (`02-INTERFACES/INTERFACE_MATRIX.csv`)
- ICDs linked via `02-INTERFACES/ICD_LINKS.md`

## Directory Structure

```
GENERATION_PROPULSION_ENERGY/
├─ 00-README.md                    # This file
├─ 01-SYSTEMS/                     # Individual ATA systems
├─ 02-INTERFACES/                  # Domain-level interfaces
├─ 03-INTEGRATION_VIEWS/           # System integration views
├─ 04-DIGITAL_THREAD/              # MBSE and Digital Twin links
├─ 05-VERIFICATION/                # Verification and validation
├─ 06-COMPLIANCE/                  # Standards and certification
├─ 07-CHANGE_LOG/                  # Domain change history
└─ 08-TEMPLATES/                   # Standard templates
```

## Related Documentation

- [Configuration Base](../../CONFIGURATION_BASE/) - Baseline configuration for all ATA chapters
- [Cross-System Integration](../../CROSS_SYSTEM_INTEGRATION/) - Aircraft-level integration
- [Digital Twin Model](../../DIGITAL_TWIN_MODEL/) - Digital twin implementation
- [Program Config Management](../../../00-PROGRAM/CONFIG_MGMT/) - Program-level configuration

## Contacts

- **Domain Lead**: Propulsion & Energy Systems Engineering
- **Integration Lead**: Systems Integration Engineering
- **Configuration Management**: Configuration Control Board (CCB)

---

**Last Updated**: 2024-01-15
