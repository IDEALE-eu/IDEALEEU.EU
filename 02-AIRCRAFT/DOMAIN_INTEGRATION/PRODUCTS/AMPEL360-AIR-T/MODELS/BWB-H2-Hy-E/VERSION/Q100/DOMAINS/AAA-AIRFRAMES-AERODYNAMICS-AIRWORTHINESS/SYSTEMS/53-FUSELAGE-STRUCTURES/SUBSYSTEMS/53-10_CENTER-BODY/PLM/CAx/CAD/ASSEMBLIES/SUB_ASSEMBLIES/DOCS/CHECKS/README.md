# CHECKS — Quality Inspection and Verification Procedures

## Purpose

This directory contains quality inspection and verification procedures for 53-10 Center Body sub-assemblies. Inspection procedures ensure that assemblies meet design requirements, manufacturing specifications, and quality standards.

## Contents

### Inspection Procedures
- **First Article Inspection (FAI)**: Complete verification of first production unit
- **In-process inspection**: Checks during assembly operations
- **Final inspection**: Complete assembly verification before acceptance
- **Source inspection**: Vendor inspection procedures
- **Receiving inspection**: Incoming parts verification

### Inspection Types
- **Visual inspection**: Surface condition, workmanship, cleanliness
- **Dimensional inspection**: Measurements and tolerances
- **Functional testing**: Operational verification (if applicable)
- **Non-destructive testing (NDT)**: X-ray, ultrasonic, eddy current, etc.
- **Destructive testing**: Sample testing (for qualification)

### Inspection Documentation
- **Inspection checklists**: Step-by-step verification lists
- **Inspection reports**: Documented inspection results
- **Measurement data**: Recorded dimensional measurements
- **Defect reports**: Non-conformance documentation
- **Certificate of conformance**: Supplier quality documents

## Naming Convention

Use the following pattern for inspection documents:
```
53-10_CHECK_<assembly>_<inspection-type>_v<version>.<ext>
```

Examples:
- `53-10_CHECK_FRAME-F05_FAI_v01.pdf`
- `53-10_CHECK_STRINGER-L01_DIMENSIONAL_v02.xlsx`
- `53-10_CHECK_BULKHEAD-BH05_NDT_v01.docx`

## Inspection Levels

### Level 1 - Normal Inspection
- Standard inspection for production parts
- Sampling or 100% inspection as defined
- Typical inspection requirements

### Level 2 - Reduced Inspection
- For proven processes with good history
- Reduced sampling frequency
- Minimum inspection requirements

### Level 3 - Tightened Inspection
- For processes with quality issues
- Increased inspection frequency
- Enhanced inspection requirements
- May require 100% inspection

## First Article Inspection (FAI)

FAI verifies first production unit:
- **All dimensions**: Complete dimensional verification
- **All materials**: Material certification verification
- **All processes**: Process verification (heat treat, etc.)
- **All characteristics**: Critical and major characteristics
- **Full documentation**: Complete inspection report

### FAI Documentation
- AS9102 forms (aerospace standard)
- Dimensional measurement report
- Material certificates
- Process certifications
- Non-conformance reports (if any)
- Corrective actions (if required)

## In-Process Inspection

Inspection points during assembly:
- **After major operations**: Key assembly steps
- **Before concealment**: Before parts are covered
- **Critical characteristics**: Key dimensions and features
- **Hold points**: Mandatory inspection before proceeding
- **Witness points**: Customer or regulatory witness required

## Dimensional Inspection

Measurement and verification:
- **Critical dimensions**: Dimensions affecting fit/function/safety
- **Major dimensions**: Important but not critical
- **Minor dimensions**: Reference or non-critical
- **Inspection methods**: Calipers, micrometers, CMM, laser scan
- **Tolerance verification**: Within specification limits

### Measurement Equipment
- **Hand tools**: Calipers, micrometers, height gauges
- **Coordinate Measuring Machine (CMM)**: 3D measurement
- **Laser scanning**: Non-contact surface measurement
- **Optical comparators**: 2D profile measurement
- **Fixtures and gauges**: Go/no-go and functional gauges

## Visual Inspection

Surface and workmanship inspection:
- **Surface condition**: Scratches, dents, corrosion
- **Cleanliness**: Contamination, foreign objects
- **Fastener installation**: Driven head formation, gap
- **Sealing**: Sealant application, fillet formation
- **Marking**: Part identification, traceability
- **Protective finishes**: Coating, paint, anodize

### Acceptance Criteria
- **Cosmetic standards**: Surface appearance requirements
- **Workmanship standards**: Acceptable quality level (AQL)
- **Damage limits**: Allowable damage (scratches, dents)
- **Repair criteria**: When repair is required vs. acceptable
- **Rework procedures**: How to correct defects

## Non-Destructive Testing (NDT)

Common NDT methods:
- **X-ray radiography**: Internal defects, porosity, cracks
- **Ultrasonic testing**: Thickness, delamination, voids
- **Eddy current**: Surface and near-surface cracks
- **Magnetic particle**: Surface and near-surface defects (ferrous materials)
- **Penetrant testing**: Surface-breaking defects
- **Visual inspection**: Enhanced with borescopes, mirrors

### NDT Requirements
- **Qualified technicians**: Certified NDT Level II or III
- **Written procedures**: Per ASTM, ASNT, or MIL standards
- **Calibration**: Equipment calibration verification
- **Documentation**: NDT reports with results
- **Disposition**: Accept, reject, or repair decisions

## Functional Testing

Operational verification (if applicable):
- **Fit checks**: Assembly of mating parts
- **Load testing**: Proof load or ultimate load testing
- **Pressure testing**: Leak test for sealed assemblies
- **Operational testing**: Function of mechanisms or systems
- **Performance testing**: Meets performance specifications

## Related Directories

- **Frame sections**: [`../../FRAME_SECTIONS/`](../../FRAME_SECTIONS/)
- **All sub-assembly directories**: Inspection procedures for each type
- **BOM**: [`../BOM/`](../BOM/) - Parts to be inspected
- **Sequence**: [`../SEQUENCE/`](../SEQUENCE/) - When to inspect during assembly
- **Revisions**: [`../../REVISIONS/`](../../REVISIONS/) - Inspection history
- **Component models**: [`../../../../MODELS/`](../../../../MODELS/) - Design reference

## Inspection Planning

### Quality Plan
- **Inspection points**: Where and when to inspect
- **Inspection methods**: How to inspect
- **Acceptance criteria**: Pass/fail standards
- **Sampling plan**: How many to inspect
- **Documentation**: Records to maintain

### Critical Characteristics
Identify and track:
- **Critical-to-Quality (CTQ)**: Characteristics affecting quality
- **Critical-to-Safety (CTS)**: Characteristics affecting safety
- **Key Product Characteristics (KPC)**: Important features
- **Special characteristics**: Regulatory or customer-required

## Acceptance Criteria

Define clear pass/fail standards:
- **Dimensional tolerances**: In specification limits
- **Surface finish**: Meets surface roughness requirements
- **Material properties**: Meets material specifications
- **Workmanship**: Meets quality standards
- **Functionality**: Operates as designed

## Non-Conformance

When defects are found:
1. **Document**: Record defect with photos/measurements
2. **Contain**: Prevent use of non-conforming parts
3. **Evaluate**: Determine impact and disposition
4. **Disposition**: Accept as-is, rework, repair, or scrap
5. **Corrective action**: Prevent recurrence
6. **Verify**: Re-inspect after corrective action

### Disposition Options
- **Accept as-is**: Defect does not affect form/fit/function
- **Rework**: Return to normal process to correct
- **Repair**: Non-standard process to correct
- **Use-as-is**: With engineering approval (waiver)
- **Scrap**: Discard non-conforming part

## Documentation Requirements

Inspection records must include:
- **Part identification**: Part number, serial number
- **Inspection date**: When inspected
- **Inspector**: Who performed inspection
- **Inspection results**: Measurements, observations
- **Acceptance decision**: Accept or reject
- **Discrepancies**: Non-conformances found
- **Disposition**: Action taken on discrepancies

## Statistical Process Control (SPC)

For production monitoring:
- **Control charts**: Track measurement trends
- **Capability studies**: Cp, Cpk calculations
- **Trend analysis**: Identify process drift
- **Out-of-control actions**: Response to variations
- **Process improvement**: Continuous improvement

## Measurement System Analysis (MSA)

Verify measurement system capability:
- **Gage R&R**: Repeatability and reproducibility
- **Bias study**: Measurement accuracy
- **Linearity study**: Accuracy across range
- **Stability study**: Consistency over time

## Metadata Requirements

Each inspection document should include:
- **Assembly reference**: Associated assembly part number
- **Inspection type**: FAI, in-process, final, etc.
- **Revision**: Procedure revision level
- **Date**: Creation or revision date
- **Author**: Responsible quality engineer
- **Approval**: Authorized approver
- **Effectivity**: Applicable serial numbers or dates
- **Status**: Draft, released, or obsolete

## Quality Management System

Inspection procedures support:
- **AS9100**: Aerospace quality management system
- **ISO 9001**: General quality management standard
- **Customer requirements**: Specific customer quality requirements
- **Regulatory requirements**: FAA, EASA, or other regulatory requirements
- **Internal standards**: Company quality standards

## Version Control

- Track inspection procedure revisions
- Document reason for changes
- Maintain previous procedure versions
- Coordinate changes with ECO (Engineering Change Order)
- Update inspection records when procedures change
- Re-train inspectors on revised procedures
