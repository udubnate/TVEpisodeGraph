from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get TV Show
tvshows = ia.search_movie('Parks and Recreation')

#get the first result
showid = tvshows[0].movieId