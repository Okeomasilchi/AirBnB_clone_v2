#!/usr/bin/python3
"""model that test the review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review



class test_review(test_basemodel):
    """
    The class "test_review" is a subclass of "test_basemodel".
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an object with a name attribute
        set to "Review" and a value attribute
        set to the Review class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        checks if the place_id attribute of a new
        object is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        tests whether the user_id attribute of an object
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        tests if the "text" attribute of an object is of
        type string.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
