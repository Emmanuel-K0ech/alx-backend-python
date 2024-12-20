#!/usr/bin/env python3
""" Module test_utils.py """
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map method
    to test that the method returns what it is supposed to.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests method output: makes sure its the expected output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Tests whether KeyError is raise
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson inherits from unnittest.TestCase - created to test
    that utils.get_json returns the expected result
    """
    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests that the utils.get_json returns expected results
        get method is called exaclty once (per input)
        Tests that the output get_json === test_payload

        Args:
            mock_get: clone of the response from request.get code
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        # self.assertIs(mock_get.call_count, 1)
        mock_get.assert_called_once_with(test_url)


# class TestMemoize(unittest.TestCase):
#     """ Memoize decorator class """

#     def test_memoize(self):
#         """
#         method()
#         """
#         class TestClass:

#             def a_method(self):
#                 return 42

#             @memoize
#             def a_property(self):
#                 return self.a_method()

#         test_obj = TestClass()
#         for i in range(2):
#             test_obj.a_property()
#         with patch('a_method') as a_mock:
#             a_mock.assert_called_once_with()
