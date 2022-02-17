# importing the module
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# adding new info set
ia.update(series, 'episodes')

# getting episodes of the series
episodes = series.data['episodes']

# printing the object i.e name
print(series)

print("=========")

# getting season
season = episodes[1]

# getting single episode of season
epi = season[1]

# getting id and printing it
get_id = epi.getID

print(get_id)
