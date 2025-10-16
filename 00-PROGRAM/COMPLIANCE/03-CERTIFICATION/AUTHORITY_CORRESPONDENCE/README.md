---
area: "00-PROGRAM/COMPLIANCE/03-CERTIFICATION/AUTHORITY_CORRESPONDENCE"
owner: "Certification Manager"
status: "Active"
---

# AUTHORITY_CORRESPONDENCE

All formal correspondence with certification authorities.

## Purpose

Centralized management of all interactions with certification authorities including:
- Questions and clarifications
- Finding reports from audits
- Issue papers for complex compliance topics
- Meeting minutes and action items

This directory ensures complete traceability and audit trail of authority engagement.

## Structure

### QUESTIONS_AND_RESPONSES/
**Purpose**: Track questions from/to certification authority and responses

**File Naming**: `QR_YYYYMMDD_[Authority]_[ShortDescription].md`

**Content**:
- Question ID and date
- Originator (us or authority)
- Question text
- Response provided
- Supporting references
- Disposition (closed, pending, requires action)

**Log File**: `QUESTIONS_LOG.csv`

### FINDING_REPORTS/
**Purpose**: Track findings issued by certification authority during audits

**File Naming**: `FINDING_[Authority]_[FindingID]_[ShortDescription].md`

**Content**:
- Finding ID and date issued
- Authority name
- Finding category (major, minor, observation)
- Finding description
- Root cause analysis
- Corrective action plan
- Closure evidence
- Authority acceptance

**Log File**: `FINDINGS_LOG.csv`

### ISSUE_PAPERS/
**Purpose**: Address complex compliance topics requiring detailed technical discussion

**File Naming**: `IP_[IssueNumber]_[ShortDescription].md`

**Content**:
- Issue description
- Technical background
- Compliance challenge
- Proposed means of compliance
- Alternative approaches considered
- Rationale and justification
- Supporting analysis or data
- Authority feedback
- Resolution

**Index File**: `ISSUE_PAPERS_INDEX.csv`

### MEETING_MINUTES/
**Purpose**: Document all meetings with certification authorities

**File Naming**: `MINUTES_YYYYMMDD_[Authority]_[MeetingType].md`

**Content**:
- Meeting date, time, location
- Attendees (both sides)
- Agenda
- Discussion summary
- Decisions made
- Action items assigned
- Next meeting scheduled

**Meeting Calendar**: `MEETING_SCHEDULE.csv`

## Authority Relationships

### EASA (European Union Aviation Safety Agency)
**Contact**: [Authority contact info - Internal only]  
**Primary for**: Aviation Type Certification (EU operations)  
**Meeting Frequency**: Monthly progress reviews

### FAA (Federal Aviation Administration)
**Contact**: [Authority contact info - Internal only]  
**Primary for**: Aviation Type Certification (US operations)  
**Meeting Frequency**: As required for US certification

### ESA (European Space Agency)
**Contact**: [Authority contact info - Internal only]  
**Primary for**: Space mission assurance (ESA-funded missions)  
**Meeting Frequency**: Per mission milestone reviews

### National Space Agencies
**Varies by mission**  
**Primary for**: Mission-specific requirements and launch approvals  
**Meeting Frequency**: Per mission-specific agreements

## Correspondence Process

### Incoming Correspondence
1. **Receipt**: Log in appropriate tracking file
2. **Distribution**: Route to technical experts
3. **Assessment**: Evaluate impact and urgency
4. **Response Preparation**: Draft response with evidence
5. **Review**: Internal review and approval
6. **Submittal**: Send to authority with tracking
7. **Follow-up**: Track to closure

### Outgoing Correspondence
1. **Initiation**: Identify need for authority engagement
2. **Preparation**: Draft question or request
3. **Review**: Certification Manager review
4. **Submittal**: Send to authority with tracking
5. **Follow-up**: Track response and action
6. **Closure**: Document disposition

## Response Timelines

### Internal Targets
- Authority questions: Response within 10 business days
- Authority findings: Corrective action plan within 5 business days
- Authority requests: Response within timeframe specified (typically 15 days)

### Authority Typical Response Times
- Questions from us: 2-4 weeks
- Plan reviews: 4-6 weeks
- Finding closure review: 2-3 weeks
- Issue paper responses: 4-8 weeks (depending on complexity)

## Quality Requirements

- All correspondence reviewed by Certification Manager before submittal
- Technical accuracy verified by subject matter experts
- References and evidence validated
- Consistency with approved plans and previous positions
- Configuration management for all versions
- Secure storage and access control

## Tracking Metrics

Track and report:
- Open questions (count and age)
- Open findings (count and severity)
- Average response time (ours and authority)
- Finding closure rate
- Issue paper resolution time
- Meeting action item closure rate

## Communication Protocols

### Formal Communications
- Use official letterhead
- Reference applicable docket/file numbers
- Copy Certification Manager on all correspondence
- Archive in this directory structure
- Track in appropriate log file

### Informal Communications
- Email or phone for clarifications
- Follow up with formal documentation if required
- Document significant discussions in meeting minutes
- Confirm verbal agreements in writing

## Document Control

- All correspondence is configuration controlled
- Original (submitted/received) versions archived
- Revisions tracked with version control
- Access restricted to authorized personnel
- Permanent retention per regulatory requirements

## Integration Points

- **Compliance Issues**: Link findings to [`../COMPLIANCE_ISSUES_LOG.csv`](../COMPLIANCE_ISSUES_LOG.csv)
- **Evidence**: Reference evidence in [`../../06-EVIDENCE/EVIDENCE_INDEX.csv`](../../06-EVIDENCE/EVIDENCE_INDEX.csv)
- **Checklists**: Update status in [`../COMPLIANCE_CHECKLISTS/`](../COMPLIANCE_CHECKLISTS/)
- **Milestones**: Track in [`../CERTIFICATION_MILESTONES.csv`](../CERTIFICATION_MILESTONES.csv)
- **CAPA**: Link to [`../../04-AUDITS/CAPA_LOG.csv`](../../04-AUDITS/CAPA_LOG.csv)

## Related Documents

- Master Plan: [`../PLAN_FOR_SOCC.md`](../PLAN_FOR_SOCC.md)
- Certification Plans: [`../CERTIFICATION_PLANS/`](../CERTIFICATION_PLANS/)
- Certification Packages: [`../CERTIFICATION_PACKAGES/`](../CERTIFICATION_PACKAGES/)

## Templates

Standard templates available in:
- Question/Response Template: [`../../99-TEMPLATES/`](../../99-TEMPLATES/)
- Finding Report Template: [`../../99-TEMPLATES/`](../../99-TEMPLATES/)
- Issue Paper Template: [`../../99-TEMPLATES/`](../../99-TEMPLATES/)
- Meeting Minutes Template: [`../../99-TEMPLATES/`](../../99-TEMPLATES/)

## Confidentiality

- All authority correspondence is Internal confidentiality level minimum
- Some correspondence may be Restricted or Confidential
- Do not share outside authorized personnel without approval
- Protect authority contact information
- Follow data protection regulations
