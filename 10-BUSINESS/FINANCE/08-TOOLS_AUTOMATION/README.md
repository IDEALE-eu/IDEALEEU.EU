# Finance Tools & Automation

This directory contains automated tools for financial reward calculation and token integration.

## Contents

### automated_reward_calculator.py

Automated calculation of token rewards for financial achievements based on performance metrics.

**Key Features:**
- Multi-category achievement assessment
- Sustained performance tracking
- Tiered reward structures
- Automatic recommendation generation

**Usage:**

```python
from automated_reward_calculator import FinanceRewardCalculator

calculator = FinanceRewardCalculator()

period_data = {
    'period': '2024-Q1',
    'CPI': 1.07,
    'SPI': 1.04,
    'cost_savings': 150000,
    'forecast_accuracy': 0.99,
    'risk_mitigation_value': 75000,
    'risk_exposure_reduction': 0.15
}

rewards = calculator.calculate_period_rewards(period_data)
print(f"Total Rewards: {rewards['total_rewards']} tokens")
```

## Achievement Assessment Categories

### Cost Performance
- Sustained CPI excellence (≥1.05 for 2+ periods): 100 tokens
- Significant cost reduction (≥$100K): 50-250 tokens (tiered)

### Schedule Performance  
- Sustained SPI excellence (≥1.03 for 2+ periods): 75 tokens
- Schedule acceleration (≥10%): 50 tokens

### Forecasting Accuracy
- Sustained accuracy (≥98% for 3+ periods): 60 tokens
- Effective risk prediction (≥$50K mitigation): 40 tokens

### Risk Management
- Risk exposure reduction (≥10%): 30 tokens

## Configuration

Reward rules are configured in `../finance_token_config.json`:

```json
{
  "reward_framework": {
    "cost_performance": {
      "sustained_cpi_excellence": {
        "threshold": 1.05,
        "periods_required": 2,
        "token_reward": 100
      }
    }
  }
}
```

## Output Format

The calculator returns:

```python
{
    'period': '2024-Q1',
    'total_rewards': 555,
    'achievements': [
        {
            'category': 'cost_performance',
            'achievement': 'sustained_cpi_excellence',
            'description': 'Sustained CPI > 1.05 for 2+ periods (Current: 1.07)',
            'token_reward': 100,
            'merit_multiplier': 1.5
        },
        # ... more achievements
    ],
    'recommendations': [
        'Focus on improving CPI/SPI metrics for token eligibility'
    ]
}
```

## Integration Points

This module integrates with:
- Finance token configuration (`../finance_token_config.json`)
- Performance history database (future integration)
- Reward logging system (`../06-REPORTING/rewardIT_LOG.csv`)

## Testing

Test the calculator:

```bash
cd /home/runner/work/IDEALEEU.EU/IDEALEEU.EU/10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION
python3 automated_reward_calculator.py
```

## Future Enhancements

Planned features:
- [ ] Real-time performance history tracking
- [ ] Machine learning-based trend prediction
- [ ] Cross-program benchmarking
- [ ] Integration with digital twin systems
- [ ] Advanced anti-gaming mechanisms

## Related Documentation

- **Main Integration**: `/finance/teknia_finance_integration.py`
- **Finance Overview**: `../README.md`
- **Token Configuration**: `../finance_token_config.json`

**Version**: 1.0.0  
**Status**: Active 🟢
