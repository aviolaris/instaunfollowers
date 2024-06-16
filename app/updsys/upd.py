"""Imports"""
import logging
import re
import requests


def get_latest_version():
    """Retrieves the latest release version of the InstaUnFollowers application from GitHub.

    Returns:
        str: The latest release version in the format 'vX.Y.Z'.
        None: If the latest release version is not available or if there was an error retrieving it.
    """
    try:
        response = requests.get('https://github.com/aviolaris/instaunfollowers/releases/latest',
                                timeout=10)
        response.raise_for_status()
        pattern = re.compile(r'v\d+\.\d+\.\d+')
        match = pattern.search(response.text)
        if match:
            version = match.group(0)
            return version
    except (requests.exceptions.RequestException, ValueError) as exc:
        logging.error("Failed to retrieve latest release version: %s", exc)
    return None


def update_needed(current_version: str, latest_version: str) -> bool:
    """
    Check whether an update is needed, based on the comparison of two version strings.

    Args:
        current_version: A string representing the current version, in the format 'vX.Y.Z'.
        latest_version: A string representing the latest version available, in the same format.

    Returns:
        A boolean value indicating if the current version is older than the latest version.
    """
    version_pattern = r'^v\d+\.\d+\.\d+$'
    if not (re.match(version_pattern, current_version) and
            re.match(version_pattern, latest_version)):
        return False
    current_version_parts = map(int, current_version[1:].split('.'))
    latest_version_parts = map(int, latest_version[1:].split('.'))
    for current_part, latest_part in zip(current_version_parts, latest_version_parts):
        if current_part < latest_part:
            return True
        if current_part > latest_part:
            return False
    return False
