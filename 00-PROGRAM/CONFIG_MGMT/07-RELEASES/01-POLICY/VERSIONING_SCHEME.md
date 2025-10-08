# Versioning Scheme

**Document Number:** CM-POL-VERSION  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Defines the version numbering scheme for releases, aligning release versions with configuration baselines and stage gates.

## 2. Version Format

Releases use semantic versioning: **MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]**

### 2.1 Components

- **MAJOR** — Increments for major configuration changes, new baselines, or breaking interface changes
- **MINOR** — Increments for minor feature additions or non-breaking interface changes
- **PATCH** — Increments for bug fixes, documentation updates, or emergency patches
- **PRERELEASE** (optional) — Alpha, beta, RC (release candidate) designators
- **BUILD** (optional) — Build metadata (date, commit SHA)

### 2.2 Examples

- `1.0.0` — First production release
- `1.1.0` — Minor update with new features
- `1.1.1` — Bug fix release
- `2.0.0-beta.1` — Major version beta release
- `1.2.3+20250115.a3f4c2d` — Release with build metadata

## 3. Mapping to Baseline Gates

Release versions are aligned with configuration baseline gates defined in [04-BASELINES/](../../04-BASELINES/).

### 3.1 Engineering Releases → CDR Draft Baseline

**Version Pattern:** `0.x.y` or `x.y.z-alpha`

- Pre-certification engineering validation
- Internal use only
- Frequent iterations
- No regulatory approval required

**Examples:**
- `0.1.0` — First engineering release
- `0.2.0` — Second engineering iteration
- `1.0.0-alpha.1` — Engineering pre-release for version 1.0

**Baseline Reference:** [04-BASELINES/CDR/](../../04-BASELINES/CDR/)

### 3.2 Certification Releases → PRR/FRR Baseline

**Version Pattern:** `x.y.z-beta` or `x.y.z-rc.n`

- **PRR** (Production Readiness Review - Aircraft)
- **FRR** (Flight Readiness Review - Spacecraft)
- Certification authority engagement
- Type certificate or equivalent approval in progress
- Limited production or flight test authorized

**Examples:**
- `1.0.0-beta.1` — First certification release
- `1.0.0-rc.1` — Release candidate 1
- `1.0.0-rc.2` — Release candidate 2 after findings addressed

**Baseline Reference:** 
- Aircraft: [04-BASELINES/PRR/](../../04-BASELINES/PRR/)
- Spacecraft: [04-BASELINES/FRR/](../../04-BASELINES/FRR/)

### 3.3 Production Releases → ORR/EIS Baseline

**Version Pattern:** `x.y.z` (stable, no prerelease suffix)

- **ORR** (Operational Readiness Review - Aircraft)
- **EIS** (Entry Into Service - Aircraft)
- Full type certificate or flight clearance obtained
- Production authorized
- Operational deployment approved

**Examples:**
- `1.0.0` — Initial production release
- `1.0.1` — Production patch release
- `1.1.0` — Production minor update
- `2.0.0` — Major production release

**Baseline Reference:**
- Aircraft: [04-BASELINES/ORR/](../../04-BASELINES/ORR/) or [04-BASELINES/EIS/](../../04-BASELINES/EIS/)
- Spacecraft: [04-BASELINES/FRR/](../../04-BASELINES/FRR/) (spacecraft typically release after FRR)

## 4. Release Naming Convention

### 4.1 Aircraft Releases

**Format:** `REL-ACFT-[VERSION]`

**Examples:**
- `REL-ACFT-0.1.0` — Engineering release
- `REL-ACFT-1.0.0-rc.1` — Certification release candidate
- `REL-ACFT-1.0.0` — Production release
- `REL-ACFT-1.0.1` — Production patch

**Directory:** [05-AIRCRAFT/REL-ACFT-[VERSION]/](../05-AIRCRAFT/)

### 4.2 Spacecraft Releases

**Format:** `REL-SC-[VERSION]`

**Examples:**
- `REL-SC-0.1.0` — Engineering release
- `REL-SC-1.0.0-beta.1` — Certification release
- `REL-SC-1.0.0` — Flight release
- `REL-SC-1.1.0` — Mission update

**Directory:** [06-SPACECRAFT/REL-SC-[VERSION]/](../06-SPACECRAFT/)

### 4.3 Component/Subsystem Releases

For component-specific releases, include component identifier:

**Format:** `REL-[ACFT|SC]-[COMPONENT]-[VERSION]`

**Examples:**
- `REL-ACFT-AVIONICS-1.2.0` — Aircraft avionics subsystem release
- `REL-SC-PROPULSION-0.3.0` — Spacecraft propulsion engineering release

## 5. Version Increment Rules

### 5.1 MAJOR Version Increment

Increment when:
- Moving to new baseline gate (e.g., CDR → PRR → ORR)
- Breaking interface changes (ICDs require non-backward-compatible updates)
- Major architectural changes
- New certification basis

**Process:**
1. CCB approval required
2. All dependent systems notified
3. Interface compatibility documented in [03-REGISTERS/RELEASE_ICD_INDEX.csv](../03-REGISTERS/RELEASE_ICD_INDEX.csv)
4. Migration/rollback plan prepared

### 5.2 MINOR Version Increment

Increment when:
- Adding new features or capabilities
- Non-breaking interface extensions
- Significant bug fixes affecting multiple subsystems
- Minor baseline updates within same gate

**Process:**
1. Engineering change order (ECO) processed
2. Regression testing completed
3. Backward compatibility verified
4. Release notes document changes

### 5.3 PATCH Version Increment

Increment when:
- Bug fixes with no interface changes
- Documentation corrections
- Minor compliance evidence updates
- Emergency patches

**Process:**
1. Fast-track ECO or waiver per [02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md)
2. Targeted testing
3. Rollback kit prepared

## 6. Prerelease Suffixes

### 6.1 Alpha (-alpha.n)

- Early engineering validation
- Incomplete feature set
- Internal team use only
- Frequent changes expected

### 6.2 Beta (-beta.n)

- Feature complete
- Certification preparation
- Extended testing
- Selected external stakeholders

### 6.3 Release Candidate (-rc.n)

- All testing complete
- Compliance evidence assembled
- CCB pre-approval
- Production-ready pending final authorization

## 7. Build Metadata

Build metadata (after `+`) is informational and does not affect version precedence.

### 7.1 Format

`+YYYYMMDD[.git-sha]`

### 7.2 Examples

- `1.0.0+20250115` — Built on 2025-01-15
- `1.0.0+20250115.a3f4c2d` — Built on 2025-01-15 from commit a3f4c2d

### 7.3 Purpose

- Traceability to source control
- Build reproducibility
- Provenance verification

## 8. Version Control in Git

### 8.1 Tagging

Git tags must match release version:
- `REL-ACFT-1.0.0` tag points to baseline commit
- Tags are immutable (no force-push)
- Signed tags required for production releases

### 8.2 Branching

Release branches follow pattern:
- `release/ACFT-1.0` — Aircraft version 1.0 family
- `release/SC-2.1` — Spacecraft version 2.1 family

See [12-CI_CD_RULES/BRANCHING_MODEL.md](../../12-CI_CD_RULES/BRANCHING_MODEL.md) for details.

## 9. Version Precedence

Follows Semantic Versioning 2.0.0 precedence rules:
1. `1.0.0-alpha.1` < `1.0.0-alpha.2` < `1.0.0-beta.1` < `1.0.0-rc.1` < `1.0.0`
2. Build metadata does not affect precedence: `1.0.0+build1` = `1.0.0+build2`

## 10. Effectivity and Serial Number Mapping

### 10.1 Effectivity

Each release defines effectivity in EFFECTIVITY.csv:
- Serial numbers affected
- Effective dates
- Modification status (embodied, optional, mandatory)

### 10.2 Example

```csv
serial_number,effective_date,mod_status,notes
ACFT-001,2025-02-01,embodied,"Factory incorporation"
ACFT-002,2025-03-15,mandatory,"Retrofit required by 2025-03-15"
ACFT-003,2025-04-01,optional,"Customer option"
```

## 11. Compliance and Audit

### 11.1 Version Traceability

Version numbers must be traceable to:
- Git commit SHA (source control)
- Baseline gate (PDR/CDR/PRR/FRR/ORR)
- CCB approval date and decision
- Certification documents (if applicable)

### 11.2 Version Register

All versions logged in [03-REGISTERS/RELEASE_REGISTER.csv](../03-REGISTERS/RELEASE_REGISTER.csv):
```csv
id,version,type,status,owner,gate,baseline,sha256
```

## 12. Special Cases

### 12.1 Rapid Development (Agile)

For rapid development cycles:
- Use alpha/beta versions frequently
- Keep prerelease number increments automated
- Transition to stable release at baseline gates

### 12.2 Long-Term Support (LTS)

LTS releases maintain separate branch:
- `release/ACFT-1.0-LTS`
- Backport critical fixes only
- Version: `1.0.x` continues indefinitely
- Clearly marked in release notes

### 12.3 Multi-Configuration

When multiple configurations share a baseline:
- Use build metadata to distinguish: `1.0.0+config-A`, `1.0.0+config-B`
- Or use minor version: `1.0.0` (config A), `1.1.0` (config B)

## 13. Related Documents

- [RELEASE_POLICY.md](./RELEASE_POLICY.md) — Release governance
- [RELEASE_TYPES.md](./RELEASE_TYPES.md) — Release type definitions
- [01-CM_PLAN.md](../../01-CM_PLAN.md) — Configuration Management Plan Section 4.1
- [04-BASELINES/](../../04-BASELINES/) — Baseline definitions

## 14. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Configuration Manager |
