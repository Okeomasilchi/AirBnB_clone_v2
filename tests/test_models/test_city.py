#!/usr/bin/python3
"""model that test the City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    The class "test_City" is a subclass of
    "test_basemodel".
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an object with a name attribute
        set to "City" and a value attribute set
        to City.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        tests if the state_id attribute of an object
        is of type string.
        """
        new = self.value()
        new.state_id = "497e3867-d6e9-4401-9c7c-9687c18d2ac7"
        self.assertEqual(type(new.state_id), str)
