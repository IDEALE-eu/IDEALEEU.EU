# derived/ — Derived Requirements

## Purpose

Store Level A **derived** requirements not directly allocated from system, with full trace to HLR/LLR, design, code, tests, hazards, and CCB changes.

## Related

* Parent index: [../README.md](../README.md)
* HLRs: [../high/](../high/) · LLRs: [../low/](../low/)
* Interfaces: [../interfaces/](../interfaces/) · Constraints: [../constraints/](../constraints/)
* Schemas: [../schemas/](../schemas/) · Coverage: [../coverage/](../coverage/)
* Reviews: [../reviews/](../reviews/) · Changes: [../changes/](../changes/)
* Trace matrix: [../TRACE.md](../TRACE.md)

## IDs and files

* IDs: `HLR-XXXX-D` or `LLR-XXXX-D`
* Filename: `HLR-XXXX-D.yaml` or `LLR-XXXX-D.yaml` (one requirement per file)
* Regex: `^HLR-\d{4}-D$` · `^LLR-\d{4}-D$`

## Authoring rules

* One SHALL sentence. No “should/may”.
* Include justification for why system did not specify it.
* Provide impact analysis: system, safety, ICDs, performance, resources, verification.
* Link a **change request** and CCB decision.
* Update hazards and assumptions as needed.
* Trace to affected HLR/LLR, design, code, and tests.
* No TBD/TBC. Numeric bounds have units and tolerances. Timing has deadlines and jitter.
* Keep bidirectional trace current in [../TRACE.md](../TRACE.md).

## Template

```yaml
# LLR-0123-D — <Title>         # or HLR-0123-D

DAL: A
Type: <HLR|LLR>
SafetyImpact: <Catastrophic|Hazardous|Major|Minor|NoEffect>

DerivedFrom:
  Reason: <Constraint|DesignChoice|Optimization|Performance|Compliance|TestFinding|SafetyMitigation>
  Evidence: ["link to analysis/test/design showing need"]

Rationale: <why system allocation was insufficient>
Statement: "<single verifiable SHALL sentence>"

Assumptions: [<explicit assumptions>]
Constraints:
  Modes: [<mode-ids>]
  Timing:
    Deadline_ms: <number>
    Jitter_ms: <number>
  Ranges:
    <parameter>: {min: <>, max: <>, units: "<>"}

InterfacesImpact:
  ChangedICDs: [IF-xxx]
  NewSignals: [{name: <>, units: "<>", rate_hz: <>, range: {min: <>, max: <>}}]

ImpactAssessment:
  SystemImpact: "<text and SYS-ids if updates proposed>"
  SafetyImpactChange: "<hazard/state changes>"
  PerformanceImpact: "<latency/CPU/RAM/stack deltas>"
  VerificationImpact: "<new/updated tests, analyses>"

Verification:
  Method: [Analysis|Review|Test]
  Tests: [TST-1234, TST-5678]
  Coverage:
    Unit: {lines_pct: <>, branches_pct: <>}
    MC_DC_Report: COV-xxxx
  Regression: ["impacted test suites"]

Links:
  RelatedHLR: [HLR-xxxx]              # when Type=LLR
  RelatedLLR: [LLR-xxxx]              # when Type=HLR
  Design: [DES-0007]
  Code:
    - "src/module/file.c:120-168"
  Hazard: [HAZ-xxxx]
  Change: CR-2025-00xx                 # must exist under ../changes/
  CCBMinutes: ["../changes/CR-2025-00xx/CCB.md"]

Status: <Draft|Baselined|Changed>
History:
  - {version: 1.0, date: 2025-10-22, change: "initial baseline", by: "<name>"}
Approvals:
  Owner: <name>, created: 2025-10-22
  Reviewer: <independent name>, date: 2025-10-22
  SafetyReviewer: <name>, date: 2025-10-22
  Approver: <name>, date: 2025-10-22
```

## Reviews

* Independent review plus safety review for every derived req.
* Reject if missing CR/CCB link, impact assessment, SHALL statement, numeric bounds, or verification plan.
* Store records in [../reviews/](../reviews/).

## CI checks

* ID regex and filename match.
* Schema validation: [../schemas/req.schema.json](../schemas/req.schema.json).
* Require `Change` and `CCBMinutes` links.
* For Type=LLR, require `RelatedHLR`; for Type=HLR, require `RelatedLLR`.
* No TBD/TBC. Enforce “shall” in `Statement`.
* Require ≥1 design ref, ≥1 code ref, and ≥1 test.
* Update [../TRACE.md](../TRACE.md) in the same commit.

## Entry / Exit

* **Entry:** PSAC, SDP, SVP, SQAP, SCMP approved; CR opened.
* **Exit:** CCB approved; hazards updated; trace closed to HLR/LLR, design, code, and tests; MC/DC evidence linked; reviews logged; [../TRACE.md](../TRACE.md) current.
