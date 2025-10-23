name = input("enter file name: ")

with open(name) as f:
    lines = f.readlines()

print("lines:", len(lines))
