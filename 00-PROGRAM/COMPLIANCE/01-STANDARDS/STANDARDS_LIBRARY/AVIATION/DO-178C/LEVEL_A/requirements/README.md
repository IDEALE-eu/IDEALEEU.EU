# requirements/ — README

## Purpose

Level A software requirements with full, bidirectional trace to design, code, tests, and coverage.

## Scope / DAL

* DAL: A (DO-178C)
* Applies to HLRs, LLRs, and derived requirements
* Includes DO-330/DO-331/DO-333 references where used

## Layout

* `high/` — HLRs (system → software)
* `low/` — LLRs (implementation-ready)
* `derived/` — requirements not directly from system
* `interfaces/` — ICDs, data models
* `constraints/` — timing, partitioning, HW/SW assumptions
* `schemas/` — JSON/YAML schemas for reqs and trace
* `coverage/` — MC/DC and unit coverage artifacts keyed by ReqID
* `reviews/` — signed review records per ID
* `changes/CR-*/` — change packages and CCB minutes
* `TRACE.md` — traceability matrix (HLR→LLR→Design→Code→Test)

## IDs

* HLR: `HLR-XXXX`
* LLR: `LLR-XXXX`
* Derived: append `-D` (e.g., `LLR-0123-D`)
* Regex: `^HLR-\d{4}$`, `^LLR-\d{4}(-D)?$`

## Authoring rules

* Use a single “shall” sentence per requirement. No “should/may.”
* Necessary, unambiguous, measurable, and verifiable.
* Numeric ranges include units and tolerances. Timing includes jitter and modes.
* No TBD/TBC at release.
* No orphans: every HLR links to ≥1 test; every LLR links to design and code.
* Derived reqs include system impact, safety assessment, and CR/CCB link.
* MC/DC coverage required for all LLR-tested decisions.
* Bidirectional trace is mandatory and kept current.

## File template

Each requirement is one file named by its ID.

```yaml
# HLR-0001 — <Title>

DAL: A
SafetyImpact: <Catastrophic|Hazardous|Major|Minor|NoEffect>
Source:
  System: SYS-xxxx
  Hazard: HAZ-xxxx
Rationale: <why>
Statement: "<single verifiable SHALL sentence>"
Assumptions: [<explicit assumptions>]
Constraints:
  Modes: [<mode-ids>]
  Timing:
    Deadline_ms: <number>
    Jitter_ms: <number>
  Ranges:
    <parameter>: {min: <>, max: <>, units: "<>"}
Interfaces:
  Inputs: [IF-xxx]
  Outputs: [IF-yyy]
Verification:
  Method: [Analysis|Review|Test]
  Tests: [TST-1234, TST-5678]
  Coverage:
    MC_DC_Report: COV-xxxx
    LinksLLR: [LLR-0123]
Links:
  Parents: [SYS-xxxx]
  Children: [LLR-0123, LLR-0456]
  Design: [DES-0007]
  Code: ["src/module/file.c:120-168"]
  Change: CR-2025-00xx
Status: <Draft|Baselined|Changed>
History:
  - {version: 1.0, date: 2025-10-22, change: "initial baseline", by: "<name>"}
Approvals:
  Owner: <name>, created: 2025-10-22
  Reviewer: <independent name>, date: 2025-10-22
  Approver: <name>, date: 2025-10-22
```

## TRACE.md

Columns:
`ReqID | Type(HLR/LLR/DRV) | ParentIDs | DesignIDs | CodeRefs | TestIDs | Coverage(MC/DC %) | Status | CR | Notes`

Rules:

* Update `TRACE.md` in the same commit as any req change.
* 100% HLR→Test and LLR→Code closure before baseline.

## Reviews

Independent review required for every HLR and LLR.

**HLR checklist**

* Rationale present
* Single SHALL statement
* Numeric bounds with units and tolerances
* Verification method defined
* System and safety links present
* Independence of reviewer

**LLR checklist**

* Implementation-ready detail
* Interface contracts defined
* Timing and failure handling specified
* Code path references present
* Test design references present
* MC/DC plan present

## CI lints

* Validate IDs by regex.
* Enforce “shall” in `Statement`; reject TBD/TBC.
* Schema-validate every req file (`schemas/req.schema.json`).
* Fail if any HLR lacks ≥1 test or any LLR lacks ≥1 code ref.
* Parse coverage reports; assert MC/DC = 100% for DAL A items under test.
* Fail if `TRACE.md` not updated with req changes.

## Entry / Exit

**Entry:** PSAC, SDP, SVP, SQAP, SCMP approved; tool qualification applied as needed.
**Exit:** HLR/LLR baselined; 100% HLR→Test and LLR→Code closed; MC/DC 100% or justified; reviews logged; TRACE.md current.

## Notes

* Use DO-178C terminology consistently.
* If code is deactivated, document the control mechanism and justification.

