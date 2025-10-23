f = open(input("from: "), "r")
new = open(input("to: "), "w")

for line in f:
    new.write(line)

f.close()
new.close()
