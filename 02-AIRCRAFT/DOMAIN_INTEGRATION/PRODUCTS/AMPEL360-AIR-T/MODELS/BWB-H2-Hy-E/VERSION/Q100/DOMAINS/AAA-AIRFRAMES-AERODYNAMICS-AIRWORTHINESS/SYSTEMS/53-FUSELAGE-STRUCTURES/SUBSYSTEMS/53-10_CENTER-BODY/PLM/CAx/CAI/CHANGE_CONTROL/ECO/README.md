# ECO — Engineering Change Orders

## Purpose

Formal Engineering Change Orders (ECOs) documenting approved modifications to the CENTER-BODY integration design.

## Content Types

- **ECO Forms** — Formal change order documentation
- **Effectivity Statements** — When/where change applies
- **Implementation Instructions** — How to incorporate change
- **Verification Plans** — Testing and validation requirements

## File Formats

- `.pdf` — ECO package documentation
- `.xlsx` — Effectivity and implementation tracking

## Naming Convention

```
ECO_{number}_{brief_description}_v{version}.{ext}
```

Examples:
- `ECO_0001_wing_attach_reinforcement_v001.pdf`
- `ECO_0025_ewis_routing_update_v001.xlsx`

## Cross-References

- [Parent: CHANGE_CONTROL](../README.md)
- [RFC Documents](../RFC/README.md)
- [Review Artifacts](../../REVIEWS/)
- [Interface Matrix](../../INTERFACE_MATRIX/README.md)

## ECO Process

1. **RFC Approval** — Approved RFC becomes ECO
2. **ECO Creation** — Formal package prepared
3. **CCB Review** — Configuration Control Board approval
4. **Implementation** — Changes incorporated
5. **Verification** — Testing and validation
6. **Closure** — ECO closed after verification

## ECO Package Contents

- ECO form (identification, description, justification)
- Affected documents list
- Effectivity statement (serial numbers, dates)
- Drawing changes (redlines or updated drawings)
- Implementation instructions
- Verification/test requirements
- Approval signatures

## Effectivity Management

Changes may be:
- **Immediate**: All future builds
- **Retrofit**: Existing aircraft modified
- **Conditional**: Based on specific criteria
- **Deferred**: Implemented at specific milestone

## Change Control

ECOs are **configuration controlled**:
- Unique sequential numbering
- Full traceability to RFC
- Approval signatures required
- Implementation tracking mandatory
- Verification sign-off required before closure
