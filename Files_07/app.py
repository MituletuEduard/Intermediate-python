liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost123": "Justin Bieber"
}


def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs:\n")
        for items in liked_songs.items():
            file.write(f"{items[0]} by {items[1]}\n")


write_liked_songs_to_file(
    liked_songs, "test.txt")
