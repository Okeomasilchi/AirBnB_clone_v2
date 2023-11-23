#!/usr/bin/python3
"""module for testing the amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    The class "test_Amenity" is a
    subclass of "test_basemodel".
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an instance of the Amenity class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        tests that the "name" attribute of an
        object is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
