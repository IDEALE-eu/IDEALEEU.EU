# Runbook

**Baseline**: GenSTD-[TIER]-YYYY-NNNN  
**Target Time**: ≤15 minutes from clean machine  
**Last Tested**: YYYY-MM-DD

---

## Purpose

This runbook provides step-by-step instructions to reproduce, validate, or implement this baseline from a clean machine in 15 minutes or less.

---

## Prerequisites

### System Requirements

- **OS**: [Linux / macOS / Windows / Any]
- **RAM**: [Minimum required]
- **Disk**: [Minimum required]
- **Network**: [Internet required? Specific access needed?]

### Software Dependencies

```bash
# List all required software with versions
- Python 3.9+
- Node.js 18+
- Git 2.x
- [Other tools]
```

### Access Requirements

- [ ] Repository access: [URL or path]
- [ ] Credentials: [What credentials are needed?]
- [ ] VPN: [Required? Which network?]
- [ ] Licenses: [Any licensed tools?]

---

## Quick Start

For experienced users, these commands should complete the full setup:

```bash
# Clone and setup (adjust to your baseline)
git clone <repo-url>
cd <baseline-directory>
./setup.sh
./validate.sh
```

Expected output: `✓ All validations passed`

---

## Detailed Steps

### Step 1: Environment Setup

**Time**: ~2 minutes

```bash
# 1. Clone the repository
git clone https://github.com/IDEALE-eu/IDEALEEU.EU
cd IDEALEEU.EU

# 2. Navigate to baseline directory
cd 00-PROGRAM/CONFIG_MGMT/04-BASELINES/GenSTD/[TIER]/[BASELINE-ID]

# 3. Check prerequisites
./check_prerequisites.sh
```

**Expected output**:
```
✓ Python 3.9+ detected
✓ All dependencies available
✓ Repository structure valid
```

**Troubleshooting**:
- If Python not found: Install from [python.org](https://python.org)
- If git fails: Check network connection and credentials

---

### Step 2: Install Dependencies

**Time**: ~3 minutes

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (if applicable)
npm install

# Install system packages (if needed)
# Example for Ubuntu/Debian:
# sudo apt-get update && sudo apt-get install -y [packages]
```

**Expected output**:
```
Successfully installed [packages]
```

**Troubleshooting**:
- If pip fails: Try `python3 -m pip install -r requirements.txt`
- If npm fails: Clear cache with `npm cache clean --force`

---

### Step 3: Configuration

**Time**: ~2 minutes

```bash
# Copy configuration template
cp config.template.yaml config.yaml

# Edit configuration (update with your values)
# Key settings to change:
# - baseline_id: GenSTD-[TIER]-YYYY-NNNN
# - environment: [dev/test/prod]
# - [other settings]

# Validate configuration
./validate_config.sh
```

**Expected output**:
```
✓ Configuration valid
✓ All required fields present
```

---

### Step 4: Build/Generate Artifacts

**Time**: ~5 minutes

```bash
# Build the baseline artifacts
./build.sh

# This should:
# 1. Generate documentation
# 2. Compile diagrams
# 3. Create manifest checksums
# 4. Run EHC validation
```

**Expected output**:
```
Building baseline GenSTD-[TIER]-YYYY-NNNN...
✓ Documentation generated
✓ Diagram compiled
✓ Checksums computed
✓ EHC validation passed
Build complete in 4m 23s
```

**Troubleshooting**:
- If diagram fails: Check that graphviz is installed
- If validation fails: Review SUMMARY.md word count and readability

---

### Step 5: Verification

**Time**: ~3 minutes

```bash
# Run full validation suite
./validate.sh

# This checks:
# - MANIFEST.json schema compliance
# - EHC artifact completeness
# - Diagram presence
# - Readability scores
# - Cross-references
# - Hash integrity
```

**Expected output**:
```
Running GenSTD EHC validation...
✓ MANIFEST.json valid
✓ SUMMARY.md word count: 148/150 ✓
✓ SUMMARY.md readability: FK 11.2 ✓
✓ DIAGRAM.svg present ✓
✓ DECISIONS.md complete ✓
✓ GLOSSARY.md complete ✓
✓ RUNBOOK.md complete ✓
✓ RISKS.md complete ✓
✓ All cross-references resolve ✓
✓ Hash integrity verified ✓

All validations PASSED ✓
```

---

## Rollback

If something goes wrong, rollback to previous state:

```bash
# Revert to last known good state
git checkout HEAD~1

# Or restore from backup
./restore_backup.sh <backup-id>

# Verify rollback
./validate.sh
```

---

## Advanced Usage

### Running Specific Validations

```bash
# Check only EHC compliance
python validate_ehc.py .

# Check only MANIFEST.json
jsonschema -i MANIFEST.json ../TEMPLATES/MANIFEST.schema.json

# Check only readability
python check_readability.py SUMMARY.md
```

### Updating the Baseline

```bash
# Make changes
vim [files]

# Regenerate checksums
./update_checksums.sh

# Validate changes
./validate.sh

# Commit
git add .
git commit -m "Update baseline: [description]"
```

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Validation fails | Missing artifact | Check all required files exist |
| Word count exceeded | SUMMARY.md too long | Edit to ≤150 words |
| Readability too low | Complex language | Simplify, use shorter sentences |
| Hash mismatch | File modified | Regenerate with `./update_checksums.sh` |
| Diagram missing | Build failed | Install graphviz, rebuild |

### Getting Help

- **Documentation**: [GenSTD README](../README.md)
- **Issues**: [GitHub Issues](https://github.com/IDEALE-eu/IDEALEEU.EU/issues)
- **Contact**: Configuration Management team

---

## Verification Checklist

After completing all steps, verify:

- [ ] All commands completed without errors
- [ ] `./validate.sh` returns all green checks
- [ ] Diagram renders correctly
- [ ] All cross-references work
- [ ] Total time was ≤15 minutes

---

## Maintenance

**Tested by**: [Name]  
**Last test date**: YYYY-MM-DD  
**Next review**: YYYY-MM-DD  
**Status**: [Passing / Needs update]

---

*This runbook must be tested on a clean machine every [frequency] to ensure it remains valid.*
