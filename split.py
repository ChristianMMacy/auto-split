import os
from ffmpeg import FFmpeg
from model.Config import Config


def main():
    config = Config()
    print(f"Config file loaded from {config.file_path}")
    print(f"{len(config.output_files)} output files defined")
    for file in config.output_files:
        try:
            if os.path.isfile(file.name):
                print(f"Found existing {file.name}... deleting")
                os.remove(file.get("name"))
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
            print(f"{file.name} generated successfully")
        except Exception as e:
            print("Error generating file. Please check your configuration.")
            raise e


if __name__ == "__main__":
    main()
