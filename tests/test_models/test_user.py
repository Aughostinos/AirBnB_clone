#!/usr/bin/python3
"""test user class"""

from models.user import User

user = User(email="test@example.com")
assert user.email == "test@example.com", "Test Failed: User.email not initialized correctly"
