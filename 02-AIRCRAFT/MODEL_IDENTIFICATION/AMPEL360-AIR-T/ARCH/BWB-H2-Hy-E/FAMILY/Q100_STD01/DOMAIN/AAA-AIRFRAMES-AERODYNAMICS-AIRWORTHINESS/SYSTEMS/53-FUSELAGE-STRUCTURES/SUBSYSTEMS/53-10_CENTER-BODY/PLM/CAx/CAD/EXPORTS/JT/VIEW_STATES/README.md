# VIEW_STATES — Saved Viewing Configurations

## Purpose

Storage for saved view states and viewpoint configurations for JT files. These define camera positions, visibility settings, and display modes for consistent viewing.

## What to Store

- Saved viewpoints and camera positions
- Section view definitions
- Visibility state configurations
- Display mode settings
- Review-specific views
- Standard viewing configurations

## Content Types

### Viewpoints
- Standard views (front, top, side, isometric)
- Key feature views
- Interface views
- Detail views
- Exploded views

### Section Views
- Cutting plane definitions
- Internal structure views
- System interface sections
- Assembly sequence views

### Display States
- Component visibility settings
- Color/transparency schemes
- Measurement and annotation visibility

## Usage

Use view states for:
- Consistent review presentations
- Standard visualization templates
- Training materials
- Documentation illustrations
- Automated report generation

## File Format

View states may be stored as:
- JT viewpoint data (embedded in JT files)
- Separate configuration files
- XML/JSON view definitions
- Viewer-specific settings

## Related Directories

- [`../CONFIGURATIONS/REVIEW/`](../CONFIGURATIONS/REVIEW/) — Review packages
- [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly files
- [`../TEMPLATES/`](../TEMPLATES/) — Template files
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Define standard views for common reviews
- Document view state purpose
- Use consistent naming
- Version control view definitions
- Share view states with stakeholders
