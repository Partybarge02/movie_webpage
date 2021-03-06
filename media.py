#!/usr/bin/env python
# This file defines the class Movie. 

import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #Define  a class varible-constant

    def __init__(self, movie_title, movie_storyline, poster_image, 
                trailer_youtube,VALID_RATINGS):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = VALID_RATINGS

    #open a webbrowser and play movie trailer   
    def show_trailer(self):#instance method
        webbrowser.open(self.trailer_youtube_url)

