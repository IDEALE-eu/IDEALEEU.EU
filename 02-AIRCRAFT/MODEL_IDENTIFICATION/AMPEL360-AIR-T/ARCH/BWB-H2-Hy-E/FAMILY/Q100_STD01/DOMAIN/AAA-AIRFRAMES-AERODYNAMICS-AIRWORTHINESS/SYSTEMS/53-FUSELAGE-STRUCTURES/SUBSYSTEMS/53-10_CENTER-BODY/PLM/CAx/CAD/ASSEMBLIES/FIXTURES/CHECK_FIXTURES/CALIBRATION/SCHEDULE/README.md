# SCHEDULE — Calibration Schedules

## Purpose

This directory contains calibration schedules and planning documents for check fixtures and inspection equipment.

## Contents

### Schedule Types
- **Master calibration schedule**: All equipment and due dates
- **Monthly schedules**: Equipment due in upcoming month
- **Equipment-specific schedules**: Individual calibration plans
- **Critical equipment schedules**: Priority items

## Naming Convention

Use the following pattern:
```
CAL_SCHEDULE_<period>_<version>.xlsx
```

Examples:
- `CAL_SCHEDULE_2024_v01.xlsx`
- `CAL_SCHEDULE_2024-Q1_v02.xlsx`
- `CAL_SCHEDULE_MONTHLY_2024-01_v01.xlsx`

## Schedule Format

### Required Information
- **Equipment ID**: Unique identifier
- **Description**: Equipment name and type
- **Location**: Where equipment is stored/used
- **Calibration frequency**: Interval (annual, semi-annual, etc.)
- **Last calibration date**: Date of most recent calibration
- **Next due date**: When calibration is required
- **Status**: Current, due soon, overdue
- **Responsible person**: Who manages calibration
- **Notes**: Special requirements or conditions

## Schedule Management

### Planning Process
1. Review master schedule monthly
2. Identify equipment due within 60 days
3. Schedule calibration appointments
4. Arrange equipment availability
5. Coordinate with calibration lab
6. Track completion
7. Update schedule with results

### Status Categories
- **Current**: Calibration valid, not due yet
- **Due soon**: Within 30 days of due date
- **Due**: Past due date but within grace period
- **Overdue**: Past grace period, remove from service
- **In calibration**: Currently at calibration lab

### Grace Period
- Standard: 0 days (must be calibrated by due date)
- With approval: Up to 15 days for non-critical items
- Critical equipment: No grace period allowed

## Calibration Tracking

### Key Metrics
- Percent current: Target 100%
- Percent due soon: Monitor trend
- Number overdue: Target 0
- On-time completion rate: Target >95%
- Average time in calibration: Minimize

### Escalation Process
- 30 days before due: Reminder to responsible person
- 15 days before due: Alert to supervisor
- At due date: Alert to quality manager
- Past due: Remove from service, escalate

## Related Directories

- **Certificates**: [`../CERTS/`](../CERTS/)
- **Records**: [`../RECORDS/`](../RECORDS/)
- **Setup procedures**: [`../../SETUP/`](../../SETUP/)
