class Song:
    all=[]
    count=0
    artists=[]
    genres=[]
    genre_count={}
    artist_count = {}

    
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.add_song_to_count()
        Song.add_to_all(self)
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
            

    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count +=increment

    def add_to_all(self):
        Song.all.append(self)
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1       

ski=Song("Skii","Young Thug","trap")
skybox=Song("Skybox","Gunna","Pop")
drake=Song("Nonstop","Drake","Hip-hop")
print(Song.count)
Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
print(Song.count)

print(Song.artist_count)
