# Architecture Decision Records (ADRs)

**Baseline**: GenSTD-[TIER]-YYYY-NNNN  
**Source OtC**: OtC-[phase]-YYYY-NNNN

---

## Decision Format

Each decision should follow this format:

### [Decision Title]

**Date**: YYYY-MM-DD  
**Owner**: [Name and role]  
**Status**: [Accepted / Rejected / Superseded]

**Context**: [What is the situation requiring this decision?]

**Decision**: [What was decided?]

**Alternatives Considered**:
1. [Alternative 1] - Rejected because [reason]
2. [Alternative 2] - Rejected because [reason]
3. [Alternative 3] - Rejected because [reason]

**Rationale**: [Why was this decision made? What factors were most important?]

**Consequences**: [What are the implications of this decision? Trade-offs?]

**Related**: [Links to other decisions, RFCs, or ECOs]

---

## Decisions

### [Decision 1 Title]

**Date**: YYYY-MM-DD  
**Owner**: [Name], [Role]  
**Status**: Accepted

**Context**: 
[Describe the context and problem]

**Decision**: 
[State the decision clearly]

**Alternatives Considered**:
1. **[Alternative A]**: Rejected - [reason]
2. **[Alternative B]**: Rejected - [reason]
3. **[Alternative C]**: Rejected - [reason]

**Rationale**: 
[Explain why this was the best choice]

**Consequences**: 
- Positive: [benefit 1], [benefit 2]
- Negative: [trade-off 1], [trade-off 2]
- Neutral: [consideration 1]

**Related**: RFC-YYYY-NNN, ECO-YYYY-NNN

---

### [Decision 2 Title]

**Date**: YYYY-MM-DD  
**Owner**: [Name], [Role]  
**Status**: Accepted

[Follow same format as above]

---

## Decision Index

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| D001 | [Decision 1] | YYYY-MM-DD | Accepted | [Name] |
| D002 | [Decision 2] | YYYY-MM-DD | Accepted | [Name] |
| D003 | [Decision 3] | YYYY-MM-DD | Superseded | [Name] |

---

## Notes

- All decisions must include at least 2 rejected alternatives
- Document why each alternative was rejected
- Link to relevant RFCs, ECOs, or technical analyses
- Update status if a decision is later superseded
- Keep this log current as the baseline evolves

---

*For more on decision-making process, see [CM Plan](../../01-CM_PLAN.md) and [CCB Process](../../05-CCB/README.md).*
