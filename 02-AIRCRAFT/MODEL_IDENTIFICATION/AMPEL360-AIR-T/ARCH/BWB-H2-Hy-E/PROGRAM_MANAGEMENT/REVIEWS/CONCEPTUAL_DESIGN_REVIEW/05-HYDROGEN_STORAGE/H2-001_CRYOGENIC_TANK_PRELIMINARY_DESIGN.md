# H2-001: Cryogenic Tank Preliminary Design
## BWB-H2-HY-E-THERMAL-CRYO-001

**Deliverable ID**: H2-001  
**Deliverable Type**: Tank Design  
**Version**: 1.0 (Template)  
**Date**: 2025-10-24  
**Status**: Draft Template  
**Owner**: Cryogenic Systems Lead  
**UTCS**: TBD

---

## 1. Tank Geometry and Sizing

### 1.1 Tank Configuration
- **Number of tanks**: [X]
- **Tank shape**: [Cylindrical/Spherical/Conformal]
- **Total capacity**: [X] kg H2
- **Operating pressure**: [X] bar
- **Operating temperature**: [X] K (-253°C)

### 1.2 Dimensions
- **Length**: [X] m
- **Diameter**: [X] m
- **Volume**: [X] m³
- **Usable capacity**: [X]% of total volume

### 1.3 Placement within BWB Structure
[Describe tank location and integration into BWB airframe]

#### Location Options Analyzed
1. Center body integration
2. Wing integration
3. Distributed tanks

#### Selected Configuration
[Describe selected placement with rationale]

---

## 2. Material Selection

### 2.1 Tank Structure
#### Materials Considered
- Aluminum alloys (2xxx, 7xxx series)
- Composite materials (carbon fiber, glass fiber)
- Stainless steel
- Titanium alloys

#### Selected Material
- **Primary structure**: [Material]
- **Liner (if composite)**: [Material]
- **Rationale**: [Justification based on strength, weight, cost, thermal properties]

### 2.2 Material Properties
| Property | Value | Units |
|----------|-------|-------|
| Density | | kg/m³ |
| Tensile strength | | MPa |
| Yield strength | | MPa |
| Thermal conductivity | | W/m·K |
| CTE | | μm/m·K |
| Fracture toughness | | MPa·m^0.5 |

---

## 3. Design Pressure and Temperature

### 3.1 Operating Conditions
- **Normal operating pressure**: [X] bar
- **Maximum operating pressure**: [X] bar
- **Operating temperature**: 20 K (-253°C)
- **Maximum temperature**: [X] K

### 3.2 Design Conditions
- **Design pressure**: [X] bar (1.5× operating pressure)
- **Proof pressure**: [X] bar (2.0× operating pressure)
- **Burst pressure**: [X] bar (4.0× operating pressure)

### 3.3 Pressure Vessel Certification
- **Code compliance**: ASME Section VIII, EN 13458, or equivalent
- **Safety factor**: [X]
- **Design life**: [X] cycles / [X] years

---

## 4. Hydrogen Capacity and Density

### 4.1 Storage Capacity
- **Total H2 mass**: [X] kg
- **Usable H2 mass**: [X] kg (accounting for ullage and boil-off)
- **Storage density**: [X] kg/m³
- **Gravimetric density**: [X] wt% (H2 mass / system mass)

### 4.2 Mission Fuel Requirements
| Mission Type | H2 Required | Margin |
|--------------|-------------|---------|
| Short-haul (< 1000 km) | [X] kg | [X]% |
| Medium-haul (1000-3000 km) | [X] kg | [X]% |
| Design mission | [X] kg | [X]% |

---

## 5. Structural Concept

### 5.1 Load-Bearing Configuration
- **Type**: [Load-bearing / Non-load-bearing]
- **Structural integration**: [Description]

### 5.2 Structural Components
- Inner tank wall
- Outer tank wall (if double-wall)
- Insulation system (see H2-002)
- Support structure
- Mounting interfaces

### 5.3 Load Paths
[Describe how loads are transferred from tank to airframe]

#### Design Load Cases
1. Internal pressure (normal operation)
2. Internal pressure + flight loads (maneuver)
3. Internal pressure + flight loads + thermal loads
4. Crash loads
5. Ground handling loads

---

## 6. Crashworthiness and Impact Protection

### 6.1 Crash Protection Strategy
[Describe approach to protect tanks in crash scenarios]

### 6.2 Protective Features
- Crush zones
- Energy-absorbing structures
- Separation from high-energy zones
- Fire protection barriers

### 6.3 Regulatory Compliance
- FAR/CS 25.952 (Fuel system crash resistance)
- Special conditions for cryogenic H2 tanks

---

## 7. Preliminary Weight Estimates

### 7.1 Component Weights
| Component | Mass (kg) | % of Total |
|-----------|-----------|------------|
| Tank structure | | |
| Insulation system | | |
| Internal components | | |
| Mounting hardware | | |
| **Total dry mass** | | **100%** |

### 7.2 System Mass Summary
| Item | Mass (kg) |
|------|-----------|
| Dry tank system | |
| H2 fuel (max) | |
| **Total loaded mass** | |

### 7.3 Weight Comparison
- **Target weight**: [X] kg
- **Estimated weight**: [X] kg
- **Margin**: [X]%

---

## 8. Tank Interfaces

### 8.1 Structural Interfaces
- Mounting points to airframe
- Load transfer mechanisms
- Interface control documents

### 8.2 Fluid Interfaces
- Fill/defuel connections
- Vent connections
- Transfer lines
- Pressure relief valves

### 8.3 Instrumentation Interfaces
- Temperature sensors
- Pressure sensors
- Level sensors
- Leak detection

---

## 9. Manufacturing Considerations

### 9.1 Fabrication Method
[Describe proposed manufacturing process]

### 9.2 Quality Control
- Non-destructive testing methods
- Pressure testing requirements
- Leak testing requirements

### 9.3 Assembly Sequence
[Describe how tank is assembled and integrated]

---

## 10. Analysis and Validation Plan

### 10.1 Structural Analysis
- Finite Element Analysis (FEA)
- Stress analysis
- Fatigue analysis
- Fracture mechanics

### 10.2 Testing Requirements
- Proof pressure test
- Burst pressure test
- Thermal cycle testing
- Fatigue testing
- Leak testing

---

## 11. Trade Studies Conducted

### 11.1 Configuration Trades
[Summarize configuration trade studies]

### 11.2 Material Trades
[Summarize material selection trades]

### 11.3 Selected Configuration Rationale
[Justify final design selections]

---

## 12. Open Issues and TBDs

1. [TBD item 1]
2. [TBD item 2]
3. [TBD item 3]

---

## 13. Next Steps for Preliminary Design Phase

1. Detailed structural analysis
2. Manufacturing process development
3. Supplier selection
4. Prototype fabrication planning

---

## References

- **Insulation System**: [H2-002_INSULATION_SYSTEM_DESIGN_CONCEPT.md](./H2-002_INSULATION_SYSTEM_DESIGN_CONCEPT.md)
- **Fuel System**: [H2-003_FUEL_SYSTEM_SCHEMATIC.md](./H2-003_FUEL_SYSTEM_SCHEMATIC.md)
- **Safety Analysis**: [H2-005_HYDROGEN_SAFETY_ANALYSIS.md](./H2-005_HYDROGEN_SAFETY_ANALYSIS.md)
- **CQH Domain**: [../../../../FAMILY/Q100_STD01/DOMAIN/CQH-CRYOGENICS-QUANTUM-H2/](../../../../FAMILY/Q100_STD01/DOMAIN/CQH-CRYOGENICS-QUANTUM-H2/)

---

**Document Control**  
**Classification**: Internal/Technical  
**Distribution**: Engineering, Manufacturing, Safety  
**Change Control**: Via ECR/ECO process
