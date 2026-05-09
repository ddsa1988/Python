def make_album(artist_name: str, album_title: str, number_songs: int = 0):
    album = {}

    if (len(artist_name.strip()) <= 0 or len(album_title.strip()) <= 0):
        return album

    album["artist_name"] = artist_name.strip().title()
    album['album_title'] = album_title.strip().title()

    if (number_songs > 0):
        album["number_songs"] = number_songs

    return album


print(make_album("metallica", "kill them all"))

print()

print(make_album("iron maiden", "killers"))

print(make_album("acdc", "back in black", 8))
