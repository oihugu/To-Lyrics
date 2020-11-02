from lyricsgenius import Genius
from project.model import *
from project.control import *
import json

class Video ():
    
    def __init__(self):
        with open('keys.json') as json_file:
            keys = json.load(json_file)
        self.genius = Genius(keys['Genius'])
        self.watson_url = keys['Watson']['url']
        self.watson_key = keys['Watson']['api']

    def user_input(self):    
        self.music = input('Type the music name: ')
        self.artist = input('Type the artist name: ')

    def searchLyrics(self):
        Lyrics = search.Lyrics(self.genius, self.music, self.artist)
        return Lyrics.getLyrics()

    def viewDict(self):
        print({'music': music}) 


if __name__ == '__main__':
    video = Video()
    video.user_input()
    lyrics = video.searchLyrics()
    mongo = mongo_interface.Management()
    mongo.export_lyrics(lyrics)