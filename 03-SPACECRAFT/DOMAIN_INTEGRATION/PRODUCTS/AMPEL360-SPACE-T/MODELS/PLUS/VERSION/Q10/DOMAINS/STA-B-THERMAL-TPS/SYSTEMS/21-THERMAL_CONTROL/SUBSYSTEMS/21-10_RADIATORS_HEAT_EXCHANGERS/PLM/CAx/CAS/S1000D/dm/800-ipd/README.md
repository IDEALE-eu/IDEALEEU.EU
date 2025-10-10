# 800-IPD — Illustrated Parts Data

## Purpose

This directory contains **Illustrated Parts Data (IPD)** Data Modules for the 21-10 Radiators & Heat Exchangers subsystem, providing parts lists, part numbers, exploded view illustrations, and procurement information.

## Contents

Data Modules with Info Code **800-8xx**:
- Parts lists with illustrations
- Exploded view diagrams
- Part numbers and nomenclature
- Interchangeability information
- Vendor/manufacturer data
- National Stock Numbers (NSN)
- Commercial and Government Entity (CAGE) codes

## Data Module Types

- **800**: IPD introduction
- **801**: Assembly illustrated parts list
- **802**: Subassembly illustrated parts list
- **803**: Provisioning parts list
- **804**: Modification parts list

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-01-00-00A-801A-A_en-US_001-00.xml
```

Where:
- `801A`: Info Code (Assembly IPD)
- Assembly/subassembly specific code

## IPD Structure

### Assembly Breakdown

**Radiator Panel Assembly**
- Radiator panel structure
- Heat pipe network
- Mounting brackets
- Thermal coating
- Fasteners and hardware

**LPHX Assembly**
- Heat exchanger core
- Inlet/outlet manifolds
- Mounting plates
- Seals and gaskets
- Fluid connectors

**Coldplate Assembly**
- Coldplate structure
- Fluid channels
- Mounting interface
- TIM/bondline materials
- Interface hardware

### Part Information

For each part:
- **Part number**: Manufacturer part number
- **Nomenclature**: Official part name
- **NSN**: National Stock Number (if applicable)
- **CAGE code**: Manufacturer identifier
- **Quantity**: Per assembly
- **Reference**: Callout on illustration
- **Interchangeability**: Alternative part numbers
- **Remarks**: Special notes, usage restrictions

## Usage Guidelines

**DO**:
- Link illustrations (ICN) to parts list
- Provide complete part identification
- Include sourcing information
- Document interchangeability
- Update for configuration changes
- Cross-reference to procedures

**DO NOT**:
- Include procedural information
- Duplicate supplier catalogs
- Use obsolete part numbers
- Omit critical identification data

## Illustration Requirements

- **Exploded views**: Show assembly relationships
- **Callouts**: Match parts list item numbers
- **Detail views**: For complex areas
- **Section views**: For internal components
- **Vector format**: SVG or CGM preferred

## Part Numbering

Follow AMPEL360 part numbering convention:
```
21-10-XXXX-YY-ZZ
```

Where:
- `21-10`: System/subsystem code
- `XXXX`: Component identifier
- `YY`: Variant code
- `ZZ`: Dash number for configuration

## Configuration Management

Track:
- **Effectivity**: Which vehicles/configurations
- **Substitutions**: Interchangeable parts
- **Modifications**: Engineering changes
- **Obsolescence**: Superseded parts
- **Lead time**: Procurement information

## Review Requirements

Before publishing:
- [ ] All parts identified correctly
- [ ] Illustrations match parts lists
- [ ] Part numbers verified with EBOM
- [ ] Supplier information current
- [ ] Interchangeability validated
- [ ] BREX validation passed

## Related Directories

- **[../500-removal-installation/](../500-removal-installation/)** — R&I procedures reference IPD
- **[../../icn/](../../icn/)** — Exploded view illustrations
- **[../../pm/IPC/](../../pm/IPC/)** — Illustrated Parts Catalog

---

**Last Updated**: 2025-10-11
