# test_apivortex.py
"""
Tests for ApiVortex module.
"""

import unittest
from apivortex import ApiVortex

class TestApiVortex(unittest.TestCase):
    """Test cases for ApiVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApiVortex()
        self.assertIsInstance(instance, ApiVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApiVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
