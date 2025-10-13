# Finance Package - Teknia Token Integration

This package provides the integration layer between Program Finance Office (PFO) financial metrics and the Teknia Token reward system.

## Overview

The Finance-Token Integration system automatically calculates and awards tokens based on financial performance achievements including:

- **Cost Performance**: CPI improvements and cost savings
- **Schedule Performance**: SPI improvements and milestone acceleration  
- **Forecasting Accuracy**: EAC accuracy and risk mitigation
- **Process Innovation**: Process improvements and efficiency gains

## Quick Start

### Installation

Ensure required dependencies are installed:

```bash
pip install pandas numpy
```

### Basic Usage

```python
from finance import FinanceTokenIntegration

# Initialize the integration
integration = FinanceTokenIntegration()

# Example: EVM data integration
evm_data = {
    'period': '2024-Q1',
    'SPI': 1.03,
    'CPI': 1.02,
    'TCPI': 1.01,
    'VAC': 50000,
    'EAC': 950000
}

# Calculate rewards
result = integration.integrate_evm_with_tokens(evm_data)
print(f"Reward Units: {result['token_rewards']['reward_units']}")
```

### Running Examples

See comprehensive examples:

```bash
python3 finance/examples_usage.py
```

## Module Structure

```
finance/
├── __init__.py                      # Package initialization
├── teknia_finance_integration.py   # Main integration module
├── teknia.tokenomics.json          # Token economics configuration
├── examples_usage.py               # Usage examples
└── README.md                        # This file
```

## Key Classes

### FinanceTokenIntegration

Main class for integrating financial metrics with token rewards.

**Methods:**
- `calculate_financial_impact_rewards(period_data)` - Calculate token rewards from period performance
- `mint_achievement_token(achievement_data)` - Mint a token for a financial achievement
- `integrate_evm_with_tokens(evm_data)` - Integrate EVM metrics with token system

## Configuration

Token economics are configured in `teknia.tokenomics.json`:

```json
{
  "teknia_tokenomics": {
    "achievement_thresholds": {
      "cost_performance": {
        "excellent": 1.05,
        "good": 1.02,
        "target": 1.00
      }
    },
    "reward_multipliers": {
      "maturity_factor": {"min": 0.5, "max": 2.0},
      "evidence_quality": {"min": 0.8, "max": 1.2}
    }
  }
}
```

## Achievement Categories

### Cost Performance Excellence
- **Threshold**: CPI ≥ 1.05 for 2+ periods
- **Reward**: 100 tokens
- **Merit**: 1.5x multiplier

### Schedule Performance Excellence  
- **Threshold**: SPI ≥ 1.03 for 2+ periods
- **Reward**: 75 tokens
- **Merit**: 1.2x multiplier

### Forecasting Accuracy
- **Threshold**: 98%+ accuracy for 3+ periods
- **Reward**: 60 tokens
- **Merit**: 1.0x multiplier

### Cost Savings
- **Threshold**: Validated savings > $100K
- **Reward**: 50 tokens + 5% of savings as $MERIT
- **Scaling**: Up to 5x multiplier for larger savings

## Integration with Business Finance

This package integrates with:
- `10-BUSINESS/FINANCE/` - Main finance domain
- `10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION/` - Automated calculators
- `10-BUSINESS/FINANCE/06-REPORTING/` - Reward logs and reports

## Token Metadata Structure

Minted tokens include comprehensive metadata:

```json
{
  "token_id": "FINANCE-{timestamp}",
  "token_type": "financial_achievement",
  "utcs_anchor": "utcs://BUSINESS/FINANCE/...",
  "financial_impact": {
    "validated_savings": 150000,
    "sustained_periods": 3,
    "cpi_improvement": 0.07,
    "spi_improvement": 0.04
  },
  "evidence": {
    "verification_status": "verified",
    "board_approval": true,
    "supporting_docs": [...]
  },
  "rewards": {
    "merit_allocated": 7500,
    "token_units": 100
  }
}
```

## Verification & Governance

All token rewards are subject to:
- ✅ Automated validation checks
- ✅ Finance board review (for rewards >50 tokens)
- ✅ Evidence documentation requirements
- ✅ Complete audit trail
- ✅ Anti-gaming mechanisms

## Logging

Achievement tokens are logged to:
```
10-BUSINESS/FINANCE/06-REPORTING/rewardIT_LOG.csv
```

Log format:
- timestamp (ISO 8601)
- token_id
- achievement_type
- impact_score
- merit_allocated
- utcs_anchor
- verification_status

## Testing

To test the integration:

```python
# Test basic functionality
python3 -c "from finance import FinanceTokenIntegration; i = FinanceTokenIntegration(); print('✓ OK')"

# Run comprehensive examples
python3 finance/examples_usage.py
```

## Related Documentation

- **Main Finance Documentation**: `10-BUSINESS/FINANCE/README.md`
- **Token Configuration**: `10-BUSINESS/FINANCE/finance_token_config.json`
- **Automated Calculator**: `10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION/automated_reward_calculator.py`

## Support

For questions or issues:
- **Technical Implementation**: Finance Automation Team
- **Token Economics**: PFO Token Strategy Team
- **Validation & Approval**: Finance Review Board

## Version

**Current Version**: 1.0.0  
**Last Updated**: 2025-10-13  
**Status**: Active 🟢

---

**License**: Internal Use Only  
**Classification**: Program Finance Integration
