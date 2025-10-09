# ATA-75 BLEED AIR — Integration View

## Functional Overview
Bleed air system for BWB H₂ hybrid-electric configuration. Minimal bleed air usage due to electric architecture, primarily for anti-ice and environmental control.

## Key Dependencies
- **ATA-21**: Integration with thermal management
- **ATA-30**: Anti-ice system supply
- **ATA-36**: ECS pressurization backup
- **ATA-71**: Engine bleed air extraction (if applicable)
- **ATA-92**: EWIS for bleed air control

## Operating Modes
- Ground: System checks
- Flight: Anti-ice and ECS support as needed
- Emergency: Isolation and safety

## Integration Points
See INTERFACE_MATRIX for detailed cross-system interfaces.

## Note
In this hybrid-electric architecture, bleed air usage is minimized. Electric thermal management is primary.
