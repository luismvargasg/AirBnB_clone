#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""Module to create a unique FileStorage instance for the console."""


storage = FileStorage()
storage.reload()
