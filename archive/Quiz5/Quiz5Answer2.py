# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def loadSongs(songArtist):
    song_dictionary = {}
    for line in open(songArtist):
        item = line.split(":")
        song_dictionary[item[1].strip('\n ')] = [(item[0])]
    return song_dictionary

print(loadSongs('songs.txt'))



