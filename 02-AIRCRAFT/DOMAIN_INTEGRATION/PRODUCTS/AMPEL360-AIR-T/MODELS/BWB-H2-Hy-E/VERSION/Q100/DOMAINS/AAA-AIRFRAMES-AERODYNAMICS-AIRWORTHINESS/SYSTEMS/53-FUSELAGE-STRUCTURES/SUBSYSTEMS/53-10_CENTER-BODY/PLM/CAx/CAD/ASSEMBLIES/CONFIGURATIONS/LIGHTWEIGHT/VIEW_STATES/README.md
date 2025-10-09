# VIEW_STATES — Display and Visualization States

## Purpose

This directory contains saved view states, display configurations, and visualization settings for lightweight assembly configurations.

## Contents

### View State Types
- **Display states**: Graphics quality and tessellation settings
- **Visibility states**: Component visibility configurations
- **Camera views**: Saved camera positions and orientations
- **Section views**: Saved section planes and cuts
- **Exploded views**: Assembly explosion states

## Naming Convention

Use the following pattern:
```
53-10_VIEW_<assembly-name>_<view-type>_<version>.<ext>
```

Examples:
- `53-10_VIEW_CENTER-BODY_low-detail_v01.catview`
- `53-10_VIEW_FRAME-SECTION_exploded_v02.view`
- `53-10_VIEW_SKIN-PANEL_section-cut_v01.state`

## View State Categories

### Performance Views
Optimized for:
- Fast navigation and rotation
- Reduced screen redraw time
- Lower GPU memory usage
- Improved responsiveness

### Review Views
Configured for:
- Design reviews and presentations
- Stakeholder walkthroughs
- Manufacturing reviews
- Assembly sequence visualization

### Analysis Views
Set up for:
- Interference checking
- Clearance verification
- Assembly sequence validation
- Installation studies

## Display Settings

### Graphics Quality
- **Low**: Coarse tessellation, basic shading
- **Medium**: Balanced quality and performance
- **High**: Fine tessellation, enhanced shading

### Visibility Controls
- Show/hide component groups
- Layer management
- Transparency settings
- Color coding schemes

### Camera Presets
- Isometric views
- Front/Top/Side orthographic views
- Custom engineering views
- Assembly sequence views

## File Formats

Different CAD systems store view states differently:
- **CATIA**: `.catview`, embedded in `.CATProduct`
- **NX**: `.view`, `.dsp` files
- **SolidWorks**: Display states in `.sldasm`
- **Creo**: Simplified reps, combined states

## Best Practices

### Creating View States
1. Set up display quality (tessellation, edges, etc.)
2. Configure component visibility
3. Set camera position and orientation
4. Test performance (frame rate, load time)
5. Save with descriptive name
6. Document purpose and use case

### Managing View States
- Create view states for common tasks
- Maintain consistent naming
- Document view state purpose
- Update when assembly changes
- Archive obsolete view states

## Use Cases

### Design Work
- **Fast navigation view**: Minimal graphics for quick pan/zoom/rotate
- **Detail view**: Higher quality for close-up work
- **Assembly view**: Exploded state for understanding structure

### Collaboration
- **Review view**: Optimized for screen sharing and presentations
- **Section view**: Show internal details to stakeholders
- **Sequence view**: Demonstrate assembly/disassembly process

### Documentation
- **Render view**: High-quality graphics for documentation
- **Technical view**: Show specific details or features
- **Comparison view**: Side-by-side configurations

## Performance Optimization

View states should achieve:
- Frame rate: >30 fps for navigation
- Load time: <5 seconds for view switch
- Memory: <2 GB for typical assemblies
- Responsiveness: <100 ms for user interactions

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Suppression states**: [`../SUPPRESSION/`](../SUPPRESSION/)
- **Configuration rules**: [`../RULES/`](../RULES/)
- **Documentation**: [`../DOCS/`](../DOCS/)
