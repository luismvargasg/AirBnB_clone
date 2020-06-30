#!/usr/bin/python3
"""unittest for BaseModel"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """defining the unittest cases for BaseModel class"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Found code style " +
                         "errors (and warnings).")