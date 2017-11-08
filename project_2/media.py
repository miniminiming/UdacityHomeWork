'''
 movies info class
'''


class Movie():
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        '''
         init movie info
         :param title  movie's tittle
         :param poster_image_url movie's preview photo url
         :param trailer_youtube_url movie's preview video url
        '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
