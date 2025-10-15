"""
Unit tests for Merkle tree implementation
"""

import sys
import os

# Add src directory to path
src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.insert(0, src_path)

import unittest

# Import module directly
import merkle

compute_merkle_root = merkle.compute_merkle_root
verify_merkle_proof = merkle.verify_merkle_proof


class TestMerkle(unittest.TestCase):
    """Test Merkle tree functions"""
    
    def test_empty_tree(self):
        """Test Merkle root of empty tree"""
        root = compute_merkle_root([])
        self.assertEqual(len(root), 64)  # SHA-256 hex length
    
    def test_single_hash(self):
        """Test Merkle root of single hash"""
        hashes = ["abc123"]
        root = compute_merkle_root(hashes)
        self.assertEqual(root, "abc123")
    
    def test_two_hashes(self):
        """Test Merkle root of two hashes"""
        hashes = ["hash1", "hash2"]
        root = compute_merkle_root(hashes)
        self.assertEqual(len(root), 64)
        self.assertNotEqual(root, "hash1")
        self.assertNotEqual(root, "hash2")
    
    def test_three_hashes(self):
        """Test Merkle root of three hashes (odd number)"""
        hashes = ["hash1", "hash2", "hash3"]
        root = compute_merkle_root(hashes)
        self.assertEqual(len(root), 64)
    
    def test_deterministic(self):
        """Test that Merkle root is deterministic"""
        hashes = ["a", "b", "c", "d"]
        root1 = compute_merkle_root(hashes)
        root2 = compute_merkle_root(hashes)
        self.assertEqual(root1, root2)
    
    def test_order_matters(self):
        """Test that hash order affects Merkle root"""
        hashes1 = ["a", "b", "c"]
        hashes2 = ["c", "b", "a"]
        root1 = compute_merkle_root(hashes1)
        root2 = compute_merkle_root(hashes2)
        self.assertNotEqual(root1, root2)
    
    def test_large_tree(self):
        """Test Merkle root with many hashes"""
        hashes = [f"hash_{i}" for i in range(100)]
        root = compute_merkle_root(hashes)
        self.assertEqual(len(root), 64)
    
    def test_verify_proof_valid(self):
        """Test verification with valid proof"""
        # Simple tree: leaf1, leaf2
        # Root = H(leaf1 + leaf2)
        leaf1 = "leaf1_hash"
        leaf2 = "leaf2_hash"
        root = compute_merkle_root([leaf1, leaf2])
        
        # Proof for leaf1 is just [leaf2]
        proof = [leaf2]
        self.assertTrue(verify_merkle_proof(leaf1, proof, root))
    
    def test_verify_proof_invalid(self):
        """Test verification with invalid proof"""
        leaf1 = "leaf1_hash"
        leaf2 = "leaf2_hash"
        root = compute_merkle_root([leaf1, leaf2])
        
        # Wrong proof
        wrong_proof = ["wrong_hash"]
        self.assertFalse(verify_merkle_proof(leaf1, wrong_proof, root))


if __name__ == "__main__":
    unittest.main()
