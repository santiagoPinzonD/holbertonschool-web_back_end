#!/usr/bin/env python3.7
""" Suite test utils.py
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized, param, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map
    """

    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, expected, nested_map, path):
        """ Test utils.access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(KeyError, nested_map={}, path=("a",)),
        param(KeyError, nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, expected, nested_map, path):
        """ Test utils.access_nested_map with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get json
    """

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test utils.get_json """
        mock_object = Mock()
        mock_object.json.return_value = test_payload

        with unittest.mock.patch('utils.requests.get',
                                 return_value=mock_object):
            response = get_json(test_url)

        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test Memoize """

    def test_memoize(self):
        """ Test memoize method """

        class TestClass:
            """ Test Class """

            def a_method(self):
                """ Method a_method """
                return 42

            @memoize
            def a_property(self):
                """ Method a_property """
                return self.a_method()

        with unittest.mock.patch.object(TestClass,
                                        'a_method',
                                        return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()
