import os

p = input("Enter path: ")

print(os.path.exists(p))   # exists
print(os.access(p, os.R_OK))  # readable
print(os.access(p, os.W_OK))  # writable
print(os.access(p, os.X_OK))  # executable
