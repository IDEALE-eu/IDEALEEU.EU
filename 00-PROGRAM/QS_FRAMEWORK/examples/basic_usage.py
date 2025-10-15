"""
Basic QS Framework Usage Example

Demonstrates the complete lifecycle of QS field management:
1. Create QS field from design space and evidence
2. Freeze the field
3. Apply decision criteria to collapse
4. Validate predictions against actual outcomes
"""

import sys
sys.path.insert(0, '../src')

from qs_api import QSAPI


def main():
    print("=" * 70)
    print("QS Framework - Basic Usage Example")
    print("=" * 70)
    print()
    
    # Step 1: Initialize API
    print("Step 1: Initialize QSAPI")
    api = QSAPI()
    print(f"✓ API initialized (version {api.version})")
    print()
    
    # Step 2: Define design space
    print("Step 2: Define design space")
    design_space = {
        "description": "Wing configuration trade study",
        "variables": ["wingspan", "root_chord", "tip_chord", "sweep_angle"],
        "ranges": {
            "wingspan": (8.0, 15.0),  # meters
            "root_chord": (1.0, 2.5),  # meters
            "tip_chord": (0.5, 1.5),  # meters
            "sweep_angle": (0, 30),    # degrees
        },
        "num_candidates": 30,
        "context": "Commercial aircraft wing design Q4 2025"
    }
    print(f"✓ Design space defined with {design_space['num_candidates']} candidates")
    print()
    
    # Step 3: Provide evidence
    print("Step 3: Provide evidence data")
    evidence = {
        "cfd_simulations": {
            "description": "CFD analysis of 100 wing configurations",
            "data_points": 100,
        },
        "wind_tunnel_tests": {
            "description": "1:10 scale model tests",
            "test_cases": 25,
        },
        "historical_data": {
            "description": "Fleet data from similar aircraft",
            "flights": 50000,
        },
    }
    print(f"✓ Evidence data defined ({len(evidence)} sources)")
    print()
    
    # Step 4: Define constraints
    print("Step 4: Define constraints")
    constraints = {
        "C_0": {
            "max_weight_kg": 1500,
            "min_safety_factor": 1.5,
            "max_cost_usd": 600000,
        },
        "phi_0": {
            "prefer_manufacturability": True,
            "prefer_maintainability": True,
        },
    }
    print(f"✓ Constraints defined (Hard: {len(constraints['C_0'])}, Soft: {len(constraints['phi_0'])})")
    print()
    
    # Step 5: Create QS field
    print("Step 5: Create QS field")
    qs_field = api.create(
        design_space=design_space,
        evidence=evidence,
        constraints=constraints,
        version="QS_2025_Q4_v1",
        metadata={
            "project": "AMPEL360-AIR-T",
            "system": "ATA-57 Wings",
            "purpose": "Trade study for Q100 variant",
        }
    )
    print(f"✓ QS field created: {qs_field.version}")
    print(f"  - Candidates: {len(qs_field.candidates)}")
    print(f"  - Frozen: {qs_field.frozen}")
    print()
    
    # Step 6: Inspect candidates
    print("Step 6: Inspect candidates")
    print(f"Top 5 candidates by aggregate score:")
    sorted_candidates = sorted(
        qs_field.candidates,
        key=lambda c: c.score_vector.get("aggregate", 0.0),
        reverse=True
    )
    for i, candidate in enumerate(sorted_candidates[:5], 1):
        score = candidate.score_vector.get("aggregate", 0.0)
        feasible = all(candidate.constraints_satisfied.values())
        print(f"  {i}. {candidate.id}: score={score:.3f}, feasible={feasible}")
    print()
    
    # Step 7: Compute coverage metrics
    print("Step 7: Compute coverage metrics")
    metrics = qs_field.compute_coverage_metrics()
    print(f"✓ Coverage metrics:")
    print(f"  - Total candidates: {metrics['total_candidates']}")
    print(f"  - Feasible candidates: {metrics['feasible_candidates']}")
    print(f"  - Coverage ratio: {metrics['coverage_ratio']:.1%}")
    print(f"  - Constraint satisfaction: {metrics['constraint_satisfaction_rate']:.1%}")
    print()
    
    # Step 8: Freeze QS field
    print("Step 8: Freeze QS field")
    merkle_root = api.freeze(qs_field)
    print(f"✓ QS field frozen")
    print(f"  - Merkle root: {merkle_root[:16]}...{merkle_root[-8:]}")
    print(f"  - Timestamp: {qs_field.timestamp}")
    print()
    
    # Step 9: Verify integrity
    print("Step 9: Verify field integrity")
    is_valid = qs_field.validate_integrity()
    print(f"✓ Integrity check: {'PASS' if is_valid else 'FAIL'}")
    print()
    
    # Step 10: Apply decision criteria
    print("Step 10: Apply decision criteria")
    criteria = {
        "evaluation_method": "weighted_sum",
        "weights": {
            "performance": 0.50,
            "cost": 0.30,
            "risk": 0.20,
        },
        "penalty_weight": 1000.0,
        "decision_authority": "CCB_Chair_Jane_Smith",
        "rationale": "Minimize cost while maximizing performance under safety constraints",
    }
    print(f"✓ Decision criteria defined:")
    print(f"  - Method: {criteria['evaluation_method']}")
    print(f"  - Weights: {criteria['weights']}")
    print(f"  - Authority: {criteria['decision_authority']}")
    print()
    
    # Step 11: Collapse to select optimal candidate
    print("Step 11: Collapse QS field")
    x_star, collapse_record = api.collapse(qs_field, criteria)
    print(f"✓ Collapse completed")
    print(f"  - Selected candidate: {x_star.id}")
    print(f"  - Predicted aggregate score: {x_star.score_vector.get('aggregate', 0.0):.3f}")
    print(f"  - Collapse timestamp: {collapse_record['collapse_event']['timestamp']}")
    print(f"  - CB anchor: {collapse_record['collapse_event']['cb_anchor']}")
    print(f"  - Collapse hash: {collapse_record['collapse_hash'][:16]}...{collapse_record['collapse_hash'][-8:]}")
    print()
    
    # Step 12: Simulate actual implementation results
    print("Step 12: Validate predictions (simulated actual results)")
    actual_performance = {
        "weight_kg": 1285.0,
        "cost_usd": 485000.0,
        "lead_time_days": 195,
    }
    
    validation_report = api.validate(qs_field, x_star, actual_performance)
    print(f"✓ Validation completed")
    print(f"  - RMSE: {validation_report['metrics']['rmse_pct']:.2f}%")
    print(f"  - Prediction accuracy: {validation_report['metrics']['prediction_accuracy']:.1f}%")
    print(f"  - Within bounds: {validation_report['metrics']['within_bounds']}")
    print(f"  - Recommendation: {validation_report['recommendation']}")
    print()
    
    # Step 13: Show deltas
    print("Step 13: Performance deltas")
    for metric, delta_info in validation_report['deltas'].items():
        print(f"  {metric}:")
        print(f"    Predicted: {delta_info['predicted']:.2f}")
        print(f"    Actual: {delta_info['actual']:.2f}")
        print(f"    Delta: {delta_info['delta']:+.2f} ({delta_info['delta_pct']:+.1f}%)")
    print()
    
    print("=" * 70)
    print("QS Framework workflow completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
