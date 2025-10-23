text = input("enter a string: ")

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())

print("number of uppercase letters:", upper)
print("number of lowercase letters:", lower)
