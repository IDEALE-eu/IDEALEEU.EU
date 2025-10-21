# Software Quality Assurance Plan (SQAP)

## Purpose
Defines the quality assurance activities, audits, process monitoring, and independence requirements for software developed under DO-178C Level A.  
Ensures that all software life-cycle processes comply with approved plans (PSAC, SDP, SVP, SCMP) and that quality evidence is objective and independent.

## Scope
Applies to all development, verification, configuration, and certification activities for the DAL A software item.  
Covers QA oversight from project initiation through certification acceptance (SOI-4).

## QA Objectives
| Objective | Method | Evidence |
|------------|---------|-----------|
| Verify compliance with approved plans | Process audits | Audit reports |
| Ensure independence between QA, development, and verification | Organizational separation | QA org chart |
| Monitor adherence to standards and procedures | Process monitoring and spot checks | QA logs |
| Verify configuration control and baseline integrity | CM audits | CM audit reports |
| Ensure all nonconformities are tracked and resolved | Problem/Anomaly tracking | PR/CR logs |
| Certify readiness for each SOI milestone | QA sign-off | SOI checklist |

## QA Organization and Independence
- QA operates independently of development and verification.  
- QA reports to the Program Quality Manager, not to Engineering.  
- QA has authority to stop activities that violate approved processes.  
- QA personnel cannot approve their own work products.

## QA Activities
1. **Plan Reviews:** confirm PSAC, SDP, SVP, SCMP baselined and consistent.  
2. **Process Audits:** verify that required steps, reviews, and approvals are executed per plan.  
3. **Product Audits:** confirm that outputs match specifications and are traceable.  
4. **Configuration Audits:** check that baselines are under control and reproducible.  
5. **Change Control Monitoring:** ensure CCB procedures are followed.  
6. **SOI Readiness Assessments:** verify evidence completeness for each certification stage.  
7. **Anomaly Tracking Oversight:** confirm all problem reports have closure and impact analyses.  
8. **Supplier/Tool QA:** review supplier quality records and tool qualification data (DO-330).

## Audit Schedule
| Phase | Audit Type | Timing | Responsible | Output |
|--------|-------------|---------|--------------|---------|
| Planning | Process | Pre-SOI-1 | QA Lead | Audit Report 001 |
| Development | Product + Process | During coding | QA Engineer | Audit Report 002 |
| Verification | Product + CM | Pre-SOI-3 | QA Lead | Audit Report 003 |
| Final | Configuration + Certification Data | Pre-SOI-4 | QA Manager | Final QA Report |

All findings are logged, categorized (minor/major), and tracked to closure in the QA database.

## Nonconformity Management
1. QA raises Nonconformity Report (NCR).  
2. Assigned owner performs root-cause analysis and corrective action.  
3. QA verifies and closes NCR.  
4. Records retained under configuration management.

## Records and Deliverables
- QA Audit Reports (process, product, CM).  
- NCR log and closure evidence.  
- QA Checklists and Independence Matrix.  
- SOI Readiness Reviews and Sign-off forms.  
- Final QA Summary for Software Accomplishment Summary (SAS) package.

## Entry / Exit Criteria
**Entry:** Approved PSAC and supporting plans, QA resources assigned, independence established.  
**Exit:** All QA findings closed, SOI checklists complete, QA approves certification release.

## Tools and Repositories
| Activity | Tool | Qualification |
|-----------|------|---------------|
| QA tracking | Jira / internal QA system | N/A |
| Document control | Git / CM system | Under SCMP |
| Audit logs | Controlled SharePoint / repo | N/A |

## Interfaces
- **With Development:** audit adherence to SDP and coding standards.  
- **With Verification:** confirm independence, review coverage and results.  
- **With CM:** verify baselines and release records.  
- **With Certification:** provide QA sign-off and readiness data.

## References
- RTCA DO-178C §7, §8  
- SAE ARP4754A  
- DO-330 (tool QA)  
- PSAC, SDP, SVP, SCMP  
- Company Quality Manual

## Approval
| Role | Name | Signature | Date |
|------|------|------------|------|
| QA Lead |  |  |  |
| Program Manager |  |  |  |
| Certification Authority |  |  |  |
