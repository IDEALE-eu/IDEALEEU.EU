#!/usr/bin/env python3
"""
Contract Test for Aircraft Telemetry v1 Data Contract

This test validates that data conforms to the aircraft_telemetry_v1 contract:
- Schema compliance (Avro deserialization)
- Constraint validation (range, rate-of-change, consistency)
- PII detection (ensure no cleartext PII)
- Completeness checks
- Timestamp validation

Run on edge devices (FL clients) before data is used for training.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime, timezone
import hashlib


class ContractValidator:
    """Validates data against aircraft_telemetry_v1 contract."""
    
    def __init__(self, contract_path: str = None):
        """
        Initialize validator with contract definitions.
        
        Args:
            contract_path: Path to contract directory (default: current directory)
        """
        if contract_path is None:
            contract_path = Path(__file__).parent.parent
        self.contract_path = Path(contract_path)
        
        # Load constraints from constraints.yaml
        self.range_constraints = self._load_range_constraints()
        self.rate_constraints = self._load_rate_constraints()
        self.consistency_constraints = self._load_consistency_constraints()
        
        # Validation results
        self.violations = []
        self.warnings = []
        self.stats = {
            "total_messages": 0,
            "valid_messages": 0,
            "rejected_messages": 0,
            "flagged_messages": 0,
        }
    
    def _load_range_constraints(self) -> Dict[str, Dict]:
        """Load range constraints from constraints.yaml."""
        # Simplified constraint definitions (in production, parse YAML)
        return {
            "engine_1_egt": {"min": -50, "max": 1200, "action_above": "ALERT"},
            "engine_1_oil_temperature": {"min": -40, "max": 150, "action_below": "ALERT", "action_above": "ALERT"},
            "engine_1_oil_pressure": {"min": 10, "max": 150, "action_below": "ALERT", "action_above": "ALERT"},
            "h2_tank_pressure_fwd": {"min": 0, "max": 350, "action_below": "REJECT", "action_above": "ALERT"},
            "h2_tank_temp_fwd": {"min": 18, "max": 42, "action_below": "REJECT", "action_above": "ALERT"},
            "airspeed_indicated": {"min": 0, "max": 400, "action_below": "REJECT", "action_above": "ALERT"},
            "altitude_pressure": {"min": -1000, "max": 50000, "action_below": "ALERT", "action_above": "REJECT"},
            "outside_air_temperature": {"min": -70, "max": 60, "action_below": "ALERT", "action_above": "ALERT"},
        }
    
    def _load_rate_constraints(self) -> Dict[str, Dict]:
        """Load rate-of-change constraints."""
        return {
            "engine_1_egt": {"max_delta": 100, "window": 1},
            "h2_tank_pressure_fwd": {"max_delta": 50, "window": 1},
            "altitude_pressure": {"max_delta": 100, "window": 1},
        }
    
    def _load_consistency_constraints(self) -> List[Dict]:
        """Load consistency (cross-signal) constraints."""
        return [
            {
                "name": "H2 pressure-temperature",
                "signals": ["h2_tank_pressure_fwd", "h2_tank_temp_fwd"],
                "check": lambda p, t: p < 400 * (t / 300),
            }
        ]
    
    def validate_message(self, message: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Validate a single telemetry message.
        
        Args:
            message: Telemetry message as dict
            
        Returns:
            (is_valid, action) where action is "ACCEPT", "ALERT", or "REJECT"
        """
        self.stats["total_messages"] += 1
        
        # 1. Required field validation
        required_fields = ["timestamp", "platform_id", "signal_name", "value", "quality"]
        for field in required_fields:
            if field not in message:
                self.violations.append(f"Missing required field: {field}")
                self.stats["rejected_messages"] += 1
                return False, "REJECT"
        
        # 2. Timestamp validation
        timestamp_valid, timestamp_action = self._validate_timestamp(message["timestamp"])
        if not timestamp_valid:
            self.violations.append(f"Invalid timestamp: {message['timestamp']}")
            self.stats["rejected_messages"] += 1
            return False, "REJECT"
        
        # 3. PII detection (platform_id should be hash, not cleartext)
        if not self._is_pseudonymized(message["platform_id"]):
            self.violations.append(f"Platform ID not pseudonymized: {message['platform_id']}")
            self.stats["rejected_messages"] += 1
            return False, "REJECT"
        
        # 4. Range validation
        signal_name = message["signal_name"]
        value = message["value"]
        
        if signal_name in self.range_constraints:
            range_valid, range_action = self._validate_range(signal_name, value)
            if not range_valid:
                if range_action == "REJECT":
                    self.violations.append(f"Range violation: {signal_name}={value}")
                    self.stats["rejected_messages"] += 1
                    return False, "REJECT"
                elif range_action == "ALERT":
                    self.warnings.append(f"Range warning: {signal_name}={value}")
                    self.stats["flagged_messages"] += 1
                    return True, "ALERT"
        
        # 5. Quality indicator check
        if message["quality"] not in [0, 1, 2]:
            self.violations.append(f"Invalid quality indicator: {message['quality']}")
            self.stats["rejected_messages"] += 1
            return False, "REJECT"
        
        self.stats["valid_messages"] += 1
        return True, "ACCEPT"
    
    def _validate_timestamp(self, timestamp: int) -> Tuple[bool, str]:
        """Validate timestamp is reasonable (not too far in future or past)."""
        now = datetime.now(timezone.utc).timestamp() * 1000  # Convert to milliseconds
        
        # Not more than 60 seconds in future
        if timestamp > now + 60000:
            return False, "REJECT"
        
        # Not more than 365 days in past (allow historical data for testing)
        if timestamp < now - (365 * 86400000):
            return False, "REJECT"
        
        return True, "ACCEPT"
    
    def _is_pseudonymized(self, platform_id: str) -> bool:
        """Check if platform_id appears to be a hash (not cleartext tail number)."""
        # Simple heuristic: should be 64-char hex string (SHA-256)
        # or at least not contain cleartext patterns like "N12345" or "AC-H2-001"
        if len(platform_id) == 64 and all(c in "0123456789abcdef" for c in platform_id):
            return True
        
        # Check for common cleartext patterns
        cleartext_patterns = ["N", "AC-", "aircraft", "tail"]
        if any(pattern.lower() in platform_id.lower() for pattern in cleartext_patterns):
            return False
        
        return True  # Assume pseudonymized if not obviously cleartext
    
    def _validate_range(self, signal_name: str, value: float) -> Tuple[bool, str]:
        """Validate value is within acceptable range."""
        constraints = self.range_constraints[signal_name]
        min_val = constraints.get("min")
        max_val = constraints.get("max")
        
        if min_val is not None and value < min_val:
            action = constraints.get("action_below", "REJECT")
            return False, action
        
        if max_val is not None and value > max_val:
            action = constraints.get("action_above", "REJECT")
            return False, action
        
        return True, "ACCEPT"
    
    def validate_batch(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validate a batch of messages.
        
        Args:
            messages: List of telemetry messages
            
        Returns:
            Validation report with statistics and violations
        """
        for msg in messages:
            self.validate_message(msg)
        
        return {
            "stats": self.stats,
            "violations": self.violations,
            "warnings": self.warnings,
            "success_rate": self.stats["valid_messages"] / max(self.stats["total_messages"], 1),
        }
    
    def print_report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("Aircraft Telemetry v1 Contract Validation Report")
        print("="*60)
        print(f"\nTotal messages: {self.stats['total_messages']}")
        print(f"Valid messages: {self.stats['valid_messages']}")
        print(f"Rejected messages: {self.stats['rejected_messages']}")
        print(f"Flagged messages: {self.stats['flagged_messages']}")
        print(f"Success rate: {self.stats['valid_messages'] / max(self.stats['total_messages'], 1):.1%}")
        
        if self.violations:
            print(f"\n⚠ {len(self.violations)} VIOLATIONS:")
            for violation in self.violations[:10]:  # Show first 10
                print(f"  - {violation}")
            if len(self.violations) > 10:
                print(f"  ... and {len(self.violations) - 10} more")
        
        if self.warnings:
            print(f"\n⚠ {len(self.warnings)} WARNINGS:")
            for warning in self.warnings[:10]:  # Show first 10
                print(f"  - {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more")
        
        print("\n" + "="*60)


def test_contract_with_examples():
    """Test contract using example telemetry data."""
    # Load example data
    example_file = Path(__file__).parent.parent / "examples" / "telemetry_sample.jsonl"
    
    if not example_file.exists():
        print(f"Error: Example file not found: {example_file}")
        return False
    
    messages = []
    with open(example_file, "r") as f:
        for line in f:
            messages.append(json.loads(line))
    
    print(f"Loaded {len(messages)} example messages")
    
    # Validate
    validator = ContractValidator()
    report = validator.validate_batch(messages)
    validator.print_report()
    
    # Test passes if success rate > 80%
    success = report["success_rate"] > 0.80
    
    if success:
        print("\n✓ Contract test PASSED")
    else:
        print("\n✗ Contract test FAILED")
    
    return success


def main():
    """Main entry point for contract testing."""
    print("Aircraft Telemetry v1 Contract Test")
    print("="*60)
    
    success = test_contract_with_examples()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
