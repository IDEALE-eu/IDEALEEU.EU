# CCB_HANDOFF

Configuration Control Board integration and handoff procedures.

## CCB Integration Points

### FL Model Baselines

FL models are configuration items (CIs) managed by CCB:

- **CI Type**: Software (embedded model)
- **CI ID**: FL-MODEL-{use_case}-{version} (e.g., FL-MODEL-PM-ENGINE-1.0.0)
- **Baseline**: Tracked in `00-PROGRAM/CONFIG_MGMT/07-RELEASES/AIRCRAFT/`

### Change Control

All production FL model deployments require ECR/ECO:

1. **ECR Submission**: AI/ML Team submits ECR (see ../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/ECR/)
2. **Impact Assessment**: CCB reviews baseline impact
3. **CCB Meeting**: Weekly CCB meeting, decision: Approve/Conditional/Reject
4. **ECO Issuance**: If approved, ECO issued with deployment authorization
5. **Deployment**: FL model deployed per ECO instructions (see ../../09-DEPLOYMENT/)

### Traceability

FL models linked in traceability matrix:

- **Requirements**: Linked in `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/REQ_ITEM.csv`
- **Tests**: Linked in [../../08-VALIDATION_VVP/TEST_PLANS.md](../../08-VALIDATION_VVP/TEST_PLANS.md)
- **Certification**: Linked in [../../08-VALIDATION_VVP/CERT_EVIDENCE_LINKS.md](../../08-VALIDATION_VVP/CERT_EVIDENCE_LINKS.md)

## CCB Meeting Cadence

- **Frequency**: Weekly (Thursdays 10:00 UTC)
- **Attendees**: Chief Engineer, Safety Engineering, AI/ML Team Lead, Configuration Manager
- **FL Model Reviews**: Typically 15-30 minutes per model

## Related Documents

- [**MAL-CB/POLICY.md**](MAL-CB/POLICY.md) - Baseline control policy
- [**../../../00-PROGRAM/CONFIG_MGMT/**](../../../00-PROGRAM/CONFIG_MGMT/) -  CONFIG_MGMT framework
- [**../../../00-PROGRAM/CONFIG_MGMT/05-CCB/**](../../../00-PROGRAM/CONFIG_MGMT/05-CCB/) -  CCB charter and procedures
