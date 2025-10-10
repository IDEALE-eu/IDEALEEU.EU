# CHECKS — Quality Assurance Validation

## Purpose

This directory contains **QA validation files** including inspection models, reference geometries, and validation datasets for quality control and inspection.

## What to Store

- CMM inspection programs (as STEP references)
- First Article Inspection (FAI) reference models
- Quality control checkpoints
- Dimensional validation references
- Inspection fixture reference geometry
- Measurement master models

## QA File Types

### Inspection References
- Nominal geometry for CMM programming
- Critical feature callouts
- Measurement point definitions
- Inspection datum references

### Validation Models
- Master inspection models
- Tolerance analysis references
- Statistical process control (SPC) references
- In-process inspection checkpoints

### FAI Support
- First article inspection models
- AS9102 inspection requirements
- Supplier quality verification

## File Naming Convention

```
53-10_QA_<check-type>_<part-name>_<revision>_<date>.step
```

Example:
```
53-10_QA_CMM_FRAME-F01_PN-12345_RevB_20250110.step
53-10_QA_FAI_BULKHEAD-B1_PN-12350_RevA_20250110.step
```

## Quality Standards

Reference applicable standards:
- AS9102 (First Article Inspection)
- AS9100 (Quality Management Systems)
- ISO 9001 (Quality Management)
- ASME Y14.5 (GD&T)
- Customer-specific requirements

## Related Directories

- [**../../PARTS/PMI/**](../../PARTS/PMI/) — PMI and GD&T source data
- [**../../REVISIONS/RELEASED/**](../../REVISIONS/RELEASED/) — Production models being inspected
- [**../../SUPPLIERS/**](../../SUPPLIERS/) — Supplier quality requirements
- [**../../TEMPLATES/**](../../TEMPLATES/) — QA templates and standards

## Inspection Workflow

1. **Export QA model**: Create inspection reference from released model
2. **CMM programming**: Use STEP file for CMM program development
3. **Inspection**: Perform dimensional inspection
4. **Validation**: Compare measured vs. nominal
5. **Documentation**: Record results and deviations

## Validation Checklist

QA files should enable:
- [ ] Critical dimension verification
- [ ] GD&T compliance checking
- [ ] Feature location validation
- [ ] Surface profile verification
- [ ] Datum establishment
- [ ] Coordinate system definition

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Quality procedures: `00-PROGRAM/QUALITY/`
- Inspection standards: `00-PROGRAM/STANDARDS/`
