import numpy as np
import pandas as pd
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('backend/ml-100k/u.data', sep='\t', names=r_cols,
                      usecols=range(3), encoding="ISO-8859-1")
m_cols = ['movie_id', 'title']
movies = pd.read_csv('backend/ml-100k/u.item', sep='|', names=m_cols,
                     usecols=range(2), encoding="ISO-8859-1")
ratings = pd.merge(movies, ratings)
movieRatings = ratings.pivot_table(index=['user_id'], columns=[
                                   'title'], values='rating')
z='Star Wars (1977)'
#z=str(sys.argv[1])
starWarsRatings=movieRatings[z]
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
similarMovies.sort_values(ascending=False)
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
# Ignore movies rated by less than 100 people
popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values(
    [('rating', 'mean')], ascending=False)[:15]
df = movieStats[popularMovies].join(
    pd.DataFrame(similarMovies, columns=['similarity']))
res=df.sort_values(['similarity'], ascending=False)[:5]
import sys
x=[]
for row in res.iterrows():
    x.append(row[0])

print(x)
sys.stdout.flush()