# 30-20 HEATERS – CAx DATA MANAGEMENT

This directory contains digital engineering artifacts for the anti-ice/anti-fog heater subsystem, supporting design, integration, verification, and sustainment of flight-qualified thermal control elements.

## CAD (Computer-Aided Design)
- 3D models of heater trace patterns and flexible heater assemblies
- Mounting interfaces with optical windows, TPS, and structural substrates
- Bondline and thermal interface material (TIM) definitions
- **Deliverables:** STEP (AP203), IGES, annotated PDF drawings

## CAE (Computer-Aided Engineering)
- Steady-state and transient thermal analyses (power-on/off scenarios)
- Power density and heat flux distribution studies
- Thermal-vacuum and survival environment simulations
- **Non-geometric data:** `CAE/DATA/analisis_termico/` (solver inputs, material properties, results summaries)

## CAM (Computer-Aided Manufacturing)
- NC programs for laser cutting, etching, or forming of heater foils
- Adhesive dispensing and bonding trajectories (e.g., for Kapton heaters)
- **Deliverables:** ISO-compliant NC code, manufacturing process plans

## CAI (Computer-Aided Integration)
- Integration fixtures for heater bonding and electrical termination
- Power and control interface definitions (linked to Systems 21 and 42)
- Harness routing and connector mating procedures
- **Deliverables:** ICDs (Power & Signal), integration work instructions

## CAV (Computer-Aided Validation)
- Thermal performance test fixtures (e.g., cold plate + vacuum chamber setups)
- Hardware-in-the-Loop (HIL) environments for controller validation
- Acceptance test procedures (power cycling, thermal response)
- **Deliverables:** test configurations, validation procedures

## CAP (Computer-Aided Process Planning)
- Bonding process plans for heater-to-substrate attachment
- Power-on sequencing and checkout procedures
- Environmental stress screening (ESS) protocols
- **Deliverables:** work instructions, process flow diagrams

## CAS (Computer-Aided Service and Sustainment)
- Heater replacement procedures (orbital or ground-based)
- Diagnostic troubleshooting flowcharts (open circuit, short, degraded performance)
- Configuration management for field upgrades
- **Deliverables:** MRO manuals, service bulletins

## CMP (Computer-Aided Compliance and Certification)
- Dielectric withstand test evidence (hipot testing)
- Thermal performance validation reports (steady-state and transient)
- Material outgassing compliance (ASTM E595)
- **Deliverables:** qualification certificates, test logs
