# CAS — Continuous Acquisition and Sustainment (S1000D CSDB)

## Purpose

This directory contains the **Common Source Database (CSDB)** and supporting infrastructure for S1000D-compliant technical publications for the 53-10 Center Body subsystem of AMPEL360 AIR-T BWB-H2-Hy-E aircraft.

The CAS structure implements:
- **CSDB**: Common Source Database for Data Modules (DMs), illustrations, and metadata
- **BREX**: Business Rules Exchange for validation
- **VALIDATION**: Schemas and quality gates
- **IETP**: Interactive Electronic Technical Publications
- **TEMPLATES**: Reusable templates and patterns
- **GUIDES**: Style guides and conventions

## Directory Structure

```
CAS/
├── README.md                    # This file
├── CSDB/                        # Common Source Database
│   ├── DMs/                     # Data Modules
│   │   ├── Descriptive/         # Descriptive Data Modules
│   │   ├── Procedural/          # Procedural Data Modules
│   │   ├── FaultIsolation/      # Fault Isolation Data Modules
│   │   ├── IPD/                 # Illustrated Parts Data
│   │   └── Common/              # Common/reusable Data Modules
│   ├── ICN/                     # Illustration Control Numbers
│   │   ├── SVG/                 # SVG format illustrations
│   │   ├── PNG/                 # PNG format illustrations
│   │   └── CGM/                 # CGM format illustrations
│   ├── DMRL/                    # Data Module Requirements List
│   ├── BREX/                    # Business Rules Exchange
│   ├── PM/                      # Publication Modules
│   ├── ACT/                     # Applicability Cross-reference Table
│   │   └── keys/                # ACT key definitions
│   ├── ExternalPubs/            # External publication references
│   └── Reuse/                   # Reusable content fragments
├── VALIDATION/                  # Validation infrastructure
│   ├── XSD/                     # XML Schema definitions
│   ├── Schematron/              # Schematron validation rules
│   ├── BREX/                    # BREX validation scripts
│   └── Reports/                 # Validation reports
├── IETP/                        # Interactive Electronic Technical Publication
│   ├── Packages/                # IETP delivery packages
│   └── SCORM/                   # SCORM-compliant packages
├── TEMPLATES/                   # Templates and patterns
│   ├── DMs/                     # Data Module templates
│   ├── ICN/                     # Illustration templates
│   ├── PublicationModule/       # PM templates
│   └── Naming/                  # Naming convention guides
└── GUIDES/                      # Style guides and documentation
    ├── StyleGuide.md            # AMPEL360 style guide
    ├── Language.md              # ASD-STE-100 language guide
    └── Conventions.md           # Naming and coding conventions
```

## S1000D Issue 6.0 Compliance

This CSDB implements **S1000D Issue 6.0** with:
- Flat namespace schema (`http://www.s1000d.org/S1000D_6-0/xml_schema_flat`)
- Business Rules Exchange (BREX) with 120 validation rules
- UTCS (Universal Traceability and Configuration System) integration
- ASD-STE-100 Simplified Technical English compliance

## BREX Rules

The **BREX Data Module** (`DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`) contains **120 validation rules** organized into categories:

1. **IDS & Metadata (001-020)**: Core metadata requirements
2. **DMC & Ownership (021-030)**: Data Module Code standards
3. **Language & Localization (031-040)**: Language and style compliance
4. **Security & QA (041-050)**: Security classification and quality assurance
5. **Applicability & ACT (051-060)**: Applicability and effectivity rules
6. **Procedural Structure (061-075)**: Procedural content rules
7. **Fault Isolation (076-085)**: Fault isolation procedures
8. **Illustrations & Graphics (086-095)**: Graphics and ICN requirements
9. **IPD & Logistics (096-105)**: Illustrated Parts Data requirements
10. **References & Linking (106-110)**: Cross-references and external links
11. **Controlled Language & Domain Safety (111-120)**: ASD-STE-100 and domain-specific safety

See [`CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv`](CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv) for complete rule listing.

## Validation Pipeline

Data Modules must pass through this validation pipeline:

```
DM Creation
    ↓
XSD Validation (schema)
    ↓
Schematron Validation (business rules)
    ↓
BREX Validation (120 rules)
    ↓
DMRL Gating (requirements check)
    ↓
QA Review
    ↓
Publication
```

### Validation Severity Levels

- **ERROR**: Blocking issue; DM cannot be released
- **WARN**: Advisory issue; should be addressed but not blocking

## DMC Naming Convention

Data Module Codes follow S1000D structure:

```
DMC-<ModelIdentCode>-<SystemDiffCode>-<SystemCode>-<SubSystemCode>-<SubSubSystemCode>-<AssyCode>-<DisassyCode><DisassyCodeVariant>-<InfoCode><InfoCodeVariant>-<ItemLocationCode>_<LanguageIsoCode>-<CountryIsoCode>_<IssueNumber>-<InWork>.xml
```

**AMPEL360 AIR-T Standards:**
- `ModelIdentCode`: **AMP360**
- `SystemDiffCode`: **AAA**
- `AssyCode`: **00A**
- `ItemLocationCode`: **A**
- `LanguageIsoCode`: **en**
- `CountryIsoCode`: **US**

**Example:**
```
DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-00.xml
```

## UTCS Integration

All Data Modules must include a **UTCS anchor** in the IDS extension:

```xml
<identAndStatusSection>
  <dmAddress>
    <dmIdent>
      <!-- ... dmCode, language, issueInfo ... -->
      <extension>
        <utcs id="UTCS-AMP360-AAA-53-10-DMC-001"/>
      </extension>
    </dmIdent>
    <!-- ... -->
  </dmAddress>
  <!-- ... -->
</identAndStatusSection>
```

BREX rules **AMP360-BREX-119** and **AMP360-BREX-120** enforce UTCS presence. CI/CD validates format and mirrors to `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`.

## Quick Start

### Creating a New Data Module

1. **Select appropriate template** from `TEMPLATES/DMs/`
2. **Copy and rename** following DMC convention
3. **Update metadata**:
   - DMC components
   - Issue date
   - Responsible partner
   - Security classification
   - UTCS anchor
4. **Author content** following ASD-STE-100
5. **Validate** using validation pipeline
6. **Submit for QA review**

### Running Validation

```bash
# Validate single DM
python VALIDATION/BREX/validate_brex.py path/to/DM.xml

# Validate all DMs in directory
python VALIDATION/BREX/validate_brex.py CSDB/DMs/
```

## Style Guidelines

### ASD-STE-100 Compliance

- Use simple, direct language
- Prefer active voice ("Remove the cover", not "The cover should be removed")
- Avoid vague adverbs ("carefully", "properly", "sufficiently")
- Avoid intensifiers ("very", "really", "quite")
- Use approved technical words only
- Sentences ≤ 25 words preferred

### U.S. English

- Use U.S. spelling: "color" not "colour", "center" not "centre"
- Use U.S. date format: YYYY-MM-DD

### Safety Messages

- **WARNING**: Risk of death or serious injury
- **CAUTION**: Risk of equipment damage or minor injury
- Never nest safety messages inside `<note>` elements
- Safety messages must precede the hazardous step

### Domain-Specific Safety (AMPEL360 AIR-T)

- **Hydrogen/H2**: Always include safety warnings for hydrogen handling
- **Cryogenic**: Verify PPE and handling steps for cryogenic systems
- **High Voltage/HV**: Verify LOTO (Lock-Out Tag-Out) references

## Publication Modules

Publication Modules (PMs) aggregate Data Modules into deliverable publications:

- **Technical Manuals** (TM)
- **Illustrated Parts Catalogs** (IPC)
- **Fault Isolation Manuals** (FIM)
- **Component Maintenance Manuals** (CMM)

See `CSDB/PM/PM-53-10_CENTER-BODY_en-US_001-00.xml` for the master PM.

## Applicability

Use the **Applicability Cross-reference Table (ACT)** to manage configuration variants:

- **Configuration sets**: CFG-BASELINE-Q100, CFG-PAX-Q100
- **Modification states**: MOD-BASE, MOD-M1, MOD-M2
- **Serial number blocks**: BLK-2026A, BLK-2026B
- **Customer options**: OPT-AVIONICS-SUITE, OPT-CABIN-LAYOUT

See `CSDB/ACT/act.xml` for ACT definitions and keys.

## IETP Delivery

Interactive Electronic Technical Publications (IETP) are delivered as:

1. **S1000D Viewer Packages**: ZIP archives with DMs, ICNs, and PM
2. **SCORM Packages**: SCORM 2004 compliant for LMS integration
3. **Web Viewer**: HTML5-based viewer for browser access

Packages are generated from CSDB content and include navigation, search, and applicability filtering.

## CI/CD Integration

This CSDB is validated in CI/CD pipelines:

1. **XSD validation** (schema compliance)
2. **Schematron validation** (business rules)
3. **BREX validation** (120 AMPEL360 rules)
4. **DMRL gating** (requirements traceability)
5. **Link checking** (internal/external references)
6. **UTCS format validation** (traceability anchor format)
7. **UTCS mirroring** (update central UTCS index)

See `00-PROGRAM/CONFIG_MGMT/12-CI/` for CI scripts.

## Related Documentation

- **Configuration Management**: [`00-PROGRAM/CONFIG_MGMT/`](../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **UTCS Central Registry**: [`00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`](../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/)
- **Requirements Traceability**: [`03-TRACEABILITY/`](../../../../03-TRACEABILITY/)
- **CAD Models**: [`../CAD/`](../CAD/)
- **CAE Analysis**: [`../CAE/`](../CAE/)

## Standards and Specifications

- **S1000D Issue 6.0**: International specification for technical publications
- **ASD-STE-100**: Simplified Technical English specification
- **ATA iSpec 2200**: Air Transport Association information standards
- **ISO 19880-8**: Hydrogen safety standards
- **CS-25**: EASA Certification Specifications for Large Aeroplanes

## Maintenance and Updates

- **Owner**: Technical Publications Office
- **Review Cycle**: Quarterly or with each baseline release
- **Change Control**: Follow `00-PROGRAM/CONFIG_MGMT/06-CHANGES/` procedures
- **Version**: 1.0.0
- **Last Updated**: 2025-10-10

## Support

For questions or issues:
- **Technical Publications**: tech-pubs@ampel360.eu
- **Configuration Management**: config-mgmt@ampel360.eu
- **BREX/Validation Issues**: validation@ampel360.eu

---

**Note**: This CSDB structure is compliant with S1000D Issue 6.0 and implements AMPEL360 AIR-T program-specific business rules. All Data Modules must reference the BREX DM and pass validation before release.
