class Album:

    def __init__(self, name: str, songs):
        self.name = name
        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song):
    #def add_song(self, song: Song):

        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        # if song_name in map(lambda x: x.name, self.songs):
        #     pass
        if song_name not in [song.name for song in self.songs]:
            return f"Song is not in the album."

        if self.published:
            return f"Cannot remove songs. Album is published."

        song = [s for s in self.songs if s.name == song_name][0]
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

        # for each in self.songs:
        #     if each.name == song_name:
        #         self.songs.remove(each)
        #         return f"Removed song {song_name} from album {self.name}."
        #
        # return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for each_song in self.songs:
            result += f"== {each_song.get_info()}\n"
        return result
