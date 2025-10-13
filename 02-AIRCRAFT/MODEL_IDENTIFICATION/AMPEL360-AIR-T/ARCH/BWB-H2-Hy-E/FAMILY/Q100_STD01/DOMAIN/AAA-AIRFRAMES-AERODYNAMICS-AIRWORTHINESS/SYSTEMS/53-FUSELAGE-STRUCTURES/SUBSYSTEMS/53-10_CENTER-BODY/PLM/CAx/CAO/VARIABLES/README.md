# VARIABLES — Design Variables

## Purpose
Definition and management of design variables for structural optimization of the center body.

## Subdirectories

### [GEOMETRY/](GEOMETRY/) — Geometric Design Variables
Parametric geometry definitions:
- Shell thickness distributions
- Stringer/frame spacing and dimensions
- Panel dimensions and curvatures
- Reinforcement locations
- Cutout positions and sizes

### [LAYUP/](LAYUP/) — Composite Layup Variables
Composite material layup optimization:
- Ply orientations (0°, ±45°, 90°)
- Ply thicknesses
- Stacking sequences
- Ply drop-off locations
- Hybrid material configurations

### [GAUGES/](GAUGES/) — Thickness and Sizing Variables
Material thickness and sizing parameters:
- Skin thickness distributions
- Stiffener dimensions (height, width, thickness)
- Doubler thicknesses
- Splice plate dimensions
- Local reinforcement sizing

### [FASTENERS/](FASTENERS/) — Fastener Design Variables
Mechanical fastener parameters:
- Fastener type and diameter
- Fastener spacing and patterns
- Edge distances
- Joint configurations
- Bonding vs. mechanical attachment trade-offs

## Guidelines
- Define realistic bounds for all variables
- Consider manufacturing constraints
- Document discrete vs. continuous variables
- Link variables to CAD/CAE models
- Maintain consistent units
- Update when design space changes
