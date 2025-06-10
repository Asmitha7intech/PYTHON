class DynamicArray:
    def __init__(self):
        # Start with an initial capacity of 2
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity  # Initialize the dynamic array

    # Add Song: Add a new song to the end of the playlist
    def add_song(self, song):
        if self.size == self.capacity:  # Resize the array if it's full
            self.resize(self.capacity * 2)
        self.array[self.size] = song
        self.size += 1

    # Remove Song: Remove a song from the playlist by its index
    def remove_song(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index.")
            return
        
        # Shift all elements to the left after the removed song
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        # Set the last element to None
        self.array[self.size - 1] = None
        self.size -= 1

        # Resize the array if the size is too small (less than a quarter of capacity)
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

    # Get Song: Retrieve a song based on its index
    def get_song(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index.")
            return None
        return self.array[index]

    # Size: Get the current number of songs in the playlist
    def get_size(self):
        return self.size

    # Resize: Automatically adjust the array size
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

# Function to interact with the user and manage the playlist
def manage_playlist():
    playlist = DynamicArray()

    while True:
        print("\n--- Playlist Menu ---")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Get Song")
        print("4. Display Playlist Size")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            song = input("Enter the song name to add: ")
            playlist.add_song(song)
            print(f"Song '{song}' added to the playlist.")

        elif choice == '2':
            index = int(input("Enter the index of the song to remove: "))
            playlist.remove_song(index)
            print(f"Song at index {index} removed from the playlist.")

        elif choice == '3':
            index = int(input("Enter the index of the song to retrieve: "))
            song = playlist.get_song(index)
            if song:
                print(f"Song at index {index}: {song}")
            else:
                print("Invalid index.")

        elif choice == '4':
            print(f"Current playlist size: {playlist.get_size()}")

        elif choice == '5':
            print("Exiting the playlist manager.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the playlist manager
manage_playlist()
