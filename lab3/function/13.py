#Write a program able to play the "Guess the number" - game,
# where the number to be guessed is randomly chosen between 1 and 20.
# This is how it should work when run in a terminal:
import random

def Great():
    print("Hello! What is your name?")

def Great2(n):
    print(f"Well, {n}, I am thinking of a number between 1 and 20.")

def Play(m, name):
    win = False
    cnt = 0
    print("If you want to stop the game print \"stop\" without \"")
    while not win:
        print("Take a guess")
        n = input()
        cnt += 1
        if n == "stop":
            print("You lose")
            break
        elif int(n) == m:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        elif int(n) < m:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

Great()
name = input()
Great2(name)
number = random.randint(1, 20)
Play(number, name)