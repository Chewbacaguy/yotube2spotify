
"""
Step 1: Log into youtube
Step 2: Grab our liked vids
Step 3: create a new playlist
Step 4: Search for any song
Step 5: Add song into new spotify playlist
"""
import json
import requests
from secrets import spotify_user_id

class CreatePlaylist:

    def _init_(self):
        self.user.id = spotify_user_id
    
    

# Step 1: Log into youtube
def get_youtube_client(self):
    

# Step 2: Grab our liked vids
def get_liked_videos(self):


# Step 3: create a new playlist
def create_playlist(self):
    request_body = json.dump({

        "name": "Youtube Liked Vids",
        "description": "All liked Youtube Vids",
        "public": True
    })

    query = "".format(self.user_id)
    response = requests.post(
        query, 
        date = request_body, 
        header = {
            "Content-Type":"application/json",
            "Authorization":"Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()

    #playlist id
    return response_json["id"]
# Step 4: Search for any song
def get_spotify_uri(self, song_name, artist):
    query = "".format(
        song_name,
        artist
    )
    response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    songs = response_json["tracks"]["items"]

# Step 5: Add song into new spotify playlist
def add_song_to_playlist(self):
    pass


#Reaserch, need 3 apis, youtube data api, spotify data api, yourube_dl 