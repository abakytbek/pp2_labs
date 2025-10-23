items = ['apple', 'banana', 'cherry']
name = input("enter file name: ")

with open(name, 'w') as f:
    f.writelines('\n'.join(items))

print("list saved to", name)
