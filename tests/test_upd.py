"""Imports"""
from unittest import TestCase
from app.upd import update_needed


class Test(TestCase):
    """Unit Tests"""
    def test_update_needed(self):
        """
        Test the function with multiple conditions.
        """
        # Test same version
        current_version = "v1.0.0"
        latest_version = "v1.0.0"
        self.assertFalse(update_needed(current_version, latest_version))

        # Test current version older
        current_version = "v1.0.0"
        latest_version = "v2.0.0"
        self.assertTrue(update_needed(current_version, latest_version))

        # Test current version newer
        current_version = "v2.0.0"
        latest_version = "v1.0.0"
        self.assertFalse(update_needed(current_version, latest_version))

        # Test major version of current version older
        current_version = "v1.0.0"
        latest_version = "v2.0.0"
        self.assertTrue(update_needed(current_version, latest_version))

        # Test major version of current version newer
        current_version = "v2.0.0"
        latest_version = "v1.0.0"
        self.assertFalse(update_needed(current_version, latest_version))

        # Test minor version of current version older
        current_version = "v1.1.0"
        latest_version = "v1.2.0"
        self.assertTrue(update_needed(current_version, latest_version))

        # Test minor version of current version newer
        current_version = "v1.2.0"
        latest_version = "v1.1.0"
        self.assertFalse(update_needed(current_version, latest_version))

        # Test patch version of current version older
        current_version = "v1.0.1"
        latest_version = "v1.0.2"
        self.assertTrue(update_needed(current_version, latest_version))

        # Test patch version of current version newer
        current_version = "v1.0.2"
        latest_version = "v1.0.1"
        self.assertFalse(update_needed(current_version, latest_version))

        # Test invalid version strings
        current_version = "1.0.0"
        latest_version = "v2.0.0"
        self.assertFalse(update_needed(current_version, latest_version))
