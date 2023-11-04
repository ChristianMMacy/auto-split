import unittest
import model
from unittest import mock

from model.Config import Config


class TestConfig(unittest.TestCase):

    @mock.patch('model.Config.Config.set_input_file')
    @mock.patch('model.Config.Config.set_output_files')
    @mock.patch('model.Config.Config.load_youtube_credentials')
    @mock.patch('model.Config.load_config_file')
    @mock.patch('model.Config.super')
    def test_initialization(self, mock_super, mock_load_config, mock_load_youtube, mock_set_input, mock_set_output):
        file_path = 'foo'
        config_file = {
            "input_file": {
                "recording_date": "bar"
            }
        }
        mock_load_config.return_value = config_file

        config = Config(file_path)

        mock_super.assert_called_once_with()
        mock_load_youtube.assert_called_once_with()
        mock_load_config.assert_called_once_with(file_path)
        mock_set_input.assert_called_once_with(config_file)
        mock_set_output.assert_called_once_with(config_file)
        self.assertEqual(config.recording_date, config_file.get("input_file").get("recording_date"))

    @mock.patch("yaml.safe_load")
    def test_load_config_file(self, mock_safe_load):
        """
        It opens a file based the passed path or default file location
        :param mock_safe_load:
        """

        """It opens a config file at the passed location"""
        with mock.patch('builtins.open', mock.mock_open()) as mock_open:
            model.Config.load_config_file("foo")

            mock_open.assert_called_once_with("foo", "r")
            mock_safe_load.assert_called_once_with(mock_open(mock_open))

        """It opens a config file at the default location when none passed"""
        with mock.patch('builtins.open', mock.mock_open()) as mock_open:
            model.Config.load_config_file()

            mock_open.assert_called_once_with(model.Config.DEFAULT_FILE_PATH, "r")


    def test_it_handles_missing_properties(self):
        pass

    def test_the_config_file_location_can_be_specified_by_env(self):
        pass

    def test_it_finds_refresh_and_secret_config_by_env(self):
        pass
