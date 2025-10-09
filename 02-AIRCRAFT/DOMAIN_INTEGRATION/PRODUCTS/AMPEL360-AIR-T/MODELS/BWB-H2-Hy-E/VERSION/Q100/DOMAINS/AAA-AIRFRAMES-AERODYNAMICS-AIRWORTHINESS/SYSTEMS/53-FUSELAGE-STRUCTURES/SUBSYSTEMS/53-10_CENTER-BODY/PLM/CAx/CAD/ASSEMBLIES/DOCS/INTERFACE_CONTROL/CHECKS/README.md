# CHECKS — Interface Verification and Validation

## Purpose

This directory contains verification procedures, validation checklists, and quality checks to ensure interface requirements are met.

## Content Types

### Verification Procedures
- Inspection procedures
- Test procedures
- Analysis procedures
- Demonstration procedures

### Checklists
- Design verification checklists
- Installation checklists
- Quality inspection checklists
- As-built verification checklists

### Test Records
- Test results
- Inspection reports
- Non-conformance reports
- Corrective action records

### Analysis Reports
- Tolerance stackup analysis
- Clearance verification
- Load analysis verification
- FEA verification

## File Formats

- `.pdf` — Test procedures and reports
- `.xlsx` — Checklists and verification matrices
- `.csv` — Inspection data logs
- `.json` — Machine-readable test data

## Verification Methods

### Inspection
- Visual inspection
- Dimensional inspection
- Surface finish inspection
- Material verification

### Test
- Fit checks
- Functional tests
- Load tests
- Environmental tests

### Analysis
- Design analysis
- Tolerance analysis
- FEA validation
- Calculations review

### Demonstration
- Assembly demonstration
- Installation demonstration
- Operational demonstration

## Check Types

### Design Checks
- **Requirements verification**: All requirements addressed
- **Interface compatibility**: Mating parts compatible
- **Tolerance stackup**: Acceptable assembly variation
- **Clearance verification**: Adequate clearances maintained
- **Load path verification**: Proper load transfer
- **Material compatibility**: No adverse material interactions

### Manufacturing Checks
- **Dimensional inspection**: Parts to drawing
- **Hole pattern verification**: Pattern matches specification
- **Fastener verification**: Correct fasteners installed
- **Torque verification**: Proper torque applied
- **Surface preparation**: Surfaces properly prepared
- **Sealant application**: Sealant properly applied

### Assembly Checks
- **Fit check**: Parts mate properly
- **Gap inspection**: Gaps within tolerance
- **Alignment check**: Proper alignment achieved
- **Clearance check**: No interferences
- **Fastener installation**: Fasteners properly installed
- **Final inspection**: Complete assembly verified

### Functional Checks
- **Operational check**: Functions as required
- **Performance verification**: Meets performance specs
- **Environmental verification**: Survives environmental conditions
- **Safety verification**: Meets safety requirements

## Verification Matrix

Track verification status:
```csv
requirement_id,requirement,verification_method,procedure,status,date,verified_by
ICD-001,Wing attachment load capacity,Test,TP-53-001,Pass,2024-01-15,J.Smith
ICD-002,Fastener torque 60-70 lb-in,Inspection,IP-53-002,Pass,2024-01-15,K.Lee
ICD-003,Clearance min 5mm,Inspection,IP-53-003,Pass,2024-01-16,M.Jones
```

## Naming Convention

```
{check_type}_{interface}_{test_id}_v{version}.{ext}
```

Examples:
- `VERIF_WING-ATTACH_LOAD-TEST_v001.pdf`
- `INSP_DOOR-FRAME_DIMENSION_v002.xlsx`
- `CHECK_BULKHEAD_FIT_v001.pdf`

## Inspection Procedures

### Dimensional Inspection
1. **Preparation**
   - Calibrated instruments
   - Inspection plan
   - Environmental control

2. **Measurement**
   - Critical dimensions
   - Coordinate measurement
   - Documentation

3. **Evaluation**
   - Compare to requirements
   - Determine conformance
   - Document results

### First Article Inspection (FAI)
- Complete dimensional inspection
- Material verification
- Process verification
- Documentation package
- Customer approval (if required)

## Test Procedures

### Standard Test Format
1. **Scope and Purpose**
2. **Equipment and Instrumentation**
3. **Test Setup**
4. **Test Procedure** (step-by-step)
5. **Data Recording**
6. **Acceptance Criteria**
7. **Safety Precautions**

### Test Documentation
- Test plan
- Test procedure
- Test report
- Test data
- Non-conformance reports
- Corrective actions

## Checklists

### Design Verification Checklist
- [ ] Requirements reviewed
- [ ] Interface definition complete
- [ ] Drawings released
- [ ] Material specifications verified
- [ ] Tolerance analysis completed
- [ ] Clearance analysis completed
- [ ] Load analysis completed
- [ ] Design review completed
- [ ] Customer approval (if required)

### Installation Checklist
- [ ] Parts verified (P/N, S/N)
- [ ] Surface preparation completed
- [ ] Fasteners verified
- [ ] Sealant applied (if required)
- [ ] Torque applied and verified
- [ ] Safety wire installed (if required)
- [ ] Final inspection passed
- [ ] Documentation completed

### Quality Inspection Checklist
- [ ] Dimensional inspection
- [ ] Visual inspection
- [ ] Material verification
- [ ] Workmanship inspection
- [ ] Test results reviewed
- [ ] Non-conformances dispositioned
- [ ] Traceability verified
- [ ] Records complete

## Non-Conformance Handling

### Non-Conformance Report (NCR)
- NCR number and date
- Part/assembly identification
- Description of non-conformance
- Root cause analysis
- Disposition (use-as-is, rework, repair, scrap)
- Corrective action
- Preventive action
- Approval signatures

### Disposition Options
- **Use-As-Is**: Acceptable without change
- **Rework**: Return to conforming condition
- **Repair**: Make acceptable (may not fully conform)
- **Scrap**: Cannot be used

## Quality Records

### Required Records
- Inspection reports
- Test reports
- Certificates of conformance
- Material certifications
- Calibration records
- Training records

### Record Retention
- Per contract requirements
- Per quality system requirements
- Typically 10+ years for aerospace

## Acceptance Criteria

### Pass/Fail Criteria
- Within specified tolerances
- No unacceptable defects
- Meets functional requirements
- Meets performance requirements

### Measurement Uncertainty
- Consider measurement capability
- Gage R&R studies
- Calibration intervals
- Environmental effects

## Cross-References

- [Interface Control Documents](../ICD/)
- [Tolerances](../TOLERANCES_GDT/)
- [Fasteners](../FASTENERS/)
- [Revisions](../REVISIONS/)

## Standards

- **ISO 9001**: Quality management systems
- **AS9100**: Quality management systems - Aerospace
- **ISO 10012**: Measurement management systems
- **ISO 10360**: Acceptance and reverification tests for CMM
- **ANSI/NCSL Z540**: Calibration laboratories and measuring and test equipment
- **MIL-STD-45662**: Calibration system requirements
- **SAE AS9102**: First Article Inspection Requirement
