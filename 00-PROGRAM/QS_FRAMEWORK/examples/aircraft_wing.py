"""
Aircraft Wing Design Trade Study Example

Demonstrates QS Framework usage for a realistic aerospace design problem:
- Multi-objective optimization (aerodynamics, structures, cost)
- Pareto frontier analysis
- Constraint handling (safety, certification)
- Uncertainty quantification
- Evidence-based prediction
"""

import sys
sys.path.insert(0, '../src')

import qs_api
import random


def generate_wing_candidates(design_space, evidence, constraints):
    """
    Custom generator for wing design candidates using domain knowledge.
    
    In practice, this would use:
    - Parametric CAD models
    - CFD and FEA solvers
    - Optimization algorithms (genetic, gradient-based)
    - Historical design databases
    """
    num_candidates = design_space.get("num_candidates", 50)
    candidates = []
    
    # Wing design parameters
    for i in range(num_candidates):
        # Generate design parameters
        wingspan = random.uniform(28.0, 38.0)  # meters
        aspect_ratio = random.uniform(8.0, 12.0)
        taper_ratio = random.uniform(0.2, 0.4)
        sweep_angle = random.uniform(20.0, 35.0)  # degrees
        thickness_ratio = random.uniform(0.10, 0.14)
        
        # Derived parameters
        wing_area = wingspan**2 / aspect_ratio
        root_chord = (2 * wing_area) / (wingspan * (1 + taper_ratio))
        tip_chord = root_chord * taper_ratio
        
        configuration = {
            "wingspan_m": wingspan,
            "aspect_ratio": aspect_ratio,
            "taper_ratio": taper_ratio,
            "sweep_angle_deg": sweep_angle,
            "thickness_ratio": thickness_ratio,
            "wing_area_m2": wing_area,
            "root_chord_m": root_chord,
            "tip_chord_m": tip_chord,
        }
        
        # Estimate performance metrics (simplified models)
        # In reality, these would come from CFD/FEA
        lift_drag_ratio = aspect_ratio * 15.0 - sweep_angle * 0.2 + random.uniform(-2, 2)
        cruise_efficiency = 0.75 + (lift_drag_ratio - 18) * 0.01
        
        # Structural weight estimation (simplified)
        structural_weight = (wing_area * 50 + wingspan * 100) * (1 + random.uniform(-0.1, 0.1))
        
        # Cost estimation
        manufacturing_complexity = (1.0 - taper_ratio) * sweep_angle / 10.0
        unit_cost = (wing_area * 5000 + structural_weight * 800 + 
                     manufacturing_complexity * 50000)
        
        # Risk assessment
        certification_risk = 0.1 if sweep_angle < 30 else 0.2
        manufacturing_risk = manufacturing_complexity / 10.0
        technology_risk = 0.05 if thickness_ratio > 0.11 else 0.15
        overall_risk = (certification_risk + manufacturing_risk + technology_risk) / 3.0
        
        # Score vector
        score_vector = {
            "aerodynamic_performance": min(cruise_efficiency, 1.0),
            "structural_efficiency": max(0.0, 1.0 - structural_weight / 5000.0),
            "cost_efficiency": max(0.0, 1.0 - unit_cost / 1000000.0),
            "risk_score": 1.0 - overall_risk,
            "aggregate": (cruise_efficiency + (1.0 - structural_weight/5000.0) + 
                         (1.0 - unit_cost/1000000.0) + (1.0 - overall_risk)) / 4.0,
        }
        
        # Uncertainty (proportional to risk)
        uncertainty = {
            "sigma_aerodynamic": 0.03 * (1 + overall_risk),
            "sigma_structural": 0.05 * (1 + overall_risk),
            "sigma_cost": 0.10 * (1 + manufacturing_complexity / 3.0),
            "confidence_interval": [
                max(0.0, score_vector["aggregate"] - 0.08),
                min(1.0, score_vector["aggregate"] + 0.08)
            ],
        }
        
        # Bounds
        bounds = {
            "lift_drag_ratio": (lift_drag_ratio * 0.9, lift_drag_ratio * 1.1),
            "weight_kg": (structural_weight * 0.95, structural_weight * 1.05),
            "cost_usd": (unit_cost * 0.9, unit_cost * 1.15),
            "development_months": (24, 36),
        }
        
        # Check constraints
        max_weight = constraints.get("C_0", {}).get("max_weight_kg", 3000)
        min_lift_drag = constraints.get("C_0", {}).get("min_lift_drag_ratio", 15.0)
        max_cost = constraints.get("C_0", {}).get("max_cost_usd", 800000)
        
        constraints_satisfied = {
            "C0_weight_limit": structural_weight <= max_weight,
            "C0_aerodynamic_performance": lift_drag_ratio >= min_lift_drag,
            "C0_cost_limit": unit_cost <= max_cost,
            "C0_certification": certification_risk < 0.25,
            "phi0_manufacturability": manufacturing_complexity < 5.0,
            "phi0_technology_maturity": technology_risk < 0.20,
        }
        
        # UTCS manifest
        utcs_manifest = {
            "context": "AMPEL360-AIR-T BWB-H2 Wing Trade Study Q4 2025",
            "content": {
                "ata_chapter": "ATA-57 Wings",
                "domain": "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS",
                "system": "57-WINGS",
            },
            "cache": {
                "cfd_case": f"wing_config_{i:03d}",
                "fea_case": f"struct_analysis_{i:03d}",
            },
            "structure": "TFA/AAA/SI",
            "style": "ISO_10303",
            "sheet": "wing_requirements_Q4.csv",
        }
        
        # Provenance
        provenance = {
            "generated_by": "wing_optimizer_v2.1",
            "timestamp": "2025-10-15T00:00:00Z",
            "parent_design": "baseline_conventional_wing_v1",
            "evidence_refs": [
                "cfd_validation_db",
                "historical_aircraft_data",
                "wind_tunnel_campaign_2025",
            ],
            "optimization_method": "multi_objective_genetic_algorithm",
        }
        
        # Create candidate
        candidate = qs_api.Candidate(
            id=f"wing_candidate_{i+1:03d}",
            configuration=configuration,
            utcs_manifest=utcs_manifest,
            score_vector=score_vector,
            uncertainty=uncertainty,
            bounds=bounds,
            constraints_satisfied=constraints_satisfied,
            provenance=provenance,
        )
        
        candidates.append(candidate)
    
    return candidates


def main():
    print("=" * 80)
    print("QS Framework - Aircraft Wing Design Trade Study")
    print("=" * 80)
    print()
    
    # Initialize API
    api = qs_api.QSAPI()
    
    # Define design space
    print("Step 1: Define wing design space")
    design_space = {
        "description": "Commercial aircraft wing optimization for BWB-H2 configuration",
        "variables": [
            "wingspan", "aspect_ratio", "taper_ratio", 
            "sweep_angle", "thickness_ratio"
        ],
        "ranges": {
            "wingspan_m": (28.0, 38.0),
            "aspect_ratio": (8.0, 12.0),
            "taper_ratio": (0.2, 0.4),
            "sweep_angle_deg": (20.0, 35.0),
            "thickness_ratio": (0.10, 0.14),
        },
        "num_candidates": 50,
        "context": "AMPEL360-AIR-T BWB-H2-Hy-E Q100 Variant",
    }
    print(f"✓ Exploring {design_space['num_candidates']} wing configurations")
    print()
    
    # Evidence base
    print("Step 2: Compile evidence base")
    evidence = {
        "cfd_database": {
            "description": "CFD simulations of 500+ wing configurations",
            "simulations": 527,
            "fidelity": "RANS with turbulence models",
        },
        "wind_tunnel_data": {
            "description": "1:15 scale model tests at TUM wind tunnel",
            "test_points": 84,
            "reynolds_number": 3.5e6,
        },
        "historical_fleet": {
            "description": "In-service data from similar aircraft",
            "aircraft_years": 250,
            "flight_hours": 125000,
        },
        "structural_tests": {
            "description": "Static and fatigue test results",
            "test_articles": 12,
            "load_cases": 45,
        },
    }
    print(f"✓ Evidence compiled from {len(evidence)} sources")
    print()
    
    # Define constraints
    print("Step 3: Define design constraints")
    constraints = {
        "C_0": {  # Hard constraints
            "max_weight_kg": 2800,
            "min_lift_drag_ratio": 16.0,
            "max_cost_usd": 750000,
            "certification": "CS-25 / FAR-25",
        },
        "phi_0": {  # Soft preferences
            "prefer_high_aspect_ratio": True,
            "prefer_low_sweep": True,
            "prefer_mature_technology": True,
        },
    }
    print(f"✓ Constraints defined:")
    print(f"  - Max weight: {constraints['C_0']['max_weight_kg']} kg")
    print(f"  - Min L/D: {constraints['C_0']['min_lift_drag_ratio']}")
    print(f"  - Max cost: ${constraints['C_0']['max_cost_usd']:,}")
    print()
    
    # Create QS field with custom generator
    print("Step 4: Generate QS field")
    qs_field = api.create(
        design_space=design_space,
        evidence=evidence,
        constraints=constraints,
        version="QS_Wing_2025_Q4_v1",
        metadata={
            "project": "AMPEL360-AIR-T",
            "variant": "Q100_STD01",
            "ata_chapter": "57-WINGS",
            "trade_study": "Wing planform optimization",
        },
        candidate_generator=generate_wing_candidates,
    )
    print(f"✓ QS field created: {qs_field.version}")
    print(f"  - Total candidates: {len(qs_field.candidates)}")
    print()
    
    # Analyze coverage
    print("Step 5: Analyze coverage")
    metrics = qs_field.compute_coverage_metrics()
    print(f"✓ Coverage metrics:")
    print(f"  - Feasible candidates: {metrics['feasible_candidates']} / {metrics['total_candidates']}")
    print(f"  - Coverage ratio: {metrics['coverage_ratio']:.1%}")
    print(f"  - Constraint satisfaction: {metrics['constraint_satisfaction_rate']:.1%}")
    print()
    
    # Pareto frontier analysis
    print("Step 6: Extract Pareto frontier")
    pareto_candidates = qs_field.get_pareto_frontier([
        "aerodynamic_performance",
        "structural_efficiency",
        "cost_efficiency",
    ])
    print(f"✓ Pareto optimal candidates: {len(pareto_candidates)}")
    print(f"  Top 3 Pareto candidates:")
    for i, candidate in enumerate(pareto_candidates[:3], 1):
        print(f"    {i}. {candidate.id}:")
        print(f"       Aero: {candidate.score_vector['aerodynamic_performance']:.3f}, "
              f"Struct: {candidate.score_vector['structural_efficiency']:.3f}, "
              f"Cost: {candidate.score_vector['cost_efficiency']:.3f}")
    print()
    
    # Freeze
    print("Step 7: Freeze QS field")
    merkle_root = api.freeze(qs_field)
    print(f"✓ Field frozen with Merkle root:")
    print(f"  {merkle_root[:32]}...")
    print()
    
    # Multiple criteria scenarios
    print("Step 8: Evaluate multiple decision scenarios")
    scenarios = [
        {
            "name": "Performance-Optimized",
            "criteria": {
                "evaluation_method": "weighted_sum",
                "weights": {
                    "aerodynamic_performance": 0.60,
                    "structural_efficiency": 0.20,
                    "cost_efficiency": 0.10,
                    "risk_score": 0.10,
                },
                "decision_authority": "Chief Engineer - Aerodynamics",
            }
        },
        {
            "name": "Cost-Optimized",
            "criteria": {
                "evaluation_method": "weighted_sum",
                "weights": {
                    "aerodynamic_performance": 0.20,
                    "structural_efficiency": 0.20,
                    "cost_efficiency": 0.50,
                    "risk_score": 0.10,
                },
                "decision_authority": "Program Manager",
            }
        },
        {
            "name": "Balanced",
            "criteria": {
                "evaluation_method": "weighted_sum",
                "weights": {
                    "aerodynamic_performance": 0.35,
                    "structural_efficiency": 0.30,
                    "cost_efficiency": 0.25,
                    "risk_score": 0.10,
                },
                "decision_authority": "CCB Chair",
            }
        },
    ]
    
    for scenario in scenarios:
        x_star, collapse_record = qs_field.collapse(scenario["criteria"])
        print(f"  Scenario: {scenario['name']}")
        print(f"    Selected: {x_star.id}")
        print(f"    Aggregate score: {x_star.score_vector['aggregate']:.3f}")
        config = x_star.configuration
        print(f"    Wingspan: {config['wingspan_m']:.1f}m, "
              f"AR: {config['aspect_ratio']:.1f}, "
              f"Sweep: {config['sweep_angle_deg']:.1f}°")
        print()
    
    # Select final configuration (Balanced)
    print("Step 9: Apply final decision criteria (Balanced)")
    final_criteria = scenarios[2]["criteria"]
    final_criteria["rationale"] = "Balanced design for production aircraft"
    x_star, collapse_record = qs_field.collapse(final_criteria)
    
    print(f"✓ Final selection: {x_star.id}")
    print(f"  Configuration:")
    for key, value in x_star.configuration.items():
        print(f"    {key}: {value:.3f}")
    print()
    
    print("=" * 80)
    print("Wing design trade study completed!")
    print("=" * 80)
    print()
    print("Next steps:")
    print("- Detailed CFD validation of selected design")
    print("- Full structural FEA analysis")
    print("- Manufacturing feasibility review")
    print("- Cost estimate refinement")
    print("- PDR presentation preparation")


if __name__ == "__main__":
    main()
