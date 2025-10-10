# VARIANTS — Model Variants for Different Configurations

## Purpose

This directory contains variant models for different configurations of the 53-10 Center Body, including test articles and production flight articles with their specific design differences.

## Organization

Variants are organized by configuration type:

- **TEST_ARTICLE/** — Test and validation article configurations
- **FLIGHT_ARTICLE/** — Production flight-ready configurations

## Naming Convention

Use the following pattern for variant models:
```
53-10_<VARIANT>_<COMPONENT>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_TEST_FRAME_FR-001_STATIC-TEST_v01.CATPart`
- `53-10_FLIGHT_SKIN_PANEL_SP-001_PRODUCTION_v02.prt`
- `53-10_TEST_ASSY_TA-001_PRESSURE-TEST_v01.CATProduct`

## Variant Differences

### TEST_ARTICLE
Test articles may include:
- Additional instrumentation provisions
- Modified geometry for test fixture attachment
- Simplified features for rapid prototyping
- Extra material for proof testing
- Test-specific interfaces

### FLIGHT_ARTICLE
Flight articles include:
- Production-intent geometry
- Flight-certified materials
- Final surface treatments
- As-designed interfaces
- Weight-optimized features

## Configuration Management

Each variant must:
- Be clearly labeled with variant designation
- Document differences from baseline design
- Include configuration justification
- Reference applicable test or flight requirements
- Maintain traceability to baseline models

## Naming and Organization

Files should clearly indicate variant type:
- Use `TEST_` or `FLIGHT_` prefix
- Include variant identifier in part number
- Store in appropriate subdirectory
- Cross-reference to baseline in [`../PARTS/`](../PARTS/)

## Related Documentation

- **Baseline parts**: [`../PARTS/`](../PARTS/)
- **Configuration rules**: [`../CONFIG/`](../CONFIG/)
- **Test requirements**: [`../../../../../../../../00-PROGRAM/VERIFICATION/`](../../../../../../../../00-PROGRAM/VERIFICATION/)
- **Production specifications**: [`../../MBOM/`](../../MBOM/)

## Quality Requirements

All variants must:
- [ ] Document deviation from baseline
- [ ] Include configuration justification
- [ ] Pass variant-specific checks
- [ ] Be approved by change control board
- [ ] Maintain interface compatibility where required
