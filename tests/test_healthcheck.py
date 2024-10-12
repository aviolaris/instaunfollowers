"""Imports"""
import unittest
from unittest.mock import patch, MagicMock
import requests
from app.healthcheck import fetch_url


class TestHealthCheck(unittest.TestCase):
    """Unit Tests"""

    @patch('app.healthcheck.requests.get')
    @patch('app.healthcheck.sys.exit')
    def test_fetch_url_success(self, mock_exit, mock_get):
        """
        Test fetch_url with a successful 200 status code
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        fetch_url('http://localhost:5000')
        mock_exit.assert_called_once_with(0)

    @patch('app.healthcheck.requests.get')
    @patch('app.healthcheck.sys.exit')
    def test_fetch_url_non_200(self, mock_exit, mock_get):
        """
        Test fetch_url with a non-200 status code
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        fetch_url('http://localhost:5000')
        mock_exit.assert_called_once_with(1)

    @patch('app.healthcheck.requests.get', side_effect=requests.exceptions.Timeout)
    @patch('app.healthcheck.sys.exit')
    def test_fetch_url_timeout(self, mock_exit, _):
        """
        Test fetch_url handling of a timeout exception
        """
        fetch_url('http://localhost:5000')
        mock_exit.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
