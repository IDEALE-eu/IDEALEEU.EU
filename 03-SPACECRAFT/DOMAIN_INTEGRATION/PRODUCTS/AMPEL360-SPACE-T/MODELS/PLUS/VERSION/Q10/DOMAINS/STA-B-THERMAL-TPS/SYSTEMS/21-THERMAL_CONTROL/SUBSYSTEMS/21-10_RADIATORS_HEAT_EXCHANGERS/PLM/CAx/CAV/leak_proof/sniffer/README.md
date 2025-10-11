# SNIFFER — Helium Leak Sniffer Testing

## Purpose

This directory contains helium leak detector (sniffer) test logs, leak rates, and scan location maps.

## Contents

- Leak detector output logs
- Leak rate measurements (scc/s)
- Scan location maps and photos
- Leak identification and tagging
- Re-test data after repairs

## File Naming Convention

```
LEAK_<serial>_<date>_<status>.<ext>
```

Examples:
- `LEAK_RAD-SN001_20251011_INITIAL.txt`
- `LEAK_HX-SN005_20251012_RETEST_after_repair.txt`
- `LEAK_CP123_20251015_FINAL_PASS.csv`

## Test Procedure

### Setup
1. Pressurize test article with helium
2. Wait for stabilization (typically 30 min)
3. Calibrate leak detector
4. Document pressure and helium concentration

### Execution
1. Scan all welds systematically
2. Scan all joints and fittings
3. Document scan path and dwell time
4. Record leak rates at each location
5. Tag any leak locations

### Acceptance
- **Pass**: All locations <1×10⁻⁶ scc/s
- **Fail**: Any location ≥1×10⁻⁶ scc/s
- **Repair**: Identify and fix leaks, re-test

## Data Collection

For each test, record:
- Test article serial number
- Test date and technician
- Leak detector ID and calibration
- Helium pressure in test article
- Ambient conditions
- Leak rates at all scan locations
- Photos of any leak locations

## Leak Documentation

If leaks found, document:
- 📍 **Location**: Weld ID, joint ID, coordinates
- 📊 **Leak Rate**: scc/s measurement
- 📷 **Photo**: Close-up of leak location
- 🏷️ **Tag**: Physical tag on hardware
- 📝 **Repair Plan**: How leak will be addressed

## Re-Test After Repair

After leak repair:
- Re-test entire system (not just repair location)
- Document leak rate at repair location
- Verify overall system leak rate acceptable
- Update test status to "PASS" if compliant

## Acceptance Criteria

- ✅ No individual leak >1×10⁻⁶ scc/s
- ✅ Total system leak rate documented
- ✅ All scan locations verified
- ✅ Photos of all leak locations (if any)
- ✅ Re-test after repair passes

## Related Directories

- **[../proof/](../proof/)** — Proof pressure testing
- **[../../procedures/](../../procedures/)** — Leak test procedures
- **[../../anomalies/](../../anomalies/)** — Leak repair NCRs

---

**Last Updated**: 2025-10-10
