# MAL-CB POLICY

Change & Baseline control policy for FL model integration with CONFIG_MGMT.

## Baseline Definition

**FL Model Baseline** includes:
- Model architecture and weights (versioned)
- Training configuration (FL algorithm, hyperparameters)
- Data contracts (input/output schemas)
- Certification evidence (DO-178C, DO-326A)

## Change Control Process

### Step 1: Change Request

**Submitter**: AI/ML Team  
**Document**: ECR (Engineering Change Request) - see ../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/ECR/  
**Contents**:
- Baseline impact (model version, schema changes)
- Justification (performance improvement, bug fix)
- Affected configuration items

### Step 2: CCB Review

**Reviewer**: Configuration Control Board  
**Criteria**:
- [ ] Impact assessment complete
- [ ] Traceability maintained (requirements ↔ model ↔ tests)
- [ ] Certification evidence updated (if applicable)
- [ ] Baseline integrity preserved

### Step 3: Approval Decision

**Approvers**: CCB  
**Outcome**: Approved | Conditional | Rejected  
**Documentation**: ECO (Engineering Change Order) issued

## Baseline Release

- FL model baselines released with system baseline
- Versioned in `00-PROGRAM/CONFIG_MGMT/07-RELEASES/AIRCRAFT/`
- Linked to requirements, tests, and certification evidence

## Related Documents

- **../../../00-PROGRAM/CONFIG_MGMT/** - CONFIG_MGMT framework
- **../../06-MODELS/REGISTRY.md** - Model versioning
