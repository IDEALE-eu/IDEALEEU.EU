# Fleet Utilization Template (Excel)

## Overview

This Excel workbook template tracks and analyzes fleet utilization across all aircraft and spacecraft, supporting planning, performance monitoring, and optimization activities.

## Workbook Structure

### Sheet 1: Fleet Inventory
- Aircraft/Spacecraft registration/serial numbers
- Type and configuration
- Age and lifecycle status
- Operational status (active, maintenance, storage)
- Base location

### Sheet 2: Daily Utilization
- Date
- Tail number
- Flight hours / mission hours
- Cycles / missions
- Block time
- Ground time
- Delays and reasons
- Aircraft on ground (AOG) status

### Sheet 3: Monthly Summary
- Summary by tail number
- Summary by fleet type
- Utilization rates vs. targets
- Availability percentages
- Year-to-date trends

### Sheet 4: Performance Metrics
- Utilization rate (hours per day)
- Availability percentage
- On-time performance
- Technical delay rate
- Cost per flight hour

### Sheet 5: Forecasts and Targets
- Monthly utilization targets
- Capacity forecasts
- Resource requirements
- Gap analysis

### Sheet 6: Charts and Dashboards
- Utilization trend charts
- Fleet availability gauges
- Performance scorecards
- Exception reports

## Data Entry Guidelines

- Enter daily operational data in Sheet 2
- Update fleet inventory changes in Sheet 1
- Review calculated summaries in Sheet 3
- Analyze performance metrics in Sheet 4
- Charts auto-update based on data

## Formulas and Calculations

- **Utilization Rate** = Total Hours / (Fleet Size × Days × Target Hours per Day)
- **Availability** = Available Hours / Total Possible Hours
- **On-Time Performance** = On-Time Departures / Total Departures × 100%

## Export and Integration

- Monthly data exported to operational data hub
- Performance metrics feed reporting dashboards
- Integration with crew scheduling and maintenance planning systems

## Template Notes

**Note**: The actual Excel file (FLEET_UTILISATION_TEMPLATE.xlsx) should be created with:
- Pre-formatted sheets with headers
- Data validation and dropdown lists
- Conditional formatting for KPIs
- Charts and pivot tables
- Protection of formula cells
- Instructions tab

This markdown file serves as documentation for the Excel template structure.

## References

- Utilization policy: **01-STRATEGY/UTILISATION_POLICY.md**
- Performance metrics: **05-OPERATIONAL_PERFORMANCE/AVAILABILITY_METRICS.md**
- Reporting: **10-REPORTING/MONTHLY_FLEET_REVIEW.md**
