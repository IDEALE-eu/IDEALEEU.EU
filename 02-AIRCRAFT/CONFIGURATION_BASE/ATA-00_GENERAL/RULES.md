# Configuration Management Rules

This document defines the core rules governing the organization and management of aircraft configuration data within the CONFIGURATION_BASE structure.

## Overview

These rules ensure consistency, traceability, and compliance across all ATA chapters and system configurations.

## Core Principles

### 1. Single Source of Truth
Each configuration item has exactly one authoritative location in the structure.

### 2. Immutable Baselines
Approved baselines cannot be modified; changes create new baseline versions.

### 3. Complete Traceability
Every configuration item must be traceable to requirements, ICDs, and change records.

---

## Primary Configuration Rules

### Rule 1: LRU Primary Location

**Statement**: Line Replaceable Units (LRUs) reside in their primary ATA chapter based on functional classification.

**Rationale**: Ensures clear ownership and prevents duplication of hardware configuration data.

**Implementation**:
- LRU hardware configuration goes in the ATA chapter corresponding to its primary function
- Example: Flight Control Computer (FCC) → ATA-27_FLIGHT_CONTROLS
- Example: Air Data Computer (ADC) → ATA-34_NAVIGATION
- Cross-references allowed via ICD/ directories

**Exceptions**:
- IMA modules and chassis → ATA-42_INTEGRATED_MODULAR_AVIONICS
- Network switches and routers → ATA-42 (when part of IMA infrastructure)

### Rule 2: Software Placement with Host LRU

**Statement**: Software resides with its host Line Replaceable Unit.

**Rationale**: Maintains software-hardware coupling and simplifies configuration management.

**Implementation**:
- Software baselines stored in SW_BASELINE/ of the host LRU's ATA chapter
- Software part numbers and versions documented with hardware configuration
- Example: FCC application software → ATA-27_FLIGHT_CONTROLS/SW_BASELINE/
- Example: IMA partition software → ATA-42/SW_BASELINE/ (with partition mapping)

**Special Cases**:
- **IMA Hosted Applications**: Software resides in ATA-42/SW_BASELINE/ with explicit partition bindings
- **Shared Libraries**: Document in host system chapter with references in dependent chapters
- **FADEC Software**: Resides in ATA-76_ENGINE_CONTROLS/SW_BASELINE/

### Rule 3: EWIS Centralization

**Statement**: ALL Electrical Wiring Interconnection System (EWIS) configurations reside ONLY in ATA-92_EWIS.

**Rationale**: Regulatory compliance (FAA/EASA EWIS requirements) and centralized wire management.

**Implementation**:
- Wire specifications, routing, and installation → ATA-92_EWIS
- Harness definitions and assemblies → ATA-92_EWIS/BASELINE/
- Connector and splice configurations → ATA-92_EWIS/HW_CONFIG/
- Zone wire lists → ATA-92_EWIS/PARAMS/
- Shielding and grounding specifications → ATA-92_EWIS/PARAMS/

**Prohibited**:
- ❌ Wire routing in system ATA chapters (e.g., ATA-27)
- ❌ Harness definitions outside ATA-92
- ❌ Connector pinouts in LRU chapters (reference only)

**Allowed**:
- ✓ LRU connector types and part numbers in system chapters (without pinouts)
- ✓ References to ATA-92 for detailed wiring
- ✓ Interface signal definitions in system ICD/ directories

### Rule 4: Change Control Requirement

**Statement**: All configuration changes require formal Engineering Change Request (ECR) and Engineering Change Order (ECO) through the Configuration Control Board (CCB).

**Implementation**:
- Submit ECR to CCB for approval
- Upon approval, ECO issued
- Changes documented in CHANGE_LOG/
- Traceability maintained to ECR/ECO numbers
- Baseline updates at appropriate gates

**Emergency Changes**:
- Follow expedited CCB process
- Document emergency approval
- Retroactive ECR/ECO within 48 hours

### Rule 5: Baseline Immutability

**Statement**: Approved baselines are immutable; modifications create new baseline versions.

**Implementation**:
- Baseline directories frozen at gate approval
- New changes create new baseline version
- Version numbers follow semantic versioning
- SHA-256 hashes verify baseline integrity
- Historical baselines preserved

---

## Data Organization Rules

### Rule 6: Standard Directory Structure

**Statement**: Each ATA chapter uses the standard 7-directory structure.

**Required Directories**:
1. `PARAMS/` - Parameters and limits
2. `BASELINE/` - Configuration baselines
3. `HW_CONFIG/` - Hardware configuration
4. `SW_BASELINE/` - Software baselines
5. `ICD/` - Interface control documents
6. `VERIFICATION/` - V&V artifacts
7. `CHANGE_LOG/` - Change history

**Optional**: Additional subdirectories allowed with CCB approval.

### Rule 7: File Naming Conventions

**Statement**: Files follow standardized naming conventions for consistency.

**Conventions**:
- `UPPERCASE_WITH_UNDERSCORES.extension`
- Parameters: `[PARAMETER_NAME].csv` or `[PARAMETER_NAME].json`
- Baselines: `BASELINE_[VERSION]_[GATE].csv`
- ICDs: `ICD_[SYSTEM1]_TO_[SYSTEM2]_[VERSION].pdf`
- Change logs: `CHANGE_LOG_[YYYY].csv`

**Examples**:
- `H2_STORAGE_PRESSURE.csv`
- `BASELINE_V1.0_PDR.csv`
- `ICD_FCC_TO_FADEC_V2.1.pdf`
- `CHANGE_LOG_2024.csv`

### Rule 8: Version Control

**Statement**: All configuration items are under version control with appropriate branching strategy.

**Implementation**:
- Main branch: Approved baselines only
- Feature branches: Development and ECR work
- Release tags: Gate baselines (SRR, PDR, CDR, etc.)
- Commit messages reference ECR/ECO numbers

---

## Cross-Chapter Rules

### Rule 9: Interface Management

**Statement**: Interfaces between systems documented in both system chapters with primary ownership.

**Implementation**:
- Primary ICD in the "providing" system chapter
- Reference ICD in the "consuming" system chapter
- Cross-references maintained in ICD/ directories
- Interface changes require approval from both system owners

**Example**:
- FCC provides data to FADEC
- Primary ICD: ATA-27_FLIGHT_CONTROLS/ICD/ICD_FCC_TO_FADEC.pdf
- Reference: ATA-76_ENGINE_CONTROLS/ICD/REFS/ICD_FCC_TO_FADEC_REF.md

### Rule 10: Shared Components

**Statement**: Components used across multiple systems documented once with cross-references.

**Implementation**:
- Component in primary functional ATA chapter
- Cross-reference documents in other chapters
- Part number mapping in Item Master
- Configuration controlled through primary chapter

---

## Special System Rules

### Rule 11: IMA Partition Management

**Statement**: IMA partitions and hosted applications follow ARINC 653 configuration standards.

**Implementation**:
- Module and chassis configuration → ATA-42/HW_CONFIG/
- Partition definitions → ATA-42/PARAMS/PARTITION_MAP.csv
- Hosted application binaries → ATA-42/SW_BASELINE/
- Application-to-partition binding documented
- CPU% and memory allocations specified

**Cross-References**:
- Application functional requirements in host system chapter
- Partition safety/security requirements in ATA-42

### Rule 12: H2 Fuel System Configuration

**Statement**: Hydrogen fuel systems follow special safety and certification requirements.

**Implementation**:
- H2 storage and distribution → ATA-28_FUEL/
- Cryogenic temperature limits → ATA-28/PARAMS/CRYO_TEMP_LIMITS.csv
- Pressure specifications → ATA-28/PARAMS/H2_STORAGE_PRESSURE.csv
- Safety parameters and limits clearly documented
- Leak detection system configuration included

### Rule 13: FADEC and Engine Control

**Statement**: Full Authority Digital Engine Control (FADEC) configuration resides in engine control chapter.

**Implementation**:
- FADEC hardware → ATA-76_ENGINE_CONTROLS/HW_CONFIG/
- FADEC software → ATA-76/SW_BASELINE/
- Engine interface → ATA-76/ICD/
- Fuel control parameters → ATA-73_ENGINE_FUEL_CONTROL/PARAMS/

---

## Data Quality Rules

### Rule 14: Schema Compliance

**Statement**: All structured data files must validate against their defined schemas.

**Implementation**:
- JSON files: Validate against JSON Schema in ATA-00_GENERAL/SCHEMAS/
- XML files: Validate against XSD in ATA-00_GENERAL/SCHEMAS/
- CSV files: Validate headers and required columns
- YAML files: Validate against YAML schema where applicable

**Tools**:
- `jsonschema` for JSON validation
- `xmllint` for XML validation
- `csvlint` for CSV validation
- Custom validators for domain-specific formats

### Rule 15: Completeness Requirements

**Statement**: Configuration items must be complete with all required attributes.

**Required Attributes**:
- Part Number (PN)
- Version/Revision
- Description
- Owner/Responsible Engineer
- Status (Draft/Approved/Obsolete)
- Creation Date
- Approval Date (if applicable)
- ECR/ECO reference (for changes)

### Rule 16: Traceability Links

**Statement**: Every configuration item must have traceability links to requirements and upstream/downstream items.

**Implementation**:
- Requirements ID links mandatory
- Interface dependencies documented
- Parent/child relationships specified
- Impact analysis for changes
- Links maintained in 00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/

---

## Verification and Validation Rules

### Rule 17: V&V Documentation

**Statement**: All configurations require appropriate verification and validation evidence.

**Requirements**:
- Test plans for hardware configurations
- Test results for software baselines
- Compliance evidence for regulatory items
- Installation verification procedures
- Integration test results

**Storage**:
- V&V artifacts → [ATA]/VERIFICATION/
- Gate evidence → CONFIG_MGMT/04-BASELINES/[GATE]/ARTIFACTS/EVIDENCE/

### Rule 18: Safety-Critical Items

**Statement**: Safety-critical configurations require additional rigor and approval.

**Additional Requirements**:
- Independent review required
- Safety assessment documented
- Failure modes analyzed (FMEA/FTA)
- Redundancy and backup configurations specified
- Special handling in change control process

---

## Maintenance and Audit Rules

### Rule 19: Regular Audits

**Statement**: Configuration audits conducted at defined intervals and gates.

**Audit Types**:
- **Physical Configuration Audit (PCA)**: Verify as-built matches configuration
- **Functional Configuration Audit (FCA)**: Verify performance against requirements
- **Baseline Audit**: Verify baseline integrity and traceability

**Frequency**:
- Quarterly internal reviews
- Gate audits (SRR, PDR, CDR, etc.)
- Annual comprehensive audit

### Rule 20: Change Log Maintenance

**Statement**: All configuration changes must be logged with complete information.

**Required Information**:
- Change date
- ECR/ECO number
- Description of change
- Affected items and baselines
- Approver
- Implementation status
- Verification status

**Format**:
- CSV format: CHANGE_LOG/CHANGE_LOG_[YYYY].csv
- Aggregated in ATA-00_GENERAL/GLOBAL_CHANGE_LOG.csv

---

## Compliance and Standards

### Rule 21: Standards Compliance

**Statement**: Configurations comply with applicable industry and regulatory standards.

**Applicable Standards**:
- ATA iSpec 2200 (system organization)
- ARINC standards (429, 664, 653, etc.)
- DO-178C (software)
- DO-254 (hardware)
- DO-160 (environmental)
- FAA/EASA EWIS requirements
- SAE AS standards

### Rule 22: Security Requirements

**Statement**: Configuration data classified and protected according to security policies.

**Classification Levels**:
- Public: General system descriptions
- Internal: Detailed configurations
- Confidential: Proprietary designs
- Restricted: Security-critical items

**Protection**:
- Access controls on repositories
- Encryption for sensitive data
- Export control compliance
- Watermarking for controlled documents

---

## Exceptions and Waivers

### Rule 23: Exception Process

**Statement**: Exceptions to these rules require formal waiver approved by CCB.

**Waiver Process**:
1. Submit waiver request with justification
2. Impact assessment by Configuration Management
3. CCB review and approval
4. Document waiver with expiration date
5. Review at expiration

**Documentation**:
- Waiver stored in CONFIG_MGMT/06-CHANGES/WAIVERS/
- Reference in affected configuration items

---

## Enforcement

These rules are enforced through:
- CI/CD quality gates
- Automated validation scripts
- Manual configuration audits
- CCB review process
- Training and awareness programs

Non-compliance may result in:
- Blocked pull requests
- ECR/ECO rejection
- Baseline rejection
- Corrective action requirements

---

## References

- [Configuration Management Plan](../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
- [Change Process](../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- [Baseline Process](../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/00-README.md)
- [CI/CD Quality Gates](../../../00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/GATES.md)

---

**Document Control**
- **Version**: 1.0
- **Effective Date**: 2024
- **Owner**: Configuration Management
- **Review**: Annually and at each program gate
