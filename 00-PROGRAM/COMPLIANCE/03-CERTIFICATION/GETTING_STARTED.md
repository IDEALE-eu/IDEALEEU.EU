---
area: "00-PROGRAM/COMPLIANCE/03-CERTIFICATION"
owner: "Certification Manager"
status: "Active - Enhanced"
date: "2025-10-16"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/CERTIFICATION"
confidentiality: "Internal"
---

# 03-CERTIFICATION - Implementation Guide

## Overview

This directory contains the complete certification framework for aerospace products (aircraft and spacecraft), providing detailed plans, checklists, and tracking systems to achieve Type Certification (aviation) or Mission Approval (space).

## Quick Start Guide

### For New Programs

1. **Phase A-B (Concept/Preliminary Design)**
   - Review certification basis and applicable standards
   - Start with [`CERTIFICATION_PACKAGES/PDR_COMPLIANCE/`](CERTIFICATION_PACKAGES/PDR_COMPLIANCE/)
   - Complete PDR compliance checklist
   - Engage with certification authority

2. **Phase C (Detailed Design)**
   - Develop detailed certification plans using templates in [`CERTIFICATION_PLANS/`](CERTIFICATION_PLANS/)
   - For Aviation: Use PSAC and PHAC templates
   - For Space: Use Mission Assurance Plan template
   - Complete CDR compliance checklist
   - Obtain authority approval of plans

3. **Phase D (Development)**
   - Execute per approved plans
   - Populate compliance checklists in [`COMPLIANCE_CHECKLISTS/`](COMPLIANCE_CHECKLISTS/)
   - Qualify tools using [`TOOL_QUALIFICATION/`](TOOL_QUALIFICATION/) templates
   - Track authority correspondence in [`AUTHORITY_CORRESPONDENCE/`](AUTHORITY_CORRESPONDENCE/)
   - Prepare for TRR using TRR compliance checklist

4. **Phase E (Verification)**
   - Complete all compliance checklist items
   - Collect evidence (reference evidence index)
   - Prepare statements of compliance
   - Prepare for certification audit

5. **Phase F (Certification)**
   - Complete final certification package using [`CERTIFICATION_PACKAGES/FINAL_CERT/`](CERTIFICATION_PACKAGES/FINAL_CERT/)
   - Submit to certification authority
   - Resolve any findings
   - Obtain Type Certificate or Mission Approval

## Directory Structure

```
03-CERTIFICATION/
├── README.md (this file)
├── GETTING_STARTED.md (implementation guide - you are here)
│
├── CERTIFICATION_PLANS/          # Detailed certification strategy documents
│   ├── README.md
│   ├── AVIATION/
│   │   ├── PSAC_DO178C.md       # Plan for Software Aspects of Certification
│   │   ├── PHAC_DO254.md        # Plan for Hardware Aspects of Certification
│   │   ├── CMP.md               # Certification Maintenance Plan (create as needed)
│   │   └── CERTIFICATION_BASIS.md (create as needed)
│   └── SPACE/
│       ├── MISSION_ASSURANCE_PLAN.md  # Mission Assurance per ECSS-Q-ST-80
│       ├── SAFETY_CASE.md             # (create as needed)
│       └── LAUNCH_APPROVAL_PACKAGE.md (create as needed)
│
├── COMPLIANCE_CHECKLISTS/        # Objective-by-objective tracking
│   ├── README.md
│   ├── DO_178C_CHECKLIST.csv    # Software objectives (60+ items)
│   ├── DO_254_CHECKLIST.csv     # Hardware objectives (80+ items)
│   ├── ECSS_Q_CHECKLIST.csv     # ECSS Quality objectives (70+ items)
│   ├── ARP4754A_CHECKLIST.csv   # (create as needed)
│   └── ARP4761_CHECKLIST.csv    # (create as needed)
│
├── CERTIFICATION_PACKAGES/       # Phase-appropriate deliverables
│   ├── README.md
│   ├── PDR_COMPLIANCE/
│   │   ├── README.md
│   │   └── PDR_COMPLIANCE_CHECKLIST.csv
│   ├── CDR_COMPLIANCE/
│   │   ├── README.md
│   │   └── CDR_COMPLIANCE_CHECKLIST.csv
│   ├── TRR_COMPLIANCE/
│   │   ├── README.md
│   │   └── TRR_COMPLIANCE_CHECKLIST.csv
│   ├── PRR_COMPLIANCE/
│   │   └── README.md
│   └── FINAL_CERT/
│       ├── README.md
│       └── FINAL_CERTIFICATION_CHECKLIST.csv
│
├── TOOL_QUALIFICATION/           # Tool qualification packages
│   ├── README.md
│   ├── TOOL_QUALIFICATION_LOG.csv (tracking 10+ tools)
│   └── EXAMPLE_TOOL/
│       └── TOOL_QUALIFICATION_PLAN_TEMPLATE.md
│
├── AUTHORITY_CORRESPONDENCE/     # Authority interaction tracking
│   ├── README.md
│   ├── QUESTIONS_AND_RESPONSES/
│   │   └── QUESTIONS_LOG.csv
│   ├── FINDING_REPORTS/
│   │   └── FINDINGS_LOG.csv
│   ├── ISSUE_PAPERS/
│   │   └── ISSUE_PAPERS_INDEX.csv
│   └── MEETING_MINUTES/
│       └── MEETING_SCHEDULE.csv
│
├── STATEMENTS_OF_COMPLIANCE/     # Formal compliance declarations
│   └── README.md
│
├── PLAN_FOR_SOCC.md             # Master certification strategy
├── CERTIFICATION_MILESTONES.csv # Key milestone tracking
├── COMPLIANCE_ISSUES_LOG.csv    # Issue tracking
└── TOOL_QUALIFICATION_LOG.csv   # Tool qualification tracking
```

## Key Artifacts Created

### 1. Certification Plans (Templates Ready to Customize)
- ✅ **PSAC (DO-178C)**: Complete 15-section plan for software certification
- ✅ **PHAC (DO-254)**: Complete 17-section plan for hardware certification
- ✅ **Mission Assurance Plan**: Complete 16-section plan for space missions per ECSS

### 2. Compliance Checklists (Populated and Ready)
- ✅ **DO-178C**: 60+ software objectives with traceability columns
- ✅ **DO-254**: 80+ hardware objectives with verification methods
- ✅ **ECSS-Q**: 70+ quality and mission assurance objectives

### 3. Tool Qualification System
- ✅ **Tool Qualification Log**: 10 example tools with TQL levels
- ✅ **Tool Qualification Plan Template**: 15-section comprehensive template
- ✅ Directory structure for tool qualification packages

### 4. Phase-Appropriate Packages
- ✅ **PDR Package**: 16-item checklist for preliminary design
- ✅ **CDR Package**: 28-item checklist for detailed design
- ✅ **TRR Package**: 29-item checklist for test readiness
- ✅ **Final Certification**: 36-item checklist for certification submittal

### 5. Authority Engagement
- ✅ Questions and responses tracking initialized
- ✅ Framework for findings, issue papers, and meeting minutes

## How to Use This Framework

### For Aviation Products

1. **Select Applicable Standards**
   - DO-178C for software
   - DO-254 for hardware
   - ARP4754A for systems engineering
   - ARP4761 for safety assessment

2. **Customize Plans**
   - Start with PSAC template for software
   - Start with PHAC template for hardware
   - Fill in program-specific information (marked with [brackets])
   - Submit to authority for approval

3. **Track Compliance**
   - Use DO-178C checklist for software objectives
   - Use DO-254 checklist for hardware objectives
   - Update status as work progresses
   - Reference evidence location

4. **Qualify Tools**
   - Identify all tools used
   - Determine qualification level (TQL-1 through TQL-5)
   - Use tool qualification plan template
   - Update tool qualification log

### For Space Missions

1. **Select Applicable Standards**
   - ECSS-Q-ST-10: Product assurance management
   - ECSS-Q-ST-20: Quality assurance
   - ECSS-Q-ST-60: Parts, materials, processes
   - ECSS-Q-ST-70: Materials and mechanical parts
   - ECSS-Q-ST-80: Software product assurance

2. **Customize Plans**
   - Start with Mission Assurance Plan template
   - Tailor to mission category (1, 2, or 3)
   - Align with mission phases
   - Coordinate with ESA or other space agencies

3. **Track Compliance**
   - Use ECSS-Q checklist for quality objectives
   - Track safety requirements separately
   - Monitor reliability predictions
   - Document nonconformances and corrective actions

## Certification Authority Engagement

### Key Milestones for Authority Review

1. **Phase B Exit (PDR)**
   - Certification basis presentation
   - Means of compliance agreement
   - Authority engagement plan approval

2. **Phase C Exit (CDR)**
   - PSAC/PHAC approval
   - Tool qualification approach approval
   - Development standards approval

3. **Phase D Mid (TRR)**
   - Mid-development status review
   - Compliance progress review
   - Issue resolution

4. **Phase E (Certification Audit)**
   - Authority audit of compliance evidence
   - Findings resolution
   - Statement of Compliance review

5. **Phase F (Type Certificate)**
   - Final certification package submittal
   - Type Certificate Data Sheet
   - Type Certificate issuance

### Authority Coordination

Track all authority interactions in [`AUTHORITY_CORRESPONDENCE/`](AUTHORITY_CORRESPONDENCE/):
- **Questions**: Use QUESTIONS_LOG.csv
- **Findings**: Use FINDINGS_LOG.csv  
- **Complex Topics**: Prepare Issue Papers
- **Meetings**: Document in MEETING_MINUTES/

## Compliance Demonstration Methods

### Test
- Requirements-based testing
- Robustness testing
- Hardware/software integration testing
- Environmental testing

### Analysis
- Safety analysis (FHA, FTA, FMEA)
- Performance analysis
- Timing and resource analysis
- Structural coverage analysis

### Review
- Requirements reviews
- Design reviews
- Code reviews
- Documentation reviews

### Inspection
- Hardware inspection
- Configuration verification
- Manufacturing process inspection

## Tool Qualification Levels

| Level | Type | Qualification Required | Example Tools |
|-------|------|----------------------|---------------|
| TQL-1 | Development | Full qualification | Compilers, code generators, HDL synthesizers |
| TQL-2 | Verification (critical) | Substantial qualification | Test execution tools, coverage analyzers |
| TQL-3 | Verification (moderate) | Moderate qualification | Static analyzers, timing analyzers |
| TQL-4 | Verification (low) | Minimal qualification | Test frameworks with manual verification |
| TQL-5 | Support | No qualification | Editors, viewers, document tools |

See [`TOOL_QUALIFICATION/README.md`](TOOL_QUALIFICATION/README.md) for details.

## Common Questions

### Q: Which certification plan do I need?
**A**: 
- Aviation software → PSAC (DO-178C)
- Aviation hardware → PHAC (DO-254)
- Space missions → Mission Assurance Plan (ECSS)
- Often need multiple plans for complete system

### Q: How do I determine Design Assurance Level (DAL)?
**A**: Based on system safety assessment (ARP4761):
- Level A: Catastrophic failure
- Level B: Hazardous failure
- Level C: Major failure
- Level D: Minor failure
- Level E: No safety effect

### Q: Do all tools need qualification?
**A**: No. Only tools that:
- Generate certification data (TQL-1)
- Verify certification data without further verification (TQL-2)
- Could fail to detect errors (TQL-3)

Tools used for information only (TQL-5) don't require qualification.

### Q: When should I engage the certification authority?
**A**: As early as possible:
- Phase A: Initial consultation
- Phase B: Certification basis agreement
- Phase C: Plan approval
- Phase D: Mid-development review
- Phase E: Certification audit
- Regular updates throughout

### Q: What if I can't comply with standard guidance?
**A**: 
1. Document deviation rationale
2. Propose alternative means of compliance
3. Prepare Issue Paper
4. Submit to authority for approval
5. Track in compliance checklist and plans

## Integration with Other Systems

### Configuration Management
- Baselines in [`../../CONFIG_MGMT/04-BASELINES/`](../../CONFIG_MGMT/04-BASELINES/)
- Change control process
- Configuration audits

### Evidence Index
- Evidence location: [`../06-EVIDENCE/EVIDENCE_INDEX.csv`](../06-EVIDENCE/EVIDENCE_INDEX.csv)
- Evidence archives
- Traceability

### Compliance Matrix
- Requirements compliance: [`../05-REGISTERS/COMPLIANCE_MATRIX.csv`](../05-REGISTERS/COMPLIANCE_MATRIX.csv)
- Verification methods
- Status tracking

### Risk Management
- Certification risks: [`../../RISK_REGISTER.md`](../../RISK_REGISTER.md)
- Risk mitigation
- Risk acceptance

## Success Metrics

Track these key metrics:
- ✅ Compliance checklist completion percentage
- ✅ Open authority findings (count and age)
- ✅ Tool qualification status
- ✅ Evidence gaps
- ✅ Schedule adherence to certification milestones
- ✅ Authority review cycle time

## Next Steps

1. **Review applicable standards** for your program
2. **Complete PDR compliance checklist** for Phase B
3. **Customize certification plans** using templates
4. **Populate compliance checklists** as work progresses
5. **Qualify tools** early in Phase C
6. **Engage authority** at each milestone
7. **Collect evidence** systematically
8. **Track everything** in provided logs and checklists

## Support and Resources

### Internal Resources
- Certification Manager: Primary point of contact
- Systems Engineering: Requirements and architecture
- Quality Assurance: Process compliance
- Configuration Management: Baseline control

### External Resources
- EASA: European Union Aviation Safety Agency
- FAA: Federal Aviation Administration  
- ESA: European Space Agency
- SAE International: ARP standards
- RTCA: DO standards
- ECSS: European space standards

## Document Control

**Version**: 2.0 (Enhanced)  
**Date**: 2025-10-16  
**Author**: Certification Team  
**Status**: Active Implementation

**Changes from v1.0**:
- Added complete certification plan templates (PSAC, PHAC, MAP)
- Populated compliance checklists with 200+ objectives
- Created phase-appropriate package checklists
- Established tool qualification framework with examples
- Enhanced authority correspondence tracking

---

**For questions or support, contact the Certification Manager.**

**Remember**: Certification is a journey, not a destination. Start early, engage often, document everything.
