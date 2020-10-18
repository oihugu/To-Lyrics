class Lyrics():

    def __init__(self, genius, music, artist):
        artist = genius.search_artist(artist, max_songs = 0)
        self.song = genius.search_song(music, artist.name)
        genius.remove_section_headers = True
        genius.verbose = True
        genius.skip_non_songs = True

    def getLyrics(self):
        lyric_list = [line for line in self.song.lyrics.split('\n')]
        
        lyric_dict = {
            'number_of_lines' : (len(lyric_list) + 1)
            }
        
        for line_number in range(len(lyric_list)):
            lyric_dict[f'line_{line_number + 1}'] = {
                'text' : lyric_list[line_number], #content of this line of the lyrics
                'keywords' : [],
                'background_images' : [], #list of urls
                'backgorund_color' :  '',  #hexacode
                'text_color' : '',  #hexacode
                'text_size' : 0, #px
                'is_script' : True if (('[' in lyric_list[line_number]) and (']' in lyric_list[line_number])) else False #indicates if the line is an instruction to the singers
            }
        
        return lyric_dict