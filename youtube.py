import dotenv
import json
import os
import pyyoutube
import typing


from model.YouTubeVideo import YouTubeVideo

SECRET_CONFIG = 'SECRET_CONFIG'
REFRESH_TOKEN = 'REFRESH_TOKEN'

scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/userinfo.profile", ]

client: typing.Optional[pyyoutube.Client] = None


def load_local_credentials():
    """
    Attempt to load YouTube credentials from the file system.
    :return: Refresh token, Secret config file path
    """
    dotenv.load_dotenv()
    return os.getenv(REFRESH_TOKEN), os.getenv(SECRET_CONFIG)


def initialize_client():
    """
    Initialize the client (if not initialized already)
    :return:
    """
    client_id, client_secret, refresh_token = load_config()
    global client
    if not client:
        client = pyyoutube.Client(client_id=client_id, client_secret=client_secret)

        if refresh_token is None:
            generate_refresh_token()
        else:
            client.access_token = client.refresh_access_token(refresh_token).access_token


def load_config():
    """ Load the configuration.
    :return: client_id, client_secret, refresh_token
    """
    refresh_token, secret_config = load_local_credentials()
    with (open(secret_config) as raw_secret_config):
        secret_config = json.loads(raw_secret_config.read())
        client_id = secret_config.get("installed").get("client_id")
        client_secret = secret_config.get("installed").get("client_secret")
        return client_id, client_secret, refresh_token


def generate_refresh_token():
    """
    With the user's help, generate a refresh token. Then print it to the console.
    """
    initialize_client()
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


def create_upload_request(title, description, recording_date, source_file_name):
    """
    Create an upload request.
    :return: an upload request
    """
    initialize_client()
    video = YouTubeVideo(title=title, description=description, recording_date=recording_date,
                         source_file_name=source_file_name)
    return client.videos.insert(body=video.video, media=video.media, parts="snippet,status")


def upload_video(title, description, recording_date, source_file_name):
    """Upload the video and print the status."""
    upload = create_upload_request(title, description, recording_date, source_file_name)
    response = None
    while response is None:
        status, response = upload.next_chunk()
        if status:
            print(f"Upload {int(status.progress() * 100)} complete.")
    print(f"Response body: {response}")
