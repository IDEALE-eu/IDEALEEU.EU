# Software Development Plan (SDP)

## Purpose
Defines the methods, standards, and environment used to develop software classified as DO-178C Level A.  
This plan ensures consistency, traceability, and compliance with the PSAC and governing standards.

## Scope
Covers all software activities from requirements to code implementation.  
Applies to new code, reused modules, and third-party components within the DAL A system.

## Development Process
| Phase | Objective | Primary Output | Verification Reference |
|--------|------------|----------------|-------------------------|
| Requirements | Capture and validate high- and low-level software requirements | SRS, SDD | SVP § 3 |
| Design | Define architecture and detailed design | HLD, LLD | SVP § 4 |
| Code | Implement design in source form | Source Code, Unit Tests | SVP § 5 |
| Integration | Integrate modules and subsystems | Executable Object Code | SVP § 6 |
| Verification | Execute tests and analyses | Test Reports, Coverage Data | SVP § 7 |

## Standards
- **Coding:** MISRA C / company Python or C++ standard.  
- **Documentation:** Markdown for draft, PDF for signed baseline.  
- **Naming:** `<SUBSYS>_<TYPE>_<ID>` convention.  
- **Complexity:** maintain cyclomatic ≤ 10 per function.  
- **Traceability:** maintained in the Requirements Management Tool and exported to the DO-178C trace matrix.

## Development Environment
| Element | Tool | Qualification |
|----------|------|---------------|
| Requirements Management | Polarion / Jama / DOORS | Tool Assurance DO-330 TQL-5 |
| Configuration Management | Git with controlled branching | N/A |
| Compiler/Linker | Certified toolchain (GCC or Green Hills) | Evaluate per DO-330 |
| Static Analysis | CodeQL / PC-lint | Qualified or reviewed |
| Build Automation | CMake / Jenkins CI | Controlled under SCMP |

Environment configuration and versions are recorded in the baseline manifest.  
Reproducibility ensured through containerized or virtual build environments.

## Independence
- Development engineers produce code and design data.  
- Verification engineers independently review requirements, design, and code.  
- QA audits adherence to this plan.

## Outputs
1. Requirements and design documentation.  
2. Verified source code and object code.  
3. Build logs and version manifests.  
4. Trace matrices linking all life-cycle artifacts.  
5. Configuration baselines per SCMP.

## Change Control
All changes follow the SCMP process:
1. Change Request (CR) logged and assigned.  
2. Impact analysis and re-verification scope defined.  
3. CCB approval before integration.  
4. Updated trace and verification evidence produced.

## Quality Metrics
- Zero compiler warnings at DAL A baseline.  
- 100 % statement/decision coverage; MC/DC verified per SVP.  
- All anomalies tracked to closure before FCR-2.

## Interfaces
- **Inputs:** PSAC (scope), system requirements.  
- **Outputs:** verified code, trace data, verification artifacts (linked to SVP).  
- **Supporting Plans:** SCMP, SQAP, SVP, DO-330 Tool Qualification Plan.

## Deliverables
| Item | Format | Owner |
|------|---------|-------|
| SDP (this document) | PDF, signed | Dev Lead |
| Coding Standards | PDF | Dev Lead |
| Tool Inventory | XLSX | CM Lead |
| Environment Baseline | YAML/JSON | CM Lead |

## References
- RTCA DO-178C  
- SAE ARP4754A  
- RTCA DO-330  
- Company Software Engineering Policy  
- PSAC for this program

## Approval
| Role | Name | Signature | Date |
|------|------|------------|------|
| Software Development Lead |  |  |  |
| Software QA Lead |  |  |  |
| Certification Authority |  |  |  |
