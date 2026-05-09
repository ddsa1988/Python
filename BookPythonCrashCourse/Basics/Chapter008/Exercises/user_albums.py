def make_album(artist_name: str, album_title: str, number_songs: int = 0):
    album = {}

    if (len(artist_name.strip()) <= 0 or len(album_title.strip()) <= 0):
        return album

    album["artist_name"] = artist_name.strip().title()
    album['album_title'] = album_title.strip().title()

    if (number_songs > 0):
        album["number_songs"] = number_songs

    return album


def main():
    albums = []
    is_active = True

    print("***** Make Albums *****\n")

    while (is_active):
        artist_name = ""
        album_title = ""
        number_songs = 0

        while (is_active):
            user_input = input("Type the artist name (or 'q' to quit): ")

            if (user_input.lower() == 'q'):
                is_active = False
                break

            if (len(user_input.strip()) == 0):
                print("Invalid artist name.")
                continue

            artist_name = user_input.title()
            break

        while (is_active):
            user_input = input("Type the album title (or 'q' to quit): ")

            if (user_input.lower() == 'q'):
                is_active = False
                break

            if (len(user_input.strip()) == 0):
                print("Invalid album title.")
                continue

            album_title = user_input.title()
            break

        while (is_active):
            user_input = input(
                "Type how many songs the album have (or 'q' to quit): ")

            if (user_input.lower() == 'q'):
                is_active = False
                break

            try:
                number_songs = int(user_input)

                if (number_songs <= 0):
                    raise ValueError("Invalid number.")

                break

            except ValueError as e:
                print(e)

        if (is_active):
            new_album = make_album(artist_name, album_title, number_songs)

            albums.append(new_album)

            print()
            continue

        if (len(albums) == 0):
            return

        print(f"\n{albums}")


if (__name__ == "__main__"):
    main()
