# Write a function that computes the volume of a sphere given its radius.
def Volume_Of_Sphere(r):
    v = (4 / 3) * 3.14159265359 * (r ** 3)
    return v

n = float(input("R = "))
print(Volume_Of_Sphere(n))