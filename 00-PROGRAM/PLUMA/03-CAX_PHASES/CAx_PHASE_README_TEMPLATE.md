# CAx Phase Template README

## Purpose

This template provides a standard structure for CAx phase directories. Copy and customize for each CAx phase (CAD, CAE, CAI, CAO, CAM, CAP, CAS, CAV, CMP).

## PLUMA Integration

This directory is part of the **PLUMA** (Product Lifecycle UiX Management Automation) platform. PLUMA orchestrates the 9-phase CAx lifecycle with industrial-scale automation.

### Phase Definition

**{PHASE}** — {PHASE_FULL_NAME}

**Focus**: {PHASE_FOCUS}

**Scalability Dimension**: {SCALABILITY_DESCRIPTION}

See [PLUMA CAx Phases Documentation](../../../../../../../../../../../../00-PROGRAM/PLUMA/03-CAX_PHASES/README.md) for comprehensive phase specifications.

### Key MAL Services
- {MAL_SERVICE_1}
- {MAL_SERVICE_2}

### Metabuilders Used
- {METABUILDER_1}
- {METABUILDER_2}

## Directory Structure

```
{PHASE}/
├── README.md                    # This file
├── MODELS/                      # CAx models and designs
├── ANALYSIS/                    # Analysis results and reports
├── VALIDATION/                  # Validation data and reports
├── REPORTS/                     # Engineering reports
├── SCRIPTS/                     # Automation scripts
├── TEMPLATES/                   # Reusable templates
└── DOC/                         # Documentation
```

## File Organization

### Naming Convention

```
{PART_ID}_{DESCRIPTION}_{REV}.{ext}
```

**Examples**:
- `GSE-07-10-001_Handling_Crane_R001.step`
- `ATA-53-10-01_Structural_Analysis_V03.pdf`
- `BWB-Q100_Wing_Design_R005.catpart`

### File Types

**Native Formats**:
- CAD: `.catpart`, `.prt`, `.sldprt`
- Analysis: `.db`, `.cdb`, `.inp`
- Documents: `.docx`, `.xlsx`

**Neutral Formats** (for interoperability):
- STEP (`.step`, `.stp`)
- IGES (`.iges`, `.igs`)
- PDF (`.pdf`)
- CSV (`.csv`)

## PLUMA Operations

### Creating Frozen Context

Capture the current phase state for reuse:

```bash
make pluma-freeze \
  PHASE={PHASE} \
  PROGRAM=${PROGRAM} \
  TAG=${TAG}
```

### Cloning Context

Clone from existing program:

```bash
make pluma-clone \
  FROM_CONTEXT=${SOURCE_PROGRAM}/{PHASE} \
  TO_CONTEXT=${TARGET_PROGRAM}/{PHASE} \
  OVERRIDES_FILE=config/overrides.yaml
```

### Phase Transition

Transition to next phase:

```bash
make pluma-phase \
  FROM_PHASE={PHASE} \
  TO_PHASE={NEXT_PHASE} \
  PROGRAM=${PROGRAM}
```

## Standards and Guidelines

### Quality Standards
- Follow applicable CAx standards for this discipline
- Ensure traceability to EBOM items
- Maintain configuration control
- Document all design decisions

### Review Process
1. Self-review before submission
2. Peer review by domain expert
3. Phase gate approval (via PLUMA Interphase Control)
4. Frozen context creation upon approval

### Configuration Management
- All artifacts under version control
- Changes tracked in configuration management system
- Baseline management via frozen contexts
- UTCS blockchain anchoring for critical milestones

## Traceability

### Requirements Traceability
- Link to requirements in MBSE models
- Document requirement satisfaction
- Maintain traceability matrix

### Interface Control
- Reference ICDs in `INTERFACES/`
- Document interface dependencies
- Coordinate changes with connected domains

## Tools and Integration

### Recommended Tools
- {TOOL_1}: {TOOL_PURPOSE_1}
- {TOOL_2}: {TOOL_PURPOSE_2}

### PLUMA Metabuilders
This phase uses the following auto-generated UIs:
- {METABUILDER_1}: {METABUILDER_PURPOSE_1}
- {METABUILDER_2}: {METABUILDER_PURPOSE_2}

See [Metabuilders Documentation](../../../../../../../../../../../../00-PROGRAM/PLUMA/05-METABUILDERS/README.md) for details.

## Automation

### Available Scripts
- `scripts/validate.sh`: Validate artifacts against standards
- `scripts/export.sh`: Export to neutral formats
- `scripts/report.sh`: Generate phase report

### CI/CD Integration
This directory is monitored by PLUMA CI/CD pipelines:
- Automatic validation on commits
- Phase transition checks
- Frozen context integrity verification

## Metrics

### Phase Metrics
Track the following metrics for this phase:
- Artifact count
- Validation pass rate
- Review cycle time
- Resource utilization

View metrics: `make pluma-metrics PHASE={PHASE} PROGRAM=${PROGRAM}`

## Best Practices

1. **Organize Early**: Set up directory structure at phase start
2. **Name Consistently**: Use standard naming conventions
3. **Document Thoroughly**: Explain design decisions and rationale
4. **Review Regularly**: Conduct periodic peer reviews
5. **Validate Often**: Run validation checks frequently
6. **Freeze Milestones**: Create frozen contexts at key milestones
7. **Reuse When Possible**: Check for similar artifacts in other programs

## Related Documentation

### PLUMA Documentation
- [Master Architecture](../../../../../../../../../../../../00-PROGRAM/PLUMA/01-ARCHITECTURE/MASTER_ARCHITECTURE_V1.1.md)
- [CAx Phases](../../../../../../../../../../../../00-PROGRAM/PLUMA/03-CAX_PHASES/README.md)
- [Integration Guide](../../../../../../../../../../../../00-PROGRAM/PLUMA/07-INTEGRATION/README.md)

### TFA Documentation
- [TFA Implementation](../../../../../../../../../../../../02-AIRCRAFT/MODEL_IDENTIFICATION/TFA_IMPLEMENTATION_SUMMARY.md)
- [Automation Guide](../../../../../../../../../../../../02-AIRCRAFT/MODEL_IDENTIFICATION/AUTOMATION_README.md)

### Program Documentation
- [Digital Thread](../../../../../../../../../../../../00-PROGRAM/DIGITAL_THREAD/README.md)
- [Configuration Management](../../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/README.md)
- [Quality Management](../../../../../../../../../../../../00-PROGRAM/QUALITY_QMS/README.md)

## Support

For questions or issues:
- **PLUMA Support**: pluma-support@ideale.eu
- **Phase Lead**: {PHASE_LEAD_EMAIL}
- **Domain Lead**: {DOMAIN_LEAD_EMAIL}

---

**Last Updated**: {DATE}  
**Template Version**: 1.0  
**PLUMA Version**: 1.1
