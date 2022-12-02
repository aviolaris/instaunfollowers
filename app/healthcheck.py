"""Imports"""
import sys
import requests


def fetch_url(url):
    """
    Fetch url, receive response and convert it to exit code.
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
