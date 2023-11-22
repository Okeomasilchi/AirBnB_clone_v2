#!/usr/bin/python3
"""This module test the console"""
import unittest
from unittest.mock import patch
from console import HBNBCommand


# The TestDoCreateMethod class is a unit test case for testing the creation of a method.
class TestDoCreateMethod(unittest.TestCase):

    def setUp(self):
        """
        The setUp function initializes instances of the HBNBCommand class.
        """
        self.instance = HBNBCommand()
        self.cmd = HBNBCommand()

    def tearDown(self):
        """
        The tearDown function is a placeholder that does nothing.
        """
        pass

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_no_args(self, mock_storage, mock_print):
        """
        The function tests the behavior of the "create" command when no arguments are provided.
        
        Args:
          mock_storage: The `mock_storage` parameter is a mock object that is used to simulate the
        behavior of the storage system. It is typically used to check if certain methods or functions
        are called with the expected arguments.
          mock_print: The `mock_print` parameter is a mock object that is used to assert that a specific
        print statement is called with the expected arguments. In this case, it is used to assert that
        the `print` function is called with the message "** class name missing **" when the `create`
        command is
        """
        self.cmd.onecmd("create")
        mock_print.assert_called_with("** class name missing **")
        mock_storage.assert_not_called()

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_unknown_class(self, mock_storage, mock_print):
        """
        The function tests the behavior of the "create" command when an unknown class is provided as an
        argument.
        
        Args:
          mock_storage: The `mock_storage` parameter is a mock object that is used to simulate the
        behavior of the storage system. It is typically used to check if certain methods or functions
        are called with the expected arguments.
          mock_print: The `mock_print` parameter is a mock object that is used to simulate the behavior
        of the `print` function. It allows you to assert that certain messages are printed when the
        `create` command is executed with an unknown class. In this case, the assertion is that the
        message `** class
        """
        self.cmd.onecmd("create UnknownClass")
        mock_print.assert_called_with("** class doesn't exist **")
        mock_storage.assert_not_called()

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_valid_class_no_args(self, mock_storage, mock_print):
        """
        The function tests the "create" command for a valid class with no arguments.
        
        Args:
          mock_storage: The `mock_storage` parameter is a mock object that is used to assert that a
        specific method is called. It is likely a mock of a storage object or a storage service that is
        used to create instances of a class.
          mock_print: The `mock_print` parameter is a MagicMock object that is used to mock the `print`
        function. It allows you to assert that the `print` function was called with certain arguments
        during the test.
        """
        with patch.object(self.cmd.classes['User'], '__init__', return_value=None):
            self.cmd.onecmd("create User")
        mock_storage.assert_called_once()
        mock_print.assert_called_with(self.instance.id)

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_valid_class_and_args(self, mock_storage, mock_print):
        """
        The function tests the "do_create" method by mocking the storage and print functions and
        asserting that they are called with the correct arguments.
        
        Args:
          mock_storage: The `mock_storage` parameter is a mock object that is used to assert that a
        specific method is called. It is typically used to mock the storage or database layer in order
        to isolate the code being tested.
          mock_print: The `mock_print` parameter is a mock object that is used to simulate the behavior
        of the `print` function. It is used to assert that the correct value is printed when the
        `create` command is executed.
        """
        with patch.object(self.cmd.classes['User'], '__init__', return_value=None):
            self.cmd.onecmd("create User attribute1=value1 attribute2=value2")
        mock_storage.assert_called_once()
        mock_print.assert_called_with(self.instance.id)

    def test_parse_params_with_valid_args(self):
        """
        The function "test_parse_params_with_valid_args" tests the "parse_params" method by passing a
        list of arguments and comparing the result with the expected dictionary.
        """
        args_list = ["attribute1=value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute1': 'value1', 'attribute2': 'value2'}
        self.assertEqual(result, expected_result)

    def test_parse_params_with_invalid_args(self):
        """
        The function `test_parse_params_with_invalid_args` tests the `parse_params` method by passing in
        a list of arguments, including an invalid parameter, and checks if the returned result matches
        the expected result.
        """
        args_list = ["invalid_param", "attribute1=value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute1': 'value1', 'attribute2': 'value2'}
        self.assertEqual(result, expected_result)

    def test_parse_params_with_malformed_args(self):
        """
        The function `test_parse_params_with_malformed_args` tests the `parse_params` method by passing
        a list of arguments and asserting that the returned result matches the expected result.
        """
        args_list = ["attribute1value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute2': 'value2'}
        self.assertEqual(result, expected_result)
