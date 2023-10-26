import contextlib
import yaml
from model import OutputFile, File


class Config(contextlib.ExitStack):
    file_path = 'resources/files.yml'

    input_file: File
    output_files = []

    def __init__(self):
        super().__init__()
        raw_config_file = self.enter_context(open(self.file_path, 'r'))
        config_file = yaml.safe_load(raw_config_file)

        self.input_file = File.File(config_file.get("input_file"))

        raw_output_files = config_file.get("output_files")
        for output_file in raw_output_files:
            self.output_files.append(OutputFile.OutputFile(output_file))
