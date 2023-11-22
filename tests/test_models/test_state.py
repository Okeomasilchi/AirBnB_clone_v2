#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """
        The function initializes an object with a name attribute set to "State" and a value attribute
        set to State.
        """
        """ """
        # `super().__init__(*args, **kwargs)` is calling the `__init__` method of the parent class
        # (`test_basemodel`). This allows the child class (`test_state`) to inherit and initialize any
        # attributes or methods defined in the parent class. The `*args` and `**kwargs` allow any
        # additional arguments to be passed to the parent class's `__init__` method.
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        The function tests that the "name" attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
