# Configuration Management Plan

## 1. Introduction

### 1.1 Purpose
This Configuration Management Plan (CMP) defines the processes, procedures, and organizational responsibilities for configuration management (CM) throughout the IDEALE EU aerospace program lifecycle.

### 1.2 Scope
This plan applies to:
- Aircraft development and production
- Spacecraft development and production
- Ground support equipment
- Software and firmware
- Documentation and specifications
- Test equipment and procedures

### 1.3 Applicable Standards
- **AS9100** - Quality Management System for Aerospace
- **ARP4754A** - Development of Civil Aircraft and Systems
- **ECSS-M-ST-40C** - Configuration and Information Management
- **ISO 10007** - Configuration Management Guidelines
- **DO-178C** - Software Considerations in Airborne Systems
- **DO-254** - Design Assurance Guidance for Electronic Hardware

## 2. Configuration Management Organization

### 2.1 Configuration Manager
- Develops and maintains CM plan
- Manages CM tools and systems
- Coordinates CCB activities
- Reports CM metrics to program management

### 2.2 Configuration Control Board (CCB)
- Reviews and approves/rejects change requests
- Assesses impact of changes
- Authorizes release of baselines
- Membership defined in 05-CCB/01-MEMBERS.md

### 2.3 Engineering
- Submits Engineering Change Requests (ECRs)
- Implements approved Engineering Change Orders (ECOs)
- Updates design documentation

### 2.4 Quality Assurance
- Conducts configuration audits
- Verifies CM compliance
- Reviews change implementations

## 3. Configuration Identification

### 3.1 Configuration Items (CIs)
Configuration items include:
- Hardware assemblies and components
- Software and firmware
- Documents and specifications
- Tooling and GSE
- Test procedures

### 3.2 Part Numbering
See **02-PART_NUMBERING.md** for detailed part numbering scheme.

Key principles:
- Unique identifier for each CI
- Intelligent numbering with category codes
- Revision control (letters for design, numbers for process)
- Interchangeability tracking

### 3.3 Serialization
See **03-SERIALIZATION.md** for serialization rules.

Serialized items:
- Flight-critical hardware
- Test articles
- Major assemblies
- Controlled tooling

## 4. Configuration Control

### 4.1 Baseline Management
Baselines are established at each stage gate:
- **SRR Baseline** - System requirements
- **PDR Baseline** - Preliminary design
- **CDR Baseline** - Critical design (design freeze)
- **TRR Baseline** - Test readiness
- **PRR Baseline** - Production readiness
- **ORR/EIS Baseline** - Operational readiness (Aircraft)
- **FRR Baseline** - Flight readiness (Spacecraft)

Baselines stored in **04-BASELINES/[GATE]/**

### 4.2 Change Process
All changes to baselined items must follow the ECR/ECO process:

1. **Initiation** - Submit ECR (template in 13-TEMPLATES/ECR.yml)
2. **Classification** - Categorize as Class I, II, or III
3. **Impact Assessment** - Engineering evaluates impact
4. **CCB Review** - CCB evaluates and approves/rejects
5. **Implementation** - If approved, ECO issued and implemented
6. **Verification** - QA verifies implementation
7. **Closure** - Document in 06-CHANGES/

### 4.3 Change Classification
- **Class I** - Affects form, fit, function, or certification; requires CCB approval
- **Class II** - Documentation or minor changes; delegated approval
- **Class III** - Administrative changes; CM approval only

### 4.4 Deviations and Waivers
- **Deviation** - Temporary departure from requirements (one-time)
- **Waiver** - Permanent acceptance of non-conforming item

Documented in **06-CHANGES/DEVIATIONS/** and **06-CHANGES/WAIVERS/**

## 5. Configuration Status Accounting

### 5.1 Item Master
Maintained in **08-ITEM_MASTER/ITEMS.csv**:
- Part number
- Description
- Revision level
- Status (development, production, obsolete)
- Effectivity
- Owner

### 5.2 Traceability
Maintained in **10-TRACEABILITY/**:
- Requirements to configuration items (**REQ_ITEM.csv**)
- Changes to baselines (**CHANGE_BASELINE.csv**)
- UTCS threads (Use Case → Test Case → System thread)

### 5.3 Reporting
Monthly CM metrics:
- Open ECRs/ECOs
- Change backlog
- Baseline integrity
- Audit findings

## 6. Configuration Audits

### 6.1 Physical Configuration Audit (PCA)
Verifies as-built configuration matches design documentation.

### 6.2 Functional Configuration Audit (FCA)
Verifies item performance meets requirements.

### 6.3 Configuration Management Audit
Verifies CM processes are followed.

Documentation in **11-AUDITS/**

## 7. Interface Management

### 7.1 Interface Control Documents (ICDs)
All internal and external interfaces documented in **09-INTERFACES/**

### 7.2 ICD Process
1. Identify interface
2. Create ICD (template ICD-XXXX.md)
3. Coordinate with stakeholders
4. Obtain signatures
5. Place under configuration control

## 8. Release Management

### 8.1 Release Process
1. Verification complete
2. Documentation package prepared
3. CCB approval
4. Release to manufacturing/operations
5. Archived in **07-RELEASES/[AIRCRAFT|SPACECRAFT]/**

### 8.2 Release Package Contents
- Approved drawings
- Bill of materials
- Specifications
- Manufacturing instructions
- Test procedures
- Certification evidence (if applicable)

## 9. CI/CD Integration

### 9.1 Version Control
Git-based version control with:
- Branching model (see **12-CI_CD_RULES/BRANCHING_MODEL.md**)
- Tagging conventions (see **12-CI_CD_RULES/TAGGING.md**)
- Code owners (see **12-CI_CD_RULES/CODEOWNERS**)

### 9.2 Automated Gates
Pre-merge checks defined in **12-CI_CD_RULES/GATES.md**

## 10. Training

All personnel involved in CM activities receive training on:
- CM processes and procedures
- CM tools
- Change control process
- Baseline management

## 11. CM Tools

- **Git** - Version control
- **PLM/PDM System** - Item master and document management
- **Issue Tracking** - ECR/ECO workflow
- **Traceability Tools** - Requirements management

## 12. Metrics and Continuous Improvement

Key metrics:
- ECR/ECO cycle time
- Change backlog
- Baseline integrity score
- Audit findings closure rate
- Configuration item identification coverage

Regular reviews and improvements to CM processes.
