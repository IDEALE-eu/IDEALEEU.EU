"""
QS Framework - Quantum Superposition for Decision Management

This package implements the Quantum Superposition (QS) technical specification v2.0
for managing pre-optimized configuration candidates before criteria collapse.

Copyright (c) 2025 IDEALE-EU
License: Apache-2.0
"""

__version__ = "2.0.0"
__status__ = "Canonical"

from .qs_field import Candidate, QSField
from .qs_api import QSAPI
from .merkle import compute_merkle_root

__all__ = [
    "Candidate",
    "QSField",
    "QSAPI",
    "compute_merkle_root",
]
