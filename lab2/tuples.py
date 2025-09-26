#Create
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allow dublicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male") 
#('abc', 34, True, 40, 'male')

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#<class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#('apple', 'banana', 'cherry')
