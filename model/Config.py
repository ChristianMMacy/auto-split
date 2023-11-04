import contextlib
from os import getenv

import yaml
from model import OutputFile, File
from dotenv import load_dotenv


class Config(contextlib.ExitStack):
    file_path = 'resources/files.yml'
    recording_date = None

    input_file: File
    output_files = []

    refresh_token: None
    secret_config: None

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.refresh_token = getenv('REFRESH_TOKEN')
        self.secret_config = getenv('SECRET_CONFIG')

        with(self.enter_context(open(self.file_path, 'r'))) as raw_config_file:
            config_file = yaml.safe_load(raw_config_file)

            self.input_file = File.File(config_file.get("input_file"))
            self.recording_date = config_file.get("input_file").get("recording_date")

            raw_output_files = config_file.get("output_files")
            for output_file in raw_output_files:
                self.output_files.append(OutputFile.OutputFile(output_file))
