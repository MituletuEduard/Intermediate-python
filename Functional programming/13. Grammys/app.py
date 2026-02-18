from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55),
            ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]


# Check if the duration of the song is longer than 5 minutes
def longer_than_five_minutes(song):
    return song[1] > 5.00


def minutes_to_seconds(song):  # Convert the duration from minutes to seconds
    minutes = int(song[1])
    seconds = round((song[1] - minutes) * 100)
    return minutes * 60 + seconds


def add_durations(duration1, duration2):  # Add two durations together
    return duration1 + duration2


filtered_songs = list(filter(longer_than_five_minutes, playlist))
print(f"Melodii lungi: {filtered_songs}")

durations = list(map(minutes_to_seconds, playlist))
print(f"Durate în secunde: {durations}")

total_playtime = reduce(add_durations, durations, 0)
print(f"Timp total de redare (secunde): {total_playtime}")

"""
Docstring for Intermediate python.Functional programming.13. Grammys.app

For many, music is so personal. We have created a playlist of songs that have won the “Song of the Year” 🏆 Grammy award in the past 5 years.

Let's play around with the data!

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

Lastly, add up the total playtime of the playlist with reduce().

Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

A longer_than_five_minutes() function for filter().
A minutes_to_seconds() function for map().
An add_durations() function for reduce().
"""
