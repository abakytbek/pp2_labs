# Write a function that takes a category name and returns just those movies under that category.
from task import movies
def Categ(n, movies):
    for movie in movies:
        if movie["category"] == n:
            print(movie)

n = input()
Categ(n, movies)