def Square(n):
    start = 1
    while start <= n:
        yield start ** 2
        start += 1

for sq in Square(5):
    print(sq, end=" ")