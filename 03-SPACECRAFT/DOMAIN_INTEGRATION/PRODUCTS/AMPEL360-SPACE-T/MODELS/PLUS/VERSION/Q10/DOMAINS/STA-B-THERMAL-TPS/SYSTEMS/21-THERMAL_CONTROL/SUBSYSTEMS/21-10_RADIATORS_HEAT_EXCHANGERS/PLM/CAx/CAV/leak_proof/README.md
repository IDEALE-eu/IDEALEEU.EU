# LEAK_PROOF — Leak Detection and Pressure Testing

## Purpose

This directory contains leak detection test data, proof pressure testing, and burst test results for fluid systems in radiators and heat exchangers.

## Contents

- **[sniffer/](sniffer/)** — Helium leak sniffer logs and locations
- **[proof/](proof/)** — Proof pressure test traces
- **[burst/](burst/)** — Burst test curves and failure photos

## Test Objectives

### Leak Testing
- Verify no leakage above <1×10⁻⁶ scc/s per joint
- Scan all welds, fittings, and joints
- Identify and document leak locations
- Verify repairs effective

### Proof Testing
- Demonstrate structural integrity at 1.5× MEOP
- Hold pressure for 5 minutes minimum
- Verify no permanent deformation
- Confirm no leakage increase

### Burst Testing (Witness Sample)
- Validate design safety factor
- Document failure mode and location
- Measure burst pressure
- Confirm margin to operating pressure

## Test Requirements

All pressure vessels and fluid systems must:
- ✅ Pass helium leak test
- ✅ Pass proof pressure test
- ✅ Have witness burst test data
- ✅ Be certified for flight use

## Safety Requirements

Pressure testing requires:
- ⚠️ **Pressure containment** or blast shield
- 🦺 **Personnel exclusion** during pressurization
- 🚨 **Overpressure protection** installed
- 📹 **Remote monitoring** capability
- 🛑 **Emergency shutdown** procedures

## Related Directories

- **[../plans/](../plans/)** — Leak/proof test plans
- **[../procedures/](../procedures/)** — Test procedures
- **[../reports/](../reports/)** — Test reports
- **[../anomalies/](../anomalies/)** — Leak repair records

---

**Last Updated**: 2025-10-10
