from numpy.core.fromnumeric import shape
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import seaborn as sns
import sys

credits = pd.read_csv('backend/tmdb_5000_credits.csv')
movies_incomplete = pd.read_csv("backend/tmdb_5000_movies.csv")

credits_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_dirty = movies_incomplete.merge(credits_renamed, on='id')
movies_clean = movies_dirty.drop(
    columns=['homepage', 'title_x', 'title_y', 'status', 'production_countries'])


tfv = TfidfVectorizer(min_df=5)

# Filling NaN with empty
movies_clean['overview'] = movies_clean['overview'].fillna('')

# Fitting the TF-IDF on overview of all movies
tfv_matrix = tfv.fit_transform(movies_clean['overview'])


# using linear kernel
ker = sigmoid_kernel(tfv_matrix, tfv_matrix)

#  mapping of indices and movie titles
indices = pd.Series(movies_clean.index,
                    index=movies_clean['original_title'])

title = sys.argv[1]
#title="Deadpool"
# Get index corresponding to original_title
idx = indices[title]

# Get the similarity scores
lin_scores = list(enumerate(ker[idx]))

# Sortmovies
lin_scores = sorted(lin_scores, key=lambda x: x[1], reverse=True)

# Scores of  10 most similar movies
lin_scores = lin_scores[1:7]
# Movie indices
movie_indices = [i[0] for i in lin_scores]

# Top 10 most similar movies
#print(movies_clean['original_title'].iloc[movie_indices])
x=movies_clean['original_title'].iloc[movie_indices]
res=[]
#print(shape(x))
for item in x:
    res.append(item)

print(res)
sys.stdout.flush()

# sys.modules[__name__]=give_rec
