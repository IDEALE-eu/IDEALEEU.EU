# 500-REMOVAL-INSTALLATION — Removal & Installation Procedures

## Purpose

This directory contains **removal and installation (R&I)** Data Modules (DMs) for the 21-10 Radiators & Heat Exchangers subsystem components, including step-by-step procedures for disassembly and assembly.

## Contents

Data Modules with Info Code **500-5xx**:
- Removal procedures
- Installation procedures
- Access procedures
- Closeup procedures
- Adjustment procedures
- Rigging procedures
- Fit and alignment checks

## Data Module Types

- **500**: R&I introduction
- **501**: Removal procedure
- **502**: Installation procedure
- **503**: Removal and installation procedure (combined)
- **504**: Access/closeup procedures
- **505**: Adjustment/rigging procedures

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-01-00-00A-503A-A_en-US_001-00.xml
```

Where:
- `00-01`: Component disassembly code
- `503A`: Info Code (R&I combined)
- Component specific identification

## Components Covered

### Radiator Assemblies
- Radiator panels
- Radiator support structure
- Mounting brackets and fasteners
- Interface connections

### Heat Exchangers
- Liquid plate heat exchangers (LPHX)
- Coldplates
- Heat pipes
- Fluid connections and fittings

### Associated Components
- Thermal interface materials (TIM)
- Mounting hardware
- Fluid lines and quick disconnects
- Thermal sensors

## Usage Guidelines

**DO**:
- Provide sequential step-by-step procedures
- Include torque specifications
- Document special tools required
- Specify consumables (TIM, sealants, gaskets)
- Include safety warnings and cautions
- Reference applicable drawings and ICNs
- Document cleanliness requirements

**DO NOT**:
- Include troubleshooting (use 200-series)
- Include repair procedures (use 600-series)
- Include scheduled maintenance (use 400-series)
- Skip critical steps or safety notices

## Procedure Structure

1. **Preparation**: Tools, parts, safety
2. **Access**: Opening panels, removing covers
3. **Disconnection**: Electrical, fluid, mechanical
4. **Removal**: Step-by-step disassembly
5. **Installation**: Reverse order with specifics
6. **Connection**: Reconnecting interfaces
7. **Closeup**: Reinstalling access panels
8. **Test**: Functional verification

## Special Considerations

- **Contamination control**: Clean room procedures
- **Torque values**: All critical fasteners
- **TIM application**: Thickness, coverage, curing
- **Leak testing**: Pressure test requirements
- **Alignment**: Critical fit tolerances

## Review Requirements

Before publishing:
- [ ] Procedures validated with hardware
- [ ] Torque specifications verified
- [ ] Special tools identified
- [ ] Safety notices included
- [ ] Illustrations accurate and complete
- [ ] BREX validation passed

## Related Directories

- **[../800-ipd/](../800-ipd/)** — Parts identification
- **[../900-tools-consumables/](../900-tools-consumables/)** — Tools and materials
- **[../../icn/](../../icn/)** — Exploded view illustrations

---

**Last Updated**: 2025-10-11
