"""Imports"""
import sys
import requests


def fetch_url(url):
    """
    Fetch the given URL, receive response, and convert it to exit code.

    Parameters:
    - url: str: the URL to fetch
    - timeout: int: the number of seconds to wait for a response before timing out

    Returns:
    - int: the exit code corresponding to the response

    Raises:
    - requests.exceptions.Timeout: if the request times out
    """
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        if status_code == 200:
            sys.exit(0)
        else:
            sys.exit(1)
    except requests.exceptions.Timeout:
        sys.exit(1)


fetch_url('http://localhost:5000')
