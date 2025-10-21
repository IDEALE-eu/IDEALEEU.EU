# DO-178C Level A – README

## Purpose
Holds Level A compliance evidence and controls for the item under certification. Centralizes plans, development baselines, verification results, coverage, CM/QA records, and certification artifacts.

## Scope
- Highest DAL (A): catastrophic failure condition
- Full independence for verification and QA
- Structural coverage to MC/DC with gap justifications
- Tool qualification as required (DO-330)
- Partitioning evidence if hosted on IMA

## Layout

- [planning/](./planning/) — PSAC, SDP, SVP, SQAP, SCMP
- [requirements/](./requirements/) — high/low-level, trace IDs
- [design/](./design/) — HLD/LLD, interfaces, partitioning assumptions
- [source/](./source/) — tagged code baseline(s)
- [verification/](./verification/) — procedures, results, defects, coverage, mcdc_justification/
- [tools/](./tools/) — DO-330 plans/evidence
- [cm/](./cm/) — baselines, CCB minutes, PR/CR logs
- [qa/](./qa/) — audits, reviews, independence records
- [certification/](./certification/) — SAS, CI, SOI minutes, checklists

## Entry points
- **Plan set:** [planning/PSAC.md](./planning/PSAC.md)
- **Traceability index:** [requirements/TRACE.md](./requirements/TRACE.md)
- **Verification index:** [verification/INDEX.md](./verification/INDEX.md)
- **Certification index:** [certification/SAS.md](./certification/SAS.md)

## Required objectives (Level A)
- Plans approved and baselined: PSAC, SDP, SVP, SQAP, SCMP
- Requirements-based verification with independence
- Reviews/analysis complete across req/design/code/tests
- Structural coverage: 100% statement, decision, and MC/DC at item level
- Problem reporting and CM under CCB control
- QA surveillance and acceptance records
- Tool qualification evidence where tools automate verification or can insert errors
- Platform/partitioning evidence if applicable

## Evidence checklist
- ✅ Plans (PSAC/SDP/SVP/SQAP/SCMP)
- ✅ Req/design/code baselines with trace to tests
- ✅ Test procedures + results + anomalies
- ✅ Coverage reports + MC/DC justification
- ✅ PR/CR logs + CCB minutes
- ✅ QA audits/reports + independence matrix
- ✅ Tool qual (DO-330) data
- ✅ SAS + Configuration Index + SOI minutes

## Gating
- **FCR-1:** Plans approved, traceability established, test environment qualified
- **FCR-2:** All objectives met, anomalies dispositioned, SAS ready for authority review

## Naming/trace rules
- Use stable IDs: `REQ-XXXX`, `DES-XXXX`, `TST-XXXX`, `PR-XXXX`
- One source of truth per artifact. Cross-link rather than duplicate
- All binaries and reports must include hash, date, and baseline tag

## Reproducibility
- Record build env and commit SHA in each report footer
- Capture coverage tool versions and options
- Store generated artifacts under `verification/` or `certification/` with immutable filenames

## Contacts
- **Dev Lead:** …
- **IV&V Lead (independent):** …
- **QA:** …
- **CM/CCB Chair:** …



