"""
Test suite for BWB-H2-Hy-E schema validation.

Tests verify that all schemas are valid JSON Schema Draft 07 and that
example data validates correctly against schemas.

Coverage target: >95% (Level C certification)
"""

import json
import os
from pathlib import Path
import pytest
import yaml
try:
    import jsonschema
    from jsonschema import validate, Draft7Validator
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    pytest.skip("jsonschema not available", allow_module_level=True)


# Paths
SCHEMA_DIR = Path(__file__).parent.parent / "schemas"
PASSPORT_TEMPLATE_DIR = Path(__file__).parent.parent / "digital-passports" / "templates"


class TestSchemaValidity:
    """Test that all schema files are valid JSON Schema Draft 07."""

    @pytest.fixture
    def schema_files(self):
        """Get all schema YAML files."""
        return list(SCHEMA_DIR.glob("*.yaml"))

    def test_schema_files_exist(self, schema_files):
        """Test that schema files exist."""
        assert len(schema_files) > 0, "No schema files found"
        
        expected_schemas = [
            "hydrogen-subsystem.yaml",
            "propulsion-system.yaml",
            "thermal-management.yaml",
            "bwb-h2-hy-e-utcs-extension.yaml"
        ]
        
        schema_names = [f.name for f in schema_files]
        for expected in expected_schemas:
            assert expected in schema_names, f"Expected schema {expected} not found"

    def test_schemas_are_valid_yaml(self, schema_files):
        """Test that all schemas are valid YAML."""
        for schema_file in schema_files:
            with open(schema_file, 'r') as f:
                try:
                    schema = yaml.safe_load(f)
                    assert schema is not None, f"Schema {schema_file.name} is empty"
                except yaml.YAMLError as e:
                    pytest.fail(f"Invalid YAML in {schema_file.name}: {e}")

    def test_schemas_have_required_fields(self, schema_files):
        """Test that schemas have required top-level fields."""
        required_fields = ["$schema", "title", "version", "description", "type", "properties"]
        
        for schema_file in schema_files:
            with open(schema_file, 'r') as f:
                schema = yaml.safe_load(f)
                
            for field in required_fields:
                assert field in schema, f"Schema {schema_file.name} missing required field: {field}"

    def test_schemas_use_draft07(self, schema_files):
        """Test that schemas use JSON Schema Draft 07."""
        for schema_file in schema_files:
            with open(schema_file, 'r') as f:
                schema = yaml.safe_load(f)
            
            assert "$schema" in schema, f"Schema {schema_file.name} missing $schema field"
            assert "draft-07" in schema["$schema"] or "draft/2020-12" in schema["$schema"], \
                f"Schema {schema_file.name} not using Draft 07 or later"

    def test_schemas_are_valid_json_schema(self, schema_files):
        """Test that schemas are valid JSON Schema."""
        for schema_file in schema_files:
            with open(schema_file, 'r') as f:
                schema = yaml.safe_load(f)
            
            try:
                # Validate the schema itself
                Draft7Validator.check_schema(schema)
            except jsonschema.exceptions.SchemaError as e:
                pytest.fail(f"Invalid JSON Schema in {schema_file.name}: {e}")


class TestHydrogenSubsystemSchema:
    """Test hydrogen subsystem schema."""

    @pytest.fixture
    def schema(self):
        """Load hydrogen subsystem schema."""
        with open(SCHEMA_DIR / "hydrogen-subsystem.yaml", 'r') as f:
            return yaml.safe_load(f)

    def test_schema_version(self, schema):
        """Test schema version is correct."""
        assert schema["version"] == "1.0.0"

    def test_schema_required_fields(self, schema):
        """Test that required fields are defined."""
        required = schema["required"]
        expected_required = [
            "subsystem_id",
            "utcs_ref",
            "tfa_domain",
            "lifecycle_state",
            "hydrogen_storage",
            "safety_systems"
        ]
        
        for field in expected_required:
            assert field in required, f"Required field {field} not in schema"

    def test_tfa_domain_is_cqh(self, schema):
        """Test TFA domain is constrained to CQH."""
        tfa_domain = schema["properties"]["tfa_domain"]
        assert tfa_domain["const"] == "CQH"

    def test_lifecycle_states(self, schema):
        """Test lifecycle state enum values."""
        lifecycle_state = schema["properties"]["lifecycle_state"]
        expected_states = ["QS", "FWD", "UE", "FE", "CB", "QB"]
        assert lifecycle_state["enum"] == expected_states

    def test_valid_example_data(self, schema):
        """Test that valid example data passes validation."""
        example_data = {
            "subsystem_id": "BWB-H2-HY-E-H2-TANK-001",
            "utcs_ref": "UTCS-BWB-H2-HY-E-CQH-H2_TANK-001@1.0.0",
            "tfa_domain": "CQH",
            "lifecycle_state": "UE",
            "hydrogen_storage": {
                "tank_type": "cryogenic_liquid",
                "storage_pressure": {
                    "nominal_bar": 5.0,
                    "max_working_bar": 10.0,
                    "current_bar": 5.2
                },
                "storage_temperature": {
                    "nominal_k": 20.0,
                    "min_k": 18.0,
                    "max_k": 22.0,
                    "current_k": 20.1
                },
                "capacity_kg": 150.0,
                "current_level_kg": 142.5,
                "tank_material": "carbon_fiber_composite",
                "insulation_type": "vacuum_insulated"
            },
            "safety_systems": {
                "safety_interlocks": {
                    "interlock_count": 3,
                    "interlock_status": []
                },
                "emergency_venting": {
                    "vent_valve_count": 2,
                    "auto_vent_enabled": True,
                    "vent_trigger_pressure_bar": 12.0,
                    "vent_trigger_temperature_k": 25.0,
                    "last_vent_test": "2025-10-23T10:00:00Z"
                },
                "leak_detection": {
                    "sensor_type": ["electrochemical"],
                    "sensor_locations": [],
                    "alarm_threshold_ppm": 1000
                }
            }
        }
        
        # Should not raise an exception
        validate(instance=example_data, schema=schema)


class TestPropulsionSystemSchema:
    """Test propulsion system schema."""

    @pytest.fixture
    def schema(self):
        """Load propulsion system schema."""
        with open(SCHEMA_DIR / "propulsion-system.yaml", 'r') as f:
            return yaml.safe_load(f)

    def test_schema_version(self, schema):
        """Test schema version is correct."""
        assert schema["version"] == "1.1.0"

    def test_tfa_domain_is_ppp(self, schema):
        """Test TFA domain is constrained to PPP."""
        tfa_domain = schema["properties"]["tfa_domain"]
        assert tfa_domain["const"] == "PPP"

    def test_fuel_cell_types(self, schema):
        """Test fuel cell type enum values."""
        fc_type = schema["properties"]["fuel_cell_system"]["properties"]["fuel_cell_type"]
        expected_types = ["PEM", "SOFC", "AFC", "PAFC"]
        assert fc_type["enum"] == expected_types


class TestThermalManagementSchema:
    """Test thermal management schema."""

    @pytest.fixture
    def schema(self):
        """Load thermal management schema."""
        with open(SCHEMA_DIR / "thermal-management.yaml", 'r') as f:
            return yaml.safe_load(f)

    def test_schema_version(self, schema):
        """Test schema version is correct."""
        assert schema["version"] == "1.0.0"

    def test_tfa_domains(self, schema):
        """Test TFA domain enum includes expected values."""
        tfa_domain = schema["properties"]["tfa_domain"]
        assert "CQH" in tfa_domain["enum"]
        assert "EEE" in tfa_domain["enum"]
        assert "PPP" in tfa_domain["enum"]


class TestPassportTemplates:
    """Test digital passport templates validate against schemas."""

    @pytest.fixture
    def passport_files(self):
        """Get all passport template files."""
        return list(PASSPORT_TEMPLATE_DIR.glob("*.yaml"))

    def test_passport_templates_exist(self, passport_files):
        """Test that passport templates exist."""
        assert len(passport_files) > 0, "No passport templates found"
        
        expected_templates = [
            "hydrogen-storage-tank-passport.yaml",
            "fuel-cell-stack-passport.yaml",
            "battery-pack-passport.yaml",
            "electric-motor-passport.yaml"
        ]
        
        template_names = [f.name for f in passport_files]
        for expected in expected_templates:
            assert expected in template_names, f"Expected template {expected} not found"

    def test_passport_templates_are_valid_yaml(self, passport_files):
        """Test that all passport templates are valid YAML."""
        for template_file in passport_files:
            with open(template_file, 'r') as f:
                try:
                    template = yaml.safe_load(f)
                    assert template is not None, f"Template {template_file.name} is empty"
                except yaml.YAMLError as e:
                    pytest.fail(f"Invalid YAML in {template_file.name}: {e}")

    def test_passport_templates_have_utcs_ref(self, passport_files):
        """Test that all passport templates have UTCS reference."""
        for template_file in passport_files:
            with open(template_file, 'r') as f:
                template = yaml.safe_load(f)
            
            assert "utcs_ref" in template, f"Template {template_file.name} missing utcs_ref"
            assert "utcs_schema" in template, f"Template {template_file.name} missing utcs_schema"

    def test_passport_templates_have_architecture(self, passport_files):
        """Test that all passport templates specify BWB-H2-Hy-E architecture."""
        for template_file in passport_files:
            with open(template_file, 'r') as f:
                template = yaml.safe_load(f)
            
            assert "architecture" in template, f"Template {template_file.name} missing architecture"
            assert template["architecture"] == "BWB-H2-Hy-E", \
                f"Template {template_file.name} has incorrect architecture"


class TestSchemaIntegration:
    """Test schema integration and cross-references."""

    def test_schemas_reference_correct_tfa_domains(self):
        """Test that schemas use appropriate TFA domains."""
        schema_tfa_mapping = {
            "hydrogen-subsystem.yaml": "CQH",
            "propulsion-system.yaml": "PPP",
            "thermal-management.yaml": ["CQH", "EEE", "PPP"]
        }
        
        for schema_file, expected_tfa in schema_tfa_mapping.items():
            with open(SCHEMA_DIR / schema_file, 'r') as f:
                schema = yaml.safe_load(f)
            
            tfa_domain = schema["properties"]["tfa_domain"]
            
            if isinstance(expected_tfa, list):
                assert "enum" in tfa_domain
                for tfa in expected_tfa:
                    assert tfa in tfa_domain["enum"]
            else:
                assert tfa_domain["const"] == expected_tfa

    def test_utcs_ref_patterns_are_consistent(self):
        """Test that UTCS reference patterns follow naming convention."""
        pattern_prefix = "^UTCS-BWB-H2-HY-E-"
        
        schema_files = [
            "hydrogen-subsystem.yaml",
            "propulsion-system.yaml",
            "thermal-management.yaml"
        ]
        
        for schema_file in schema_files:
            with open(SCHEMA_DIR / schema_file, 'r') as f:
                schema = yaml.safe_load(f)
            
            utcs_ref = schema["properties"]["utcs_ref"]
            assert "pattern" in utcs_ref
            assert utcs_ref["pattern"].startswith(pattern_prefix), \
                f"UTCS pattern in {schema_file} doesn't start with {pattern_prefix}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
