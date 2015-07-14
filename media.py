class Movie():
    """A class that stores a movie's title, storyline, poster URL, trailer URL and year of release."""

    def __init__(self, movie_title, storyline, poster_url, trailer_url, year):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.year = year
