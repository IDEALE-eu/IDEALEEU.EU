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
- **ModelIdent**: AMP360 (or Q100 for version-specific modules)
- **SysDiff**: AAA (Airframes-Aerodynamics-Airworthiness) or system-specific code (e.g., 53)
- **SysCode**: 53 (Fuselage Structures)
- **SubSysCode**: 10 (Center Body)
- **AssyCode**: 00A (for AMP360) or 00 (for Q100)
- **ItemLoc**: A
- **LangCode-CountryCode**: en-US (or es-ES for Spanish variants)

### Q100 Variant

Some Data Modules use **Q100** as the `modelIdentCode` to represent version-specific content:
- **Purpose**: Version/family-specific technical documentation
- **Example**: `DMC-Q100-53-10-00-00-00-0-000-0-A_es-ES_001-00.xml`
- **Language**: Typically es-ES (Spanish) for Q100 modules
- **Documentation**: See `Descriptive/00_GENERAL/DMC/README_Q100.md` for details
- **BREX**: Uses `DMC-Q100-BREX-AAA-STRUCTURES-00-00-0-0-000-A-A_es-ES_001-00.xml`

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
5. **Reference ICNs correctly** from the Centralized Illustration Repository (CIR)
6. **Pass quality review** before release (inWork=00)

### Validation Command
```bash
# Validate single DM
python ../../VALIDATION/BREX/validate_brex.py <dm-file>

# Validate entire directory
python ../../VALIDATION/BREX/validate_brex.py DataModules/

# Check ICN links
python ../../VALIDATION/tools/check_links.py DataModules/
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
- **CIR (Illustrations)**: `../Illustrations/CIR/` - Centralized Illustration Repository

## Illustrations and ICN References

### Centralized Illustration Repository (CIR)

All illustrations are stored in the **Centralized Illustration Repository (CIR)** at:
```
../Illustrations/CIR/53-10/
```

Instead of maintaining ICN subdirectories within each DataModule folder, all ICNs are centralized. This provides:
- Single source of truth for all illustrations
- Reusability across multiple Data Modules
- Easier version control and maintenance
- Simplified CI/CD validation

### Referencing ICNs in Data Modules

Use **relative paths** to reference illustrations from the CIR:

```xml
<!-- From DataModules/Descriptive/10_SYSTEM-DESCRIPTION/DMC-xxx.xml -->
<figure>
  <title>Center Body Aft Bulkhead Assembly</title>
  <graphic infoEntityIdent="ICN-53-10-20-0001-A">
    <sheet chgType="new" gnbr="00" revdate="2025-10-10"
           infoEntityIdent="ICN-53-10-20-0001-A">
      <graphicRef xlink:href="../../../Illustrations/CIR/53-10/DERIVED/SVG/ICN-53-10-20-0001-A.svg"/>
    </sheet>
  </graphic>
</figure>
```

### Interactive Graphics with Hotspots

For interactive illustrations with clickable hotspot regions:

```xml
<figure>
  <title>Center Body Aft Bulkhead (Interactive)</title>
  <graphic infoEntityIdent="ICN-53-10-20-0001-A">
    <hotspot>
      <hotspotRef xlink:href="../../../Illustrations/CIR/53-10/HOTSPOTS/ICN-53-10-20-0001-A.map.xml"/>
    </hotspot>
  </graphic>
</figure>
```

### Path Calculation

From a DM located at `DataModules/Descriptive/10_SYSTEM-DESCRIPTION/`:
1. Go up 3 directory levels: `../../../`
2. Navigate to CIR: `Illustrations/CIR/53-10/`
3. Select format: `DERIVED/SVG/`
4. Reference file: `ICN-53-10-20-0001-A.svg`

Result: `../../../Illustrations/CIR/53-10/DERIVED/SVG/ICN-53-10-20-0001-A.svg`

### ICN Naming Pattern

```
ICN-<chapter>-<section>-<subsection>-<seq>-<issue>.<ext>
```

Example: `ICN-53-10-20-0001-A.svg`
- **53**: Fuselage Structures (chapter)
- **10**: Center Body (subsystem)
- **20**: Aft Bulkhead (component)
- **0001**: Sequential number
- **A**: Revision letter
- **svg**: File format

For more details, see:
- CIR Documentation: `../Illustrations/CIR/README.md`
- Naming Conventions: `../../GUIDES/Conventions.md`

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
