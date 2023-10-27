import json
import os
from ffmpeg import FFmpeg
from model.Config import Config
from pyyoutube import Client, AccessToken


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
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    with (open(config.secret_config) as raw_secret_config):
        secret_config = json.loads(raw_secret_config.read())
        client_id = secret_config.get("installed").get("client_id")
        client_secret = secret_config.get("installed").get("client_secret")

        client = Client(client_id=client_id, client_secret=client_secret)
        auth_url_response = client.get_authorize_url(scope=scopes)

        if config.refresh_token is None:
            # Debug and inspect this response to get the refresh token
            # Visit the [url,] from auth_url_response, sign in, and get the "code" query param from the response
            # Run again to get the access_token_response and add the refresh token to environment (e.g. via .env.local)
            access_token_response = client.generate_access_token(
                code="Follow Steps Above to Generate This",
                scope=scopes, return_json=True)
        else:
            access_token_response = client.refresh_access_token(config.refresh_token)
        AccessToken(access_token=access_token_response.access_token, expires_in=access_token_response.expires_in,
                    token_type=access_token_response.token_type)
        print(access_token_response)
        print(auth_url_response)


if __name__ == "__main__":
    main()
