# TEMPLATES — S1000D Data Module Templates

## Purpose

This directory contains reusable templates for creating S1000D Data Modules, Publication Modules, and other CSDB content for AMPEL360 AIR-T.

## Directory Structure

```
TEMPLATES/
├── README.md              # This file
├── DMs/                   # Data Module templates
│   ├── TEMPLATE_Descriptive_DM.xml
│   ├── TEMPLATE_Procedural_DM.xml
│   └── TEMPLATE_IPD_DM.xml (coming soon)
├── ICN/                   # Illustration templates
├── PublicationModule/     # PM templates
└── Naming/                # Naming convention guides
```

## Data Module Templates

### Descriptive Data Module Template

**File**: `DMs/TEMPLATE_Descriptive_DM.xml`

**Use for**: System and component descriptions, theory of operation

**Info codes**: 000-099 (typically 040-049 for descriptions)

**Steps to use**:
1. Copy template to `CSDB/DMs/Descriptive/`
2. Rename following DMC convention:
   ```
   DMC-AMP360-AAA-<sys>-<subsys>-<subsub>-00A-<component><variant>-<infocode><infovar>-A_en-US_001-01.xml
   ```
3. Update placeholders:
   - `[PLACEHOLDER-SEQ]`: Unique UTCS sequence number
   - `[PLACEHOLDER - Technical Name]`: Component/system name
   - `[PLACEHOLDER - Information Type]`: Description, Overview, etc.
   - Content placeholders in `<description>` section
4. Author content following ASD-STE-100 guidelines
5. Validate with BREX: `python ../../VALIDATION/BREX/validate_brex.py <file>`
6. Update `inWork` to `00` when ready for release

**Example renamed file**:
```
DMC-AMP360-AAA-53-10-10-00A-040A-D_en-US_001-01.xml
```
(Forward Bulkhead Description, Draft)

### Procedural Data Module Template

**File**: `DMs/TEMPLATE_Procedural_DM.xml`

**Use for**: Installation, removal, inspection, servicing procedures

**Info codes**: 
- 100-199: Testing and troubleshooting
- 300-399: Disassembly/Assembly
- 400-499: Servicing
- 500-599: Adjustment/Test
- 600-699: Inspection

**Steps to use**:
1. Copy template to `CSDB/DMs/Procedural/`
2. Rename with appropriate info code (e.g., 310 for installation)
3. Update metadata and UTCS anchor
4. Complete `<preliminaryRqmts>`:
   - Required personnel and skill level
   - Required tools
   - Required supplies/consumables
   - Required conditions (power off, jacks, etc.)
5. Author procedure steps:
   - Use imperative mood: "Remove the cover"
   - One action per step
   - Add safety warnings BEFORE hazardous steps
   - Add figures at step level
   - Maximum 20 words per sentence
6. Complete `<closeRqmts>` (post-procedure checks)
7. Validate and release

**Safety message requirements**:
- **WARNING**: Before steps with risk of death or serious injury
- **CAUTION**: Before steps with risk of equipment damage
- **NOTE**: Additional information (never use for safety)

**Example renamed file**:
```
DMC-AMP360-AAA-53-10-10-00A-310A-P_en-US_001-01.xml
```
(Forward Bulkhead Installation Procedure, Draft)

## Template Features

All templates include:
- ✅ S1000D Issue 6.0 namespace declarations
- ✅ Complete IDS structure with all required metadata
- ✅ UTCS anchor placeholder
- ✅ Security classification (01 = Unclassified)
- ✅ Quality assurance metadata
- ✅ Placeholder comments and instructions
- ✅ Compliance with BREX rules (when placeholders filled)

## Naming Convention

### DMC Pattern
```
DMC-<ModelIdent>-<SysDiff>-<Sys>-<SubSys>-<SubSub>-<Assy>-<Disassy><Var>-<Info><InfoVar>-<Item>_<Lang>-<Country>_<Issue>-<InWork>.xml
```

### AMPEL360 Fixed Values
- `ModelIdent`: **AMP360**
- `SysDiff`: **AAA**
- `Assy`: **00A**
- `Item`: **A**
- `Lang`: **en**
- `Country`: **US**

### Variable Values
- `Sys-SubSys-SubSub`: Based on ATA chapters (e.g., 53-10-00)
- `Disassy-Var`: Component (00-99) + variant (0-9)
- `Info-InfoVar`: Information type + variant (e.g., 040A, 310A)
- `Issue`: 001-999 (increments on each release)
- `InWork`: 00 (released) or 01-99 (draft)

## UTCS Anchor Format

```xml
<extension>
  <utcs id="UTCS-AMP360-AAA-<Sys>-<SubSys>-DMC-<SeqNum>"/>
</extension>
```

**Sequential numbering by subsystem**:
- 53-10: UTCS-AMP360-AAA-53-10-DMC-001, 002, 003...
- 53-20: UTCS-AMP360-AAA-53-20-DMC-001, 002, 003...

**UTCS registry**: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`

## Validation Checklist

Before releasing a Data Module:

- [ ] File renamed following DMC convention
- [ ] All `[PLACEHOLDER]` text replaced
- [ ] UTCS anchor unique and registered
- [ ] Issue date updated
- [ ] Content authored in ASD-STE-100
- [ ] Safety warnings positioned correctly
- [ ] Figures and tables titled
- [ ] XML well-formed (syntax check)
- [ ] XSD validation passed
- [ ] BREX validation passed (120 rules)
- [ ] Peer review completed
- [ ] QA review approved
- [ ] `qaReviewed="true"`
- [ ] `inWork="00"` (released)

## Best Practices

### Content Authoring

1. **Use ASD-STE-100 Simplified Technical English**
   - Simple words and short sentences
   - Active voice: "Remove the cover" not "The cover should be removed"
   - Present tense for descriptions
   - Imperative mood for instructions

2. **Structure Procedures Clearly**
   - Prerequisites before procedure
   - One action per step
   - Safety warnings before hazardous steps
   - Close-out requirements at end

3. **Use Consistent Terminology**
   - Same word for same item throughout
   - Define technical terms on first use
   - Avoid synonyms

4. **Add Appropriate Graphics**
   - Figures at step level (not inside para)
   - Descriptive figure titles
   - ICN references from CSDB/ICN/
   - Callouts numbered sequentially

5. **Include Traceability**
   - UTCS anchor in every DM
   - Cross-references to related DMs
   - Links to requirements (when applicable)

### Metadata Management

1. **Issue Numbers**
   - Start at 001 for new DMs
   - Increment on each approved release
   - Use inWork 01-99 for drafts

2. **Security Classification**
   - Default: 01 (Unclassified)
   - Update if content is sensitive
   - Set `commercialExportControl` appropriately

3. **Quality Assurance**
   - `qaReviewed="false"` during authoring
   - `qaReviewed="true"` after QA approval
   - Required before release (BREX-044)

4. **Reason for Update**
   - Required for issues > 001 (BREX-048)
   - Reference ECO or change request
   - Brief description of changes

## Tools and Scripts

### Create New DM from Template

```bash
# Copy and rename template
cp TEMPLATES/DMs/TEMPLATE_Descriptive_DM.xml \
   CSDB/DMs/Descriptive/DMC-AMP360-AAA-53-10-00-00A-040A-D_en-US_001-01.xml

# Auto-generate UTCS anchor (if script available)
python tools/generate_utcs.py CSDB/DMs/Descriptive/DMC-*.xml
```

### Validate Template Usage

```bash
# Check for remaining placeholders
grep -r "\[PLACEHOLDER" CSDB/DMs/

# Validate BREX compliance
python VALIDATION/BREX/validate_brex.py CSDB/DMs/
```

### Batch Operations

```bash
# Update issue dates for release
python tools/update_dates.py CSDB/DMs/

# Set inWork=00 for release
python tools/release_dms.py CSDB/DMs/
```

## Template Customization

If you need to create a custom template:

1. Copy an existing template
2. Update for specific use case
3. Add comments explaining placeholders
4. Validate against BREX
5. Document in this README
6. Share with team

## Support

For template questions:
- **Usage**: tech-pubs@ampel360.eu
- **BREX Issues**: validation@ampel360.eu
- **Tool Support**: automation@ampel360.eu

## Related Documentation

- **Style Guide**: [`../GUIDES/StyleGuide.md`](../GUIDES/StyleGuide.md)
- **Language Guide**: [`../GUIDES/Language.md`](../GUIDES/Language.md)
- **Conventions**: [`../GUIDES/Conventions.md`](../GUIDES/Conventions.md)
- **BREX Rules**: [`../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv`](../CSDB/BREX/AMP360-AIR-T_BREX_120rules_index.csv)

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-10  
**Owner**: Technical Publications Office  
**Review Cycle**: With S1000D updates
