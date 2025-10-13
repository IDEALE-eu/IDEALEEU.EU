# RFC — Request for Change Documents

## Purpose

Request for Change (RFC) documents proposing modifications to the CENTER-BODY integration design before formal approval.

## Content Types

- **RFC Forms** — Standardized change request documentation
- **Technical Justifications** — Engineering rationale for changes
- **Impact Analyses** — Assessment of change effects
- **Cost/Schedule Impacts** — Resource requirement estimates

## File Formats

- `.pdf` — RFC forms and supporting documentation
- `.xlsx` — Impact analysis worksheets
- `.docx` — Technical justification reports

## Naming Convention

```
RFC_{number}_{brief_description}_v{version}.{ext}
```

Examples:
- `RFC_001_wing_attach_mod_v001.pdf`
- `RFC_015_harness_reroute_impact_v002.xlsx`

## Cross-References

- [Parent: CHANGE_CONTROL](../README.md)
- [ECO Process](../ECO/README.md)
- [Review Artifacts](../../REVIEWS/)

## RFC Process

1. **Initiation** — Problem identified or improvement proposed
2. **RFC Submittal** — Formal request with justification
3. **Initial Review** — Integration lead assessment
4. **Impact Analysis** — Multi-discipline evaluation
5. **Disposition** — Approve, reject, or defer
6. **ECO Creation** — If approved, create formal ECO

## RFC Content Requirements

Each RFC must include:
- **Description**: Clear statement of proposed change
- **Justification**: Why change is needed
- **Impact Analysis**: Affected systems, interfaces, documents
- **Cost/Schedule**: Resource and timing implications
- **Alternatives**: Other options considered
- **Recommendation**: Proposed disposition

## Approval Authority

- **Minor changes**: Integration lead
- **Moderate changes**: Chief engineer
- **Major changes**: Program manager + CCB

## Change Control

RFCs are tracked but not version controlled until approved and converted to ECO.
