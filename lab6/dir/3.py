import os

p = input("enter path: ")

if os.path.exists(p):
    print(os.path.dirname(p))  # dir
    print(os.path.basename(p)) # file
else:
    print("no path")
