# CONFIG_MGMT

Configuration management standards.

## Overview

Configuration management (CM) ensures controlled evolution of product configuration throughout its lifecycle. This directory contains standards for CM applicable to both aircraft and spacecraft.

## Applicable Standards

### ISO 10007:2017 - Quality Management - Guidelines for Configuration Management
- **Scope**: CM principles and best practices
- **Coverage**: CM planning, identification, control, status accounting, audit
- **Applicability**: Any industry, product, or service

### EIA-649C - National Consensus Standard for Configuration Management
- **Scope**: Detailed CM requirements and processes
- **Coverage**: CM principles, planning, identification, change management, status accounting, audit
- **Origin**: Electronics Industries Alliance (now TechAmerica)

### CMII - Configuration Management II
- **Scope**: Best practices for CM in complex products
- **Concepts**: Class I/II/III changes, Change Review Board (CRB)
- **Training**: CMII certification available

## Configuration Management Fundamentals

### Four Pillars of CM
1. **Configuration Identification** - Define product baselines and configuration items
2. **Configuration Control** - Manage changes to baselines
3. **Configuration Status Accounting** - Track configuration and changes
4. **Configuration Audit** - Verify configuration matches documentation

### Configuration Item (CI)
- Hardware, software, documents, or combinations designated for CM
- Each CI has unique identifier, version/revision
- Examples: Part number, drawing number, software build number

### Baseline
- Approved configuration at a point in time
- Types:
  - **Functional Baseline**: Requirements (after SRR/SDR)
  - **Allocated Baseline**: Requirements allocated to subsystems (after PDR)
  - **Product Baseline**: Design released for production (after CDR)
  - **As-Built Configuration**: Actual built configuration
  - **As-Maintained Configuration**: Current operational configuration

## CM Processes

### Configuration Planning
- **CM Plan (CMP)**: Define CM approach, roles, tools, processes
- **Tailoring**: Adapt CM processes to program needs
- **Integration**: Align with broader project and quality management

### Configuration Identification
- **Product Structure**: Break down product into CIs (WBS, PBS)
- **Naming Conventions**: Part numbers, document numbers, software versions
- **Baselines**: Define what constitutes each baseline
- **Interface Control**: Define and control interfaces between CIs

### Change Management
- **Change Request (CR)**: Initiate change proposal
- **Change Assessment**: Evaluate impact (cost, schedule, performance, risk)
- **Change Approval**: Configuration Control Board (CCB) or delegated authority
- **Change Implementation**: Execute approved change
- **Change Verification**: Verify change implemented correctly

### Status Accounting
- **Configuration Database**: Maintain current and historical configuration
- **Traceability**: Link requirements, design, parts, documents
- **Reports**: Configuration status, change status, baseline reports
- **Metrics**: Number of changes, time to process, open vs. closed

### Configuration Audit
- **Functional Configuration Audit (FCA)**: Verify product meets requirements
- **Physical Configuration Audit (PCA)**: Verify as-built matches design
- **Combined Audit**: FCA + PCA together
- **Timing**: Before acceptance, before delivery, periodically in service

## Change Classification

### CMII Classification
- **Class I**: Affects form, fit, function, or interface - requires CCB approval
- **Class II**: Affects documentation or supporting data - controlled but may be delegated
- **Class III**: Minor corrections, no functional impact - minimal control

### Aircraft (Part 21)
- **Major Change**: Requires amended Type Certificate or STC
- **Minor Change**: Approved by designated engineering representative
- **No Safety Effect**: May not require approval

### Spacecraft (ECSS)
- **Critical Change**: Affects safety or mission-critical functions - extensive review
- **Important Change**: Significant impact - CCB approval
- **Minor Change**: Limited impact - expedited approval

## Configuration Control Board (CCB)

### Purpose
- Review and approve changes to baseline
- Ensure changes are necessary, feasible, and properly implemented
- Balance technical, cost, schedule considerations

### Membership
- Program manager (chair)
- Chief engineer
- Systems engineering lead
- Domain leads (software, hardware, etc.)
- Quality assurance
- Safety engineer
- Customer representative (if applicable)

### Process
1. **Submission**: Change request submitted with justification and impact analysis
2. **Review**: CCB members review CR
3. **Discussion**: CCB meeting to discuss CR
4. **Decision**: Approve, disapprove, defer, or request more information
5. **Documentation**: Record decision and rationale
6. **Implementation**: Approved changes implemented per schedule

## Tools and Systems

### PLM/PDM Systems
- Siemens Teamcenter
- Dassault Systèmes 3DEXPERIENCE / ENOVIA
- PTC Windchill
- SAP PLM
- Aras Innovator

### Version Control
- Git (software, documents)
- Subversion (SVN)
- PLM system (CAD, documents, data)

### Change Management
- Jira, ServiceNow, Polarion (issue/change tracking)
- PLM system change workflow
- Custom change management tools

## Key Deliverables

1. **Configuration Management Plan (CMP)** - CM approach and processes
2. **Product Breakdown Structure (PBS)** - Hierarchy of CIs
3. **Configuration Item List** - All CIs with identifiers and baselines
4. **Interface Control Documents (ICDs)** - Controlled interfaces
5. **Change Requests (CRs)** - Change proposals and dispositions
6. **Configuration Status Report** - Current configuration and changes
7. **Configuration Audit Reports** - FCA, PCA results

## Compliance Requirements

- CM per ISO 10007 or EIA-649C
- CM plan established and approved
- Baselines defined and controlled
- Changes approved by CCB or delegated authority
- Configuration audits performed per schedule
- Configuration database maintained and accurate

## Integration with Other Standards

### Aircraft
- **Part 21**: CM supports production certificate and type certificate
- **AS9100**: CM is part of quality management system
- **ARP4754A**: CM coordinates with systems engineering

### Spacecraft
- **ECSS-M-ST-40C**: Project management and CM
- **ECSS-Q-ST-20C**: Quality assurance includes CM oversight
- **ECSS-E-ST-10C**: Systems engineering uses CM processes

## Best Practices

- Establish CM early (Phase A or earlier)
- Tailor CM processes to program complexity
- Automate where possible (PLM, workflows)
- Train team on CM processes and tools
- Regular CCB meetings (weekly or biweekly during development)
- Configuration audits before major milestones (PDR, CDR, delivery)
- Maintain accurate as-built configuration

## Common Pitfalls

- CM processes too bureaucratic (slows development)
- CM processes too loose (configuration drifts)
- Inadequate impact analysis before changes
- Poorly documented changes (hard to understand later)
- Configuration database not maintained
- As-built configuration diverges from design

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - CM standards
- ISO 10007:2017 (purchase from ISO)
- EIA-649C (purchase from TechAmerica / SAE)
- 00-PROGRAM/CONFIG_MGMT/ - Program CM implementation

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
