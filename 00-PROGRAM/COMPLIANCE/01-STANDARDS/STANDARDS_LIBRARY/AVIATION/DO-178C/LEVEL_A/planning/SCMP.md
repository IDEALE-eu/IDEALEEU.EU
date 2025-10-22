# Software Configuration Management Plan (SCMP)

## Purpose
Defines the configuration management (CM) process for software developed under DO-178C Level A.  
Ensures all life-cycle data are identified, controlled, traceable, and reproducible from creation through certification.

## Scope
Applies to all software configuration items (SCIs), derived data, and baselines within the program.  
Includes source code, requirements, design, verification artifacts, tools, and certification data.

## Objectives
| Objective | Description | Evidence |
|------------|-------------|-----------|
| Identification | Assign unique identifiers to all SCIs | Configuration Index |
| Control | Maintain integrity of all baselines under CCB authority | CCB records |
| Change Management | Control and record all modifications | CR/PR logs |
| Status Accounting | Track configuration state and change history | CM database |
| Auditing | Verify integrity and consistency of items | Audit reports |

## Configuration Identification
Each SCI must have:
- Unique identifier (e.g., `SWC_<type>_<id>`).  
- Version, date, author, and approval metadata.  
- Stored in the controlled repository defined below.

### Configuration Items
| Category | Examples | Storage |
|-----------|-----------|----------|
| Requirements | SRS, LLR | CM repository `/requirements/` |
| Design | HLD, LLD | `/design/` |
| Source Code | `.c`, `.py`, `.h`, build scripts | `/source/` |
| Verification Data | procedures, results, coverage | `/verification/` |
| Tools | qualified tools, scripts | `/tools/` |
| Certification | SAS, CI, SOI minutes | `/certification/` |

## Repository and Tools
| Function | Tool | Control Level |
|-----------|------|---------------|
| Version Control | Git (controlled main branch) | High |
| Issue Tracking | Jira / PR tracker | High |
| Document Control | Git + controlled export to PDF | Medium |
| Build System | Jenkins / CI pipeline | Controlled |
| Backup | Encrypted, versioned storage | Scheduled daily |

Access rights defined by role; all repositories under central authority of the Configuration Control Board (CCB).

## Baseline Management
### Baseline Types
| Baseline | Purpose | Approval |
|-----------|----------|----------|
| Development | Working integration | Dev Lead |
| Test | Verified build for testing | Verification Lead |
| Release | Certified build for submission | CCB |
| Certification | Approved data set for authority | QA + CCB |

Each baseline captured with hash, tag, and build manifest (commit SHA, tool versions, environment checksum).

## Change Control Process
1. **Initiation** – Submit Change Request (CR) or Problem Report (PR).  
2. **Evaluation** – Impact analysis (safety, certification, trace).  
3. **CCB Review** – Approve, defer, or reject.  
4. **Implementation** – Controlled update and re-verification.  
5. **Closure** – QA verifies evidence, updates CM logs.

All changes tracked in CM log:
```

CR_ID | Description | Impacted Items | CCB Decision | Date | Status

```

## Configuration Audits
Two mandatory audits:
- **Functional Configuration Audit (FCA):** verify software meets requirements and verification complete.  
- **Physical Configuration Audit (PCA):** verify each delivered item matches configuration index and repository contents.

Audit results recorded in QA audit reports and referenced in the Software Accomplishment Summary (SAS).

## Status Accounting
The CM system must produce:
- Current baseline identifier and date.  
- List of open/closed CRs and PRs.  
- Trace from requirement → design → code → test → release.  
- Tool and environment configuration history.

## Records and Deliverables
| Artifact | Format | Owner |
|-----------|---------|-------|
| SCMP (this plan) | PDF, signed | CM Lead |
| Configuration Index | XLSX / JSON | CM |
| CCB Minutes | PDF | CM Secretary |
| Change Log | CSV / Tracker Export | CM |
| Audit Reports | PDF | QA |
| Baseline Manifest | YAML / JSON | CM |

## Interfaces
- **With QA:** audit CM processes and baselines.  
- **With Development:** establish release gates and tags.  
- **With Verification:** synchronize test baselines.  
- **With Certification:** provide configuration index and SAS inputs.

## References
- RTCA DO-178C §8  
- RTCA DO-330 (tool configuration)  
- SAE ARP4754A  
- PSAC, SDP, SVP, SQAP

## Approval
| Role | Name | Signature | Date |
|------|------|------------|------|
| Configuration Management Lead |  |  |  |
| Software QA Lead |  |  |  |
| Certification Authority |  |  |  |

