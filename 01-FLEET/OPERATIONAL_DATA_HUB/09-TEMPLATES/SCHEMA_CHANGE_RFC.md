# Schema Change Request (RFC)

## Request Information
RFC ID: RFC-YYYY-XXXX
Date: YYYY-MM-DD
Requestor: Name / Team
Priority: LOW | MEDIUM | HIGH | CRITICAL

## Change Summary
**One-sentence summary**: Brief description of the proposed change

## Current State
Schema: schema_name_here
Current Version: X.Y.Z
Status: ACTIVE | DEPRECATED
Owner: Team Name

### Current Schema Definition
```json
{
  "fields": [
    {
      "name": "field_name",
      "type": "current_type",
      "doc": "current description"
    }
  ]
}
```

## Proposed Change

### Change Type
- [ ] Breaking Change (MAJOR version increment)
- [ ] Backward-Compatible Addition (MINOR version increment)
- [ ] Bug Fix / Documentation (PATCH version increment)

### New Schema Version
Proposed Version: X.Y.Z

### New Schema Definition
```json
{
  "fields": [
    {
      "name": "field_name",
      "type": "new_type",
      "doc": "new description"
    }
  ]
}
```

### Changes Made
- Change 1: Description
- Change 2: Description
- Change 3: Description

## Rationale

### Business Justification
Why is this change necessary?
- Reason 1
- Reason 2

### Technical Justification
What technical problems does this solve?
- Technical reason 1
- Technical reason 2

### Alternatives Considered
- Alternative 1: Description (why not chosen)
- Alternative 2: Description (why not chosen)

## Impact Assessment

### Affected Systems
| System/Service | Impact Level | Migration Required | Owner |
|----------------|--------------|-------------------|-------|
| System 1 | LOW/MEDIUM/HIGH | YES/NO | Team Name |
| System 2 | LOW/MEDIUM/HIGH | YES/NO | Team Name |

### Consumers Impacted
1. **Consumer 1**
   - Impact: Description of impact
   - Migration Effort: X hours/days
   - Owner: Team Name

2. **Consumer 2**
   - Impact: Description of impact
   - Migration Effort: X hours/days
   - Owner: Team Name

### Breaking Change Analysis (if applicable)
- **Total Consumers**: X
- **Affected Consumers**: Y
- **Migration Complexity**: Low | Medium | High
- **Estimated Total Migration Effort**: X hours

## Implementation Plan

### Phase 1: Preparation (Days 1-14)
- [ ] Create ECR (Engineering Change Request)
- [ ] Document migration guide
- [ ] Notify all affected stakeholders
- [ ] Create sample data for testing

### Phase 2: Implementation (Days 15-30)
- [ ] Register new schema version
- [ ] Update ingestion pipelines
- [ ] Deploy to staging environment
- [ ] Test with sample data

### Phase 3: Migration (Days 31-120)
- [ ] Create new topic/dataset (if breaking change)
- [ ] Enable dual-publish (v1 and v2)
- [ ] Notify consumers to begin migration
- [ ] Monitor migration progress
- [ ] Support consumer migrations

### Phase 4: Deprecation (Days 121+)
- [ ] Mark old version as DEPRECATED
- [ ] Stop dual-publish (if applicable)
- [ ] Archive old version after 1 year

### Rollback Plan
If issues arise:
1. Revert to previous schema version
2. Notify consumers of rollback
3. Investigate root cause
4. Revise RFC and retry

## Migration Guide for Consumers

### For Breaking Changes
```language
# Example migration code
# Before (v1):
old_code_example()

# After (v2):
new_code_example()
```

### For Backward-Compatible Changes
```language
# No changes required for existing consumers
# New field available: field_name
# Access new field: data.field_name (will be null for old data)
```

## Testing Plan

### Unit Tests
- [ ] Schema validation tests
- [ ] Compatibility tests
- [ ] Serialization/deserialization tests

### Integration Tests
- [ ] End-to-end pipeline tests
- [ ] Consumer integration tests
- [ ] Performance tests

### Acceptance Criteria
- All tests pass
- No increase in error rate
- Latency within SLA
- Data quality metrics maintained

## Risks and Mitigation

### Risk 1: [Risk Description]
- **Likelihood**: Low | Medium | High
- **Impact**: Low | Medium | High
- **Mitigation**: Mitigation strategy

### Risk 2: [Risk Description]
- **Likelihood**: Low | Medium | High
- **Impact**: Low | Medium | High
- **Mitigation**: Mitigation strategy

## Communication Plan

### Stakeholders to Notify
- [ ] Data Steward
- [ ] Affected consumer teams
- [ ] CCB (for breaking changes)
- [ ] Security team (if data classification changes)

### Notification Timeline
- Day 0: RFC submitted
- Day 7: CCB review (if required)
- Day 14: Implementation begins
- Day 30: Migration period starts
- Day 120: Deprecation notice
- Day 365: Archive old version

### Communication Channels
- [ ] Email to affected teams
- [ ] Slack announcement (#data-engineering)
- [ ] Confluence page updated
- [ ] Monthly engineering newsletter

## Approval

### Required Approvals
- [ ] Data Steward: __________________ Date: __________
- [ ] Schema Owner: __________________ Date: __________
- [ ] CCB Chair (for breaking changes): __________________ Date: __________
- [ ] Security Officer (if classification changes): __________________ Date: __________

### ECR/ECO Reference
ECR ID: ECR-YYYY-XXXX (if applicable)
ECO ID: ECO-YYYY-XXXX (assigned after approval)

## Post-Implementation Review

### Success Metrics
- All consumers migrated successfully
- No production incidents related to change
- Data quality metrics maintained
- SLA compliance maintained

### Lessons Learned
(To be filled after implementation)
- What went well
- What could be improved
- Recommendations for future changes

## Related Documents
- Schema Registry: ../02-DATA_INGESTION/SCHEMA_REGISTRY/
- Configuration Management: ../07-INTEGRATIONS/CONFIG_MGMT_LINKS.md
- Data Contracts: ../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/

## Change History
| Version | Date       | Changes                | Author      |
|---------|------------|------------------------|-------------|
| 1.0     | YYYY-MM-DD | Initial RFC submitted  | Requestor   |
