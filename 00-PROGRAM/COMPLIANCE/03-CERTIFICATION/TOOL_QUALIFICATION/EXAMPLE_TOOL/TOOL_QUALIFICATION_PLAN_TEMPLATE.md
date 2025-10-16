---
document_id: "TQP-EXAMPLE-001"
title: "Tool Qualification Plan - [Tool Name]"
tool_name: "[Tool Name]"
tool_version: "[Version]"
tool_vendor: "[Vendor]"
qualification_level: "TQL-[1/2/3/4/5]"
version: "1.0"
status: "Draft"
date: "2025-10-16"
---

# Tool Qualification Plan (TQP)
## [Tool Name] [Version]

## 1. Purpose and Scope

### 1.1 Purpose
This Tool Qualification Plan (TQP) defines the approach for qualifying [Tool Name] [Version] for use in the certification of [Product Name] per DO-178C Section 12 / DO-254 Section 11 / DO-330.

### 1.2 Scope
This plan covers:
- Tool assessment and qualification level determination
- Tool operational requirements
- Tool verification approach
- Tool configuration management
- Tool qualification deliverables

### 1.3 Tool Description
**Tool Name**: [Tool Name]  
**Version**: [Version]  
**Vendor**: [Vendor]  
**Tool Type**: [Development / Verification]  
**Qualification Level**: TQL-[1/2/3/4/5]

## 2. Tool Assessment

### 2.1 Tool Usage
The tool will be used for:
- [Primary usage description]
- [Secondary usage description]
- [Additional uses]

### 2.2 Tool Output
Tool outputs include:
- [Output type 1] - [Usage in certification]
- [Output type 2] - [Usage in certification]
- [Output type 3] - [Usage in certification]

### 2.3 Tool Error Impact
**Error Impact Analysis**:
- Type of errors the tool could introduce: [Description]
- Consequence if error goes undetected: [Description]
- Likelihood of detection by other means: [High/Medium/Low]

### 2.4 Qualification Level Determination
Based on DO-330 criteria:

**TQL-1**: Development tool whose output is part of airborne software/hardware and could insert an error.
- [ ] Applies to this tool

**TQL-2**: Verification tool whose output is used to satisfy verification without further verification.
- [ ] Applies to this tool

**TQL-3**: Verification tool whose output inspected and could fail to detect an error.
- [ ] Applies to this tool

**TQL-4**: Verification tool that automates verification process, output independently verified.
- [ ] Applies to this tool

**TQL-5**: Tool output used for information only or independently verified.
- [ ] Applies to this tool (no qualification required)

**Determined Qualification Level**: TQL-[X]

**Rationale**: [Justification for qualification level]

## 3. Tool Operational Requirements (TOR)

### 3.1 Functional Requirements
The tool shall:
1. [Functional requirement 1]
2. [Functional requirement 2]
3. [Functional requirement 3]
4. [Continue as needed...]

### 3.2 Operational Scenarios
The tool will be used in the following scenarios:
1. **Scenario 1**: [Description]
   - Input: [Input description]
   - Expected Output: [Expected output]
   - Success Criteria: [Criteria]

2. **Scenario 2**: [Description]
   - Input: [Input description]
   - Expected Output: [Expected output]
   - Success Criteria: [Criteria]

### 3.3 Error Detection Requirements
The tool shall detect and report:
- Invalid inputs: [How detected]
- Processing errors: [How detected]
- Resource limitations: [How detected]
- Configuration errors: [How detected]

### 3.4 Tool Limitations
Known limitations of the tool:
- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

Mitigation:
- [How limitation is managed in usage]

## 4. Tool Qualification Approach

### 4.1 Qualification Method
**Selected Approach**: [Choose one or combination]
- [ ] Tool Qualification by Tool Developer (vendor-provided qualification)
- [ ] Tool Qualification by Tool User (develop qualification package)
- [ ] Tool Output Verification (verify each output manually)

**Rationale**: [Justification for selected approach]

### 4.2 Qualification Activities
Activities to be performed:

| Activity | Responsibility | Target Date | Status |
|----------|----------------|-------------|--------|
| Tool Assessment Report | [Role] | [Date] | Planned |
| Tool Operational Requirements | [Role] | [Date] | Planned |
| Tool Verification Plan | [Role] | [Date] | Planned |
| Tool Verification Procedures | [Role] | [Date] | Planned |
| Tool Verification Execution | [Role] | [Date] | Planned |
| Tool Qualification Summary | [Role] | [Date] | Planned |
| Tool Configuration Documentation | [Role] | [Date] | Planned |

### 4.3 Verification Methods
Tool verification will use:
- **Requirements-Based Testing**: Verify tool operational requirements
- **Functional Testing**: Verify tool functions correctly
- **Boundary Testing**: Verify tool behavior at limits
- **Error Handling Testing**: Verify error detection and reporting
- **Comparison Testing**: Compare tool output to known good results
- **Historical Performance**: Review service history and problem reports

## 5. Tool Verification Requirements

### 5.1 Verification Test Cases
Test cases will verify each Tool Operational Requirement:

| TOR ID | Test Case ID | Test Description | Expected Result |
|--------|--------------|------------------|-----------------|
| TOR-1 | TC-001 | [Description] | [Expected] |
| TOR-2 | TC-002 | [Description] | [Expected] |
| TOR-3 | TC-003 | [Description] | [Expected] |

### 5.2 Verification Coverage
- All Tool Operational Requirements will be verified
- Operational scenarios will be tested
- Error detection capabilities will be verified
- Tool limitations will be documented and verified

### 5.3 Acceptance Criteria
Tool qualification is complete when:
- All Tool Operational Requirements verified
- All verification test cases pass
- All discrepancies resolved or documented
- Tool Qualification Summary approved
- Configuration documented and controlled

## 6. Tool Configuration Management

### 6.1 Tool Identification
- **Tool Name**: [Name]
- **Version**: [Version number]
- **Release Date**: [Date]
- **Vendor Part Number**: [P/N]
- **License Type**: [License info]
- **Installation Location**: [Path/server]

### 6.2 Configuration Control
- Tool version locked for certification
- Changes require re-qualification assessment
- Configuration documented in Tool Qualification Data
- Installation procedure documented
- Configuration verification procedure defined

### 6.3 Tool Configuration Items
Configuration items under control:
- Tool executable(s)
- Configuration files
- License files
- Supporting libraries
- Installation scripts
- User documentation

### 6.4 Change Management
If tool changes are required:
1. Document change request
2. Perform impact analysis
3. Determine need for re-qualification
4. Update Tool Qualification Data
5. Re-verify affected requirements
6. Update Tool Qualification Summary

## 7. Tool Qualification Data (TQD)

### 7.1 TQD Contents
Tool Qualification Data will include:
- Tool Assessment Report (TAR)
- Tool Qualification Plan (TQP) - this document
- Tool Operational Requirements (TOR)
- Tool Verification Procedures
- Tool Verification Results
- Tool Configuration Documentation
- Tool User Documentation
- Tool Installation Procedures
- Tool Qualification Summary (TQS)

### 7.2 TQD Organization
```
TOOL_QUALIFICATION/[ToolName_Version]/
├── [ToolName]_TAR.md (Tool Assessment Report)
├── [ToolName]_TQP.md (Tool Qualification Plan - this document)
├── [ToolName]_TOR.md (Tool Operational Requirements)
├── [ToolName]_TQS.md (Tool Qualification Summary)
└── [ToolName]_TQD/ (Tool Qualification Data)
    ├── TEST_PROCEDURES/
    │   ├── TP-001_[Description].md
    │   └── TP-002_[Description].md
    ├── TEST_RESULTS/
    │   ├── TR-001_[Results].md
    │   └── TR-002_[Results].md
    ├── CONFIGURATION_DOCS/
    │   ├── Installation_Procedure.md
    │   ├── Configuration_Specification.md
    │   └── Version_Verification.md
    └── USER_DOCUMENTATION/
        ├── User_Manual.pdf
        └── Operating_Procedures.md
```

## 8. Tool Vendor Qualification Data

### 8.1 Vendor-Provided Qualification
If using vendor-provided qualification:
- Vendor qualification package reviewed
- Applicability to our usage verified
- Gaps identified and addressed
- Vendor support agreement in place
- Tool configuration matches qualified configuration

### 8.2 Vendor Documentation
Vendor documentation includes:
- Tool Requirements Specification
- Tool Design Description
- Tool Verification Report
- Tool Configuration Management Data
- Tool Problem Reports

### 8.3 Vendor Qualification Acceptance
Criteria for accepting vendor qualification:
- Qualification performed per DO-330
- Qualification applicable to our usage
- Tool version matches qualified version
- Configuration controlled
- Vendor provides ongoing support

## 9. Tool Problem Reporting

### 9.1 Problem Identification
Tool problems identified through:
- Tool error messages
- Unexpected tool behavior
- Incorrect tool outputs
- User reports
- Vendor problem reports

### 9.2 Problem Assessment
For each problem:
1. Document problem description
2. Assess impact on certification
3. Determine if re-qualification needed
4. Notify certification authority if required
5. Implement corrective action
6. Update Tool Qualification Data

### 9.3 Problem Tracking
Tool problems tracked in:
- Tool Problem Report log
- Integration with project problem reporting system
- Certification authority notification if impacts compliance

## 10. Tool Qualification Review

### 10.1 Review Requirements
Tool qualification reviewed by:
- Software/Hardware Manager
- Quality Assurance
- Certification Manager
- Independent reviewers (for critical tools)

### 10.2 Review Criteria
Review verifies:
- Tool assessment complete and correct
- Qualification level appropriate
- Tool Operational Requirements complete
- Verification approach adequate
- Verification complete and correct
- Configuration controlled
- Documentation complete

### 10.3 Review Schedule
- TQP Review: During planning phase
- TOR Review: Before verification starts
- Verification Results Review: After testing
- TQS Review: Before tool use in certification
- Annual Review: For maintained tools

## 11. Tool Operational Usage

### 11.1 Authorized Users
Only authorized users may operate qualified tool:
- Users trained on tool operation
- Users familiar with tool limitations
- Users understand qualified configuration

### 11.2 Usage Restrictions
Tool shall be used only:
- Per Tool Operational Requirements
- Within qualified configuration
- For purposes defined in TQP
- With documented procedures

### 11.3 Usage Documentation
Each tool usage shall document:
- Tool version and configuration
- Input data
- Tool settings and options
- Output data
- Verification of output (if required)

## 12. Authority Coordination

### 12.1 Authority Notification
Certification authority will be:
- Notified of tool qualification approach
- Provided Tool Qualification Plan for review
- Provided Tool Qualification Summary
- Notified of tool changes or problems

### 12.2 Authority Review
Authority may:
- Review tool qualification package
- Request additional verification
- Audit tool usage
- Impose restrictions on tool usage

Reference: [`../../AUTHORITY_CORRESPONDENCE/`](../../AUTHORITY_CORRESPONDENCE/)

## 13. Schedule and Milestones

### 13.1 Qualification Schedule
| Milestone | Description | Target Date | Status |
|-----------|-------------|-------------|--------|
| TQP Approved | Tool Qualification Plan approved | [Date] | Planned |
| TOR Complete | Tool Operational Requirements complete | [Date] | Planned |
| Verification Complete | All verification testing complete | [Date] | Planned |
| TQS Approved | Tool Qualification Summary approved | [Date] | Planned |
| Tool Operational | Tool available for project use | [Date] | Planned |

### 13.2 Qualification Completion
Tool qualification must be complete before:
- Tool outputs used in certification data
- Phase [X] milestone review
- [Other constraint]

## 14. References

### 14.1 Applicable Standards
- DO-330: Software Tool Qualification Considerations
- DO-178C Section 12: Software Development Tools
- DO-254 Section 11: Tool Assessment and Qualification
- [Project-specific standards]

### 14.2 Related Documents
- PSAC: Plan for Software Aspects of Certification
- PHAC: Plan for Hardware Aspects of Certification
- Tool Qualification Log: [`../TOOL_QUALIFICATION_LOG.csv`](../TOOL_QUALIFICATION_LOG.csv)

## 15. Document Control

### 15.1 Revisions
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-16 | [Name] | Initial draft |

### 15.2 Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Software/Hardware Manager | [Name] | | |
| Quality Assurance Manager | [Name] | | |
| Certification Manager | [Name] | | |

---

**Document Location**: `00-PROGRAM/COMPLIANCE/03-CERTIFICATION/TOOL_QUALIFICATION/[ToolName_Version]/[ToolName]_TQP.md`  
**Next Review**: Upon tool version change or annually  
**Related Documents**: TAR, TOR, TQD, TQS
