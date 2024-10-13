"""Imports"""
import unittest
import zipfile
from unittest import TestCase, mock
from app.app import (app, create_upload_dir, find_unfollowers,
                     get_unfollowers_paginated, parse_usernames,
                     UPLOAD_FOLDER)


class TestApp(TestCase):
    """Unit Tests"""

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.app = app.test_client()
        self.app.testing = True

    @mock.patch('app.app.os.makedirs')
    @mock.patch('app.app.os.path.exists')
    def test_directory_does_not_exist_makedirs_called(self, mock_exists, mock_makedirs):
        """
        Test that 'create_upload_dir' calls 'os.makedirs' when the directory does not exist.
        """
        mock_exists.return_value = False
        create_upload_dir()
        mock_exists.assert_called_once_with(UPLOAD_FOLDER)
        mock_makedirs.assert_called_once_with(UPLOAD_FOLDER)

    @mock.patch('app.app.os.makedirs')
    @mock.patch('app.app.os.path.exists')
    def test_directory_exists_makedirs_not_called(self, mock_exists, mock_makedirs):
        """
        Test that 'create_upload_dir' does not call 'os.makedirs' when the directory exists.
        """
        mock_exists.return_value = True
        create_upload_dir()
        mock_exists.assert_called_once_with(UPLOAD_FOLDER)
        mock_makedirs.assert_not_called()

    @mock.patch('app.app.os.makedirs')
    @mock.patch('app.app.os.path.exists')
    def test_makedirs_raises_exception_handled(self, mock_exists, mock_makedirs):
        """
        Test that 'create_upload_dir' handles exceptions raised by 'os.makedirs'.
        """
        mock_exists.return_value = False
        mock_makedirs.side_effect = OSError("Unable to create directory")
        try:
            create_upload_dir()
        except OSError:
            self.fail("create_upload_dir raised an OSError unexpectedly!")
        mock_exists.assert_called_once_with(UPLOAD_FOLDER)
        mock_makedirs.assert_called_once_with(UPLOAD_FOLDER)

    @mock.patch('app.app.parse_usernames')
    def test_parse_usernames_valid_input(self, mock_parse_usernames):
        """
        Test that 'parse_usernames' extracts usernames correctly from valid HTML source.
        """
        mock_parse_usernames.return_value = ['user1', 'user2']
        html_source = '<div><a target="_blank" ' \
                      'href="https://www.instagram.com/user1">user1</a>' \
                      '</div><div><a target="_blank" ' \
                      'href="https://www.instagram.com/user2">user2</a>' \
                      '</div>'
        expected_output = ['user1',
                           'user2']
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)

    @mock.patch('app.app.parse_usernames')
    def test_parse_usernames_valid_input_with_no_links(self, mock_parse_usernames):
        """
        Test that 'parse_usernames' returns an empty list when no links are found.
        """
        mock_parse_usernames.return_value = []
        html_source = '<div>test</div>'
        expected_output = []
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)

    @mock.patch('app.app.parse_usernames')
    def test_parse_usernames_empty_input(self, mock_parse_usernames):
        """
        Test that 'parse_usernames' returns an empty list for empty input.
        """
        mock_parse_usernames.return_value = []
        html_source = ''
        expected_output = []
        result = parse_usernames(html_source)
        self.assertEqual(result, expected_output)

    def test_parse_usernames_invalid_input(self):
        """
        Test that 'parse_usernames' raises a TypeError when input is not a string.
        """
        html_source = ['<a target="_blank" href="https://instagram.com/user1">user1</a>',
                       '<a target="_blank" href="https://instagram.com/user2">user2</a>']
        with self.assertRaises(TypeError):
            parse_usernames(html_source)

    @mock.patch('app.app.get_unfollowers_paginated')
    def test_get_unfollowers_paginated(self, mock_get_unfollowers_paginated):
        """
        Test that 'get_unfollowers_paginated' returns the correct paginated results.
        """
        mock_get_unfollowers_paginated.return_value = ['unfollower3',
                                                       'unfollower4']
        unfollowers_list = ['unfollower1', 'unfollower2', 'unfollower3',
                            'unfollower4', 'unfollower5']
        offset = 2
        per_page = 2
        result = get_unfollowers_paginated(unfollowers_list,
                                           offset,
                                           per_page)
        self.assertEqual(result, ['unfollower3', 'unfollower4'])

    @mock.patch('app.app.get_unfollowers_paginated')
    def test_get_unfollowers_paginated_invalid_offset(self, mock_get_unfollowers_paginated):
        """
        Test that 'get_unfollowers_paginated' returns an empty list for an invalid offset.
        """
        mock_get_unfollowers_paginated.return_value = []
        unfollowers_list = ['unfollower1', 'unfollower2', 'unfollower3',
                            'unfollower4', 'unfollower5']
        offset = 10
        per_page = 2
        result = get_unfollowers_paginated(unfollowers_list, offset, per_page)
        self.assertEqual(result, [])

    @mock.patch('app.app.get_unfollowers_paginated')
    def test_get_unfollowers_paginated_list_with_one_element(self, mock_get_unfollowers_paginated):
        """
        Test that 'get_unfollowers_paginated' works with a list that has one element.
        """
        mock_get_unfollowers_paginated.return_value = ['unfollower1']
        unfollowers_list = ['unfollower1']
        offset = 0
        per_page = 1
        result = get_unfollowers_paginated(unfollowers_list,
                                           offset,
                                           per_page)
        self.assertEqual(result, ['unfollower1'])

    @mock.patch('app.app.get_unfollowers_paginated')
    def test_get_unfollowers_paginated_list_empty(self, mock_get_unfollowers_paginated):
        """
        Test that 'get_unfollowers_paginated' returns an empty list when given an empty list.
        """
        mock_get_unfollowers_paginated.return_value = []
        unfollowers_list = []
        offset = 0
        per_page = 1
        result = get_unfollowers_paginated(unfollowers_list,
                                           offset,
                                           per_page)
        self.assertEqual(result, [])

    @mock.patch('app.app.zipfile.ZipFile')
    def test_find_unfollowers_valid_zip(self, mock_zipfile):
        """
        Test that 'find_unfollowers' correctly identifies unfollowers from a valid zip file.
        """
        mock_zipfile.return_value.__enter__.return_value.namelist.return_value = ['followers.html',
                                                                                  'following.html']
        mock_zipfile.return_value.__enter__.return_value.read.side_effect = [
            b'<a href="https://www.instagram.com/user1">user1</a>',
            b'<a href="https://www.instagram.com/user2">user2</a>'
        ]
        unfollowers = find_unfollowers('test.zip')
        self.assertEqual(unfollowers, ['user2'])

    @mock.patch('app.app.zipfile.ZipFile')
    def test_find_unfollowers_invalid_zip(self, mock_zipfile):
        """
        Test that 'find_unfollowers' handles invalid zip files correctly.
        """
        mock_zipfile.side_effect = zipfile.BadZipFile
        unfollowers = find_unfollowers('invalid.zip')
        self.assertIsNone(unfollowers)

    @mock.patch('app.app.zipfile.ZipFile')
    def test_find_unfollowers_empty_html(self, mock_zipfile):
        """
        Test that 'find_unfollowers' returns an empty list when
        both the 'followers' and 'following' files are empty.
        """
        mock_zipfile.return_value.__enter__.return_value.namelist.return_value = ['followers.html',
                                                                                  'following.html']
        mock_zipfile.return_value.__enter__.return_value.read.side_effect = [b'', b'']
        unfollowers = find_unfollowers('test.zip')
        self.assertEqual(unfollowers, [])

    def test_unfollowers_route(self):
        """
        Test that the '/unfollowers' route returns the correct paginated results.
        """
        with self.app as client:
            unfollowers_list = [f'user{i}' for i in range(1, 21)]
            with client.session_transaction() as sess:
                sess['unfollowers'] = unfollowers_list
            response = client.get('/unfollowers?page=1')
            self.assertEqual(response.status_code, 200)
            for i in range(1, 11):
                self.assertIn(f'user{i}'.encode(), response.data)
            response = client.get('/unfollowers?page=2')
            self.assertEqual(response.status_code, 200)
            for i in range(11, 21):
                self.assertIn(f'user{i}'.encode(), response.data)

    @mock.patch('app.app.os.remove')
    @mock.patch('app.app.os.path.exists')
    def test_upload_no_file(self, mock_exists, _):
        """
        Test the file upload route when no file is uploaded.
        """
        mock_exists.return_value = False
        response = self.app.post('/', data={})
        self.assertEqual(response.status_code, 302)

    @mock.patch('app.app.os.remove')
    @mock.patch('app.app.os.path.exists')
    def test_upload_empty_filename(self, mock_exists, _):
        """
        Test the file upload route with an empty file name.
        """
        mock_exists.return_value = False
        data = {'file': (b'', '')}
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 302)

    @mock.patch('app.app.os.remove')
    @mock.patch('app.app.os.path.exists')
    def test_upload_invalid_extension(self, mock_exists, _):
        """
        Test the file upload route with an invalid file extension.
        """
        mock_exists.return_value = False
        data = {'file': (b'test content', 'test.txt')}
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 302)

    @mock.patch('platform.system')
    def test_windows_specific_logic(self, mock_platform):
        """
        Test that the application runs correctly on the Windows platform.
        """
        mock_platform.return_value = "Windows"
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
