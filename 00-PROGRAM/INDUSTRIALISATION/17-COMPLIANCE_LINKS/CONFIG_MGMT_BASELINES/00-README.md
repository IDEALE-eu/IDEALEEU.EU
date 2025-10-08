# CONFIG_MGMT_BASELINES

Configuration management and product baselines.

## Overview

Configuration management (CM) ensures product integrity through formal control of design, documentation, and changes.

## CM Baselines

### Functional Baseline
- Requirements and specifications
- What the product must do

### Design Baseline
- Design documentation (drawings, models, specs)
- Design freeze at CDR

### Product Baseline
- As-built configuration
- Actual serial number configuration

## Configuration Control

### Engineering Changes
- ECN (Engineering Change Notice) process
- Impact analysis (cost, schedule, performance)
- Approval workflow
- Effectivity (which serial numbers affected)

### Change Classification
- **Class I:** Major impact, customer approval required
- **Class II:** Minor impact, internal approval
- **Emergency:** Safety or regulatory, fast-track

### Deviation/Waiver
- One-time departure from requirements
- Engineering approval required
- Tracked and dispositioned

## Configuration Identification

- Part numbering system
- Revision levels
- Serial number assignment
- Configuration item hierarchy

## Configuration Status Accounting

- Track configuration of each serial number
- As-designed vs. as-built differences
- Change implementation status
- Configuration audits

## Links

- To **DIGITAL_THREAD_HOOKS/** for data integration
- To **00-PROGRAM/CONFIG_MGMT/** for program CM
- To **09-LOGISTICS/TRACEABILITY_RFID/** for as-built tracking
- To **16-IT_INTEGRATION/PLM_LINKS/** for engineering data
