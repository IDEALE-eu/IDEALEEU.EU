# Finance Reporting Directory

This directory contains financial reporting outputs including token reward logs.

## Contents

### rewardIT_LOG.csv
Achievement and token reward log. Tracks all financial achievements that result in token rewards.

**Format**: CSV with the following columns:
- `timestamp` - Achievement timestamp (ISO 8601 format)
- `token_id` - Unique token identifier
- `achievement_type` - Type of achievement (e.g., cost_performance_excellence)
- `impact_score` - Numerical impact score
- `merit_allocated` - Amount of $MERIT allocated
- `utcs_anchor` - UTCS thread anchor reference
- `verification_status` - Verification status (pending, verified, rejected)

### Usage

The reward log is automatically updated by the finance token integration system when achievements are recorded and tokens are minted.

To view the log:
```bash
cat 06-REPORTING/rewardIT_LOG.csv
```

To analyze rewards:
```python
import pandas as pd

df = pd.read_csv('06-REPORTING/rewardIT_LOG.csv')
print(df.head())
print(f"Total tokens issued: {df['impact_score'].sum()}")
```

### Notes

- Log file is created automatically on first achievement
- All entries are immutable (append-only)
- Regular backups recommended
- Audit trail compliant
