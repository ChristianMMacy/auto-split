import contextlib
from os import getenv

import yaml
from dotenv import load_dotenv

from model import OutputFile, File

DEFAULT_FILE_PATH = 'resources/files.yml'


def load_config_file(file_path=DEFAULT_FILE_PATH):
    with(open(file_path, 'r')) as raw_config_file:
        return yaml.safe_load(raw_config_file)


class Config(contextlib.ExitStack):
    file_path: DEFAULT_FILE_PATH
    input_file: File
    recording_date = None
    output_files = []

    refresh_token: None
    secret_config: None

    def __init__(self, file_path=None):
        super().__init__()

        if file_path:
            self.file_path = file_path

        config = load_config_file(self.file_path)
        self.set_input_file(config)
        self.set_output_files(config)
        self.recording_date = config.get("input_file").get("recording_date")

    def set_input_file(self, config_file):
        self.input_file = File.File(config_file.get("input_file"))

    def set_output_files(self, config_file):
        for output_file in config_file.get("output_files", []):
            self.output_files.append(OutputFile.OutputFile(output_file))
