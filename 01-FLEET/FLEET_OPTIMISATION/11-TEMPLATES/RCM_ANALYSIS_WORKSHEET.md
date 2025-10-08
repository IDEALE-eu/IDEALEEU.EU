# RCM Analysis Worksheet

## Overview

This worksheet template guides the reliability-centered maintenance (RCM) analysis process to systematically determine the most appropriate maintenance strategies for systems and components.

## RCM Analysis Steps

### 1. System Definition and Boundaries

#### System Information
- **System ID**: [Unique identifier]
- **System Name**: [e.g., Hydraulic System, Propulsion System]
- **Aircraft/Spacecraft Type**: [Type designation]
- **ATA/System Code**: [Classification code]
- **Analysis Date**: [Date]
- **Analysis Team**: [Names and roles]

#### System Boundaries
- **Interfaces**: [Connected systems]
- **Scope**: [What is included/excluded]
- **Operating Context**: [Normal operating conditions]

### 2. Functions and Functional Failures

| Function ID | Function Description | Performance Standard | Functional Failure |
|-------------|---------------------|---------------------|-------------------|
| F01 | [Primary function] | [Quantitative standard] | [Loss of function] |
| F02 | [Secondary function] | [Quantitative standard] | [Partial loss] |

**Function Description Format**: 
- What the system does
- Performance level expected
- Operating context

### 3. Failure Modes and Effects Analysis (FMEA)

| Failure Mode ID | Failure Mode | Failure Cause | Local Effect | System Effect | End Effect | Detection Method |
|-----------------|--------------|---------------|--------------|---------------|------------|------------------|
| FM01 | [How it fails] | [Why it fails] | [Impact at component] | [Impact on system] | [Impact on aircraft/mission] | [How detected] |

### 4. Consequence Classification

For each failure mode, classify consequences:

| Failure Mode | Hidden (H/Y/N) | Safety (H/Y/N) | Operational (H/Y/N) | Economic (H/Y/N) | Consequence Category |
|--------------|----------------|----------------|---------------------|------------------|---------------------|
| FM01 | | | | | [Safety/Operational/Economic/Hidden] |

**Consequence Definitions**:
- **Safety**: Could cause injury or death
- **Operational**: Impairs mission capability
- **Economic**: Only economic impact (cost of repair)
- **Hidden**: Failure not evident to operating crew

### 5. Task Selection Logic

Apply RCM decision logic based on consequence category:

#### For Safety Consequences:
1. Is there a scheduled on-condition task that reduces risk to acceptable level? → **On-Condition Task**
2. Is there a scheduled restoration/discard task that reduces risk to acceptable level? → **Scheduled Restoration/Discard**
3. Is there a combination of tasks that reduces risk? → **Combination of Tasks**
4. If no effective tasks → **Redesign** (or accept risk if tolerable)

#### For Operational/Economic Consequences:
1. Is there a scheduled on-condition task that is cost-effective? → **On-Condition Task**
2. Is there a scheduled restoration/discard task that is cost-effective? → **Scheduled Restoration/Discard**
3. Is there a failure finding task for hidden failures? → **Failure Finding Task**
4. If no cost-effective tasks → **Run-to-Failure** (corrective maintenance)

### 6. Maintenance Task Specification

| Task ID | Failure Mode | Task Description | Task Type | Interval | Resources Required | Acceptance Criteria |
|---------|--------------|------------------|-----------|----------|-------------------|-------------------|
| MT01 | FM01 | [Detailed task description] | [On-Condition/Restoration/Discard/FF] | [Hours/cycles/calendar] | [Labor, tools, parts] | [Pass/fail criteria] |

**Task Types**:
- **On-Condition (Condition Monitoring)**: Inspect, test, or monitor to detect pending failure
- **Scheduled Restoration**: Overhaul or refurbish at specified interval
- **Scheduled Discard**: Replace at specified interval regardless of condition
- **Failure Finding**: Periodic test to detect hidden failures
- **Run-to-Failure**: No preventive task, repair when failure occurs

### 7. Task Interval Optimization

| Task ID | Initial Interval | Failure Distribution | P-F Interval | Optimized Interval | Rationale |
|---------|------------------|---------------------|--------------|-------------------|-----------|
| MT01 | [Initial] | [Weibull, exponential, etc.] | [If applicable] | [Optimized] | [Statistical/cost/risk basis] |

**P-F Interval**: Time between potential failure (detectable) and functional failure

### 8. Cost-Benefit Analysis

| Task ID | Preventive Task Cost | Failure Cost (Average) | Task Effectiveness | Net Benefit | Decision |
|---------|---------------------|------------------------|-------------------|-------------|----------|
| MT01 | $[Cost per task] | $[Cost of failure] | [Probability reduction] | $[Annual savings] | [Implement/Reject] |

### 9. Implementation Plan

| Task ID | Implementation Date | Training Required | Tooling Required | Documentation Updates | Responsibility |
|---------|-------------------|-------------------|------------------|---------------------|----------------|
| MT01 | [Date] | [Yes/No, description] | [List special tools] | [Manuals, task cards] | [Name/role] |

### 10. Review and Continuous Improvement

- **Review Frequency**: [Quarterly/Annual]
- **Performance Metrics**: [Reliability, cost, compliance]
- **Feedback Mechanism**: [How operational data informs updates]
- **Change Management**: [Process for task adjustments]

## RCM Analysis Review and Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Analysis Lead | | | |
| Engineering Manager | | | |
| Maintenance Manager | | | |
| Safety Manager | | | |
| Regulatory Compliance | | | |

## References

- RCM methodology: SAE JA1011/JA1012
- Maintenance program: **04-MAINTENANCE_PLANNING/MAINTENANCE_PROGRAM.md**
- Reliability data: **01-FLEET/OPERATIONAL_DATA_HUB/**
- Digital thread: **08-INTEGRATIONS/DIGITAL_THREAD_HOOKS.md**

## Appendices

### A. RCM Decision Diagram
[Include standard RCM decision logic flowchart]

### B. Failure Mode Examples
[Industry examples for reference]

### C. Task Type Descriptions
[Detailed descriptions and examples of each task type]

### D. Acronyms and Definitions
- **FMEA**: Failure Mode and Effects Analysis
- **P-F Interval**: Potential-to-Functional failure interval
- **MTBF**: Mean Time Between Failures
- **MTBUR**: Mean Time Between Unscheduled Removals
