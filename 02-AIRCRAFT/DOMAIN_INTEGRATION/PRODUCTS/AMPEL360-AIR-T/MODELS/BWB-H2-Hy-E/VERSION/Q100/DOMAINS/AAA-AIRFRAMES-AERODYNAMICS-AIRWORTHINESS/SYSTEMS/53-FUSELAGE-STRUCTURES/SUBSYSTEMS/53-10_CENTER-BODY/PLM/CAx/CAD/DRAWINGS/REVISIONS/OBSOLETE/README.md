# OBSOLETE — Obsolete Drawings

## Purpose

This directory contains or references drawings that have been superseded by newer revisions or are no longer applicable for production use. These drawings are maintained for historical reference, traceability, and configuration management.

## Scope

### Obsolete Drawing Status
- **Superseded**: Replaced by newer revision
- **Retired**: No longer applicable to current design
- **Historical**: Maintained for reference only
- **Not for production**: Must not be used for new manufacturing

## What to Store

### Obsolete Drawing Types
- Previous revisions superseded by newer versions
- Drawings for discontinued or changed designs
- Drawings for replaced or eliminated components
- Historical drawing versions for legacy hardware
- Canceled drawings never released to production

## Organization

### File Naming
Obsolete drawings retain original naming with revision:
```
53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf  (superseded by RevB)
53-10_DWG_ASM_OLD-DESIGN_D1005_SH1_RevC.pdf  (design changed)
53-10_DWG_INST_OBSOLETE-METHOD_D2015_SH1_RevA.pdf  (method retired)
```

### Metadata
Include metadata indicating:
- **Obsolete date**: When drawing became obsolete
- **Superseded by**: Drawing number/revision that replaces it
- **Reason**: Why drawing is obsolete (superseded, design change, etc.)
- **ECO/ECN**: Change order that obsoleted the drawing

### Folder Structure
Optionally organize by:
- Year obsoleted
- Superseding drawing
- Reason for obsolescence
- Component type

## Reasons for Obsolescence

### Superseded by Revision
- Most common reason
- New revision released with changes
- Previous revision moved to obsolete
- **Example**: Rev A superseded by Rev B

### Design Change
- Major design change eliminates component
- Component replaced by different design
- Assembly method changed
- **Example**: Frame design changed from machined to composite

### Component Eliminated
- Component no longer part of design
- Functionality moved to different system
- Design simplification removed component
- **Example**: Bracket eliminated due to design optimization

### Standard Changed
- New standard adopted
- Old standard no longer applicable
- Drawing format updated
- **Example**: Conversion from imperial to metric

### Process Change
- Manufacturing process changed
- Installation method changed
- Assembly sequence changed
- **Example**: Change from riveting to bonding

## Retention Requirements

### Why Keep Obsolete Drawings
- **Traceability**: Understand design history and evolution
- **Configuration management**: Complete product record
- **Support legacy hardware**: Service existing units
- **Legal/regulatory**: Compliance and certification records
- **Lessons learned**: Reference for future designs
- **Audit trail**: Complete documentation trail

### Retention Period
- **Active program**: Retain all obsolete drawings
- **Completed program**: Retain per retention schedule
- **Regulatory**: Meet certification authority requirements
- **Typical**: Minimum 10-20 years, often longer
- **Permanent**: Some drawings retained permanently

## Obsolete Drawing Markings

### Visual Indicators
Obsolete drawings should be clearly marked:
- **Watermark**: "OBSOLETE" or "SUPERSEDED"
- **Stamp**: Date obsoleted and superseding drawing
- **Header/footer**: Clear obsolete status
- **Cover sheet**: Summary of obsolescence

### Metadata Fields
- **Status**: OBSOLETE
- **Obsolete date**: When drawing became obsolete
- **Superseded by**: Replacement drawing reference
- **ECO/ECN**: Change documentation
- **Reason**: Brief description of why obsolete

## Access and Use

### Who Can Access
- Configuration management
- Historical research
- Legacy support teams
- Audit and compliance teams
- Authorized personnel for reference

### Restrictions
- **Not for production**: Must not be used for new manufacturing
- **Reference only**: Historical information only
- **Not current**: Does not represent current design
- **Controlled access**: Access may be restricted to prevent misuse

### Proper Use
Obsolete drawings may be referenced for:
- Understanding design history
- Supporting legacy hardware in service
- Researching design decisions
- Configuration audits
- Legal or regulatory inquiries
- Training and education (with proper context)

## Management

### Obsolescence Process
1. **New revision released**: Triggers obsolescence of previous
2. **ECO processed**: Documents reason for change
3. **Mark obsolete**: Update drawing status
4. **Move to OBSOLETE/**: Transfer from RELEASED/
5. **Update indices**: Reflect obsolete status
6. **Notify users**: Inform that drawing is obsolete
7. **Archive**: Long-term archival storage

### Supersession Tracking
Maintain clear links between revisions:
- Previous revision → Current revision
- Current revision → Previous revision
- Chain of supersession for all revisions
- ECO/ECN references for each change

## Configuration Management

### CM Requirements
- All obsolete drawings remain in CM system
- Status changed to OBSOLETE
- Linked to superseding drawing
- Included in configuration audits
- Maintained per retention policy
- Available for historical queries

### Baseline Management
- Obsolete drawings show design evolution
- Support historical baselines
- Document configuration changes
- Enable rollback if necessary
- Maintain complete product history

## Quality Assurance

### Archival Quality
- Ensure drawings remain readable
- Maintain file integrity
- Periodic backup of obsolete drawings
- Verify accessibility
- Preserve metadata
- Protect from accidental modification

### Periodic Review
- Review retention requirements
- Assess continued need for access
- Archive to long-term storage if appropriate
- Maintain index of obsolete drawings
- Verify supersession links remain valid

## Best Practices

### Obsolescence Management
- Mark drawings obsolete promptly
- Clearly reference superseding drawing
- Document reason for obsolescence
- Maintain complete obsolescence record
- Prevent accidental use in production
- Support queries about obsolete designs

### Historical Preservation
- Treat obsolete drawings as historical records
- Maintain readability and accessibility
- Preserve in multiple formats if possible
- Include contextual information
- Document design evolution
- Support legacy hardware

### Change Communication
- Notify all users when drawing obsoleted
- Distribute superseding drawing
- Explain impact of changes
- Provide transition support
- Update all references
- Close out obsolete work orders

## Related Directories

- **Draft**: [`../DRAFT/`](../DRAFT/) - Drawings in development
- **Released**: [`../RELEASED/`](../RELEASED/) - Current released drawings
- **Type directories**: [`../../PART/`](../../PART/), [`../../ASSEMBLY/`](../../ASSEMBLY/)
- **Index**: [`../../INDEX/`](../../INDEX/) - Master drawing index including obsolete

## References

- **Parent README**: [`../README.md`](../README.md) - Revision management
- **Drawing standards**: [`../../README.md`](../../README.md) - General drawing standards
- **Configuration Management**: `/00-PROGRAM/CONFIG_MGMT/` - CM standards and procedures
- **Change Control**: `/00-PROGRAM/CONFIG_MGMT/03-CHANGE_CONTROL/` - ECO/ECN procedures
- **Records Management**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/RECORDS_MGMT/` - Retention policies
