import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('/content/movies.csv')
df.head()
df.info()
df.isnull().sum()
df.shape
vectorizer = TfidfVectorizer()
vectorizer_features = vectorizer.fit_transform(combined_features)
print(vectorizer_features)
similarity  = cosine_similarity(vectorizer_features)
list_all_movie = df['title'].tolist()
print(list_all_movie)
movie_name = input('Enter your favourite movie name : ')
find_close_movie  = difflib.get_close_matches(movie_name,list_all_movie)
print(find_close_movie)
close_match = find_close_movie[0]
print(close_match)
index_movie = df[df.title == close_match]['index'].values[0]
print(index_movie)
similarity_score = list(enumerate(similarity[index_movie]))
max_similarity_score = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print(max_similarity_score)
print('Movies suggested for you : \n')
i = 1
for movie in max_similarity_score:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<10):
    print(i, '.',title_from_index)
    i+=1
print( title_from_index)
#Movie Recommendation System
movie_name = input('Enter your favourite movie name : ')
list_all_movie = df['title'].tolist()
close_match = difflib.get_close_matches(movie_name, list_all_movie)
close_match[0]
index_movie = df[df.title == close_match[0]]['index'].values[0]
similarity_score = list(enumerate(similarity[index_movie]))
max_similarity_score = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print('Movies suggested for you : \n')
i = 1
for movie in max_similarity_score:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<10):
    print(i, '.',title_from_index)
    i+=1
