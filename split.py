from ffmpeg import FFmpeg


def main():
    input_file_name = "test_video.mp4"
    first_file_name = "first_5_seconds.mp4"
    first_file_start = "00:00"
    first_file_duration = "00:05"
    second_file_name = "second_5_seconds.mp4"
    second_file_start = "00:05"
    second_file_duration = "00:05"
    for file in [[first_file_name, first_file_start, first_file_duration], [second_file_name,
                                                                            second_file_start,
                                                                            second_file_duration]]:
        ffmpeg = (
            FFmpeg()
            .input(input_file_name, {"ss": file[1]})
            .output(
                file[0],
                c="copy",
                t=file[2]
            )
        )

        ffmpeg.execute()


if __name__ == "__main__":
    main()
