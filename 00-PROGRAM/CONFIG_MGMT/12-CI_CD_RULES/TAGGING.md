# Git Tagging Conventions

## Overview

This document defines the tagging strategy for the IDEALE EU aerospace program repository. Tags mark important points in history such as baselines, releases, and milestones.

## Purpose

Git tags provide:
- Immutable markers for program baselines
- Version identification for releases
- Traceability to stage gates
- Historical reference points
- Release management support

## Tag Types

### 1. Baseline Tags

**Format:** `[GATE]-BASELINE-v[X.Y]`

**Examples:**
- `SRR-BASELINE-v1.0` - System Requirements Review baseline
- `PDR-BASELINE-v1.0` - Preliminary Design Review baseline
- `CDR-BASELINE-v2.0` - Critical Design Review baseline (2nd revision)
- `TRR-BASELINE-v1.0` - Test Readiness Review baseline
- `PRR-BASELINE-v1.0` - Production Readiness Review baseline
- `ORR-BASELINE-v1.0` - Operational Readiness Review baseline (Aircraft)
- `FRR-BASELINE-v1.0` - Flight Readiness Review baseline (Spacecraft)

**Usage:**
- Applied to `main` branch at stage gate completion
- Represents approved configuration at that milestone
- Requires CCB approval
- Annotated tags with detailed message
- Signed by Configuration Manager

**Tag Message Content:**
- Stage gate name and date
- Baseline description
- Key items in baseline
- CCB approval reference
- Configuration Manager signature

**Example:**
```bash
git tag -a SRR-BASELINE-v1.0 -m "System Requirements Review Baseline

Date: 2024-03-15
Stage Gate: SRR (System Requirements Review)
CCB Approval: CCB-MEETING-2024-03-15

This baseline includes:
- System requirements specification v1.0
- Stakeholder requirements v1.0
- Initial architecture definition
- Requirements traceability matrix

All configuration items reviewed and approved by CCB.

Configuration Manager: J. Smith
Date: 2024-03-15"

git push origin SRR-BASELINE-v1.0
```

### 2. Release Tags

**Format:** `v[MAJOR].[MINOR].[PATCH][-PRERELEASE]`

Following Semantic Versioning 2.0.0 (https://semver.org/)

**Examples:**
- `v1.0.0` - Major release
- `v1.1.0` - Minor release with new features
- `v1.1.1` - Patch release with bug fixes
- `v2.0.0-alpha.1` - Pre-release alpha version
- `v2.0.0-beta.2` - Pre-release beta version
- `v2.0.0-rc.1` - Release candidate

**Version Numbering:**
- **MAJOR** - Incompatible changes, major milestones
- **MINOR** - New functionality, backward compatible
- **PATCH** - Bug fixes, backward compatible
- **PRERELEASE** - alpha, beta, rc (release candidate)

**Usage:**
- Applied to `main` for official releases
- Applied to `develop` for pre-releases
- Annotated tags
- Includes changelog in message

**Example:**
```bash
git tag -a v1.0.0 -m "Version 1.0.0 - PDR Release

Release Date: 2024-06-01
Baseline: PDR-BASELINE-v1.0

New Features:
- Preliminary aircraft design complete
- Preliminary spacecraft design complete
- System architecture defined
- Interface Control Documents established

Changes:
- Updated wing design per ECR-1234
- Improved GNC algorithms per ECR-1245
- Enhanced power system per ECR-1267

Bug Fixes:
- Fixed traceability matrix gaps
- Corrected part numbering inconsistencies

Configuration Manager: J. Smith"

git push origin v1.0.0
```

### 3. Hotfix Tags

**Format:** `HOTFIX-v[X.Y.Z]`

**Examples:**
- `HOTFIX-v1.0.1` - First hotfix to v1.0.0
- `HOTFIX-v1.2.3` - Hotfix to v1.2.2

**Usage:**
- Applied to `main` after emergency fixes
- Increments patch version
- Requires expedited CCB approval
- Includes description of critical fix

**Example:**
```bash
git tag -a HOTFIX-v1.0.1 -m "Hotfix v1.0.1 - Critical Safety Issue

Date: 2024-07-15
ECR: ECR-9999 (Emergency)
CCB Approval: Emergency CCB Meeting 2024-07-15

Critical Fix:
- Corrected flight control system safety margin calculation
- Updated safety analysis per ECR-9999

Impact:
- All aircraft designs
- Requires immediate implementation
- Safety-critical change

Approved by: CCB Chair, Safety Manager, Chief Engineer
Configuration Manager: J. Smith"

git push origin HOTFIX-v1.0.1
```

### 4. Milestone Tags

**Format:** `MILESTONE-[NAME]-[DATE]`

**Examples:**
- `MILESTONE-FIRST-FLIGHT-20250101`
- `MILESTONE-CERTIFICATION-SUBMITTAL-20250615`
- `MILESTONE-FIRST-DELIVERY-20260101`

**Usage:**
- Mark significant program milestones
- Applied when milestone achieved
- Documentation and celebration purposes

### 5. ECO Tags

**Format:** `ECO-[NUMBER]-[DESCRIPTION]`

**Examples:**
- `ECO-1234-WING-MATERIAL-CHANGE`
- `ECO-5678-MANUFACTURING-PROCESS-UPDATE`

**Usage:**
- Mark completion of Engineering Change Orders
- Applied after ECO implementation and verification
- Traceability to changes

**Example:**
```bash
git tag -a ECO-1234-WING-MATERIAL-CHANGE -m "ECO-1234: Wing Material Change

ECO Number: ECO-1234
ECR Reference: ECR-1234
Implementation Date: 2024-08-01
CCB Approval: CCB-MEETING-2024-07-15

Change Description:
- Changed wing spar material from Al 7075-T6 to Al 7050-T7
- Improved fatigue resistance by 15%
- Updated manufacturing processes
- Revised inspection procedures

Affected Items:
- IDEALE-ACFT-00100 (Wing Assembly) - Rev B
- IDEALE-ACFT-00100-1 (Wing Spar) - Rev B

Verification:
- Structural analysis completed
- Material qualification completed
- Test specimens fabricated and tested

Configuration Manager: J. Smith"

git push origin ECO-1234-WING-MATERIAL-CHANGE
```

## Tag Creation Process

### Standard Process

1. **Identify Tag Need**
   - Stage gate completion
   - Release preparation
   - Milestone achievement

2. **Prepare Tag**
   - Verify commit is correct
   - Prepare tag message
   - Obtain necessary approvals

3. **Create Tag**
   ```bash
   git checkout main  # or appropriate branch
   git pull origin main
   git tag -a [TAG_NAME] -m "[TAG_MESSAGE]"
   ```

4. **Sign Tag** (if required)
   ```bash
   git tag -s [TAG_NAME] -m "[TAG_MESSAGE]"
   ```

5. **Push Tag**
   ```bash
   git push origin [TAG_NAME]
   ```

6. **Document Tag**
   - Record in configuration management database
   - Update baseline documentation
   - Notify stakeholders

### Baseline Tag Process

For stage gate baselines:

1. **Pre-Tag Activities**
   - [ ] Stage gate review completed
   - [ ] All gate criteria met
   - [ ] CCB approves baseline
   - [ ] Documentation package prepared
   - [ ] Configuration audit completed
   - [ ] All changes incorporated

2. **Create Baseline Tag**
   ```bash
   git checkout main
   git pull origin main
   git tag -a [GATE]-BASELINE-v1.0 -m "[Detailed message]"
   git push origin [GATE]-BASELINE-v1.0
   ```

3. **Post-Tag Activities**
   - [ ] Create baseline branch (if needed)
   - [ ] Archive baseline documentation
   - [ ] Update item master
   - [ ] Update traceability
   - [ ] Notify stakeholders
   - [ ] Update baseline register

## Tag Management

### Viewing Tags

```bash
# List all tags
git tag

# List tags matching pattern
git tag -l "SRR*"
git tag -l "v1.*"

# Show tag details
git show [TAG_NAME]

# List tags with messages
git tag -n9
```

### Checking Out Tags

```bash
# Checkout specific tag (detached HEAD state)
git checkout [TAG_NAME]

# Create branch from tag
git checkout -b branch-name [TAG_NAME]
```

### Tag Protection

Protected tags (cannot be deleted or modified):
- All baseline tags: `*-BASELINE-*`
- All release tags: `v*`
- All hotfix tags: `HOTFIX-*`

Configure in repository settings:
- Prevent tag deletion
- Require signed tags
- Restrict tag creation to Configuration Manager

### Tag Deletion (Use with Extreme Caution)

Tags should NEVER be deleted once pushed, except in extraordinary circumstances with CCB approval.

If absolutely necessary:
```bash
# Delete local tag
git tag -d [TAG_NAME]

# Delete remote tag (requires authorization)
git push origin :refs/tags/[TAG_NAME]
```

## Tag Naming Best Practices

### Do's
- ✅ Use descriptive names
- ✅ Follow established conventions
- ✅ Use uppercase for baseline and milestone tags
- ✅ Use semantic versioning for releases
- ✅ Include date for time-based tags
- ✅ Use annotated tags (not lightweight)
- ✅ Sign critical tags

### Don'ts
- ❌ Don't use spaces in tag names
- ❌ Don't use special characters except hyphens and dots
- ❌ Don't reuse tag names
- ❌ Don't delete tags without CCB approval
- ❌ Don't create tags without approval
- ❌ Don't use lightweight tags for important milestones

## Tag Traceability

All tags linked to:
- Baseline documentation (04-BASELINES/[GATE]/)
- CCB meeting minutes (05-CCB/02-MINUTES/)
- Change records (06-CHANGES/)
- Requirements (10-TRACEABILITY/)

Tag registry maintained in configuration management database.

## Automation

Automated tag creation can be used for:
- Pre-release versions on develop branch
- Build numbers in CI/CD pipeline
- Test releases

Not allowed for:
- Baseline tags (require manual CCB approval)
- Release tags to main (require verification)

## Tag Metrics

Track and report:
- Number of tags by type
- Time between baseline tags
- Tag creation frequency
- Releases per quarter

## Example Tag Timeline

```
main: ─o────────o────────o─────────o──────────o───>
       │        │        │         │          │
       │        │        │         │          │
    SRR-v1.0  PDR-v1.0 CDR-v1.0  TRR-v1.0  PRR-v1.0
    2024-03   2024-06  2024-09   2024-12   2025-03
```

## References

- Semantic Versioning: https://semver.org/
- Git Tag Documentation: https://git-scm.com/book/en/v2/Git-Basics-Tagging
- Configuration Management Plan: 01-CM_PLAN.md
- Branching Model: BRANCHING_MODEL.md

---

**Document Owner:** Configuration Management  
**Maintained By:** DevOps Team  
**Review Frequency:** Quarterly or as needed
