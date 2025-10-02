# Write a function that takes a list of movies and computes the average IMDB score.
from task import movies
def Ave(movies):
    sum = 0
    cnt = 0
    for movie in movies:
        sum += movie["imdb"]
        cnt += 1
    return (sum / cnt)

print(Ave(movies))