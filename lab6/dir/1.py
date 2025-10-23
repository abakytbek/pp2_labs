import os

path = input("enter path: ")

if os.path.exists(path):
    print("\nDirectories:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            print(i)

    print("\nFiles:")
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            print(i)

    print("\nAll:")
    for i in os.listdir(path):
        print(i)
else:
    print("no path")
