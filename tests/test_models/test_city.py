#!/usr/bin/python3
"""test city"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    def test_default_initialization(self):
        """Test the default initialization of the City class."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_initialization(self):
        """Test custom initialization of the City class."""
        city = City(state_id="1", name="San Francisco")
        self.assertEqual(city.state_id, "1")
        self.assertEqual(city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
