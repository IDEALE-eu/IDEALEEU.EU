#!/usr/bin/env python3
"""
Energy Budget Analysis Script

Analyzes H2 fuel consumption, battery state of charge, and energy budget
for digital twin predictions vs. actual flight data.

Author: Analytics Team
Version: 1.0
Date: 2025-01-XX
"""

import argparse
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def load_flight_data(input_file):
    """Load flight log data from CSV file."""
    print(f"Loading flight data from {input_file}...")
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print(f"Loaded {len(df)} records from {df['flight_id'].nunique()} flights")
    return df


def calculate_energy_budget(df):
    """Calculate energy budget components."""
    print("\nCalculating energy budget...")
    
    # H2 fuel cell energy (assume 33.33 kWh/kg H2, 60% efficiency)
    df['h2_energy_kwh'] = df['h2_fuel_kg'] * 33.33 * 0.6
    
    # Battery energy (from SOC and capacity)
    battery_capacity_kwh = 100  # Assumed battery pack capacity
    df['battery_energy_kwh'] = df['battery_soc_percent'] / 100 * battery_capacity_kwh
    
    # Total energy available
    df['total_energy_kwh'] = df['h2_energy_kwh'] + df['battery_energy_kwh']
    
    # Propulsion power demand (calculated from telemetry)
    df['propulsion_power_kw'] = df['thrust_n'] * df['true_airspeed_m_per_s'] / 1000 / 0.85  # Assume 85% prop efficiency
    
    return df


def analyze_flight_segments(df):
    """Analyze energy consumption by flight phase."""
    print("\nAnalyzing flight segments...")
    
    segments = {
        'Taxi': df[df['flight_phase'] == 'taxi'],
        'Takeoff': df[df['flight_phase'] == 'takeoff'],
        'Climb': df[df['flight_phase'] == 'climb'],
        'Cruise': df[df['flight_phase'] == 'cruise'],
        'Descent': df[df['flight_phase'] == 'descent'],
        'Landing': df[df['flight_phase'] == 'landing']
    }
    
    segment_summary = []
    for phase, data in segments.items():
        if len(data) > 0:
            avg_power = data['propulsion_power_kw'].mean()
            duration_hours = len(data) * 1 / 3600  # Assuming 1 Hz data
            energy_kwh = avg_power * duration_hours
            
            segment_summary.append({
                'Phase': phase,
                'Duration (min)': duration_hours * 60,
                'Avg Power (kW)': avg_power,
                'Energy (kWh)': energy_kwh,
                'H2 Consumed (kg)': energy_kwh / (33.33 * 0.6),
                'Samples': len(data)
            })
    
    summary_df = pd.DataFrame(segment_summary)
    print("\n" + summary_df.to_string(index=False))
    
    return summary_df


def compare_prediction_vs_actual(df):
    """Compare predicted vs actual energy consumption."""
    print("\nComparing predictions vs actuals...")
    
    if 'h2_fuel_kg_pred' in df.columns and 'h2_fuel_kg_actual' in df.columns:
        pred_error = df['h2_fuel_kg_pred'] - df['h2_fuel_kg_actual']
        pred_error_pct = (pred_error / df['h2_fuel_kg_actual']) * 100
        
        print(f"  Prediction Error Statistics:")
        print(f"    Mean Error: {pred_error.mean():.3f} kg ({pred_error_pct.mean():.2f}%)")
        print(f"    Std Dev: {pred_error.std():.3f} kg")
        print(f"    RMSE: {np.sqrt((pred_error**2).mean()):.3f} kg")
        print(f"    Max Over-prediction: {pred_error.max():.3f} kg")
        print(f"    Max Under-prediction: {pred_error.min():.3f} kg")
        
        return pred_error, pred_error_pct
    else:
        print("  Warning: Prediction data not available")
        return None, None


def plot_energy_budget(df, segment_summary, output_dir):
    """Generate energy budget visualizations."""
    print("\nGenerating plots...")
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Plot 1: Energy by flight phase
    fig, ax = plt.subplots(figsize=(10, 6))
    phases = segment_summary['Phase']
    energy = segment_summary['Energy (kWh)']
    ax.bar(phases, energy, color='steelblue', edgecolor='black')
    ax.set_xlabel('Flight Phase')
    ax.set_ylabel('Energy Consumption (kWh)')
    ax.set_title('Energy Budget by Flight Phase')
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'energy_by_phase.png', dpi=300)
    print(f"  Saved: {output_dir / 'energy_by_phase.png'}")
    
    # Plot 2: H2 fuel and battery over time (for first flight)
    first_flight = df[df['flight_id'] == df['flight_id'].iloc[0]]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # H2 fuel
    ax1.plot(first_flight['timestamp'], first_flight['h2_fuel_kg'], 
             linewidth=2, color='blue', label='H₂ Remaining')
    ax1.set_ylabel('H₂ Fuel (kg)')
    ax1.set_title('H₂ Fuel and Battery SOC Over Flight')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Battery SOC
    ax2.plot(first_flight['timestamp'], first_flight['battery_soc_percent'], 
             linewidth=2, color='green', label='Battery SOC')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Battery SOC (%)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fuel_battery_timeline.png', dpi=300)
    print(f"  Saved: {output_dir / 'fuel_battery_timeline.png'}")
    
    plt.close('all')


def generate_report(df, segment_summary, output_dir):
    """Generate energy budget report."""
    print("\nGenerating report...")
    
    output_dir = Path(output_dir)
    report_file = output_dir / 'energy_budget_report.txt'
    
    with open(report_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("DIGITAL TWIN ENERGY BUDGET ANALYSIS REPORT\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Flight Data: {df['flight_id'].nunique()} flights, {len(df)} records\n")
        f.write("\n")
        
        f.write("SUMMARY STATISTICS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Total H₂ Consumed: {df.groupby('flight_id')['h2_fuel_kg'].first().sum():.2f} kg\n")
        f.write(f"Average per Flight: {df.groupby('flight_id')['h2_fuel_kg'].first().mean():.2f} kg\n")
        f.write(f"Total Energy: {df['total_energy_kwh'].sum():.2f} kWh\n")
        f.write(f"Average Power: {df['propulsion_power_kw'].mean():.2f} kW\n")
        f.write("\n")
        
        f.write("ENERGY BY FLIGHT PHASE\n")
        f.write("-" * 80 + "\n")
        f.write(segment_summary.to_string(index=False))
        f.write("\n\n")
        
        f.write("RECOMMENDATIONS\n")
        f.write("-" * 80 + "\n")
        f.write("1. Monitor climb phase energy consumption - highest power demand\n")
        f.write("2. Optimize cruise altitude/speed for fuel efficiency\n")
        f.write("3. Consider regenerative descent (if applicable)\n")
        f.write("4. Calibrate model if prediction error exceeds 5%\n")
        f.write("\n")
    
    print(f"  Report saved: {report_file}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Analyze energy budget for digital twin predictions'
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Input CSV file with flight data'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='./results',
        help='Output directory for results (default: ./results)'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("DIGITAL TWIN ENERGY BUDGET ANALYSIS")
    print("=" * 80)
    
    # Load data
    df = load_flight_data(args.input)
    
    # Calculate energy budget
    df = calculate_energy_budget(df)
    
    # Analyze flight segments
    segment_summary = analyze_flight_segments(df)
    
    # Compare prediction vs actual
    compare_prediction_vs_actual(df)
    
    # Generate plots
    plot_energy_budget(df, segment_summary, args.output)
    
    # Generate report
    generate_report(df, segment_summary, args.output)
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
