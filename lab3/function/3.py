#Write a program to solve a classic puzzle: We count 35 heads and 94 legs 
#among the chickens and rabbits in a farm.
#How many rabbits and how many chickens do we have? 
#create function: solve(numheads, numlegs):

def solve(h, l):
    y = int((4 * h - l) / 2)
    x = int(h - y)
    print(f"Rabbits =", x , f"Chickens =", y)

h = int(input("NumHead = "))
l = int(input("NumLegs = "))
solve(h ,l)