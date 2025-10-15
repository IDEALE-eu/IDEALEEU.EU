---
layout: page
title: "Quick Start Guide"
description: "Get started with IDEALE-EU platform in minutes"
toc: true
---

# Quick Start Guide

## Welcome to IDEALE-EU

This guide will help you get started with the IDEALE-EU platform for aerospace digital passports and lifecycle management.

## Prerequisites

### For Engineers
- CAD software (SolidWorks, CATIA, NX, or Creo)
- Basic understanding of aerospace development processes
- Company email for SSO authentication

### For Program Managers
- Access to PLM system (Teamcenter, Windchill, or 3DEXPERIENCE)
- Program charter and stakeholder registry
- Understanding of ATA chapter structure

### For Auditors
- Regulatory authority credentials (FAA, EASA, ICAO)
- Familiarity with certification requirements
- Access to certification basis documents

## Step 1: Create Your Account

### Sign Up Process

1. Visit the [IDEALE-EU Portal](https://portal.ideale-eu.aero)
2. Click **"Sign Up"** or use **SSO** with your organization
3. Select your role:
   - Engineer
   - Program Manager
   - Auditor
   - Supplier
   - Operator
4. Complete your profile with organization details
5. Accept terms and conditions
6. Verify your email address

### Organization Setup

**For Enterprise Customers**:
- Contact [contact@ideale-eu.aero](mailto:contact@ideale-eu.aero)
- Provide organization details and user count
- Configure SSO integration (SAML 2.0, OAuth)
- Set up role-based access controls (RBAC)
- Define TFA domain permissions

## Step 2: Platform Orientation

### Dashboard Overview

Your dashboard provides:
- **Active Programs**: Programs you're assigned to
- **Recent Activity**: Latest updates across domains
- **Notifications**: ECR/ECO approvals, test results, certifications
- **Quick Actions**: Create digital passport, upload documentation, search components

### Navigation Structure

```
IDEALE-EU Platform
├── Programs (00-10 structure)
│   ├── 00-PROGRAM (charter, schedule)
│   ├── 01-REQUIREMENTS (traceability)
│   ├── 02-DESIGN (CAD models)
│   ├── ...
│   └── 10-BUSINESS (contracts)
├── TFA Domains (15 domains)
│   ├── AAA (Airframes-Aero-Airworthiness)
│   ├── PPP (Propulsion-Power-Plants)
│   ├── ...
│   └── LIB (Logistics-Inventory-Blockchain)
├── CAx Phases (9 phases)
│   ├── CAD → CAE → CAI → CAO
│   ├── CAM → CAP → CAV
│   └── CMP → CAS
└── Digital Passports (QS-anchored)
```

## Step 3: First Steps by Role

### For Engineers

#### Install CAD Plugin

1. Navigate to **Plugins > CAD Integrations**
2. Download plugin for your CAD system:
   - [SolidWorks Plugin](https://plugins.ideale-eu.aero/solidworks)
   - [CATIA V5/V6 Plugin](https://plugins.ideale-eu.aero/catia)
   - [Siemens NX Plugin](https://plugins.ideale-eu.aero/nx)
   - [PTC Creo Plugin](https://plugins.ideale-eu.aero/creo)
3. Run installer and authenticate with IDEALE-EU credentials
4. Restart CAD application
5. Verify plugin appears in toolbar/ribbon

#### Create Your First Digital Passport

1. Open a CAD assembly or part
2. Click **IDEALE-EU > Create Digital Passport**
3. Fill in metadata:
   - Part number (follow your company PN format)
   - Part name and description
   - TFA domain assignment (e.g., AAA for airframe parts)
   - Material specification
   - Manufacturing process
   - Supplier (if outsourced)
4. Click **Generate Passport**
5. System creates QS-anchored digital passport
6. Unique passport ID displayed (e.g., `PP-AAA-2025-001234`)

#### Link to Program Structure

1. Navigate to **Programs > [Your Program]**
2. Find appropriate directory (e.g., `02-DESIGN/AAA/Structures`)
3. Click **Link Component**
4. Select your digital passport
5. Confirm linkage
6. Component now appears in program tree with full traceability

### For Program Managers

#### Set Up New Program

1. Navigate to **Programs > Create New Program**
2. Enter program details:
   - Program name (e.g., "BWB-X Hydrogen Demonstrator")
   - Program code (e.g., "BWB-H2-01")
   - Start/end dates
   - Certification basis (FAA Part 25, EASA CS-25)
3. Select applicable TFA domains:
   - ☑ AAA (Airframes)
   - ☑ CQH (Cryogenics-H2)
   - ☑ PPP (Propulsion)
   - ☑ EEE (Electrical)
   - ☑ LIB (Logistics)
   - (Others as needed)
4. Create program structure (00-10 directories auto-generated)
5. Invite team members with role assignments
6. Define configuration management workflows (ECR/ECO/CCB)

#### Configure Workflows

1. Navigate to **Program Settings > Workflows**
2. Customize ECR/ECO/CCB routing:
   - Approval chains by change classification
   - Automated notifications
   - Integration with PLM system
3. Set up gates between CAx phases:
   - CAD→CAE: Design freeze required
   - CAE→CAV: Analysis completion gate
   - CAV→CMP: Certification approval gate
4. Define QS anchoring policies:
   - Frequency (every save, daily, at milestones)
   - Evidence types (CAD models, simulations, test results)
   - Blockchain bridge settings (if consortium requires)

### For Auditors

#### Access Audit Portal

1. Navigate to **Audit Dashboard**
2. Search for component by:
   - Serial number
   - Part number
   - Aircraft registration
   - Program code
3. View complete digital passport:
   - Design history (CAD versions)
   - Analysis results (CAE)
   - Manufacturing records (CAM/CAP)
   - Test evidence (CAV)
   - Configuration changes (CMP)
   - QS anchors (cryptographic proof)

#### Generate Certification Package

1. Select component or system
2. Click **Export > Certification Package**
3. Choose format:
   - PDF with embedded evidence
   - S1000D data modules (CSDB)
   - XML for regulatory submission
4. Package includes:
   - Complete traceability from requirements
   - All test results with QS anchors
   - Material certifications
   - Supplier documentation
   - Configuration history
5. Download package with cryptographic signature
6. Submit to certification authority

### For Suppliers

#### Register Components

1. Navigate to **Supplier Portal**
2. Click **Register New Component**
3. Upload documentation:
   - Material certifications
   - Manufacturing process sheets
   - Quality inspection reports
   - Dimensional inspection data
4. Enter traceability:
   - Batch/lot numbers
   - Manufacturing date
   - Serial numbers (if serialized)
5. Link to customer program (if known)
6. System generates digital passport
7. Receive confirmation with passport ID

#### Track Shipments

1. Navigate to **Shipments**
2. Create new shipment:
   - Select components (digital passport IDs)
   - Destination and shipping date
   - Carrier and tracking number
3. System updates component status
4. Customer receives notification
5. Upon delivery confirmation, component status updates to "In Customer Possession"

## Step 4: Core Workflows

### Configuration Management (ECR/ECO/CCB)

#### Submit Engineering Change Request (ECR)

1. Navigate to **Configuration > ECR/ECO > New ECR**
2. Fill in ECR form:
   - Problem statement: What needs to change and why
   - Affected components: Select from digital passport registry
   - Proposed solution: High-level description
   - Impact assessment: Cost, schedule, safety, performance
3. Attach supporting evidence (CAE results, test data, photos)
4. Submit for review
5. System routes to stakeholders based on affected domains
6. Track ECR status in real-time

#### Approval and ECO Issuance

1. Stakeholders review and comment
2. CCB meeting scheduled (if required)
3. Upon approval, ECR converts to ECO
4. Detailed implementation plan created:
   - Updated CAD models
   - Revised manufacturing instructions
   - Test/validation requirements
   - Implementation timeline
5. ECO issued with QS anchor
6. Affected components updated in digital passports
7. Audit trail maintained for entire change lifecycle

### Digital Twin and Federated Learning

#### Create Digital Twin

1. Select physical asset (aircraft, engine, component)
2. Click **Digital Twin > Create Twin**
3. System aggregates:
   - Design data (CAD geometry, properties)
   - Simulation models (CAE)
   - Manufacturing as-built data
   - Sensor/IoT integration (if available)
4. Digital twin synchronized with physical asset
5. Real-time updates from operations (if connected)

#### Enable Federated Learning

1. Navigate to **Analytics > Federated Learning**
2. Define learning objective:
   - Predictive maintenance (predict component failures before they occur)
   - Performance optimization (fuel efficiency)
   - Safety analysis (anomaly detection)
3. Configure privacy settings:
   - Data sovereignty (data stays local)
   - Model parameters shared only
   - Anonymization rules
4. Join fleet learning consortium
5. **QS pre-event capture** works as follows:
   - System continuously monitors and creates QS anchors (superposition of possible states)
   - Multiple potential outcomes exist with assigned probabilities
   - When anomaly/event occurs, superposition collapses to classical outcome (CB anchor)
   - Both QS (pre-event superposition) and CB (post-event reality) preserved immutably
   - Delta analysis: predicted QS probabilities vs actual CB outcome
   - Federated learning uses QS→CB pairs to improve future predictions
6. Receive collective intelligence from fleet without exposing proprietary data

## Step 5: Integration with Existing Tools

### PLM Integration

**Supported Systems**:
- Siemens Teamcenter
- Dassault 3DEXPERIENCE
- PTC Windchill
- Aras Innovator

**Integration Steps**:
1. Navigate to **Settings > Integrations > PLM**
2. Select your PLM system
3. Provide connection details:
   - Server URL
   - Authentication credentials (OAuth recommended)
   - Mapping rules (IDEALE-EU ↔ PLM data model)
4. Test connection
5. Enable bi-directional sync:
   - CAD models → IDEALE-EU digital passports
   - ECR/ECO workflows ↔ PLM change management
   - BOM synchronization
6. Schedule sync frequency (real-time, hourly, daily)

### ERP Integration

**Supported Systems**:
- SAP
- Oracle E-Business Suite
- Microsoft Dynamics 365

**Integration Steps**:
1. Navigate to **Settings > Integrations > ERP**
2. Configure data exchange:
   - Part master data sync
   - Purchase orders linked to digital passports
   - Invoice matching with delivery verification
   - Inventory tracking
3. Enable smart contracts for:
   - Automated payment release upon QS-verified delivery
   - Warranty claims processing
   - Supplier performance scoring

## Step 6: Best Practices

### Digital Passport Strategy

✅ **Do**:
- Create digital passports early (at design phase)
- Implement QS pre-event anchoring for critical components (captures superposition before events)
- Use CB post-event anchoring to record actual outcomes
- Link components to program structure
- Maintain as-designed vs as-built reconciliation
- Leverage QS→CB validation pairs for federated learning

❌ **Don't**:
- Wait until manufacturing to create passports
- Skip QS pre-event anchoring for predictive-critical components
- Create duplicate passports for same component
- Ignore "to scale" validation requirements
- Share raw flight data (use federated learning with QS→CB pairs instead)

### Configuration Management

✅ **Do**:
- Use ECR for all proposed changes
- Include thorough impact analysis
- QS-anchor CCB meeting minutes
- Update affected digital passports immediately
- Maintain frozen baselines for certifications

❌ **Don't**:
- Make changes without ECR/ECO process
- Skip stakeholder reviews
- Lose traceability of change rationale
- Allow backdated changes (QS prevents this)

### Scaling from Prototype to Production

✅ **Do**:
- Re-validate simulations (CAE) at production scale
- Use digital twins to predict scaling effects
- QS-anchor both prototype and production data
- Leverage federated learning for scaling insights
- Plan for "to scale" validation early

❌ **Don't**:
- Assume linear scaling of physics
- Skip production-scale testing
- Neglect to document scaling assumptions
- Ignore fleet data when available

## Step 7: Get Help

### Support Resources

- **Documentation**: [https://docs.ideale-eu.aero](https://docs.ideale-eu.aero)
- **API Reference**: [https://api.ideale-eu.aero](https://api.ideale-eu.aero)
- **Community Forum**: [https://community.ideale-eu.aero](https://community.ideale-eu.aero)
- **Video Tutorials**: [https://learn.ideale-eu.aero](https://learn.ideale-eu.aero)

### Contact Support

- **Email**: support@ideale-eu.aero
- **Phone**: +32 2 XXX XXXX (EU) | +1 XXX XXX XXXX (US)
- **Live Chat**: Available in portal (Mon-Fri 09:00-18:00 CET)

### Training Programs

- **Engineer Onboarding**: 2-day course covering CAD integration and digital passports
- **Program Manager Training**: 1-day course on program setup and workflows
- **Auditor Certification**: Half-day course on audit dashboard and evidence verification
- **Supplier Integration**: 4-hour workshop on portal usage and API integration

### Webinars and Events

- **Monthly Webinar Series**: "IDEALE-EU Best Practices"
- **Quarterly User Conference**: Networking and advanced topics
- **Annual Summit**: Roadmap previews and industry trends

## Next Steps

Now that you're set up, explore:

- [TFA Domains Reference](/docs/tfa-domains/) - Understand the 15 domains
- [CAx Lifecycle](/docs/cax-lifecycle/) - Learn about 9 phases and "to scale"
- [API Reference](/api/) - Programmatic access for advanced integrations
- [PLUMA Quick Start](./00-PROGRAM/PLUMA/QUICK_START.md) - Product Lifecycle UiX Management Automation

---

*Welcome to the future of aerospace lifecycle management. Start building tamper-proof digital passports today.*
