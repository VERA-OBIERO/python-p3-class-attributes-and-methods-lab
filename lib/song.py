class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self,name,artist,genre):
        self.add_song_to_count()
        self.name = name
        self.artist = artist 
        self.genre = genre
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist)
    
    @classmethod 
    def add_to_genre_count(cls):
        cls.genre_count = {genre: cls.genres.count(genre) for genre in set(cls.genres)}

    @classmethod 
    def add_to_artist_count(cls):
        cls.artist_count = {artist: cls.artists.count(artist) for artist in set(cls.artists)}





