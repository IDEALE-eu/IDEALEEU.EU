# PROCEDURES — Test Procedures

## Purpose

This directory contains detailed test procedures (PRO) for executing tests on radiators, heat exchangers, and thermal control hardware.

## Contents

Test procedures documenting:
- Step-by-step test execution instructions
- Chamber/rig setup procedures
- Safety protocols and precautions
- Instrumentation installation and checkout
- Data acquisition configuration
- Emergency procedures
- Post-test activities

## File Naming Convention

```
PRO-21-10-<test-type>__r<NN>__<status>.pdf
```

Examples:
- `PRO-21-10-tvac_setup__r01__REL.pdf`
- `PRO-21-10-leak_sniffer__r02__RVW.pdf`
- `PRO-21-10-coldplate_perf__r01__REL.pdf`

### Status Codes
- **WIP** — Work in progress
- **RVW** — Under review
- **REL** — Released/approved

## Procedure Requirements

Each test procedure should include:
- **Scope**: Applicable hardware and test conditions
- **References**: Test plan, drawings, specifications
- **Personnel**: Required roles and qualifications
- **Equipment**: List of all required equipment
- **Safety**: Hazards, PPE, emergency procedures
- **Setup**: Detailed setup instructions with photos
- **Pre-Test**: Checks, calibrations, verifications
- **Execution**: Step-by-step test steps
- **Data Collection**: What to record and when
- **Post-Test**: Shutdown, inspection, preservation
- **Deviations**: How to handle and document deviations

## Procedure Types

### Setup Procedures
- Chamber installation and mounting
- Instrumentation installation
- Plumbing and electrical connections
- Fixture installation

### Test Execution Procedures
- TVAC test execution
- Leak test execution
- Pressure proof/burst testing
- Vibration test execution
- Thermal performance testing

### Safety Procedures
- Emergency shutdown procedures
- Hazardous material handling
- Pressure system safety
- Vacuum system safety

## Safety Requirements

All procedures must include:
- ⚠️ **Hazard identification** and risk assessment
- 🦺 **PPE requirements** for all personnel
- 🚨 **Emergency procedures** and contacts
- 🛑 **Stop work conditions** clearly defined
- ✅ **Safety checks** at critical steps

## Approval Requirements

Test procedures require approval from:
- ✅ Test engineer
- ✅ Safety officer
- ✅ Quality assurance
- ✅ Facility manager (for facility procedures)

## Execution Guidelines

**DO**:
- Follow procedures exactly as written
- Document all deviations immediately
- Stop if unexpected conditions occur
- Communicate issues to test director
- Complete all data sheets

**DO NOT**:
- Skip steps or take shortcuts
- Proceed if safety concerns arise
- Make undocumented changes
- Continue if equipment malfunctions

## Related Directories

- **[../plans/](../plans/)** — Test plans
- **[../setups/](../setups/)** — Setup configurations
- **[../templates/](../templates/)** — Procedure templates
- **[../anomalies/](../anomalies/)** — Deviation records

---

**Last Updated**: 2025-10-10
