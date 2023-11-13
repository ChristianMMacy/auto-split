import os

from ffmpeg import FFmpeg

import youtube
from model.Config import Config


def main():
    # Update YouTube so it's not doing stuff automatically on import
    config = Config()
    print(f"Config file loaded from {config.file_path}")
    print(f"{len(config.output_files)} output files defined")
    for file in config.output_files:
        if os.path.isfile(file.name):
            print(f"Found existing {file.name}... deleting")
            os.remove(file.name)
        generate_file(input_file_name=config.input_file.name, output_file_name=file.name, start=file.start,
                      duration=file.duration)
        try:
            youtube.upload_video(title=file.title, description=file.description,
                                 recording_date=config.input_file.recording_date, source_file_name=file.name)
        except Exception as e:
            print("Error uploading file.")
            raise e


def generate_file(input_file_name, output_file_name, start, duration):
    try:
        ffmpeg = (
            FFmpeg()
            .input(input_file_name, {"ss": start})
            .output(
                output_file_name,
                c="copy",
                t=duration
            )
        )

        ffmpeg.execute()
        print(f"{output_file_name} generated successfully")
    except Exception as e:
        print("Error generating file. Please check your configuration.")
        raise e


if __name__ == "__main__":
    main()
