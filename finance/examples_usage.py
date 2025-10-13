#!/usr/bin/env python3
"""
Example Usage of Finance-Token Integration System

This script demonstrates the complete workflow of the Teknia Finance Integration
system, from EVM performance tracking to token reward minting.
"""

import sys
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from finance import FinanceTokenIntegration

def example_1_basic_evm_integration():
    """Example 1: Basic EVM integration with token reward calculation"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic EVM Integration")
    print("="*70)
    
    integration = FinanceTokenIntegration()
    
    # Simulate quarterly EVM data
    evm_data = {
        'period': '2024-Q1',
        'SPI': 1.03,  # Schedule Performance Index
        'CPI': 1.02,  # Cost Performance Index
        'TCPI': 1.01,  # To-Complete Performance Index
        'VAC': 50000,  # Variance at Completion
        'EAC': 950000  # Estimate at Completion
    }
    
    print(f"\nInput EVM Data for {evm_data['period']}:")
    print(f"  SPI: {evm_data['SPI']}")
    print(f"  CPI: {evm_data['CPI']}")
    print(f"  TCPI: {evm_data['TCPI']}")
    
    # Calculate rewards
    result = integration.integrate_evm_with_tokens(evm_data)
    
    print(f"\nToken Rewards Calculated:")
    print(f"  Total Reward Units: {result['token_rewards']['reward_units']:.2f}")
    print(f"\n  Impact Score Breakdown:")
    for category, score in result['token_rewards']['impact_scores'].items():
        print(f"    - {category}: {score:.2f}")
    
    print(f"\n  Merit Allocation:")
    for category, amount in result['token_rewards']['merit_allocation'].items():
        print(f"    - {category}: {amount:.2f}")
    
    if result['recommendations']:
        print(f"\n  Recommendations:")
        for rec in result['recommendations']:
            print(f"    - {rec}")

def example_2_high_performance_achievement():
    """Example 2: High performance achievement with token minting"""
    print("\n" + "="*70)
    print("EXAMPLE 2: High Performance Achievement - Token Minting")
    print("="*70)
    
    integration = FinanceTokenIntegration()
    
    # Simulate sustained high performance
    achievement_data = {
        'utcs_anchor': 'utcs://BUSINESS/FINANCE/EVM-PERFORMANCE',
        'validated_savings': 150000,
        'sustained_periods': 3,
        'cpi_delta': 0.07,  # 7% improvement in CPI
        'spi_delta': 0.04,  # 4% improvement in SPI
        'verification_status': 'verified',
        'board_approval': True,
        'supporting_docs': [
            'EVM_Report_2024_Q1.pdf',
            'Finance_Board_Approval_2024_Q1.pdf',
            'Cost_Savings_Analysis.xlsx'
        ],
        'reward_units': 250,
        'merit_allocation': 12500
    }
    
    print("\nAchievement Details:")
    print(f"  Validated Savings: ${achievement_data['validated_savings']:,}")
    print(f"  Sustained Periods: {achievement_data['sustained_periods']}")
    print(f"  CPI Improvement: {achievement_data['cpi_delta']:.1%}")
    print(f"  SPI Improvement: {achievement_data['spi_delta']:.1%}")
    print(f"  Board Approval: {'Yes' if achievement_data['board_approval'] else 'No'}")
    
    # Mint achievement token
    token_id = integration.mint_achievement_token(achievement_data)
    
    print(f"\n✓ Achievement Token Minted: {token_id}")
    print(f"  Reward Units: {achievement_data['reward_units']}")
    print(f"  $MERIT Allocated: ${achievement_data['merit_allocation']:,}")
    print(f"  UTCS Anchor: {achievement_data['utcs_anchor']}")

def example_3_cost_savings_identification():
    """Example 3: Cost savings identification and reward calculation"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Cost Savings Identification")
    print("="*70)
    
    integration = FinanceTokenIntegration()
    
    # Simulate cost analysis with identified savings
    period_data = {
        'period': '2024-Q2',
        'metrics': {
            'cpi': 1.08,
            'spi': 1.05,
            'actual_cost': 475000,
            'forecast_cost': 480000,
            'initial_risk_exposure': 200000,
            'current_risk_exposure': 150000,
            'process_improvements': [
                {'name': 'Automated testing', 'impact_score': 3.0},
                {'name': 'Parallel processing', 'impact_score': 2.5}
            ]
        }
    }
    
    print(f"\nPeriod Analysis for {period_data['period']}:")
    print(f"  CPI: {period_data['metrics']['cpi']}")
    print(f"  SPI: {period_data['metrics']['spi']}")
    print(f"  Forecast Accuracy: {(1 - abs(period_data['metrics']['actual_cost'] - period_data['metrics']['forecast_cost'])/period_data['metrics']['forecast_cost']):.1%}")
    print(f"  Risk Reduction: {((period_data['metrics']['initial_risk_exposure'] - period_data['metrics']['current_risk_exposure'])/period_data['metrics']['initial_risk_exposure']):.1%}")
    
    # Calculate rewards
    rewards = integration.calculate_financial_impact_rewards(period_data)
    
    print(f"\nReward Calculation Results:")
    print(f"  Total Reward Units: {rewards['reward_units']:.2f}")
    print(f"\n  Detailed Impact Scores:")
    for category, score in rewards['impact_scores'].items():
        print(f"    - {category}: {score:.2f}")

def example_4_automated_calculator():
    """Example 4: Using the automated reward calculator"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Automated Reward Calculator")
    print("="*70)
    
    # Note: This imports from the tools directory
    tools_path = Path(__file__).parent.parent / '10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION'
    sys.path.insert(0, str(tools_path))
    
    try:
        from automated_reward_calculator import FinanceRewardCalculator
    except ImportError:
        print("\n⚠ Warning: Could not import FinanceRewardCalculator")
        print("  Please ensure 10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION is accessible")
        return
    
    calculator = FinanceRewardCalculator()
    
    # Comprehensive period data
    period_data = {
        'period': '2024-Q3',
        'CPI': 1.07,
        'SPI': 1.04,
        'cost_savings': 175000,
        'forecast_accuracy': 0.99,
        'risk_mitigation_value': 85000,
        'risk_exposure_reduction': 0.18,
        'schedule_acceleration': 12
    }
    
    print(f"\nComprehensive Performance Analysis for {period_data['period']}:")
    print(f"  CPI: {period_data['CPI']}")
    print(f"  SPI: {period_data['SPI']}")
    print(f"  Cost Savings: ${period_data['cost_savings']:,}")
    print(f"  Forecast Accuracy: {period_data['forecast_accuracy']:.1%}")
    print(f"  Risk Mitigation Value: ${period_data['risk_mitigation_value']:,}")
    
    # Calculate period rewards
    rewards = calculator.calculate_period_rewards(period_data)
    
    print(f"\n✓ Total Rewards Earned: {rewards['total_rewards']} tokens")
    print(f"\nAchievements Unlocked ({len(rewards['achievements'])}):")
    for i, achievement in enumerate(rewards['achievements'], 1):
        print(f"  {i}. {achievement['achievement']}")
        print(f"     Category: {achievement['category']}")
        print(f"     Reward: {achievement['token_reward']} tokens")
        print(f"     Merit Multiplier: {achievement['merit_multiplier']:.2f}x")
    
    if rewards['recommendations']:
        print(f"\nRecommendations for Further Improvement:")
        for rec in rewards['recommendations']:
            print(f"  • {rec}")

def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("TEKNIA FINANCE-TOKEN INTEGRATION")
    print("Example Usage Demonstration")
    print("="*70)
    
    try:
        example_1_basic_evm_integration()
        example_2_high_performance_achievement()
        example_3_cost_savings_identification()
        example_4_automated_calculator()
        
        print("\n" + "="*70)
        print("✓ All Examples Completed Successfully")
        print("="*70)
        print("\nFor more information:")
        print("  - Documentation: 10-BUSINESS/FINANCE/README.md")
        print("  - Configuration: finance/teknia.tokenomics.json")
        print("  - Reward Log: 10-BUSINESS/FINANCE/06-REPORTING/rewardIT_LOG.csv")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error during example execution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
