---
title: "Multi-Layer Qualification Plan (MLQP) for GENCMS + CSDB"
version: "1.0"
date: "2025-10-16"
owner: "Certification Manager"
---

# MLQP Starter Kit for GENCMS + CSDB

## Overview

This Multi-Layer Qualification Plan (MLQP) starter kit provides a comprehensive framework for qualifying Data Modules (DM), Publication Modules (PM), and Interactive Electronic Technical Publications (IETP) within the GENCMS (Generic Content Management System) and CSDB (Common Source Database) environment.

The kit implements a defense-in-depth approach with automated validation, human oversight, security controls, audit trails, and evidence collection to ensure data quality and compliance with S1000D standards.

## Purpose

Qualify technical data products through:
- **Automated validation**: Schema, BREX, DMRL, reference integrity, applicability
- **Dual control**: Separation of duties, distinct approver requirements
- **Security gating**: Classification-based access, audience scoping, state transitions
- **Audit logging**: Immutable records of all access and modification events
- **Evidence collection**: Comprehensive build manifests for traceability
- **SLA enforcement**: Review deadlines, escalation paths, override tracking

## Directory Structure

```
MLQP_GENCMS_CSDB/
├── README.md                 # This file
├── policies/
│   └── rbac.rego            # OPA policy for RBAC with dual control
├── schemas/
│   ├── audit_log.schema.json      # Audit log entry schema
│   └── evidence_bundle.schema.json # Evidence bundle schema
├── tests/
│   ├── acceptance/
│   │   └── test_compliance.py     # Acceptance tests
│   └── security/
│       └── test_threats.py        # Security tests
├── ci/
│   ├── github/
│   │   └── mlqp.yml              # GitHub Actions workflow
│   └── gitlab/
│       └── .gitlab-ci.yml        # GitLab CI pipeline
├── configs/
│   └── agents.yaml               # Validation agent configuration
├── docs/
│   └── MLQP.md                   # MLQP documentation
├── scripts/
│   ├── validate.sh               # Validation script
│   ├── publish_dry_run.sh        # Publish preview script
│   ├── pack_evidence.sh          # Evidence packing script
│   └── deploy_staging.sh         # Staging deployment script
└── evidence/
    ├── bundle.json               # Example evidence bundle
    ├── approvals.json            # Approval records
    ├── access_decisions.json     # Access control decisions
    └── previews/                 # Applicability previews by audience
        ├── AVN.json
        ├── GEN.json
        └── INT.json
```

## Qualification Layers

### Layer 1: Automated Validation

**Validators**:
1. **SchemaValidator**: Validates against S1000D XML schemas
2. **BREXAgent**: Checks Business Rules Exchange (BREX) compliance
3. **DMRLChecker**: Verifies Data Module Requirements List conformance
4. **RefIntegrityAgent**: Ensures cross-reference integrity
5. **ApplicabilityAgent**: Generates applicability previews by audience

**Configuration**: See `configs/agents.yaml`

**Hard Failures**: Schema, DMRL, and reference checks must pass
**Advisory**: BREX violations reported but don't block progression

### Layer 2: Human Review

**Dual Approval Requirements**:
- Minimum 2 approvers required for publication
- Approvers must be distinct users
- Approvers cannot approve their own work
- Approvers must not share primary group with author (separation of duties)

**Review SLA**: 7 days (configurable in `configs/agents.yaml`)

### Layer 3: Security Gating

**Access Control** (enforced via OPA policy `policies/rbac.rego`):
- **Classification-based**: User clearance must meet or exceed object classification
- **Audience-based**: User must belong to at least one target audience
- **Role-based**: Actions gated by user roles (Viewer, Author, Reviewer, Publisher, Admin)
- **State-based**: Operations allowed only in appropriate workflow states

**Workflow States**:
- `inWork`: Editing allowed
- `review`: Approval allowed
- `approved`: Publication allowed
- `issue`: Published (read-only)

**Roles**:
- **Viewer**: View only
- **Author**: View and edit (in inWork state)
- **Reviewer**: View and approve (in review state)
- **Publisher**: View and publish (in approved state)
- **Auditor**: View only (for audit purposes)
- **Admin**: All operations

### Layer 4: Audit Logging

**Audit Log Schema**: `schemas/audit_log.schema.json`

Every operation logged with:
- Timestamp (ISO 8601)
- Request ID (for correlation)
- Actor (user/service with roles, groups, clearance)
- Action (view, edit, approve, publish, admin)
- Object (DM/PM/ICN with state, audience, classification)
- Outcome (allow/deny/success/failure)
- Reason (for denials)
- Findings (validation results)
- Signature (optional cryptographic attestation)

**Requirements**:
- Append-only log storage
- Tamper-evident (use signatures or immutable storage)
- Long-term retention per regulatory requirements

### Layer 5: Evidence Collection

**Evidence Bundle Schema**: `schemas/evidence_bundle.schema.json`

Each build produces:
- **Build ID**: Unique identifier
- **Timestamp**: Build execution time
- **Policy Version**: MLQP version applied
- **Inputs**: Source DMs, PM, BREX, DMRL, schemas, container images
- **Validators**: Results from each validation agent
- **Artifacts**: Generated outputs (IETP, PDFs, logs, reports) with SHA256 digests
- **Digests**: Input and container integrity hashes
- **Flags**: Policy violations or warnings

**Evidence Location**: `evidence/bundle.json`

**Usage**: Enables reproducibility, audit trail, and compliance demonstration

### Layer 6: Escalation and SLA

**SLA Monitoring**:
- Review due: 7 days from submission (configurable)
- Approval threshold: 2 distinct approvers (configurable)
- Automatic escalation on SLA breach
- Override logging for emergency changes

**Alert Thresholds**:
- Classification violations
- Failed dual approval
- Mixed-issue blocking (if multiple S1000D issues in single publication)
- Expired reviews

## Integration

### CI/CD Integration

**GitHub Actions**: Use `ci/github/mlqp.yml` as a template
**GitLab CI**: Use `ci/gitlab/.gitlab-ci.yml` as a template

**Pipeline Stages**:
1. **Preflight**: Linting and basic checks
2. **Validate**: Run all validation agents
3. **Build**: Dry-run publication preview
4. **Test**: Execute pytest acceptance and security tests
5. **Evidence**: Pack evidence bundle
6. **Deploy**: Staging deployment (manual gate)

### OPA Policy Engine

**Policy File**: `policies/rbac.rego`

**Integration**:
```bash
# Evaluate policy
opa eval -d policies/rbac.rego -i input.json "data.gencms.authz.allow"

# Example input.json:
{
  "user": {
    "id": "user123",
    "roles": ["Author", "Reviewer"],
    "groups": ["G-Engineering"],
    "clearance": 2,
    "audiences": ["AVN", "GEN"]
  },
  "object": {
    "type": "DM",
    "state": "review",
    "audience": ["AVN"],
    "classification": 1,
    "owner": "user456",
    "approvals": [
      {"user": "reviewer1", "groups": ["G-Review"]},
      {"user": "qa2", "groups": ["G-QA"]}
    ]
  },
  "action": "approve"
}
```

**Expected Output**: `true` (allow) or `false` (deny)

### Validation Agents

Agents configured in `configs/agents.yaml`:
- **Endpoint**: HTTP service URL
- **Timeout**: Request timeout in seconds
- **Hard Fail**: Whether failure blocks pipeline

**Example Agent Request**:
```json
POST /schema/validate
{
  "dm_list": ["DMC-AAA-BBB-CCC-00-10-10-01A-040A-A_en-US_001-00"],
  "schemas_pack": "S1000D_Issue_6.0"
}
```

**Expected Response**:
```json
{
  "result": "pass",
  "findings": []
}
```

## Testing

### Acceptance Tests

**File**: `tests/acceptance/test_compliance.py`

Tests verify:
- Evidence bundle exists
- Core validators pass
- Issue compatibility flags set correctly
- Applicability previews generated for each audience

**Run**:
```bash
pytest tests/acceptance/ -v
```

### Security Tests

**File**: `tests/security/test_threats.py`

Tests verify:
- Dual approval enforced (≥2 distinct users)
- Classification respected (clearance ≥ classification)
- Access control decisions logged

**Run**:
```bash
pytest tests/security/ -v
```

### Example Evidence

Sample evidence files provided in `evidence/`:
- `bundle.json`: Complete evidence bundle
- `approvals.json`: Dual approval records
- `access_decisions.json`: Access control logs
- `previews/*.json`: Applicability by audience

## Customization

### Extending Roles

Edit `policies/rbac.rego`, section `role_caps`:
```rego
role_caps := {
  "Viewer": {"view"},
  "Author": {"view","edit"},
  "Reviewer": {"view","approve"},
  "Publisher": {"view","publish"},
  "Auditor": {"view"},
  "Admin": {"view","edit","approve","publish","admin"},
  "YourCustomRole": {"view","edit","custom_action"},
}
```

### Adding Validators

Edit `configs/agents.yaml`:
```yaml
agents:
  - name: YourValidator
    endpoint: http://validator.local/your/endpoint
    timeout_s: 60
    hard_fail: true
```

Update `tests/acceptance/test_compliance.py` to verify results.

### Adjusting SLA

Edit `configs/agents.yaml`:
```yaml
sla:
  review_due_days: 14  # Change from 7 to 14 days
  approvals_required: 3  # Require 3 approvals instead of 2
```

Update OPA policy `policies/rbac.rego` if approvals logic changes.

### Custom Workflows

Modify state gates in `policies/rbac.rego`:
```rego
state_allows("edit")    { input.object.state == "inWork" }
state_allows("approve") { input.object.state == "review" }
state_allows("publish") { input.object.state == "approved" }
```

Add new states and transition rules as needed.

## Deployment

### Prerequisites

- OPA (Open Policy Agent) installed
- Python 3.11+ with pytest
- S1000D validation agents available
- Evidence storage (file system or object store)

### Quick Start

1. **Clone or copy this MLQP starter kit**
2. **Configure agents**: Edit `configs/agents.yaml` with your validator endpoints
3. **Customize policy**: Adjust `policies/rbac.rego` for your organization
4. **Set up CI/CD**: Use templates in `ci/` directory
5. **Run tests**: `pytest tests/ -v`
6. **Integrate into build**: Reference scripts in `scripts/` from your pipeline

### Production Checklist

- [ ] OPA policy reviewed and approved
- [ ] Validation agents deployed and tested
- [ ] Audit log storage configured (append-only, tamper-evident)
- [ ] Evidence archive retention policy defined
- [ ] SLA monitoring and alerts configured
- [ ] Role mappings verified with organizational structure
- [ ] Classification levels aligned with security policy
- [ ] Audience definitions match program requirements
- [ ] Test suite passing on representative data
- [ ] CI/CD pipeline integrated and tested

## Standards Compliance

This MLQP framework supports compliance with:

- **S1000D**: International Specification for Technical Publications
- **DO-178C**: Software Considerations in Airborne Systems (for software in IETP viewers)
- **DO-254**: Hardware Design Assurance (for IETP display hardware)
- **ISO 27001**: Information Security Management
- **AS9100D**: Quality Management Systems for Aerospace

Reference the parent certification framework in:
- `../../CERTIFICATION_PLANS/`
- `../../COMPLIANCE_CHECKLISTS/`
- `../../TOOL_QUALIFICATION/`

## Troubleshooting

### Tests Failing

**Issue**: `test_evidence_bundle_exists` fails  
**Solution**: Ensure `evidence/bundle.json` exists and is valid JSON

**Issue**: `test_dual_approval_enforced` fails  
**Solution**: Check `evidence/approvals.json` has ≥2 distinct approvers per object

**Issue**: Validator tests fail  
**Solution**: Verify agents endpoints in `configs/agents.yaml` are accessible

### OPA Policy Issues

**Issue**: Policy always denies  
**Solution**: Check input shape matches expected format, verify role/group/audience overlap

**Issue**: Dual approval bypass  
**Solution**: Verify `distinct_approvers >= 2` and `not_self_approval` logic in policy

### CI/CD Issues

**Issue**: Pipeline timeout  
**Solution**: Increase agent timeout_s in `configs/agents.yaml`

**Issue**: Scripts not executable  
**Solution**: `chmod +x scripts/*.sh`

## Support and Extension

For questions or enhancements:
1. Review `docs/MLQP.md` for layer descriptions
2. Check parent certification documentation in `../../`
3. Extend tests in `tests/` for new requirements
4. Update schemas in `schemas/` for new evidence types
5. Consult OPA documentation for policy extensions

## References

- **OPA Policy Language**: https://www.openpolicyagent.org/docs/latest/policy-language/
- **S1000D Specification**: http://www.s1000d.org/
- **JSON Schema**: https://json-schema.org/
- **pytest Documentation**: https://docs.pytest.org/

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-16 | MLQP Team | Initial MLQP starter kit |

---

**Location**: `00-PROGRAM/COMPLIANCE/03-CERTIFICATION/TOOL_QUALIFICATION/MLQP_GENCMS_CSDB/`  
**Integration**: Works with existing certification framework  
**Status**: Ready for customization and deployment
