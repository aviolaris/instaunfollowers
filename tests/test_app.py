"""Imports"""
from unittest import TestCase
from app.app import parse_usernames, get_unfollowers_paginated


class Test(TestCase):
    """Unit Tests"""

    def test_parse_usernames_valid_input(self):
        """
        Test the function with valid html source
        """
        html_source = '<div><a target="_blank" ' \
                      'href="https://www.instagram.com/user1">user1</a>' \
                      '</div><div><a target="_blank" ' \
                      'href="https://www.instagram.com/user2">user2</a>' \
                      '</div>'
        expected_output = ['user1',
                           'user2']
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    def test_parse_usernames_valid_input_with_no_links(self):
        """
        Test the function with html source that contains no links
        """
        html_source = '<div>test</div>'
        expected_output = []
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_parse_usernames_empty_input(self):
        """
        Test the function with an empty input
        """
        html_source = ''
        expected_output = []
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_parse_usernames_invalid_input(self):
        """
        Test the function with an invalid input (not a string)
        """
        html_source = ['<a target="_blank" href="https://instagram.com/user1">user1</a>',
                       '<a target="_blank" href="https://instagram.com/user2">user2</a>']
        self.assertRaises(TypeError, parse_usernames, html_source)

    def test_get_unfollowers_paginated(self):
        """
        Test for normal usage of the function.
        """
        unfollowers_list = ['unfollower1', 'unfollower2', 'unfollower3',
                            'unfollower4', 'unfollower5']
        offset = 2
        per_page = 2
        expected_result = ['unfollower3', 'unfollower4']
        self.assertEqual(get_unfollowers_paginated(unfollowers_list,
                                                   offset,
                                                   per_page),
                         expected_result)

    def test_get_unfollowers_paginated_invalid_offset(self):
        """
        Test the function with invalid offset value
        """
        unfollowers_list = ['unfollower1', 'unfollower2', 'unfollower3',
                            'unfollower4', 'unfollower5']
        offset = 10
        per_page = 2
        expected_result = []
        self.assertEqual(get_unfollowers_paginated(unfollowers_list,
                                                   offset,
                                                   per_page),
                         expected_result)

    def test_get_unfollowers_paginated_list_with_one_element(self):
        """
        Test the function with list that has only one element
        """
        unfollowers_list = ['unfollower1']
        offset = 0
        per_page = 1
        expected_result = ['unfollower1']
        self.assertEqual(get_unfollowers_paginated(unfollowers_list,
                                                   offset,
                                                   per_page),
                         expected_result)

    def test_get_unfollowers_paginated_list_empty(self):
        """
        Test the function with empty list
        """
        unfollowers_list = []
        offset = 0
        per_page = 1
        expected_result = []
        self.assertEqual(get_unfollowers_paginated(unfollowers_list,
                                                   offset,
                                                   per_page),
                         expected_result)
