#Step 1: Log into youtube
#Step 2: Grab liked videos
#Step 4: Search for song
#Step 5: Add this song to spotify playlist

import json
class CreatePlaylist:

    def _init_(self):
        pass

    #Step 1: Log into youtube

    def get_youtube_client(self):
        pass

    #Step 2: Grab like videos

    def get_liked_videos(self):
        pass         

    #Step 3: Create playlist

    def create_playlist(self):
        request_body = json.dumps({ "name": "New Playlist",
        "description": "New playlist description",
         "public": True

        })

        query = "https://api.spotify.com/v1.users/{}/playlists".format

    #Step 4: Search for song

    def get_spotify_url(self):
        pass

    #Step 5: Add song to playlist

    def add_song_to_playlist(self):
        pass
