#!/usr/bin/env python3
"""
Endocircular CO₂ Battery System - Energy Storage Simulation

This module implements a closed-loop CO₂-based energy storage system (dry ice battery).
The system stores energy as solid/liquid CO₂ and recovers it through controlled phase
transitions and expansion cycles.

Key Features:
- Thermodynamic property calculations for CO₂ phases
- Multiple cycle types: sublimation, sCO₂ Brayton, CAES-like
- Energy storage and recovery efficiency modeling
- Safety and operational boundary monitoring
- Mass balance tracking (closed system)

Physical Constants:
- Triple point: 5.185 bar, -56.6°C
- Critical point: 73.8 bar, 31.04°C
- Sublimation at 1 atm: -78.5°C
- Latent heat of sublimation: ~571 kJ/kg (158 Wh/kg)
- Dry ice density: ~1560 kg/m³

Author: IDEALE-EU Energy Systems Team
Version: 1.0.0
Date: 2025-10-23
"""

import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple, Optional


class CO2Phase(Enum):
    """CO₂ phase states."""
    SOLID = "solid"
    LIQUID = "liquid"
    GAS = "gas"
    SUPERCRITICAL = "supercritical"


class CycleType(Enum):
    """Energy recovery cycle types."""
    SUBLIMATION_EXPANDER = "sublimation_expander"
    SCO2_BRAYTON = "sco2_brayton"
    CAES_PNEUMATIC = "caes_pneumatic"
    HYBRID = "hybrid"


@dataclass
class CO2Properties:
    """Thermodynamic properties of CO₂."""
    
    # Constants
    MOLECULAR_WEIGHT = 44.01  # g/mol
    R_SPECIFIC = 188.92  # J/(kg·K), specific gas constant
    
    # Triple point
    T_TRIPLE_C = -56.6  # °C
    P_TRIPLE_BAR = 5.185  # bar
    
    # Critical point
    T_CRITICAL_C = 31.04  # °C
    P_CRITICAL_BAR = 73.8  # bar
    
    # Sublimation at 1 atm
    T_SUBLIMATION_1ATM_C = -78.5  # °C
    
    # Latent heats (kJ/kg)
    L_SUBLIMATION = 571.0  # solid → gas
    L_FUSION = 184.0  # solid → liquid (at triple point)
    L_VAPORIZATION = 387.0  # liquid → gas (approximate)
    
    # Densities (kg/m³)
    RHO_SOLID = 1560.0  # dry ice
    RHO_LIQUID = 1178.0  # at 0°C, ~35 bar
    RHO_GAS_STP = 1.977  # at 0°C, 1 bar
    
    # Specific heats (kJ/(kg·K))
    CP_SOLID = 1.4  # approximate
    CP_LIQUID = 2.0  # approximate
    CP_GAS = 0.844  # at constant pressure, 25°C
    CV_GAS = 0.655  # at constant volume, 25°C
    
    @staticmethod
    def celsius_to_kelvin(temp_c: float) -> float:
        """Convert Celsius to Kelvin."""
        return temp_c + 273.15
    
    @staticmethod
    def kelvin_to_celsius(temp_k: float) -> float:
        """Convert Kelvin to Celsius."""
        return temp_k - 273.15
    
    @staticmethod
    def bar_to_pa(pressure_bar: float) -> float:
        """Convert bar to Pascal."""
        return pressure_bar * 1e5
    
    @staticmethod
    def pa_to_bar(pressure_pa: float) -> float:
        """Convert Pascal to bar."""
        return pressure_pa / 1e5
    
    @classmethod
    def determine_phase(cls, temp_c: float, pressure_bar: float) -> CO2Phase:
        """
        Determine CO₂ phase based on temperature and pressure.
        
        Note: This is a simplified model. For production use, employ CoolProp
        or REFPROP for accurate phase determination along saturation curves.
        
        Args:
            temp_c: Temperature in Celsius
            pressure_bar: Pressure in bar
            
        Returns:
            CO2Phase enum value
        """
        # Supercritical: both T and P above critical point
        if temp_c > cls.T_CRITICAL_C and pressure_bar > cls.P_CRITICAL_BAR:
            return CO2Phase.SUPERCRITICAL
        
        # Below triple point pressure → solid (sublimation region) or gas
        if pressure_bar < cls.P_TRIPLE_BAR:
            if temp_c < cls.T_SUBLIMATION_1ATM_C:
                return CO2Phase.SOLID
            else:
                return CO2Phase.GAS
        
        # Below triple point temperature → solid
        if temp_c < cls.T_TRIPLE_C:
            return CO2Phase.SOLID
        
        # Between triple and critical point
        # Simplified: liquid exists in pressure range between saturation curves
        # For accurate determination, use CoolProp:
        #   import CoolProp.CoolProp as CP
        #   phase = CP.PropsSI('Phase','T',T_K,'P',P_Pa,'CO2')
        if temp_c < cls.T_CRITICAL_C:
            # Rough approximation: liquid exists above ~10 bar in this region
            # This is oversimplified - actual saturation pressure varies with T
            if pressure_bar > 10:
                return CO2Phase.LIQUID
            else:
                return CO2Phase.GAS
        else:
            # Above critical temperature but below critical pressure
            return CO2Phase.GAS


@dataclass
class SystemDesign:
    """CO₂ battery system design parameters."""
    
    co2_mass_kg: float  # Total CO₂ mass in system
    storage_temp_c: float  # Storage temperature (solid/liquid)
    storage_pressure_bar: float  # Storage pressure
    expansion_pressure_bar: float  # Expansion outlet pressure
    expander_efficiency: float  # Mechanical efficiency of expander/turbine
    recuperator_effectiveness: float  # Heat exchanger effectiveness
    liquefaction_cop: float  # Coefficient of performance for recharge
    cycle_type: CycleType  # Type of thermodynamic cycle
    
    def __post_init__(self):
        """Validate design parameters."""
        if self.co2_mass_kg <= 0:
            raise ValueError("CO₂ mass must be positive")
        if not 0 < self.expander_efficiency <= 1.0:
            raise ValueError("Expander efficiency must be between 0 and 1")
        if not 0 < self.recuperator_effectiveness <= 1.0:
            raise ValueError("Recuperator effectiveness must be between 0 and 1")
        if self.liquefaction_cop <= 0:
            raise ValueError("Liquefaction COP must be positive")


class CO2BatterySystem:
    """
    Endocircular CO₂ battery system model.
    
    This class models a closed-loop CO₂ energy storage system where CO₂
    is stored as solid or liquid and expanded through a turbine/expander
    to generate electricity. The system maintains mass balance with no venting.
    """
    
    def __init__(self, design: SystemDesign):
        """
        Initialize CO₂ battery system.
        
        Args:
            design: System design parameters
        """
        self.design = design
        self.props = CO2Properties()
        
        # Validate storage conditions
        storage_phase = self.props.determine_phase(
            design.storage_temp_c,
            design.storage_pressure_bar
        )
        if storage_phase not in [CO2Phase.SOLID, CO2Phase.LIQUID, CO2Phase.SUPERCRITICAL]:
            raise ValueError(
                f"Invalid storage conditions: {storage_phase}. "
                "Storage must be solid, liquid, or supercritical."
            )
    
    def calculate_stored_energy_thermal(self) -> float:
        """
        Calculate total thermal energy stored in the CO₂.
        
        Returns:
            Thermal energy in kWh
        """
        # Use latent heat of sublimation as baseline
        energy_kj = self.design.co2_mass_kg * self.props.L_SUBLIMATION
        energy_kwh = energy_kj / 3600.0
        return energy_kwh
    
    def calculate_stored_energy_density(self) -> float:
        """
        Calculate volumetric energy density.
        
        Returns:
            Energy density in kWh/m³ (thermal)
        """
        volume_m3 = self.design.co2_mass_kg / self.props.RHO_SOLID
        energy_kwh = self.calculate_stored_energy_thermal()
        return energy_kwh / volume_m3
    
    def calculate_expansion_work_ideal(
        self,
        inlet_temp_c: float,
        inlet_pressure_bar: float,
        outlet_pressure_bar: float
    ) -> float:
        """
        Calculate ideal expansion work (isentropic).
        
        Args:
            inlet_temp_c: Inlet temperature in Celsius
            inlet_pressure_bar: Inlet pressure in bar
            outlet_pressure_bar: Outlet pressure in bar
            
        Returns:
            Specific work in kJ/kg
        """
        # Simplified ideal gas expansion work
        # w = cp * T1 * (1 - (P2/P1)^((γ-1)/γ))
        gamma = self.props.CP_GAS / self.props.CV_GAS  # ~1.289
        
        T1_K = self.props.celsius_to_kelvin(inlet_temp_c)
        pressure_ratio = outlet_pressure_bar / inlet_pressure_bar
        
        # Isentropic expansion
        exponent = (gamma - 1) / gamma
        work_kj_per_kg = self.props.CP_GAS * T1_K * (1 - pressure_ratio**exponent)
        
        return work_kj_per_kg
    
    def calculate_cycle_efficiency_sublimation(
        self,
        ambient_temp_c: float = 25.0,
        heat_source_temp_c: float = 80.0
    ) -> Dict[str, float]:
        """
        Calculate efficiency for sublimation + expander cycle.
        
        Args:
            ambient_temp_c: Ambient temperature for heat rejection
            heat_source_temp_c: Heat source temperature for sublimation
            
        Returns:
            Dictionary with efficiency metrics
        """
        # Energy input: latent heat for sublimation
        Q_sublimation = self.props.L_SUBLIMATION  # kJ/kg
        
        # Expansion work (from ~5 bar to 1 bar, at heat source temp)
        w_expansion_ideal = self.calculate_expansion_work_ideal(
            heat_source_temp_c,
            self.design.storage_pressure_bar,
            self.design.expansion_pressure_bar
        )
        
        # Account for expander efficiency
        w_expansion_actual = w_expansion_ideal * self.design.expander_efficiency
        
        # Thermal-to-mechanical efficiency
        eta_thermal = w_expansion_actual / Q_sublimation
        
        # Carnot limit for comparison
        T_hot = self.props.celsius_to_kelvin(heat_source_temp_c)
        T_cold = self.props.celsius_to_kelvin(ambient_temp_c)
        eta_carnot = 1 - (T_cold / T_hot)
        
        # Electrical output (assume generator efficiency ~95%)
        eta_generator = 0.95
        eta_overall = eta_thermal * eta_generator
        
        return {
            "thermal_efficiency": eta_thermal,
            "electrical_efficiency": eta_overall,
            "carnot_efficiency": eta_carnot,
            "specific_work_kj_kg": w_expansion_actual,
            "specific_energy_output_kwh_kg": w_expansion_actual / 3600.0,
        }
    
    def calculate_cycle_efficiency_sco2_brayton(
        self,
        hot_side_temp_c: float = 550.0,
        cold_side_temp_c: float = 35.0,
        compression_ratio: float = 3.0
    ) -> Dict[str, float]:
        """
        Calculate efficiency for supercritical CO₂ Brayton cycle.
        
        Args:
            hot_side_temp_c: Turbine inlet temperature
            cold_side_temp_c: Compressor inlet temperature
            compression_ratio: Pressure ratio
            
        Returns:
            Dictionary with efficiency metrics
        """
        gamma = self.props.CP_GAS / self.props.CV_GAS
        
        # Ideal Brayton efficiency
        exponent = (gamma - 1) / gamma
        eta_brayton_ideal = 1 - (1 / compression_ratio**exponent)
        
        # Account for component efficiencies
        eta_turbine = self.design.expander_efficiency
        eta_compressor = 0.85  # typical compressor efficiency
        epsilon = self.design.recuperator_effectiveness
        
        # Simplified real cycle efficiency
        # With recuperator, efficiency can be significantly higher
        eta_real = eta_brayton_ideal * eta_turbine * (1 + 0.5 * epsilon)
        
        # Typical sCO₂ cycles achieve 40-55% at high temperatures
        eta_real = min(eta_real, 0.55)
        
        # Carnot limit
        T_hot = self.props.celsius_to_kelvin(hot_side_temp_c)
        T_cold = self.props.celsius_to_kelvin(cold_side_temp_c)
        eta_carnot = 1 - (T_cold / T_hot)
        
        return {
            "thermal_efficiency": eta_real,
            "electrical_efficiency": eta_real * 0.95,  # generator
            "carnot_efficiency": eta_carnot,
            "ideal_brayton_efficiency": eta_brayton_ideal,
            "compression_ratio": compression_ratio,
        }
    
    def calculate_roundtrip_efficiency(
        self,
        discharge_efficiency: float,
        recharge_energy_factor: float = None
    ) -> Dict[str, float]:
        """
        Calculate round-trip efficiency (charge + discharge).
        
        Args:
            discharge_efficiency: Electrical efficiency during discharge
            recharge_energy_factor: Optional override for recharge energy
                                   (if None, calculated from liquefaction COP)
            
        Returns:
            Dictionary with round-trip metrics
        """
        # Energy out during discharge (per kg)
        E_out = self.props.L_SUBLIMATION / 3600.0 * discharge_efficiency  # kWh/kg
        
        # Energy in during recharge
        if recharge_energy_factor is None:
            # Use liquefaction COP (Coefficient of Performance)
            # COP = Heat_removed / Work_input
            # For liquefaction: Work = Heat / COP
            Q_removal = self.props.L_SUBLIMATION  # kJ/kg to remove
            E_in = Q_removal / (self.design.liquefaction_cop * 3600.0)  # kWh/kg
        else:
            E_in = E_out / recharge_energy_factor
        
        # Round-trip efficiency
        eta_roundtrip = E_out / E_in if E_in > 0 else 0
        
        return {
            "discharge_energy_kwh_kg": E_out,
            "recharge_energy_kwh_kg": E_in,
            "roundtrip_efficiency": eta_roundtrip,
            "energy_loss_kwh_kg": E_in - E_out,
        }
    
    def calculate_system_performance(
        self,
        ambient_temp_c: float = 25.0,
        heat_source_temp_c: float = 80.0
    ) -> Dict[str, float]:
        """
        Calculate complete system performance metrics.
        
        Args:
            ambient_temp_c: Ambient temperature
            heat_source_temp_c: Available heat source temperature
            
        Returns:
            Comprehensive performance dictionary
        """
        # Storage metrics
        thermal_energy_kwh = self.calculate_stored_energy_thermal()
        energy_density_kwh_m3 = self.calculate_stored_energy_density()
        
        # Cycle efficiency based on type
        if self.design.cycle_type == CycleType.SUBLIMATION_EXPANDER:
            cycle_eff = self.calculate_cycle_efficiency_sublimation(
                ambient_temp_c, heat_source_temp_c
            )
        elif self.design.cycle_type == CycleType.SCO2_BRAYTON:
            cycle_eff = self.calculate_cycle_efficiency_sco2_brayton()
        else:
            # Default to sublimation
            cycle_eff = self.calculate_cycle_efficiency_sublimation(
                ambient_temp_c, heat_source_temp_c
            )
        
        # Electrical energy recoverable
        electrical_energy_kwh = (
            thermal_energy_kwh * cycle_eff["electrical_efficiency"]
        )
        
        # Round-trip efficiency
        roundtrip = self.calculate_roundtrip_efficiency(
            cycle_eff["electrical_efficiency"]
        )
        
        # Specific energy (gravimetric)
        specific_energy_wh_kg = (electrical_energy_kwh * 1000) / self.design.co2_mass_kg
        
        return {
            "co2_mass_kg": self.design.co2_mass_kg,
            "thermal_energy_stored_kwh": thermal_energy_kwh,
            "electrical_energy_recoverable_kwh": electrical_energy_kwh,
            "energy_density_volumetric_kwh_m3": energy_density_kwh_m3,
            "specific_energy_wh_kg": specific_energy_wh_kg,
            "cycle_type": self.design.cycle_type.value,
            "discharge_efficiency": cycle_eff["electrical_efficiency"],
            "roundtrip_efficiency": roundtrip["roundtrip_efficiency"],
            "carnot_efficiency": cycle_eff.get("carnot_efficiency", 0),
            "recharge_energy_kwh": roundtrip["recharge_energy_kwh_kg"] * self.design.co2_mass_kg,
        }
    
    def check_safety_limits(
        self,
        operating_temp_c: float,
        operating_pressure_bar: float
    ) -> Dict[str, any]:
        """
        Check if operating conditions are within safe limits.
        
        Args:
            operating_temp_c: Current operating temperature
            operating_pressure_bar: Current operating pressure
            
        Returns:
            Dictionary with safety status and warnings
        """
        warnings = []
        is_safe = True
        
        # Check for excessive pressure
        MAX_PRESSURE_BAR = 200.0  # typical safe limit for high-pressure systems
        if operating_pressure_bar > MAX_PRESSURE_BAR:
            warnings.append(f"Pressure {operating_pressure_bar} bar exceeds safe limit {MAX_PRESSURE_BAR} bar")
            is_safe = False
        
        # Check for excessively low temperature (embrittlement risk)
        MIN_TEMP_C = -100.0
        if operating_temp_c < MIN_TEMP_C:
            warnings.append(f"Temperature {operating_temp_c}°C below safe limit {MIN_TEMP_C}°C (embrittlement risk)")
            is_safe = False
        
        # Check for solid formation in unwanted areas
        phase = self.props.determine_phase(operating_temp_c, operating_pressure_bar)
        if phase == CO2Phase.SOLID and operating_pressure_bar > self.props.P_TRIPLE_BAR:
            warnings.append("Risk of solid CO₂ formation in piping (blockage hazard)")
            is_safe = False
        
        # Check for supercritical conditions without proper design
        if (phase == CO2Phase.SUPERCRITICAL and 
            self.design.cycle_type != CycleType.SCO2_BRAYTON):
            warnings.append("Supercritical conditions require sCO₂ Brayton cycle design")
        
        return {
            "is_safe": is_safe,
            "warnings": warnings,
            "phase": phase.value,
            "pressure_bar": operating_pressure_bar,
            "temperature_c": operating_temp_c,
        }
    
    def verify_mass_balance(
        self,
        initial_mass_kg: float,
        current_mass_kg: float,
        tolerance_percent: float = 1.0
    ) -> Dict[str, any]:
        """
        Verify mass balance in closed system (no venting).
        
        Args:
            initial_mass_kg: Initial CO₂ mass
            current_mass_kg: Current CO₂ mass in system
            tolerance_percent: Acceptable mass loss percentage
            
        Returns:
            Dictionary with mass balance status
        """
        mass_loss_kg = initial_mass_kg - current_mass_kg
        mass_loss_percent = (mass_loss_kg / initial_mass_kg) * 100
        
        is_balanced = abs(mass_loss_percent) <= tolerance_percent
        
        return {
            "is_balanced": is_balanced,
            "initial_mass_kg": initial_mass_kg,
            "current_mass_kg": current_mass_kg,
            "mass_loss_kg": mass_loss_kg,
            "mass_loss_percent": mass_loss_percent,
            "tolerance_percent": tolerance_percent,
        }


def create_example_system(
    co2_mass_kg: float = 100.0,
    cycle_type: CycleType = CycleType.SUBLIMATION_EXPANDER
) -> CO2BatterySystem:
    """
    Create an example CO₂ battery system with typical parameters.
    
    Args:
        co2_mass_kg: Total CO₂ mass (default 100 kg)
        cycle_type: Type of thermodynamic cycle
        
    Returns:
        Configured CO2BatterySystem instance
    """
    if cycle_type == CycleType.SUBLIMATION_EXPANDER:
        # For sublimation cycle: store as solid, heat to evaporate, expand from higher pressure
        design = SystemDesign(
            co2_mass_kg=co2_mass_kg,
            storage_temp_c=-80.0,  # Dry ice storage (solid phase)
            storage_pressure_bar=10.0,  # Store at elevated pressure for expansion
            expansion_pressure_bar=1.0,  # Expand to atmospheric
            expander_efficiency=0.75,  # 75% turbine efficiency
            recuperator_effectiveness=0.85,  # 85% heat exchanger
            liquefaction_cop=1.5,  # Conservative COP for cryogenic liquefaction
            cycle_type=cycle_type,
        )
    elif cycle_type == CycleType.SCO2_BRAYTON:
        # For sCO₂ Brayton: operate above critical point
        design = SystemDesign(
            co2_mass_kg=co2_mass_kg,
            storage_temp_c=35.0,  # Above critical temperature
            storage_pressure_bar=100.0,  # Well above critical pressure
            expansion_pressure_bar=80.0,  # High-pressure expansion
            expander_efficiency=0.85,  # Higher efficiency for sCO₂ turbine
            recuperator_effectiveness=0.90,  # High-effectiveness recuperator
            liquefaction_cop=2.0,  # Better COP at higher temperatures
            cycle_type=cycle_type,
        )
    else:
        # Default configuration
        design = SystemDesign(
            co2_mass_kg=co2_mass_kg,
            storage_temp_c=-80.0,
            storage_pressure_bar=10.0,
            expansion_pressure_bar=1.0,
            expander_efficiency=0.75,
            recuperator_effectiveness=0.85,
            liquefaction_cop=1.5,
            cycle_type=cycle_type,
        )
    
    return CO2BatterySystem(design)


if __name__ == "__main__":
    # Example usage
    print("=" * 80)
    print("CO₂ ENDOCIRCULAR BATTERY SYSTEM - EXAMPLE CALCULATION")
    print("=" * 80)
    
    # Create system
    system = create_example_system(co2_mass_kg=100.0)
    
    # Calculate performance
    performance = system.calculate_system_performance(
        ambient_temp_c=25.0,
        heat_source_temp_c=80.0
    )
    
    print("\nSYSTEM DESIGN:")
    print(f"  CO₂ Mass: {performance['co2_mass_kg']:.1f} kg")
    print(f"  Cycle Type: {performance['cycle_type']}")
    print(f"  Storage: {system.design.storage_temp_c:.1f}°C, {system.design.storage_pressure_bar:.1f} bar")
    
    print("\nENERGY STORAGE:")
    print(f"  Thermal Energy: {performance['thermal_energy_stored_kwh']:.2f} kWh")
    print(f"  Electrical Energy Recoverable: {performance['electrical_energy_recoverable_kwh']:.2f} kWh")
    print(f"  Volumetric Density: {performance['energy_density_volumetric_kwh_m3']:.1f} kWh/m³")
    print(f"  Specific Energy: {performance['specific_energy_wh_kg']:.1f} Wh/kg")
    
    print("\nEFFICIENCY:")
    print(f"  Discharge Efficiency: {performance['discharge_efficiency']*100:.1f}%")
    print(f"  Round-Trip Efficiency: {performance['roundtrip_efficiency']*100:.1f}%")
    print(f"  Carnot Limit: {performance['carnot_efficiency']*100:.1f}%")
    print(f"  Recharge Energy Required: {performance['recharge_energy_kwh']:.2f} kWh")
    
    print("\nSAFETY CHECK:")
    safety = system.check_safety_limits(system.design.storage_temp_c, system.design.storage_pressure_bar)
    print(f"  Status: {'SAFE' if safety['is_safe'] else 'UNSAFE'}")
    print(f"  Phase: {safety['phase']}")
    if safety['warnings']:
        for warning in safety['warnings']:
            print(f"  Warning: {warning}")
    
    print("\n" + "=" * 80)
