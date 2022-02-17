from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get TV Show
tvshows = ia.search_movie('Parks and Recreation')

#get the first result
showid = tvshows[0].movieID

# getting information
series = ia.get_movie(showid)

# adding new info set
ia.update(series, 'episodes')

# getting episodes of the series
episodes = series.data['episodes']

for i in episodes.keys():
    for j in episodes[i]:
        cur_ep = episodes[i][j]
        print(cur_ep['title'] + ' ' + str(cur_ep['rating']))

    print(i)

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
