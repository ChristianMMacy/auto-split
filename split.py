import json
import os

from ffmpeg import FFmpeg
from pyyoutube import Client, Video, VideoSnippet, Thumbnails
from pyyoutube.media import Media
from pyyoutube.models.common import Thumbnail

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


def hit_youtube():
    config = Config()
    scopes = ["https://www.googleapis.com/auth/youtube",
              "https://www.googleapis.com/auth/youtube.force-ssl",
              "https://www.googleapis.com/auth/userinfo.profile", ]
    with (open(config.secret_config) as raw_secret_config):
        secret_config = json.loads(raw_secret_config.read())
        client_id = secret_config.get("installed").get("client_id")
        client_secret = secret_config.get("installed").get("client_secret")

        client = Client(client_id=client_id, client_secret=client_secret)

        if config.refresh_token is None:
            authorize_url, state = client.get_authorize_url(scope=scopes, access_type="offline")
            print('Click the URL to authenticate and copy the redirected URL:\n', authorize_url)
            url = input('Enter the redirected URL\n')
            # Debug and inspect this response to get the refresh token
            # Visit the [url,] from auth_url_response, sign in, and get the "code" query param from the response
            # Run again to get the access_token_response and add the refresh token to environment (e.g. via .env)
            access_token_response = client.generate_access_token(
                authorization_response=url,
                scope=scopes)
            print(f"Your refresh token: {access_token_response.refresh_token}")
        else:
            client.access_token = client.refresh_access_token(config.refresh_token).access_token
        body = Video(snippet=VideoSnippet(title="test video", description="test",
                                          thumbnails=Thumbnails(default=Thumbnail("resources/profpic.jpg"))))
        media = Media(filename="out/first_5_seconds.mp4")
        upload = client.videos.insert(body=body, media=media, parts="snippet")
        response = None
        while response is None:
            status, response = upload.next_chunk()
            if status:
                print(f"Upload {int(status.progress() * 100)} complete.")
        print(f"Response body: {response}")


if __name__ == "__main__":
    main()
