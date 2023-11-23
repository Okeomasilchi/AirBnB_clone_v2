#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.user import User
from models.state import State
from models.city import City
from models import storage
import os


class TestDBStorage(unittest.TestCase):
    """The TestDBStorage class is a unit test case for
    testing the functionality of a database storage
    system.
    """
    @classmethod
    def setUpClass(cls):
        """
        sets up the necessary environment variables for
        testing a database storage class.
        """
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        cls.storage = storage.DBStorage()

    @classmethod
    def tearDownClass(cls):
        """
        deletes specific environment variables.
        """
        del os.environ['HBNB_ENV']
        del os.environ['HBNB_MYSQL_USER']
        del os.environ['HBNB_MYSQL_PWD']
        del os.environ['HBNB_MYSQL_HOST']
        del os.environ['HBNB_MYSQL_DB']

    def setUp(self):
        """
        The setUp function reloads the storage.
        """
        self.storage.reload()

    def tearDown(self):
        """
        used to close the storage in a test case.
        """
        self.storage.close()

    def test_all_method(self):
        """
        tests the `all` method of a storage object
        """
        # Create some objects to test the all method
        state = State(name="TestState")
        city = City(name="TestCity", state_id=state.id)
        user = User(name="TestUser")
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(user)
        self.storage.save()

        # Test the all method for State
        all_states = self.storage.all(State)
        self.assertIn(state.id, all_states)
        self.assertEqual(all_states[state.id]['name'], "TestState")

        # Test the all method for City
        all_cities = self.storage.all(City)
        self.assertIn(city.id, all_cities)
        self.assertEqual(all_cities[city.id]['name'], "TestCity")
        
        # Test the all method for User
        all_users = self.storage.all(User)
        self.assertIn(user.id, all_users)
        self.assertEqual(all_users[user.id]['name'], "TestUser")

    def test_new_method(self):
        """
        tests a new method by creating a new object
        and checking if it's in the session.
        """
        user = User(name="NewUser")
        self.storage.new(user)
        self.assertIn(user, self.storage._DBStorage__session.new)

    def test_save_method(self):
        """
        tests the save method by creating a new user
        object, adding it to the session, and
        then saving it.
        """
        user = User(name="NewUser")
        self.storage.new(user)
        self.storage.save()
        self.assertIn(user, self.storage._DBStorage__session)

    def test_delete_method(self):
        """
        tests the delete method by creating a new object,
        adding it to the session,
        deleting it, and then saving.
        """
        user = User(name="ToDeleteUser")
        self.storage.new(user)
        self.storage.save()
        self.assertIn(user, self.storage._DBStorage__session)
        self.storage.delete(user)
        self.assertNotIn(user, self.storage._DBStorage__session)
