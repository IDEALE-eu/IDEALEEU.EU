# Links to Configuration Management

## Purpose

This document provides relative path links to the central Configuration Management (CM) structure for the Q100 version.

## Configuration Management Structure

The Configuration Management files are located at:
`00-PROGRAM/CONFIG_MGMT/`

## Relative Paths from Q100 Version

From the Q100 version directory:
```
02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/
```

To Configuration Management (relative path):
```
../../../../../../../00-PROGRAM/CONFIG_MGMT/
```

## Key CM References

### 1. Configuration Management Plan
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`  
**Purpose:** Overall CM strategy and processes

### 2. Part Numbering
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md`  
**Purpose:** Part numbering scheme and allocation

### 3. Serialization
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/03-SERIALIZATION.md`  
**Purpose:** Serial number allocation and tracking

### 4. Baselines
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/`  
**Purpose:** Configuration baselines and releases
- Integration Baselines (IBL-*)
- Product Baselines (PBL-*)
- Functional Baselines (FBL-*)

### 5. Configuration Control Board (CCB)
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/05-CCB/`  
**Purpose:** Change control and decision records
- CCB Charter
- Meeting minutes
- Decision logs

### 6. Change Management
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/`  
**Purpose:** Engineering change process
- Engineering Change Notices (ECN)
- Change Requests (CR)
- Deviation/Waiver process

### 7. Releases
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/`  
**Purpose:** Release management and versioning
- Release policy
- Version scheme (SemVer + Build metadata)
- Release notes

### 8. Item Master
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/`  
**Purpose:** Master data for configuration items
- Bills of Material (BOM)
- Part specifications
- Supplier information

### 9. Interface Control Documents (ICDs)
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`  
**Purpose:** Interface specifications between systems
- See also: `../04-ICD_LINKS/ICD_INDEX.md` (this version)

### 10. Traceability
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/`  
**Purpose:** Requirements to design to verification traceability
- Requirements database
- Verification matrix
- Validation evidence

### 11. Audits
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/11-AUDITS/`  
**Purpose:** Configuration audits
- Physical Configuration Audit (PCA)
- Functional Configuration Audit (FCA)
- Audit reports

### 12. CI/CD Rules
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/`  
**Purpose:** Continuous integration and deployment
- Build automation
- Test automation
- Deployment processes

### 13. Templates
**Path:** `../../../../../../../00-PROGRAM/CONFIG_MGMT/13-TEMPLATES/`  
**Purpose:** Standard templates for CM documents
- ECN template
- CCB decision template
- Baseline release template

## Version-Specific CM Files

### Configuration (This Version)
**Path:** `./00-CONFIG/`  
**Contents:**
- Configuration rules (RULES.md)
- Configuration schemas (SCHEMAS/)
- Configuration sets (CONFIG_SETS/)

### Effectivity (This Version)
**Path:** `./01-EFFECTIVITY/`  
**Contents:**
- MSN effectivity mapping (MSN_EFFECTIVITY.csv)
- Serial blocks (BLOCKS/)
- Modifications (MODS/)

### Release Tags (This Version)
**Path:** `./02-RELEASE_TAGS/`  
**Contents:**
- Integration Baseline tags
- Release documentation

### Traceability (This Version)
**Path:** `./03-TRACEABILITY/`  
**Contents:**
- Configuration to requirements mapping
- This document (links to central CM)

### ICD Links (This Version)
**Path:** `./04-ICD_LINKS/`  
**Contents:**
- ICD index for this version
- Links to interface specifications

## Usage Examples

### Example 1: Submit an Engineering Change
1. Prepare ECN using template from `../../../../../../../00-PROGRAM/CONFIG_MGMT/13-TEMPLATES/`
2. Submit to CCB via process in `../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/`
3. If approved, update version-specific files:
   - Configuration: `./00-CONFIG/CONFIG_SETS/`
   - Effectivity: `./01-EFFECTIVITY/MSN_EFFECTIVITY.csv`
   - Traceability: `./03-TRACEABILITY/CONFIG_TO_REQ_MAP.md`

### Example 2: Release New Configuration
1. Follow release process in `../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/`
2. Update baseline in `../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
3. Create release tag in `./02-RELEASE_TAGS/`
4. Update version scheme per `../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/01-POLICY/VERSIONING_SCHEME.md`

### Example 3: Trace Requirement to Configuration
1. Start with requirement in `../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/`
2. Follow mapping in `./03-TRACEABILITY/CONFIG_TO_REQ_MAP.md`
3. Locate configuration in `./00-CONFIG/CONFIG_SETS/`
4. Check effectivity in `./01-EFFECTIVITY/MSN_EFFECTIVITY.csv`

### Example 4: Verify Interface Specification
1. Identify interface from system INTERFACE_MATRIX (e.g., `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/INTERFACE_MATRIX/`)
2. Look up ICD in `./04-ICD_LINKS/ICD_INDEX.md`
3. Access detailed ICD in `../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

## Document Control

- **Version:** 1.0.0
- **Last Updated:** 2025-03-31
- **Owner:** Configuration Management Office
- **Review Cycle:** With each baseline release

## Navigation Helper

To navigate from Q100 version to program-level CM:
```bash
cd ../../../../../../../00-PROGRAM/CONFIG_MGMT/
```

To return from program-level CM to Q100 version:
```bash
cd ../../02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/
```

---

**Note:** All paths are relative to maintain repository structure independence. Always verify paths are correct for your specific repository clone location.
