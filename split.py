import os
import yaml
from ffmpeg import FFmpeg

with open('files.yml', 'r') as raw_file:
    file_config = yaml.safe_load(raw_file)


def main():
    for file in file_config["output_files"]:
        if os.path.isfile(file["name"]):
            os.remove(file["name"])
        ffmpeg = (
            FFmpeg()
            .input(file_config['input_file']['name'], {"ss": file["start"]})
            .output(
                file["name"],
                c="copy",
                t=file["duration"]
            )
        )

        ffmpeg.execute()


if __name__ == "__main__":
    main()
