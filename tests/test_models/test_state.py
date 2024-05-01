#!/usr/bin/python3
"""test state"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    def test_initialization(self):
        """Test the initialization of State attributes."""
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_initialization(self):
        """Test the initialization with custom values."""
        state = State(name="California")
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
