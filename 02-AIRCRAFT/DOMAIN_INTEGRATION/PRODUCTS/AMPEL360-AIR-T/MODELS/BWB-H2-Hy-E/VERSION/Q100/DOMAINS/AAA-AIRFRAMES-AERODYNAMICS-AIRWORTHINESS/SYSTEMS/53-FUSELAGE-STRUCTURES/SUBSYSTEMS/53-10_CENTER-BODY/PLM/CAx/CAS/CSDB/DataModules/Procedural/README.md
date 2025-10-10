# Procedural Data Modules (DMC: P)

## Purpose

This directory contains **Procedural Data Modules** for the AMPEL360 AIR-T 53-10 Center Body subsystem. Procedural DMs provide step-by-step instructions for maintenance, installation, removal, servicing, inspection, and adjustment tasks.

## InfoCode Ranges

### Disassembly/Assembly (300-399)
- **310A**: Removal procedure
- **320A**: Installation procedure
- **330A**: Disassembly procedure
- **340A**: Assembly procedure
- **350A**: Access procedure

### Servicing (400-499)
- **410A**: Lubrication procedure
- **420A**: Cleaning procedure
- **430A**: Refueling/charging procedure
- **440A**: Fluid servicing
- **450A**: Filter replacement

### Adjustment/Test (500-599)
- **510A**: Adjustment procedure
- **520A**: Rigging procedure
- **530A**: Calibration procedure
- **540A**: Functional test
- **550A**: Operational test

### Inspection (600-699)
- **610A**: Visual inspection
- **620A**: Detailed inspection
- **630A**: Special inspection
- **640A**: Non-destructive inspection
- **650A**: Structural inspection

## DMC Naming Pattern

```
DMC-AMP360-AAA-53-10-<XX>-00A-<InfoCode><Var>-P_en-US_<Issue>-<InWork>.xml
```

Where:
- `<XX>` = Disassembly code (00=general, 10-99=specific components)
- `<InfoCode>` = 300-699 for procedures
- `<Var>` = A-Z variant (usually A)
- `<Issue>` = 001, 002, 003...
- `<InWork>` = 00 (released) or 01-99 (draft)

## Examples

### Forward Bulkhead Removal
```
DMC-AMP360-AAA-53-10-10-00A-310A-P_en-US_001-00.xml
```
- Procedure to remove the forward bulkhead
- Disassembly code 10: Forward bulkhead
- InfoCode 310A: Removal procedure

### Forward Bulkhead Installation
```
DMC-AMP360-AAA-53-10-10-00A-320A-P_en-US_001-00.xml
```
- Procedure to install the forward bulkhead
- InfoCode 320A: Installation procedure

### Center Body Visual Inspection
```
DMC-AMP360-AAA-53-10-00-00A-610A-P_en-US_001-00.xml
```
- General visual inspection of Center Body
- Disassembly code 00: General
- InfoCode 610A: Visual inspection

## Template

Use the procedural template:
```bash
../../TEMPLATES/DMs/TEMPLATE_Procedural_DM.xml
```

## Content Structure

Every procedural DM must include:

### 1. Prerequisites
- Required conditions
- Prior procedures that must be completed
- System state requirements

### 2. Required Tools
- Special tools
- Common tools
- Test equipment
- Consumables

### 3. Required Materials
- Parts and materials
- Consumables
- Lubricants, sealants, etc.

### 4. Safety Information
- Warnings (risk of injury)
- Cautions (risk of equipment damage)
- Notes (important information)
- Personal protective equipment

### 5. Procedure Steps
- Numbered sequential steps
- Clear, concise instructions
- One action per step
- Illustrations/photos where needed

### 6. Close-out Requirements
- Inspection requirements
- Verification steps
- Documentation requirements
- Return to service criteria

## Procedure Types

### Removal Procedures (310-319)
1. Preparation and safety
2. Access steps
3. Disconnection steps
4. Removal steps
5. Post-removal inspection
6. Storage requirements

### Installation Procedures (320-329)
1. Pre-installation inspection
2. Positioning
3. Connection steps
4. Torque requirements
5. Verification
6. Access closure

### Inspection Procedures (600-699)
1. Preparation
2. Inspection points
3. Acceptance criteria
4. Rejection criteria
5. Documentation requirements

## ASD-STE-100 Guidelines

### Command Structure
- Use imperative mood: "Remove the bolt"
- One command per step
- Active voice
- Present tense

### Step Numbering
- Main steps: 1, 2, 3...
- Sub-steps: a, b, c...
- Use only when necessary

### Safety Messages
- **WARNING**: Risk of personal injury or death
- **CAUTION**: Risk of equipment damage
- **NOTE**: Important information

## Quality Checklist

- [ ] DMC follows naming convention
- [ ] Metadata complete and correct
- [ ] UTCS anchors included
- [ ] Prerequisites clearly stated
- [ ] Tools and materials listed
- [ ] Safety messages properly formatted
- [ ] Steps clear and sequential
- [ ] One action per step
- [ ] Illustrations referenced correctly
- [ ] Close-out requirements specified
- [ ] Technical accuracy verified
- [ ] ASD-STE-100 compliance checked
- [ ] BREX validation passed
- [ ] Peer review completed
- [ ] QA approval obtained

## Validation

```bash
# Validate single procedural DM
python ../../../VALIDATION/BREX/validate_brex.py DMC-*-P_*.xml

# Validate all procedural DMs
python ../../../VALIDATION/BREX/validate_brex.py .
```

## Safety Requirements

### WARNING Usage
Use for procedures that could result in:
- Personal injury
- Loss of life
- Serious equipment damage

### CAUTION Usage
Use for procedures that could result in:
- Equipment damage
- Mission failure
- Data loss

### NOTE Usage
Use for:
- Important information
- Helpful hints
- Best practices

## Related Resources

- **Style Guide**: `../../../GUIDES/StyleGuide.md`
- **Language Guide**: `../../../GUIDES/Language.md`
- **Conventions**: `../../../GUIDES/Conventions.md`
- **BREX Rules**: `../../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`
- **Special Tools**: See InfoCode 700-799 DMs
