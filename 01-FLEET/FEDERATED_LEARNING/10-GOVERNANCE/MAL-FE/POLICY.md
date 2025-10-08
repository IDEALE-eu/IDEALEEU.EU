# MAL-FE POLICY

Fleet Experiments approval workflow policy.

## Approval Workflow

### Step 1: Proposal Submission

**Submitter**: AI/ML Engineer  
**Document**: Experiment proposal (see ../../15-TEMPLATES/)  
**Contents**:
- Hypothesis and objectives
- Success criteria and metrics
- Resource requirements (compute, bandwidth)
- Duration and rollback plan
- Risk assessment

### Step 2: Technical Review

**Reviewer**: AI/ML Team Lead  
**Criteria**:
- [ ] Scientifically sound methodology
- [ ] Metrics aligned with business goals
- [ ] Resource requirements feasible
- [ ] Rollback plan adequate

**Timeline**: 2 business days

### Step 3: Operational Review

**Reviewer**: Fleet Operations Manager  
**Criteria**:
- [ ] No disruption to fleet operations
- [ ] Network bandwidth available
- [ ] Timing aligned with maintenance schedule
- [ ] Client selection reasonable

**Timeline**: 2 business days

### Step 4: Safety Review (if applicable)

**Reviewer**: Safety Engineering  
**Criteria**:
- [ ] No safety-critical system interference
- [ ] Resource constraints respected
- [ ] Rollback tested

**Timeline**: 3 business days (if required)

### Step 5: Approval Decision

**Approvers**: AI/ML Team Lead + Fleet Operations Manager (+ Safety if applicable)  
**Outcome**: Approved | Conditional | Rejected  
**Documentation**: Approval logged in experiment tracking (../../07-EXPERIMENTS/TRACKING.md)

## Post-Experiment Review

- Results presented to stakeholders within 1 week
- Decision: Deploy, iterate, or discard
- Lessons learned documented

## Related Documents

- [**../../07-EXPERIMENTS/**](../../07-EXPERIMENTS/) -  Experiment tracking
- [**../../15-TEMPLATES/**](../../15-TEMPLATES/) -  Experiment proposal template
