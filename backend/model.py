from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import sys

# input both files
credits = pd.read_csv('backend/tmdb_5000_credits.csv')
movies = pd.read_csv("backend/tmdb_5000_movies.csv")

# merging both files
movies = movies.rename(index=str, columns={'id': 'movie_id'})
movies = movies.merge(credits, on='movie_id')

movies['overview'] = movies['overview'].fillna('')

# creating vectorizer
countvectorizer = CountVectorizer()
countvectorizer_matrix = countvectorizer.fit_transform(movies['overview'])

# creating kernel
kernel = linear_kernel(countvectorizer_matrix, countvectorizer_matrix)

indexes = pd.Series(movies.index, index=movies['original_title'])

title = sys.argv[1]
# title="Deadpool"

f = 0
idx = -1
for i in indexes.iteritems():
    if(i[0] == title):
        f = 1
        # print("found")
        idx = i[1]
        break
if f == 0:
    res = "Not Found"
    print(res)
    sys.stdout.flush()
    exit(0)

# Find similarity
similarity = list(enumerate(kernel[idx]))

# Sort by descnding to get top matches
similarity = sorted(similarity, key=lambda x: x[1], reverse=True)

similarity = similarity[0:6]
#movie_indexes = [i[0] for i in similarity]

movie_indexes = []
movie_scores = []
for row in similarity:
    movie_indexes.append(row[0])
    movie_scores.append(row[1])


# print(movies_clean['original_title'].iloc[movie_indexes])
x = movies['original_title'].iloc[movie_indexes]
res = []
# print(shape(x))
# for item in x:
#    res.append(item)

for i in range(len(x)):
    res.append(x.iloc[i]+":"+str(movie_scores[i]))
    # res.append(movie_scores[i])

print(res)
sys.stdout.flush()

# sys.modules[__name__]=give_rec
