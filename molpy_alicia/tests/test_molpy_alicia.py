"""
Unit and regression test for the molpy_alicia package.
"""

# Import package, test suite, and other packages as needed
import molpy_alicia
import pytest
import sys

def test_molpy_alicia_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molpy_alicia" in sys.modules
