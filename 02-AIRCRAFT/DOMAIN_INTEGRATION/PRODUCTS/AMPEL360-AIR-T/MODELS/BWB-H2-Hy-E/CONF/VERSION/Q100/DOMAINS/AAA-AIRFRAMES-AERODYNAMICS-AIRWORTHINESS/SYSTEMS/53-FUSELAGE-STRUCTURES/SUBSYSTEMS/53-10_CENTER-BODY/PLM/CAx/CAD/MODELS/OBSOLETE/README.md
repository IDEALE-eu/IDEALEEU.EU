# OBSOLETE — Obsolete and Superseded Models

## Purpose

This directory serves as an archive for CAD models that are no longer current but must be retained for historical reference, traceability, and configuration management purposes.

## What Belongs Here

Models that are:
- **Superseded**: Replaced by newer revisions
- **Abandoned**: Design concepts not pursued
- **Obsolete**: No longer applicable to current configuration
- **Historical**: Needed for reference only
- **Archived**: End-of-life but retained for records

## Why Keep Obsolete Models

Obsolete models are retained for:
- **Traceability**: Historical design decisions
- **Investigations**: Failure analysis, incident investigation
- **Compliance**: Regulatory record-keeping requirements
- **Reference**: Learning from past designs
- **Configuration**: As-built vs. as-designed documentation
- **Legal**: Product liability records

## Organization

Organize obsolete models by:
- **Supersession date**: When model became obsolete
- **Part type**: Original category (frame, skin, etc.)
- **Reason**: Why obsolete (superseded, abandoned, etc.)

## Naming Convention

Obsolete models retain original name with suffix:
```
<ORIGINAL-NAME>_OBS-<DATE>_<REASON>.<ext>
```

Examples:
- `53-10_FRAME_FR-001_v01_OBS-20240115_SUPERSEDED.CATPart`
- `53-10_CONCEPT_DESIGN-A_OBS-20240120_ABANDONED.prt`
- `53-10_SKIN-PANEL_SP-003_r01_OBS-20240125_CONFIG-CHANGE.sldprt`

## Obsolescence Reasons

Common obsolescence reasons:
- **SUPERSEDED**: New revision or redesign released
- **ABANDONED**: Design concept not pursued
- **CONFIG-CHANGE**: Configuration change made design obsolete
- **REQUIREMENTS-CHANGE**: Requirements change invalidated design
- **TEST-FAILURE**: Failed qualification testing
- **COST**: Design not cost-effective
- **WEIGHT**: Did not meet weight targets
- **MANUFACTURABILITY**: Manufacturing issues

## Metadata

Include obsolescence metadata:
- **Obsolete date**: When model became obsolete
- **Reason**: Why obsolete
- **Superseded by**: Replacement model (if applicable)
- **Effectivity**: Serial numbers/dates where used
- **Notes**: Additional context

## Retention Policy

Obsolete models are retained:
- **Minimum retention**: As required by regulation/contract
- **Typical retention**: Life of aircraft program + 20 years
- **Critical items**: Indefinite retention
- **Review**: Periodic review for continued necessity

## Access

Obsolete models:
- Clearly marked as obsolete
- Read-only access
- Not to be used for new designs
- Available for reference only
- May be archived to long-term storage

## Preventing Misuse

To prevent use of obsolete models:
- Clear obsolescence markings
- Watermarks on views/drawings
- Separate directory location
- Documentation of status
- User notifications

## Migration to Archive

Eventually, obsolete models may:
- Be compressed for long-term storage
- Be moved to deep archive
- Be migrated to neutral formats (STEP, IGES)
- Have reduced metadata
- Be stored off-site

## Related Documentation

- **Released models**: [`../RELEASED/`](../RELEASED/)
- **Current parts**: [`../PARTS/`](../PARTS/)
- **Configuration records**: [`../../../../../../../../00-PROGRAM/CONFIG_MGMT/`](../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Change history**: PLM system change records

## Documentation Requirements

When moving models to OBSOLETE/:
- [ ] Document obsolescence reason
- [ ] Note superseding model (if any)
- [ ] Update configuration records
- [ ] Notify affected stakeholders
- [ ] Create obsolescence record
- [ ] Update EBOM/MBOM

## Quality Records

Maintain with obsolete models:
- Original design rationale
- Test results (if any)
- Review records
- Approval documentation
- Issue/discrepancy records
- Lessons learned

## Search and Retrieval

Obsolete models should be:
- Indexed for searchability
- Tagged with keywords
- Linked to configuration items
- Documented in archive catalog
- Retrievable when needed

## Legal and Compliance

Obsolete models support:
- Product liability defense
- Regulatory compliance
- Audit trails
- Certification basis
- Type certificate amendments
