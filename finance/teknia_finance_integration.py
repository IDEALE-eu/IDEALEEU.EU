#!/usr/bin/env python3
"""
Teknia Finance Integration v1.0
Bridges program finance (EVM, forecasting, cost models) with Teknia Token rewards
"""

import json
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from decimal import Decimal
import hashlib

class FinanceTokenIntegration:
    """Integrates program finance metrics with Teknia Token reward system"""
    
    def __init__(self, finance_root: Path = Path("10-BUSINESS/FINANCE")):
        self.finance_root = finance_root
        self.token_config = self._load_token_config()
        self.reward_log = finance_root / "06-REPORTING/rewardIT_LOG.csv"
        
    def calculate_financial_impact_rewards(self, period_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate token rewards based on financial performance metrics"""
        
        # Extract key financial metrics
        metrics = self._extract_financial_metrics(period_data)
        
        # Calculate normalized impact scores
        impact_scores = {
            "cost_performance": self._normalize_cpi_impact(metrics.get('cpi', 1.0)),
            "schedule_performance": self._normalize_spi_impact(metrics.get('spi', 1.0)),
            "forecast_accuracy": self._calculate_forecast_accuracy(metrics),
            "risk_reduction": self._assess_risk_mitigation(metrics),
            "process_innovation": self._evaluate_process_improvements(metrics)
        }
        
        # Calculate total reward units
        total_impact = sum(impact_scores.values())
        maturity_factor = self._calculate_maturity_factor(metrics)
        evidence_robustness = self._assess_evidence_quality(metrics)
        
        reward_units = self._calculate_reward_units(
            total_impact, maturity_factor, evidence_robustness
        )
        
        return {
            "period": period_data.get('period'),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "impact_scores": impact_scores,
            "reward_units": reward_units,
            "merit_allocation": self._calculate_merit_allocation(reward_units),
            "token_metadata": self._prepare_token_metadata(metrics, impact_scores)
        }
    
    def mint_achievement_token(self, achievement_data: Dict[str, Any]) -> str:
        """Mint Teknia Token for financial achievement"""
        
        token_id = f"FINANCE-{int(datetime.utcnow().timestamp())}"
        
        token_metadata = {
            "token_id": token_id,
            "token_type": "financial_achievement",
            "utcs_anchor": achievement_data.get('utcs_anchor', 'utcs://BUSINESS/FINANCE'),
            "achievement_date": datetime.utcnow().isoformat() + "Z",
            "financial_impact": {
                "validated_savings": achievement_data.get('validated_savings'),
                "sustained_periods": achievement_data.get('sustained_periods', 0),
                "cpi_improvement": achievement_data.get('cpi_delta', 0),
                "spi_improvement": achievement_data.get('spi_delta', 0)
            },
            "evidence": {
                "verification_status": achievement_data.get('verification_status', 'pending'),
                "board_approval": achievement_data.get('board_approval', False),
                "supporting_docs": achievement_data.get('supporting_docs', [])
            },
            "rewards": {
                "merit_allocated": achievement_data.get('merit_allocation', 0),
                "token_units": achievement_data.get('reward_units', 0)
            }
        }
        
        # Log the achievement
        self._log_achievement(token_id, token_metadata)
        
        # Mint token in Teknia system
        self._mint_teknia_token(token_id, token_metadata)
        
        return token_id
    
    def integrate_evm_with_tokens(self, evm_data: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate EVM metrics with token reward system"""
        
        performance_metrics = {
            "spi": evm_data.get('SPI', 0),
            "cpi": evm_data.get('CPI', 0),
            "tCPI": evm_data.get('TCPI', 0),
            "vac": evm_data.get('VAC', 0),
            "eac": evm_data.get('EAC', 0)
        }
        
        # Calculate performance-based rewards
        rewards = self.calculate_financial_impact_rewards({
            'period': evm_data.get('period'),
            'metrics': performance_metrics
        })
        
        return {
            "evm_metrics": performance_metrics,
            "token_rewards": rewards,
            "recommendations": self._generate_financial_recommendations(performance_metrics)
        }
    
    def _extract_financial_metrics(self, period_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract financial metrics from period data"""
        metrics = period_data.get('metrics', {})
        if not metrics and 'cpi' in period_data:
            # Handle case where metrics are at top level
            metrics = period_data
        return metrics
    
    def _calculate_reward_units(self, normalized_impact: float, 
                              maturity: float, evidence_robustness: float) -> float:
        """Calculate reward units based on impact, maturity, and evidence"""
        
        base_units = normalized_impact * 100  # Base scaling
        
        # Apply maturity multiplier (0.5 to 2.0)
        maturity_multiplier = 0.5 + (maturity * 1.5)
        
        # Apply evidence quality multiplier (0.8 to 1.2)
        evidence_multiplier = 0.8 + (evidence_robustness * 0.4)
        
        return base_units * maturity_multiplier * evidence_multiplier
    
    def _normalize_cpi_impact(self, cpi: float) -> float:
        """Normalize CPI impact for reward calculation"""
        if cpi >= 1.05:
            return 1.0  # Excellent performance
        elif cpi >= 1.02:
            return 0.7  # Good performance
        elif cpi >= 1.00:
            return 0.4  # On target
        elif cpi >= 0.98:
            return 0.2  # Slightly below
        else:
            return 0.0  # Poor performance
    
    def _normalize_spi_impact(self, spi: float) -> float:
        """Normalize SPI impact for reward calculation"""
        if spi >= 1.05:
            return 1.0
        elif spi >= 1.02:
            return 0.7
        elif spi >= 1.00:
            return 0.4
        elif spi >= 0.98:
            return 0.2
        else:
            return 0.0
    
    def _calculate_forecast_accuracy(self, metrics: Dict[str, Any]) -> float:
        """Calculate forecast accuracy impact"""
        actual = metrics.get('actual_cost', 0)
        forecast = metrics.get('forecast_cost', 0)
        
        if actual == 0 or forecast == 0:
            return 0.0
        
        accuracy = 1 - (abs(actual - forecast) / forecast)
        return max(0.0, min(1.0, accuracy))
    
    def _assess_risk_mitigation(self, metrics: Dict[str, Any]) -> float:
        """Assess risk mitigation effectiveness"""
        initial_risk = metrics.get('initial_risk_exposure', 0)
        current_risk = metrics.get('current_risk_exposure', 0)
        
        if initial_risk == 0:
            return 0.0
        
        mitigation_effectiveness = (initial_risk - current_risk) / initial_risk
        return max(0.0, min(1.0, mitigation_effectiveness))
    
    def _evaluate_process_improvements(self, metrics: Dict[str, Any]) -> float:
        """Evaluate process improvement impacts"""
        improvements = metrics.get('process_improvements', [])
        total_impact = sum(imp.get('impact_score', 0) for imp in improvements)
        return min(1.0, total_impact / 10.0)  # Normalize to 0-1 scale
    
    def _calculate_maturity_factor(self, metrics: Dict[str, Any]) -> float:
        """Calculate maturity factor based on data quality and process maturity"""
        data_quality = metrics.get('data_quality_score', 0.5)
        process_maturity = metrics.get('process_maturity_score', 0.5)
        return (data_quality + process_maturity) / 2.0
    
    def _assess_evidence_quality(self, metrics: Dict[str, Any]) -> float:
        """Assess quality of supporting evidence"""
        evidence_indicators = [
            metrics.get('audit_trail_completeness', 0),
            metrics.get('documentation_quality', 0),
            metrics.get('stakeholder_validation', 0),
            metrics.get('independent_verification', 0)
        ]
        return sum(evidence_indicators) / len(evidence_indicators)
    
    def _calculate_merit_allocation(self, reward_units: float) -> Dict[str, float]:
        """Calculate $MERIT allocation across contributors"""
        # This would integrate with your actual merit distribution system
        return {
            "innovation_treasury": reward_units * 0.7,
            "team_allocation": reward_units * 0.2,
            "individual_contributors": reward_units * 0.1
        }
    
    def _prepare_token_metadata(self, metrics: Dict[str, Any], 
                              impact_scores: Dict[str, float]) -> Dict[str, Any]:
        """Prepare metadata for token minting"""
        return {
            "impact_breakdown": impact_scores,
            "financial_metrics": {
                "cpi": metrics.get('cpi'),
                "spi": metrics.get('spi'),
                "forecast_accuracy": metrics.get('forecast_accuracy'),
                "risk_exposure": metrics.get('risk_exposure')
            },
            "verification_data": {
                "period": metrics.get('period'),
                "reviewer": metrics.get('reviewer', 'finance_board'),
                "approval_date": datetime.utcnow().isoformat() + "Z"
            }
        }
    
    def _log_achievement(self, token_id: str, metadata: Dict[str, Any]):
        """Log achievement to rewardIT_LOG.csv"""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "token_id": token_id,
            "achievement_type": metadata.get('token_type'),
            "impact_score": sum(metadata.get('financial_impact', {}).values()),
            "merit_allocated": metadata['rewards']['merit_allocated'],
            "utcs_anchor": metadata.get('utcs_anchor'),
            "verification_status": metadata['evidence']['verification_status']
        }
        
        # Append to CSV log
        df = pd.DataFrame([log_entry])
        if self.reward_log.exists():
            df.to_csv(self.reward_log, mode='a', header=False, index=False)
        else:
            df.to_csv(self.reward_log, index=False)
    
    def _mint_teknia_token(self, token_id: str, metadata: Dict[str, Any]):
        """Mint Teknia Token using the token system"""
        # Integration with Teknia Token minting system
        try:
            # This would call your actual token minting process
            print(f"Minting Teknia Token: {token_id}")
            print(f"Metadata: {json.dumps(metadata, indent=2)}")
            
            # In production, this would integrate with your blockchain/token system
            # Example: teknia_system.mint_token(token_id, metadata)
            
        except Exception as e:
            print(f"Token minting failed: {e}")
            # Log error but don't fail the entire process
    
    def _generate_financial_recommendations(self, metrics: Dict[str, Any]) -> List[str]:
        """Generate financial recommendations based on performance"""
        recommendations = []
        
        if metrics.get('cpi', 1.0) < 1.0:
            recommendations.append("Review cost performance and implement corrective actions")
        
        if metrics.get('spi', 1.0) < 1.0:
            recommendations.append("Address schedule delays and optimize resource allocation")
        
        if metrics.get('tCPI', 1.0) > 1.1:
            recommendations.append("Evaluate feasibility of current performance measurement baseline")
        
        return recommendations
    
    def _load_token_config(self) -> Dict[str, Any]:
        """Load token configuration"""
        config_path = Path("finance/teknia.tokenomics.json")
        if config_path.exists():
            with config_path.open() as f:
                return json.load(f)
        return {}

# Example usage
def main():
    """Example integration with program finance data"""
    integration = FinanceTokenIntegration()
    
    # Example EVM data
    evm_data = {
        'period': '2024-Q1',
        'SPI': 1.03,
        'CPI': 1.02,
        'TCPI': 1.01,
        'VAC': 50000,
        'EAC': 950000
    }
    
    # Integrate EVM with token rewards
    result = integration.integrate_evm_with_tokens(evm_data)
    print(json.dumps(result, indent=2))
    
    # Mint achievement token for sustained performance
    if result['token_rewards']['reward_units'] > 50:
        achievement_data = {
            'utcs_anchor': 'utcs://BUSINESS/FINANCE/EVM-PERFORMANCE',
            'validated_savings': 50000,
            'sustained_periods': 2,
            'cpi_delta': 0.02,
            'spi_delta': 0.03,
            'verification_status': 'verified',
            'board_approval': True,
            'supporting_docs': ['EVM_Report_2024_Q1.pdf', 'Finance_Board_Approval.pdf']
        }
        
        token_id = integration.mint_achievement_token(achievement_data)
        print(f"Minted achievement token: {token_id}")

if __name__ == "__main__":
    main()
