# MODEL_BASELINES

Model baselines aligned with configuration management.

## Purpose

This directory contains symbolic links, manifests, or references to configuration baselines established at major stage gates. Model baselines are the authoritative snapshots of the system architecture at specific points in time.

## Baseline Structure

Each baseline includes:
- **Model Version**: SysML model snapshot (version tag or commit SHA)
- **Requirements Snapshot**: Requirements database state
- **ICD Version**: Interface Control Document versions
- **Metadata**: Baseline date, approver, stage gate

## Baseline Naming Convention

Format: `BASELINE_<GATE>_<DATE>_<VERSION>`

Examples:
- `BASELINE_PDR_2025-03-15_V1.0/`
- `BASELINE_CDR_2025-09-20_V2.0/`
- `BASELINE_TRR_2026-01-10_V2.1/`

## Contents

### Manifest File
Each baseline directory contains a `MANIFEST.yaml`:

```yaml
baseline_id: BASELINE_PDR_2025-03-15_V1.0
stage_gate: PDR
date: 2025-03-15
version: 1.0
approver: Chief Engineer
description: Preliminary Design Review baseline

models:
  - name: Aircraft System Architecture
    path: SYSML_MODELS/AIRCRAFT/SYSTEM_ARCHITECTURE.sysml
    version: 1.0.5
    commit_sha: abc123def456
  
  - name: Spacecraft System Architecture
    path: SYSML_MODELS/SPACECRAFT/SYSTEM_ARCHITECTURE.sysml
    version: 1.0.3
    commit_sha: 789ghi012jkl

requirements:
  database: DOORS
  snapshot_id: REQ_SNAPSHOT_PDR_20250315
  total_requirements: 1245
  allocated_requirements: 1184
  allocation_percentage: 95.1%

interfaces:
  - id: ICD-001
    name: Avionics-GNC Interface
    version: 1.2
  - id: ICD-002
    name: Propulsion-Power Interface
    version: 1.1

traceability:
  requirements_to_model: 95.1%
  model_to_verification: 87.3%
  
references:
  config_mgmt_baseline: /CONFIG_MGMT/04-BASELINES/BASELINE_PDR_2025-03-15/
```

### Symbolic Links
Symbolic links to the actual baseline artifacts in CONFIG_MGMT:
```bash
ln -s /CONFIG_MGMT/04-BASELINES/BASELINE_PDR_2025-03-15 ./BASELINE_PDR_2025-03-15
```

## Baseline Establishment Process

1. **Pre-Baseline Review**
   - Model completeness check
   - Requirements allocation verification (≥95%)
   - Interface definition completeness
   - Traceability gap analysis

2. **Baseline Approval**
   - Configuration Control Board (CCB) review
   - Stakeholder sign-off
   - Formal approval by Chief Engineer

3. **Baseline Capture**
   - Create model version tag
   - Export requirements snapshot
   - Generate ICDs
   - Create manifest file
   - Link to CONFIG_MGMT baseline

4. **Post-Baseline**
   - Lock baseline (read-only)
   - Enable change control for subsequent changes
   - Communicate baseline availability to stakeholders

## Change Management

### Changes After Baseline
- All changes require Change Request (CR)
- Impact analysis performed using traceability
- CCB approval required for baseline changes
- New baseline created if significant changes accumulate

### Baseline Updates
- Minor updates: Patch version (e.g., 1.0.1)
- Major updates: New baseline at next stage gate

## Integration with CONFIG_MGMT

### Alignment
- Model baselines synchronized with CONFIG_MGMT/04-BASELINES/
- Common baseline naming and versioning
- Unified change control process

### Cross-References
- Each model baseline references its corresponding CONFIG_MGMT baseline
- Configuration items (CIs) from CONFIG_MGMT linked to MBSE elements

## Audit and Compliance

### Baseline Audit
- Verify baseline completeness (all artifacts present)
- Validate traceability (requirements ↔ model)
- Check approval documentation
- Confirm change control compliance

### Compliance Requirements
- AS9100: Configuration management
- ECSS-M-ST-40: Configuration identification and baselines
- ISO 27001: Access control and audit trail

## Related Documents

- **CONFIG_MGMT/04-BASELINES/** - Program-level configuration baselines
- **04-MBSE/SYSML_MODELS/** - SysML model repository
- **04-MBSE/REQUIREMENTS_ALLOCATION.csv** - Requirements traceability
- **03-ARCHITECTURE/INTEGRATION_POINTS.md** - Stage gate baseline criteria
