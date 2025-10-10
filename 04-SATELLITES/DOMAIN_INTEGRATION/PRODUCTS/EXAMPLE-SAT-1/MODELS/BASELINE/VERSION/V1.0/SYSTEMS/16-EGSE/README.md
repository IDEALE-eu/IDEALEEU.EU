# 16-EGSE — Electrical Ground Support Equipment

**Status:** Non-flight. Ground use only. Not part of flight mass/power/thermal/reliability budgets.

## Purpose
Provide power, stimulus, monitoring, and command/telemetry interfaces during AIT. Support functional tests, software load, and end-to-end checkout.

## Scope
- Power supplies, distribution, protections
- Telemetry/command front-ends and simulators
- Harness break-out panels and patching
- Load banks and signal conditioners
- Time sync and data recording

## Interfaces
- Flight systems via central ICDs in `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- Typical links: 51-PRIMARY_STRUCTURE (fixtures), 97-ELECTRICAL_HARNESS (test harness), 50-MECHANISMS_DEPLOYABLES (actuation tests)

## Compliance
- Follow project ground-support standards referenced in `00-PROGRAM/STANDARDS/`
- Cleanliness and ESD controls per program rules

## Governance
- No PLM/CAx here. No `SUBSYSTEMS/`. No local ICDs or test docs.
- EGSE hardware and procedures live in engineering workspaces; only references tracked centrally.

## Ownership
AIT Electrical (EGSE Lead). Changes via ECR/ECO in `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`.

