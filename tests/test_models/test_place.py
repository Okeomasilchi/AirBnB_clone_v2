#!/usr/bin/python3
"""model that test the Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    The class "test_Place" is a subclass of "test_basemodel".
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an object with a name attribute set to
        "Place" and a value attribute
        set to the Place class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        tests if the city_id attribute of an object
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        tests whether the user_id attribute of an
        object is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        tests if the "name" attribute of an object
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        tests that the description attribute of a new
        object is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        tests if the "number_rooms" attribute of an
        object is of type integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        tests if the "number_bathrooms" attribute of
        an object is of type integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        tests whether the "max_guest" attribute of an
        object is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        tests whether the "price_by_night" attribute
        of an object is of type integer.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        tests if the latitude attribute of an object
        is of type float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        tests if the latitude attribute of an object
        is of type float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        tests whether the `amenity_ids` attribute of
        an object is of type list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
