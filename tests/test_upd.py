"""Imports"""
from unittest import TestCase
from unittest.mock import patch
import requests
from app.updsys.upd import get_latest_version, update_needed


class Test(TestCase):
    """Unit Tests"""

    @patch('requests.get')
    def test_get_latest_version(self, mock_get):
        """
        Test the function with mocked HTTP responses.
        """
        # Mock a successful response with a valid version string
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = '<html>... v2.0.0 ...</html>'
        self.assertEqual(get_latest_version(), 'v2.0.0')
        # Mock a response with no valid version string
        mock_response.text = '<html>... no version here ...</html>'
        self.assertIsNone(get_latest_version())
        # Mock an error response
        mock_get.side_effect = requests.exceptions.RequestException
        self.assertIsNone(get_latest_version())

    def test_update_needed(self):
        """
        Test the function with multiple conditions
        and return comments for failed tests.
        """
        test_cases = [
            ("v1.0.0", "v1.0.0", False, "Test same version"),
            ("v1.0.0", "v2.0.0", True, "Test current version older"),
            ("v2.0.0", "v1.0.0", False, "Test current version newer"),
            ("v1.0.0", "v2.0.0", True, "Test major version of current version older"),
            ("v2.0.0", "v1.0.0", False, "Test major version of current version newer"),
            ("v1.1.0", "v1.2.0", True, "Test minor version of current version older"),
            ("v1.2.0", "v1.1.0", False, "Test minor version of current version newer"),
            ("v1.0.1", "v1.0.2", True, "Test patch version of current version older"),
            ("v1.0.2", "v1.0.1", False, "Test patch version of current version newer"),
            ("1.0.0", "v2.0.0", False, "Test invalid version strings"),
        ]
        failed_tests = []
        for current_version, latest_version, expected_result, comment in test_cases:
            with self.subTest(current_version=current_version, latest_version=latest_version):
                try:
                    self.assertEqual(update_needed(current_version, latest_version),
                                     expected_result)
                except AssertionError:
                    failed_tests.append(comment)
        if failed_tests:
            self.fail(f"Tests failed for the following cases: {', '.join(failed_tests)}")
