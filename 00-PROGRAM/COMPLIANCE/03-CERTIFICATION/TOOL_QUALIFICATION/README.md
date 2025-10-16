---
area: "00-PROGRAM/COMPLIANCE/03-CERTIFICATION/TOOL_QUALIFICATION"
owner: "Certification Manager"
status: "Active"
---

# TOOL_QUALIFICATION

Tool qualification artifacts for software and hardware tools used in certification.

## Purpose

Per DO-178C Section 12 and DO-254 Section 11, tools that:
- Generate outputs used in certification (development tools)
- Verify outputs used in certification (verification tools)

Must be qualified to ensure tool outputs are reliable and do not introduce errors.

## Tool Qualification Criteria

### Development Tools (TQL-1)
Tools whose output is part of the airborne/space product and could insert an error.

**Examples**:
- Code generators
- Automated test generators
- Hardware synthesis tools
- Automated design tools

**Qualification Requirement**: HIGH - Full qualification required

### Verification Tools (TQL-2 through TQL-5)
Tools that verify outputs and could fail to detect an error.

**TQL-2**: Tool output used to satisfy verification without further verification
- Example: Automated test execution tools with pass/fail determination

**TQL-3**: Tool output inspected and can fail to detect an error
- Example: Static analysis tools, coverage analysis tools

**TQL-4**: Tool automates verification process, output independently verified
- Example: Test automation frameworks with manual result verification

**TQL-5**: Tool output used for information only or independently verified
- Example: Code editors, document viewers

**Qualification Requirement**: Varies by TQL level (TQL-2 highest, TQL-5 lowest/none)

## Tool Qualification Process

### 1. Tool Assessment
**Document**: Tool Assessment Report (TAR)
- Identify all tools used in project
- Determine tool qualification level (TQL-1 through TQL-5)
- Assess qualification requirement
- Document in `TOOL_QUALIFICATION_LOG.csv`

### 2. Tool Qualification Plan (TQP)
**Document**: `[ToolName]_TQP.md`
- Tool description and version
- Tool operational requirements (TOR)
- Qualification approach
- Verification methods
- Success criteria
- Schedule

### 3. Tool Operational Requirements (TOR)
**Document**: `[ToolName]_TOR.md`
- Tool functional requirements
- Tool operational scenarios
- Expected tool behavior
- Error detection requirements
- Tool limitations and constraints

### 4. Tool Qualification Data (TQD)
**Evidence**: `[ToolName]_TQD/`
- Tool verification test procedures
- Tool verification test results
- Tool configuration documentation
- Tool user documentation
- Tool installation/setup procedures
- Tool operational procedures

### 5. Tool Qualification Summary (TQS)
**Document**: `[ToolName]_TQS.md`
- Summary of qualification activities
- Verification results summary
- Known limitations and constraints
- Approved configuration
- Qualification approval and date
- Configuration control requirements

## Tool Qualification Levels and Requirements

| TQL | Tool Type | Qualification Rigor | Key Documents |
|-----|-----------|-------------------|---------------|
| TQL-1 | Development | Full qualification | TQP, TOR, TQD, TQS |
| TQL-2 | Verification (critical) | Substantial qualification | TQP, TOR, TQD, TQS |
| TQL-3 | Verification (moderate) | Moderate qualification | TQP, TOR, TQD, TQS |
| TQL-4 | Verification (low) | Minimal qualification | TAR, tool records |
| TQL-5 | Support/Info | No qualification | TAR only |

## Tool Qualification Alternatives

### Alternative 1: Tool Qualification by Tool Developer
- Use tools with existing qualification data from vendor
- Verify applicability to our usage
- Maintain tool configuration control
- More cost-effective but less control

### Alternative 2: Tool Qualification by User (Our Organization)
- Develop complete qualification package
- Full control and customization
- More expensive and time-consuming
- Required for custom/in-house tools

### Alternative 3: Tool Output Verification
- Manually verify each tool output
- No tool qualification required
- Most expensive operationally
- Only practical for limited tool usage

## Tool Configuration Management

Qualified tools must maintain:
- **Version Control**: Specific qualified version documented
- **Configuration Lock**: Prevent unauthorized changes
- **Usage Control**: Only authorized users
- **Change Management**: Any changes require re-qualification assessment
- **Problem Reports**: Track and resolve tool issues

## Tool Qualification Tracking

### TOOL_QUALIFICATION_LOG.csv
Central tracking of all tools:
```csv
Tool_ID,Tool_Name,Tool_Version,Tool_Vendor,Qualification_Level,Usage_Description,TQL_Status,TOR_Reference,TQD_Reference,TQS_Reference,Qualified_Date,Review_Date,Owner,Notes
```

### Status Values
- **Assessment**: Tool being evaluated
- **Planned**: Qualification planned
- **In Progress**: Qualification underway
- **Qualified**: Qualification complete and approved
- **Maintained**: Qualified and in operational use
- **Superseded**: Replaced by newer version
- **Retired**: No longer in use

## Directory Structure

```
TOOL_QUALIFICATION/
├── README.md (this file)
├── [ToolName_Version]/
│   ├── [ToolName]_TAR.md (Tool Assessment Report)
│   ├── [ToolName]_TQP.md (Tool Qualification Plan)
│   ├── [ToolName]_TOR.md (Tool Operational Requirements)
│   ├── [ToolName]_TQS.md (Tool Qualification Summary)
│   └── [ToolName]_TQD/ (Tool Qualification Data)
│       ├── TEST_PROCEDURES/
│       ├── TEST_RESULTS/
│       ├── CONFIGURATION_DOCS/
│       └── USER_DOCUMENTATION/
```

## Authority Review

Tool qualification packages are:
- Reviewed as part of certification plan approval
- Subject to authority audit during Phase E
- Referenced in Statements of Compliance
- Part of certification basis

Authority may:
- Request additional qualification evidence
- Challenge qualification approach
- Require specific tool versions
- Impose usage restrictions

## Common Qualified Tools

### Software Development
- Compilers (requires qualification)
- Code generators (requires qualification)
- Static analysis tools (TQL-2 or TQL-3)
- Coverage analysis tools (TQL-2 or TQL-3)

### Hardware Development
- HDL synthesis tools (requires qualification)
- Place and route tools (requires qualification)
- Timing analysis tools (TQL-2 or TQL-3)
- Logic equivalence checking (TQL-2)

### Verification
- Test execution frameworks (TQL-2 to TQL-4)
- Requirements management tools (TQL-4 or TQL-5)
- Configuration management tools (TQL-4 or TQL-5)

### Support Tools (typically TQL-5, no qualification)
- Text editors
- PDF viewers
- Office productivity software

## Best Practices

1. **Early Assessment**: Identify and assess tools in Phase B-C
2. **Vendor Qualification**: Use vendor-qualified tools when possible
3. **Version Control**: Lock qualified tool versions
4. **Output Verification**: Consider verification in lieu of qualification
5. **Documentation**: Maintain complete tool records
6. **Training**: Ensure users trained on qualified tools
7. **Problem Reporting**: Track and resolve tool issues promptly

## Integration Points

- **Certification Plans**: Reference tool qualification in PSAC/PHAC
- **Compliance Checklists**: Tool qualification objectives tracked
- **Evidence Index**: Tool qualification data referenced
- **Configuration Management**: Tool versions baselined
- **Process Compliance**: Tool usage per approved procedures

## Related Documents

- Master Plan: [`../PLAN_FOR_SOCC.md`](../PLAN_FOR_SOCC.md)
- PSAC (Software Plan): [`../CERTIFICATION_PLANS/AVIATION/PSAC_DO178C.md`](../CERTIFICATION_PLANS/AVIATION/)
- PHAC (Hardware Plan): [`../CERTIFICATION_PLANS/AVIATION/PHAC_DO254.md`](../CERTIFICATION_PLANS/AVIATION/)
- Tool Qualification Log: [`../TOOL_QUALIFICATION_LOG.csv`](../TOOL_QUALIFICATION_LOG.csv)

## Standards References

- DO-178C Section 12: Software Development Tools and Previously Developed Software
- DO-254 Section 11: Tool Assessment and Qualification
- EASA CM-SWCEH-001: Software and Complex Hardware Development Assurance
- FAA Order 8110.49: Software Approval Guidelines
