import unittest
from unittest import mock

import youtube


class YouTubeTest(unittest.TestCase):

    @mock.patch('os.getenv')
    @mock.patch('dotenv.load_dotenv')
    def test_load_local_credentials(self, ignored, mock_getenv):
        """
        It returns environment variables for refresh token and environment path
        :param ignored:
        :param mock_getenv:
        :return:
        """
        mock_getenv.side_effect = ["foo", "bar"]
        self.assertEqual(youtube.load_local_credentials(), ('foo', 'bar'))
        mock_getenv.assert_has_calls([mock.call(youtube.REFRESH_TOKEN), mock.call(youtube.SECRET_CONFIG)])

    def test_initialize_client(self):
        pass

    def test_load_config(self):
        pass

    def test_generate_refresh_token(self):
        pass

    def test_create_upload_request(self):
        pass

    def test_upload_video(self):
        pass
