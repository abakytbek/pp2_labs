import os

p = input("enter path: ")

if os.path.exists(p):
    if os.access(p, os.W_OK):
        os.remove(p)
        print("file deleted")
    else:
        print("no permission")
else:
    print("file not found")
