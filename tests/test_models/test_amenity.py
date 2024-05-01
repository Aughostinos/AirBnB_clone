#!/usr/bin/python3
"""test amenity"""
from models.amenity import Amentiy
import unittest


class TestAmenity(unittest.TestCase):
    def test_initialization(self):
        """Test that the Amenity class is initialized correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_custom_initialization(self):
        """Test initialization with a custom name."""
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
