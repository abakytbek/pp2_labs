# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
from task import movies
def above(movie):
    if movie["imdb"] > 5.5:
        return True

for i in movies:
    if above(i):
        print(i["name"])