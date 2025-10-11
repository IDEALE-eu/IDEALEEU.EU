# STANDARDS — Standards Applicability & Compliance

## Purpose

This directory contains documentation of applicable standards, their implementation, deviations, waivers, and normative references for the 21-10 RADIATORS_HEAT_EXCHANGERS subsystem.

## Contents

### Subdirectories

- [**applicability_matrix/**](./applicability_matrix/) - Standards Applicability Matrix (SAM)
- [**deviations_waivers/**](./deviations_waivers/) - Deviations, waivers, NCR with risk assessments
- [**refs/**](./refs/) - Normative reference list (standard IDs and versions)

## Applicable Standards

### ECSS Standards
- **ECSS-E-ST-10C**: System engineering general requirements
- **ECSS-E-ST-31C**: Thermal control
- **ECSS-E-ST-32C**: Structural general requirements
- **ECSS-Q-ST-70C**: Materials, mechanical parts, and processes
- **ECSS-E-ST-10-03C**: Testing

### NASA Standards
- **NASA-STD-5001**: Structural design and test factors of safety
- **NASA-STD-6016**: Standard materials and processes requirements
- **NASA-STD-7009**: Standard for models and simulations
- **NASA-STD-8739**: Workmanship standards

### Industry Standards
- **ASTM E595**: Outgassing test for space materials
- **MIL-STD-1540E**: Test requirements for launch vehicles
- **ISO 1101**: Geometric product specifications
- **AS9100**: Quality management systems

## Standards Applicability Matrix (SAM)

The SAM documents:
- Which standards apply to this subsystem
- Specific clauses and requirements
- Level of applicability (Full/Partial/Not Applicable)
- Compliance method and evidence
- Approved deviations or tailoring

## Compliance Philosophy

### Full Compliance
Standards fully applicable without modification:
- Design requirements
- Material selection
- Process qualification
- Test methods

### Partial Compliance (Tailoring)
Standards with approved modifications:
- Reduced test levels (if justified)
- Alternative methods (equivalent performance)
- Scope reduction (not applicable sections)

### Non-Compliance (Waiver)
Requirements not met with formal waiver:
- Technical impossibility
- Risk acceptance by authority
- Mitigation measures implemented

## File Naming

```
21-10-CMP-STD_<artifact>__r<NN>__<STATUS>.<ext>
```

Examples:
- `21-10-CMP-STD-SAM-master__r02__REL.xlsx`
- `21-10-CMP-STD-REFS-normative__r01__REL.pdf`
- `21-10-CMP-STD-WAIVER-thermal-margin__r01__REL.pdf`

## Review Process

1. Standards identification during requirements phase
2. Applicability assessment at PDR
3. Compliance demonstration at CDR
4. Final verification at acceptance review
5. Deviation/waiver approval by Design Review Board (DRB)

## Configuration Control

- Standards list baselined at PDR
- Changes require ECN approval
- Waivers tracked in NCR system
- Customer approval for critical deviations

## Standards

Self-referencing:
- **ECSS-M-ST-10C**: Project planning and implementation
- **ISO 9001**: Quality management
- **AS9100**: Aerospace quality management

## Related Documentation

- Requirements: [`../requirements/`](../requirements/)
- Test evidence: [`../test_evidence/`](../test_evidence/)
- Certificates: [`../certificates/`](../certificates/)
