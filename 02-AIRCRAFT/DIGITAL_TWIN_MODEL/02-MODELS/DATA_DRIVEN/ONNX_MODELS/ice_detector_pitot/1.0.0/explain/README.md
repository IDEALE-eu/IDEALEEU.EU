# Model Explainability

This directory contains explainability artifacts for understanding model decisions.

## Files

- **shap_values.npz**: SHAP (SHapley Additive exPlanations) values for feature importance
- **saliency_maps.npz**: Saliency maps showing input sensitivity
- **feature_importance.json**: Ranked feature importance scores

## Explainability Methods

### SHAP Values
SHAP values explain individual predictions by quantifying each feature's contribution to the anomaly score.

### Saliency Maps
Gradient-based saliency maps show which input features the model is most sensitive to.

### Feature Importance
Aggregated importance across the test set, showing which sensors are most critical for ice detection.

## Usage

These artifacts help domain experts understand and validate model behavior, and support certification efforts by providing transparency into model decision-making.

## Top Features (from feature_importance.json)
1. Differential pressure (pitot-static)
2. Pitot heater current
3. Outside air temperature
4. Pitot temperature
5. Airspeed indicated

## Notes

Explainability is particularly important for safety-critical ML models, as it helps build trust and supports validation that the model is learning physically meaningful patterns rather than spurious correlations.
