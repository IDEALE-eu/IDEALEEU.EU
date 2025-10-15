#!/usr/bin/env python3
"""
Automated Reward Calculator for Finance Achievements
Real-time token allocation based on financial KPIs
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Any

class FinanceRewardCalculator:
    """Automated calculation of token rewards for financial achievements"""
    
    def __init__(self):
        self.reward_rules = self._load_reward_rules()
        self.performance_history = self._load_performance_history()
    
    def calculate_period_rewards(self, period_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate rewards for a specific period"""
        
        achievements = []
        total_rewards = 0
        
        # Check cost performance achievements
        cost_achievements = self._assess_cost_performance(period_data)
        achievements.extend(cost_achievements)
        
        # Check schedule performance achievements  
        schedule_achievements = self._assess_schedule_performance(period_data)
        achievements.extend(schedule_achievements)
        
        # Check forecasting achievements
        forecast_achievements = self._assess_forecasting_accuracy(period_data)
        achievements.extend(forecast_achievements)
        
        # Check risk management achievements
        risk_achievements = self._assess_risk_management(period_data)
        achievements.extend(risk_achievements)
        
        # Calculate total rewards
        total_rewards = sum(ach['token_reward'] for ach in achievements)
        
        return {
            'period': period_data['period'],
            'total_rewards': total_rewards,
            'achievements': achievements,
            'recommendations': self._generate_reward_recommendations(achievements)
        }
    
    def _assess_cost_performance(self, period_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Assess cost performance achievements"""
        achievements = []
        cpi = period_data.get('CPI', 1.0)
        
        # Sustained CPI performance
        if self._check_sustained_performance('CPI', cpi, 1.05, 2):
            achievements.append({
                'category': 'cost_performance',
                'achievement': 'sustained_cpi_excellence',
                'description': f'Sustained CPI > 1.05 for 2+ periods (Current: {cpi})',
                'token_reward': 100,
                'merit_multiplier': 1.5
            })
        
        # Significant cost savings
        cost_savings = period_data.get('cost_savings', 0)
        if cost_savings > 100000:
            achievement_level = min(5, cost_savings // 20000)  # Cap at 5x multiplier
            achievements.append({
                'category': 'cost_savings',
                'achievement': 'significant_cost_reduction',
                'description': f'Identified cost savings of ${cost_savings:,.0f}',
                'token_reward': 50 * achievement_level,
                'merit_multiplier': 0.05  # 5% of savings as MERIT
            })
        
        return achievements
    
    def _assess_schedule_performance(self, period_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Assess schedule performance achievements"""
        achievements = []
        spi = period_data.get('SPI', 1.0)
        
        # Sustained SPI performance
        if self._check_sustained_performance('SPI', spi, 1.03, 2):
            achievements.append({
                'category': 'schedule_performance', 
                'achievement': 'sustained_spi_excellence',
                'description': f'Sustained SPI > 1.03 for 2+ periods (Current: {spi})',
                'token_reward': 75,
                'merit_multiplier': 1.2
            })
        
        # Milestone acceleration
        acceleration = period_data.get('schedule_acceleration', 0)
        if acceleration > 10:  # 10% acceleration
            achievements.append({
                'category': 'schedule_acceleration',
                'achievement': 'significant_schedule_improvement',
                'description': f'Achieved {acceleration}% schedule acceleration',
                'token_reward': 50,
                'merit_multiplier': 0.8
            })
        
        return achievements
    
    def _assess_forecasting_accuracy(self, period_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Assess forecasting accuracy achievements"""
        achievements = []
        forecast_accuracy = period_data.get('forecast_accuracy', 0)
        
        # High forecasting accuracy
        if forecast_accuracy >= 0.98:  # 98% accuracy
            sustained_periods = self._get_sustained_forecast_accuracy(0.98)
            if sustained_periods >= 3:
                achievements.append({
                    'category': 'forecasting',
                    'achievement': 'sustained_forecast_accuracy',
                    'description': f'Sustained 98%+ forecast accuracy for {sustained_periods} periods',
                    'token_reward': 60,
                    'merit_multiplier': 1.0
                })
        
        # Risk mitigation through forecasting
        risk_mitigation = period_data.get('risk_mitigation_value', 0)
        if risk_mitigation > 50000:
            achievements.append({
                'category': 'risk_forecasting',
                'achievement': 'effective_risk_prediction',
                'description': f'Mitigated ${risk_mitigation:,.0f} in risks through accurate forecasting',
                'token_reward': 40,
                'merit_multiplier': 0.03  # 3% of mitigated value
            })
        
        return achievements
    
    def _assess_risk_management(self, period_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Assess risk management achievements"""
        achievements = []
        
        # Risk exposure reduction
        risk_reduction = period_data.get('risk_exposure_reduction', 0)
        if risk_reduction > 0.1:  # 10% reduction
            achievements.append({
                'category': 'risk_management',
                'achievement': 'effective_risk_reduction',
                'description': f'Achieved {risk_reduction:.1%} reduction in risk exposure',
                'token_reward': 30,
                'merit_multiplier': 0.5
            })
        
        return achievements
    
    def _check_sustained_performance(self, metric: str, current_value: float, 
                                  threshold: float, periods: int) -> bool:
        """Check if performance has been sustained over multiple periods"""
        # Implementation would check historical performance data
        # This is a simplified version
        return current_value >= threshold
    
    def _get_sustained_forecast_accuracy(self, threshold: float) -> int:
        """Get number of periods with sustained forecast accuracy"""
        # Implementation would analyze historical forecast data
        return 3  # Simplified implementation
    
    def _generate_reward_recommendations(self, achievements: List[Dict[str, Any]]) -> List[str]:
        """Generate recommendations for reward optimization"""
        recommendations = []
        
        if not achievements:
            recommendations.append("Focus on improving CPI/SPI metrics for token eligibility")
            return recommendations
        
        # Analyze achievement patterns
        categories = [ach['category'] for ach in achievements]
        
        if 'cost_savings' not in categories:
            recommendations.append("Implement should-cost analysis to identify savings opportunities")
        
        if 'risk_management' not in categories:
            recommendations.append("Enhance risk identification and mitigation processes")
        
        return recommendations
    
    def _load_reward_rules(self) -> Dict[str, Any]:
        """Load reward rules from configuration"""
        # This would load from a configuration file
        return {
            'cost_performance': {
                'sustained_cpi_threshold': 1.05,
                'sustained_periods': 2,
                'base_reward': 100
            },
            'schedule_performance': {
                'sustained_spi_threshold': 1.03, 
                'sustained_periods': 2,
                'base_reward': 75
            }
        }
    
    def _load_performance_history(self) -> pd.DataFrame:
        """Load historical performance data"""
        # This would load from your performance database
        return pd.DataFrame()

# Example usage
def main():
    calculator = FinanceRewardCalculator()
    
    # Example period data
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
    print("Reward Calculation Results:")
    print(f"Total Tokens: {rewards['total_rewards']}")
    print("Achievements:")
    for achievement in rewards['achievements']:
        print(f"  - {achievement['description']}: {achievement['token_reward']} tokens")

if __name__ == "__main__":
    main()
