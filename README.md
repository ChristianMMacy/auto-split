# auto-split

Splits video simply and quickly.

# Splitting a Video
## ./resources/files.yml
This file is how we define the input video and output videos. A sample configuration is included that you can play with.

The properties you can add/modify are:
```yaml
input_file:
  name: string-path

output_files:
  - name: string-path
    start: string-time
    end: string-time (ignored if duration is provided)
    duration: string-time
```

### string-path
The path and name of the file relative to where the script is executed. E.g. `resources/input.mp4` or `out/output-1.mp4`.

### string-time
A time code formatted as hours:minutes:seconds.milliseconds, e.g. "01:02:03.400".

Hours and milliseconds are optional. E.g. "01:02" is 1 minute and 2 seconds.

## ./out
**KNOWN ISSUE**: For now, you need to manually create the "out" folder.

## Docker
This is the easiest way to get started.

The docker-compose file assumes a "resources" directory and an "out" directory for bind mounts.
1. `docker compose up`

## Local Python and Dependencies
Running the app with Docker is easier in general, but if you need to add dependencies you'll want to follow these steps to get set up locally with Python, etc.

1. Install `ffmpeg` and `python3`
    - `brew install python ffmpeg`
2. Install dependencies
    - `pip install -r requirements.txt`
3. Try splitting the test video into three
    - `python3 split.py`
4. Try updating the number of files by adding a file to "output_files"
