import os
import yaml
from ffmpeg import FFmpeg
from datetime import datetime, timedelta

from model.Config import Config

with open('resources/files.yml', 'r') as raw_file:
    file_config = yaml.safe_load(raw_file)


def main():
    config = Config()
    for file in config.output_files:
        if os.path.isfile(file.name):
            os.remove(file.name)
        ffmpeg = (
            FFmpeg()
            .input(config.input_file.name, {"ss": file.start})
            .output(
                file.name,
                c="copy",
                t=file.duration
            )
        )

        ffmpeg.execute()


def format_time(delta: timedelta):
    return (datetime.utcfromtimestamp(0) + delta).strftime("%H:%M:%S.%f")[:-5]


if __name__ == "__main__":
    main()
