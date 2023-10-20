import os
import yaml
from ffmpeg import FFmpeg
from datetime import time, datetime, date, timedelta

with open('resources/files.yml', 'r') as raw_file:
    file_config = yaml.safe_load(raw_file)

default_time = "00:00:00.0"


def main():
    for file in file_config["output_files"]:
        start = time.fromisoformat(file.get("start", default_time))
        end = time.fromisoformat(file.get("end", default_time))
        delta = datetime.combine(date.min, end) - datetime.combine(date.min, start)
        duration = file.get("duration", format_time(delta))
        if os.path.isfile(file["name"]):
            os.remove(file["name"])
        ffmpeg = (
            FFmpeg()
            .input(file_config['input_file']['name'], {"ss": file["start"]})
            .output(
                file["name"],
                c="copy",
                t=duration
            )
        )

        ffmpeg.execute()


def format_time(delta: timedelta):
    return (datetime.utcfromtimestamp(0) + delta).strftime("%H:%M:%S.%f")[:-5]


if __name__ == "__main__":
    main()
