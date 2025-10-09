# PRODUCTS - Mission-Specific Spacecraft Systems

## Overview

This directory organizes spacecraft systems by mission, model configuration, and version using a hierarchical product structure.

## Directory Hierarchy

```
PRODUCTS/
└── <MISSION>/              # Mission name (e.g., EXAMPLE_MISSION, MARS_ORBITER, LUNAR_LANDER)
    └── MODELS/
        └── <CONFIGURATION>/   # Configuration variant (e.g., CONFIG_A, CONFIG_B, FLIGHT_MODEL)
            └── VERSION/
                └── <TAG>/     # Version tag (e.g., V1.0, V2.1, PDR_BASELINE)
                    └── SYSTEMS/
                        └── ATA-XX_NAME/    # ATA-numbered systems
```

## Mission Organization

Each mission has its own product directory containing:
- Multiple model configurations (if applicable)
- Version-controlled system baselines
- Complete SYSTEMS hierarchy per version

### Example Missions
- **EXAMPLE_MISSION** - Template/example structure
- **MARS_ORBITER** - Mars orbital mission
- **LUNAR_LANDER** - Lunar surface mission
- **LEO_SATELLITE** - Low Earth Orbit satellite
- **DEEP_SPACE_PROBE** - Interplanetary probe

## Model Configurations

Model configurations represent different variants of the spacecraft:
- **CONFIG_A** - Baseline configuration
- **CONFIG_B** - Alternative payload configuration
- **FLIGHT_MODEL** - Flight-ready configuration
- **ENGINEERING_MODEL** - Ground test configuration
- **QUALIFICATION_MODEL** - Environmental qualification unit

## Version Control

Versions correspond to program milestones and releases:
- **V0.1** - Initial concept
- **V1.0** - PDR (Preliminary Design Review) baseline
- **V2.0** - CDR (Critical Design Review) baseline
- **V3.0** - QR (Qualification Review) baseline
- **V4.0** - AR (Acceptance Review) baseline
- **RELEASE_CANDIDATE** - Pre-flight baseline

## SYSTEMS Structure

Each version contains a complete SYSTEMS directory with all ATA-numbered systems. See [README.md](../README.md) for detailed system organization.

### Key System Categories
- **A:** Structures & Mechanisms
- **B:** Thermal & TPS
- **C:** Power / EPS
- **D:** Communications
- **E:** Navigation & Data
- **F:** Avionics & SW
- **G:** Control & Health
- **H:** ECLSS & Crew
- **I:** Propulsion
- **J:** Docking & Robotics
- **K:** Safety & Environment
- **L:** Ground & Ops
- **M:** Program & Records

## Configuration Management

### Baseline Creation
1. Create new VERSION directory for milestone
2. Copy or branch SYSTEMS from previous version
3. Update configuration items per ECR/ECO
4. Conduct configuration audit
5. Obtain CCB approval
6. Tag version in configuration management system

### Change Control
- All changes tracked through ECR (Engineering Change Request)
- Approved changes implemented via ECO (Engineering Change Order)
- Version increments follow semver pattern: MAJOR.MINOR.PATCH
- Baseline changes require CCB approval

### Traceability
Each version maintains traceability to:
- **Requirements:** Links to `00-PROGRAM/REQUIREMENTS/`
- **Interfaces:** References to `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Changes:** ECR/ECO references in change logs
- **Tests:** Links to `03-SPACECRAFT/AIT/` test procedures

## Usage Examples

### Creating a New Mission
```bash
# Create mission product structure
mkdir -p PRODUCTS/NEW_MISSION/MODELS/CONFIG_A/VERSION/V1.0/SYSTEMS

# Copy template systems structure
cp -r PRODUCTS/EXAMPLE_MISSION/MODELS/CONFIG_A/VERSION/V1.0/SYSTEMS/* \
      PRODUCTS/NEW_MISSION/MODELS/CONFIG_A/VERSION/V1.0/SYSTEMS/

# Customize systems for mission
# Update INTEGRATION_VIEW.md files with mission-specific data
# Update INTERFACE_MATRIX CSV files with actual interfaces
```

### Creating a Version Baseline
```bash
# Branch from previous version
cp -r PRODUCTS/MISSION/MODELS/CONFIG_A/VERSION/V1.0 \
      PRODUCTS/MISSION/MODELS/CONFIG_A/VERSION/V2.0

# Update configuration items
# Review and update changed systems
# Tag in configuration management
```

### Creating a Configuration Variant
```bash
# Copy from baseline configuration
cp -r PRODUCTS/MISSION/MODELS/CONFIG_A \
      PRODUCTS/MISSION/MODELS/CONFIG_B

# Modify systems for variant
# Update INTEGRATION_VIEW.md for configuration differences
# Update INTERFACE_MATRIX for variant-specific interfaces
```

## Documentation Standards

Each mission/model/version should maintain:
- [ ] Complete SYSTEMS hierarchy
- [ ] INTEGRATION_VIEW.md for each system
- [ ] INTERFACE_MATRIX CSV for each system
- [ ] PLM/EBOM_LINKS for subsystems
- [ ] Release notes documenting changes from previous version

## Integration with Program Documents

### Requirements Traceability
- System requirements in `00-PROGRAM/REQUIREMENTS/`
- Allocation matrix links requirements to systems
- Verification tracked in INTEGRATION_VIEW.md

### Interface Control
- Formal ICDs in `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- Interface matrices provide local summaries
- ICD references in interface matrix CSVs

### PLM Integration
- Part numbers follow `00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md`
- PLM links in `SUBSYSTEMS/*/PLM/EBOM_LINKS.md`
- CAx artifacts in `SUBSYSTEMS/*/PLM/CAx/`

## Quality Assurance

### Configuration Audits
Before each major milestone:
- [ ] Verify all systems present
- [ ] Check INTEGRATION_VIEW.md completeness
- [ ] Validate INTERFACE_MATRIX CSVs
- [ ] Confirm PLM links and part numbers
- [ ] Review change log completeness

### Validation Scripts
CI/CD scripts validate:
- Directory structure compliance
- Required files present
- CSV syntax and completeness
- Markdown formatting
- Cross-reference integrity

See: `scripts/validate-structure.sh`

## Migration Notes

### From Legacy Structure
To migrate from existing spacecraft organization:
1. Map existing systems to ATA chapters
2. Create mission-specific product directory
3. Establish version baseline (e.g., V1.0)
4. Migrate systems to SYSTEMS/ATA-XX_NAME/ pattern
5. Create INTEGRATION_VIEW.md for each system
6. Generate INTERFACE_MATRIX CSVs
7. Organize PLM artifacts under SUBSYSTEMS/*/PLM/CAx/

### From Aircraft Domain
The structure mirrors `02-AIRCRAFT/DOMAIN_INTEGRATION/`:
- Same ATA chapter pattern
- Same SYSTEMS/SUBSYSTEMS/PLM hierarchy
- Same INTEGRATION_VIEW.md and INTERFACE_MATRIX approach
- Adapted for spacecraft-specific systems (propulsion, thermal, etc.)

## References

- [DOMAIN_INTEGRATION README](../README.md) - Main integration documentation
- [00-PROGRAM/CONFIG_MGMT/](../../00-PROGRAM/CONFIG_MGMT/) - Configuration management
- [03-SPACECRAFT/SYSTEMS_ENGINEERING/](../../SYSTEMS_ENGINEERING/) - Systems engineering processes
- [03-SPACECRAFT/AIT/](../../AIT/) - Assembly, integration, and test

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-09 | Configuration Management | Initial products organization |
