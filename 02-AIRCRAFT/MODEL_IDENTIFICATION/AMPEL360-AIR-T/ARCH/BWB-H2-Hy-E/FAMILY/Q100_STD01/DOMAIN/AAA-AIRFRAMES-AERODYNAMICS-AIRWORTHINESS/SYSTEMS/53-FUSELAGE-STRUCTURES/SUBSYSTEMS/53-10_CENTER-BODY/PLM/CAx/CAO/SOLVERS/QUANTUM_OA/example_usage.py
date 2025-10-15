#!/usr/bin/env python3
"""
example_usage.py - Example usage of the QOx-CSDB module

This script demonstrates how to use the quantum optimization module
for different problem types.
"""

from qox_csdb import solve_qox
import json


def example_join_order_optimization():
    """Example: Optimize join order for a database query."""
    print("\n" + "="*60)
    print("Example 1: Join Order Optimization (JOO)")
    print("="*60)
    
    # Define workload statistics
    S = {
        "workload_id": "tpc_h_q3",
        "window": "2025-10-14/1h",
        "tables": [
            {"name": "orders", "card": 1.5e6},
            {"name": "lineitem", "card": 6.0e6},
            {"name": "customer", "card": 1.5e5}
        ],
        "joins": [
            {"a": "orders.custkey", "b": "customer.custkey", "sf": 0.67},
            {"a": "lineitem.orderkey", "b": "orders.orderkey", "sf": 0.15}
        ],
        "cost_model": {"cpu_per_tuple": 1.0, "io_per_page": 1.0}
    }
    
    # Define constraints
    constraints = {"sla_ms_p95": 300}
    
    # Solve
    result = solve_qox("JOO", S, constraints, solver="qaoa", p=1, shots=4000)
    
    print(f"\nResults:")
    print(f"  Cost: {result['cost']:.2f}")
    print(f"  Feasible: {result['feasible']}")
    print(f"  Latency improvement: {result['meta']['kpi']['latency_drop']:.1%}")
    print(f"  Energy improvement: {result['meta']['kpi']['energy_drop']:.1%}")
    print(f"  Solution vector: {result['x'][:5]}... (truncated)")
    print(f"  UTCS ID: {result['meta']['utcs_id13'][:60]}...")


def example_index_selection():
    """Example: Select optimal database indexes under storage constraint."""
    print("\n" + "="*60)
    print("Example 2: Index Selection (IS)")
    print("="*60)
    
    S = {
        "workload_id": "oltp_workload",
        "window": "2025-10-14/24h",
        "tables": [
            {"name": "users", "card": 1.0e6},
            {"name": "orders", "card": 5.0e6},
            {"name": "products", "card": 1.0e5}
        ],
        "joins": [
            {"a": "orders.user_id", "b": "users.id", "sf": 0.80},
            {"a": "orders.product_id", "b": "products.id", "sf": 0.50}
        ],
        "cost_model": {"cpu_per_tuple": 1.0, "io_per_page": 1.0}
    }
    
    constraints = {"storage_budget_mb": 5000}
    
    result = solve_qox("IS", S, constraints, solver="qaoa")
    
    print(f"\nResults:")
    print(f"  Cost: {result['cost']:.2f}")
    print(f"  Feasible: {result['feasible']}")
    print(f"  Storage improvement: {result['meta']['kpi']['storage_drop']:.1%}")
    print(f"  Energy improvement: {result['meta']['kpi']['energy_drop']:.1%}")
    print(f"  Violations: {result['violations']}")


def example_with_hooks():
    """Example: Using hooks to monitor optimization progress."""
    print("\n" + "="*60)
    print("Example 3: Job Shop Scheduling with Monitoring")
    print("="*60)
    
    # Track optimization progress
    progress = {"samples": [], "refinements": []}
    
    def on_compile(stats):
        print(f"\n  [COMPILE] QUBO size: n={stats['n']}, λ={stats['lam']:.2f}")
    
    def on_sample(seed, cost):
        progress["samples"].append(cost)
        if seed % 2 == 0:  # Print every other sample
            print(f"  [SAMPLE {seed}] Cost: {cost:.3f}")
    
    def on_refine(cost, feasible):
        progress["refinements"].append(cost)
    
    def on_result(kpi):
        print(f"\n  [RESULT] Energy drop: {kpi['energy_drop']:.1%}, "
              f"Makespan drop: {kpi['makespan_drop']:.1%}")
    
    S = {
        "workload_id": "etl_pipeline",
        "window": "2025-10-14/1h",
        "tables": [{"name": f"stage_{i}", "card": 1e5} for i in range(4)],
        "joins": [{"a": f"stage_{i}.id", "b": f"stage_{i+1}.id", "sf": 0.9} 
                  for i in range(3)],
        "cost_model": {"cpu_per_tuple": 1.0, "io_per_page": 1.0}
    }
    
    constraints = {
        "precedence": [("extract", "transform"), ("transform", "load")]
    }
    
    result = solve_qox(
        "JSSP-ETL",
        S,
        constraints,
        hooks={
            "on_compile": on_compile,
            "on_sample": on_sample,
            "on_refine": on_refine,
            "on_result": on_result,
        },
        seeds=4
    )
    
    print(f"\n  Progress summary:")
    print(f"    Samples collected: {len(progress['samples'])}")
    print(f"    Refinement steps: {len(progress['refinements'])}")
    print(f"    Final cost: {result['cost']:.3f}")
    print(f"    Best sample cost: {min(progress['samples']):.3f}")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("QOx-CSDB - Quantum Optimization Examples")
    print("="*60)
    
    example_join_order_optimization()
    example_index_selection()
    example_with_hooks()
    
    print("\n" + "="*60)
    print("✅ All examples completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
