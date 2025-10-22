# high/ — HLRs

## Purpose

Store Level A High-Level Requirements with full trace to LLRs, design, code, tests, and coverage.

## Related

* Parent index: [../README.md](../README.md)
* LLRs: [../low/](../low/)
* Derived reqs: [../derived/](../derived/)
* Interfaces: [../interfaces/](../interfaces/)
* Constraints: [../constraints/](../constraints/)
* Schemas: [../schemas/](../schemas/)
* Coverage: [../coverage/](../coverage/)
* Reviews: [../reviews/](../reviews/)
* Changes: [../changes/](../changes/)
* Trace matrix: [../TRACE.md](../TRACE.md)

## IDs and files

* ID: `HLR-XXXX`
* Filename: `HLR-XXXX.yaml` (one requirement per file)
* Regex: `^HLR-\d{4}$`

## Authoring rules

* One SHALL sentence per requirement. No “should/may”.
* Necessary, unambiguous, measurable, and verifiable.
* Include numeric bounds with units and tolerances.
* Timing includes deadlines and jitter per mode.
* No TBD/TBC at release.
* Each HLR links to ≥1 LLR and ≥1 verification case.
* Bidirectional trace kept current in [../TRACE.md](../TRACE.md).

## Template

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
Links:
  ChildrenLLR: [LLR-0123, LLR-0456]
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

## Reviews

* Independent review for every HLR.
* Reject if rationale, SHALL statement, numeric bounds, verification method, or safety links are missing.
* Store records in [../reviews/](../reviews/).

## CI checks

* ID regex and filename match.
* Schema validation: [../schemas/req.schema.json](../schemas/req.schema.json).
* Enforce “shall” in `Statement`; forbid TBD/TBC.
* Require ≥1 test and ≥1 child LLR link.
* Update [../TRACE.md](../TRACE.md) in same commit as any change.

## Entry / Exit

* **Entry:** PSAC, SDP, SVP, SQAP, SCMP approved.
* **Exit:** HLRs baselined; 100% HLR→Test and HLR→LLR trace closed; MC/DC evidence referenced where applicable; reviews logged; [../TRACE.md](../TRACE.md) current.

