# BREX - Business Rules Exchange

## Overview

This directory contains BREX (Business Rules Exchange) Data Modules that define validation rules for AMPEL360 AIR-T S1000D content.

BREX files specify business rules that Data Modules must comply with beyond the standard S1000D schema validation.

## BREX Files

### AMP360 BREX (English)

**File**: `DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`

**Purpose**: Primary BREX for AMPEL360 AIR-T project
- **Language**: English (en-US)
- **Model Identifier**: AMP360
- **Domain**: AAA (Airframes-Aerodynamics-Airworthiness)
- **Rules**: 120 validation rules covering:
  - IDS & Metadata (20 rules)
  - DMC & Ownership (10 rules)
  - Language & Localization (10 rules)
  - Security & QA (10 rules)
  - Applicability & ACT (10 rules)
  - Procedural Structure (15 rules)
  - Fault Isolation (10 rules)
  - Illustrations & Graphics (10 rules)
  - IPD & Logistics (10 rules)
  - References & Linking (5 rules)
  - Controlled Language & Domain Safety (10 rules)

**Validation Requirements**:
- `modelIdentCode` must be "AMP360"
- `systemDiffCode` must be "AAA"
- Language must be "en-US"

**Index**: See `AMP360-AIR-T_BREX_120rules_index.csv` for complete rule listing

### Q100 BREX (Spanish)

**File**: `DMC-Q100-BREX-AAA-STRUCTURES-00-00-0-0-000-A-A_es-ES_001-00.xml`

**Purpose**: BREX for Q100 version-specific modules
- **Language**: Spanish (es-ES)
- **Model Identifier**: Q100
- **Domain**: AAA-STRUCTURES (Airframes domain, Structures focus)
- **Rules**: Subset of validation rules specific to Q100 family
  - Identification and Metadata
  - DMC Coding for Q100
  - Language and Localization (Spanish)
  - Applicability and Configuration
  - BREX References
  - Content and Text
  - Structures Domain Specific (ATA 53)

**Validation Requirements**:
- `modelIdentCode` must be "Q100" or "AMP360"
- `systemCode` for structures typically "53" (Fuselage)
- Language recommended as "es-ES" for Q100 modules
- Specific rules for system 53 (Fuselage Structures)

## Usage

### Referencing BREX in Data Modules

Data Modules should reference the appropriate BREX file:

#### AMP360 Data Modules
```xml
<brexDmRef>
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="AMP360" 
              systemDiffCode="AAA"
              systemCode="00" 
              subSystemCode="00" 
              subSubSystemCode="00"
              assyCode="00A" 
              disassyCode="00" 
              disassyCodeVariant="0"
              infoCode="000A" 
              infoCodeVariant="A" 
              itemLocationCode="A"/>
    </dmRefIdent>
  </dmRef>
</brexDmRef>
```

#### Q100 Data Modules
```xml
<brexDmRef>
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="Q100" 
              systemDiffCode="BREX"
              systemCode="AAA" 
              subSystemCode="STRUCTURES" 
              subSubSystemCode="00"
              assyCode="00" 
              disassyCode="0" 
              disassyCodeVariant="0"
              infoCode="000" 
              infoCodeVariant="A" 
              itemLocationCode="A"/>
    </dmRefIdent>
  </dmRef>
</brexDmRef>
```

### Validating Against BREX

Use the validation script to check Data Modules against BREX rules:

```bash
# Validate a single DM
python ../../VALIDATION/BREX/validate_brex.py \
  ../DataModules/Descriptive/00_GENERAL/DMC-xxx.xml

# Validate with specific BREX file
python ../../VALIDATION/BREX/validate_brex.py \
  --brex DMC-Q100-BREX-AAA-STRUCTURES-00-00-0-0-000-A-A_es-ES_001-00.xml \
  ../DataModules/Descriptive/00_GENERAL/DMC-Q100-xxx.xml

# Validate entire directory
python ../../VALIDATION/BREX/validate_brex.py ../DataModules/
```

## BREX Rule Severity Levels

- **ERROR**: Must be fixed before release (inWork=00)
- **WARN**: Should be addressed but does not block release

## Version-Specific Considerations

### AMP360 vs Q100

| Aspect | AMP360 | Q100 |
|--------|--------|------|
| **Model Identifier** | AMP360 | Q100 |
| **Language** | en-US | es-ES |
| **Domain Code** | AAA | 53 or AAA |
| **Use Case** | General project documentation | Version/family-specific content |
| **BREX Strictness** | Comprehensive (120 rules) | Focused subset |

Both BREX files are valid S1000D Business Rules Exchange modules and serve different documentation needs within the AMPEL360 AIR-T program.

## Related Documentation

- **Validation Guide**: `../../VALIDATION/README.md`
- **Conventions**: `../../GUIDES/Conventions.md`
- **Data Modules**: `../DataModules/README.md`
- **Q100 Documentation**: `../DataModules/Descriptive/00_GENERAL/DMC/README_Q100.md`

## S1000D Compliance

Both BREX files follow:
- **S1000D Issue 5.x/6.0** specification
- **Chapter 7**: Business Rules Exchange format
- **XPath 1.0**: For rule expressions
- **XML Schema**: S1000D 6.0 namespace

## Maintenance

BREX files should be updated when:
- New validation requirements are identified
- Project standards evolve
- Domain-specific rules need refinement
- Language variants require specific rules

All BREX changes must be reviewed and approved by the configuration management team.

---

**Status**: Configuration-controlled  
**Authority**: AMPEL360 AIR-T Configuration Management  
**Last Updated**: 2025-10-15
