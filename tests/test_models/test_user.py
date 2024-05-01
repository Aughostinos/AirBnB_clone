#!/usr/bin/python3
"""test user class"""

from models.user import User


def test_attribute(user, attribute, expected):
    actual = getattr(user, attribute)
    assert actual == expected, f"Test Failed: User.{attribute} is '{actual}' but expected '{expected}'"
    return "OK"
