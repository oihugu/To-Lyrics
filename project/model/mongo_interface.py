import pymongo

class Management():

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://hugo:Jz6jJVjy2pUSxrG@tl.hchjw.mongodb.net/')
        self.db = self.client['db']
        self.lyrics =  self.db['lyrics']
    
    def export_lyrics(self, json):
        self.lyrics.insert(json)


