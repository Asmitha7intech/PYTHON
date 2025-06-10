def resize(playlist, capacity):
    """Resize the playlist array when the capacity is reached."""
    return playlist[:capacity]

def add_song(playlist, song):
    """Add a new song to the playlist."""
    playlist.append(song)
    if len(playlist) == len(playlist) + 1:  # Check if resizing is needed
        playlist = resize(playlist, len(playlist) * 2)
    return playlist

def remove_song(playlist, index):
    """Remove a song from the playlist by its index."""
    if index < 0 or index >= len(playlist):
        print("Index out of bounds!")
    else:
        del playlist[index]
    return playlist

def get_song(playlist, index):
    """Retrieve a song by its index."""
    if index < 0 or index >= len(playlist):
        print("Index out of bounds!")
    else:
        print(f"Song at index {index}: {playlist[index]}")

def playlist_size(playlist):
    """Return the current number of songs in the playlist."""
    return len(playlist)

def main():
    playlist = []  # Initialize the playlist as an empty list
    while True:
        print("\nChoose an action:")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Get Song")
        print("4. Show Playlist Size")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            song = input("Enter the song name: ")
            playlist = add_song(playlist, song)
            print(f"'{song}' added to the playlist.")

        elif choice == "2":
            index = int(input("Enter the index of the song to remove: "))
            playlist = remove_song(playlist, index)
            print(f"Song at index {index} removed.")

        elif choice == "3":
            index = int(input("Enter the index of the song to retrieve: "))
            get_song(playlist, index)

        elif choice == "4":
            print(f"Playlist size: {playlist_size(playlist)}")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please choose between 1-5.")

if __name__ == "__main__":
    main()

