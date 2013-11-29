class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
				

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
					
this_is_song = Song(["Fader Jakob, fader jakob",
					"Sover du? Sover du?",
					"Horer du min klokke?"])
					
Me_singing = Song(["Her er en sang jeg vil synge",
						"Den er kjempebra",
						"derfor kan vi nynne, trallaLALALA"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

this_is_song.sing_me_a_song()

Me_singing.sing_me_a_song()