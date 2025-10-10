# Conventions — Naming and Coding Standards for AMPEL360 AIR-T S1000D

## Purpose

This document defines naming conventions, coding standards, and organizational patterns for S1000D Data Modules, illustrations, and associated content in the AMPEL360 AIR-T program.

## Data Module Code (DMC) Convention

### DMC Structure

```
DMC-<ModelIdent>-<SysDiff>-<SysCode>-<SubSysCode>-<SubSubSysCode>-<AssyCode>-<DisassyCode><DisassyVar>-<InfoCode><InfoVar>-<ItemLoc>_<LangCode>-<CountryCode>_<IssueNum>-<InWork>.xml
```

### AMPEL360 Fixed Values

| Component | Value | Description |
|-----------|-------|-------------|
| ModelIdent | **AMP360** | AMPEL360 AIR-T model identifier |
| SysDiff | **AAA** | Airframes-Aerodynamics-Airworthiness domain |
| AssyCode | **00A** | Standard assembly code |
| ItemLoc | **A** | Standard item location |
| LangCode | **en** | English language |
| CountryCode | **US** | United States variant |

### Variable Components

#### System Code (SysCode)
Based on **ATA Chapters**:
- **53**: Fuselage Structures
- **06**: Dimensions and Stations
- **24**: Electrical Power
- **28**: Fuel (Hydrogen) System
- **57**: Wings

**Examples**:
- `53-10`: Center Body (Fuselage)
- `24-20`: Fuel Cell Power Generation
- `28-10`: Hydrogen Storage

#### Information Code (InfoCode)
Defines **type of information**:

| Range | Type | Description |
|-------|------|-------------|
| 000-039 | Function | System description, theory of operation |
| 040-049 | Description | Component descriptions |
| 050-099 | Operation | Operating instructions |
| 100-199 | Test | Testing and troubleshooting |
| 200-299 | Standard Practices | General procedures |
| 300-399 | Disassembly/Assembly | Removal/installation procedures |
| 400-499 | Servicing | Lubrication, refueling, charging |
| 500-599 | Adjustment/Test | Rigging, calibration |
| 600-699 | Inspection | Visual/detailed inspection |
| 700-799 | Special Tools | Tool descriptions and procedures |
| 800-899 | IPD | Illustrated Parts Data |
| 900-999 | Wiring | Wiring diagrams, electrical schematics |

**InfoCode Variant** (A-Z):
- **A**: Primary variant
- **B-Z**: Alternative variants for same information type

#### Disassembly Code (DisassyCode)
Identifies **specific component** within subsystem:
- `00`: General/overview
- `10-99`: Specific components

**Examples**:
- `53-10-00`: Center Body general
- `53-10-10`: Forward bulkhead
- `53-10-20`: Aft bulkhead
- `53-10-30`: Center body skin panels

**DisassyCode Variant** (0-9):
- **0**: Standard variant
- **1-9**: Configuration variants

#### Issue Number and In-Work
- **IssueNum**: `001` to `999` (increments with each approved release)
- **InWork**: `00` (released), `01-99` (draft/in-work)

### DMC Examples

#### Descriptive DM
```
DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```
- System: 53 (Fuselage)
- Subsystem: 10 (Center Body)
- Component: 00 (General)
- Info: 040A (Description)
- Type: D (Descriptive)
- Released (inWork=00)

#### Procedural DM
```
DMC-AMP360-AAA-53-10-10-00A-310A-P_en-US_002-00.xml
```
- System: 53 (Fuselage)
- Subsystem: 10 (Center Body)
- Component: 10 (Forward Bulkhead)
- Info: 310A (Installation Procedure)
- Type: P (Procedural)
- Issue 2, released

#### IPD DM
```
DMC-AMP360-AAA-53-10-00-00A-800A-I_en-US_001-00.xml
```
- Info: 800A (Illustrated Parts Data)
- Type: I (IPD)

## File Naming Convention

### Data Module Files
**Pattern**: `DMC-<full-dmc>_<lang>-<country>_<issue>-<inwork>.xml`

**Example**:
```
DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```

**Rules**:
- Always `.xml` extension
- No spaces or special characters except hyphen and underscore
- Case-sensitive (use exact case as specified)

### Illustration Control Number (ICN) Files

**Pattern**: `ICN-<SystemCode>-<SubSysCode>-<Type>-<SeqNum>-<Var>.<format>`

**Examples**:
```
ICN-53-10-ISO-001-A.svg
ICN-53-10-EXPL-002-A.png
ICN-53-10-SEC-003-B.svg
ICN-24-20-SCHM-010-A.svg
```

#### ICN Type Codes

| Code | Type | Description |
|------|------|-------------|
| ISO | Isometric | 3D isometric view |
| EXPL | Exploded | Exploded assembly view |
| SEC | Section | Cross-section or cutaway |
| SCHM | Schematic | Electrical/hydraulic schematic |
| WIRE | Wiring | Wiring diagram |
| DET | Detail | Detail view of component |
| ASSY | Assembly | Assembly view |
| PHOTO | Photograph | Photo or realistic rendering |

#### ICN Formats
- **SVG**: Vector graphics (preferred)
- **PNG**: Raster graphics (min 300 DPI)
- **CGM**: Computer Graphics Metafile (legacy)

#### ICN Variant
- **A**: Primary variant
- **B-Z**: Alternative variants (different views, configurations)

### Publication Module (PM) Files

**Pattern**: `PM-<SystemCode>-<SubSysCode>_<Name>_<lang>-<country>_<issue>-<inwork>.xml`

**Example**:
```
PM-53-10_CENTER-BODY_en-US_001-00.xml
```

### Applicability Cross-reference Table (ACT)

**Pattern**: `ACT-<SystemCode>-<SubSysCode>_<lang>-<country>_<issue>-<inwork>.xml`

**Example**:
```
ACT-53-10_en-US_001-00.xml
```

### Data Module Requirements List (DMRL)

**Pattern**: `DMRL-<SystemCode>-<SubSysCode>_<lang>-<country>_<issue>-<inwork>.xml`

**Example**:
```
DMRL-53-10_en-US_001-00.xml
```

### BREX Files

**Pattern**: `DMC-<ModelIdent>-<SysDiff>-00-00-00-00A-000A-A_<lang>-<country>_<issue>-<inwork>.xml`

**Example**:
```
DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml
```

**Note**: BREX uses `00-00-00` for system code (applies to all systems).

## Directory Organization

### CSDB Structure
```
CSDB/
├── DMs/
│   ├── Descriptive/         # Info codes 000-099
│   ├── Procedural/          # Info codes 100-799
│   ├── FaultIsolation/      # Info codes 100-199 (troubleshooting)
│   ├── IPD/                 # Info codes 800-899
│   └── Common/              # Reusable/shared DMs
├── ICN/
│   ├── SVG/                 # Organized by system-subsystem
│   ├── PNG/
│   └── CGM/
├── DMRL/                    # One DMRL per subsystem
├── BREX/                    # Program-level BREX DMs
├── PM/                      # Publication Modules
├── ACT/                     # Applicability tables
├── ExternalPubs/            # External references
└── Reuse/                   # Reusable content fragments
```

### ICN Subdirectories
Organize by system-subsystem:
```
ICN/SVG/
├── 53-10/                   # Center Body
│   ├── ICN-53-10-ISO-001-A.svg
│   ├── ICN-53-10-EXPL-002-A.svg
│   └── ...
├── 53-20/                   # Nose Section
├── 24-20/                   # Fuel Cell Power
└── ...
```

## XML Coding Standards

### Indentation
- **2 spaces** per level (no tabs)
- Consistent indentation throughout

**Example**:
```xml
<dmodule>
  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode modelIdentCode="AMP360" .../>
      </dmIdent>
    </dmAddress>
  </identAndStatusSection>
</dmodule>
```

### Attributes
- **Quote style**: Double quotes (`"`)
- **Order**: Alphabetical (if not specified by schema)
- **Line length**: Max 120 characters (break long attribute lists)

**Example**:
```xml
<dmCode 
  assyCode="00A"
  disassyCode="00"
  disassyCodeVariant="0"
  infoCode="040A"
  infoCodeVariant="A"
  itemLocationCode="A"
  modelIdentCode="AMP360"
  subSubSystemCode="00"
  subSystemCode="10"
  systemCode="53"
  systemDiffCode="AAA"/>
```

### Comments
- Use comments for complex sections
- Include BREX rule IDs in comments where relevant
- No commented-out XML (remove or use DRAFT status)

**Example**:
```xml
<!-- This procedure applies only to MOD-M1 configuration (BREX-055) -->
<applic>
  <cond>
    <applicRefId>MOD-M1</applicRefId>
  </cond>
</applic>
```

### Whitespace
- Blank line between major sections
- No trailing whitespace
- Single blank line at end of file

### Namespaces
Use S1000D Issue 6.0 flat namespace:
```xml
<dmodule xmlns="http://www.s1000d.org/S1000D_6-0/xml_schema_flat"
         xmlns:xlink="http://www.w3.org/1999/xlink">
```

### IDs and References
- **Format**: `<element-type>-<system>-<number>`
- **Examples**:
  - `step-53-10-001`
  - `fig-53-10-iso-001`
  - `table-53-10-torque-001`

**Must be unique** within DM (BREX-014).

## UTCS Anchor Convention

### Format
```
UTCS-<ModelIdent>-<SysDiff>-<SysCode>-<SubSysCode>-DMC-<SeqNum>
```

### Example
```xml
<extension>
  <utcs id="UTCS-AMP360-AAA-53-10-DMC-001"/>
</extension>
```

### Rules
- **Required** in all DMs (BREX-119, BREX-120)
- **Unique** across entire CSDB
- **Sequential**: Increment `<SeqNum>` within subsystem
- **Format validated** by CI/CD

### UTCS Registry
Central registry: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`

CI/CD validates and mirrors UTCS anchors to central registry.

## Metadata Standards

### Issue Date
```xml
<issueDate year="2025" month="10" day="10"/>
```
- **Format**: YYYY-MM-DD
- **Update**: On each release (inWork=00)

### Responsible Partner Company
```xml
<responsiblePartnerCompany enterpriseCode="AAA"/>
```
- **AAA**: AMPEL360 AIR-T program code

### Security Classification
```xml
<security securityClassification="01" commercialExportControl="false"/>
```

| Code | Classification |
|------|----------------|
| 01 | Unclassified |
| 02 | Restricted |
| 03 | Confidential |
| 04 | Secret |
| 05 | Top Secret |

**Default**: `01` (Unclassified)

### Quality Assurance
```xml
<qualityAssurance 
  qaResponsiblePartnerCompany="AAA"
  qaReviewed="true"/>
```
- **qaReviewed**: `true` for released DMs, `false` for drafts

### Reason for Update
**Required** for changed issues (BREX-048):
```xml
<reasonForUpdate>
  Updated torque values per ECO-2025-0042
</reasonForUpdate>
```

## Version Control Integration

### Git Commit Messages
**Format**: `[DMC] <brief description>`

**Examples**:
```
[DMC] Add center body installation procedure (DMC-AMP360-AAA-53-10-10-00A-310A-P)
[DMC] Update torque values in DMC-AMP360-AAA-53-10-00-00A-040A-D
[ICN] Add isometric view for forward bulkhead (ICN-53-10-ISO-001-A)
[BREX] Fix rule AMP360-BREX-087 XPath expression
```

### Branch Naming
- `feature/dmc-<system>-<subsys>-<brief>`
- `bugfix/dmc-<system>-<subsys>-<brief>`
- `release/issue-<issuenum>`

**Examples**:
```
feature/dmc-53-10-installation-procedure
bugfix/dmc-53-10-torque-values
release/issue-002
```

## Quality Gates

### Pre-commit Checks
- [ ] Valid XML syntax
- [ ] Schema validation (XSD)
- [ ] File naming convention
- [ ] UTCS anchor present

### Pre-merge Checks
- [ ] BREX validation (120 rules)
- [ ] Schematron validation
- [ ] Link checking (internal/external refs)
- [ ] Peer review completed

### Pre-release Checks
- [ ] QA review approved
- [ ] qaReviewed="true"
- [ ] inWork="00"
- [ ] Issue number incremented
- [ ] UTCS registry updated

## Tools and Automation

### Validation Scripts
```bash
# Validate DMC naming
python tools/validate_dmc_naming.py CSDB/DMs/

# Validate BREX compliance
python VALIDATION/BREX/validate_brex.py CSDB/DMs/

# Check UTCS anchors
python tools/validate_utcs.py CSDB/DMs/
```

### Automatic Naming
Use templates to generate properly named files:
```bash
# Generate new DM from template
python tools/new_dm.py --system 53 --subsystem 10 --info 310 --type P
```

### Batch Operations
```bash
# Increment issue numbers for release
python tools/increment_issue.py CSDB/DMs/Procedural/

# Update issue dates
python tools/update_dates.py CSDB/DMs/
```

## Compliance Summary

### BREX Rules Related to Naming/Conventions
- **BREX-021**: ModelIdentCode = AMP360
- **BREX-022**: SystemDiffCode = AAA
- **BREX-024**: AssyCode = 00A
- **BREX-025**: ItemLocationCode = A
- **BREX-030**: CountryIsoCode = US
- **BREX-031**: LanguageIsoCode = en
- **BREX-093**: No spaces in ICN filenames
- **BREX-119**: UTCS anchor required
- **BREX-120**: UTCS format validated

### Validation Coverage
All naming conventions are enforced by:
1. XSD schema validation
2. BREX rules
3. CI/CD pipeline checks
4. Pre-commit hooks

## Support and Resources

### Naming Tools
- DMC generator: `tools/new_dm.py`
- ICN naming checker: `tools/validate_icn_naming.py`
- UTCS generator: `tools/generate_utcs.py`

### Reference Documents
- S1000D Issue 6.0 Specification (Chap 7: Data Module Code)
- ATA iSpec 2200 (Chapter/Section numbering)
- AMPEL360 System Breakdown Structure

### Support Contacts
- **Naming Questions**: tech-pubs@ampel360.eu
- **UTCS Issues**: config-mgmt@ampel360.eu
- **Tool Support**: automation@ampel360.eu

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-10  
**Owner**: Technical Publications Office  
**Review Cycle**: Annually or with S1000D updates
