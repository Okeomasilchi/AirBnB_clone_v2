#!/usr/bin/python3
"""module for testing the basemodel class """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    The test_basemodel class is a subclass of the
    unittest.TestCase class.
    """

    def __init__(self, *args, **kwargs):
        """
        constructor for a class called BaseModel,
        which initializes the name and
        value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        placeholder function that does nothing.
        """
        pass

    def tearDown(self):
        """
        remove a file named 'file.json' and
        ignores any errors that
        occur.
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        tests if the value returned by self.value()
        is of type self.value.
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        creates a new instance of `BaseModel`
        using the values from an
        existing instance.
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        tests if a `TypeError` is raised when
        trying to create a new `BaseModel`
        instance with invalid keyword arguments.
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        tests the string representation of an object.
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        tests whether the `to_dict` method of
        an object returns the same
        dictionary when called twice.
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        tests if passing `None` as a keyword argument
        raises a `TypeError`.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        tests if a `KeyError` is raised when
        calling the `value` function
        with keyword arguments.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        tests if the "id" attribute of an object
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        tests if the "created_at" attribute of an
        object is of type datetime.datetime.
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        tests if the "updated_at" attribute of a
        BaseModel object is of type datetime.datetime
        and if it is different from the
        "created_at" attribute.
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
