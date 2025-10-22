# low/ — LLRs

## Purpose

Store Level A Low-Level Requirements with full trace to design, code, tests, and coverage.

## Related

* Parent index: [../README.md](../README.md)
* HLRs: [../high/](../high/)
* Derived reqs: [../derived/](../derived/)
* Interfaces: [../interfaces/](../interfaces/)
* Constraints: [../constraints/](../constraints/)
* Schemas: [../schemas/](../schemas/)
* Coverage: [../coverage/](../coverage/)
* Reviews: [../reviews/](../reviews/)
* Changes: [../changes/](../changes/)
* Trace matrix: [../TRACE.md](../TRACE.md)

## IDs and files

* ID: `LLR-XXXX`
* Filename: `LLR-XXXX.yaml` (one requirement per file)
* Regex: `^LLR-\d{4}$`
* Derived requirements live in [../derived/](../derived/) with `-D` suffix.

## Authoring rules

* One SHALL sentence per requirement. No “should/may”.
* Implementation-ready: define inputs, outputs, algorithms, states, errors, and limits.
* Numeric bounds include units and tolerances. Timing includes deadlines and jitter per mode.
* Specify preconditions, postconditions, invariants, and failure handling.
* Define concurrency behavior and shared-resource usage.
* No TBD/TBC at release.
* Each LLR links to ≥1 parent HLR, ≥1 design ref, ≥1 code ref, and ≥1 test.
* MC/DC required for all decision logic verified by test.
* Keep bidirectional trace current in [../TRACE.md](../TRACE.md).

## Template

```yaml
# LLR-0001 — <Title>

DAL: A
SafetyImpact: <Catastrophic|Hazardous|Major|Minor|NoEffect>
ParentsHLR: [HLR-xxxx]
Rationale: <why>
Statement: "<single verifiable SHALL sentence>"
Assumptions: [<explicit assumptions>]

Interfaces:
  Inputs:
    - {name: <>, type: <>, units: "<>", range: {min: <>, max: <>}, rate_hz: <>, mode: [<mode-ids>]}
  Outputs:
    - {name: <>, type: <>, units: "<>", accuracy: <>, latency_ms: <>, mode: [<mode-ids>]}
Constraints:
  Modes: [<mode-ids>]
  Timing:
    Deadline_ms: <number>
    Jitter_ms: <number>
    ExecutionTimeBudget_ms: <number>
  Ranges:
    <parameter>: {min: <>, max: <>, units: "<>"}
  Resources:
    CPU_pct: <number>
    RAM_kB: <number>
    Stack_kB: <number>
Behavior:
  Preconditions: [<conditions>]
  Postconditions: [<conditions>]
  Invariants: [<conditions>]
  FailureHandling: [<deterministic responses, fallbacks, faults>]
  Concurrency: {reentrancy: <Yes/No>, sync: <mutex/lock-free/NA>}
Numerics:
  Precision: <e.g., 1e-6>
  Saturation: <strategy>
  OverflowHandling: <strategy>

Verification:
  Method: [Analysis|Review|Test]
  Tests: [TST-1234, TST-5678]
  Coverage:
    Unit: {lines_pct: <>, branches_pct: <>}
    MC_DC_Report: COV-xxxx

Links:
  Design: [DES-0007]
  Code:
    - "src/module/file.c:120-168"
    - "src/module/file.h:34-65"
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

* Independent review for every LLR.
* Reject if missing parent HLR, SHALL statement, numeric bounds, timing, interfaces, verification, or code/design links.
* Store records in [../reviews/](../reviews/).

## CI checks

* ID regex and filename match.
* Schema validation: [../schemas/req.schema.json](../schemas/req.schema.json).
* Enforce “shall” in `Statement`; forbid TBD/TBC.
* Inputs/outputs reference symbols defined in [../interfaces/](../interfaces/).
* Require ≥1 parent HLR, ≥1 code ref, and ≥1 test.
* Parse coverage; assert MC/DC = 100% where applicable.
* Update [../TRACE.md](../TRACE.md) in same commit as any change.

## Entry / Exit

* **Entry:** PSAC, SDP, SVP, SQAP, SCMP approved.
* **Exit:** LLRs baselined; 100% LLR→Code and HLR→LLR trace closed; tests implemented and passing; MC/DC evidence linked; reviews logged; [../TRACE.md](../TRACE.md) current.
