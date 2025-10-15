"""
Unit tests for QS Field data structures
"""

import sys
import os

# Add src directory to path
src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.insert(0, src_path)

import unittest

# Import modules directly (not as package)
import merkle
import qs_field

Candidate = qs_field.Candidate
QSField = qs_field.QSField


class TestCandidate(unittest.TestCase):
    """Test Candidate class"""
    
    def setUp(self):
        """Set up test candidate"""
        self.candidate_data = {
            "id": "x_test_1",
            "configuration": {"param_1": 10.0, "param_2": 20.0},
            "utcs_manifest": {"context": "test", "content": {}},
            "score_vector": {"performance": 0.85, "cost": 0.70, "aggregate": 0.78},
            "uncertainty": {"sigma_performance": 0.05},
            "bounds": {"weight_kg": (1200, 1350)},
            "constraints_satisfied": {"C0_safety": True},
            "provenance": {"generated_by": "test"},
        }
    
    def test_candidate_creation(self):
        """Test creating a candidate"""
        candidate = Candidate(**self.candidate_data)
        self.assertEqual(candidate.id, "x_test_1")
        self.assertEqual(candidate.configuration["param_1"], 10.0)
        self.assertTrue(len(candidate.hash) == 64)  # SHA-256 hex length
    
    def test_candidate_hash_deterministic(self):
        """Test that hash is deterministic"""
        candidate1 = Candidate(**self.candidate_data)
        candidate2 = Candidate(**self.candidate_data)
        self.assertEqual(candidate1.hash, candidate2.hash)
    
    def test_candidate_to_dict(self):
        """Test conversion to dictionary"""
        candidate = Candidate(**self.candidate_data)
        data = candidate.to_dict()
        self.assertEqual(data["id"], "x_test_1")
        self.assertIn("hash", data)
    
    def test_candidate_from_dict(self):
        """Test creation from dictionary"""
        candidate = Candidate(**self.candidate_data)
        data = candidate.to_dict()
        candidate2 = Candidate.from_dict(data)
        self.assertEqual(candidate.id, candidate2.id)
        self.assertEqual(candidate.hash, candidate2.hash)


class TestQSField(unittest.TestCase):
    """Test QSField class"""
    
    def setUp(self):
        """Set up test QS field"""
        self.candidates = []
        for i in range(10):
            candidate = Candidate(
                id=f"x_{i}",
                configuration={"param": i * 10.0},
                utcs_manifest={"context": "test"},
                score_vector={"aggregate": 0.5 + i * 0.05},
                uncertainty={},
                bounds={},
                constraints_satisfied={"C0": i % 3 != 0},  # Every 3rd fails
                provenance={},
            )
            self.candidates.append(candidate)
        
        self.qs_field = QSField(
            version="QS_TEST_v1",
            candidates=self.candidates,
            scores=[c.score_vector["aggregate"] for c in self.candidates],
            bounds={},
            priors={},
            constraints={},
        )
    
    def test_qs_field_creation(self):
        """Test creating QS field"""
        self.assertEqual(self.qs_field.version, "QS_TEST_v1")
        self.assertEqual(len(self.qs_field.candidates), 10)
        self.assertFalse(self.qs_field.frozen)
    
    def test_freeze(self):
        """Test freezing QS field"""
        merkle_root = self.qs_field.freeze()
        self.assertTrue(self.qs_field.frozen)
        self.assertTrue(len(merkle_root) == 64)
        self.assertEqual(merkle_root, self.qs_field.merkle_root)
    
    def test_freeze_twice_raises_error(self):
        """Test that freezing twice raises error"""
        self.qs_field.freeze()
        with self.assertRaises(ValueError):
            self.qs_field.freeze()
    
    def test_collapse_requires_freeze(self):
        """Test that collapse requires frozen field"""
        criteria = {"evaluation_method": "weighted_sum", "weights": {}}
        with self.assertRaises(ValueError):
            self.qs_field.collapse(criteria)
    
    def test_collapse_selects_best(self):
        """Test that collapse selects best candidate"""
        self.qs_field.freeze()
        criteria = {
            "evaluation_method": "weighted_sum",
            "weights": {"aggregate": 1.0},
            "penalty_weight": 1000.0,
        }
        x_star, collapse_record = self.qs_field.collapse(criteria)
        
        # Should select candidate with highest aggregate score and satisfied constraints
        self.assertIsNotNone(x_star)
        self.assertIn("collapse_event", collapse_record)
        self.assertEqual(collapse_record["collapse_event"]["selected_candidate"], x_star.id)
    
    def test_validate_integrity(self):
        """Test integrity validation"""
        self.qs_field.freeze()
        
        # Save original merkle root
        original_root = self.qs_field.merkle_root
        
        # Validation should pass initially
        self.assertTrue(self.qs_field.validate_integrity())
        
        # Tamper with a candidate's ID (which changes its hash)
        original_id = self.qs_field.candidates[0].id
        self.qs_field.candidates[0].id = "tampered"
        # Force hash recomputation
        self.qs_field.candidates[0].__post_init__()
        
        # Validation should now fail (merkle root no longer matches)
        self.assertFalse(self.qs_field.validate_integrity())
        
        # Restore for other tests
        self.qs_field.candidates[0].id = original_id
        self.qs_field.candidates[0].__post_init__()
    
    def test_coverage_metrics(self):
        """Test coverage metrics computation"""
        metrics = self.qs_field.compute_coverage_metrics()
        self.assertEqual(metrics["total_candidates"], 10)
        # Every 3rd candidate fails constraint (0, 3, 6, 9) = 4 fail, 6 pass
        self.assertEqual(metrics["feasible_candidates"], 6)
        self.assertAlmostEqual(metrics["coverage_ratio"], 0.6)
    
    def test_pareto_frontier(self):
        """Test Pareto frontier extraction"""
        # Add multiple objectives to candidates
        for i, candidate in enumerate(self.qs_field.candidates):
            candidate.score_vector.update({
                "cost": 0.3 + i * 0.05,
                "risk": 0.9 - i * 0.05,
            })
        
        pareto = self.qs_field.get_pareto_frontier(["cost", "risk"])
        self.assertTrue(len(pareto) > 0)
        self.assertTrue(len(pareto) <= len(self.qs_field.candidates))
    
    def test_get_candidate_by_id(self):
        """Test retrieving candidate by ID"""
        candidate = self.qs_field.get_candidate_by_id("x_5")
        self.assertIsNotNone(candidate)
        self.assertEqual(candidate.id, "x_5")
        
        not_found = self.qs_field.get_candidate_by_id("x_999")
        self.assertIsNone(not_found)
    
    def test_to_dict_and_from_dict(self):
        """Test serialization and deserialization"""
        data = self.qs_field.to_dict()
        qs_field_2 = QSField.from_dict(data)
        
        self.assertEqual(qs_field_2.version, self.qs_field.version)
        self.assertEqual(len(qs_field_2.candidates), len(self.qs_field.candidates))


if __name__ == "__main__":
    unittest.main()
