"""
Merkle Tree Implementation for QS Field Integrity

Provides cryptographic proof of field completeness and tamper-evidence.
"""

import hashlib
from typing import List


def compute_merkle_root(hashes: List[str]) -> str:
    """
    Compute Merkle tree root from list of hashes.
    
    Args:
        hashes: List of hash strings (e.g., SHA-256 hex digests)
        
    Returns:
        Merkle root hash as hex string
        
    Example:
        >>> hashes = ["abc...", "def...", "ghi..."]
        >>> root = compute_merkle_root(hashes)
        >>> print(root)
        0xABCD...
    """
    if not hashes:
        return hashlib.sha256(b"").hexdigest()
    
    if len(hashes) == 1:
        return hashes[0]
    
    # Pair up hashes and hash them together
    next_level = []
    for i in range(0, len(hashes), 2):
        left = hashes[i]
        right = hashes[i + 1] if i + 1 < len(hashes) else hashes[i]
        combined = hashlib.sha256((left + right).encode()).hexdigest()
        next_level.append(combined)
    
    return compute_merkle_root(next_level)


def verify_merkle_proof(leaf_hash: str, proof: List[str], root: str) -> bool:
    """
    Verify that a leaf hash is part of a Merkle tree with the given root.
    
    Args:
        leaf_hash: Hash of the leaf to verify
        proof: List of sibling hashes from leaf to root
        root: Expected Merkle root
        
    Returns:
        True if verification succeeds, False otherwise
    """
    current = leaf_hash
    for sibling in proof:
        # Combine in sorted order to ensure deterministic results
        if current <= sibling:
            combined = hashlib.sha256((current + sibling).encode()).hexdigest()
        else:
            combined = hashlib.sha256((sibling + current).encode()).hexdigest()
        current = combined
    
    return current == root
