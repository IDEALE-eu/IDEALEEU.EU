# Plan for Software Aspects of Certification (PSAC)

## Purpose
Defines the software scope, software level assignments, and certification strategy for this DO-178C Level A item. It is the controlling document for all subordinate plans and certification evidence.

## Scope
- **Standard:** DO-178C, with references to ARP4754A and DO-330 (tool qualification).
- **Software Level (DAL):** A – failure condition classified as catastrophic.
- **System Context:** Derived from system safety assessment; maps functions to software components.
- **Applicability:** All software and tools contributing to airborne system behavior.

## Certification Approach
- Compliance demonstration per DO-178C objectives for Level A.
- Use of established development and verification environments under configuration control.
- Application of independence between development, verification, and QA activities.
- Evidence delivered through life-cycle data and traceable baselines.

## Life-Cycle Data Overview
| Category | Data Item | Responsibility |
|-----------|------------|----------------|
| **Planning** | PSAC, SDP, SVP, SQAP, SCMP | Project Manager / Leads |
| **Development** | High- and Low-Level Requirements, Design Data, Source Code | Development Lead |
| **Verification** | Test Procedures, Test Results, Reviews, Coverage Reports | Independent Verification |
| **Configuration** | Baselines, CCB Records, Problem Reports | CM Lead |
| **Quality** | Audit Records, QA Findings, Approvals | QA Lead |
| **Certification** | SAS, SOI Minutes, Compliance Checklists | Certification Focal |

## Subordinate Plans
- **Software Development Plan (SDP):** defines methods, coding standards, and environments.  
- **Software Verification Plan (SVP):** describes test and review processes and coverage metrics.  
- **Software Configuration Management Plan (SCMP):** defines baseline control and change tracking.  
- **Software Quality Assurance Plan (SQAP):** describes QA independence and audits.  
- **Tool Qualification Plan (if required):** defines qualification strategy for verification or development tools per DO-330.

## Independence Matrix
| Activity | Performer | Independence Requirement | Implemented By |
|-----------|------------|---------------------------|----------------|
| Requirements verification | Independent team | Full | IV&V |
| Code reviews | Independent engineer | Full | IV&V |
| Test witnessing | QA or IV&V | Full | QA |
| CM audits | QA | Full | QA |

## Certification Data Deliverables
1. Signed PSAC and subordinate plans.  
2. Life-cycle data repositories with controlled baselines.  
3. Traceability from system requirement → software requirement → test case → result.  
4. Verification records showing 100 % statement/decision and MC/DC coverage.  
5. Configuration index and Software Accomplishment Summary (SAS).  
6. Tool qualification evidence (if applicable).

## Compliance Demonstration
All DO-178C Level A objectives are mapped to evidence within the certification data index.  
Verification independence, coverage, and reviews will be verified at each SOI milestone (SOI-1 through SOI-4).  
Authority coordination occurs via the Certification Liaison documented in this PSAC.

## Records and Traceability
Each artifact shall include:
- Title, version, baseline ID, date, author, approver.
- Reference to this PSAC and corresponding DO-178C objectives.
- SHA-256 hash for reproducibility.

## References
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*  
- RTCA DO-330, *Software Tool Qualification Considerations*  
- SAE ARP4754A, *Guidelines for Development of Civil Aircraft and Systems*  
- SAE ARP4761, *Safety Assessment Process*  
- Company Standards and Certification Policy Manual.

## Approval
| Role | Name | Signature | Date |
|------|------|------------|------|
| Project Manager |  |  |  |
| Software QA Lead |  |  |  |
| Certification Authority Representative |  |  |  |
