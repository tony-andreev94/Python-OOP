# from defining_classes_lecture1.EXERCISE.spoopify_08.project.song import Song
# from defining_classes_lecture1.EXERCISE.spoopify_08.project.album import Album
class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
    #def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album.name} has been removed."
        return f"Album {album_name} is not found."



        # for each_album in self.albums:
        #     if each_album.name == album_name:
        #         if not each_album.published:
        #             self.albums.remove(each_album)
        #             return f"Album {each_album.name} has been removed."
        #         #else album is published
        #         return f"Album has been published. It cannot be removed."
        #
        # return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for each_album in self.albums:
            result += f"{each_album.details()}\n"
        return result



# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
