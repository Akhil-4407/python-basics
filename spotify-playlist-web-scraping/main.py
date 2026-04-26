from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic
import random
from setup_auth import authenticate
from song_manager import SongManager
import os
if not os.path.exists("browser.json"):
    auth = authenticate()
    auth.get_json()

with open("file.txt","r") as file:
    dates = eval(file.read().split(" = ")[1])
date = random.choice(dates)
PLAYLIST_NAME = f"{date} Billboard 100"

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
response = requests.get(url=URL, headers=my_headers)
content = response.text

soup = BeautifulSoup(content,"html.parser")
songs_list = [song.getText().strip() for song in soup.find_all(name="h3", class_="chart-entry__title")]
song_artist = [artist.getText().strip() for artist in soup.find_all(name="span", class_="chart-entry__artist")]

yt = YTMusic("./browser.json")

playlist_id = None
playlists = yt.get_library_playlists(limit=100)
for playlist in playlists:
    if playlist["title"] == PLAYLIST_NAME:
        playlist_id = playlist["playlistId"]
        break
if playlist_id:
    print("This playlist already extists.")
else:
    playlist_id = yt.create_playlist(
        title=PLAYLIST_NAME,
        description="Created using python",
        privacy_status="PRIVATE",
    )
    print("Play list created successfully.")
    manager = SongManager(ID=playlist_id,songs=songs_list,artists=song_artist,yt=yt)
    print("Starting the search for Bill Board Hot 100...")
    manager.search()
    print("Starting to add songs...")
    manager.add()



