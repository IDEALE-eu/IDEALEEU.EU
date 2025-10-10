# CMP · 21-10_RADIATORS_HEAT_EXCHANGERS
Authoritative **compliance & certification evidence** for radiators, embedded heat-pipe radiators, liquid plate heat exchangers (LPHX), coldplates, mounts, TIM/bondlines, and coating stacks. No source code. No flight SW.

---

## Scope & Objectives
- Demonstrate conformity to requirements and standards for **design, materials, special processes, inspection, and test**.
- Preserve court-grade traceability from **requirement → verification method → evidence → release**.
- Q-baseline: **Q10**.

---

## Evidence Types (owned by CMP)
- **Requirements & Traceability:** RTM, VCRM, verification matrix, NCR/waiver linkage.
- **Standards Applicability:** SAM with compliance statements, deviations, waivers.
- **Analyses:** thermal, structural, reliability, safety (FMEA/FTA) summaries referencing detailed models in CAE.
- **Test Evidence Links:** certified references to CAV artifacts (TVAC, leak/proof/burst, vibration/shock, coating optical).
- **Materials & Processes:** outgassing, cleanliness, conformity of adhesives/TIM/coatings; special-process qualifications (bond/braze/coat/clean).
- **Certificates:** CoC, calibration references, special-process approvals, supplier qualifications.
- **Reports:** design compliance report, qualification report (QR), acceptance report (ATR/ATP).
- **Audits & Releases:** internal/external audit findings, IEF manifests, digital signatures and checksums.

---

## Layout
```
CMP/
├─ requirements/
│  ├─ rtm/                       # Requirement Traceability Matrix
│  ├─ vcrm/                      # Verif. Cross-Reference Matrix
│  └─ verification_matrix/       # Method vs. Req (A/T/I/D)
├─ standards/
│  ├─ applicability_matrix/      # ECSS/NASA/ISO mapping & clauses
│  ├─ deviations_waivers/        # DW/NCR with risk sign-off
│  └─ refs/                      # Normative references (IDs only)
├─ analyses/
│  ├─ thermal/                   # budgets, margins, correlation summaries
│  ├─ structural/                # stress, flatness, stiffness reports
│  ├─ reliability/               # FMEA/FTA, MTBF, criticality
│  └─ safety/                    # hazard analysis, FMEA, single-point failures
├─ test_evidence/
│  ├─ tvac/                      # refs to CAV, acceptance criteria met
│  ├─ leak_proof_burst/          # He leak, proof, burst certs
│  ├─ vib_shock/                 # sine/random/shock reports
│  ├─ thermal_perf/              # coldplate ∆T-Q, SER validation
│  ├─ flow_dp/                   # hydraulic characterization
│  └─ coating_optical/           # α/ε certs, thickness, durability
├─ materials_processes/
│  ├─ outgassing/                # CVCM/TML per ASTM E595
│  ├─ cleanliness/               # NVR/particle, bake-out logs
│  ├─ adhesives_tim/             # datasheets, cure logs, witness coupons
│  ├─ coatings/                  # paint/SSM specs, α/ε targets, thickness
│  └─ special_process_quals/     # weld/braze/bond operator certs
├─ certificates/
│  ├─ coc/                       # Certificates of Conformity (supplier)
│  ├─ calibration/               # sensor/gage cal chains
│  └─ approvals/                 # MRB, process approvals, waivers
├─ reports/
│  ├─ design_compliance/         # DCR: req vs design evidence
│  ├─ qualification/             # QR: proto/qual unit results
│  ├─ acceptance/                # ATR/ATP: flight unit sign-off
│  └─ final_data_pack/           # IEF manifest, SHA256 checksums
├─ audits/
│  ├─ internal/                  # peer reviews, gate reviews
│  └─ external/                  # customer/agency audits, findings
├─ ncr_waivers/                  # non-conformance, deviations, dispositions
└─ templates/                    # RTM, VCRM, report templates
```

---

## Naming & revisions
`21-10-CMP_<artifact>__rNN__{WIP|RVW|REL}.*`  
Examples:  
- `21-10-CMP-RTM-radiators__r03__REL.xlsx`  
- `21-10-CMP-QR-coldplate__r02__RVW.pdf`  
- `21-10-CMP-IEF-manifest__r01__REL.json`

---

## Requirement Traceability (RTM)
- **Parent Req ID:** from SRD/SSRD (e.g., `STA-B-21-10-THM-001`).
- **Derived Req:** design/process requirements (CAD, CAE, CAP).
- **Verification Method:** A (analysis), T (test), I (inspection), D (demonstration).
- **Evidence Location:** pointer to CAE model, CAV test report, CAI inspection log.
- **Status:** Open / In-Progress / Verified / Accepted.
- **NCR/Waiver:** cross-ref if non-conformance or deviation approved.

## Standards Applicability Matrix (SAM)
- **Standard:** ECSS-E-ST-10-03C, NASA-STD-5001, ISO 1101, etc.
- **Clause:** specific section/requirement.
- **Applicability:** Full / Partial / Not Applicable.
- **Compliance Statement:** how requirement is met (ref to CAD, CAE, CAV, CAP).
- **Deviations:** if tailored; link to waiver/DRB decision.

## Verification Methods
- **A (Analysis):** CAE thermal/structural models (refs in `analyses/`).
- **T (Test):** TVAC, leak, vib, flow (refs in `test_evidence/` → CAV).
- **I (Inspection):** dimensional, visual, NDT (refs in CAI checklists).
- **D (Demonstration):** functional checks, pressure tests (refs in CAV/CAI).

---

## Materials & Process Compliance

### Outgassing (ASTM E595)
- **Requirement:** CVCM ≤ 0.1%, TML ≤ 1.0%.
- **Evidence:** test reports per material; certs in `materials_processes/outgassing/`.

### Cleanliness (NVR/Particle)
- **Requirement:** per contamination control plan (e.g., Level 100A).
- **Evidence:** wipe samples, particle counts; logs in `materials_processes/cleanliness/`.

### Adhesives/TIM
- **Requirement:** approved materials list; shelf-life, storage, cure per datasheet.
- **Evidence:** datasheets, cure logs, DSC/pull test on witness coupons.

### Coatings
- **Requirement:** α/ε targets (e.g., α ≤ 0.15, ε ≥ 0.85 for white paint).
- **Evidence:** spectrophotometer data on witness coupons; thickness measurements.

### Special Process Qualifications
- **Requirement:** operators cert'd per NASA-STD-8739 (welding), IPC-A-610 (assembly).
- **Evidence:** cert copies in `materials_processes/special_process_quals/`.

---

## Reports

### Design Compliance Report (DCR)
- **Content:** req-by-req evidence; analysis/test/inspection summary; margin assessment.
- **Sign-off:** chief engineer, quality, customer (if required).
- **Location:** `reports/design_compliance/`.

### Qualification Report (QR)
- **Content:** proto/qual unit test results; correlation to predictions; lessons learned.
- **Sign-off:** test lead, thermal lead, program manager.
- **Location:** `reports/qualification/`.

### Acceptance Test Report (ATR)
- **Content:** flight unit acceptance test results; ATP execution; pass/fail per criteria.
- **Sign-off:** test lead, quality, configuration control.
- **Location:** `reports/acceptance/`.

### Final Data Package (IEF)
- **Content:** manifest of all deliverables (CAD STEP, drawings, reports, certs); SHA256 checksums.
- **Delivery:** customer portal upload; hard-copy if required.
- **Location:** `reports/final_data_pack/`.

---

## Audits & Non-Conformances

### Internal Audits
- **Peer Reviews:** design reviews (PDR/CDR); findings tracked.
- **Gate Reviews:** qual/accept gates; go/no-go decisions.
- **Evidence:** minutes, action items, closure evidence in `audits/internal/`.

### External Audits
- **Customer/Agency:** on-site audits; findings, CARs (Corrective Action Requests).
- **Closure:** root cause, corrective action, verification; logs in `audits/external/`.

### NCR/Waivers
- **NCR:** non-conformance report; disposition (use-as-is, rework, scrap).
- **Waiver:** approved deviation from requirement; risk acceptance by authority.
- **Evidence:** NCR form, disposition rationale, MRB sign-off in `ncr_waivers/`.

---

## Release & Configuration Control
- **Baseline:** Q10 locked at acceptance; config-controlled in PDM/PLM.
- **Changes:** ECN (Engineering Change Notice) process; re-verify affected reqs.
- **Digital Signatures:** PDF sign-offs; checksums for file integrity.
- **Archival:** long-term retention per records management plan (e.g., 20+ years).
