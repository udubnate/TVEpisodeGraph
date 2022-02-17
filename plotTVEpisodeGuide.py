from imdb import Cinemagoer
import pandas as pd
import plotly.express as px
import sys

tv_show = "the boys"
## backend rendering engine is plotly for pandas
pd.options.plotting.backend = "plotly"

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get TV Show
tvshows = ia.search_movie(tv_show)

#get the first result
showid = tvshows[0].movieID

# getting information
series = ia.get_movie(showid)

# adding new info set
try:
    # getting episodes of the series
    ia.update(series, 'episodes')
    episodes = series.data['episodes']
except:
    print("This show doesn't have any episodes. Canceling Request")
    sys.exit()

lst = []

for i in episodes.keys():
    for j in episodes[i]:
        cur_ep = episodes[i][j]
        obj = []
        obj.append(cur_ep['title'])
        
        # if rating doesn't exist, fill with zero
        if 'rating' in cur_ep:
            obj.append(cur_ep['rating'])
        else:
            obj.append(0)
        
        lst.append(obj)

    print(i)

df = pd.DataFrame(lst, columns =['title', 'rating'])
print(df )
fig = px.bar(df, x='title', y='rating')
fig.show()