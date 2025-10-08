# RASCI Matrix - Release Management

**Document Number:** CM-POL-RASCI  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Defines roles and responsibilities for release management activities using the RASCI model:
- **R** — Responsible (does the work)
- **A** — Accountable (ultimate ownership, single point)
- **S** — Supporting (provides resources/support)
- **C** — Consulted (provides input)
- **I** — Informed (kept updated)

## 2. Roles

### 2.1 Primary Roles

- **PM** — Program Manager
- **CM** — Configuration Manager
- **RM** — Release Manager
- **CCB** — Configuration Control Board
- **EM** — Engineering Manager
- **QM** — Quality Manager
- **SM** — Safety Manager
- **SO** — Security Officer
- **CL** — Certification Lead
- **MFG** — Manufacturing Manager
- **OPS** — Operations Manager

### 2.2 Supporting Roles

- **ENG** — Engineering Team
- **QA** — Quality Assurance
- **TEST** — Test Engineering
- **CERT** — Certification Team
- **IT** — IT/DevOps Team
- **DOC** — Documentation Team
- **SUP** — Supply Chain
- **MAINT** — Maintenance Organization

## 3. RASCI Matrix by Activity

### 3.1 Release Planning

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL | MFG | OPS |
|----------|----|----|----|----|----|----|----|----|----|----|-----|
| Define release scope | C | C | R/A | I | C | C | C | I | C | C | C |
| Schedule release date | A | C | R | I | C | C | I | I | C | C | C |
| Identify baseline gate | C | A | R | I | R | C | C | I | C | I | I |
| Resource allocation | A | C | C | I | S | S | I | I | I | S | I |

### 3.2 Release Package Preparation

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL | MFG | OPS | ENG | QA | DOC |
|----------|----|----|----|----|----|----|----|----|----|----|-----|-----|----|----|
| Collect artifacts | I | C | A | I | S | S | S | I | S | C | I | R | R | R |
| Prepare EBOM | I | C | C | I | R | C | I | I | I | C | I | R | I | I |
| Prepare MBOM | I | C | C | I | C | C | I | I | I | R | I | S | I | I |
| Generate SBOM | I | C | A | I | S | C | I | C | C | I | I | R | I | I |
| Assemble compliance evidence | I | C | R | I | S | A | S | C | S | C | I | S | R | C |
| Create release notes | I | C | A | I | C | C | C | C | C | C | C | R | I | R |
| Freeze ICDs | I | C | R | I | A | C | C | I | C | C | I | S | I | C |
| Generate provenance attestations | I | I | A | I | C | C | I | S | I | I | I | S | C | I |
| Calculate SHA256 hashes | I | I | R | I | C | C | I | A | I | I | I | S | C | I |

### 3.3 Compliance Verification

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL | QA | CERT |
|----------|----|----|----|----|----|----|----|----|----|----|------|
| Review conformity checklist | I | C | R | I | C | S | C | C | C | A | C |
| Verify DO-178C evidence | I | I | C | I | C | S | C | I | R | A | R |
| Verify DO-254 evidence | I | I | C | I | C | S | C | I | R | A | R |
| Verify AS9100 compliance | I | I | C | I | C | A | C | I | C | R | C |
| Verify ECSS compliance | I | I | C | I | C | A | C | I | R | R | R |
| Review safety case | I | C | C | I | C | S | A | C | C | R | R |
| Assess export classification | I | C | C | I | I | I | C | A | C | C | I |
| QA sign-off | I | C | R | I | C | A | C | C | C | R | S |

### 3.4 CCB Review and Approval

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL |
|----------|----|----|----|----|----|----|----|----|-----|
| Submit package to CCB | I | C | R/A | I | C | C | C | C | C |
| Technical review | I | C | S | C | R | C | C | I | C |
| Quality review | I | C | S | C | C | R | C | C | C |
| Safety review | I | C | S | C | C | C | R | C | C |
| Security review | I | C | S | C | C | C | C | R | C |
| Certification review | I | C | S | C | C | C | C | C | R |
| CCB decision | I | C | R | A | C | C | C | C | C |
| Document approval | I | A | R | S | I | I | I | I | I |

### 3.5 Distribution and Deployment

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL | MFG | OPS | IT |
|----------|----|----|----|----|----|----|----|----|----|----|-----|-----|----|
| Prepare distribution package | I | C | A | I | C | C | I | C | I | C | C | R |
| Verify package integrity | I | C | R | I | C | A | I | C | I | I | I | R |
| Control distribution | I | C | A | I | I | C | I | S | I | C | C | R |
| Log distribution | I | C | R | I | I | I | I | I | I | C | C | A |
| Deploy to production | I | C | S | I | C | C | C | I | I | A | C | R |
| Deploy to operations | I | C | S | I | C | C | C | I | I | C | A | R |
| Verify deployment | I | C | C | I | C | R | C | I | I | S | S | A |

### 3.6 Registration and Record Keeping

| Activity | PM | CM | RM | CCB | QM |
|----------|----|----|----|----|-----|
| Update RELEASE_REGISTER.csv | I | A | R | I | C |
| Update DISTRIBUTION_LOG.csv | I | C | R | I | C |
| Update RELEASE_ICD_INDEX.csv | I | A | R | I | C |
| Archive release package | I | C | R | I | C |
| Update baselines | I | A | R | S | C |

### 3.7 Post-Release Activities

| Activity | PM | CM | RM | CCB | EM | QM | SM | OPS | MAINT |
|----------|----|----|----|----|----|----|----|----|-------|
| Monitor deployment | I | C | R | I | C | C | C | S | S |
| Track issues/defects | I | C | R | I | C | A | C | S | S |
| Collect metrics | I | C | A | I | C | R | C | C | C |
| Conduct post-release review | C | C | R | I | C | C | C | C | C |
| Update lessons learned | I | A | R | I | C | C | C | C | C |
| Plan rollback (if needed) | I | C | R | A | S | S | S | C | C |

### 3.8 Emergency Patch

| Activity | PM | CM | RM | CCB | EM | QM | SM | SO | CL |
|----------|----|----|----|----|----|----|----|----|-----|
| Assess severity | I | C | C | I | R | C | A | C | C |
| Fast-track approval | A | C | C | R | C | C | C | C | C |
| Prepare patch | I | C | R | I | S | C | S | I | C |
| Deploy urgently | I | C | A | I | C | C | C | I | I |
| Follow-up documentation | I | C | R | I | S | A | S | C | C |

## 4. Role Descriptions

### 4.1 Release Manager (RM)

**Responsibilities:**
- Prepare release packages per templates
- Coordinate with all stakeholders
- Ensure conformity checklist completion
- Submit to CCB
- Manage distribution
- Maintain release registers
- Track post-release metrics

**Accountable for:**
- Release package completeness and accuracy
- Distribution control
- Register accuracy
- Schedule adherence

### 4.2 Configuration Manager (CM)

**Responsibilities:**
- Oversee release process
- Ensure baseline integrity
- Approve release registration
- Audit release compliance
- Maintain release policy

**Accountable for:**
- Release process compliance
- Baseline traceability
- Configuration control
- Policy maintenance

### 4.3 Configuration Control Board (CCB)

**Responsibilities:**
- Review release packages
- Approve/reject releases
- Authorize distribution
- Resolve conflicts
- Approve emergency patches

**Accountable for:**
- Release approval decisions
- Program impact assessment
- Risk acceptance

### 4.4 Quality Manager (QM)

**Responsibilities:**
- Verify compliance evidence
- Conduct conformity reviews
- Sign off on quality aspects
- Track defects and metrics

**Accountable for:**
- Quality assurance of releases
- Compliance verification
- Post-release quality metrics

### 4.5 Safety Manager (SM)

**Responsibilities:**
- Review safety case
- Assess safety impact
- Approve safety-critical releases
- Track safety-related issues

**Accountable for:**
- Safety assessment
- Hazard closure verification
- Safety case completeness

### 4.6 Security Officer (SO)

**Responsibilities:**
- Review export classification
- Assess cybersecurity risks
- Approve distribution controls
- Track security vulnerabilities

**Accountable for:**
- Export control compliance
- Security risk assessment
- Distribution authorization

### 4.7 Certification Lead (CL)

**Responsibilities:**
- Coordinate with certification authorities
- Verify certification evidence
- Manage compliance plans
- Track findings and closures

**Accountable for:**
- Certification readiness
- Authority interface
- Compliance evidence completeness

## 5. Escalation Matrix

### 5.1 Level 1: Release Manager

- Routine issues
- Schedule coordination
- Documentation questions

### 5.2 Level 2: Configuration Manager

- Process exceptions
- Baseline conflicts
- Policy interpretation

### 5.3 Level 3: CCB

- Approval disputes
- Scope changes
- Risk acceptance

### 5.4 Level 4: Program Manager

- Strategic decisions
- Resource conflicts
- Stakeholder escalations

## 6. Communication Plan

### 6.1 Release Planning

- **Frequency:** Monthly
- **Participants:** RM, CM, EM, QM, MFG, OPS
- **Purpose:** Coordinate upcoming releases

### 6.2 Release Status

- **Frequency:** Weekly (during active release)
- **Participants:** RM, CM, domain leads
- **Purpose:** Track progress, identify blockers

### 6.3 CCB Meetings

- **Frequency:** Bi-weekly or as needed
- **Participants:** CCB members, RM, presenters
- **Purpose:** Review and approve releases

### 6.4 Post-Release Review

- **Frequency:** After each major release
- **Participants:** All stakeholders
- **Purpose:** Lessons learned, process improvement

## 7. Training Requirements

### 7.1 Release Manager

- Release policy and procedures (mandatory)
- CCB process (mandatory)
- Compliance standards overview (recommended)
- SBOM and provenance tools (mandatory)

### 7.2 All Stakeholders

- Release process overview (mandatory)
- Role-specific responsibilities (mandatory)
- Export control awareness (recommended)

## 8. Related Documents

- [RELEASE_POLICY.md](./RELEASE_POLICY.md) — Release governance
- [RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md) — Process steps
- [05-CCB/01-MEMBERS.md](../../05-CCB/01-MEMBERS.md) — CCB composition

## 9. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Configuration Manager |
