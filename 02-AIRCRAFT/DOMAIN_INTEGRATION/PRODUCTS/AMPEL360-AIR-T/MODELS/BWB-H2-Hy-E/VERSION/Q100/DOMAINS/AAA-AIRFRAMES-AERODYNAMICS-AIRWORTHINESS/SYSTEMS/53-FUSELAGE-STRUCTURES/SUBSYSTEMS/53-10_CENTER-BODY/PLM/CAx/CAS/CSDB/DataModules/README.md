# DataModules - S1000D Data Modules Repository

## Overview

This directory contains the S1000D Issue 6.0 compliant Data Modules (DMs) for the AMPEL360 AIR-T BWB-H2-Hy-E aircraft, specifically for the **53-10 Center Body** subsystem.

Data Modules are the fundamental building blocks of S1000D technical publications. Each DM is a self-contained unit of information covering a specific topic or procedure.

## Directory Structure

```
DataModules/
├── Descriptive/        # Descriptive Data Modules (DMC: D)
├── Procedural/         # Procedural Data Modules (DMC: P)
├── IPD/               # Illustrated Parts Data (DMC: I)
├── Wiring/            # Wiring and Schematics (DMC: W)
└── FunctionalTest/    # Functional Test Modules (DMC: T)
```

## Data Module Types

### Descriptive (InfoCode 040-049)
- **Purpose**: System and component descriptions
- **DMC Type**: D (Descriptive)
- **Content**: System theory of operation, component descriptions, functional overviews
- **Example**: `DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml`

### Procedural (InfoCode 300-399, 400-699)
- **Purpose**: Maintenance and operational procedures
- **DMC Type**: P (Procedural)
- **Content**: Installation, removal, servicing, inspection, adjustment procedures
- **Example**: `DMC-AMP360-AAA-53-10-10-00A-310A-P_en-US_001-00.xml`

### Illustrated Parts Data (InfoCode 800-899)
- **Purpose**: Parts catalogs with illustrations
- **DMC Type**: I (IPD)
- **Content**: Parts lists, part numbers, illustrations, applicability
- **Example**: `DMC-AMP360-AAA-53-10-00-00A-800A-I_en-US_001-00.xml`

### Wiring (InfoCode 900-999)
- **Purpose**: Electrical wiring diagrams and schematics
- **DMC Type**: W (Wiring)
- **Content**: Wiring diagrams, electrical schematics, connector pinouts
- **Example**: `DMC-AMP360-AAA-53-10-00-00A-900A-W_en-US_001-00.xml`

### Functional Test (InfoCode 100-199)
- **Purpose**: Testing and troubleshooting procedures
- **DMC Type**: T (Test)
- **Content**: Functional tests, troubleshooting, fault isolation
- **Example**: `DMC-AMP360-AAA-53-10-00-00A-100A-T_en-US_001-00.xml`

## Naming Convention

All Data Modules follow the standard DMC naming convention:

```
DMC-<ModelIdent>-<SysDiff>-<SysCode>-<SubSysCode>-<SubSubSysCode>-<AssyCode>-<DisassyCode><DisassyVar>-<InfoCode><InfoVar>-<ItemLoc>_<LangCode>-<CountryCode>_<IssueNum>-<InWork>.xml
```

### AMPEL360 Standard Values
- **ModelIdent**: AMP360
- **SysDiff**: AAA (Airframes-Aerodynamics-Airworthiness)
- **SysCode**: 53 (Fuselage Structures)
- **SubSysCode**: 10 (Center Body)
- **AssyCode**: 00A
- **ItemLoc**: A
- **LangCode-CountryCode**: en-US

## Creating New Data Modules

### From Templates
Use the templates in `../../TEMPLATES/DMs/`:
- `TEMPLATE_Descriptive_DM.xml` - For descriptive content
- `TEMPLATE_Procedural_DM.xml` - For procedural content

### Example Workflow
```bash
# Copy template
cp ../../TEMPLATES/DMs/TEMPLATE_Descriptive_DM.xml \
   Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-01.xml

# Edit content
# ... update metadata, content, UTCS anchors ...

# Validate against BREX
python ../../VALIDATION/BREX/validate_brex.py \
   Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-01.xml

# Release (update inWork from 01 to 00)
mv Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-01.xml \
   Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```

## Validation

All Data Modules must:
1. **Validate against S1000D XML Schema** (XSD)
2. **Pass BREX validation** (120 business rules)
3. **Comply with ASD-STE-100** Simplified Technical English
4. **Include UTCS anchors** for traceability
5. **Pass quality review** before release (inWork=00)

### Validation Command
```bash
# Validate single DM
python ../../VALIDATION/BREX/validate_brex.py <dm-file>

# Validate entire directory
python ../../VALIDATION/BREX/validate_brex.py DataModules/
```

## Metadata Requirements

Every Data Module must include:
- **DMC** (Data Module Code) - Unique identifier
- **Issue Info** - Version and status (inWork flag)
- **Language** - en-US for AMPEL360
- **Security Classification** - Default: 01 (Unclassified)
- **Responsible Partner Company** - Authoring organization
- **Originator** - Technical author
- **Applicability** - Reference to ACT for configuration control
- **UTCS Anchors** - Traceability to requirements

## Version Control

- **Issue Number**: Increments with each approved release (001, 002, 003...)
- **In-Work**: 00 = Released, 01-99 = Draft/in-work
- **Example**: `001-01` = Issue 1, Draft 1; `001-00` = Issue 1, Released

## Quality Gates

Before releasing a Data Module (setting inWork=00):
1. ✅ Content complete and technically accurate
2. ✅ All XSD and BREX validation passed
3. ✅ ASD-STE-100 compliance verified
4. ✅ UTCS anchors validated
5. ✅ Peer review completed
6. ✅ Quality assurance approval obtained

## Related Resources

- **BREX Rules**: `../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`
- **Templates**: `../../TEMPLATES/DMs/`
- **Style Guide**: `../../GUIDES/StyleGuide.md`
- **Conventions**: `../../GUIDES/Conventions.md`
- **Language Guide**: `../../GUIDES/Language.md`
- **Validation**: `../../VALIDATION/`

## S1000D Compliance

This implementation follows:
- **S1000D Issue 6.0** specification
- **ASD-STE-100** Simplified Technical English
- **ATA iSpec 2200** chapter numbering (where applicable)
- **AMPEL360 program standards** and business rules

## Support

For questions or issues:
- Review the guides in `../../GUIDES/`
- Check BREX rules in `../BREX/`
- Consult validation reports in `../../VALIDATION/Reports/`
- Contact the AMPEL360 technical publications team
