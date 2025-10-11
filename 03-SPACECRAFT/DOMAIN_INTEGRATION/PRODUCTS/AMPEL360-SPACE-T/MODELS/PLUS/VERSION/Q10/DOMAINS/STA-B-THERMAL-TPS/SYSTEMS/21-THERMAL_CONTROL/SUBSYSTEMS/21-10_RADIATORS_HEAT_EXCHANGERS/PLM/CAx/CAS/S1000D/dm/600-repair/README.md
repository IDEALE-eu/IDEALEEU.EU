# 600-REPAIR — Repair Procedures

## Purpose

This directory contains **repair** Data Modules (DMs) for the 21-10 Radiators & Heat Exchangers subsystem, including procedures for repairing damaged or malfunctioning components at the organizational and intermediate maintenance levels.

## Contents

Data Modules with Info Code **600-6xx**:
- Repair procedures
- Damage assessment
- Repair limits and criteria
- Rework procedures
- Bonding and sealing procedures
- Coating repair and reapplication
- Leak repair procedures
- Structural repair

## Data Module Types

- **600**: Repair introduction
- **601**: General repair procedures
- **602**: Structural repair
- **603**: Mechanical repair
- **604**: Surface treatment repair
- **609**: Repair limits

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-01-00-00A-601A-A_en-US_001-00.xml
```

Where:
- `601A`: Info Code (General repair)
- Repair type specific code

## Repair Categories

### Radiator Panel Repairs
- Surface coating repair
- Minor dent repair
- Bonded joint repair
- Thermal coating reapplication
- Optical coating restoration

### Heat Exchanger Repairs
- Leak sealing procedures
- Gasket replacement
- Surface preparation and re-coating
- Thread repair (helicoil installation)
- Fluid port repair

### TIM/Bondline Repairs
- Old TIM removal
- Surface preparation and cleaning
- New TIM application
- Bondline thickness verification

### Coating Repairs
- Paint and coating removal
- Surface preparation
- Primer application
- Thermal control coating application
- Optical properties verification

## Usage Guidelines

**DO**:
- Define damage limits clearly
- Specify repair vs. replace criteria
- Document material specifications
- Include curing/drying times
- Provide acceptance criteria
- Include safety precautions
- Reference technical standards

**DO NOT**:
- Exceed authorized repair limits
- Skip quality verification steps
- Use unauthorized materials
- Proceed without proper training
- Mix repair and overhaul procedures (700-series)

## Repair Assessment

1. **Damage inspection**
2. **Severity classification**
3. **Repairability determination**
4. **Repair method selection**
5. **Material and tool preparation**
6. **Repair execution**
7. **Quality verification**
8. **Documentation and certification**

## Quality Requirements

- **Visual inspection**: Surface finish, uniformity
- **Dimensional check**: Thickness, flatness
- **Leak test**: Pressure decay test
- **Thermal test**: Heat rejection verification
- **Optical properties**: Emissivity, absorptivity
- **Documentation**: Repair records and tags

## Review Requirements

Before publishing:
- [ ] Repair limits validated by engineering
- [ ] Materials specifications verified
- [ ] Safety warnings included
- [ ] Acceptance criteria defined
- [ ] Quality verification procedures complete
- [ ] BREX validation passed

## Related Directories

- **[../700-overhaul/](../700-overhaul/)** — Depot-level overhaul
- **[../500-removal-installation/](../500-removal-installation/)** — R&I procedures
- **[../900-tools-consumables/](../900-tools-consumables/)** — Repair materials

---

**Last Updated**: 2025-10-11
