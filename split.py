from ffmpeg import FFmpeg


def main():
    ffmpeg1 = (
        FFmpeg()
        .input("test_video.mp4", {"ss": "00:00"})
        .output(
            "first_5_seconds.mp4",
            c="copy",
            t="00:05"
        )
    )

    ffmpeg1.execute()

    ffmpeg2 = (
        FFmpeg()
        .input("test_video.mp4", {"ss": "00:05"})
        .output(
            "second_5_seconds.mp4",
            c="copy",
            t="00:05"
        )
    )

    ffmpeg2.execute()


if __name__ == "__main__":
    main()
