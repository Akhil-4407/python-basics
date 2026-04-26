import ytmusicapi
class SongManager:
    def __init__(self,ID,songs,artists,yt):
        self.playlistID = ID
        self.songs = songs
        self.artists = artists
        self.yt = yt
        self.ids = []
    def search(self):
        for i,j in zip(self.songs,self.artists):
            search_query = f"{i} {j}"
            try:
                id = self.yt.search(query=search_query,filter="songs",limit=1)
                if id:
                    video_id = id[0]['videoId']
                    print(f"Found song {i} by {j}")
                    self.ids.append(video_id)
            except IndexError:
                print("No songs to search.")
            except:
                print(f"Could not find the song {i} by {j}")
    def add(self):
        if not self.ids:
            print("No songs to add!")
            return
        try:
            response = self.yt.add_playlist_items(self.playlistID, self.ids)
            print(f"Successfully added {len(self.ids)} songs to the playlist!")
            print(f"API Response: {response}")
        except:
            print("An Unexcepted error occured.")