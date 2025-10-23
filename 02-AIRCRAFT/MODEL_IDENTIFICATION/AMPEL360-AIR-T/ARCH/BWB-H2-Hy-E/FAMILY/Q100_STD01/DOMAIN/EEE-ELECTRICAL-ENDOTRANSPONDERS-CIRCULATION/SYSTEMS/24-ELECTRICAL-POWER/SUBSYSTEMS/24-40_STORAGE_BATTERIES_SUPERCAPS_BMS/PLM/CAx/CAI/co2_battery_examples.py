#!/usr/bin/env python3
"""
CO₂ Endocircular Battery System - Usage Examples

This script demonstrates various use cases for the CO₂ battery system,
including design trade-offs, performance calculations, and safety analysis.

Run with: python3 co2_battery_examples.py
"""

import sys
from pathlib import Path

# Add CAE directory to path (where the core simulation module is located)
cae_dir = Path(__file__).parent.parent / "CAE"
sys.path.insert(0, str(cae_dir))

from co2_battery_endocircular import (
    CO2Phase,
    CycleType,
    CO2Properties,
    SystemDesign,
    CO2BatterySystem,
    create_example_system,
)


def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"{title:^80}")
    print("=" * 80)


def example_1_basic_sublimation_system():
    """Example 1: Basic sublimation cycle for UAV application."""
    print_section_header("EXAMPLE 1: UAV Power Augmentation (Sublimation Cycle)")
    
    print("\nAPPLICATION: Small UAV requiring 2 kW for 30 minutes (1 kWh)")
    print("DESIGN CHOICE: Simple sublimation + expander for low complexity")
    
    # Create system
    system = create_example_system(
        co2_mass_kg=50.0,  # 50 kg CO₂
        cycle_type=CycleType.SUBLIMATION_EXPANDER
    )
    
    # Calculate performance
    perf = system.calculate_system_performance(
        ambient_temp_c=20.0,  # Flight altitude ambient
        heat_source_temp_c=70.0  # Waste heat from propulsion
    )
    
    print(f"\nSYSTEM CONFIGURATION:")
    print(f"  CO₂ Mass: {perf['co2_mass_kg']:.1f} kg")
    print(f"  Storage: {system.design.storage_temp_c:.1f}°C, {system.design.storage_pressure_bar:.1f} bar")
    print(f"  Expansion Ratio: {system.design.storage_pressure_bar / system.design.expansion_pressure_bar:.1f}:1")
    
    print(f"\nENERGY STORAGE:")
    print(f"  Thermal Energy: {perf['thermal_energy_stored_kwh']:.2f} kWh")
    print(f"  Electrical Energy: {perf['electrical_energy_recoverable_kwh']:.2f} kWh")
    print(f"  Specific Energy: {perf['specific_energy_wh_kg']:.1f} Wh/kg")
    print(f"  ✓ Meets requirement: {perf['electrical_energy_recoverable_kwh']:.2f} > 1.0 kWh")
    
    print(f"\nEFFICIENCY:")
    print(f"  Discharge: {perf['discharge_efficiency']*100:.1f}%")
    print(f"  Round-Trip: {perf['roundtrip_efficiency']*100:.1f}%")
    print(f"  Recharge Energy: {perf['recharge_energy_kwh']:.2f} kWh")
    
    # Volume and weight
    volume_m3 = system.design.co2_mass_kg / system.props.RHO_SOLID
    print(f"\nPHYSICAL CHARACTERISTICS:")
    print(f"  CO₂ Volume: {volume_m3*1000:.1f} liters")
    print(f"  System Weight: ~{system.design.co2_mass_kg * 1.5:.1f} kg (incl. tank)")
    print(f"  Power Density: {perf['electrical_energy_recoverable_kwh'] / (system.design.co2_mass_kg * 1.5):.1f} Wh/kg")


def example_2_sco2_stationary():
    """Example 2: Stationary sCO₂ Brayton cycle for grid storage."""
    print_section_header("EXAMPLE 2: Grid-Scale Storage (sCO₂ Brayton Cycle)")
    
    print("\nAPPLICATION: 100 kWh storage for renewable energy smoothing")
    print("DESIGN CHOICE: sCO₂ Brayton for high efficiency with waste heat")
    
    # Design for 100 kWh output
    # Working backwards: 100 kWh / 0.40 efficiency / 0.1586 kWh/kg = ~1575 kg
    co2_mass = 1600.0  # kg
    
    design = SystemDesign(
        co2_mass_kg=co2_mass,
        storage_temp_c=40.0,  # Above critical
        storage_pressure_bar=100.0,  # Well above critical
        expansion_pressure_bar=80.0,  # High-pressure expansion
        expander_efficiency=0.85,
        recuperator_effectiveness=0.90,
        liquefaction_cop=2.0,  # Better COP at higher temp
        cycle_type=CycleType.SCO2_BRAYTON,
    )
    
    system = CO2BatterySystem(design)
    
    # Calculate with high-temperature heat source
    perf = system.calculate_system_performance(
        ambient_temp_c=25.0,
        heat_source_temp_c=450.0  # Industrial waste heat or solar
    )
    
    print(f"\nSYSTEM CONFIGURATION:")
    print(f"  CO₂ Mass: {perf['co2_mass_kg']:.0f} kg")
    print(f"  Storage: {design.storage_temp_c:.1f}°C, {design.storage_pressure_bar:.1f} bar")
    print(f"  Operating Pressure: {design.storage_pressure_bar:.0f} → {design.expansion_pressure_bar:.0f} bar")
    print(f"  Recuperator: {design.recuperator_effectiveness*100:.0f}% effectiveness")
    
    print(f"\nENERGY CAPACITY:")
    print(f"  Thermal Energy: {perf['thermal_energy_stored_kwh']:.1f} kWh")
    print(f"  Electrical Energy: {perf['electrical_energy_recoverable_kwh']:.1f} kWh")
    print(f"  Target: 100 kWh → Achievement: {perf['electrical_energy_recoverable_kwh']/100*100:.1f}%")
    
    print(f"\nPERFORMANCE:")
    print(f"  Discharge Efficiency: {perf['discharge_efficiency']*100:.1f}%")
    print(f"  Round-Trip Efficiency: {perf['roundtrip_efficiency']*100:.1f}%")
    print(f"  Carnot Limit: {perf['carnot_efficiency']*100:.1f}%")
    print(f"  Capacity Factor: {perf['discharge_efficiency']/perf['carnot_efficiency']*100:.1f}% of Carnot")
    
    print(f"\nECONOMICS (Rough Estimate):")
    capital_cost_per_kwh = 100  # $/kWh
    total_cost = perf['electrical_energy_recoverable_kwh'] * capital_cost_per_kwh
    print(f"  Capital Cost: ${total_cost:,.0f} (@ ${capital_cost_per_kwh}/kWh)")
    print(f"  Levelized Cost: ${total_cost / (10000 * perf['electrical_energy_recoverable_kwh']):.3f}/kWh")
    print(f"  (Assuming 10,000 cycles over lifetime)")


def example_3_hybrid_aircraft():
    """Example 3: Hybrid aircraft with multiple storage systems."""
    print_section_header("EXAMPLE 3: Hybrid Aircraft Energy Management")
    
    print("\nAPPLICATION: Regional aircraft with H₂ fuel cell + CO₂ battery")
    print("DESIGN STRATEGY: CO₂ battery for peak power, H₂ for cruise")
    
    # CO₂ battery for takeoff/climb augmentation
    co2_system = create_example_system(
        co2_mass_kg=200.0,
        cycle_type=CycleType.SUBLIMATION_EXPANDER
    )
    
    perf = co2_system.calculate_system_performance(
        ambient_temp_c=15.0,  # ISA sea level
        heat_source_temp_c=80.0  # Fuel cell waste heat
    )
    
    print(f"\nCO₂ BATTERY SUBSYSTEM:")
    print(f"  Mass: {perf['co2_mass_kg']:.0f} kg")
    print(f"  Electrical Capacity: {perf['electrical_energy_recoverable_kwh']:.1f} kWh")
    print(f"  Peak Power: ~{perf['electrical_energy_recoverable_kwh'] * 4:.0f} kW (15-min discharge)")
    
    # Mission segments
    print(f"\nMISSION PROFILE:")
    
    # Takeoff
    takeoff_power_kw = 50.0
    takeoff_duration_min = 2.0
    takeoff_energy_kwh = takeoff_power_kw * takeoff_duration_min / 60.0
    print(f"  Takeoff: {takeoff_power_kw:.0f} kW × {takeoff_duration_min:.0f} min = {takeoff_energy_kwh:.2f} kWh")
    
    # Climb
    climb_power_kw = 30.0
    climb_duration_min = 10.0
    climb_energy_kwh = climb_power_kw * climb_duration_min / 60.0
    print(f"  Climb: {climb_power_kw:.0f} kW × {climb_duration_min:.0f} min = {climb_energy_kwh:.2f} kWh")
    
    # Total peak energy
    total_peak_kwh = takeoff_energy_kwh + climb_energy_kwh
    print(f"  Total Peak Energy: {total_peak_kwh:.2f} kWh")
    print(f"  CO₂ Battery Coverage: {perf['electrical_energy_recoverable_kwh'] / total_peak_kwh * 100:.0f}%")
    
    # Recharge during cruise
    cruise_duration_h = 2.0
    waste_heat_available_kw = 15.0
    recharge_potential_kwh = waste_heat_available_kw * cruise_duration_h
    print(f"\nRECHARGE DURING CRUISE:")
    print(f"  Cruise Duration: {cruise_duration_h:.1f} hours")
    print(f"  Waste Heat Available: {waste_heat_available_kw:.0f} kW")
    print(f"  Recharge Potential: {recharge_potential_kwh:.1f} kWh")
    print(f"  Required: {perf['recharge_energy_kwh']:.1f} kWh")
    print(f"  ✓ Feasible: {recharge_potential_kwh >= perf['recharge_energy_kwh']}")


def example_4_safety_analysis():
    """Example 4: Safety limits and operational boundaries."""
    print_section_header("EXAMPLE 4: Safety Analysis and Operational Limits")
    
    print("\nSCENARIO: Analyze safety for various operating conditions")
    
    system = create_example_system(co2_mass_kg=100.0)
    
    # Test scenarios
    scenarios = [
        ("Normal Operation", 25.0, 10.0),
        ("High Pressure", 30.0, 150.0),
        ("Extreme Pressure", 30.0, 220.0),  # Exceeds safe limit
        ("Low Temperature", -95.0, 10.0),  # Near embrittlement
        ("Extreme Cold", -110.0, 10.0),  # Exceeds safe limit
        ("Solid in Piping", -75.0, 15.0),  # Risk of blockage
    ]
    
    print(f"\n{'Scenario':<20} {'Temp (°C)':<12} {'Press (bar)':<12} {'Phase':<15} {'Status':<10}")
    print("-" * 80)
    
    for name, temp, pressure in scenarios:
        safety = system.check_safety_limits(temp, pressure)
        status = "✓ SAFE" if safety["is_safe"] else "✗ UNSAFE"
        phase = safety["phase"].upper()
        
        print(f"{name:<20} {temp:<12.1f} {pressure:<12.1f} {phase:<15} {status:<10}")
        
        if safety["warnings"]:
            for warning in safety["warnings"]:
                print(f"  ⚠ {warning}")
    
    # Mass balance check
    print(f"\nMASS BALANCE VERIFICATION:")
    
    initial_mass = 100.0
    test_cases = [
        ("Perfect seal", 100.0, True),
        ("Minor leak", 99.5, True),
        ("Acceptable loss", 99.0, True),
        ("Excessive leak", 95.0, False),
    ]
    
    print(f"\n{'Case':<20} {'Initial (kg)':<15} {'Current (kg)':<15} {'Loss (%)':<12} {'Status':<10}")
    print("-" * 80)
    
    for name, current_mass, expected_ok in test_cases:
        balance = system.verify_mass_balance(initial_mass, current_mass, tolerance_percent=1.0)
        status = "✓ OK" if balance["is_balanced"] else "✗ LEAK"
        
        print(f"{name:<20} {initial_mass:<15.1f} {current_mass:<15.1f} "
              f"{balance['mass_loss_percent']:<12.2f} {status:<10}")


def example_5_design_trade_study():
    """Example 5: Design trade-offs for different mass configurations."""
    print_section_header("EXAMPLE 5: Design Trade Study - Mass vs Performance")
    
    print("\nQUESTION: How does CO₂ mass affect system performance?")
    print("ANALYSIS: Compare systems from 50 kg to 500 kg")
    
    masses = [50, 100, 200, 350, 500]
    
    print(f"\n{'Mass (kg)':<12} {'Energy (kWh)':<15} {'Specific (Wh/kg)':<18} "
          f"{'Volume (L)':<15} {'Efficiency (%)':<15}")
    print("-" * 90)
    
    for mass_kg in masses:
        system = create_example_system(co2_mass_kg=mass_kg)
        perf = system.calculate_system_performance()
        
        volume_liters = mass_kg / system.props.RHO_SOLID * 1000
        
        print(f"{mass_kg:<12.0f} {perf['electrical_energy_recoverable_kwh']:<15.2f} "
              f"{perf['specific_energy_wh_kg']:<18.1f} {volume_liters:<15.1f} "
              f"{perf['discharge_efficiency']*100:<15.1f}")
    
    print("\nOBSERVATION: Specific energy and efficiency independent of scale")
    print("IMPLICATION: System sizing primarily driven by energy requirement")


def example_6_cycle_comparison():
    """Example 6: Compare different thermodynamic cycles."""
    print_section_header("EXAMPLE 6: Cycle Comparison - Sublimation vs sCO₂ Brayton")
    
    print("\nCOMPARISON: Same CO₂ mass, different cycle architectures")
    
    co2_mass = 150.0
    
    # Sublimation cycle
    system_sub = create_example_system(
        co2_mass_kg=co2_mass,
        cycle_type=CycleType.SUBLIMATION_EXPANDER
    )
    perf_sub = system_sub.calculate_system_performance(
        ambient_temp_c=25.0,
        heat_source_temp_c=80.0
    )
    
    # sCO₂ Brayton cycle
    system_sco2 = create_example_system(
        co2_mass_kg=co2_mass,
        cycle_type=CycleType.SCO2_BRAYTON
    )
    perf_sco2 = system_sco2.calculate_system_performance(
        ambient_temp_c=25.0,
        heat_source_temp_c=450.0  # High-temp heat source
    )
    
    print(f"\n{'Metric':<35} {'Sublimation':<20} {'sCO₂ Brayton':<20}")
    print("-" * 80)
    
    metrics = [
        ("CO₂ Mass (kg)", perf_sub["co2_mass_kg"], perf_sco2["co2_mass_kg"]),
        ("Thermal Energy (kWh)", perf_sub["thermal_energy_stored_kwh"], perf_sco2["thermal_energy_stored_kwh"]),
        ("Electrical Energy (kWh)", perf_sub["electrical_energy_recoverable_kwh"], perf_sco2["electrical_energy_recoverable_kwh"]),
        ("Discharge Efficiency (%)", perf_sub["discharge_efficiency"]*100, perf_sco2["discharge_efficiency"]*100),
        ("Round-Trip Efficiency (%)", perf_sub["roundtrip_efficiency"]*100, perf_sco2["roundtrip_efficiency"]*100),
        ("Specific Energy (Wh/kg)", perf_sub["specific_energy_wh_kg"], perf_sco2["specific_energy_wh_kg"]),
    ]
    
    for name, val_sub, val_sco2 in metrics:
        print(f"{name:<35} {val_sub:<20.1f} {val_sco2:<20.1f}")
    
    print(f"\nKEY DIFFERENCES:")
    print(f"  • Storage Temperature: {system_sub.design.storage_temp_c:.0f}°C vs {system_sco2.design.storage_temp_c:.0f}°C")
    print(f"  • Operating Pressure: {system_sub.design.storage_pressure_bar:.0f} vs {system_sco2.design.storage_pressure_bar:.0f} bar")
    print(f"  • Electrical Output: {perf_sco2['electrical_energy_recoverable_kwh'] / perf_sub['electrical_energy_recoverable_kwh']:.1f}× higher")
    print(f"  • Efficiency Gain: +{(perf_sco2['discharge_efficiency'] - perf_sub['discharge_efficiency'])*100:.1f} percentage points")
    
    print(f"\nTRADE-OFFS:")
    print(f"  Sublimation: Simpler, lower pressure, but lower efficiency")
    print(f"  sCO₂ Brayton: Higher efficiency, but requires high-temp heat + high pressure")


def main():
    """Run all examples."""
    print("=" * 80)
    print("CO₂ ENDOCIRCULAR BATTERY SYSTEM - USAGE EXAMPLES")
    print("=" * 80)
    print("\nThis script demonstrates various applications and design considerations")
    print("for CO₂-based energy storage systems.")
    
    try:
        example_1_basic_sublimation_system()
        example_2_sco2_stationary()
        example_3_hybrid_aircraft()
        example_4_safety_analysis()
        example_5_design_trade_study()
        example_6_cycle_comparison()
        
        print_section_header("EXAMPLES COMPLETE")
        print("\nFor more information, see CO2_BATTERY_TECHNICAL_DOCS.md")
        print("For implementation details, see co2_battery_endocircular.py")
        print("For testing, run: pytest test_co2_battery.py -v")
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
