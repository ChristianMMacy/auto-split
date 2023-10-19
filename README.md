# auto-split

Splits video simply and quickly.

# Splitting a Video

1. Install `ffmpeg` and `python3`
    - `brew install python ffmpeg pyyaml python-ffmpeg`
2. Try splitting the test video into three
    - `python3 split.py`
3. Try updating the number of files by adding a file to "output_files"
    - The properties for the "output_files" in `files.yml` are:
      - name: string (the output filename -- will overwrite)
      - start: HH:MM:SS(.ss)
      - end: HH:MM:SS(.ss)
      - duration: HH:MM:SS(.ss)
