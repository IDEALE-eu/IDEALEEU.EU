# CONFIG — Configuration Management

## Purpose

This directory manages test configurations, baselines, and test article control for the 53-10 CENTER-BODY validation program, ensuring configuration integrity and traceability.

## Directory Structure

### BASELINES/
Configuration baselines for test articles and test setups.

**Baseline Types**:
- Design baseline (as-designed configuration)
- Manufacturing baseline (as-built configuration)
- Test baseline (as-tested configuration)
- Post-test baseline (as-inspected after test)

### TEST_ITEMS/
Individual test article configurations and modification history.

**Test Article Types**:
- Static test articles
- Fatigue test articles
- Environmental test articles
- Witness coupons
- Development test articles

## Configuration Baseline

### Baseline Documentation

Each baseline includes:

1. **Configuration Identification**
   - Test article serial number
   - Part numbers and revisions
   - Drawing numbers and revisions
   - Material specifications
   - Special processes

2. **As-Built Configuration**
   - Manufacturing records
   - Material certifications
   - Process certifications (cure cycles, NDT, etc.)
   - Deviation records
   - Quality acceptance records

3. **Instrumentation Configuration**
   - Sensor locations and orientations
   - Sensor part numbers and serial numbers
   - Calibration records
   - Wiring diagrams
   - DAQ system configuration

4. **Test Configuration**
   - Test rig configuration
   - Boundary conditions (supports, constraints)
   - Load application method
   - Environmental chamber setup (if applicable)
   - Safety systems

5. **Modification History**
   - All modifications from design baseline
   - Engineering change orders (ECOs)
   - Repair records
   - Configuration change records

### Baseline Control

**Baseline Approval**:
- Engineering approval for design baseline
- Manufacturing approval for as-built baseline
- Test Engineering approval for test baseline
- Configuration Control Board (CCB) approval for changes

**Baseline Format**: `BASELINES/[TEST_ARTICLE_ID]/Baseline_[TYPE]_[DATE].pdf`

## Test Article Management

### Test Article Numbering

Format: `TA-53-10-[TYPE]-[SEQ]`

**Type Codes**:
- **STA**: Static test article
- **FAT**: Fatigue test article
- **ENV**: Environmental test article
- **DTM**: Development test model
- **WIT**: Witness coupon

Examples:
- `TA-53-10-STA-001`: Static test article #1
- `TA-53-10-FAT-002`: Fatigue test article #2

### Test Article Documentation

Each test article folder contains:

1. **Test Article Data Package**
   - Design drawings and specifications
   - Manufacturing travelers
   - Material certifications
   - Quality acceptance records
   - Photos of as-built article

2. **Instrumentation Package**
   - Sensor installation drawings
   - Sensor calibration records
   - Wiring schematics
   - DAQ configuration files

3. **Test History**
   - Tests performed
   - Test conditions
   - Observations and anomalies
   - Post-test inspection reports

4. **Modification Records**
   - ECOs applied
   - Repair records
   - Configuration changes

5. **Disposition**
   - Test completion status
   - Final condition assessment
   - Disposition (retain, scrap, archive)

### Test Article Status

Track test article status:
- **PLANNED**: Test article planned, not yet fabricated
- **FABRICATION**: Under manufacture
- **ACCEPTANCE**: Undergoing acceptance inspection
- **READY**: Ready for test, in storage
- **IN-TEST**: Currently being tested
- **POST-TEST**: Test complete, awaiting disposition
- **RETAINED**: Retained for future use or reference
- **SCRAPPED**: Disposed of per procedure
- **ARCHIVED**: Preserved for historical record

**Status Tracker**: `TEST_ITEMS/Test_Article_Status.xlsx`

## Configuration Change Control

### Change Process

1. **Change Request**: Identify need for change
2. **Impact Assessment**: Evaluate effect on tests, schedule, cost
3. **CCB Review**: Configuration Control Board reviews change
4. **Approval**: CCB approves or rejects change
5. **Implementation**: Change implemented with ECO
6. **Verification**: Change verified correct
7. **Documentation**: Configuration records updated

### Engineering Change Order (ECO)

**ECO Contents**:
- ECO number and date
- Description of change
- Reason for change
- Affected test articles
- Impact assessment
- Approval signatures
- Implementation instructions
- Verification requirements

**ECO Format**: `CONFIG/ECO/ECO-53-10-[YEAR]-[SEQ].pdf`

### Configuration Control Board (CCB)

**CCB Members**:
- Chief Engineer (chair)
- Test Engineering Lead
- Certification Manager
- Quality Manager
- Configuration Manager

**CCB Authority**:
- Approve/reject configuration changes
- Approve test article modifications
- Approve baseline changes
- Resolve configuration conflicts

## Configuration Audit

### Physical Configuration Audit (PCA)

Verify as-built configuration matches documentation:
- Visual inspection
- Dimensional verification
- Material verification
- Process verification
- Instrumentation verification

**Frequency**: Before first test, after major modifications

**Report**: `CONFIG/Audits/PCA_[TEST_ARTICLE]_[DATE].pdf`

### Functional Configuration Audit (FCA)

Verify test article performs as intended:
- Pre-test functional checks
- Instrumentation functionality
- System integration checks

**Frequency**: Before each test campaign

**Report**: `CONFIG/Audits/FCA_[TEST_ARTICLE]_[DATE].pdf`

## Configuration Database

Maintain configuration database:
- Test article inventory
- Baseline configurations
- Modification history
- Current status
- Location tracking
- Test history

**Database**: `CONFIG/Configuration_Database.xlsx`

## References

- Design drawings: `../../../CAD/`
- Test procedures: `../../PROCEDURES/`
- Quality records: `../../QA/`
- Change control: Company configuration management procedures

---

**Owner**: Configuration Manager with Test Engineering support  
**CCB**: Meets as needed, minimum monthly during active testing  
**Audit**: PCA before first test, FCA before each campaign  
**Database**: Updated continuously, audited quarterly
