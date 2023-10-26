import os
from ffmpeg import FFmpeg
from model.Config import Config


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


if __name__ == "__main__":
    main()
