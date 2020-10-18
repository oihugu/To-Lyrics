from lyricsgenius import Genius
from project import *
import json

class Video ():
    
    def __init__(self):
        with open('keys.json') as json_file:
            keys = json.load(json_file)
        self.genius = Genius(keys['Genius'])

    def user_input(self):    
        self.music = input('Type the music name: ')
        self.artist = input('Type the artist name: ')

    def searchLyrics(self):
        Lyrics = search.Lyrics(self.genius, self.music, self.artist)
        return Lyrics.getLyrics()

    def viewDict(self):
        print({'music': music}) 



video = Video()
video.user_input()
print(video.searchLyrics())