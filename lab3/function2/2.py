# Write a function that returns a sublist of movies with an IMDB score above 5.5.
from task import movies
def above(movies):
    new = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            new.append(movie)
    return new


sublist = above(movies)
for movie in sublist:
    print(movie)