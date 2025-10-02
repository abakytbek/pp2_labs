# Write a function that takes a category and computes the average IMDB score.
from task import movies
def Ave_Cat(n, movies):
    sum = 0
    cnt = 0
    for movie in movies:
        if movie["category"] == n:
            cnt += 1
            sum += movie["imdb"]
    return (sum / cnt)

n = input()
print(Ave_Cat(n, movies))