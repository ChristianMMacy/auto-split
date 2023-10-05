# auto-split
Splits video simply and quickly.

# Splitting a Video
1. Install `ffmpeg`
    - `brew install ffmpeg`
2. Try splitting the test video into two
   1. `ffmpeg -ss 00:00 -i test_video.mp4 -t 00:05 -c copy first_5_seconds.mp4`
   2. `ffmpeg -ss 00:05 -i test_video.mp4 -t 00:05 -c copy second_5_seconds.mp4`
   3. You should now have three files
      - test_video.mp4
      - first_5_seconds.mp4
      - second_5_seconds.mp4
