# Release Workflow

**Document Number:** CM-WF-RELEASE  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Defines the standard workflow for preparing, reviewing, approving, and distributing releases.

## 2. Scope

Applies to all release types except emergency patches (see [EMERGENCY_PATCH_WORKFLOW.md](./EMERGENCY_PATCH_WORKFLOW.md)).

## 3. Process Overview

```
┌─────────────────┐
│   Initiation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Preparation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Verification   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CCB Review     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Distribution   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Registration   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Post-Release    │
└─────────────────┘
```

## 4. Phase 1: Initiation

### 4.1 Trigger

Release initiated by:
- Baseline gate completion (PDR/CDR/PRR/FRR/ORR)
- Production schedule milestone
- Operational update requirement
- Customer delivery commitment

### 4.2 Activities

#### 4.2.1 Define Release Scope

**Responsible:** Release Manager  
**Input:** Baseline definition, change records  
**Output:** Release scope document

Actions:
1. Identify baseline gate and associated baseline
2. List all changes since previous release
3. Identify affected configuration items
4. Document interfaces and dependencies
5. Determine release type per [01-POLICY/RELEASE_TYPES.md](../01-POLICY/RELEASE_TYPES.md)
6. Assign version number per [01-POLICY/VERSIONING_SCHEME.md](../01-POLICY/VERSIONING_SCHEME.md)

#### 4.2.2 Create Release Plan

**Responsible:** Release Manager  
**Input:** Release scope, project schedule  
**Output:** Release plan

Include:
- Release identifier (REL-ACFT-x.y.z or REL-SC-x.y.z)
- Target distribution date
- Key milestones and deadlines
- Required approvals
- Distribution list
- Risk assessment
- Resource requirements

#### 4.2.3 Kickoff Meeting

**Participants:** Release Manager, domain leads, QA, certification  
**Duration:** 1 hour  
**Output:** Confirmed plan, assigned responsibilities

Agenda:
1. Review release scope and objectives
2. Confirm timeline and milestones
3. Assign responsibilities per [01-POLICY/RASCI.md](../01-POLICY/RASCI.md)
4. Identify risks and dependencies
5. Establish communication plan

### 4.3 Entry Criteria

- Baseline gate completed and approved
- All baseline verification activities closed
- Configuration items identified and under control
- Release Manager assigned

### 4.4 Exit Criteria

- Release scope approved by Configuration Manager
- Release plan documented and distributed
- Kickoff meeting completed
- Responsibilities assigned

### 4.5 Duration

1-2 weeks before preparation phase

## 5. Phase 2: Preparation

### 5.1 Activities

#### 5.1.1 Collect Artifacts

**Responsible:** Engineering teams, Release Manager  
**Duration:** 2-4 weeks

Collect:
- Design documentation (drawings, specifications, models)
- Bill of Materials (EBOM, MBOM)
- Test results (verification and validation reports)
- Analysis results (stress, thermal, etc.)
- Software/firmware builds with source code references
- Interface Control Documents (at baseline revision)
- Change records (ECRs/ECOs) since previous release

#### 5.1.2 Generate SBOM

**Responsible:** Engineering, IT/DevOps  
**Duration:** 1 week

Actions:
1. Identify all software components and versions
2. List all third-party libraries and dependencies
3. Document licenses
4. Generate SBOM in CycloneDX format
5. Include vulnerability scan results
6. Sign SBOM with authorized key

Tools: SPDX generators, CycloneDX tools

#### 5.1.3 Assemble Compliance Evidence

**Responsible:** Quality Assurance, Certification team  
**Duration:** 2-4 weeks

Compile:
- **Aircraft:**
  - DO-178C software lifecycle data
  - DO-254 hardware lifecycle data
  - DO-160 environmental qualification
  - AS9100 quality system evidence
  - ARP4754A system development records
  - ARP4761 safety assessment
- **Spacecraft:**
  - ECSS-Q-ST-80 software standards
  - ECSS-Q-ST-70 materials and processes
  - Radiation test results
  - ESA production assurance evidence
  - PSS-05-0 software engineering
  - PSS-01-60 dependability

Evidence package contents:
- Compliance matrices (requirements vs. evidence)
- Test reports and certificates
- Analysis reports
- Review meeting minutes
- Audit results
- Certification authority correspondence

#### 5.1.4 Prepare Release Notes

**Responsible:** Release Manager, Technical Writer  
**Duration:** 1 week

Template: [04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md](../04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md)

Include:
- Release identifier and version
- Release type and purpose
- Summary of changes
- New features or capabilities
- Bug fixes
- Known limitations
- Compatibility information
- Installation/deployment instructions
- Effectivity (serial numbers, dates)
- Safety and security notices
- References to detailed documentation

#### 5.1.5 Freeze ICDs

**Responsible:** Release Manager, Interface Coordinators  
**Duration:** 1 week

Actions:
1. Identify all ICDs used in this configuration
2. Verify all ICDs at baseline revision
3. Copy ICDs to release package INTERFACES/ICDs/
4. Update [03-REGISTERS/RELEASE_ICD_INDEX.csv](../03-REGISTERS/RELEASE_ICD_INDEX.csv)
5. Document backward compatibility status

#### 5.1.6 Create Manifest

**Responsible:** Release Manager  
**Duration:** 1-2 days

Template: [04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml](../04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml)

Manifest includes:
- Release metadata (ID, version, date, type)
- Baseline reference
- File inventory with SHA256 hashes
- Dependencies
- Effectivity data
- Approval signatures (placeholders)

#### 5.1.7 Generate Provenance Attestations

**Responsible:** IT/DevOps, Security  
**Duration:** 1 week

Create in-toto/SLSA attestations:
1. **Build attestation** — Who, what, when, where for builds
2. **Materials attestation** — Source materials and dependencies
3. **Review attestation** — Code review and approval records

Store in PROVENANCE/ directory.

#### 5.1.8 Calculate Hashes

**Responsible:** IT/DevOps, Release Manager  
**Duration:** 1 day

Actions:
1. Generate SHA256 hash for every file in release package
2. Create SHA256SUMS.txt
3. Sign SHA256SUMS.txt with release signing key
4. Include hash verification instructions

#### 5.1.9 Prepare Rollback Kit

**Responsible:** Engineering, Operations  
**Duration:** 1 week

Rollback kit contents:
- rollback_procedure.md (step-by-step instructions)
- Previous version artifacts (if rollback requires)
- Scripts to automate rollback (if applicable)
- Verification procedures post-rollback
- Contact information for support
- Known issues with rollback

#### 5.1.10 Prepare Distribution Package

**Responsible:** Release Manager, IT  
**Duration:** 1-2 days

Actions:
1. Create distribution archive (ZIP or TAR.GZ)
2. Include all release artifacts
3. Create README with instructions
4. Generate final SHA256 for distribution package
5. Test extraction and integrity verification

### 5.2 Entry Criteria

- Phase 1 complete
- All artifacts available
- Resources allocated

### 5.3 Exit Criteria

- All artifacts collected and organized
- SBOM generated and signed
- Compliance evidence package complete
- Release notes drafted
- ICDs frozen
- Manifest created
- Provenance attestations generated
- Hashes calculated
- Rollback kit prepared
- Distribution package ready

### 5.4 Duration

4-8 weeks

## 6. Phase 3: Verification

### 6.1 Activities

#### 6.1.1 Conformity Checklist Review

**Responsible:** Release Manager, QA  
**Duration:** 1 week

Template: [04-TEMPLATES/CONFORMITY_CHECKLIST.md](../04-TEMPLATES/CONFORMITY_CHECKLIST.md)

Verify:
- [ ] All required artifacts present
- [ ] SBOM complete and signed
- [ ] Provenance attestations valid
- [ ] Hashes verified
- [ ] Compliance evidence complete
- [ ] Release notes accurate
- [ ] ICDs frozen and indexed
- [ ] Manifest accurate
- [ ] Export classification documented
- [ ] Rollback kit tested
- [ ] Distribution package integrity verified

#### 6.1.2 Compliance Verification

**Responsible:** Quality Assurance  
**Duration:** 1-2 weeks

Review:
- Compliance matrices (100% coverage required)
- Test traceability (requirements → tests → results)
- Certification evidence completeness
- Safety case closure
- Standards conformance

For each applicable standard:
1. Review compliance matrix
2. Verify evidence links
3. Check test coverage
4. Confirm all findings closed
5. Document any waivers or deviations

#### 6.1.3 Export Classification Review

**Responsible:** Security Officer  
**Duration:** 1 week

Actions:
1. Review technology for export control applicability
2. Determine ECCN (Export Control Classification Number)
3. Check against USML (US Munitions List) if applicable
4. Document dual-use determination
5. Complete [09-DISTRIBUTION/EXPORT_CLASSIFICATION.md](../09-DISTRIBUTION/EXPORT_CLASSIFICATION.md)
6. Obtain legal review if needed

#### 6.1.4 Baseline Traceability Verification

**Responsible:** Configuration Manager  
**Duration:** 1 week

Verify:
- Release maps to approved baseline
- All changes since previous release documented
- Baseline reference accurate (symlink or documentation)
- Configuration items properly identified
- Effectivity data correct

#### 6.1.5 Dry Run Deployment

**Responsible:** IT, Operations (if applicable)  
**Duration:** 1 week

Test:
1. Extract distribution package
2. Verify hash integrity
3. Follow installation instructions
4. Test rollback procedure
5. Document any issues
6. Refine procedures based on findings

### 6.2 Entry Criteria

- Phase 2 complete
- Release package assembled

### 6.3 Exit Criteria

- Conformity checklist 100% complete
- QA verification sign-off obtained
- Export classification documented
- Baseline traceability verified
- Dry run deployment successful
- All issues resolved or documented

### 6.4 Duration

2-3 weeks

## 7. Phase 4: CCB Review

### 7.1 Activities

#### 7.1.1 Submit to CCB

**Responsible:** Release Manager  
**Duration:** 1 day

Actions:
1. Package all documents for CCB review
2. Submit via CCB submission process (see [05-CCB/](../../05-CCB/))
3. Schedule CCB meeting
4. Distribute materials to CCB members (minimum 1 week advance)

#### 7.1.2 CCB Review Meeting

**Participants:** CCB members, Release Manager, domain experts  
**Duration:** 2-4 hours

Agenda:
1. Release overview (Release Manager) — 15 min
2. Technical review (Engineering Manager) — 30 min
3. Compliance review (Quality Manager) — 30 min
4. Safety review (Safety Manager) — 20 min
5. Security/Export review (Security Officer) — 15 min
6. Certification status (Certification Lead) — 20 min
7. Questions and discussion — 30 min
8. CCB decision — 10 min

#### 7.1.3 CCB Decision

**Accountable:** CCB Chair  

Possible decisions:
1. **Approved** — Release authorized for distribution
2. **Approved with conditions** — Minor issues must be resolved before distribution
3. **Deferred** — Significant issues require rework and resubmission
4. **Rejected** — Release not ready, major rework required

#### 7.1.4 Address CCB Actions

**Responsible:** Release Manager, Engineering  
**Duration:** Variable (hours to weeks depending on severity)

If conditions or deferrals:
1. Document all CCB action items
2. Assign owners and deadlines
3. Resolve issues
4. Update release package
5. Re-verify affected areas
6. Resubmit to CCB if required

### 7.2 Entry Criteria

- Phase 3 complete
- Package submitted to CCB at least 1 week in advance

### 7.3 Exit Criteria

- CCB approval obtained (unconditional or conditions met)
- Approval signatures collected
- CCB decision documented in release package SIGNOFF/

### 7.4 Duration

1-3 weeks (including potential rework)

## 8. Phase 5: Distribution

### 8.1 Activities

#### 8.1.1 Finalize Package

**Responsible:** Release Manager  
**Duration:** 1-2 days

Actions:
1. Add CCB approval signatures to manifest
2. Update release notes with final approval date
3. Regenerate hashes if any files changed
4. Create final distribution package
5. Verify package integrity

#### 8.1.2 Control Distribution

**Responsible:** Release Manager, IT  
**Duration:** 1 week

Actions:
1. Distribute per approved distribution list
2. Use secure channels (encrypted, authenticated)
3. Log each distribution in [03-REGISTERS/DISTRIBUTION_LOG.csv](../03-REGISTERS/DISTRIBUTION_LOG.csv)
4. Provide hash verification instructions
5. Track acknowledgments of receipt

Distribution channels:
- Internal: Secure file server, configuration management system
- External: Secure FTP, encrypted email, physical media (if required)

#### 8.1.3 Customer Notification

**Responsible:** Release Manager, Program Office  
**Duration:** 1 day

Actions:
1. Send release notification to customers/stakeholders
2. Include release notes summary
3. Provide access instructions
4. Communicate effectivity and compliance dates
5. Provide support contact information

### 8.2 Entry Criteria

- Phase 4 complete (CCB approval obtained)

### 8.3 Exit Criteria

- Distribution package delivered to all authorized recipients
- Distribution logged
- Acknowledgments received
- Notifications sent

### 8.4 Duration

1-2 weeks

## 9. Phase 6: Registration

### 9.1 Activities

#### 9.1.1 Update Release Register

**Responsible:** Release Manager  
**Duration:** 1 day

Update [03-REGISTERS/RELEASE_REGISTER.csv](../03-REGISTERS/RELEASE_REGISTER.csv):
- Release ID
- Version
- Type
- Status (released)
- Owner
- Gate
- Baseline reference
- SHA256 of distribution package
- Approval date
- Distribution date

#### 9.1.2 Archive Release Package

**Responsible:** Release Manager, Configuration Manager  
**Duration:** 1-2 days

Actions:
1. Create permanent archive in [05-AIRCRAFT/REL-ACFT-x.y.z/](../05-AIRCRAFT/) or [06-SPACECRAFT/REL-SC-x.y.z/](../06-SPACECRAFT/)
2. Ensure all directories per structure in problem statement
3. Create baseline reference symlink to [04-BASELINES/](../../04-BASELINES/)
4. Set read-only permissions
5. Backup to secondary location

#### 9.1.3 Update Baselines

**Responsible:** Configuration Manager  
**Duration:** 1 day

Actions:
1. Update baseline records in [04-BASELINES/](../../04-BASELINES/)
2. Cross-reference to release
3. Update configuration identification records

#### 9.1.4 Update Traceability

**Responsible:** Configuration Manager  
**Duration:** 1 day

Update [10-TRACEABILITY/CHANGE_BASELINE.csv](../../10-TRACEABILITY/CHANGE_BASELINE.csv):
- Link changes to release
- Update baseline mapping

### 9.2 Entry Criteria

- Phase 5 complete (distribution accomplished)

### 9.3 Exit Criteria

- Release register updated
- Release package archived
- Baselines updated
- Traceability updated
- Audit trail complete

### 9.4 Duration

1 week

## 10. Phase 7: Post-Release

### 10.1 Activities

#### 10.1.1 Monitor Deployment

**Responsible:** Release Manager, Operations  
**Duration:** Ongoing (3-6 months)

Track:
- Deployment status
- Issues reported
- Rollbacks (if any)
- Customer feedback

#### 10.1.2 Collect Metrics

**Responsible:** Release Manager, QA  
**Duration:** Ongoing

Metrics per [10-METRICS/](../10-METRICS/):
- Release cycle time
- Defects found post-release
- Compliance coverage
- Rollback frequency
- Customer satisfaction

#### 10.1.3 Post-Release Review

**Responsible:** Release Manager  
**Duration:** 1 meeting (2-3 hours)  
**Timing:** 3 months after release

Participants: All key stakeholders

Agenda:
1. Release execution review
2. Metrics review
3. Issues and resolutions
4. Lessons learned
5. Process improvements

#### 10.1.4 Lessons Learned

**Responsible:** Release Manager, Configuration Manager  
**Duration:** 1 week

Capture:
- What went well
- What could be improved
- Process gaps identified
- Tool enhancements needed
- Training needs

Document and share with program.

### 10.2 Entry Criteria

- Phase 6 complete (registration accomplished)
- Sufficient deployment time elapsed (typically 3 months)

### 10.3 Exit Criteria

- Post-release review completed
- Lessons learned documented
- Process improvements identified
- Metrics reported

### 10.4 Duration

Ongoing, with formal review at 3 months

## 11. Roles and Responsibilities

See [01-POLICY/RASCI.md](../01-POLICY/RASCI.md) for detailed RASCI matrix.

## 12. Templates and Tools

### 12.1 Templates

- [04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml](../04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml)
- [04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md](../04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md)
- [04-TEMPLATES/CONFORMITY_CHECKLIST.md](../04-TEMPLATES/CONFORMITY_CHECKLIST.md)

### 12.2 Tools

- Configuration management system (Git, PLM)
- SBOM generators (CycloneDX, SPDX)
- Provenance tools (in-toto, SLSA)
- Hash calculators (sha256sum)
- Archive tools (zip, tar)

## 13. Success Criteria

A successful release:
- Meets all conformity checklist requirements
- Obtains CCB approval
- Distributes on schedule
- Has zero critical issues in first 30 days
- Achieves >95% compliance coverage
- Receives positive customer feedback

## 14. Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md)
- [01-POLICY/RELEASE_TYPES.md](../01-POLICY/RELEASE_TYPES.md)
- [01-POLICY/VERSIONING_SCHEME.md](../01-POLICY/VERSIONING_SCHEME.md)
- [01-POLICY/RASCI.md](../01-POLICY/RASCI.md)
- [EMERGENCY_PATCH_WORKFLOW.md](./EMERGENCY_PATCH_WORKFLOW.md)
- [01-CM_PLAN.md](../../01-CM_PLAN.md)

## 15. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Configuration Manager |
