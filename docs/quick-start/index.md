---
layout: page
title: "Quick Start Guide"
description: "Get started with IDEALE-EU in minutes"
---

# Quick Start Guide

Get up and running with IDEALE-EU in minutes. This guide covers account setup, role-specific workflows, and first steps for creating digital passports.

## Account Setup and Orientation

### Create Your Account
1. Visit [portal.ideale-eu.aero](https://portal.ideale-eu.aero)
2. Click "Sign Up" and provide your organization details
3. Verify your email address
4. Complete your profile information
5. Select your primary role (Engineer, PM, Auditor, or Supplier)

### Portal Orientation
- **Dashboard**: Overview of your programs, recent activity, and alerts
- **Digital Passports**: Create and manage component passports
- **QS Anchoring**: Freeze and verify evidence states
- **Programs**: Access program structures and configurations
- **Settings**: Manage integrations, API keys, and preferences

---

## Role-Specific Workflows

### For Engineers

#### Initial Setup
1. Install CAD plugin for your primary tool (SolidWorks, CATIA, NX, or Creo)
2. Configure PLM integration (Teamcenter, 3DEXPERIENCE, or Windchill)
3. Set up your TFA domain preferences

#### Create Your First Digital Passport
1. Open your CAD model
2. Select **IDEALE-EU → Create Passport** from the plugin menu
3. Fill in required metadata:
   - Part Number
   - TFA Domain (e.g., AAA for Airframes)
   - ATA Chapter (if applicable)
   - Material specification
   - Design owner
4. Click **Generate Passport**
5. Review the auto-populated fields
6. **QS Anchor** to freeze the initial design state

#### Daily Engineering Workflow
1. **Design Phase (CAD)**:
   - Create/modify 3D models
   - Generate drawings
   - Document design decisions
   - QS anchor major milestones

2. **Analysis Phase (CAE)**:
   - Run FEA, CFD, or other simulations
   - Attach analysis results to passport
   - Document assumptions and boundary conditions
   - QS anchor validated configurations

3. **Design Reviews**:
   - Share passport link with reviewers
   - Track comments and approvals
   - Update passport with review outcomes
   - QS anchor approved designs

---

### For Program Managers

#### Set Up New Program
1. Navigate to **Programs → Create New**
2. Define program structure using 00-10 directory template:
   - **00-PROGRAM**: Governance, CM, QMS
   - **01-FLEET**: Operational data
   - **02-AIRCRAFT**: Product structures (or 03-09 for other products)
   - **10-BUSINESS**: Market and partnerships

3. Configure program settings:
   - Team members and roles
   - TFA domains in scope
   - Certification requirements
   - Review gates and milestones

#### Program Dashboard Management
- **Status Overview**: Track progress across all WBS elements
- **Critical Path**: Monitor schedule health
- **Quality Metrics**: NCRs, CARs, audit findings
- **Configuration Baseline**: Current approved configuration
- **Risk Register**: Active risks and mitigations

#### Configuration Management (ECR/ECO/CCB)
1. **Engineering Change Request (ECR)**:
   - Engineer submits change proposal
   - PM reviews impact (cost, schedule, performance)
   - Attach affected digital passports

2. **Engineering Change Order (ECO)**:
   - CCB reviews and approves ECR
   - Generate ECO with approved changes
   - Update all affected passports
   - QS anchor new baseline

3. **Configuration Control Board (CCB)**:
   - Weekly or bi-weekly meetings
   - Review pending changes
   - Approve/defer/reject ECOs
   - Maintain baseline integrity

---

### For Auditors

#### Access Audit Portal
1. Log in with auditor credentials
2. Select program or supplier to audit
3. Review available evidence packages

#### Verify QS Evidence
1. Navigate to **QS Verification** section
2. Enter passport ID or component serial number
3. Review evidence chain:
   - Creation timestamp
   - QS anchor points (frozen states)
   - Modification history
   - Approval trail
   - Merkle root verification

4. Verify cryptographic seals:
   - Hash integrity check
   - Digital signature validation
   - Blockchain bridge confirmation (if used)

#### Generate Certification Package
1. Select components for certification
2. Choose evidence type:
   - Design certification (CAD, CAE, CAV)
   - Manufacturing certification (CAM, CAP)
   - Service certification (CAS)

3. Export package formats:
   - PDF for FAA/EASA submission
   - CSDB (S1000D) for technical publications
   - JSON/XML for digital exchange

4. Include:
   - All QS-anchored evidence
   - Test reports and analysis results
   - Approval signatures
   - Traceability matrix
   - Compliance statements

---

### For Suppliers

#### Register Components
1. Log in to Supplier Portal
2. Navigate to **Component Registration**
3. For each component:
   - Part number and description
   - Material certifications
   - Manufacturing process
   - Quality control data
   - Test results

4. Create digital passport:
   - Upload manufacturing data
   - Attach certificates of conformance
   - Link to material traceability
   - QS anchor as-manufactured state

#### Submit to OEM
1. Package component data:
   - Digital passport
   - Inspection reports
   - Serialization data
   - Delivery documentation

2. Submit via portal or API
3. Track approval status
4. Maintain historical records

#### API Integration
For automated integration:
```bash
# Example: Register component via CLI
ideale-eu supplier register \
  --part-number "SUP-AAA-12345" \
  --serial "SN-00123" \
  --material "AL-7075-T6" \
  --cert "CERT-2025-001.pdf"
```

---

## CAD Plugin Installation

### SolidWorks (2020-2025)
1. Download installer: [SolidWorks Plugin](https://downloads.ideale-eu.aero/plugins/solidworks)
2. Close SolidWorks
3. Run installer as administrator
4. Restart SolidWorks
5. Configure: **Tools → Add-Ins → IDEALE-EU**
6. Enter API key from portal

### CATIA V5 (R20+) and V6
1. Download: [CATIA Plugin](https://downloads.ideale-eu.aero/plugins/catia)
2. Extract to CATIA startup directory
3. Edit `CATSettings` file with your API credentials
4. Restart CATIA
5. Access via **Start → Mechanical Design → IDEALE-EU**

### Siemens NX (12+)
1. Download: [NX Plugin](https://downloads.ideale-eu.aero/plugins/nx)
2. Install via NX Package Manager
3. Configure in **Preferences → IDEALE-EU Integration**
4. Restart NX
5. Access via **Tools → IDEALE-EU**

### PTC Creo (7-10)
1. Download: [Creo Plugin](https://downloads.ideale-eu.aero/plugins/creo)
2. Copy to `<creo_loadpoint>/Common Files/plugins/`
3. Edit `config.pro` to load plugin
4. Restart Creo
5. Access via **Tools → IDEALE-EU Passport**

---

## Integration with PLM/ERP Systems

### PLM Integration

#### Siemens Teamcenter
- Real-time synchronization of part metadata
- Automatic passport creation on item creation
- BOM structure mapping to TFA domains
- Change management integration

Configuration:
```yaml
plm:
  type: teamcenter
  endpoint: https://teamcenter.yourcompany.com
  credentials:
    username: ${TC_USER}
    password: ${TC_PASSWORD}
  sync_interval: 300  # seconds
```

#### Dassault 3DEXPERIENCE
- Native integration via 3DSpace
- Passport as 3DEXPERIENCE object
- Lifecycle synchronization
- Collaboration space integration

#### PTC Windchill
- RESTful API integration
- Part-to-passport mapping
- Change notice synchronization
- Document management integration

#### Aras Innovator
- Graph-based relationship mapping
- Digital thread visualization
- Custom workflow integration
- Open architecture benefits

### ERP Integration

#### SAP S/4HANA
- Material master synchronization
- Production order tracking
- Quality notifications (QM)
- Serialization integration

#### Oracle E-Business Suite
- Inventory management integration
- Work order tracking
- Quality management
- Supply chain visibility

#### Microsoft Dynamics 365
- CRM integration for customer portals
- Supply chain management
- Field service integration
- Financial traceability

---

## First Digital Passport Creation

### Step-by-Step Process

1. **Prepare Component Data**:
   - 3D CAD model (native or STEP)
   - 2D drawings (PDF or DWG)
   - Material specification
   - Design requirements document

2. **Open IDEALE-EU Portal or Plugin**:
   - Choose creation method (web portal or CAD plugin)
   - Select TFA domain
   - Choose ATA chapter (aircraft) or equivalent

3. **Fill Required Fields**:
   - **Part Number**: Unique identifier (e.g., AAA-12345)
   - **Description**: Clear component description
   - **Domain**: TFA domain code (AAA, PPP, etc.)
   - **Material**: Material specification (e.g., AL-7075-T6)
   - **Owner**: Design responsible engineer
   - **Program**: Associated program/project

4. **Attach Artifacts**:
   - Upload CAD model
   - Add drawings
   - Link analysis results (if available)
   - Include material certifications

5. **Set Metadata**:
   - Effectivity range
   - Configuration baseline
   - Drawing revision
   - Approval status

6. **Review and Create**:
   - Preview passport data
   - Verify completeness
   - Click **Create Passport**
   - System generates unique passport ID

7. **QS Anchor Initial State**:
   - Click **QS Anchor** button
   - Add anchor description (e.g., "Initial design release")
   - Confirm anchor operation
   - System creates immutable snapshot with cryptographic seal

8. **Share and Collaborate**:
   - Copy passport link
   - Share with team members
   - Set access permissions
   - Track views and interactions

---

## Next Steps

### Continue Learning
- [TFA Domains Reference](/docs/tfa-domains/) - Understand domain structure
- [CAx Lifecycle](/docs/cax-lifecycle/) - Learn the 9-phase lifecycle
- [QS Technical Specification](/docs/technical/qs-specification/) - Deep dive into evidence anchoring
- [Glossary](/docs/glossary/) - Reference for all terminology

### Get Help
- **Support Email**: support@ideale-eu.aero
- **Community Forum**: [community.ideale-eu.aero](https://community.ideale-eu.aero)
- **Training Courses**: Available for all roles

### Best Practices
- QS anchor at major milestones (design freeze, approval, release)
- Use descriptive anchor labels
- Attach supporting evidence before anchoring
- Review passport completeness regularly
- Maintain consistent naming conventions
- Link related passports (assemblies, components)

---

*Ready to create your first digital passport? [Log in to the portal →](https://portal.ideale-eu.aero)*
