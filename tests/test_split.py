import unittest
from unittest import mock

from .context import split


class SplitTest(unittest.TestCase):

    @mock.patch('split.generate_file')
    @mock.patch('split.Config')
    @mock.patch('youtube.upload_video')
    @mock.patch('os.remove')
    @mock.patch('os.path.isfile')
    def test_removes_existing_files_then_generates_and_uploads(self, mock_is_file, mock_remove, mock_upload,
                                                               mock_config,
                                                               mock_generate_file):
        mock_config.return_value.name = "foo"
        mock_config.return_value.file_path = "bar"
        mock_config.return_value.recording_date = "today"
        mock_is_file.return_value = True
        with mock.patch('model.File.File', name="foo", start="00", duration="10", title="bar") as mock_file:
            mock_config.return_value.output_files = [mock_file]

            split.main()
            mock_remove.assert_called_once_with(mock_file.name)
            mock_generate_file.assert_called_once_with(input_file_name=mock_config().input_file.name,
                                                       output_file_name=mock_file.name, start=mock_file.start,
                                                       duration=mock_file.duration)
            mock_upload.assert_called_once_with(title=mock_file.title, description=mock_file.description,
                                                recording_date=mock_config().input_file.recording_date,
                                                source_file_name=mock_file.name)
