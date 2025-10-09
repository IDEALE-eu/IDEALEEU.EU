# Change Rules - CABINS_CARGO_PAX Domain

## Purpose

This document defines the change control rules and processes for the CABINS_CARGO_PAX domain integration.

## Change Classification

### Class 1: Major Changes (CCB Approval Required)

Require Configuration Control Board (CCB) approval:

1. **Architecture Changes**
   - New system interfaces
   - Changes to domain boundaries
   - Major integration approach changes

2. **Safety-Critical Changes**
   - Emergency equipment modifications
   - Structural attachment changes
   - Fire protection system changes
   - Cargo restraint modifications

3. **Cross-Domain Interfaces**
   - Changes affecting ATA-21 (ECS)
   - Changes affecting ATA-24 (Electrical)
   - Changes affecting ATA-26 (Fire)
   - Changes affecting ATA-38 (Water/Waste)

4. **Baseline Changes**
   - Configuration baseline updates
   - Gate-level configuration changes
   - Release baseline modifications

### Class 2: Minor Changes (Domain Owner Approval)

Require Domain Owner approval only:

1. **System-Level Changes**
   - Within-system modifications
   - Non-critical component changes
   - Process improvements

2. **Documentation Updates**
   - Non-architecture documentation
   - Template refinements
   - Metric definitions

3. **Internal Interfaces**
   - Changes within subsystems
   - PLM workflow updates
   - Report format changes

### Class 3: Administrative Changes (Direct Implementation)

No formal approval required:

1. Formatting corrections
2. Typographical fixes
3. Link updates
4. Date updates
5. Contact information changes

## Change Process

### Class 1 Changes

```
1. Change Request Initiation
   ↓
2. Impact Analysis (Systems Integration)
   ↓
3. Safety Assessment (if applicable)
   ↓
4. CCB Review Package Preparation
   ↓
5. CCB Meeting and Approval
   ↓
6. Implementation Planning
   ↓
7. Execution and Verification
   ↓
8. Baseline Update
   ↓
9. Stakeholder Notification
```

### Class 2 Changes

```
1. Change Request
   ↓
2. Domain Owner Review
   ↓
3. Approval/Rejection
   ↓
4. Implementation
   ↓
5. Documentation Update
   ↓
6. Notification to CM
```

### Class 3 Changes

```
1. Identify Issue
   ↓
2. Make Correction
   ↓
3. Update Change Log
```

## Impact Analysis Requirements

All Class 1 and Class 2 changes require impact analysis covering:

1. **Technical Impact**
   - Affected systems and interfaces
   - Design modifications required
   - Testing and verification needs

2. **Schedule Impact**
   - Implementation timeline
   - Dependencies and critical path
   - Milestone impacts

3. **Cost Impact**
   - Engineering effort
   - Hardware/software changes
   - Testing and certification costs

4. **Safety Impact**
   - Safety assessment needs
   - Certification impact
   - Risk assessment

5. **Documentation Impact**
   - Affected documents
   - Update requirements
   - Training needs

## Interface Change Control

### Internal Interfaces (within domain)

- ATA-25 ↔ ATA-44: Domain Owner approval
- ATA-25 ↔ ATA-50: Domain Owner approval
- ATA-44 ↔ ATA-50: Domain Owner approval

### External Interfaces (cross-domain)

Changes to interfaces with systems outside this domain require:

1. Interface Change Notice (ICN)
2. Both domain owners' approval
3. Systems Integration review
4. CCB approval for critical interfaces
5. Update to Interface Management database

## PLM Change Control

### CAD Model Changes

1. Check-out from PLM system
2. Design modification
3. Design review (as per change class)
4. Check-in with revision notes
5. Export neutral files (STEP, JT, QIF)
6. Update metadata

### Integration View Changes

1. Master assembly modifications
2. Layout updates
3. Neutral exports regeneration
4. Integration report updates
5. Stakeholder review

## Traceability Requirements

All changes must be traceable:

1. **Forward Traceability**
   - Requirements to design
   - Design to implementation
   - Implementation to verification

2. **Backward Traceability**
   - Test results to requirements
   - Configuration to baseline
   - Changes to change requests

## Change Documentation

### Required Documentation

1. **Change Request Form**
   - Description of change
   - Justification and rationale
   - Impact analysis summary
   - Proposed implementation

2. **Approval Records**
   - Approval authority
   - Approval date
   - Conditions or restrictions

3. **Implementation Records**
   - What was changed
   - When it was changed
   - Who made the change
   - Verification results

4. **Baseline Updates**
   - Updated configuration items
   - New baseline version
   - Change log entries

## Change Review Meetings

### CCB Meetings

- **Frequency**: Bi-weekly or as needed
- **Attendees**: Domain Owner, Systems Integration, CM, Safety, Certification
- **Agenda**: Pending Class 1 changes, impacts, decisions

### Domain Review Meetings

- **Frequency**: Weekly
- **Attendees**: Domain Owner, ATA Owners, Systems Integration
- **Agenda**: Class 2 changes, ongoing issues, metrics

## Emergency Changes

In case of critical safety or operational issues:

1. Domain Owner can authorize immediate change
2. CCB notification within 24 hours
3. Formal change request within 48 hours
4. Retroactive CCB approval at next meeting
5. Full documentation within 1 week

## Metrics and Reporting

Track and report:

1. Number of changes by class
2. Change approval cycle time
3. Change rejection rate
4. Impact on schedule and cost
5. Rework due to inadequate change control

## References

- [Configuration Rules](../../../CONFIGURATION_BASE/00-COMMON/RULES.md)
- [Interface Management Process](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [CCB Charter](../../../../00-PROGRAM/CONFIG_MGMT/)

## Contacts

- **CCB Chair**: Program Configuration Manager
- **Domain Owner**: Cabin & Cargo Engineering Lead
- **Systems Integration**: Integration Team Lead

---

**Last Updated**: 2025-01-15
