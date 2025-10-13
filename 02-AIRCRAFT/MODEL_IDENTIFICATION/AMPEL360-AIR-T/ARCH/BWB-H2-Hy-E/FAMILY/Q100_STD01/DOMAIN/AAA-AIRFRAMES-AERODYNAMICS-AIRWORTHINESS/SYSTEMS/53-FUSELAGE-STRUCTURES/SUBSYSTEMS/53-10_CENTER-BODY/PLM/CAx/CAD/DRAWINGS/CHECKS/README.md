# CHECKS — Drawing Quality Checks and Checklists

## Purpose

This directory contains quality check checklists, validation procedures, and quality assurance documentation to ensure all drawings meet required standards before release.

## What to Store

### Check Templates
- **Pre-release checklists**: Comprehensive quality checks before release
- **Self-check checklists**: Designer self-verification checklists
- **Peer review checklists**: Technical review checklists
- **Checker checklists**: Independent checker verification
- **Approval checklists**: Final approval verification

### Validation Procedures
- **Dimensional check procedures**: Verify dimensions complete and correct
- **GD&T validation**: Verify GD&T application correctness
- **Model-drawing comparison**: Verify drawing matches CAD model
- **Interface verification**: Verify interface dimensions and requirements
- **BOM validation**: Verify BOM completeness and accuracy

### Quality Records
- **Completed checklists**: Archived check records
- **Issue logs**: Drawing issues identified during checks
- **Correction tracking**: Track resolution of identified issues
- **Review meeting minutes**: Design review documentation

## Check Types

### Self-Check (Designer)
**Purpose**: Designer verifies own work before submitting for review

**Checklist Items**:
- [ ] Drawing created from correct CAD model version
- [ ] All required views shown
- [ ] All dimensions necessary for manufacturing shown
- [ ] Tolerances specified (general or specific)
- [ ] Material specification complete
- [ ] Surface finish requirements specified
- [ ] GD&T applied to critical features
- [ ] Datums defined and referenced correctly
- [ ] Title block complete (except approvals)
- [ ] Drawing number assigned and unique
- [ ] Revision block initialized
- [ ] Notes clear and complete
- [ ] References to standards included
- [ ] No obvious errors or omissions

### Peer Review (Team)
**Purpose**: Informal technical review by engineering peers

**Checklist Items**:
- [ ] Design intent clear
- [ ] Dimensions logical and complete
- [ ] Manufacturing feasibility verified
- [ ] Assembly considerations addressed
- [ ] Interface requirements met
- [ ] Standard practices followed
- [ ] Potential issues identified
- [ ] Suggestions for improvement noted

### Checker Review (Independent)
**Purpose**: Formal technical review by independent checker

**Checklist Items**:
- [ ] Drawing complete per standards
- [ ] All dimensions shown and toleranced
- [ ] Material specifications correct
- [ ] Surface finish appropriate
- [ ] GD&T application correct
- [ ] Views adequate for definition
- [ ] Section views appropriate
- [ ] Detail views at correct scale
- [ ] Notes accurate and complete
- [ ] BOM correct (for assemblies)
- [ ] References valid
- [ ] Drawing-model consistency verified
- [ ] Manufacturing issues identified
- [ ] Ready for approval

### Engineering Approval
**Purpose**: Final review and approval by engineering management

**Checklist Items**:
- [ ] Design meets requirements
- [ ] Technical content correct
- [ ] Checker review complete
- [ ] All issues resolved
- [ ] Configuration management ready
- [ ] Authorized for release

## Detailed Check Procedures

### Dimensional Completeness Check
1. Verify all features dimensioned
2. Check dimension from proper datums
3. Confirm no over-dimensioning
4. Verify no missing dimensions
5. Check dimension units consistent
6. Verify dimension precision appropriate

### Tolerance Check
1. General tolerance block present
2. Specific tolerances where required
3. Tolerances achievable by manufacturing
4. Critical dimensions identified
5. Tolerance stack-up acceptable
6. Fit requirements met

### GD&T Check
1. Datums defined properly (A, B, C hierarchy)
2. Datum features appropriate for function
3. GD&T symbols applied correctly
4. Feature control frames complete
5. Material condition modifiers correct
6. Tolerance values appropriate
7. GD&T consistent with function

### Material Specification Check
1. Material fully specified (grade, form, condition)
2. Material appropriate for application
3. Heat treatment specified if required
4. Material available and approved
5. Material finish/coating specified
6. Special processes noted

### Drawing-Model Consistency Check
1. Drawing dimensions match model
2. Geometry consistent with model
3. Features match model features
4. Modifications noted and approved
5. Model revision matches drawing
6. Export/derivation correct

### BOM Check (Assemblies)
1. All components listed in BOM
2. Item numbers match balloons
3. Part numbers correct
4. Quantities correct
5. Descriptions accurate
6. Materials specified (if applicable)
7. BOM matches assembly model

## Check Documentation

### Check Record Template
```
Drawing Number: _______________________
Drawing Title: ________________________
Revision: _____
Check Type: [ ] Self-check  [ ] Peer Review  [ ] Checker  [ ] Approval
Checker Name: _________________________
Date: _________________________________

Checklist Items: (See detailed checklist)

Issues Identified:
1. _____________________________________
2. _____________________________________
3. _____________________________________

Resolution:
Issue 1: _______________________________
Issue 2: _______________________________
Issue 3: _______________________________

Status: [ ] Pass  [ ] Conditional Pass  [ ] Fail
Signature: ____________________________
Date: _________________________________
```

### Issue Tracking
Log all issues identified:
- Issue ID
- Drawing number
- Issue description
- Severity (Critical, Major, Minor)
- Assigned to
- Status (Open, In Progress, Resolved, Closed)
- Resolution description
- Verification status

## Quality Standards

### Drawing Quality Criteria
**Excellent**:
- No errors or omissions
- Exceeds standard requirements
- Manufacturing-friendly
- Clear and unambiguous

**Good**:
- Meets all requirements
- Minor clarifications may be helpful
- Manufacturability verified
- Ready for release

**Needs Work**:
- Missing information
- Unclear or ambiguous
- Manufacturing concerns
- Requires revision

**Unacceptable**:
- Major errors or omissions
- Does not meet standards
- Not manufacturable as shown
- Significant rework required

### Pass/Fail Criteria
**Pass**: Ready for next stage or release
**Conditional Pass**: Minor issues to be corrected, re-check not required
**Fail**: Significant issues, must be revised and re-checked

## Best Practices

### Check Process
- Allow adequate time for checks
- Don't rush quality checks
- Use checklists systematically
- Document all checks
- Track issues to closure
- Learn from issues found

### Checker Independence
- Checker should be independent of designer
- Fresh eyes catch more issues
- Technical expertise required
- Objectivity important
- Constructive feedback

### Issue Resolution
- Address all identified issues
- Document resolution approach
- Verify corrections effective
- Close loop on all issues
- Learn from repeated issues

### Continuous Improvement
- Review check effectiveness
- Update checklists based on experience
- Share lessons learned
- Improve processes
- Reduce recurring issues

## Check Timing

### During Development
- Frequent self-checks during creation
- Informal peer reviews at milestones
- Catch issues early

### Before Review
- Complete self-check before submitting
- Allow time for corrections
- Submit only quality work

### Formal Review
- Scheduled checker review
- Allow adequate review time
- Provide supporting information
- Be responsive to questions

### Before Release
- Final approval check
- Verify all issues resolved
- Configuration management ready
- Quality release gate

## Related Directories

- **Templates**: [`../TEMPLATES/`](../TEMPLATES/) - Standard drawing templates
- **Revisions**: [`../REVISIONS/`](../REVISIONS/) - Revision management
- **All drawing types**: [`../PART/`](../PART/), [`../ASSEMBLY/`](../ASSEMBLY/), etc.
- **Quality standards**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/QUALITY/`

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **Quality procedures**: `/00-PROGRAM/CONFIG_MGMT/QUALITY_PROCEDURES/`
- **Check templates**: Files in this directory
- **Drawing standards**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DRAWING_STANDARDS/`
