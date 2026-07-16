# test_decentroweavex.py
"""
Tests for DecentroWeaveX module.
"""

import unittest
from decentroweavex import DecentroWeaveX

class TestDecentroWeaveX(unittest.TestCase):
    """Test cases for DecentroWeaveX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentroWeaveX()
        self.assertIsInstance(instance, DecentroWeaveX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentroWeaveX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
