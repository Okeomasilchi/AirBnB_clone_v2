#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


# The class "test_User" is a subclass of "test_basemodel".
class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """
        The function initializes an object with a name attribute set to "User" and a value attribute set
        to User.
        """
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        The function tests if the "first_name" attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        The function tests whether the last name attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        The function tests whether the "email" attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        The function tests if the password attribute of an object is of type string.
        """
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
