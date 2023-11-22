#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


# The class "test_Place" is a subclass of "test_basemodel".
class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """
        The function initializes an object with a name attribute set to "Place" and a value attribute
        set to the Place class.
        """
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        The function tests if the city_id attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        The function tests whether the user_id attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        The function tests if the "name" attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        The function tests that the description attribute of a new object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        The function tests if the "number_rooms" attribute of an object is of type integer.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        The function tests if the latitude attribute of an object is of type float.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        The function tests if the latitude attribute of an object is of type float.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        The function tests whether the `amenity_ids` attribute of an object is of type list.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
