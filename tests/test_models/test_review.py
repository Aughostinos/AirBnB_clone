#!/usr/bin/python3
"""test review"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    def test_initialization(self):
        """Test the initialization of Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_custom_initialization(self):
        """Test custom initialization of Review."""
        review = Review(place_id="123", user_id="321", text="Great place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "321")
        self.assertEqual(review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
