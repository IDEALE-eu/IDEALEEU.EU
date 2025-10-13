# Descriptive Data Modules (DMC: D)

## Purpose

This directory contains **Descriptive Data Modules** for the AMPEL360 AIR-T 53-10 Center Body subsystem. Descriptive DMs provide system descriptions, theory of operation, and component overviews.

## InfoCode Range

**040-049**: Component descriptions
- **040A**: General description
- **041A**: System description
- **042A**: Component description
- **043A**: Installation description
- **044A**: Interface description

**000-039**: Functional descriptions (also descriptive)
- **000A**: System function
- **001A**: Operational theory

## Content Types

### System Descriptions
- Overall system architecture
- System boundaries and interfaces
- Functional requirements
- Operating principles

### Component Descriptions
- Physical description
- Location and mounting
- Specifications
- Key features
- Related components

### Theory of Operation
- How the system/component works
- Operational modes
- Control logic
- Safety features

## DMC Naming Pattern

```
DMC-AMP360-AAA-53-10-<XX>-00A-<InfoCode><Var>-D_en-US_<Issue>-<InWork>.xml
```

Where:
- `<XX>` = Disassembly code (00=general, 10-99=specific components)
- `<InfoCode>` = 040-049 for descriptions
- `<Var>` = A-Z variant (usually A)
- `<Issue>` = 001, 002, 003...
- `<InWork>` = 00 (released) or 01-99 (draft)

## Examples

### General Center Body Description
```
DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```
- General description of the entire Center Body subsystem
- InfoCode 040A: General description

### Forward Bulkhead Description
```
DMC-AMP360-AAA-53-10-10-00A-040A-D_en-US_001-00.xml
```
- Description of the forward bulkhead component
- Disassembly code 10: Forward bulkhead
- InfoCode 040A: Component description

### Aft Bulkhead Description
```
DMC-AMP360-AAA-53-10-20-00A-040A-D_en-US_001-00.xml
```
- Description of the aft bulkhead component
- Disassembly code 20: Aft bulkhead

## Template

Use the descriptive template:
```bash
../../TEMPLATES/DMs/TEMPLATE_Descriptive_DM.xml
```

## Content Structure

Typical sections in a descriptive DM:
1. **Introduction** - Brief overview
2. **Description** - Detailed description
3. **Features** - Key features and characteristics
4. **Specifications** - Technical specifications
5. **Related Information** - Cross-references

## ASD-STE-100 Guidelines

- Use approved words only
- Simple sentence structure (max 20 words)
- Active voice for instructions
- Present tense for descriptions
- Consistent terminology

## Quality Checklist

- [ ] DMC follows naming convention
- [ ] Metadata complete (DMC, issue, language, security)
- [ ] UTCS anchors included for traceability
- [ ] Content uses ASD-STE-100 Simplified English
- [ ] Technical accuracy verified by SME
- [ ] Cross-references validated
- [ ] Illustrations referenced correctly
- [ ] BREX validation passed
- [ ] Peer review completed
- [ ] QA approval obtained

## Validation

```bash
# Validate single DM
python ../../../VALIDATION/BREX/validate_brex.py DMC-*.xml

# Validate all descriptive DMs
python ../../../VALIDATION/BREX/validate_brex.py .
```

## Related Resources

- **Style Guide**: `../../../GUIDES/StyleGuide.md`
- **Language Guide**: `../../../GUIDES/Language.md`
- **Conventions**: `../../../GUIDES/Conventions.md`
- **BREX Rules**: `../../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`
