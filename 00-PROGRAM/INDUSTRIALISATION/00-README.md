# INDUSTRIALISATION

Manufacturing readiness, DFM/DFA (Design for Manufacturing/Assembly), and production planning documentation.

## Overview

This directory contains comprehensive industrialisation documentation covering the entire manufacturing lifecycle from strategy through production readiness for both aircraft and spacecraft vehicles.

## Contents

- **00-README.md** - This file
- **01-STRATEGY/** - Industrialisation strategy, footprint, make/buy, and ramp planning
- **02-FACTORY_DESIGN/** - Plant layout, line design, and ergonomics/EHS
- **03-PROCESS_PLANNING/** - Process flow, PFMEA, control plans, and special processes
- **04-MBOM_ROUTINGS/** - Manufacturing BOM, routings, and line balancing
- **05-TOOLING_JIGS_FIXTURES/** - Tool design, jigs, fixtures, and gauge calibration
- **06-WORK_INSTRUCTIONS/** - EWIS, operation sheets, and visual aids
- **07-SUPPLIER_INDUSTRIALISATION/** - APQP, PPAP, and supplier audits
- **08-QUALITY/** - AS9102 FAI, MSA/SPC, NCR/CAPA, and inspection plans
- **09-LOGISTICS/** - Material flow, kitting, warehouse, and traceability/RFID
- **10-TEST_INSPECTION/** - Test rigs, ATE, NDT, and functional testing
- **11-PRR/** - Production Readiness Review checklists and evidence
- **12-RATE_READINESS/** - Capacity models, takt/OEE, and bottleneck analysis
- **13-TRAINING_COMPETENCY/** - Skill matrix and certification records
- **14-MAINTENANCE_TPM/** - Preventive maintenance plans and spares/tool control
- **15-COSTING_STD_TIMES/** - Should-cost models and time studies
- **16-IT_INTEGRATION/** - MES, ERP, QMS, and PLM links
- **17-COMPLIANCE_LINKS/** - Configuration management baselines and digital thread hooks
- **18-TEMPLATES/** - Standard templates for work instructions, PFMEA, control plans, and PRR
- **19-METRICS/** - SQDCME dashboard, FPY/scrap, on-time readiness, and lessons learned
- **20-AIRCRAFT_LINE/** - Aircraft-specific final assembly layout, tooling, and startup readiness
- **21-SPACECRAFT_AIT_LINE/** - Spacecraft-specific AIT cleanroom, GSE tooling, and readiness

## Industrialisation Philosophy

The industrialisation approach follows aerospace industry best practices:

1. **Early DFM/DFA** - Design for Manufacturing and Assembly from initial design phases
2. **Concurrent Engineering** - Parallel development of product and manufacturing processes
3. **Risk-Based Planning** - PFMEA and control plans drive process design
4. **Lean Manufacturing** - Flow optimization, waste elimination, and continuous improvement
5. **Digital Thread** - Seamless EBOM→MBOM→routing→work instruction flow
6. **Supplier Partnership** - APQP and PPAP ensure supply chain readiness
7. **Quality Built-In** - Mistake-proofing and in-process verification
8. **Rate Readiness** - Capacity modeling and takt time planning for production ramp

## Key Integration Points

### With Design Engineering
- DFM/DFA feedback loops
- Tolerance analysis and stack-up studies
- Material and process selection
- Producibility assessments

### With Quality
- Control plans aligned with inspection plans
- First Article Inspection (FAI) per AS9102
- Statistical Process Control (SPC)
- Non-Conformance Report (NCR) and Corrective Action/Preventive Action (CAPA)

### With Supply Chain
- Make/buy decisions
- Supplier industrialisation (APQP/PPAP)
- Supplier audits and qualification
- Supply chain capacity planning

### With IT Systems
- PLM/PDM for EBOM management
- ERP for MBOM and routing management
- MES for shop floor execution
- QMS for quality data management

## Standards and Compliance

### Aerospace Standards
- **AS9100** - Quality Management Systems for Aviation, Space, and Defense
- **AS9102** - First Article Inspection Requirement
- **AS9145** - Advanced Product Quality Planning (APQP) and Production Part Approval Process (PPAP)
- **ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
- **DO-178C/DO-254** - Software and hardware airworthiness considerations

### Spacecraft Standards
- **ECSS-Q-ST-10-09** - Nonconformance control system
- **ECSS-Q-ST-10-04** - Inspection
- **ECSS-M-ST-10** - Space project management and organization
- **ECSS-E-ST-10-02** - Verification

### Lean and Quality Tools
- Six Sigma DMAIC
- 5S workplace organization
- Visual management
- Kaizen continuous improvement
- Total Productive Maintenance (TPM)

## Stage Gates

Production readiness is tracked through key milestones:

- **MCR (Manufacturing Concept Review)** - Manufacturing strategy and footprint approved
- **PDR (Preliminary Design Review)** - Process concepts and layouts defined
- **CDR (Critical Design Review)** - Process validation complete, tooling designed
- **TRR (Test Readiness Review)** - Production test capability demonstrated
- **PRR (Production Readiness Review)** - All manufacturing systems ready for production
- **ORR (Operational Readiness Review)** - Full rate production capability verified

## Metrics

Key manufacturing metrics tracked:

- **FPY (First Pass Yield)** - % of units passing first time
- **Scrap Rate** - % of material/parts scrapped
- **Rework Rate** - % of units requiring rework
- **Takt Time** - Available time / customer demand
- **OEE (Overall Equipment Effectiveness)** - Availability × Performance × Quality
- **DPMO (Defects Per Million Opportunities)** - Quality metric
- **Schedule Adherence** - On-time delivery performance
- **Cost Variance** - Actual vs. target manufacturing cost
