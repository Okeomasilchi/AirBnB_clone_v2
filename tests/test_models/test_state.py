#!/usr/bin/python3
"""model that test the state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """subclass of "test_basemodel"."""
    def __init__(self, *args, **kwargs):
        """
        initializes an object with a name attribute
        set to "State" and a value attribute
        set to State.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        tests that the "name" attribute of an object
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
