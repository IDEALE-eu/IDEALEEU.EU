# BWB-H2-Hy-E Integration Guide

**Version:** 1.0.0  
**Date:** 2025-10-23  
**Audience:** System Integrators, Maintenance Engineers, Software Developers

---

## Quick Start

This guide shows how to integrate BWB-H2-Hy-E architecture components with the IDEALE-EU platform.

---

## Prerequisites

### Software Requirements
```bash
# Python 3.11+
python --version  # Should show 3.11 or higher

# Navigate to BWB-H2-Hy-E directory
cd 00-PROGRAM/STANDARDS/02-AIRCRAFT/BWB-H2-Hy-E

# Install testing dependencies
pip install -r requirements-test.txt

# Verify installation
pytest tests/ -v
```

### Knowledge Requirements
- Familiarity with UTCS framework
- Understanding of TFA domain classification
- Knowledge of AAMMPP digital passport system
- Basic YAML and JSON Schema experience

---

## Integration Workflows

### 1. Creating a Component Digital Passport

**Use Case:** Register a new hydrogen storage tank in the system.

**Steps:**

1. **Copy the appropriate template**
```bash
cd 00-PROGRAM/STANDARDS/02-AIRCRAFT/BWB-H2-Hy-E
cp digital-passports/templates/hydrogen-storage-tank-passport.yaml \
   /path/to/instance/tank-001-passport.yaml
```

2. **Fill in the placeholder values**
```yaml
# Replace {TANK_ID} with actual ID, e.g., "001"
# Replace {SERIAL_NUMBER} with actual serial, e.g., "HT-BWB-2025-001"
# Replace {YYYY-MM-DD} with actual dates
# Replace {OEM_NAME} with manufacturer name
```

3. **Validate against schema**
```python
import yaml
import jsonschema

# Load schema
with open('schemas/hydrogen-subsystem.yaml') as f:
    schema = yaml.safe_load(f)

# Load instance data
with open('/path/to/instance/tank-001-passport.yaml') as f:
    data = yaml.safe_load(f)

# Validate
try:
    jsonschema.validate(instance=data, schema=schema)
    print("✓ Valid passport")
except jsonschema.ValidationError as e:
    print(f"✗ Validation error: {e.message}")
```

4. **Register in AAMMPP**
```bash
# Using AAMMPP API (example)
curl -X POST https://aammpp.idealeeu.eu/api/v1/passports \
  -H "Content-Type: application/yaml" \
  --data-binary @tank-001-passport.yaml
```

### 2. Executing a Maintenance Workflow

**Use Case:** Perform pre-flight safety interlock verification.

**Steps:**

1. **Load workflow definition**
```python
import yaml

with open('maintenance-workflows/safety-interlock-verification.yaml') as f:
    workflow = yaml.safe_load(f)

print(f"Workflow: {workflow['workflow_name']}")
print(f"Duration: {sum(step['duration_minutes'] for step in workflow['steps'])} minutes")
```

2. **Verify prerequisites**
```python
# Check technician certification
technician_id = "TECH-H2-042"
required_certs = workflow['personnel_requirements'][0]['certifications']

# Check tool calibration
for tool in workflow['equipment_required']:
    if tool['calibration_required']:
        # Verify calibration date
        print(f"Tool {tool['name']} requires calibration within {tool['calibration_interval_days']} days")
```

3. **Execute steps sequentially**
```python
for step in workflow['steps']:
    print(f"\n--- {step['step_name']} ---")
    print(f"Duration: {step['duration_minutes']} minutes")
    
    # Present actions to technician
    for action in step['actions']:
        print(f"  • {action}")
    
    # Wait for technician confirmation
    # Record test data
    # Validate acceptance criteria
    # Require sign-off
```

4. **Update digital passport**
```python
# Record maintenance activity in UTCS
maintenance_record = {
    "date": "2025-10-23T15:30:00Z",
    "type": "inspection",
    "workflow_id": "BWB-H2-HY-E-SAFETY-INTERLOCK-VERIFY",
    "technician": "TECH-H2-042",
    "result": "passed",
    "notes": "All safety interlocks verified operational"
}

# Append to passport maintenance_history
# Update UTCS digital passport
```

### 3. Performance Monitoring & Degradation Tracking

**Use Case:** Track fuel cell stack performance degradation.

**Steps:**

1. **Run baseline performance test**
```python
# Load workflow
with open('maintenance-workflows/fuel-cell-degradation-tracking.yaml') as f:
    workflow = yaml.safe_load(f)

# Execute performance test
test_results = {
    "polarization_curve": [...],  # Voltage vs. current data
    "peak_power_kw": 248.5,
    "efficiency_percent": 54.2,
    "temperature_distribution": [...],
    "h2_consumption_rate": 25.0  # kg/h
}
```

2. **Analyze degradation**
```python
# Retrieve historical performance
historical_data = get_fc_performance_history("FC-PEM-001")

# Calculate degradation rate
initial_power = 250.0  # kW
current_power = 248.5  # kW
operating_hours = 500.0

# Guard against division by zero
if operating_hours > 0:
    degradation_percent = ((initial_power - current_power) / initial_power) * 100
    degradation_rate_per_1000h = (degradation_percent / operating_hours) * 1000
    
    print(f"Degradation rate: {degradation_rate_per_1000h:.2f}%/1000h")
    
    # Predict remaining life
    if degradation_rate_per_1000h > 0 and current_power < initial_power * 0.85:
        remaining_life_hours = ((initial_power * 0.85) - current_power) / (degradation_rate_per_1000h / 1000 * initial_power)
        if remaining_life_hours > 0:
            print(f"Estimated remaining life: {remaining_life_hours:.0f} hours")
    elif current_power >= initial_power * 0.85:
        print("Component above minimum threshold - no replacement needed yet")
else:
    print("⚠ No operating hours recorded yet - cannot calculate degradation")
```

3. **Make maintenance decision**
```python
# Apply decision matrix from workflow
if degradation_rate_per_1000h > 1.0:
    print("⚠ Increase monitoring frequency to 50 flight hours")
elif current_power < initial_power * 0.85:
    print("⚠ Schedule stack replacement")
elif current_power < initial_power * 0.80:
    print("🚫 Ground aircraft - immediate replacement required")
else:
    print("✓ Continue normal operations")
```

### 4. Schema Validation in CI/CD

**Use Case:** Validate all digital passports in CI pipeline.

**GitHub Actions Example:**

```yaml
# .github/workflows/validate-bwb-h2-hy-e.yml
name: Validate BWB-H2-Hy-E Components

on:
  push:
    paths:
      - 'data/bwb-h2-hy-e/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          cd 00-PROGRAM/STANDARDS/02-AIRCRAFT/BWB-H2-Hy-E
          pip install -r requirements-test.txt
      
      - name: Run schema validation tests
        run: |
          cd 00-PROGRAM/STANDARDS/02-AIRCRAFT/BWB-H2-Hy-E
          pytest tests/ -v --cov=schemas --cov-fail-under=95
      
      - name: Validate all passport instances
        run: |
          python scripts/validate_all_passports.py \
            --schema-dir 00-PROGRAM/STANDARDS/02-AIRCRAFT/BWB-H2-Hy-E/schemas \
            --instance-dir data/bwb-h2-hy-e
```

---

## API Integration

### REST API Examples

#### Register Component
```bash
POST /api/v1/components/bwb-h2-hy-e
Content-Type: application/yaml

utcs_ref: "UTCS-BWB-H2-HY-E-CQH-H2_TANK-001@1.0.0"
...
```

#### Query Component Status
```bash
GET /api/v1/components/UTCS-BWB-H2-HY-E-CQH-H2_TANK-001

Response:
{
  "utcs_ref": "UTCS-BWB-H2-HY-E-CQH-H2_TANK-001@1.0.0",
  "lifecycle_state": "CB",
  "current_level_kg": 142.5,
  "safety_status": "operational"
}
```

#### Schedule Maintenance
```bash
POST /api/v1/maintenance/schedule
Content-Type: application/json

{
  "workflow_id": "BWB-H2-HY-E-SAFETY-INTERLOCK-VERIFY",
  "component_utcs_ref": "UTCS-BWB-H2-HY-E-CQH-H2_TANK-001@1.0.0",
  "scheduled_date": "2025-10-24T08:00:00Z",
  "technician_id": "TECH-H2-042"
}
```

---

## Common Integration Patterns

### Pattern 1: Sensor Data Integration

**Scenario:** Real-time monitoring of hydrogen tank pressure and temperature.

```python
# Sensor data ingestion
def ingest_tank_sensor_data(tank_id, sensor_data):
    """Update tank status with sensor readings."""
    
    # Validate sensor data structure
    required_fields = ['pressure_bar', 'temperature_k']
    if not all(field in sensor_data for field in required_fields):
        raise ValueError(f"Missing required sensor data fields: {required_fields}")
    
    # Validate sensor data ranges
    if sensor_data['pressure_bar'] > get_tank_max_pressure(tank_id):
        trigger_over_pressure_alarm(tank_id)
    
    if sensor_data['temperature_k'] > get_tank_max_temp(tank_id):
        trigger_over_temperature_alarm(tank_id)
    
    # Update digital passport
    update_passport_field(
        utcs_ref=f"UTCS-BWB-H2-HY-E-CQH-H2_TANK-{tank_id}@1.0.0",
        field_path="hydrogen_storage.storage_pressure.current_bar",
        value=sensor_data['pressure_bar']
    )
```

### Pattern 2: Lifecycle State Transitions

**Scenario:** Component moves from QS to CB state.

```python
def transition_component_state(utcs_ref, new_state, evidence):
    """Transition component lifecycle state with evidence."""
    
    # Validate transition
    current_state = get_component_state(utcs_ref)
    valid_transitions = {
        "QS": ["FWD"],
        "FWD": ["UE"],
        "UE": ["FE", "CB"],
        "FE": ["CB"],
        "CB": ["QB"],
        "QB": ["CB"]
    }
    
    if new_state not in valid_transitions.get(current_state, []):
        raise ValueError(f"Invalid transition: {current_state} → {new_state}")
    
    # Record evidence
    record_qr_evidence(utcs_ref, evidence)
    
    # Update passport
    update_passport_field(
        utcs_ref=utcs_ref,
        field_path="lifecycle_state",
        value=new_state
    )
```

### Pattern 3: Cross-Component Dependencies

**Scenario:** Fuel cell depends on hydrogen supply and cooling.

```python
def check_fuel_cell_dependencies(fc_utcs_ref):
    """Verify all dependencies operational before fuel cell startup."""
    
    dependencies = get_component_dependencies(fc_utcs_ref)
    
    # Validate dependencies structure
    required_deps = ['h2_tank', 'cooling_system']
    if not all(dep in dependencies for dep in required_deps):
        return False, f"Missing required dependencies: {required_deps}"
    
    # Check hydrogen supply
    try:
        h2_tank_status = get_component_status(dependencies['h2_tank'])
        if h2_tank_status['current_level_kg'] < 10.0:
            return False, "Insufficient hydrogen supply"
    except KeyError as e:
        return False, f"Invalid H2 tank status data: {e}"
    
    # Check cooling system
    try:
        cooling_status = get_component_status(dependencies['cooling_system'])
        if cooling_status['coolant_flow_lpm'] < 40.0:
            return False, "Insufficient coolant flow"
    except KeyError as e:
        return False, f"Invalid cooling system status data: {e}"
    
    # Check safety interlocks
    interlock_status = check_safety_interlocks(fc_utcs_ref)
    if not interlock_status.get('all_armed', False):
        return False, "Safety interlocks not armed"
    
    return True, "All dependencies operational"
```

---

## Troubleshooting

### Issue: Schema Validation Fails

**Symptom:** `jsonschema.ValidationError` when validating passport

**Solution:**
1. Check required fields are present
2. Verify enum values match exactly (case-sensitive)
3. Ensure numeric values within min/max constraints
4. Validate UTCS reference pattern matches schema

```python
# Debug validation error
try:
    jsonschema.validate(instance=data, schema=schema)
except jsonschema.ValidationError as e:
    print(f"Field: {'.'.join(str(p) for p in e.absolute_path)}")
    print(f"Error: {e.message}")
    print(f"Expected: {e.schema}")
```

### Issue: Test Coverage Below 95%

**Symptom:** `pytest --cov-fail-under=95` fails

**Solution:**
1. Add tests for uncovered schema properties
2. Test both valid and invalid data
3. Add integration tests for cross-schema references

```bash
# Generate coverage report
pytest tests/ --cov=schemas --cov-report=html
# Open htmlcov/index.html to see uncovered lines
```

### Issue: Workflow Execution Timeout

**Symptom:** Maintenance workflow takes longer than expected

**Solution:**
1. Check personnel availability and certification
2. Verify tool calibration current
3. Review step dependencies and prerequisites
4. Consider parallel execution where safe

---

## Best Practices

1. **Always validate before committing**: Run `pytest tests/` before pushing changes
2. **Use templates consistently**: Don't modify template structure without schema update
3. **Version control passports**: Track passport changes in UTCS version history
4. **Automate monitoring**: Set up automated alerts for critical thresholds
5. **Document deviations**: Any non-standard maintenance must be documented in UTCS

---

## Support

- **Technical Issues**: Open GitHub issue with label `bwb-h2-hy-e`
- **Schema Questions**: Contact Configuration Management Board
- **Integration Support**: Email architecture@idealeeu.eu
- **Emergency**: Follow hydrogen safety emergency procedures in workflow

---

**Document Version:** 1.0.0  
**Last Updated:** 2025-10-23  
**Next Review:** 2026-01-23
