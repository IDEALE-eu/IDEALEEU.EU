# 700-OVERHAUL — Overhaul Procedures

## Purpose

This directory contains **overhaul** Data Modules (DMs) for the 21-10 Radiators & Heat Exchangers subsystem, including depot-level maintenance, complete disassembly, inspection, refurbishment, and reassembly procedures.

## Contents

Data Modules with Info Code **700-7xx**:
- Complete overhaul procedures
- Major disassembly procedures
- Component refurbishment
- Performance restoration
- Life extension procedures
- Certification and testing
- Overhaul limits and criteria

## Data Module Types

- **700**: Overhaul introduction
- **701**: Disassembly for overhaul
- **702**: Cleaning and inspection
- **703**: Repair and refurbishment
- **704**: Reassembly after overhaul
- **705**: Testing and certification

## File Naming Convention

Follow S1000D DMC format:
```
DMC-AMPEL360-2110-00-00-00-00A-700A-A_en-US_001-00.xml
```

Where:
- `700A`: Info Code (Overhaul)
- Overhaul phase specific code

## Overhaul Scope

### Complete Radiator Overhaul
- Full disassembly to component level
- Thermal coating removal and reapplication
- Structural integrity assessment
- Fluid path cleaning and flushing
- Mounting interface refurbishment
- Performance testing and certification

### Heat Exchanger Overhaul
- Complete disassembly of LPHX
- Internal passage cleaning
- Seal replacement
- Surface refinishing
- Leak testing
- Thermal performance validation

### System-Level Overhaul
- Complete subsystem removal
- Individual component overhaul
- Interface refurbishment
- System integration
- End-to-end performance testing

## Usage Guidelines

**DO**:
- Follow complete overhaul sequence
- Document all findings and discrepancies
- Replace all life-limited parts
- Perform all required inspections
- Meet original performance specifications
- Obtain depot certification
- Update configuration records

**DO NOT**:
- Skip inspection steps
- Reuse consumable items
- Exceed overhaul time limits
- Bypass quality gates
- Use organizational-level repair for depot work

## Overhaul Process

1. **Receiving Inspection**
   - Documentation review
   - Initial condition assessment
   - Damage recording

2. **Disassembly**
   - Complete teardown
   - Part segregation and tagging
   - Discrepancy documentation

3. **Cleaning**
   - Solvent cleaning
   - Ultrasonic cleaning
   - Drying and preparation

4. **Inspection**
   - Dimensional inspection
   - NDT (ultrasonic, X-ray, dye penetrant)
   - Material analysis
   - Corrosion assessment

5. **Refurbishment**
   - Parts replacement
   - Surface treatment
   - Coating application
   - Machining and finishing

6. **Reassembly**
   - Assembly per specifications
   - Torque requirements
   - Quality checkpoints

7. **Testing**
   - Leak testing
   - Performance testing
   - Thermal cycling
   - Acceptance testing

8. **Certification**
   - Documentation completion
   - Airworthiness/spaceworthiness certification
   - Configuration update

## Overhaul Intervals

- **Time-based**: Calendar time since last overhaul
- **Usage-based**: Flight/mission hours
- **Condition-based**: Performance degradation
- **Event-based**: After specific incidents

## Acceptance Criteria

- **Structural**: No cracks, corrosion, deformation
- **Dimensional**: Within specification tolerances
- **Leak test**: Zero leakage at specified pressure
- **Thermal**: Meets heat rejection requirements
- **Coating**: Proper thickness, adhesion, optical properties

## Review Requirements

Before publishing:
- [ ] Complete process flow validated
- [ ] Inspection criteria defined
- [ ] Acceptance standards documented
- [ ] Test procedures specified
- [ ] Safety requirements included
- [ ] BREX validation passed

## Related Directories

- **[../600-repair/](../600-repair/)** — Component repair procedures
- **[../500-removal-installation/](../500-removal-installation/)** — R&I procedures
- **[../../qc/](../../qc/)** — Quality control documentation

---

**Last Updated**: 2025-10-11
