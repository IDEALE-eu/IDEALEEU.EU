#!/usr/bin/env python3
"""
A360 Fee Calculator
Calculates fees for all A360 platform services with TT token discounts
"""

from typing import Dict, Optional
from decimal import Decimal
from enum import Enum


class ServiceType(Enum):
    """Types of services in A360 platform"""
    TRADING_MAKER = "trading_maker"
    TRADING_TAKER = "trading_taker"
    LEASE_ORIGINATION = "lease_origination"
    DPP_MINT = "dpp_mint"
    DPP_ATTESTATION = "dpp_attestation"
    REPAIR_ESCROW = "repair_escrow"


class FeeCalculator:
    """Calculate fees for A360 platform services"""
    
    # Base fee rates (before discounts)
    BASE_FEES = {
        ServiceType.TRADING_MAKER: Decimal("0.001"),  # 0.10%
        ServiceType.TRADING_TAKER: Decimal("0.003"),  # 0.30%
        ServiceType.LEASE_ORIGINATION: Decimal("0.005"),  # 0.5% (min)
        ServiceType.REPAIR_ESCROW: Decimal("0.015"),  # 1.5%
    }
    
    # Fixed fees
    DPP_MINT_EUR = Decimal("0.10")
    DPP_MINT_TT = Decimal("0.05")
    DPP_ATTESTATION_TT = Decimal("0.10")
    REPAIR_ESCROW_CAP_EUR = Decimal("500.00")
    
    # Discount thresholds
    MAKER_DISCOUNT_THRESHOLD_TT = 10000  # Tokens required for maker discount
    TAKER_DISCOUNT_THRESHOLD_TT = 5000   # Tokens required for taker discount
    
    # Discount rates
    MAKER_DISCOUNT = Decimal("0.50")  # 50% discount
    TAKER_DISCOUNT = Decimal("0.20")  # 20% discount
    
    def __init__(self, tt_balance: float = 0, tt_staked: float = 0):
        """
        Initialize fee calculator
        
        Args:
            tt_balance: TT tokens held (not staked)
            tt_staked: TT tokens staked
        """
        self.tt_balance = Decimal(str(tt_balance))
        self.tt_staked = Decimal(str(tt_staked))
        self.total_tt = self.tt_balance + self.tt_staked
    
    def calculate_trading_fee(
        self,
        trade_value_eur: float,
        is_maker: bool = False
    ) -> Dict[str, Decimal]:
        """
        Calculate trading fees
        
        Args:
            trade_value_eur: Trade value in EUR
            is_maker: True if maker, False if taker
            
        Returns:
            Dictionary with fee details
        """
        value = Decimal(str(trade_value_eur))
        service_type = ServiceType.TRADING_MAKER if is_maker else ServiceType.TRADING_TAKER
        base_rate = self.BASE_FEES[service_type]
        
        # Determine discount
        discount = Decimal("0")
        if is_maker and self.tt_staked >= self.MAKER_DISCOUNT_THRESHOLD_TT:
            discount = self.MAKER_DISCOUNT
        elif not is_maker and self.total_tt >= self.TAKER_DISCOUNT_THRESHOLD_TT:
            discount = self.TAKER_DISCOUNT
        
        # Calculate fees
        base_fee = value * base_rate
        discount_amount = base_fee * discount
        final_fee = base_fee - discount_amount
        
        return {
            "service": service_type.value,
            "trade_value_eur": value,
            "base_rate_pct": base_rate * 100,
            "base_fee_eur": base_fee,
            "discount_pct": discount * 100,
            "discount_amount_eur": discount_amount,
            "final_fee_eur": final_fee,
            "tt_balance": self.tt_balance,
            "tt_staked": self.tt_staked,
            "discount_qualified": discount > 0
        }
    
    def calculate_lease_origination_fee(
        self,
        lease_value_eur: float,
        lease_term_months: int
    ) -> Dict[str, Decimal]:
        """
        Calculate lease origination fee
        
        Args:
            lease_value_eur: Total lease value in EUR
            lease_term_months: Lease term in months
            
        Returns:
            Dictionary with fee details
        """
        value = Decimal(str(lease_value_eur))
        
        # Fee rate scales with term: 0.5% to 1.0%
        # 0.5% for 3-6 months, 1.0% for 12+ months
        if lease_term_months <= 6:
            rate = Decimal("0.005")  # 0.5%
        elif lease_term_months >= 12:
            rate = Decimal("0.010")  # 1.0%
        else:
            # Linear interpolation between 6 and 12 months
            rate = Decimal("0.005") + (Decimal("0.005") * (lease_term_months - 6) / 6)
        
        fee = value * rate
        
        return {
            "service": ServiceType.LEASE_ORIGINATION.value,
            "lease_value_eur": value,
            "lease_term_months": lease_term_months,
            "fee_rate_pct": rate * 100,
            "origination_fee_eur": fee
        }
    
    def calculate_dpp_mint_fee(self) -> Dict[str, Decimal]:
        """
        Calculate DPP minting fee
        
        Returns:
            Dictionary with fee details
        """
        return {
            "service": ServiceType.DPP_MINT.value,
            "fee_eur": self.DPP_MINT_EUR,
            "fee_tt": self.DPP_MINT_TT,
            "total_eur_equivalent": self.DPP_MINT_EUR + (self.DPP_MINT_TT * Decimal("1.0"))
        }
    
    def calculate_dpp_attestation_fee(self) -> Dict[str, Decimal]:
        """
        Calculate DPP attestation fee
        
        Returns:
            Dictionary with fee details
        """
        return {
            "service": ServiceType.DPP_ATTESTATION.value,
            "fee_tt": self.DPP_ATTESTATION_TT
        }
    
    def calculate_repair_escrow_fee(
        self,
        repair_value_eur: float
    ) -> Dict[str, Decimal]:
        """
        Calculate repair escrow fee
        
        Args:
            repair_value_eur: Repair quote value in EUR
            
        Returns:
            Dictionary with fee details
        """
        value = Decimal(str(repair_value_eur))
        rate = self.BASE_FEES[ServiceType.REPAIR_ESCROW]
        
        # Calculate fee with cap
        calculated_fee = value * rate
        capped_fee = min(calculated_fee, self.REPAIR_ESCROW_CAP_EUR)
        
        return {
            "service": ServiceType.REPAIR_ESCROW.value,
            "repair_value_eur": value,
            "fee_rate_pct": rate * 100,
            "calculated_fee_eur": calculated_fee,
            "cap_eur": self.REPAIR_ESCROW_CAP_EUR,
            "final_fee_eur": capped_fee,
            "capped": calculated_fee > self.REPAIR_ESCROW_CAP_EUR
        }
    
    def calculate_all_fees(
        self,
        trade_value_eur: float = 0,
        is_maker: bool = False,
        lease_value_eur: float = 0,
        lease_term_months: int = 0,
        repair_value_eur: float = 0,
        dpp_mints: int = 0,
        dpp_attestations: int = 0
    ) -> Dict[str, any]:
        """
        Calculate all fees for a transaction bundle
        
        Returns:
            Summary of all fees
        """
        results = {
            "tt_balance": self.tt_balance,
            "tt_staked": self.tt_staked,
            "total_tt": self.total_tt,
            "fees": []
        }
        
        total_eur = Decimal("0")
        total_tt = Decimal("0")
        
        if trade_value_eur > 0:
            fee = self.calculate_trading_fee(trade_value_eur, is_maker)
            results["fees"].append(fee)
            total_eur += fee["final_fee_eur"]
        
        if lease_value_eur > 0 and lease_term_months > 0:
            fee = self.calculate_lease_origination_fee(lease_value_eur, lease_term_months)
            results["fees"].append(fee)
            total_eur += fee["origination_fee_eur"]
        
        if repair_value_eur > 0:
            fee = self.calculate_repair_escrow_fee(repair_value_eur)
            results["fees"].append(fee)
            total_eur += fee["final_fee_eur"]
        
        if dpp_mints > 0:
            fee = self.calculate_dpp_mint_fee()
            for _ in range(dpp_mints):
                results["fees"].append(fee)
                total_eur += fee["fee_eur"]
                total_tt += fee["fee_tt"]
        
        if dpp_attestations > 0:
            fee = self.calculate_dpp_attestation_fee()
            for _ in range(dpp_attestations):
                results["fees"].append(fee)
                total_tt += fee["fee_tt"]
        
        results["summary"] = {
            "total_fees_eur": total_eur,
            "total_fees_tt": total_tt,
            "total_eur_equivalent": total_eur + total_tt  # Simplified, assumes 1:1
        }
        
        return results


def main():
    """Example usage of fee calculator"""
    
    print("=" * 60)
    print("A360 Fee Calculator - Examples")
    print("=" * 60)
    
    # Example 1: Trading without TT
    print("\n--- Example 1: Trading without TT tokens ---")
    calc = FeeCalculator(tt_balance=0, tt_staked=0)
    fee = calc.calculate_trading_fee(trade_value_eur=10000, is_maker=False)
    print(f"Trade value: €{fee['trade_value_eur']}")
    print(f"Base rate: {fee['base_rate_pct']}%")
    print(f"Fee: €{fee['final_fee_eur']}")
    
    # Example 2: Trading with TT discount
    print("\n--- Example 2: Trading with TT discount (Maker) ---")
    calc = FeeCalculator(tt_balance=0, tt_staked=15000)
    fee = calc.calculate_trading_fee(trade_value_eur=10000, is_maker=True)
    print(f"Trade value: €{fee['trade_value_eur']}")
    print(f"TT staked: {calc.tt_staked}")
    print(f"Base rate: {fee['base_rate_pct']}%")
    print(f"Discount: {fee['discount_pct']}%")
    print(f"Fee: €{fee['final_fee_eur']} (saved €{fee['discount_amount_eur']})")
    
    # Example 3: Lease origination
    print("\n--- Example 3: Lease Origination ---")
    calc = FeeCalculator()
    fee = calc.calculate_lease_origination_fee(lease_value_eur=50000, lease_term_months=12)
    print(f"Lease value: €{fee['lease_value_eur']}")
    print(f"Term: {fee['lease_term_months']} months")
    print(f"Fee rate: {fee['fee_rate_pct']}%")
    print(f"Origination fee: €{fee['origination_fee_eur']}")
    
    # Example 4: DPP minting
    print("\n--- Example 4: DPP Minting ---")
    calc = FeeCalculator()
    fee = calc.calculate_dpp_mint_fee()
    print(f"EUR fee: €{fee['fee_eur']}")
    print(f"TT fee: {fee['fee_tt']} TT")
    
    # Example 5: Repair escrow with cap
    print("\n--- Example 5: Repair Escrow (Capped) ---")
    calc = FeeCalculator()
    fee = calc.calculate_repair_escrow_fee(repair_value_eur=50000)
    print(f"Repair value: €{fee['repair_value_eur']}")
    print(f"Calculated fee: €{fee['calculated_fee_eur']}")
    print(f"Cap: €{fee['cap_eur']}")
    print(f"Final fee: €{fee['final_fee_eur']}")
    print(f"Capped: {fee['capped']}")
    
    # Example 6: Bundle calculation
    print("\n--- Example 6: Transaction Bundle ---")
    calc = FeeCalculator(tt_balance=6000, tt_staked=5000)
    result = calc.calculate_all_fees(
        trade_value_eur=25000,
        is_maker=False,
        lease_value_eur=100000,
        lease_term_months=24,
        repair_value_eur=5000,
        dpp_mints=2,
        dpp_attestations=3
    )
    print(f"TT Balance: {result['tt_balance']}")
    print(f"TT Staked: {result['tt_staked']}")
    print(f"Total fees EUR: €{result['summary']['total_fees_eur']}")
    print(f"Total fees TT: {result['summary']['total_fees_tt']} TT")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
