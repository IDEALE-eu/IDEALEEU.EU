# FAI — First Article Inspection

## Purpose

This directory contains first article inspection (FAI) packages documenting complete verification of the first production unit against all design requirements.

## Contents

- Dimensional inspection reports
- Material certifications
- Process verification records
- Functional test results
- Coating verification
- Weld/joint inspection records
- As-built configuration documentation
- Non-conformance dispositions
- FAI summary report

## File Naming Convention

```
FAI_<serial>_<section>_<date>.{pdf|xlsx}
```

Examples:
- `FAI_RAD-SN001_dimensional_20251011.pdf`
- `FAI_HX-SN005_materials_20251012.xlsx`
- `FAI_CP123_summary_report_20251015.pdf`

## FAI Package Requirements

Complete FAI package includes:

### 1. Dimensional Inspection
- All critical dimensions measured
- Comparison to design drawings
- Tolerance verification
- CMM reports or manual inspection
- Photos of critical features

### 2. Material Certifications
- Material test reports (MTRs)
- Chemical composition verification
- Mechanical property testing
- Material traceability to lot/heat
- Vendor certifications

### 3. Process Verification
- Welding procedure qualification
- Brazing parameter verification
- Coating application records
- Heat treatment records
- Cleaning and contamination control

### 4. Functional Testing
- Leak test (helium sniffer)
- Proof pressure test
- Flow/pressure drop test
- Thermal performance test (if required)
- Visual and functional inspection

### 5. Workmanship Verification
- Visual inspection per IPC-A-610 or equivalent
- Weld inspection per AWS or equivalent
- Surface finish verification
- Cleanliness verification
- Photos of as-built configuration

## Inspection Criteria

All measurements compared to:
- ✅ Design drawings and tolerances
- ✅ Material specifications
- ✅ Process specifications
- ✅ Workmanship standards
- ✅ Functional requirements

## Non-Conformances

Any deviations must be:
- Documented with NCR number
- Dispositioned (use-as-is, repair, rework, scrap)
- Approved by engineering and QA
- Included in FAI package with justification

## Approval Process

FAI package requires approval from:
- ✅ Manufacturing engineer
- ✅ Quality assurance
- ✅ Design engineer
- ✅ Program management
- ✅ Customer (if specified in contract)

## FAI Benefits

First article inspection:
- Validates design can be manufactured
- Identifies process issues early
- Establishes baseline for production
- Demonstrates compliance to requirements
- Provides lessons learned for subsequent units

## Production Acceptance

After FAI approval:
- Production units built to same processes
- Periodic audits verify process control
- Key characteristics monitored
- FAI referenced for acceptance criteria

## Traceability

FAI package provides:
- Serial number traceability
- Material lot traceability
- Process parameter records
- Test data baseline
- Configuration baseline

## Related Directories

- **[../calibration/](../calibration/)** — Inspection equipment calibration
- **[../reports/](../reports/)** — Additional test reports
- **[../anomalies/](../anomalies/)** — NCRs and dispositions
- **[../../CAI/](../../CAI/)** — Inspection procedures and plans
- **[../../EBOM_LINKS.md](../../EBOM_LINKS.md)** — BOM traceability

---

**Last Updated**: 2025-10-10
