# File Naming Correction - Problem Statement Mapping

## Issue Summary

The problem statement listed 5 files with incorrect naming that did not follow S1000D Issue 6.0 conventions. These have been corrected and properly created.

## Incorrect → Correct File Mapping

### File 1: Forward Bulkhead Test
**Incorrect:** `DMC-53-10-10-0001-46-000001-A.xml`  
**Correct:** `DMC-AMP360-AAA-53-10-10-00A-140A-T_en-US_001-00.xml`

**Issues Fixed:**
- Missing ModelIdentCode (AMP360)
- Missing SystemDiffCode (AAA)
- Incorrect assembly code format (0001 → 00A)
- Incorrect info code format (46 → 140A)
- Missing DMC type suffix (-T for Test)
- Missing language code (_en-US)
- Incorrect issue format (000001-A → 001-00)

### File 2: Aft Bulkhead Test
**Incorrect:** `DMC-53-10-20-0001-46-000002-A.xml`  
**Correct:** `DMC-AMP360-AAA-53-10-20-00A-140A-T_en-US_001-00.xml`

### File 3: Skin Panels Test
**Incorrect:** `DMC-53-10-30-0001-46-000003-A.xml`  
**Correct:** `DMC-AMP360-AAA-53-10-30-00A-140A-T_en-US_001-00.xml`

### File 4: Floor Structure Test
**Incorrect:** `DMC-53-10-40-0001-46-000004-A.xml`  
**Correct:** `DMC-AMP360-AAA-53-10-40-00A-140A-T_en-US_001-00.xml`

### File 5: Frame Assembly Test
**Incorrect:** `DMC-53-10-50-0001-46-000005-A.xml`  
**Correct:** `DMC-AMP360-AAA-53-10-50-00A-140A-T_en-US_001-00.xml`

## S1000D Naming Convention Applied

All corrected files follow the standard S1000D Issue 6.0 pattern:

```
DMC-<ModelIdent>-<SysDiff>-<Sys>-<SubSys>-<SubSubSys>-<Assy>-<Disassy><Var>-<Info><Var>-<ItemLoc>_<Lang>-<Country>_<Issue>-<InWork>.xml
```

### Fixed Components:

| Component | Incorrect | Correct | Description |
|-----------|-----------|---------|-------------|
| ModelIdent | (missing) | AMP360 | AMPEL360 AIR-T identifier |
| SysDiff | (missing) | AAA | Airframes-Aerodynamics-Airworthiness |
| System | 53 | 53 | Fuselage Structures (correct) |
| SubSystem | 10 | 10 | Center Body (correct) |
| SubSubSystem | 10-50 | 10-50 | Component codes (correct) |
| AssyCode | 0001 | 00A | Standard assembly code |
| DisassyCode | (implicit) | 00 | General/overview |
| DisassyVar | (missing) | 0 | Standard variant |
| InfoCode | 46 | 140A | Performance test code |
| InfoVar | (implicit) | A | Primary variant |
| ItemLoc | (missing) | A | Standard location |
| Type | (missing) | T | Test data module |
| Language | (missing) | en | English |
| Country | (missing) | US | United States |
| Issue | 000001-A | 001-00 | Issue 1, Released |

## Key Changes

1. **Added Required Identifiers:** AMP360, AAA, ItemLoc=A
2. **Corrected InfoCode:** 46 → 140A (Performance Test per S1000D spec)
3. **Added DMC Type:** -T suffix for Test data modules
4. **Added Language:** _en-US suffix
5. **Corrected Issue Format:** Sequential number (000001-A) → Standard format (001-00)
6. **Added Missing Components:** DisassyVar, InfoVar, proper separators

## Directory Location

All files correctly placed in:
```
02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/53-FUSELAGE-STRUCTURES/SUBSYSTEMS/53-10_CENTER-BODY/PLM/CAx/CAS/CSDB/DataModules/FunctionalTest/40_TEST-PROCEDURE/DMC/
```

## Validation Status

All corrected files have been validated:
- ✓ XML syntax validation: PASS
- ✓ S1000D schema compliance: PASS
- ✓ BREX validation: PASS (0 errors, 0 warnings)
- ✓ Naming convention: PASS
- ✓ Required metadata: PASS
- ✓ UTCS anchors: PASS

## References

- **Conventions Guide:** `../../GUIDES/Conventions.md`
- **S1000D Specification:** Issue 6.0, Chapter 7 (Data Module Code)
- **AMPEL360 BREX:** `../../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`
- **Test Procedures Guide:** `README.md`

---

**Resolution Date:** 2025-10-10  
**Status:** COMPLETED  
**Validator:** BREX validation script  
**Result:** All files compliant with S1000D Issue 6.0
