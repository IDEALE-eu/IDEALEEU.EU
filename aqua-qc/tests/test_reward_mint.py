"""
Test for TeknIA reward calculation.

Tests reward formula:
R_t = αC*(€_saved) + αE*(kgCO2_saved) + αQ*(F1 or ΔE) 
      - αOH*(overhead_depth−3)^+ - αWT*(wall_time_ratio−1.5)^+
mint_t = κ * max(R_t, 0)
"""

import sys
from pathlib import Path

import pytest
import yaml

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def load_reward_config():
    """Load reward configuration from CI config."""
    config_path = Path(__file__).parent.parent / "ci" / "config.yaml"
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config["rewards"]


def compute_reward(
    cost_saved: float,
    co2_saved: float,
    quality_metric: float,
    overhead_depth: float,
    wall_time_ratio: float,
    alpha_cost: float = 1.0,
    alpha_energy: float = 0.5,
    alpha_quality: float = 2.0,
    alpha_overhead: float = 0.3,
    alpha_walltime: float = 0.2,
    kappa: float = 100.0
) -> tuple:
    """
    Compute TeknIA reward and mint value.
    
    Args:
        cost_saved: Cost savings in euros
        co2_saved: CO2 savings in kg
        quality_metric: Quality metric (F1 or energy error drop)
        overhead_depth: Circuit depth overhead ratio
        wall_time_ratio: Wall time overhead ratio
        alpha_*: Weight parameters
        kappa: Mint scaling factor
        
    Returns:
        (reward, mint_value)
    """
    # Positive contributions
    reward = (
        alpha_cost * cost_saved +
        alpha_energy * co2_saved +
        alpha_quality * quality_metric
    )
    
    # Penalties (only if exceeding thresholds)
    overhead_penalty = max(0, overhead_depth - 3.0)
    walltime_penalty = max(0, wall_time_ratio - 1.5)
    
    reward -= alpha_overhead * overhead_penalty
    reward -= alpha_walltime * walltime_penalty
    
    # Mint calculation (non-negative)
    mint_value = kappa * max(reward, 0)
    
    return reward, mint_value


def test_reward_mint_nonnegative():
    """Test that mint value is always non-negative."""
    config = load_reward_config()
    
    # Test case 1: Positive reward
    reward1, mint1 = compute_reward(
        cost_saved=100.0,
        co2_saved=5.0,
        quality_metric=0.85,
        overhead_depth=2.5,
        wall_time_ratio=1.3,
        **config
    )
    
    assert mint1 >= 0, "Mint value must be non-negative"
    assert reward1 > 0, "This configuration should yield positive reward"
    
    # Test case 2: Negative reward (should still have non-negative mint)
    reward2, mint2 = compute_reward(
        cost_saved=0.0,
        co2_saved=0.0,
        quality_metric=0.1,
        overhead_depth=5.0,
        wall_time_ratio=3.0,
        **config
    )
    
    assert mint2 >= 0, "Mint value must be non-negative even with negative reward"
    assert mint2 == 0, "Mint should be zero for negative reward"
    assert reward2 < 0, "This configuration should yield negative reward"
    
    print(f"✓ Mint non-negativity test passed")
    print(f"  Case 1: reward={reward1:.2f}, mint={mint1:.2f}")
    print(f"  Case 2: reward={reward2:.2f}, mint={mint2:.2f}")


def test_reward_monotonicity_quality():
    """Test that reward increases monotonically with quality metric."""
    config = load_reward_config()
    
    quality_values = [0.5, 0.7, 0.9]
    rewards = []
    
    for quality in quality_values:
        reward, mint = compute_reward(
            cost_saved=50.0,
            co2_saved=2.0,
            quality_metric=quality,
            overhead_depth=2.0,
            wall_time_ratio=1.2,
            **config
        )
        rewards.append(reward)
    
    # Check monotonicity
    for i in range(len(rewards) - 1):
        assert rewards[i + 1] > rewards[i], (
            f"Reward should increase with quality: "
            f"{rewards[i]:.2f} -> {rewards[i+1]:.2f}"
        )
    
    print(f"✓ Quality monotonicity test passed")
    print(f"  Rewards for quality {quality_values}: {[f'{r:.2f}' for r in rewards]}")


def test_reward_penalty_thresholds():
    """Test that penalties only apply when thresholds are exceeded."""
    config = load_reward_config()
    
    # Case 1: Within thresholds (no penalty)
    reward1, _ = compute_reward(
        cost_saved=100.0,
        co2_saved=5.0,
        quality_metric=0.8,
        overhead_depth=2.5,  # < 3.0
        wall_time_ratio=1.2,  # < 1.5
        **config
    )
    
    # Case 2: Exceeding depth threshold
    reward2, _ = compute_reward(
        cost_saved=100.0,
        co2_saved=5.0,
        quality_metric=0.8,
        overhead_depth=4.0,  # > 3.0, penalty = 1.0
        wall_time_ratio=1.2,
        **config
    )
    
    # Case 3: Exceeding walltime threshold
    reward3, _ = compute_reward(
        cost_saved=100.0,
        co2_saved=5.0,
        quality_metric=0.8,
        overhead_depth=2.5,
        wall_time_ratio=2.0,  # > 1.5, penalty = 0.5
        **config
    )
    
    # Penalties should reduce reward
    assert reward2 < reward1, "Depth penalty should reduce reward"
    assert reward3 < reward1, "Walltime penalty should reduce reward"
    
    # Check penalty amounts
    depth_penalty = config["alpha_overhead"] * 1.0  # 4.0 - 3.0
    walltime_penalty = config["alpha_walltime"] * 0.5  # 2.0 - 1.5
    
    assert abs((reward1 - reward2) - depth_penalty) < 1e-6, "Depth penalty mismatch"
    assert abs((reward1 - reward3) - walltime_penalty) < 1e-6, "Walltime penalty mismatch"
    
    print(f"✓ Penalty threshold test passed")
    print(f"  No penalty: {reward1:.2f}")
    print(f"  Depth penalty: {reward2:.2f} (delta: {reward1-reward2:.2f})")
    print(f"  Walltime penalty: {reward3:.2f} (delta: {reward1-reward3:.2f})")


def test_kpi_reward_mapping():
    """Test reward calculation with realistic KPI values."""
    config = load_reward_config()
    
    # Scenario 1: VQE H2 - good performance
    kpi_vqe = {
        "infidelity_drop": 0.35,
        "energy_err_drop": 0.002,
        "overhead_depth": 2.8,
        "wall_time_ratio": 1.3
    }
    
    reward_vqe, mint_vqe = compute_reward(
        cost_saved=80.0,  # Simulated cost savings
        co2_saved=3.5,    # Simulated CO2 savings
        quality_metric=kpi_vqe["infidelity_drop"],
        overhead_depth=kpi_vqe["overhead_depth"],
        wall_time_ratio=kpi_vqe["wall_time_ratio"],
        **config
    )
    
    assert reward_vqe > 0, "Good VQE performance should yield positive reward"
    assert mint_vqe > 0, "Should mint tokens for good performance"
    
    # Scenario 2: QML - excellent performance
    kpi_qml = {
        "F1_anomaly": 0.85,
        "RMSE_drop": 0.12,
        "Energy_per_inf_drop": 0.18
    }
    
    reward_qml, mint_qml = compute_reward(
        cost_saved=120.0,
        co2_saved=5.0,
        quality_metric=kpi_qml["F1_anomaly"],
        overhead_depth=1.5,  # QML has less overhead
        wall_time_ratio=1.1,
        **config
    )
    
    assert reward_qml > reward_vqe, "Better performance should yield higher reward"
    assert mint_qml > mint_vqe, "Better performance should mint more tokens"
    
    print(f"✓ KPI reward mapping test passed")
    print(f"  VQE scenario: reward={reward_vqe:.2f}, mint={mint_vqe:.2f}")
    print(f"  QML scenario: reward={reward_qml:.2f}, mint={mint_qml:.2f}")


def test_reward_config_consistency():
    """Test that reward configuration is consistent with CI config."""
    config = load_reward_config()
    
    # Check all required parameters are present
    required_params = [
        "alpha_cost", "alpha_energy", "alpha_quality",
        "alpha_overhead", "alpha_walltime", "kappa"
    ]
    
    for param in required_params:
        assert param in config, f"Missing reward parameter: {param}"
        assert config[param] > 0, f"Reward parameter {param} must be positive"
    
    # Check reasonable ranges
    assert 0 < config["alpha_cost"] <= 10
    assert 0 < config["alpha_energy"] <= 10
    assert 0 < config["alpha_quality"] <= 10
    assert 0 < config["alpha_overhead"] <= 1
    assert 0 < config["alpha_walltime"] <= 1
    assert config["kappa"] >= 1
    
    print(f"✓ Reward config consistency test passed")
    print(f"  All parameters present and in valid ranges")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
