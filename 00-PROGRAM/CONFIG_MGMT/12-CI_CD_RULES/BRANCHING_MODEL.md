# Git Branching Model

## Overview

This document defines the Git branching strategy for the IDEALE EU aerospace program repository. The branching model supports parallel development, configuration management, and release management while maintaining baseline integrity.

## Branch Types

### 1. Main Branch

**Branch:** `main`

- **Purpose:** Production-ready code and documentation
- **Protection:** Fully protected, requires CCB approval for merges
- **Baseline:** Represents approved program baselines
- **Merges:** Only from `release/*` or `hotfix/*` branches
- **Tags:** All official releases tagged on main

**Protection Rules:**
- Require pull request reviews (minimum 2 approvals)
- Require CCB member approval
- Require status checks to pass
- Require branches to be up to date
- Require signed commits
- Restrict push access (only release managers)
- No force push
- No deletions

### 2. Develop Branch

**Branch:** `develop`

- **Purpose:** Integration branch for ongoing development
- **Protection:** Protected, requires review
- **Baseline:** Working baseline between stage gates
- **Merges:** From `feature/*` branches
- **Tags:** Pre-release versions

**Protection Rules:**
- Require pull request reviews (minimum 1 approval)
- Require status checks to pass
- Require linear history
- No force push

### 3. Feature Branches

**Branch Pattern:** `feature/[feature-name]`

**Examples:**
- `feature/wing-design-update`
- `feature/gnc-algorithm-improvement`
- `feature/ecr-1234-implement`

- **Purpose:** Development of new features, changes, or ECOs
- **Created From:** `develop`
- **Merged To:** `develop`
- **Lifetime:** Duration of development effort
- **Naming:** Descriptive, lowercase with hyphens
- **Delete:** After merge to develop

**Workflow:**
```bash
# Create feature branch
git checkout develop
git pull origin develop
git checkout -b feature/my-feature

# Work on feature
git add .
git commit -m "Implement feature component"

# Keep updated with develop
git checkout develop
git pull origin develop
git checkout feature/my-feature
git rebase develop

# Create pull request to develop
# After approval and merge, delete branch
git push origin --delete feature/my-feature
```

### 4. Release Branches

**Branch Pattern:** `release/[version]`

**Examples:**
- `release/srr-baseline`
- `release/pdr-baseline`
- `release/v1.0.0`

- **Purpose:** Preparation for baseline release at stage gates
- **Created From:** `develop`
- **Merged To:** `main` and `develop`
- **Lifetime:** Duration of release preparation and testing
- **Naming:** Stage gate or version number
- **Delete:** After merge to main

**Workflow:**
```bash
# Create release branch
git checkout develop
git pull origin develop
git checkout -b release/pdr-baseline

# Finalize release (bug fixes only, no new features)
# Update version numbers, documentation
git add .
git commit -m "Prepare PDR baseline release"

# Merge to main
git checkout main
git pull origin main
git merge --no-ff release/pdr-baseline
git tag -a PDR-BASELINE-v1.0 -m "PDR Baseline"
git push origin main --tags

# Merge back to develop
git checkout develop
git pull origin develop
git merge --no-ff release/pdr-baseline
git push origin develop

# Delete release branch
git push origin --delete release/pdr-baseline
```

### 5. Hotfix Branches

**Branch Pattern:** `hotfix/[issue-description]`

**Examples:**
- `hotfix/critical-safety-issue`
- `hotfix/ecr-5678-urgent`

- **Purpose:** Emergency fixes to production baseline
- **Created From:** `main`
- **Merged To:** `main` and `develop`
- **Lifetime:** Duration of hotfix development
- **Priority:** Highest, requires expedited CCB review
- **Delete:** After merge

**Workflow:**
```bash
# Create hotfix branch
git checkout main
git pull origin main
git checkout -b hotfix/critical-issue

# Fix the issue
git add .
git commit -m "Fix critical safety issue"

# Merge to main
git checkout main
git pull origin main
git merge --no-ff hotfix/critical-issue
git tag -a HOTFIX-v1.0.1 -m "Critical safety fix"
git push origin main --tags

# Merge to develop
git checkout develop
git pull origin develop
git merge --no-ff hotfix/critical-issue
git push origin develop

# Delete hotfix branch
git push origin --delete hotfix/critical-issue
```

### 6. ECR/ECO Branches

**Branch Pattern:** `ecr/[ecr-number]-[description]` or `eco/[eco-number]-[description]`

**Examples:**
- `ecr/1234-wing-material-change`
- `eco/5678-update-manufacturing-process`

- **Purpose:** Implementation of approved Engineering Change Requests/Orders
- **Created From:** `develop` (ECR) or `release/*` (ECO if affecting baseline)
- **Merged To:** `develop` or release branch
- **Lifetime:** Duration of implementation
- **Requires:** ECR approval before merge
- **Delete:** After merge

### 7. Baseline Branches

**Branch Pattern:** `baseline/[gate]-[date]`

**Examples:**
- `baseline/srr-20240315`
- `baseline/cdr-20241001`

- **Purpose:** Long-lived branches capturing stage gate baselines
- **Created From:** `main` at baseline tag
- **Merged To:** Never (read-only)
- **Lifetime:** Permanent (archived)
- **Protection:** Read-only after creation
- **Purpose:** Historical reference and traceability

**Workflow:**
```bash
# Create baseline branch from main at tag
git checkout main
git pull origin main
git checkout -b baseline/cdr-20241001 CDR-BASELINE-v1.0
git push origin baseline/cdr-20241001
```

## Branch Workflow Summary

```
main (production baselines)
  ↑
  └── release/pdr-baseline
        ↑
      develop (integration)
        ↑
        ├── feature/wing-design
        ├── feature/gnc-update
        └── ecr/1234-change
```

## Pull Request Process

### 1. Create Pull Request
- Create PR from feature/ECR branch to develop
- Fill out PR template with description and checklist
- Link related issues/ECRs
- Assign reviewers (CODEOWNERS auto-assigned)

### 2. Review Process
- Code/document review by peers
- Configuration Manager review for CM compliance
- CCB member review for baseline changes
- Automated checks must pass (linting, tests, etc.)

### 3. Approval and Merge
- Minimum approvals obtained
- All comments addressed
- CI/CD checks passed
- Squash or merge commit (maintain history)
- Delete source branch after merge

## Commit Message Guidelines

Format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Build process or auxiliary tool changes
- `ecr`: ECR implementation
- `eco`: ECO implementation

**Example:**
```
feat(aircraft/wing): Update wing spar material to Al 7050

Implement ECR-1234 to change wing spar material from Al 7075-T6
to Al 7050-T7 for improved fatigue resistance.

ECR-1234
Reviewed-by: J. Smith
```

## Configuration Management Integration

### Baselines and Tags
- Stage gate baselines tagged on `main`: `SRR-BASELINE-v1.0`, `PDR-BASELINE-v1.0`, etc.
- Pre-releases tagged on `develop`: `v0.1.0-alpha`, `v0.2.0-beta`
- Hotfixes tagged: `HOTFIX-v1.0.1`

### CCB Process
1. ECR submitted and assigned number
2. Feature branch created: `ecr/[number]-[description]`
3. Development work completed
4. PR created for CCB review
5. CCB reviews and approves/rejects
6. If approved, becomes ECO and merged
7. If rejected, branch closed without merge

### Traceability
- All commits linked to requirements or ECRs in commit message
- PRs linked to issues/ECRs
- Tags mark official baselines
- Baseline branches preserve history

## Tool Configuration

### Git Configuration
```bash
# Recommended Git settings
git config --global core.autocrlf input
git config --global pull.rebase false
git config --global init.defaultBranch main
git config --global commit.gpgsign true
```

### .gitignore
See repository root `.gitignore` for excluded files.

## Best Practices

### Do's
- ✅ Create feature branches from develop
- ✅ Keep branches short-lived (< 2 weeks if possible)
- ✅ Rebase feature branches regularly with develop
- ✅ Write clear, descriptive commit messages
- ✅ Link commits to ECRs/requirements
- ✅ Delete branches after merge
- ✅ Tag all baselines
- ✅ Use signed commits for traceability

### Don'ts
- ❌ Don't commit directly to main or develop
- ❌ Don't force push to protected branches
- ❌ Don't merge without PR and review
- ❌ Don't include generated files or binaries (use .gitignore)
- ❌ Don't create long-lived feature branches
- ❌ Don't merge unreviewed code
- ❌ Don't modify baseline branches

## Emergency Procedures

For critical production issues:
1. Create hotfix branch from main
2. Implement fix with expedited review
3. Emergency CCB meeting if required
4. Fast-track PR approval
5. Merge to main and develop
6. Create hotfix tag
7. Notify all stakeholders

## Branch Metrics

Track and report:
- Open feature branches by age
- Average PR cycle time
- Branch merge frequency
- Number of active branches
- Baseline tag history

---

**Document Owner:** Configuration Management  
**Maintained By:** DevOps Team  
**Review Frequency:** Quarterly or as needed
