#!/usr/bin/python3
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up for test methods."""
        self.place = Place(city_id="123", user_id="321", name="Holiday Home",
                           description="A nice place", number_rooms=3,
                           number_bathrooms=2, max_guest=4, price_by_night=150,
                           latitude=36.778259, longitude=-119.417931,
                           amenity_ids=["pool", "wifi"])

    def test_attribute_types(self):
        """Test that all attributes are initialized with correct types."""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_default_values(self):
        """Test default values for attributes not initialized."""
        default_place = Place()
        self.assertEqual(default_place.city_id, "")
        self.assertEqual(default_place.user_id, "")
        self.assertEqual(default_place.name, "")
        self.assertEqual(default_place.description, "")
        self.assertEqual(default_place.number_rooms, 0)
        self.assertEqual(default_place.number_bathrooms, 0)
        self.assertEqual(default_place.max_guest, 0)
        self.assertEqual(default_place.price_by_night, 0)
        self.assertEqual(default_place.latitude, 0.0)
        self.assertEqual(default_place.longitude, 0.0)
        self.assertEqual(default_place.amenity_ids, [])


