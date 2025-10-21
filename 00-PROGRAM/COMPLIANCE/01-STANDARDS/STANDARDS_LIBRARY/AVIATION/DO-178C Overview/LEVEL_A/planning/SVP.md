# Software Verification Plan (SVP)

## Purpose
Defines the verification strategy, independence matrix, and coverage objectives for software classified as DO-178C Level A.  
Ensures that all DO-178C objectives are met with documented evidence and full independence between development and verification.

## Scope
Applies to all software components, tools, and artifacts contributing to airborne functionality at DAL A.  
Covers reviews, analyses, and tests from requirements to executable object code.

## Verification Objectives
| Category | Objective | Method | Output |
|-----------|------------|--------|--------|
| **Reviews/Analyses** | Requirements, design, code compliance | Inspection & analysis | Review records |
| **Requirements-based Testing** | Verify HLRs/LLRs | Functional, boundary, and stress tests | Test procedures and results |
| **Structural Coverage** | Ensure code fully exercised | Statement, decision, MC/DC | Coverage reports |
| **Tool Qualification** | Validate tool reliability | DO-330 process | Qualification data |
| **Regression Testing** | Detect unintended effects | Automated reruns | Regression logs |

## Verification Strategy
1. **Planning** – Verification environment defined and tools baselined.  
2. **Reviews** – Independent reviews at each lifecycle stage.  
3. **Analysis** – Static and data-flow checks on all source code.  
4. **Testing** – Unit, integration, and system tests executed in controlled environments.  
5. **Coverage Measurement** – MC/DC analysis with justifications for any infeasible conditions.  
6. **Traceability** – Bidirectional trace from system requirement to test case and result.  
7. **Regression and Anomaly Tracking** – All anomalies logged and retested after correction.  

## Independence Matrix
| Activity | Performer | Independent From | Evidence |
|-----------|------------|------------------|-----------|
| Requirements review | Verification Engineer | Requirements Author | Review record |
| Design review | IV&V | Design Engineer | Design review checklist |
| Code review | IV&V | Developer | Code review log |
| Test procedure creation | IV&V | Developer | Test case document |
| Test execution | IV&V / QA | Developer | Test report |
| QA audits | QA | Dev/Verification | Audit report |

## Verification Levels
| Level | Description | Verification Focus |
|--------|--------------|--------------------|
| Unit | Module or function level | Code correctness and LLR satisfaction |
| Integration | Interfaces between units | Data and control flow |
| System | End-to-end functions | HLR satisfaction, performance, fault handling |

## Coverage Objectives
- 100 % statement coverage  
- 100 % decision coverage  
- 100 % Modified Condition/Decision Coverage (MC/DC)  
- All infeasible code justified and documented  

Coverage measured using qualified tools or independent review per DO-178C §6.4.4.2.  

## Test Environment
| Category | Tool/Method | Qualification |
|-----------|-------------|---------------|
| Test Framework | Pytest / CTest / custom harness | Review or DO-330 qualification |
| Coverage Tool | gcov / lcov / Bullseye | Qualified or reviewed |
| Simulator/Target | Hardware-in-loop or virtual environment | Under configuration control |
| Defect Tracking | Jira / internal tracker | N/A |

All versions, configurations, and results archived under configuration management per SCMP.

## Verification Artifacts
- Verification Procedures (unit, integration, system)  
- Test Results and Anomaly Reports  
- Review Records (requirements, design, code)  
- Coverage Analysis Reports and Justifications  
- Verification Summary Report (VSR)  
- Inputs to the Software Accomplishment Summary (SAS)

## Entry/Exit Criteria
**Entry:**  
- Approved PSAC, SDP, SCMP, and SQAP.  
- Baseline development data.  
- Qualified or reviewed tools.

**Exit:**  
- All verification objectives satisfied.  
- All anomalies resolved or justified.  
- 100 % MC/DC achieved or justified.  
- QA approval for certification data release.

## Deliverables
| Artifact | Format | Owner |
|-----------|---------|-------|
| SVP (this document) | PDF, signed | Verification Lead |
| Test Procedures | Markdown / PDF | IV&V |
| Test Results | CSV / PDF | IV&V |
| Coverage Reports | HTML / PDF | IV&V |
| Verification Summary Report | PDF | QA / Certification |

## References
- RTCA DO-178C §6, §12  
- RTCA DO-330 (Tool Qualification)  
- SAE ARP4754A / ARP4761  
- PSAC, SDP, SCMP, SQAP

## Approval
| Role | Name | Signature | Date |
|------|------|------------|------|
| Verification Lead |  |  |  |
| Software QA Lead |  |  |  |
| Certification Authority |  |  |  |
