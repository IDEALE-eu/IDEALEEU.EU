# requirements/ — README

## Purpose
Store Level A software requirements with full trace to design, code, and tests.

## Layout
```

requirements/
high/           # HLRs (system → software)
low/            # LLRs (implementation-ready)
derived/        # requirements not directly from system
interfaces/     # ICDs, data models
constraints/    # timing, partitioning, HW/SW assumptions
TRACE.md        # traceability matrix (HLR→LLR→Design→Code→Test)
schemas/        # req/trace validators

```

## IDs
- HLR: `HLR-XXXX`  
- LLR: `LLR-XXXX`  
- Derived: append `-D` (e.g., `LLR-0123-D`)

## File template
Each requirement is one file named by its ID.
```

# HLR-0001 — <Title>

Rationale: <why>
Statement: <verifiable text>
Constraints: <bounds, modes, timing>
Verification: {Analysis|Review|Test}; Cases: TST-xxxx
Links: Parent SYS-xxxx; Children LLR-xxxx; Design DES-xxxx; Code path:line

```

## Quality rules
- Necessary, unambiguous, measurable, and verifiable.
- Numeric ranges and units mandatory. No TBD at release.
- No orphans: every HLR has tests; every LLR links to design and code.
- Changes via CR/CCB only; update `TRACE.md` on the same day.

## Reviews
Independent review for every HLR/LLR. Reject if missing rationale, bounds, or verification.

## Entry / Exit
- **Entry:** PSAC/SDP approved.  
- **Exit:** HLR/LLR baselined; 100% HLR→Test and LLR→Code trace closed; `TRACE.md` current.
