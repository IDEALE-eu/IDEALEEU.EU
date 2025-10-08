# Unique Identifier (UID) Strategy

## Overview

This document defines the unique identifier conventions for the Digital Thread, ensuring consistent identification and traceability across all systems and lifecycle phases.

## Principles

1. **Uniqueness**: Each UID is globally unique within the program
2. **Persistence**: UIDs are immutable once assigned
3. **Semanticity**: UIDs contain meaningful structure (human-readable)
4. **Traceability**: UIDs enable end-to-end lifecycle tracking
5. **Standards Compliance**: Aligned with AIA ALS-001, ISO 10303, ECSS-M-ST-40

## UID Formats

### Product UIDs

**Aircraft**
- Format: `ACFT-<SERIAL>-<TYPE>`
- Serial: 3-digit sequential number
- Type: Aircraft configuration designator
- Example: `ACFT-001-H2` (First hydrogen-powered aircraft)

**Spacecraft**
- Format: `SC-<SERIAL>-<MISSION>`
- Serial: 3-digit sequential number
- Mission: Mission designator
- Example: `SC-001-DEMO` (First demo mission spacecraft)

**Subsystems**
- Format: `<PRODUCT>-<SUBSYSTEM>-<SERIAL>`
- Product: Parent product UID
- Subsystem: 2-3 letter subsystem code
- Serial: 3-digit sequential number
- Example: `ACFT-001-GNC-001` (GNC subsystem of aircraft 001)

### Part UIDs

**Format**: `<PART_NUMBER>-<SERIAL>-<LOT>`

Components:
- Part Number: 6-10 alphanumeric (manufacturer part number)
- Serial: 3-digit serialization (if serialized part)
- Lot: Manufacturing lot identifier (optional)

Examples:
- `P123456-001-LOT2024-03` (Serialized part from lot)
- `P789ABC-012` (Serialized part, no lot tracking)
- `M456XYZ` (Non-serialized part, no serial or lot)

**Serialization Criteria**:
- Flight-safety critical parts: Always serialized
- High-value parts (>$10k): Always serialized
- Repairable/serviceable parts: Always serialized
- Consumables/low-cost: Non-serialized

### Document UIDs

**Format**: `<DOCTYPE>-<ID>-<VERSION>`

Components:
- DOCTYPE: Document type (3-6 letter code)
- ID: Sequential identifier within type
- Version: Semantic version (V<major>.<minor>)

Document Type Codes:
- `SPEC`: Specification
- `DWG`: Drawing
- `REQ`: Requirement
- `PROC`: Procedure
- `TEST`: Test Procedure/Report
- `ANAL`: Analysis
- `ICD`: Interface Control Document

Examples:
- `SPEC-001234-V2.1` (Specification, version 2.1)
- `DWG-789456-V1.0` (Drawing, version 1.0)
- `ICD-AVIONICS-GNC-V1.2` (ICD between avionics and GNC)

### Event UIDs

**Format**: `<EVENT_TYPE>-<TIMESTAMP>-<SEQUENCE>`

Components:
- EVENT_TYPE: Type of event (4-6 letters)
- TIMESTAMP: ISO 8601 datetime (YYYYMMDDTHHmmSS)
- SEQUENCE: 3-digit sequence (for events in same second)

Event Type Codes:
- `TEST`: Test event
- `MAINT`: Maintenance event
- `ANOM`: Anomaly
- `CHANGE`: Design or configuration change
- `INSP`: Inspection
- `FAIL`: Failure event

Examples:
- `TEST-20250315T143000-001` (Test on 2025-03-15 at 14:30:00)
- `MAINT-20250420T090000-001` (Maintenance event)
- `ANOM-20250505T173045-002` (Anomaly, second event that second)

### Requirement UIDs

**Format**: `<LEVEL>-REQ-<ID>`

Components:
- LEVEL: Requirement level (SYS, SUB, COMP, IF)
- ID: Sequential identifier within level

Requirement Levels:
- `SYS`: System-level requirement
- `SUB`: Subsystem-level requirement
- `COMP`: Component-level requirement
- `IF`: Interface requirement

Examples:
- `SYS-REQ-001` (System requirement 1)
- `SUB-REQ-123` (Subsystem requirement 123)
- `IF-REQ-045` (Interface requirement 45)

### Process UIDs

**Format**: `PROC-<TYPE>-<ID>`

Components:
- TYPE: Process type (3-6 letters)
- ID: Sequential identifier

Process Types:
- `MFG`: Manufacturing
- `ASSY`: Assembly
- `TEST`: Testing
- `INSP`: Inspection
- `AIT`: Assembly, Integration, Test (spacecraft)

Examples:
- `PROC-MFG001-001` (Manufacturing process)
- `PROC-AIT005-003` (Spacecraft AIT process)

## UID Assignment Authority

### Centralized Assignment
- **Product UIDs**: Program configuration management
- **Part UIDs**: PLM system (automatic assignment)
- **Document UIDs**: Document management system
- **Event UIDs**: Event logging system (automatic timestamp-based)

### Assignment Rules
- UIDs assigned at creation time
- UIDs never reused (even for deleted/obsolete items)
- UIDs never modified (immutable)
- UID conflicts detected and prevented by system

## Traceability Links

### Link Format
UIDs are used in traceability relationships:
- **Parent-Child**: `ACFT-001` → `ACFT-001-GNC-001`
- **Part-Document**: `P123456-001` ← `SPEC-001234-V2.1`
- **Requirement-Design**: `SYS-REQ-001` → `ACFT-001-GNC-001`
- **Part-Event**: `P123456-001` ← `TEST-20250315T143000-001`

### Traceability Database
- Graph database stores UID relationships
- Bi-directional traceability queries
- Audit trail of relationship creation/modification

## Barcode and RFID

### Physical Marking
Serialized parts marked with:
- Human-readable UID (laser-etched, stamped)
- 2D barcode (Data Matrix, QR Code)
- RFID tag (for high-value, trackable parts)

### Encoding Standards
- Data Matrix: ISO/IEC 16022
- QR Code: ISO/IEC 18004
- RFID: ISO/IEC 18000-6C (EPC Gen2)

### Barcode Content
Encoded data includes:
- Part UID
- Part number
- Serial number
- Lot number (if applicable)
- ITAR/EAR flag (if controlled)

## AIA ALS-001 Compliance

### Alignment
This UID strategy aligns with AIA ALS-001 (Aerospace Logistics Standard):
- Unique identification of serialized items
- As-maintained configuration tracking
- Logistics data exchange
- MRO integration

### ALS-001 Data Elements
Supported ALS-001 data elements:
- Manufacturer
- Part Number
- Serial Number
- Configuration
- Effectivity
- Maintenance actions

## ECSS-M-ST-40 Compliance

### Configuration Identification
Per ECSS-M-ST-40:
- Configuration items (CIs) identified by UIDs
- Baselines include UID snapshots
- Change control tracks UID relationships
- Configuration status accounting (CSA) by UID

## ITAR/EAR Handling

### Controlled Data Tagging
UIDs for controlled technical data include metadata:
- ITAR_Controlled: true/false
- EAR_Controlled: true/false
- Export_Classification: USML category or ECCN

### Access Control
- UID metadata triggers access control checks
- Export compliance verified before data exchange
- Audit trail of access to controlled UIDs

## Migration from Legacy Systems

### Legacy UID Mapping
For parts/documents from legacy systems:
- Maintain legacy identifier as attribute
- Create new UID per this strategy
- Cross-reference table: Legacy ID ↔ New UID

### Transition Period
- Dual-identifier support during migration
- Legacy IDs deprecated after transition (12 months)
- All new items use new UID convention

## UID Quality and Validation

### Validation Rules
Automated validation of UIDs:
- Format compliance (regex patterns)
- Uniqueness check (no duplicates)
- Referential integrity (linked UIDs exist)
- Immutability enforcement (no changes to assigned UIDs)

### Error Handling
- UID format errors: Rejected at creation
- UID conflicts: Auto-generate alternate UID
- Broken links: Flagged for manual resolution

## Alignment with CONFIG_MGMT

This UID strategy is aligned with:
- **CONFIG_MGMT/03-SERIALIZATION.md**: Serialization rules
- **CONFIG_MGMT/04-BASELINES/**: Baseline identification
- **CONFIG_MGMT/09-INTERFACES/**: Interface identification

Cross-reference: Configuration items in CONFIG_MGMT use the same UID conventions defined here.

## Conclusion

This UID strategy provides a comprehensive, standards-compliant approach to unique identification across the Digital Thread lifecycle. Consistent application of these conventions enables robust traceability, configuration management, and compliance with aerospace standards.
