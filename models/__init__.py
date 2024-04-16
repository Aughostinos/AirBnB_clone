#!/usr/bin/python3
""" _init method"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
