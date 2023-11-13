import pyyoutube
from pyyoutube.media import Media


class YouTubeVideo:
    video = None
    media = None

    title = None
    description = None
    source_file_name = None
    thumbnail_file_name = None
    playlists = None
    recording_date = None

    privacy = "private"
    made_for_kids = False
    language = 'en-us'
    location = {
        "placeId": "ChIJOdqTINoMK4cRZ0jAwEveN6U",
        "description": "Unitarian Universalist Congregation of Phoenix"
    }
    category = "CREATOR_VIDEO_CATEGORY_GOVERNMENT"

    def __init__(self, title, description, source_file_name, recording_date):
        self.video = pyyoutube.Video(
            snippet=pyyoutube.VideoSnippet(title=title, description=description, defaultAudioLanguage=self.language,
                                           defaultLanguage=self.language,
                                           publishedAt=recording_date
                                           ), status=pyyoutube.VideoStatus(privacyStatus=self.privacy))
        self.media = Media(filename=source_file_name)
